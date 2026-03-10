# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
MCP server implementation for sustainability.

This module implements the main MCP server class and request handling.
"""

import json
from typing import Any, Sequence

from mcp.server import Server
from mcp.types import Tool, TextContent, ImageContent, EmbeddedResource

from config.settings import settings
from config.logging import get_logger
from tools.registry import get_tools
from utils.http_client import get_http_client

logger = get_logger(__name__)


class MCPServer:
    """MCP server for sustainability."""

    def __init__(self):
        """Initialize the MCP server."""
        self.settings = settings
        self.server = Server("sustainability-mcp")
        self.tools = {}
        self.http_client = None

    async def initialize(self) -> None:
        """Initialize server components."""
        try:
            if self.http_client is None:
                self.http_client = get_http_client()

            await self._register_tools()
            self._register_handlers()

        except Exception as e:
            logger.error(f"Failed to initialize MCP server: {e}")
            raise

    async def _register_tools(self) -> None:
        """Register MCP tools."""
        try:
            if self.http_client is None:
                raise RuntimeError("HTTP client not initialized")

            tool_classes = get_tools()

            for tool_class in tool_classes:
                tool_instance = tool_class(self.http_client)
                self.tools[tool_instance.name] = tool_instance

        except Exception as e:
            logger.error(f"Failed to register tools: {str(e)}", exc_info=True)
            raise

    def _register_handlers(self) -> None:
        """Register MCP protocol handlers."""

        @self.server.list_tools()
        async def handle_list_tools() -> list[Tool]:
            """Handle list_tools requests."""
            return await self.get_tools()

        @self.server.call_tool()
        async def handle_call_tool(
            name: str, arguments: dict[str, Any]
        ) -> Sequence[TextContent | ImageContent | EmbeddedResource]:
            """Handle tool calls."""
            if name not in self.tools:
                raise ValueError(f"Unknown tool: {name}")

            try:
                result = await self.tools[name].execute(arguments)

                if isinstance(result, str):
                    text = result
                else:
                    text = json.dumps(result, indent=2, ensure_ascii=False)

                return [TextContent(type="text", text=text)]

            except Exception as e:
                logger.error(f"Tool execution failed: {str(e)}", exc_info=True)
                error_msg = f"Error executing tool {name}: {str(e)}"
                return [TextContent(type="text", text=error_msg)]

    async def get_tools(self) -> list[Tool]:
        """Get list of available tools."""
        tool_list = []

        for tool in self.tools.values():
            tool_list.append(
                Tool(
                    name=tool.name,
                    description=tool.description,
                    inputSchema=tool.input_schema,
                )
            )

        return tool_list

    async def shutdown(self) -> None:
        """Gracefully shutdown server components."""
        try:
            logger.info("Initiating server shutdown sequence...")

            if hasattr(self, "http_client") and self.http_client:
                logger.debug("Closing HTTP client connections...")
                try:
                    await self.http_client.close()
                    logger.debug("HTTP client closed successfully")
                except Exception as e:
                    logger.error(f"Error closing HTTP client: {str(e)}")

            if hasattr(self, "tools"):
                logger.debug(f"Clearing {len(self.tools)} tool instances...")
                self.tools.clear()

            logger.info("Server shutdown sequence complete")

        except Exception as e:
            logger.error(f"Error during shutdown: {str(e)}", exc_info=True)


# CRITICAL: Do NOT create global instances - let app.py handle instantiation
