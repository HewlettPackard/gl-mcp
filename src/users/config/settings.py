# (c) Copyright 2025 Hewlett Packard Enterprise Development LP
"""
Settings configuration for users MCP server.

This module handles environment variable configuration and application settings.
"""

from pydantic import AliasChoices, Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings from environment variables."""

    # GreenLake API Configuration
    greenlake_api_base_url: str = Field(
        default="https://global.api.greenlake.hpe.com",
        description="Base URL for HPE GreenLake APIs",
        alias="GREENLAKE_API_BASE_URL",
    )

    # Authentication Configuration
    greenlake_client_id: str = Field(
        description="OAuth2 client ID for GreenLake authentication",
        alias="GREENLAKE_CLIENT_ID",
    )

    greenlake_client_secret: str = Field(
        description="OAuth2 client secret for GreenLake authentication",
        alias="GREENLAKE_CLIENT_SECRET",
    )

    greenlake_workspace_id: str = Field(description="GreenLake workspace identifier", alias="GREENLAKE_WORKSPACE_ID")

    # Application Configuration
    log_level: str = Field(default="INFO", description="Logging level", alias="LOG_LEVEL")

    # HTTP Client Configuration
    http_timeout: int = Field(default=30, description="HTTP request timeout in seconds", alias="HTTP_TIMEOUT")

    http_retries: int = Field(default=3, description="HTTP request retry attempts", alias="HTTP_RETRIES")

    # MCP Tool Configuration
    mcp_tool_mode: str = Field(
        default="static",
        description="MCP tool mode: 'static' for individual endpoint tools, 'dynamic' for meta-tools",
        alias="MCP_TOOL_MODE",
    )

    # Testing Configuration
    is_testing: bool = Field(
        default=False,
        description="Whether the application is in testing mode",
        validation_alias=AliasChoices("TESTING", "PYTEST_CURRENT_TEST"),
    )

    @field_validator("mcp_tool_mode")
    @classmethod
    def validate_tool_mode(cls, v: str) -> str:
        """Validate that tool mode is either 'static' or 'dynamic'."""
        v_lower = v.lower()
        if v_lower not in ["static", "dynamic"]:
            raise ValueError(f"Invalid tool mode: {v}. Must be 'static' or 'dynamic'")
        return v_lower

    @field_validator("is_testing", mode="before")
    @classmethod
    def validate_testing(cls, v) -> bool:
        """Convert testing flags to boolean (handles PYTEST_CURRENT_TEST strings)."""
        if isinstance(v, bool):
            return v
        # PYTEST_CURRENT_TEST is set to a non-empty string when pytest runs
        # TESTING can be "true", "1", "yes", "on", etc.
        if isinstance(v, str):
            # Any non-empty string from PYTEST_CURRENT_TEST means we're testing
            if v and v.lower() not in ("false", "0", "no", "off"):
                return True
        return bool(v)

    @property
    def token_issuer_url(self) -> str:
        """Get the OAuth2 token issuer URL."""
        return f"{self.greenlake_api_base_url}/authorization/v2/oauth2/{self.greenlake_workspace_id}/token"

    # Compatibility properties for shared auth components
    @property
    def client_id(self) -> str:
        """Get client ID (compatibility with shared auth)."""
        return self.greenlake_client_id

    @property
    def client_secret(self) -> str:
        """Get client secret (compatibility with shared auth)."""
        return self.greenlake_client_secret

    @property
    def workspace_id(self) -> str:
        """Get workspace ID (compatibility with shared auth)."""
        return self.greenlake_workspace_id

    @property
    def token_issuer(self) -> str:
        """Get token issuer URL (compatibility with shared auth)."""
        return self.token_issuer_url

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", case_sensitive=False, extra="ignore")

    # SERVICE-SPECIFIC PROPERTIES
    @property
    def service_api_url(self) -> str:
        """Get the full URL for the service API."""
        return self.greenlake_api_base_url


# Global settings instance - lazy initialization to avoid test failures
_settings = None


def get_settings() -> Settings:
    """Get the global settings instance."""
    global _settings
    if _settings is None:
        _settings = Settings()  # type: ignore[call-arg]
    return _settings


# Backward compatibility - expose as settings
# This uses lazy initialization to avoid test failures
class SettingsProxy:
    def __getattr__(self, name):
        return getattr(get_settings(), name)


settings = SettingsProxy()
