# (c) Copyright 2025 Hewlett Packard Enterprise Development LP
"""OAuth2 client credentials provider for subscriptions API authentication."""

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
    """OAuth2 client credentials provider for subscriptions API."""

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        token_url: str,
        workspace_id: str | None = None,
        max_retries: int = 5,
        initial_backoff: float = 1.0,
        max_backoff: float = 60.0,
    ):
        """Initialize the OAuth2 provider.

        Args:
            client_id: OAuth2 client ID
            client_secret: OAuth2 client secret
            token_url: OAuth2 token endpoint URL
            workspace_id: Optional workspace ID for scoped access
            max_retries: Maximum number of retry attempts for 429 errors (default: 5)
            initial_backoff: Initial backoff delay in seconds (default: 1.0)
            max_backoff: Maximum backoff delay in seconds (default: 60.0)
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.token_url = token_url
        self.workspace_id = workspace_id
        self.max_retries = max_retries
        self.initial_backoff = initial_backoff
        self.max_backoff = max_backoff

        logger.info(
            "OAuth2 provider initialized",
            client_id=client_id,
            token_url=token_url,
            workspace_id=workspace_id,
            max_retries=max_retries,
        )

    def _make_token_request(self) -> dict:
        """Make the actual HTTP request for token.

        Returns:
            Response JSON data

        Raises:
            httpx.HTTPStatusError: For all HTTP errors including 429
        """
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

            # Raise exception for any non-2xx status code
            response.raise_for_status()

            return response.json()

    def get_token(self) -> OAuth2TokenResponse:
        """Get an access token using client credentials flow with exponential backoff for rate limits.

        Implements exponential backoff retry logic for 429 (Too Many Requests) responses.
        Other errors are raised immediately without retry.

        Returns:
            OAuth2 token response with access token and metadata

        Raises:
            httpx.HTTPStatusError: If token request fails with HTTP error status (after retries for 429)
            httpx.RequestError: If network/connection error occurs
        """
        for attempt in range(self.max_retries + 1):
            try:
                # Apply backoff delay before retry attempts
                if attempt > 0:
                    backoff_delay = min(self.initial_backoff * (2 ** (attempt - 1)), self.max_backoff)
                    logger.warning(
                        "Retrying token request after rate limit",
                        attempt=attempt + 1,
                        backoff_seconds=backoff_delay,
                    )
                    time.sleep(backoff_delay)

                logger.info(
                    "Requesting access token",
                    attempt=attempt + 1,
                    max_attempts=self.max_retries + 1,
                )

                # Make the token request
                token_data = self._make_token_request()

                # Parse and return successful response
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
                    expires_in=oauth_token.expires_in,
                    attempts=attempt + 1,
                )

                return oauth_token

            except httpx.HTTPStatusError as e:
                # Retry only on 429, raise immediately for other errors
                if e.response.status_code == 429 and attempt < self.max_retries:
                    logger.warning(
                        "Rate limit hit, will retry",
                        status_code=429,
                        remaining_attempts=self.max_retries - attempt,
                    )
                    continue

                # Last retry or non-429 error - raise it
                logger.error(
                    "Token request failed",
                    status_code=e.response.status_code,
                    attempts=attempt + 1,
                )
                raise

        # This line should never be reached, but satisfy type checker
        raise httpx.HTTPStatusError(
            "Failed to acquire token after exhausting all retries",
            request=None,  # type: ignore
            response=None,  # type: ignore
        )

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
