# (c) Copyright 2025 Hewlett Packard Enterprise Development LP
"""OAuth2 client credentials provider for audit-logs API authentication."""

import time

import httpx
from loguru import logger
from pydantic import BaseModel, Field


class OAuth2TokenResponse(BaseModel):
    """OAuth2 token response model."""

    access_token: str = Field(description="The access token")
    token_type: str = Field(default="Bearer", description="Token type")
    expires_in: int | None = Field(default=None, description="Token lifetime in seconds")
    scope: str | None = Field(default=None, description="Token scope")
    issued_at: float = Field(default_factory=time.time, description="Timestamp when token was issued")

    @property
    def expires_at(self) -> float | None:
        """Calculate expiration timestamp."""
        if self.expires_in is None:
            return None
        return self.issued_at + self.expires_in

    def expires_at_timestamp(self) -> float | None:
        """Get expiration timestamp (alias for expires_at property)."""
        return self.expires_at


class OAuth2Provider:
    """OAuth2 client credentials provider for audit-logs API."""

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        token_url: str,
        workspace_id: str | None = None,
    ):
        """Initialize the OAuth2 provider.

        Args:
            client_id: OAuth2 client ID
            client_secret: OAuth2 client secret
            token_url: OAuth2 token endpoint URL
            workspace_id: Optional workspace ID for scoped access
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.token_url = token_url
        self.workspace_id = workspace_id

        logger.info(
            "OAuth2 provider initialized",
            client_id=client_id,
            token_url=token_url,
            workspace_id=workspace_id,
        )

    def get_token(self) -> OAuth2TokenResponse:
        """Get an access token using client credentials flow.

        Returns:
            OAuth2 token response with access token and metadata

        Raises:
            httpx.HTTPStatusError: If token request fails with HTTP error status
            httpx.RequestError: If network/connection error occurs
        """
        try:
            logger.info("Requesting access token", token_url=self.token_url)

            # Make token request using httpx instead of requests-oauthlib
            # This avoids the issue with requests-oauthlib's OAuth2 implementation
            with httpx.Client(timeout=30.0) as client:
                response = client.post(
                    self.token_url,
                    headers={"Content-Type": "application/x-www-form-urlencoded"},
                    data={
                        "grant_type": "client_credentials",
                        "client_id": self.client_id,
                        "client_secret": self.client_secret,
                    },
                )

                # Check for exact 200 status - reject all other codes including other 2xx
                if response.status_code != 200:
                    error_msg = f"HTTP {response.status_code}: {response.text}"
                    logger.error(
                        "Token request failed",
                        status_code=response.status_code,
                        error=error_msg,
                        expected_status=200,
                    )

                    # Raise for 4xx/5xx errors
                    if response.status_code >= 400:
                        response.raise_for_status()
                    else:
                        # Raise custom error for unexpected 2xx/3xx codes
                        raise httpx.HTTPStatusError(
                            f"Unexpected status code {response.status_code}, expected 200",
                            request=response.request,
                            response=response,
                        )

                token_data = response.json()

            # Create structured response
            # Handle scope - convert list to string if needed
            scope = token_data.get("scope")
            if isinstance(scope, list):
                scope = " ".join(scope) if scope else None

            oauth_token = OAuth2TokenResponse(
                access_token=token_data["access_token"],
                token_type=token_data.get("token_type", "Bearer"),
                expires_in=token_data.get("expires_in"),
                scope=scope,
            )

            logger.info(
                "Access token acquired successfully",
                token_type=oauth_token.token_type,
                expires_in=oauth_token.expires_in,
                scope=oauth_token.scope,
            )

            return oauth_token

        except Exception as e:
            logger.error("Failed to acquire access token", error=str(e), token_url=self.token_url)
            raise

    def validate_token(self, token: str) -> bool:
        """Validate an access token.

        Args:
            token: Access token to validate

        Returns:
            True if token is valid, False otherwise
        """
        try:
            # For now, we'll assume tokens are valid if they exist
            # In a real implementation, you might want to make a test API call
            # or use token introspection if supported by the OAuth2 server
            return bool(token and len(token.strip()) > 0)

        except Exception as e:
            logger.error("Token validation failed", error=str(e))
            return False
