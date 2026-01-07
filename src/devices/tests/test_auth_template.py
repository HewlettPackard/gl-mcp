# (c) Copyright 2025 Hewlett Packard Enterprise Development LP
"""
Tests for authentication components in devices MCP server.

This file contains tests for OAuth2 provider and token manager.
"""

import pytest
from unittest.mock import Mock, patch
import time
import httpx

from auth.oauth2_provider import OAuth2Provider, OAuth2TokenResponse
from auth.token_manager import TokenManager, TokenInfo


class TestTokenInfo:
    """Test cases for TokenInfo model."""

    def test_token_info_creation(self):
        """Test TokenInfo creation with basic fields."""
        token_info = TokenInfo(
            token="test-token-devices",
            expires_at=time.time() + 3600,
        )

        assert token_info.token == "test-token-devices"
        assert token_info.expires_at is not None
        assert token_info.created_at is not None
        assert not token_info.is_expired()

    def test_token_info_expiry_check(self):
        """Test token expiry checking logic."""
        # Create expired token
        expired_token = TokenInfo(
            token="expired-token",
            expires_at=time.time() - 100,  # 100 seconds ago
        )
        assert expired_token.is_expired()

        # Create valid token
        valid_token = TokenInfo(
            token="valid-token",
            expires_at=time.time() + 3600,  # 1 hour from now
        )
        assert not valid_token.is_expired()

    def test_token_info_expiry_with_buffer(self):
        """Test token expiry checking with buffer."""
        # Create token that expires in 200 seconds
        soon_expiring = TokenInfo(token="soon-expiring", expires_at=time.time() + 200)

        # Should be expired with default 300s buffer
        assert soon_expiring.is_expired()

        # Should not be expired with 100s buffer
        assert not soon_expiring.is_expired(buffer_seconds=100)

    def test_time_until_expiry(self):
        """Test time until expiry calculation."""
        future_time = time.time() + 1000
        token_info = TokenInfo(token="test-token", expires_at=future_time)

        time_left = token_info.time_until_expiry()
        assert time_left is not None
        assert 990 <= time_left <= 1000  # Allow small timing variance

    def test_time_until_expiry_no_expiration(self):
        """Test time until expiry when no expiration is set."""
        token_info = TokenInfo(token="test-token")
        assert token_info.time_until_expiry() is None


class TestOAuth2Provider:
    """Test cases for OAuth2Provider."""

    @pytest.fixture
    def oauth2_provider(self):
        """Create OAuth2Provider instance for testing."""
        return OAuth2Provider(
            client_id="test-client-id",
            client_secret="test-client-secret",
            token_url="https://devices.example.com/oauth2/token",
            workspace_id="test-workspace-id",
        )

    @pytest.fixture
    def mock_token_response(self):
        """Mock successful token response."""
        return {
            "access_token": "test-access-token-devices",
            "token_type": "Bearer",
            "expires_in": 3600,
            "scope": "read write",
        }

    def test_oauth2_provider_initialization(self, oauth2_provider):
        """Test OAuth2Provider initialization for devices."""
        assert oauth2_provider.client_id == "test-client-id"
        assert oauth2_provider.client_secret == "test-client-secret"
        assert "devices" in oauth2_provider.token_url
        assert oauth2_provider.workspace_id == "test-workspace-id"

    @patch("auth.oauth2_provider.httpx.Client")
    def test_get_token_success(self, mock_client_class, mock_token_response):
        """Test successful token acquisition for devices."""
        # Setup mock client instance and response
        mock_client_instance = Mock()
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = mock_token_response
        mock_client_instance.post.return_value = mock_response
        mock_client_instance.__enter__ = Mock(return_value=mock_client_instance)
        mock_client_instance.__exit__ = Mock(return_value=None)
        mock_client_class.return_value = mock_client_instance

        # Create provider
        oauth2_provider = OAuth2Provider(
            client_id="test-client-id",
            client_secret="test-client-secret",
            token_url="https://devices.example.com/oauth2/token",
            workspace_id="test-workspace-id",
        )

        # Get token
        token = oauth2_provider.get_token()

        # Verify token response
        assert isinstance(token, OAuth2TokenResponse)
        assert token.access_token == "test-access-token-devices"
        assert token.token_type == "Bearer"
        assert token.expires_in == 3600
        assert token.scope == "read write"

        # Verify httpx.Client was called correctly
        mock_client_class.assert_called_once_with(timeout=30.0)
        mock_client_instance.post.assert_called_once_with(
            "https://devices.example.com/oauth2/token",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data={
                "grant_type": "client_credentials",
                "client_id": "test-client-id",
                "client_secret": "test-client-secret",
            },
        )

    @patch("auth.oauth2_provider.httpx.Client")
    def test_get_token_failure(self, mock_client_class):
        """Test failed token acquisition for devices."""
        # Setup mock client to return error response
        mock_client_instance = Mock()
        mock_response = Mock()
        mock_response.status_code = 400
        mock_response.text = "Bad Request: Invalid client credentials"
        mock_response.raise_for_status = Mock(
            side_effect=Exception("Token request failed: HTTP 400: Bad Request: Invalid client credentials")
        )
        mock_client_instance.post.return_value = mock_response
        mock_client_instance.__enter__ = Mock(return_value=mock_client_instance)
        mock_client_instance.__exit__ = Mock(return_value=None)
        mock_client_class.return_value = mock_client_instance

        oauth2_provider = OAuth2Provider(
            client_id="test-client-id",
            client_secret="test-client-secret",
            token_url="https://devices.example.com/oauth2/token",
            workspace_id="test-workspace-id",
        )

        # Expect exception when getting token
        with pytest.raises(Exception) as exc_info:
            oauth2_provider.get_token()

        assert "Token request failed" in str(exc_info.value)
        assert "HTTP 400" in str(exc_info.value)

    def test_oauth2_token_response_creation(self, mock_token_response):
        """Test OAuth2TokenResponse object creation."""
        token = OAuth2TokenResponse(**mock_token_response)

        assert token.access_token == "test-access-token-devices"
        assert token.token_type == "Bearer"
        assert token.expires_in == 3600
        assert token.scope == "read write"

    def test_oauth2_token_response_expiry_calculation(self):
        """Test token expiry calculation."""
        expires_in = 3600
        token_data = {
            "access_token": "test-token",
            "token_type": "Bearer",
            "expires_in": expires_in,
        }

        start_time = time.time()
        token = OAuth2TokenResponse(**token_data)
        end_time = time.time()

        # The expiry should be approximately start_time + expires_in
        expected_expiry = start_time + expires_in
        # Token creation should be fast (within 1 second)
        assert (end_time - start_time) < 1.0
        if token.expires_at:
            assert abs(token.expires_at - expected_expiry) < 2  # Allow 2 second tolerance

    def test_validate_token(self, oauth2_provider):
        """Test token validation for devices."""
        # Test valid token
        assert oauth2_provider.validate_token("valid-token") is True

        # Test empty token
        assert oauth2_provider.validate_token("") is False
        assert oauth2_provider.validate_token(None) is False

        # Test whitespace-only token
        assert oauth2_provider.validate_token("   ") is False

    @patch("auth.oauth2_provider.httpx.Client")
    def test_get_token_http_exception(self, mock_client_class):
        """Test handling of HTTP client exceptions during token acquisition."""
        # Setup mock client to raise an exception
        mock_client_instance = Mock()
        mock_client_instance.post.side_effect = Exception("Network error")
        mock_client_instance.__enter__ = Mock(return_value=mock_client_instance)
        mock_client_instance.__exit__ = Mock(return_value=None)
        mock_client_class.return_value = mock_client_instance

        oauth2_provider = OAuth2Provider(
            client_id="test-client-id",
            client_secret="test-client-secret",
            token_url="https://devices.example.com/oauth2/token",
            workspace_id="test-workspace-id",
        )

        # Expect exception when getting token
        with pytest.raises(Exception) as exc_info:
            oauth2_provider.get_token()

        assert "Network error" in str(exc_info.value)

    @patch("auth.oauth2_provider.httpx.Client")
    @patch("auth.oauth2_provider.time.sleep")
    def test_get_token_retries_on_429(self, mock_sleep, mock_client_class):
        """Test that get_token retries on 429 rate limit errors."""
        # Setup mock client to return 429 twice, then succeed
        mock_client_instance = Mock()

        # Create mock 429 responses that will raise HTTPStatusError
        mock_response_429 = Mock()
        mock_response_429.status_code = 429
        mock_response_429.text = "Too Many Requests"
        mock_response_429.raise_for_status.side_effect = httpx.HTTPStatusError(
            "429 Too Many Requests", request=Mock(), response=mock_response_429
        )

        mock_response_success = Mock()
        mock_response_success.status_code = 200
        mock_response_success.json.return_value = {
            "access_token": "test-token-after-retry",
            "token_type": "Bearer",
            "expires_in": 3600,
        }

        # First two calls return 429, third call succeeds
        mock_client_instance.post.side_effect = [
            mock_response_429,
            mock_response_429,
            mock_response_success,
        ]
        mock_client_instance.__enter__ = Mock(return_value=mock_client_instance)
        mock_client_instance.__exit__ = Mock(return_value=None)
        mock_client_class.return_value = mock_client_instance

        oauth2_provider = OAuth2Provider(
            client_id="test-client-id",
            client_secret="test-client-secret",
            token_url="https://devices.example.com/oauth2/token",
            max_retries=5,
            initial_backoff=1.0,
        )

        # Should succeed after retries
        token = oauth2_provider.get_token()

        assert token.access_token == "test-token-after-retry"
        assert mock_client_instance.post.call_count == 3
        # Should have slept twice (after first and second 429)
        assert mock_sleep.call_count == 2
        # First retry: 1s, second retry: 2s
        mock_sleep.assert_any_call(1.0)
        mock_sleep.assert_any_call(2.0)

    @patch("auth.oauth2_provider.httpx.Client")
    @patch("auth.oauth2_provider.time.sleep")
    def test_get_token_exhausts_retries_on_persistent_429(self, mock_sleep, mock_client_class):
        """Test that get_token fails after exhausting retries on persistent 429 errors."""
        # Setup mock client to always return 429
        mock_client_instance = Mock()
        mock_response_429 = Mock()
        mock_response_429.status_code = 429
        mock_response_429.text = "Too Many Requests"
        mock_response_429.raise_for_status.side_effect = httpx.HTTPStatusError(
            "429 Too Many Requests", request=Mock(), response=mock_response_429
        )

        mock_client_instance.post.return_value = mock_response_429
        mock_client_instance.__enter__ = Mock(return_value=mock_client_instance)
        mock_client_instance.__exit__ = Mock(return_value=None)
        mock_client_class.return_value = mock_client_instance

        oauth2_provider = OAuth2Provider(
            client_id="test-client-id",
            client_secret="test-client-secret",
            token_url="https://devices.example.com/oauth2/token",
            max_retries=3,
            initial_backoff=1.0,
        )

        # Should raise after exhausting retries
        with pytest.raises(httpx.HTTPStatusError) as exc_info:
            oauth2_provider.get_token()

        assert exc_info.value.response.status_code == 429
        # Should try: initial + 3 retries = 4 attempts
        assert mock_client_instance.post.call_count == 4
        # Should sleep 3 times (after each of the first 3 attempts)
        assert mock_sleep.call_count == 3

    @patch("auth.oauth2_provider.httpx.Client")
    @patch("auth.oauth2_provider.time.sleep")
    def test_get_token_exponential_backoff_calculation(self, mock_sleep, mock_client_class):
        """Test that exponential backoff is calculated correctly."""
        # Setup mock client to return 429 repeatedly
        mock_client_instance = Mock()
        mock_response_429 = Mock()
        mock_response_429.status_code = 429
        mock_response_429.text = "Too Many Requests"
        mock_response_429.raise_for_status.side_effect = httpx.HTTPStatusError(
            "429 Too Many Requests", request=Mock(), response=mock_response_429
        )

        mock_client_instance.post.return_value = mock_response_429
        mock_client_instance.__enter__ = Mock(return_value=mock_client_instance)
        mock_client_instance.__exit__ = Mock(return_value=None)
        mock_client_class.return_value = mock_client_instance

        oauth2_provider = OAuth2Provider(
            client_id="test-client-id",
            client_secret="test-client-secret",
            token_url="https://devices.example.com/oauth2/token",
            max_retries=5,
            initial_backoff=1.0,
            max_backoff=60.0,
        )

        # Should raise after exhausting retries
        with pytest.raises(httpx.HTTPStatusError):
            oauth2_provider.get_token()

        # Verify exponential backoff: 1s, 2s, 4s, 8s, 16s
        expected_delays = [1.0, 2.0, 4.0, 8.0, 16.0]
        actual_calls = [call[0][0] for call in mock_sleep.call_args_list]
        assert actual_calls == expected_delays

    @patch("auth.oauth2_provider.httpx.Client")
    @patch("auth.oauth2_provider.time.sleep")
    def test_get_token_respects_max_backoff(self, mock_sleep, mock_client_class):
        """Test that backoff delay respects max_backoff limit."""
        # Setup mock client to return 429 repeatedly
        mock_client_instance = Mock()
        mock_response_429 = Mock()
        mock_response_429.status_code = 429
        mock_response_429.text = "Too Many Requests"
        mock_response_429.raise_for_status.side_effect = httpx.HTTPStatusError(
            "429 Too Many Requests", request=Mock(), response=mock_response_429
        )

        mock_client_instance.post.return_value = mock_response_429
        mock_client_instance.__enter__ = Mock(return_value=mock_client_instance)
        mock_client_instance.__exit__ = Mock(return_value=None)
        mock_client_class.return_value = mock_client_instance

        oauth2_provider = OAuth2Provider(
            client_id="test-client-id",
            client_secret="test-client-secret",
            token_url="https://devices.example.com/oauth2/token",
            max_retries=5,
            initial_backoff=1.0,
            max_backoff=5.0,  # Cap at 5 seconds
        )

        # Should raise after exhausting retries
        with pytest.raises(httpx.HTTPStatusError):
            oauth2_provider.get_token()

        # Verify backoff respects max: 1s, 2s, 4s, 5s (capped), 5s (capped)
        expected_delays = [1.0, 2.0, 4.0, 5.0, 5.0]
        actual_calls = [call[0][0] for call in mock_sleep.call_args_list]
        assert actual_calls == expected_delays

    @patch("auth.oauth2_provider.httpx.Client")
    @patch("auth.oauth2_provider.time.sleep")
    def test_get_token_no_retry_on_non_429_errors(self, mock_sleep, mock_client_class):
        """Test that non-429 errors are not retried."""
        # Setup mock client to return 401 (Unauthorized)
        mock_client_instance = Mock()
        mock_response_401 = Mock()
        mock_response_401.status_code = 401
        mock_response_401.text = "Unauthorized"
        mock_response_401.raise_for_status = Mock(side_effect=Exception("HTTP 401: Unauthorized"))

        mock_client_instance.post.return_value = mock_response_401
        mock_client_instance.__enter__ = Mock(return_value=mock_client_instance)
        mock_client_instance.__exit__ = Mock(return_value=None)
        mock_client_class.return_value = mock_client_instance

        oauth2_provider = OAuth2Provider(
            client_id="test-client-id",
            client_secret="test-client-secret",
            token_url="https://devices.example.com/oauth2/token",
            max_retries=5,
        )

        # Should fail immediately without retries
        with pytest.raises(Exception) as exc_info:
            oauth2_provider.get_token()

        assert "401" in str(exc_info.value)
        # Should only try once (no retries for non-429)
        assert mock_client_instance.post.call_count == 1
        # Should never sleep
        assert mock_sleep.call_count == 0

    def test_oauth2_provider_initialization_with_retry_params(self):
        """Test OAuth2Provider initialization with custom retry parameters."""
        oauth2_provider = OAuth2Provider(
            client_id="test-client-id",
            client_secret="test-client-secret",
            token_url="https://devices.example.com/oauth2/token",
            workspace_id="test-workspace-id",
            max_retries=10,
            initial_backoff=2.0,
            max_backoff=120.0,
        )

        assert oauth2_provider.max_retries == 10
        assert abs(oauth2_provider.initial_backoff - 2.0) < 0.001
        assert abs(oauth2_provider.max_backoff - 120.0) < 0.001

    def test_oauth2_provider_default_retry_params(self):
        """Test OAuth2Provider uses correct default retry parameters."""
        oauth2_provider = OAuth2Provider(
            client_id="test-client-id",
            client_secret="test-client-secret",
            token_url="https://devices.example.com/oauth2/token",
        )

        # Verify defaults: max_retries=5, initial_backoff=1.0, max_backoff=60.0
        assert oauth2_provider.max_retries == 5
        assert abs(oauth2_provider.initial_backoff - 1.0) < 0.001
        assert abs(oauth2_provider.max_backoff - 60.0) < 0.001


class TestTokenManager:
    """Test cases for TokenManager."""

    @pytest.fixture
    def mock_settings(self):
        """Mock settings for testing devices."""
        settings = Mock()
        settings.client_id = "test-client-id"
        settings.client_secret = "test-client-secret"
        settings.workspace_id = "test-workspace-id"
        settings.token_issuer = "https://devices.example.com/oauth2/token"
        settings.is_testing = False  # Default to non-test mode for explicit control
        return settings

    @pytest.fixture
    def token_manager(self, mock_settings):
        """Create TokenManager instance for testing."""
        with patch("auth.token_manager.OAuth2Provider") as mock_provider:
            # Mock the OAuth2 provider to avoid real network calls
            mock_provider_instance = Mock()
            mock_provider.return_value = mock_provider_instance
            return TokenManager(settings=mock_settings)

    @pytest.fixture
    def valid_token(self):
        """Create a valid token for testing."""
        return OAuth2TokenResponse(
            access_token="valid-token-devices",
            token_type="Bearer",
            expires_in=3600,
            scope="read write",
        )

    @pytest.fixture
    def expired_token(self):
        """Create an expired token for testing."""
        return OAuth2TokenResponse(
            access_token="expired-token-devices",
            token_type="Bearer",
            expires_in=-100,  # Already expired
            scope="read write",
        )

    def test_token_manager_initialization(self):
        """Test TokenManager initialization for devices with lazy token loading."""
        with patch("auth.token_manager.OAuth2Provider") as mock_provider_class:
            # Setup mock provider
            mock_provider = Mock()
            mock_provider_class.return_value = mock_provider

            mock_settings = Mock()
            mock_settings.client_id = "test-client-id"
            mock_settings.client_secret = "test-client-secret"
            mock_settings.workspace_id = "test-workspace-id"
            mock_settings.token_issuer = "https://devices.example.com/oauth2/token"
            mock_settings.is_testing = False  # Not in test mode

            token_manager = TokenManager(settings=mock_settings)

            # With lazy initialization, token should NOT be fetched during init
            assert token_manager._token_info is None
            assert token_manager._oauth2_provider is not None
            # Verify get_token was NOT called during initialization
            mock_provider.get_token.assert_not_called()

    def test_token_manager_initialization_test_mode(self):
        """Test TokenManager initialization in test mode sets test token."""
        with patch("auth.token_manager.OAuth2Provider") as mock_provider_class:
            mock_provider = Mock()
            mock_provider_class.return_value = mock_provider

            mock_settings = Mock()
            mock_settings.client_id = "test"  # Test client ID
            mock_settings.client_secret = "test-client-secret"
            mock_settings.workspace_id = "test-workspace-id"
            mock_settings.token_issuer = "https://devices.example.com/oauth2/token"
            mock_settings.is_testing = True

            token_manager = TokenManager(settings=mock_settings)

            # In test mode, test token should be set immediately
            assert token_manager._token_info is not None
            assert token_manager._token_info.token == "test_token_12345"
            assert token_manager._oauth2_provider is not None
            # Verify get_token was NOT called (test token used instead)
            mock_provider.get_token.assert_not_called()

    @patch("auth.token_manager.OAuth2Provider")
    def test_get_valid_token_when_none_cached(self, mock_provider_class, mock_settings, valid_token):
        """Test lazy token generation when none is cached for devices."""
        # Setup mock provider
        mock_provider = Mock()
        mock_provider.get_token.return_value = valid_token
        mock_provider_class.return_value = mock_provider

        token_manager = TokenManager(settings=mock_settings)

        # Token should NOT be generated during initialization (lazy init)
        assert token_manager._token_info is None
        mock_provider.get_token.assert_not_called()

        # Token should be generated on first call to get_auth_headers
        auth_headers = token_manager.get_auth_headers()

        assert "Authorization" in auth_headers
        assert f"Bearer {valid_token.access_token}" in auth_headers["Authorization"]
        # Now get_token should have been called (lazy initialization)
        mock_provider.get_token.assert_called_once()

    @patch("auth.token_manager.OAuth2Provider")
    def test_get_valid_token_when_valid_cached(self, mock_provider_class, mock_settings, valid_token):
        """Test getting token when valid one is cached for devices."""
        # Setup mock provider to return proper token
        mock_provider = Mock()
        mock_provider.get_token.return_value = valid_token
        mock_provider_class.return_value = mock_provider

        token_manager = TokenManager(settings=mock_settings)

        # Manually set a valid cached token
        token_manager._set_token_from_oauth2_response(valid_token)

        # First call should use cached token without calling get_token
        auth_headers = token_manager.get_auth_headers()

        assert "Authorization" in auth_headers
        assert f"Bearer {valid_token.access_token}" in auth_headers["Authorization"]
        # Should not call get_token since cached token is valid
        mock_provider.get_token.assert_not_called()

    @patch("auth.token_manager.OAuth2Provider")
    def test_get_valid_token_when_expired_cached(self, mock_provider_class, mock_settings, expired_token, valid_token):
        """Test automatic token refresh when expired token is cached for devices."""
        # Setup mock provider
        mock_provider = Mock()
        mock_provider.get_token.return_value = valid_token
        mock_provider_class.return_value = mock_provider

        token_manager = TokenManager(settings=mock_settings)

        # Set up expired cached token
        token_manager._set_token_from_oauth2_response(expired_token)

        # Should automatically refresh the token
        auth_headers = token_manager.get_auth_headers()

        assert "Authorization" in auth_headers
        assert f"Bearer {valid_token.access_token}" in auth_headers["Authorization"]
        # Should call get_token to refresh expired token
        mock_provider.get_token.assert_called_once()

    @patch("auth.token_manager.OAuth2Provider")
    def test_lazy_initialization_multiple_calls(self, mock_provider_class, mock_settings, valid_token):
        """Test that lazy initialization only fetches token once for multiple calls."""
        # Setup mock provider
        mock_provider = Mock()
        mock_provider.get_token.return_value = valid_token
        mock_provider_class.return_value = mock_provider

        token_manager = TokenManager(settings=mock_settings)

        # Verify no token on initialization
        assert token_manager._token_info is None
        mock_provider.get_token.assert_not_called()

        # First call should fetch token
        headers1 = token_manager.get_auth_headers()
        assert "Authorization" in headers1
        mock_provider.get_token.assert_called_once()

        # Second call should reuse cached token
        headers2 = token_manager.get_auth_headers()
        assert "Authorization" in headers2
        assert headers1 == headers2
        # Still only called once
        mock_provider.get_token.assert_called_once()

        # Third call should also reuse cached token
        headers3 = token_manager.get_auth_headers()
        assert headers2 == headers3
        # Still only called once
        mock_provider.get_token.assert_called_once()

    @patch("auth.token_manager.OAuth2Provider")
    def test_initialization_with_initial_token(self, mock_provider_class, mock_settings):
        """Test TokenManager initialization with pre-provided token bypasses lazy init."""
        mock_provider = Mock()
        mock_provider_class.return_value = mock_provider

        # Initialize with an initial token
        initial_token = "pre-provided-token-devices"
        token_manager = TokenManager(settings=mock_settings, initial_token=initial_token)

        # Token should be set immediately (not lazy)
        assert token_manager._token_info is not None
        assert token_manager._token_info.token == initial_token

        # Should not call OAuth provider
        mock_provider.get_token.assert_not_called()

        # Getting headers should use the pre-provided token
        headers = token_manager.get_auth_headers()
        assert f"Bearer {initial_token}" == headers["Authorization"]
        mock_provider.get_token.assert_not_called()

    def test_is_token_valid_with_valid_token(self, mock_settings, valid_token):
        """Test token validity check with valid token."""
        with patch("auth.token_manager.OAuth2Provider") as mock_provider_class:
            # Setup mock to return valid token during initialization
            mock_provider = Mock()
            mock_provider.get_token.return_value = valid_token
            mock_provider_class.return_value = mock_provider

            token_manager = TokenManager(settings=mock_settings)
            token_manager._set_token_from_oauth2_response(valid_token)
            assert token_manager.is_token_valid() is True

    def test_is_token_valid_with_expired_token(self, mock_settings, expired_token):
        """Test token validity check with expired token."""
        with patch("auth.token_manager.OAuth2Provider") as mock_provider_class:
            # Setup mock to return expired token during initialization
            mock_provider = Mock()
            mock_provider.get_token.return_value = expired_token
            mock_provider_class.return_value = mock_provider

            token_manager = TokenManager(settings=mock_settings)
            token_manager._set_token_from_oauth2_response(expired_token)
            assert token_manager.is_token_valid() is False

    def test_is_token_valid_with_none(self, mock_settings):
        """Test token validity check with None token."""
        with patch("auth.token_manager.OAuth2Provider") as mock_provider_class:
            # Setup mock to return a valid token during initialization but we'll clear it
            mock_provider = Mock()
            valid_init_token = OAuth2TokenResponse(
                access_token="init-token",
                token_type="Bearer",
                expires_in=3600,
                scope="read write",
            )
            mock_provider.get_token.return_value = valid_init_token
            mock_provider_class.return_value = mock_provider

            token_manager = TokenManager(settings=mock_settings)
            token_manager._token_info = None
            assert token_manager.is_token_valid() is False

    def test_is_token_valid_with_soon_expiring_token(self, mock_settings):
        """Test token validity check with soon-to-expire token."""
        with patch("auth.token_manager.OAuth2Provider") as mock_provider_class:
            # Setup mock to return a valid token during initialization
            mock_provider = Mock()
            valid_init_token = OAuth2TokenResponse(
                access_token="init-token",
                token_type="Bearer",
                expires_in=3600,
                scope="read write",
            )
            mock_provider.get_token.return_value = valid_init_token
            mock_provider_class.return_value = mock_provider

            # Token expires in 30 seconds (within buffer)
            soon_expiring_token = OAuth2TokenResponse(
                access_token="soon-expiring-token",
                token_type="Bearer",
                expires_in=30,
                scope="read write",
            )

            token_manager = TokenManager(settings=mock_settings)
            token_manager._set_token_from_oauth2_response(soon_expiring_token)
            # Should be considered invalid due to buffer
            assert token_manager.is_token_valid() is False

    @patch("auth.token_manager.OAuth2Provider")
    def test_token_refresh_on_auth_error(self, mock_provider_class, mock_settings, valid_token):
        """Test manual token refresh using refresh_token method."""
        # Setup mock provider
        mock_provider = Mock()
        mock_provider_class.return_value = mock_provider

        # Create refreshed token
        refreshed_token = OAuth2TokenResponse(
            access_token="refreshed-token-devices",
            token_type="Bearer",
            expires_in=3600,
            scope="read write",
        )
        # Always return refreshed_token for any call to get_token
        mock_provider.get_token.return_value = refreshed_token

        token_manager = TokenManager(settings=mock_settings)

        # With lazy init, token should be None initially
        assert token_manager._token_info is None

        # Get initial token through auth headers (triggers lazy init)
        initial_headers = token_manager.get_auth_headers()
        assert "Authorization" in initial_headers
        assert initial_headers["Authorization"].startswith("Bearer ")
        assert mock_provider.get_token.call_count == 1

        # Force refresh by calling refresh_token
        token_manager.refresh_token()

        # Verify that refresh_token caused an additional call to get_token
        assert mock_provider.get_token.call_count == 2

    @patch("auth.token_manager.OAuth2Provider")
    def test_get_authorization_header(self, mock_provider_class, mock_settings, valid_token):
        """Test getting authorization header with lazy initialization for devices."""
        # Setup mock provider
        mock_provider = Mock()
        mock_provider.get_token.return_value = valid_token
        mock_provider_class.return_value = mock_provider

        token_manager = TokenManager(settings=mock_settings)

        # Token should be None initially (lazy init)
        assert token_manager._token_info is None

        headers = token_manager.get_auth_headers()

        expected_header = f"Bearer {valid_token.access_token}"
        assert headers["Authorization"] == expected_header
        # Verify token was fetched (lazy init triggered)
        mock_provider.get_token.assert_called_once()


class TestAuthIntegration:
    """Integration tests for auth components."""

    @pytest.fixture
    def mock_settings(self):
        """Mock settings for integration testing."""
        settings = Mock()
        settings.client_id = "integration-client-id"
        settings.client_secret = "integration-client-secret"
        settings.workspace_id = "integration-workspace-id"
        settings.token_issuer = "https://devices.integration.com/oauth2/token"
        settings.is_testing = False  # Disable test mode for integration tests
        return settings

    @patch("auth.oauth2_provider.httpx.Client")
    def test_end_to_end_token_flow(self, mock_client_class, mock_settings):
        """Test complete lazy token acquisition and management flow for devices."""
        # Setup mock httpx.Client
        mock_client_instance = Mock()
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "access_token": "integration-test-token-devices",
            "token_type": "Bearer",
            "expires_in": 3600,
            "scope": "read write admin",
        }
        mock_client_instance.post.return_value = mock_response
        mock_client_instance.__enter__ = Mock(return_value=mock_client_instance)
        mock_client_instance.__exit__ = Mock(return_value=None)
        mock_client_class.return_value = mock_client_instance

        # Create token manager with lazy initialization
        token_manager = TokenManager(settings=mock_settings)

        # Verify token is NOT fetched during initialization (lazy init)
        assert token_manager._token_info is None
        mock_client_instance.post.assert_not_called()

        # Get token through manager (triggers lazy init)
        auth_headers = token_manager.get_auth_headers()

        # Verify token properties through headers
        assert "Authorization" in auth_headers
        assert "integration-test-token-devices" in auth_headers["Authorization"]
        assert auth_headers["Authorization"].startswith("Bearer ")

        # Verify httpx.Client was called correctly
        mock_client_class.assert_called()
        mock_client_instance.post.assert_called()


# Error handling and edge case tests
class TestAuthErrorHandling:
    """Test error handling in auth components."""

    def test_oauth2_provider_with_invalid_config(self):
        """Test OAuth2Provider with invalid configuration."""
        # Try to create provider with empty client_id - should work but log warning
        provider = OAuth2Provider(
            client_id="",  # Empty client_id - still valid but not recommended
            client_secret="secret",
            token_url="invalid-url",
            workspace_id="workspace",
        )
        # OAuth2Provider doesn't validate input in constructor, it validates during token fetch
        assert provider.client_id == ""
        assert provider.client_secret == "secret"

    def test_token_response_with_invalid_data(self):
        """Test OAuth2TokenResponse validation with invalid data types."""
        # Test that OAuth2TokenResponse requires valid string for access_token
        try:
            # This should work fine - testing with minimal valid data
            token = OAuth2TokenResponse(access_token="test-token", token_type="Bearer")
            assert token.access_token == "test-token"
            assert token.token_type == "Bearer"
        except Exception:
            # If this fails, there's an issue with the model itself
            pytest.fail("OAuth2TokenResponse should accept valid minimal data")

    @patch("auth.token_manager.OAuth2Provider")
    def test_token_manager_handles_oauth_errors(self, mock_provider_class):
        """Test TokenManager handles OAuth provider errors gracefully with lazy init."""
        # Setup mock provider to raise exception
        mock_provider = Mock()
        mock_provider.get_token.side_effect = Exception("OAuth server error")
        mock_provider_class.return_value = mock_provider

        mock_settings = Mock()
        mock_settings.client_id = "production-id"  # Use non-test ID to bypass test detection
        mock_settings.client_secret = "production-secret"
        mock_settings.workspace_id = "production-workspace"
        mock_settings.token_issuer = "https://production.com/token"
        mock_settings.is_testing = False  # Explicitly set to non-test mode

        # With lazy initialization, TokenManager creation should succeed
        token_manager = TokenManager(settings=mock_settings)
        assert token_manager._token_info is None

        # Error should occur when trying to get auth headers (first token fetch)
        with pytest.raises(Exception, match="OAuth server error"):
            token_manager.get_auth_headers()
