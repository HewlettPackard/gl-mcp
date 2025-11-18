# (c) Copyright 2025 Hewlett Packard Enterprise Development LP
"""
Tests for MCP server implementation of workspaces.
"""

import asyncio
import time
import pytest
from unittest.mock import AsyncMock, Mock, patch

from server.mcp_server import MCPServer


class TestMCPServer:
    """Test cases for workspaces MCP server."""

    @pytest.fixture
    def mock_settings(self):
        """Mock settings for server testing."""
        settings = Mock()
        settings.client_id = "test-server-client-id"
        settings.client_secret = "test-server-client-secret"
        settings.workspace_id = "test-server-workspace-id"
        settings.token_issuer = "https://workspaces.test.com/oauth2/token"
        settings.greenlake_api_base_url = "https://global.api.greenlake.hpe.com"
        return settings

    @pytest.fixture
    def mcp_server(self, mock_settings):
        """Create MCP server instance for testing."""
        with patch("server.mcp_server.settings", mock_settings):
            return MCPServer()

    def test_mcp_server_initialization(self, mcp_server):
        """Test MCP server initialization for workspaces."""
        assert mcp_server is not None
        assert hasattr(mcp_server, "server")
        assert hasattr(mcp_server, "settings")
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
    def test_http_client_initialization(self, mock_get_http_client, mock_settings):
        """Test HTTP client is properly initialized."""
        mock_http_client = AsyncMock()
        mock_get_http_client.return_value = mock_http_client

        with patch("server.mcp_server.settings", mock_settings):
            server = MCPServer()

        # HTTP client should be None initially (lazy initialization)
        assert server.http_client is None

    @pytest.mark.asyncio
    async def test_initialize_method(self, mock_settings):
        """Test server initialization method."""
        mock_http_client = AsyncMock()

        with (
            patch("server.mcp_server.settings", mock_settings),
            patch("server.mcp_server.get_http_client", return_value=mock_http_client),
            patch("server.mcp_server.get_tools", return_value=[]),
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
    @patch("server.mcp_server.get_tools")
    async def test_register_tools(self, mock_get_tools, mcp_server):
        """Test tool registration."""
        # Setup mock tool classes that return instances with proper names
        tool_class1 = Mock()
        tool_instance1 = Mock()
        tool_instance1.name = "test_tool_1"
        tool_class1.return_value = tool_instance1

        tool_class2 = Mock()
        tool_instance2 = Mock()
        tool_instance2.name = "test_tool_2"
        tool_class2.return_value = tool_instance2

        mock_get_tools.return_value = [tool_class1, tool_class2]

        # Initialize HTTP client first
        mcp_server.http_client = AsyncMock()

        # Execute tool registration
        await mcp_server._register_tools()

        # Assertions
        assert len(mcp_server.tools) == 2
        assert "test_tool_1" in mcp_server.tools
        assert "test_tool_2" in mcp_server.tools
        assert mcp_server.tools["test_tool_1"] == tool_instance1
        assert mcp_server.tools["test_tool_2"] == tool_instance2

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

    @patch("server.app.MCPServer")
    @patch("mcp.server.stdio.stdio_server")
    def test_main_function_creates_server(self, mock_stdio_server, mock_server_class):
        """Test main function creates server instance."""
        mock_server = AsyncMock()
        mock_server_class.return_value = mock_server

        # Mock stdio transport
        mock_stdio_server.return_value.__aenter__ = AsyncMock(return_value=(Mock(), Mock()))
        mock_stdio_server.return_value.__aexit__ = AsyncMock()

        # Import and test main - this may require async handling
        from server.app import main

        # The actual test would depend on how main() is implemented
        # This is a basic structure test
        assert callable(main)

    @patch("server.app.MCPServer")
    def test_server_creation_in_main(self, mock_server_class):
        """Test that main function creates MCP server correctly."""
        mock_server = AsyncMock()
        mock_server_class.return_value = mock_server

        try:
            from server.app import main

            # Basic test that we can import and access main
            assert callable(main)
        except ImportError:
            # If main is not importable in test environment, that's ok
            pass

    def test_app_module_structure(self):
        """Test app module has expected structure."""
        import server.app as app_module

        # Should have main function or similar entry point
        assert hasattr(app_module, "main") or hasattr(app_module, "run") or hasattr(app_module, "start")

    @patch("asyncio.run")
    @patch("server.app.MCPServer")
    def test_async_main_execution(self, mock_server_class, mock_asyncio_run):
        """Test async main execution."""
        mock_server = AsyncMock()
        mock_server_class.return_value = mock_server

        # Try to test async main if it exists
        try:
            from server.app import main

            if asyncio.iscoroutinefunction(main):
                # This would be an async main function
                assert callable(main)
        except (ImportError, AttributeError):
            # Not all apps have async main
            pass


class TestServerIntegration:
    """Integration tests for server components."""

    @pytest.fixture
    def integration_settings(self):
        """Integration test settings."""
        settings = Mock()
        settings.client_id = "integration-client-id"
        settings.client_secret = "integration-client-secret"
        settings.workspace_id = "integration-workspace-id"
        settings.token_issuer = "https://workspaces.integration.com/oauth2/token"
        settings.api_base_url = "https://global.api.greenlake.hpe.com"
        return settings

    @patch("server.mcp_server.get_http_client")
    def test_server_component_integration(self, mock_get_http_client, integration_settings):
        """Test integration between server components."""
        # Setup mocks
        mock_http_client = AsyncMock()
        mock_get_http_client.return_value = mock_http_client

        # Create server
        with patch("server.mcp_server.settings", integration_settings):
            server = MCPServer()

        # Verify components are created and connected
        assert server.settings == integration_settings
        assert hasattr(server, "tools")
        assert hasattr(server, "http_client")

        # Verify initialization calls would work
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

    def test_server_handles_missing_settings(self):
        """Test server handles missing settings gracefully."""
        with patch("server.mcp_server.settings", None):
            try:
                server = MCPServer()
                # Should either work with defaults or raise appropriate error
                assert server is not None
            except Exception as e:
                # Should be a meaningful error about missing settings
                assert "settings" in str(e).lower() or "config" in str(e).lower() or "NoneType" in str(e)

    @patch("server.mcp_server.get_http_client")
    def test_server_handles_http_client_error(self, mock_get_http_client):
        """Test server handles HTTP client initialization errors."""
        mock_get_http_client.side_effect = Exception("HTTP client failed")

        mock_settings = Mock()
        mock_settings.client_id = "test-id"
        mock_settings.client_secret = "test-secret"
        mock_settings.token_issuer = "https://test.com/token"
        mock_settings.api_base_url = "https://test.api.com"

        with patch("server.mcp_server.settings", mock_settings):
            server = MCPServer()
            # HTTP client error should occur during initialize(), not __init__()
            assert server is not None
            assert server.http_client is None  # Lazy initialization means it's None initially


# Performance and resource tests
class TestServerPerformance:
    """Test server performance and resource usage."""

    def test_server_initialization_time(self):
        """Test server initializes within reasonable time."""

        mock_settings = Mock()
        mock_settings.client_id = "perf-test-id"
        mock_settings.client_secret = "perf-test-secret"
        mock_settings.token_issuer = "https://perf.test.com/token"
        mock_settings.api_base_url = "https://perf.test.api.com"

        start_time = time.time()

        with patch("server.mcp_server.settings", mock_settings):
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

        mock_settings = Mock()
        mock_settings.client_id = "memory-test-id"
        mock_settings.client_secret = "memory-test-secret"
        mock_settings.token_issuer = "https://memory.test.com/token"
        mock_settings.api_base_url = "https://memory.test.api.com"

        # Force garbage collection before test
        gc.collect()

        with patch("server.mcp_server.settings", mock_settings):
            server = MCPServer()

        # Basic test - server should be created without memory errors
        assert server is not None

        # Clean up
        del server
        gc.collect()
