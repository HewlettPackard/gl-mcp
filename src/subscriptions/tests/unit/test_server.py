# (c) Copyright 2025 Hewlett Packard Enterprise Development LP
"""Unit tests for the subscriptions MCP server."""

from __future__ import annotations

from unittest.mock import AsyncMock, patch

import pytest

from server.mcp_server import MCPServer


class _DummyTool:
    """Minimal tool used to exercise registration logic."""

    def __init__(self, http_client) -> None:
        self._http_client = http_client

    @property
    def name(self) -> str:
        return "dummy"

    @property
    def description(self) -> str:
        return "Tool used in unit tests."

    @property
    def input_schema(self) -> dict:
        return {"type": "object", "properties": {}}

    async def execute(self, arguments):
        return [{"success": True, "tool": self.name, "result": arguments}]


@pytest.mark.asyncio
async def test_initialize_registers_tools(mock_http_client):
    server = MCPServer()
    with (
        patch("server.mcp_server.get_http_client", return_value=mock_http_client),
        patch("server.mcp_server.get_tools", return_value=[_DummyTool]),
    ):
        await server.initialize()

    assert "dummy" in server.tools
    assert server.http_client is mock_http_client


@pytest.mark.asyncio
async def test_get_tools_returns_protocol_objects():
    server = MCPServer()
    server.tools = {"dummy": _DummyTool(AsyncMock())}

    tools = await server.get_tools()

    assert tools
    assert tools[0].name == "dummy"
    assert tools[0].inputSchema["type"] == "object"


@pytest.mark.asyncio
async def test_shutdown_closes_http_client(mock_http_client):
    server = MCPServer()
    server.http_client = mock_http_client

    await server.shutdown()

    mock_http_client.close.assert_awaited_once()
