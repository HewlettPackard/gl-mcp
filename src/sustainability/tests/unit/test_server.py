# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""Unit tests for the Sustainability_Insight_Center MCP server."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest

from mcp.types import Tool
from server.mcp_server import MCPServer


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_fastmcp_tool(name: str, description: str = "Test tool") -> MagicMock:
    """Return a mock that looks like a FastMCP FunctionTool."""
    tool = MagicMock()
    tool.name = name
    tool.description = description
    tool.to_tool_definition.return_value = Tool(
        name=name,
        description=description,
        inputSchema={"type": "object", "properties": {}},
    )
    return tool


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_initialize_populates_tools_from_fastmcp(mock_http_client):
    """MCPServer.initialize() should read back tools registered with FastMCP."""
    server = MCPServer()

    dummy_tool = _make_fastmcp_tool("dummy")

    with (
        patch("server.mcp_server.get_http_client", return_value=mock_http_client),
        patch("server.mcp_server.get_tool_classes", return_value=[]),
    ):
        # Pre-seed FastMCP's tool manager so initialize() can read it back
        server.mcp._tool_manager._tools = {"dummy": dummy_tool}
        await server.initialize()

    assert "dummy" in server.tools
    assert server.http_client is mock_http_client


@pytest.mark.asyncio
async def test_get_tools_returns_protocol_objects():
    """MCPServer.get_tools() should return mcp.types.Tool objects."""
    server = MCPServer()
    server.tools = {"dummy": _make_fastmcp_tool("dummy")}

    tools = await server.get_tools()

    assert tools
    assert tools[0].name == "dummy"
    assert tools[0].inputSchema["type"] == "object"


@pytest.mark.asyncio
async def test_shutdown_closes_http_client(mock_http_client):
    """MCPServer.shutdown() should close the HTTP client."""
    server = MCPServer()
    server.http_client = mock_http_client

    await server.shutdown()

    mock_http_client.close.assert_awaited_once()
