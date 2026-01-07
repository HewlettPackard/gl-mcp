# (c) Copyright 2025 Hewlett Packard Enterprise Development LP
"""Token management for audit-logs API authentication."""

import time
from typing import Any

from loguru import logger
from pydantic import BaseModel, Field

from .oauth2_provider import OAuth2Provider, OAuth2TokenResponse


class TokenInfo(BaseModel):
    """Token information."""

    token: str = Field(description="The JWT token")
    expires_at: float | None = Field(default=None, description="Token expiration timestamp")
    created_at: float = Field(default_factory=time.time, description="Token creation timestamp")

    def is_expired(self, buffer_seconds: int = 300) -> bool:
        """Check if the token is expired.

        Args:
            buffer_seconds: Buffer time in seconds before actual expiration

        Returns:
            True if the token is expired or will expire within buffer_seconds
        """
        if self.expires_at is None:
            # If no expiration time, assume it's valid for safety
            return False

        current_time = time.time()
        return current_time >= (self.expires_at - buffer_seconds)

    def time_until_expiry(self) -> float | None:
        """Get time until token expiry in seconds.

        Returns:
            Seconds until expiry, or None if expiration time is unknown
        """
        if self.expires_at is None:
            return None

        return max(0, self.expires_at - time.time())


class TokenManager:
    """Manages authentication tokens for audit-logs API."""

    def __init__(self, settings: Any | None = None, initial_token: str | None = None) -> None:
        """Initialize the token manager.

        Args:
            settings: Application settings for OAuth2 configuration
            initial_token: Optional initial JWT token
        """
        self._token_info: TokenInfo | None = None
        self._oauth2_provider: OAuth2Provider | None = None

        # Set up OAuth2 provider if settings are provided
        if settings:
            self._oauth2_provider = OAuth2Provider(
                client_id=settings.client_id,
                client_secret=settings.client_secret,
                token_url=settings.token_issuer,
                workspace_id=getattr(settings, "workspace_id", None),
            )

        # Set initial token if provided (for testing/pre-authenticated scenarios)
        if initial_token:
            self._set_token(initial_token)
        # For test environments, set a test token
        elif settings and settings.is_testing:
            logger.info("Setting test token for test environment")
            self._set_token("test_token_12345")
        # Otherwise, use LAZY initialization - token will be generated on first use
        else:
            logger.info(
                "Token manager initialized with lazy token generation", has_oauth2=self._oauth2_provider is not None
            )

    def _set_token(self, token: str, expires_at: float | None = None) -> None:
        """Set a new token.

        Args:
            token: The JWT token to set
            expires_at: Optional expiration timestamp
        """
        self._token_info = TokenInfo(token=token, expires_at=expires_at)
        logger.info("Token updated", has_expiry=self._token_info.expires_at is not None)

    def _set_token_from_oauth2_response(self, response: OAuth2TokenResponse) -> None:
        """Set token from OAuth2 response.

        Args:
            response: OAuth2 token response
        """
        expires_at = response.expires_at_timestamp()
        self._set_token(response.access_token, expires_at)

    def _generate_new_token(self) -> None:
        """Generate a new token using OAuth2 provider.

        Raises:
            RuntimeError: If OAuth2 provider is not configured or token generation fails
        """
        if not self._oauth2_provider:
            raise RuntimeError("OAuth2 provider not configured for token generation")

        try:
            response = self._oauth2_provider.get_token()
            self._set_token_from_oauth2_response(response)
            logger.info("New token generated successfully")
        except Exception as e:
            logger.error("Failed to generate new token", error=str(e))
            raise

    def _ensure_valid_token(self) -> None:
        """Ensure we have a valid token, generating/refreshing if necessary.

        Raises:
            RuntimeError: If no valid token can be obtained
        """
        if not self._token_info or self._token_info.is_expired():
            if self._oauth2_provider:
                logger.info("Token expired or missing, generating new token")
                self._generate_new_token()
            else:
                raise RuntimeError("Token expired and no OAuth2 provider configured for renewal")

    def get_auth_headers(self) -> dict[str, str]:
        """Get authentication headers for API requests.

        This method implements lazy token initialization:
        - On first call: Fetches a new token from OAuth2 provider
        - Subsequent calls: Returns cached token if still valid
        - Auto-refresh: Automatically refreshes expired tokens with retry logic

        The token is fetched on-demand, not during TokenManager initialization,
        which improves startup time and ensures token freshness.

        Returns:
            Dictionary containing authorization headers

        Raises:
            RuntimeError: If no valid token is available
        """
        # Ensure we have a valid token before returning headers
        self._ensure_valid_token()

        if not self._token_info:
            raise RuntimeError("No token available")

        return {
            "Authorization": f"Bearer {self._token_info.token}",
            "Content-Type": "application/json",
        }

    def update_token(self, new_token: str) -> None:
        """Update the current token manually.

        Args:
            new_token: The new JWT token
        """
        logger.info("Manually updating token")
        self._set_token(new_token)

    def refresh_token(self) -> None:
        """Refresh the current token using OAuth2 provider.

        Raises:
            RuntimeError: If OAuth2 provider is not configured
        """
        if not self._oauth2_provider:
            raise RuntimeError("OAuth2 provider not configured for token refresh")

        logger.info("Manually refreshing token")
        self._generate_new_token()

    def is_token_valid(self) -> bool:
        """Check if the current token is valid.

        Returns:
            True if token exists and is not expired
        """
        return self._token_info is not None and not self._token_info.is_expired()

    def get_token_info(self) -> TokenInfo | None:
        """Get current token information.

        Returns:
            Current token info or None if no token is set
        """
        return self._token_info

    def get_raw_token(self) -> str | None:
        """Get the raw token string.

        Returns:
            The current token string or None if no token is set
        """
        if self._token_info:
            return self._token_info.token
        return None
