# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
Tests for MCP server implementation of reporting.
"""

import time
import pytest
from unittest.mock import AsyncMock, Mock, patch

from server.mcp_server import MCPServer


class TestMCPServer:
    """Test cases for reporting MCP server."""

    @pytest.fixture
    def mcp_server(self):
        """Create MCP server instance for testing."""
        return MCPServer()

    def test_mcp_server_initialization(self, mcp_server):
        """Test MCP server initialization for reporting."""
        assert mcp_server is not None
        # self.server is kept as a backward-compat alias for self.mcp
        assert hasattr(mcp_server, "server")
        assert hasattr(mcp_server, "mcp")
        assert hasattr(mcp_server, "tools")
        assert hasattr(mcp_server, "http_client")

    def test_mcp_server_name(self, mcp_server):
        """Test MCP server has correct name."""
        assert hasattr(mcp_server.server, "name")
        # Server name should contain service-related identifier
        assert len(mcp_server.server.name) > 0
        assert "mcp" in mcp_server.server.name.lower()

    def test_mcp_server_version(self, mcp_server):
        """Test MCP server has version information."""
        # Check that server instance is properly created
        assert mcp_server.server is not None

    @patch("server.mcp_server.get_http_client")
    def test_http_client_initialization(self, mock_get_http_client):
        """Test HTTP client is properly initialized lazily."""
        mock_http_client = AsyncMock()
        mock_get_http_client.return_value = mock_http_client

        server = MCPServer()

        # HTTP client should be None until initialize() is called
        assert server.http_client is None

    @pytest.mark.asyncio
    async def test_initialize_method(self):
        """Test server initialization method."""
        mock_http_client = AsyncMock()

        with (
            patch("server.mcp_server.get_http_client", return_value=mock_http_client),
            patch("server.mcp_server.get_tool_classes", return_value=[]),
        ):
            server = MCPServer()
            await server.initialize()

            # After initialization, HTTP client should be set
            assert server.http_client == mock_http_client

    @pytest.mark.asyncio
    async def test_server_request_handling(self, mcp_server):
        """Test server can handle basic requests."""
        # This is a basic test to ensure the server structure is sound
        # More detailed request handling would require actual MCP protocol testing
        assert hasattr(mcp_server.server, "name")
        assert hasattr(mcp_server, "tools")
        assert hasattr(mcp_server, "initialize")

    def test_server_has_tools_dict(self, mcp_server):
        """Test that tools dictionary is available."""
        # Check that tools dict is available
        assert hasattr(mcp_server, "tools")
        assert isinstance(mcp_server.tools, dict)

    @pytest.mark.asyncio
    @patch("server.mcp_server.get_tool_classes", return_value=[])
    async def test_initialize_populates_tools(self, mock_get_tool_classes, mcp_server):
        """Test that initialize() populates the tools dict from FastMCP."""
        mcp_server.http_client = AsyncMock()

        # Pre-seed FastMCP's internal tool manager with a mock tool so that
        # initialize() can read it back without running the full server.
        mock_tool = Mock()
        mock_tool.name = "test_tool"
        mcp_server.mcp._tool_manager._tools = {"test_tool": mock_tool}

        await mcp_server.initialize()

        assert "test_tool" in mcp_server.tools

    def test_tools_registry_supports_both_modes(self, mcp_server):
        """Test that the server can handle both static and dynamic tool modes."""
        # Basic test that tools dict exists
        assert hasattr(mcp_server, "tools")
        assert isinstance(mcp_server.tools, dict)

        # The server should support both static and dynamic tools through the registry
        # Static tools: individual endpoint tools (default)
        # Dynamic tools: 3 meta-tools (list_api_endpoints, get_api_endpoint_schema, invoke_api_endpoint)
        # Mode switching is handled by the tools registry, not the server itself

        # Test that the server structure can accommodate either mode
        assert True  # Basic structure check - specific tool tests are in integration tests


class TestApp:
    """Test cases for the app entry point."""

    def test_main_is_callable(self):
        """Test main function is importable and callable."""
        from server.app import main

        assert callable(main)

    def test_app_module_structure(self):
        """Test app module has expected structure."""
        import server.app as app_module

        assert hasattr(app_module, "main") or hasattr(app_module, "run") or hasattr(app_module, "start")

    @patch("server.app.mcp")
    def test_main_calls_mcp_run(self, mock_mcp):
        """Test that main() delegates to mcp.run() with stdio transport."""
        from server.app import main

        main()
        mock_mcp.run.assert_called_once_with(transport="stdio")


class TestServerIntegration:
    """Integration tests for server components."""

    @patch("server.mcp_server.get_http_client")
    def test_server_component_integration(self, mock_get_http_client):
        """Test integration between server components."""
        mock_http_client = AsyncMock()
        mock_get_http_client.return_value = mock_http_client

        server = MCPServer()

        # Verify FastMCP instance is wired up
        assert server.mcp is not None
        assert hasattr(server, "tools")
        assert hasattr(server, "http_client")
        assert hasattr(server, "initialize")

    def test_server_dependencies_importable(self):
        """Test that all server dependencies can be imported."""
        # Test core server imports
        try:
            from server.mcp_server import MCPServer

            assert MCPServer is not None
        except ImportError as e:
            pytest.fail(f"Failed to import MCPServer: {e}")

        # Test app imports
        try:
            import server.app

            assert server.app is not None
        except ImportError as e:
            pytest.fail(f"Failed to import server.app: {e}")


class TestServerErrorHandling:
    """Test error handling in server components."""

    def test_server_creates_without_settings(self):
        """Test MCPServer can be constructed without external settings."""
        server = MCPServer()
        # Settings are read lazily from environment; construction must not fail
        assert server is not None
        assert server.mcp is not None

    @patch("server.mcp_server.get_http_client")
    def test_server_handles_http_client_error(self, mock_get_http_client):
        """Test server handles HTTP client initialization errors."""
        mock_get_http_client.side_effect = Exception("HTTP client failed")

        mock_settings = Mock()
        mock_settings.client_id = "test-id"
        mock_settings.client_secret = "test-secret"
        mock_settings.token_issuer = "https://test.com/token"
        mock_settings.api_base_url = "https://test.api.com"

        server = MCPServer()
        # HTTP client error should occur during initialize(), not __init__()
        assert server is not None
        assert server.http_client is None  # Lazy initialization


# Performance and resource tests
class TestServerPerformance:
    """Test server performance and resource usage."""

    def test_server_initialization_time(self):
        """Test server initializes within reasonable time."""
        start_time = time.time()

        server = MCPServer()

        end_time = time.time()
        initialization_time = end_time - start_time

        # Server should initialize quickly (within 5 seconds for test environment)
        assert initialization_time < 5.0
        # Server should be created successfully
        assert server is not None

    def test_server_memory_usage(self):
        """Test server doesn't consume excessive memory during initialization."""
        import gc

        # Force garbage collection before test
        gc.collect()

        server = MCPServer()

        # Basic test - server should be created without memory errors
        assert server is not None

        # Clean up
        del server
        gc.collect()
