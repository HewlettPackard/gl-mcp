# (c) Copyright 2025 Hewlett Packard Enterprise Development LP
"""End-to-End tests for workspaces MCP Server.

test_server_health: Verifies that the server initializes correctly and can establish a session
test_list_tools: Validates that the server properly lists all available tools

Usage:
    pytest -xvs tests/e2e/test_e2e.py
"""

import asyncio

import pytest

from tests.e2e.mcp_test_utils import (
    check_credentials,
    cleanup_mcp_session,
    create_mcp_session,
)

# Skip all tests if credentials are missing
missing_credentials = check_credentials()
pytestmark = pytest.mark.skipif(
    missing_credentials is not None,
    reason=f"Missing required environment variables: {missing_credentials}",
)


class TestHpeGreenlakeForWorkspaceManagementApiMCPServerE2E:
    """End-to-End tests for the workspaces MCP server.

    These tests start the actual MCP server and connect to it using a real MCP client.
    """

    @pytest.mark.asyncio
    async def test_server_health(self):
        """Test that the server is healthy by checking if we can initialize a session."""
        session = None
        session_cm = None
        stdio_transport = None
        stdio_client_cm = None
        process = None

        try:
            # Create a session for this test
            session, session_cm, stdio_transport, stdio_client_cm, process = await create_mcp_session("server.app")
            print("MCP session initialized successfully")

            # If we got this far, the session was initialized successfully
            assert session is not None, "Session should be initialized"

        except Exception as e:
            pytest.fail(f"Failed to initialize MCP session: {str(e)}")
        finally:
            # Clean up
            if session:
                await cleanup_mcp_session(session, session_cm, stdio_transport, stdio_client_cm, process)

    @pytest.mark.asyncio
    async def test_list_tools(self):
        """Test that the server properly lists available tools."""
        session = None
        session_cm = None
        stdio_transport = None
        stdio_client_cm = None
        process = None

        try:
            # Create a session for this test
            session, session_cm, stdio_transport, stdio_client_cm, process = await create_mcp_session("server.app")
            print("MCP session initialized successfully")

            # Get available tools with a timeout
            try:
                # Wrap the call in asyncio.wait_for for a timeout
                tools_response = await asyncio.wait_for(
                    session.list_tools(),
                    timeout=10.0,  # 10 second timeout
                )

                # Convert tools to a dictionary for easier checking
                tools = {tool.name: tool for tool in tools_response.tools}

                # Verify that at least some tools are available
                assert len(tools) > 0, "Server should provide at least one tool"

                # Print available tools for debugging
                print(f"Available tools: {list(tools.keys())}")

                # For static mode, verify that we have at least some tools
                # The actual tool names will depend on the OpenAPI spec
                assert len(tools) >= 1, "Should have at least one tool in static mode"
                # You can add specific tool assertions based on your OpenAPI spec if needed

            except asyncio.TimeoutError:
                pytest.fail("Timed out waiting for list_tools response")

        except Exception as e:
            pytest.fail(f"Failed to list tools: {str(e)}")
        finally:
            # Clean up
            if session:
                await cleanup_mcp_session(session, session_cm, stdio_transport, stdio_client_cm, process)


if __name__ == "__main__":
    pytest.main(["-xvs", __file__])
