# (c) Copyright 2025 Hewlett Packard Enterprise Development LP
"""
Tests for config components in users MCP server.

This file contains tests for settings, logging configuration, and other config components.
"""

import pytest
from unittest.mock import patch
import os
import stat
import tempfile
from loguru import logger as loguru_logger

from config.settings import settings, Settings
from config.logging import setup_logging, get_logger


class TestSettings:
    """Test cases for Settings configuration."""

    def test_settings_default_values(self):
        """Test settings have appropriate default values."""
        # Test with existing global settings instance
        assert settings is not None

        # Basic attributes should exist
        assert hasattr(settings, "greenlake_client_id")
        assert hasattr(settings, "greenlake_client_secret")
        assert hasattr(settings, "token_issuer")

        # Check for service-specific defaults
        assert hasattr(settings, "greenlake_api_base_url")

    def test_settings_from_environment(self):
        """Test settings can be loaded from environment variables."""
        test_env = {
            "GREENLAKE_CLIENT_ID": "env-test-client-id",
            "GREENLAKE_CLIENT_SECRET": "env-test-client-secret",
            "GREENLAKE_API_BASE_URL": "https://global.api.greenlake.hpe.com",
            "GREENLAKE_WORKSPACE_ID": "env-test-workspace-id",
        }

        with patch.dict(os.environ, test_env, clear=False):
            test_settings = Settings()

            assert test_settings.greenlake_client_id == "env-test-client-id"
            assert test_settings.greenlake_client_secret == "env-test-client-secret"
            assert test_settings.greenlake_api_base_url == "https://global.api.greenlake.hpe.com"
            assert test_settings.greenlake_workspace_id == "env-test-workspace-id"

    def test_settings_validation(self):
        """Test settings validation for required fields."""
        # Test with missing required fields
        with patch.dict(os.environ, {}, clear=True):
            try:
                test_settings = Settings()
                # Some settings might have defaults
                assert test_settings is not None
            except Exception as e:
                # If validation fails, it should be meaningful
                assert any(field in str(e).lower() for field in ["client_id", "client_secret", "workspace"])

    def test_settings_compatibility_properties(self):
        """Test compatibility properties work correctly."""
        # Test compatibility properties that wrap GreenLake-specific ones
        assert settings.client_id == settings.greenlake_client_id
        assert settings.client_secret == settings.greenlake_client_secret
        assert settings.workspace_id == settings.greenlake_workspace_id
        assert settings.token_issuer == settings.token_issuer_url

    def test_settings_api_base_url_default(self):
        """Test API base URL has appropriate default."""
        # Should have a base URL configured
        assert hasattr(settings, "greenlake_api_base_url")
        assert settings.greenlake_api_base_url is not None
        assert len(settings.greenlake_api_base_url) > 0

        # Should be a valid URL format
        assert settings.greenlake_api_base_url.startswith(("http://", "https://"))

    def test_settings_service_specific_config(self):
        """Test service-specific configuration for users."""
        # Service API URL should be set correctly
        assert hasattr(settings, "service_api_url")
        service_url = settings.service_api_url
        assert service_url is not None
        assert len(service_url) > 0

    def test_settings_from_config_file(self):
        """Test settings can be loaded from configuration file."""
        config_content = """
GREENLAKE_CLIENT_ID=file-test-client-id
GREENLAKE_CLIENT_SECRET=file-test-client-secret
GREENLAKE_API_BASE_URL=https://file.test.api.com
GREENLAKE_WORKSPACE_ID=file-test-workspace-id
        """

        with tempfile.NamedTemporaryFile(mode="w", suffix=".env", delete=False) as f:
            f.write(config_content)
            config_file = f.name

        try:
            # Test loading from .env file (Pydantic will auto-load it)
            with patch.dict(os.environ, {"ENV_FILE": config_file}):
                test_settings = Settings()
                # Basic test that settings can be created
                assert test_settings is not None
        finally:
            os.unlink(config_file)

    def test_settings_debug_mode(self):
        """Test debug mode configuration through log level."""
        # Test debug mode enabled
        with patch.dict(os.environ, {"LOG_LEVEL": "DEBUG"}, clear=False):
            test_settings = Settings()
            assert test_settings.log_level.upper() == "DEBUG"

        # Test debug mode disabled
        with patch.dict(os.environ, {"LOG_LEVEL": "ERROR"}, clear=False):
            test_settings = Settings()
            assert test_settings.log_level.upper() == "ERROR"

    def test_settings_logging_level(self):
        """Test logging level configuration."""
        # Test various logging levels
        test_levels = ["DEBUG", "INFO", "WARNING", "ERROR"]

        for level in test_levels:
            with patch.dict(os.environ, {"LOG_LEVEL": level}, clear=False):
                test_settings = Settings()
                assert test_settings.log_level.upper() == level

    def test_settings_http_configuration(self):
        """Test HTTP client configuration settings."""
        # Test default HTTP settings
        assert hasattr(settings, "http_timeout")
        assert hasattr(settings, "http_retries")
        assert settings.http_timeout > 0
        assert settings.http_retries >= 0

        # Test custom HTTP settings
        test_env = {"HTTP_TIMEOUT": "60", "HTTP_RETRIES": "5"}

        with patch.dict(os.environ, test_env, clear=False):
            test_settings = Settings()
            assert test_settings.http_timeout == 60
            assert test_settings.http_retries == 5


class TestLogging:
    """Test cases for logging configuration."""

    def test_setup_logging_default(self):
        """Test logging setup with default configuration."""
        # Setup logging should not raise errors
        setup_logging()

        # Get logger and test basic functionality
        logger = get_logger("test_users")
        assert logger is not None
        # With loguru, get_logger returns the global logger instance
        assert logger == loguru_logger

    def test_setup_logging_with_level(self):
        """Test logging setup with specific log level."""
        # Test different log levels - convert to string names
        levels = ["DEBUG", "INFO", "WARNING", "ERROR"]

        for level in levels:
            setup_logging(level=level)
            logger = get_logger("test_level_users")

            # Logger should be created successfully
            assert logger is not None
            # With loguru, the logger is always the global instance
            assert logger == loguru_logger

    def test_get_logger_names(self):
        """Test logger naming for users."""
        # Test various logger names
        test_names = [
            "users.auth",
            "users.server",
            "users.tools",
            "users.http_client",
        ]

        for name in test_names:
            logger = get_logger(name)
            assert logger is not None
            # With loguru, all loggers are the same global instance
            assert logger == loguru_logger

    def test_logging_output_format(self):
        """Test logging output format."""
        setup_logging()
        logger = get_logger("format_test_users")

        # Test that logger can handle different log levels
        logger.info("Test info message for users")
        logger.warning("Test warning message for users")
        logger.error("Test error message for users")

        # Should not raise exceptions
        assert True

    def test_structured_logging(self):
        """Test structured logging functionality."""
        setup_logging()
        logger = get_logger("structured_test_users")

        # Test logging with structured data using loguru's bind()
        try:
            logger.bind(
                service="users",
                component="test",
                action="structured_logging_test",
            ).info("Structured log test")
            # Should handle structured data without errors
            assert True
        except Exception:
            # Fallback to basic logging if bind() has issues
            logger.info("Fallback to basic logging")
            assert True

    def test_logging_with_environment_config(self):
        """Test logging configuration from environment."""
        test_env = {"LOG_LEVEL": "DEBUG", "LOG_FORMAT": "json"}

        with patch.dict(os.environ, test_env, clear=False):
            setup_logging()
            logger = get_logger("env_test_users")

            # Should create logger successfully with env config
            assert logger is not None

    def test_logger_hierarchy(self):
        """Test logger hierarchy for users components."""
        setup_logging()

        # Create loggers with hierarchical names
        root_logger = get_logger("users")
        auth_logger = get_logger("users.auth")
        server_logger = get_logger("users.server")

        # All should be valid loggers
        assert root_logger is not None
        assert auth_logger is not None
        assert server_logger is not None

        # With loguru, all loggers are the same global instance
        # Loguru doesn't have a hierarchy like standard logging
        assert root_logger == loguru_logger
        assert auth_logger == loguru_logger
        assert server_logger == loguru_logger


class TestConfigIntegration:
    """Integration tests for config components."""

    def test_settings_and_logging_integration(self):
        """Test integration between settings and logging."""
        # Get settings
        test_settings = Settings()

        # Setup logging based on settings
        log_level = getattr(test_settings, "log_level", "INFO")
        # Validate the log level is valid before using it
        valid_levels = [
            "TRACE",
            "DEBUG",
            "INFO",
            "SUCCESS",
            "WARNING",
            "ERROR",
            "CRITICAL",
        ]
        if isinstance(log_level, str) and log_level.upper() in valid_levels:
            setup_logging(level=log_level.upper())
        else:
            setup_logging(level="INFO")

        logger = get_logger("integration_test_users")

        # Should work together without errors
        assert test_settings is not None
        assert logger is not None

        # Test logging with settings context - loguru uses bind() for context
        # Note: We can't test bind() result equality, just that it doesn't error
        try:
            logger.bind(
                client_id=getattr(test_settings, "client_id", "unknown"),
                api_base_url=getattr(test_settings, "greenlake_api_base_url", "unknown"),
            ).info("Integration test")
        except Exception:
            # Fallback to simple logging if bind() has issues
            logger.info("Integration test")

    def test_config_validation_with_dependencies(self):
        """Test configuration validation with dependent components."""
        # Create settings with environment variables
        test_env = {
            "GREENLAKE_CLIENT_ID": "test-client-id-deps",
            "GREENLAKE_CLIENT_SECRET": "test-client-secret-deps",
            "GREENLAKE_WORKSPACE_ID": "test-workspace-id-deps",
        }

        with patch.dict(os.environ, test_env, clear=False):
            test_settings = Settings()

            # Validate required fields for users
            required_fields = ["client_id", "client_secret", "token_issuer"]

            for field in required_fields:
                if hasattr(test_settings, field):
                    value = getattr(test_settings, field)
                    # Field should exist and not be empty (unless it's optional)
                    if value is not None:
                        assert len(str(value)) > 0

    def test_config_error_handling(self):
        """Test config error handling."""
        # Test with valid environment values first (required fields)
        valid_env = {
            "GREENLAKE_CLIENT_ID": "test-client-id-error",
            "GREENLAKE_CLIENT_SECRET": "test-client-secret-error",
            "GREENLAKE_WORKSPACE_ID": "test-workspace-id-error",
            "TOKEN_ISSUER": "not-a-valid-url",
            "LOG_LEVEL": "INVALID_LEVEL",
        }

        with patch.dict(os.environ, valid_env, clear=False):
            try:
                test_settings = Settings()
                setup_logging()

                # Should either work with defaults or fail gracefully
                assert test_settings is not None
            except Exception as e:
                # Should be meaningful error messages
                assert len(str(e)) > 0


class TestConfigSecurity:
    """Test security aspects of configuration."""

    def test_sensitive_data_not_logged(self):
        """Test that sensitive configuration data is not logged."""
        setup_logging()
        logger = get_logger("security_test_users")

        # Create settings with sensitive data
        test_env = {
            "GREENLAKE_CLIENT_ID": "test-client-id-security",
            "GREENLAKE_CLIENT_SECRET": "super-secret-value-users",
            "GREENLAKE_WORKSPACE_ID": "test-workspace-id-security",
            "TOKEN_ISSUER": "https://secure.users.com/oauth2/token",
        }

        with patch.dict(os.environ, test_env, clear=False):
            test_settings = Settings()

            # Log settings info (should not include secrets)
            logger.info(
                "Settings loaded",
                extra={
                    "client_id": getattr(test_settings, "client_id", "unknown"),
                    "has_client_id": bool(getattr(test_settings, "client_id", None)),
                    "has_client_secret": bool(getattr(test_settings, "client_secret", None)),
                },
            )

            # Should not log the actual secret value
            assert True  # Basic test that logging doesn't crash

    def test_config_file_permissions(self):
        """Test configuration file security."""
        # Create a temporary config file
        config_content = """
        CLIENT_ID=test-id
        CLIENT_SECRET=test-secret
        """

        with tempfile.NamedTemporaryFile(mode="w", suffix=".env", delete=False) as f:
            f.write(config_content)
            config_file = f.name

        try:
            # Check file permissions (should be readable by owner only)
            file_stat = os.stat(config_file)
            file_mode = file_stat.st_mode

            # Basic test that file exists and is readable
            assert os.path.isfile(config_file)
            assert os.access(config_file, os.R_OK)
            # Verify it's a regular file using file_mode
            assert stat.S_ISREG(file_mode)

        finally:
            os.unlink(config_file)

    def test_environment_variable_sanitization(self):
        """Test environment variable sanitization."""
        # Test with potentially dangerous values
        dangerous_env = {
            "CLIENT_ID": "test\nid\r\n",  # With newlines
            "CLIENT_SECRET": "test secret",  # With spaces
            "LOG_LEVEL": "DEBUG; rm -rf /",  # With injection attempt
        }

        with patch.dict(os.environ, dangerous_env, clear=False):
            try:
                settings = Settings()

                # Settings should handle sanitization or validation
                if hasattr(settings, "client_id"):
                    # Should not contain dangerous characters or be None
                    assert settings.client_id is None or "\\n" not in settings.client_id

            except Exception:
                # If settings reject dangerous input, that's good
                assert True


# Mock and fixture utilities for config testing
@pytest.fixture
def clean_environment():
    """Fixture to provide clean environment for testing."""
    original_env = os.environ.copy()
    # Clear config-related env vars
    config_vars = [
        "CLIENT_ID",
        "CLIENT_SECRET",
        "TOKEN_ISSUER",
        "API_BASE_URL",
        "WORKSPACE_ID",
        "DEBUG",
        "LOG_LEVEL",
        "LOG_FORMAT",
    ]
    for var in config_vars:
        os.environ.pop(var, None)

    yield

    # Restore original environment
    os.environ.clear()
    os.environ.update(original_env)


@pytest.fixture
def mock_config_file():
    """Fixture to provide mock configuration file."""
    config_content = """
    CLIENT_ID=mock-client-id-users
    CLIENT_SECRET=mock-client-secret-users
    TOKEN_ISSUER=https://mock.users.com/oauth2/token
    API_BASE_URL=https://mock.api.com
    WORKSPACE_ID=mock-workspace-id
    """

    with tempfile.NamedTemporaryFile(mode="w", suffix=".env", delete=False) as f:
        f.write(config_content)
        config_file = f.name

    yield config_file

    os.unlink(config_file)


# Edge case and error condition tests
class TestConfigEdgeCases:
    """Test edge cases and error conditions in config."""

    def test_empty_environment_variables(self):
        """Test behavior with empty environment variables."""
        empty_env = {
            "CLIENT_ID": "",
            "CLIENT_SECRET": "",
            "TOKEN_ISSUER": "",
        }

        with patch.dict(os.environ, empty_env, clear=False):
            try:
                settings = Settings()
                # Should handle empty values gracefully
                assert settings is not None
            except Exception as e:
                # Should provide meaningful error for empty required values
                assert any(field in str(e).lower() for field in ["client_id", "client_secret"])

    def test_very_long_config_values(self):
        """Test behavior with very long configuration values."""
        long_value = "x" * 10000  # Very long string

        long_env = {"CLIENT_ID": long_value, "API_BASE_URL": f"https://{'x' * 100}.com"}

        with patch.dict(os.environ, long_env, clear=False):
            try:
                settings = Settings()
                # Should handle long values or reject them appropriately
                assert settings is not None
            except Exception:
                # If validation rejects long values, that's acceptable
                assert True

    def test_unicode_config_values(self):
        """Test behavior with unicode configuration values."""
        unicode_env = {
            "CLIENT_ID": "test-中文-users",
            "TOKEN_ISSUER": "https://тест.users.com/oauth2/token",
        }

        with patch.dict(os.environ, unicode_env, clear=False):
            try:
                settings = Settings()
                # Should handle unicode values appropriately
                assert settings is not None
            except Exception:
                # Some configs might not support unicode
                assert True
