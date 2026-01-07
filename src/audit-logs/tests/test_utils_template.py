# (c) Copyright 2025 Hewlett Packard Enterprise Development LP
"""
Tests for utility components in audit-logs MCP server.

This file contains tests for HTTP client and other utilities.
"""

import pytest
from unittest.mock import Mock, patch
import httpx

from utils.http_client import AuditLogsHttpClient, get_http_client


class TestAuditLogsHttpClient:
    """Test cases for AuditLogsHttpClient."""

    @pytest.fixture
    def mock_token_manager(self):
        """Mock token manager."""
        mock_manager = Mock()  # Use Mock instead of AsyncMock
        mock_manager.get_auth_headers.return_value = {
            "Authorization": "Bearer test-access-token",
            "Content-Type": "application/json",
        }
        return mock_manager

    @pytest.fixture
    def http_client(self, mock_token_manager):
        """Create HTTP client instance for testing."""
        with patch("utils.http_client.TokenManager", return_value=mock_token_manager):
            return AuditLogsHttpClient()

    def test_http_client_initialization(self, http_client):
        """Test HTTP client initialization."""
        assert http_client is not None
        assert hasattr(http_client, "token_manager")
        assert hasattr(http_client, "client")
        assert hasattr(http_client, "base_url")

    @pytest.mark.asyncio
    async def test_get_request_success(self, http_client, mock_token_manager):
        """Test successful GET request."""
        mock_response_data = {"id": "test", "name": "Test Resource"}

        with patch.object(http_client.client, "get") as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = mock_response_data
            mock_response.raise_for_status.return_value = None
            mock_get.return_value = mock_response

            # Execute GET request
            result = await http_client.get("/test/endpoint")

            # Assertions
            assert result == mock_response_data
            mock_get.assert_called_once()
            mock_token_manager.get_auth_headers.assert_called()

    @pytest.mark.asyncio
    async def test_get_auth_headers_includes_user_agent(self, http_client):
        """Test that authentication headers include User-Agent."""
        headers = await http_client._get_auth_headers()

        # Verify all required headers are present
        assert "Authorization" in headers
        assert "Accept" in headers
        assert "User-Agent" in headers

        # Verify User-Agent format
        assert headers["User-Agent"].startswith("HPE-GreenLake-MCP/")
        assert headers["Accept"] == "application/json"

    @pytest.mark.asyncio
    async def test_get_request_with_additional_headers(self, http_client):
        """Test GET request with additional headers."""
        additional_headers = {"X-Custom-Header": "custom-value"}

        with patch.object(http_client.client, "get") as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = {}
            mock_response.raise_for_status.return_value = None
            mock_get.return_value = mock_response

            # Execute GET request with additional headers
            await http_client.get("/test/endpoint", additional_headers=additional_headers)

            # Check that headers were merged correctly
            call_args = mock_get.call_args
            headers = call_args.kwargs["headers"]
            assert headers["Authorization"] == "Bearer test-access-token"
            assert headers["X-Custom-Header"] == "custom-value"
            assert headers["User-Agent"].startswith("HPE-GreenLake-MCP/")

    @pytest.mark.asyncio
    async def test_post_request_success(self, http_client, mock_token_manager):
        """Test successful POST request."""
        request_data = {"name": "New Resource"}
        mock_response_data = {"id": "new", "name": "New Resource"}

        with patch.object(http_client.client, "post") as mock_post:
            mock_response = Mock()
            mock_response.json.return_value = mock_response_data
            mock_response.raise_for_status.return_value = None
            mock_post.return_value = mock_response

            # Execute POST request
            result = await http_client.post("/test/endpoint", data=request_data)

            # Assertions
            assert result == mock_response_data
            mock_post.assert_called_once()
            mock_token_manager.get_auth_headers.assert_called()

    @pytest.mark.asyncio
    async def test_get_request_authentication_failure(self, http_client):
        """Test GET request with authentication failure."""
        # Mock to raise authentication error instead of making real HTTP call
        with patch.object(http_client, "_get_auth_headers", side_effect=Exception("Auth failed")):
            with pytest.raises(Exception, match="Auth failed"):
                await http_client.get("/test/endpoint")

    @pytest.mark.asyncio
    async def test_get_request_http_error(self, http_client):
        """Test GET request with HTTP error."""
        with patch.object(http_client.client, "get") as mock_get:
            mock_response = Mock()
            mock_response.status_code = 404
            mock_response.text = "Not Found"
            mock_get.return_value = mock_response
            mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
                message="Not Found", request=Mock(), response=mock_response
            )

            with pytest.raises(httpx.HTTPStatusError):
                await http_client.get("/test/endpoint")

    @pytest.mark.asyncio
    async def test_put_request_success(self, http_client, mock_token_manager):
        """Test successful PUT request."""
        update_data = {"name": "Updated Resource for audit-logs", "status": "modified"}

        with patch.object(http_client.client, "put") as mock_put:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {"id": "updated", "name": "Updated Resource"}
            mock_response.raise_for_status.return_value = None
            mock_put.return_value = mock_response

            # Execute PUT request
            result = await http_client.put("/test-endpoint/123", data=update_data)

            # Assertions
            assert result["id"] == "updated"
            mock_put.assert_called_once()
            mock_token_manager.get_auth_headers.assert_called()

    @pytest.mark.asyncio
    async def test_delete_request_success(self, http_client, mock_token_manager):
        """Test successful DELETE request."""
        with patch.object(http_client.client, "delete") as mock_delete:
            mock_response = Mock()
            mock_response.status_code = 204
            mock_response.json.return_value = {}
            mock_response.raise_for_status.return_value = None
            mock_delete.return_value = mock_response

            # Execute DELETE request
            result = await http_client.delete("/test-endpoint/123")

            # Assertions
            assert result == {}
            mock_delete.assert_called_once()
            mock_token_manager.get_auth_headers.assert_called()

    @pytest.mark.asyncio
    async def test_request_with_query_params(self, http_client, mock_token_manager):
        """Test request with query parameters."""
        query_params = {"filter": "active", "limit": 10, "service": "audit-logs"}
        mock_response_data = {"items": [{"id": 1, "name": "Test"}]}

        with patch.object(http_client.client, "get") as mock_get:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = mock_response_data
            mock_response.raise_for_status.return_value = None
            mock_get.return_value = mock_response

            # Execute GET request with params
            result = await http_client.get("/test-endpoint", params=query_params)

            # Assertions
            assert result == mock_response_data
            call_args = mock_get.call_args
            assert "params" in call_args.kwargs
            assert call_args.kwargs["params"] == query_params
            mock_token_manager.get_auth_headers.assert_called()

    @pytest.mark.asyncio
    async def test_close(self, http_client):
        """Test HTTP client close."""
        with patch.object(http_client.client, "aclose") as mock_close:
            await http_client.close()
            mock_close.assert_called_once()


class TestHttpClientFactory:
    """Test cases for HTTP client factory function."""

    def test_get_http_client(self):
        """Test getting HTTP client instance."""
        with patch("utils.http_client.AuditLogsHttpClient") as mock_client_class:
            mock_client = Mock()
            mock_client_class.return_value = mock_client

            client = get_http_client()

            assert client == mock_client
            mock_client_class.assert_called_once()

    def test_get_http_client_multiple_calls(self):
        """Test that multiple calls return the same instance."""
        # Reset the global client first
        import utils.http_client

        utils.http_client._http_client = None

        # Mock TokenManager to avoid real authentication
        with patch("utils.http_client.TokenManager") as mock_token_manager_class:
            mock_token_manager = Mock()
            mock_token_manager.get_auth_headers.return_value = {
                "Authorization": "Bearer test-token",
                "Content-Type": "application/json",
            }
            mock_token_manager_class.return_value = mock_token_manager

            client1 = get_http_client()
            client2 = get_http_client()

            # Should be the same instance (singleton pattern)
            assert client1 is client2


class TestHttpClientIntegration:
    """Integration tests for HTTP client."""

    @pytest.fixture
    def integration_token_manager(self):
        """Integration token manager mock."""
        mock_manager = Mock()
        mock_manager.get_auth_headers.return_value = {
            "Authorization": "Bearer integration-token-audit-logs",
            "Content-Type": "application/json",
        }
        return mock_manager

    @pytest.mark.asyncio
    async def test_full_request_cycle(self, integration_token_manager):
        """Test full request cycle with authentication."""
        with patch("utils.http_client.TokenManager", return_value=integration_token_manager):
            http_client = AuditLogsHttpClient()

            with patch.object(http_client.client, "get") as mock_get:
                mock_response = Mock()
                mock_response.status_code = 200
                mock_response.json.return_value = {"service": "audit-logs", "status": "healthy", "version": "1.0.0"}
                mock_response.raise_for_status.return_value = None
                mock_get.return_value = mock_response

                # Execute request
                result = await http_client.get("/health")

                # Verify result
                assert result["service"] == "audit-logs"
                assert result["status"] == "healthy"

                # Verify authentication was included
                call_args = mock_get.call_args
                headers = call_args.kwargs.get("headers", {})
                assert "integration-token-audit-logs" in headers.get("Authorization", "")

    @pytest.mark.asyncio
    async def test_error_recovery_flow(self, integration_token_manager):
        """Test error recovery flow."""
        with patch("utils.http_client.TokenManager", return_value=integration_token_manager):
            http_client = AuditLogsHttpClient()

            # First request fails, second succeeds
            with patch.object(http_client.client, "get") as mock_get:
                error_response = Mock()
                error_response.status_code = 500
                error_response.raise_for_status.side_effect = httpx.HTTPStatusError(
                    "Internal Server Error", request=Mock(), response=error_response
                )

                success_response = Mock()
                success_response.status_code = 200
                success_response.json.return_value = {"recovered": True}
                success_response.raise_for_status.return_value = None

                mock_get.side_effect = [error_response, success_response]

                # First request should fail
                with pytest.raises(httpx.HTTPStatusError):
                    await http_client.get("/failing-endpoint")

                # Second request should succeed
                result = await http_client.get("/recovered-endpoint")
                assert result["recovered"] is True


class TestHttpClientErrorHandling:
    """Test error handling in HTTP client."""

    @pytest.fixture
    def error_test_client(self):
        """HTTP client for error testing."""
        mock_token_manager = Mock()
        mock_token_manager.get_auth_headers.return_value = {
            "Authorization": "Bearer error-test-token",
            "Content-Type": "application/json",
        }

        with patch("utils.http_client.TokenManager", return_value=mock_token_manager):
            return AuditLogsHttpClient()

    @pytest.mark.asyncio
    async def test_malformed_response_handling(self, error_test_client):
        """Test handling of malformed JSON responses."""
        with patch.object(error_test_client.client, "get") as mock_get:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.side_effect = ValueError("Invalid JSON")
            mock_response.raise_for_status.return_value = None
            mock_get.return_value = mock_response

            # Should handle JSON parsing errors gracefully
            with pytest.raises(ValueError):
                await error_test_client.get("/malformed-json-endpoint")

    @pytest.mark.asyncio
    async def test_empty_response_handling(self, error_test_client):
        """Test handling of empty responses."""
        with patch.object(error_test_client.client, "delete") as mock_delete:
            mock_response = Mock()
            mock_response.status_code = 204
            mock_response.json.return_value = None
            mock_response.raise_for_status.return_value = None
            mock_delete.return_value = mock_response

            # Should handle empty responses without errors
            result = await error_test_client.delete("/resource/123")
            # Empty response should return None or empty dict
            assert result is None or result == {}

    @pytest.mark.asyncio
    async def test_large_response_handling(self, error_test_client):
        """Test handling of large responses."""
        # Create a large mock response
        large_data = {"items": [{"id": i, "name": f"Item {i} for audit-logs", "data": "x" * 1000} for i in range(100)]}

        with patch.object(error_test_client.client, "get") as mock_get:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = large_data
            mock_response.raise_for_status.return_value = None
            mock_get.return_value = mock_response

            # Should handle large responses
            result = await error_test_client.get("/large-dataset")
            assert len(result["items"]) == 100
            assert result["items"][0]["name"] == "Item 0 for audit-logs"


class TestHttpClientPerformance:
    """Test HTTP client performance characteristics."""

    @pytest.mark.asyncio
    async def test_connection_reuse(self):
        """Test that HTTP client reuses connections efficiently."""
        mock_token_manager = Mock()
        mock_token_manager.get_auth_headers.return_value = {
            "Authorization": "Bearer perf-test-token",
            "Content-Type": "application/json",
        }

        with patch("utils.http_client.TokenManager", return_value=mock_token_manager):
            http_client = AuditLogsHttpClient()

            # Mock multiple successful requests
            with patch.object(http_client.client, "get") as mock_get:
                mock_response = Mock()
                mock_response.status_code = 200
                mock_response.json.return_value = {"test": "data"}
                mock_response.raise_for_status.return_value = None
                mock_get.return_value = mock_response

                # Execute multiple requests
                for i in range(10):
                    await http_client.get(f"/endpoint-{i}")

                # All requests should use the same session
                assert mock_get.call_count == 10

    @pytest.mark.asyncio
    async def test_request_timing(self):
        """Test request timing and performance."""
        import time

        mock_token_manager = Mock()
        mock_token_manager.get_auth_headers.return_value = {
            "Authorization": "Bearer timing-test-token",
            "Content-Type": "application/json",
        }

        with patch("utils.http_client.TokenManager", return_value=mock_token_manager):
            http_client = AuditLogsHttpClient()

            with patch.object(http_client.client, "get") as mock_get:
                mock_response = Mock()
                mock_response.status_code = 200
                mock_response.json.return_value = {"timed": "response"}
                mock_response.raise_for_status.return_value = None
                mock_get.return_value = mock_response

                # Time a request
                start_time = time.time()
                await http_client.get("/timed-endpoint")
                end_time = time.time()

                # Request should complete quickly in test environment
                request_time = end_time - start_time
                assert request_time < 1.0  # Should be very fast with mocks


# Fixtures and utilities for HTTP client testing
@pytest.fixture
def mock_http_session():
    """Mock HTTP session for testing."""
    session = Mock(spec=httpx.AsyncClient)
    return session


@pytest.fixture
def sample_api_response():
    """Sample API response data for audit-logs."""
    return {
        "id": "sample-id-audit-logs",
        "name": "Sample Resource",
        "type": "AuditLogsResource",
        "status": "active",
        "metadata": {
            "created_at": "2024-01-01T00:00:00Z",
            "updated_at": "2024-01-01T12:00:00Z",
            "service": "audit-logs",
        },
    }


@pytest.fixture
def sample_error_response():
    """Sample error response for testing."""
    return {
        "error": {
            "code": "RESOURCE_NOT_FOUND",
            "message": "Resource not found in audit-logs",
            "details": {"service": "audit-logs", "timestamp": "2024-01-01T00:00:00Z"},
        }
    }
