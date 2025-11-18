# (c) Copyright 2025 Hewlett Packard Enterprise Development LP
"""
MCP server implementation for devices.

This module implements the main MCP server class and request handling.
"""

import json
from typing import Any, Sequence

from mcp.server import Server
from mcp.types import Tool, TextContent, ImageContent, EmbeddedResource

# Import local components
from config.settings import settings
from config.logging import get_logger
from tools.registry import get_tools
from utils.http_client import get_http_client

logger = get_logger(__name__)


class MCPServer:
    """MCP server for devices."""

    def __init__(self):
        """Initialize the MCP server."""
        self.settings = settings
        self.server = Server("devices-mcp")
        self.tools = {}
        # CRITICAL: Use lazy initialization to avoid authentication at import time
        self.http_client = None

    async def initialize(self) -> None:
        """Initialize server components."""
        try:
            # Initialize HTTP client lazily
            if self.http_client is None:
                self.http_client = get_http_client()

            # Register tools
            await self._register_tools()

            # Register MCP handlers
            self._register_handlers()

        except Exception as e:
            logger.error(f"Failed to initialize MCP server: {e}")
            raise

    async def _register_tools(self) -> None:
        """Register MCP tools."""
        try:
            # Ensure HTTP client is initialized
            if self.http_client is None:
                raise RuntimeError("HTTP client not initialized")

            # Get all available tools
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

                # Convert result to MCP format with proper JSON serialization
                if isinstance(result, str):
                    text = result
                else:
                    # Properly serialize to JSON instead of using str()
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
        """
        Gracefully shutdown server components.

        This method cleans up all resources including HTTP connections,
        ensuring no resource leaks occur during container termination.

        Called automatically by the shutdown handler when SIGTERM or SIGINT is received.
        """
        try:
            logger.info("Initiating server shutdown sequence...")

            # Close HTTP client if it exists
            if hasattr(self, "http_client") and self.http_client:
                logger.debug("Closing HTTP client connections...")
                try:
                    await self.http_client.close()
                    logger.debug("HTTP client closed successfully")
                except Exception as e:
                    logger.error(f"Error closing HTTP client: {str(e)}")

            # Clear tool instances to release references
            if hasattr(self, "tools"):
                logger.debug(f"Clearing {len(self.tools)} tool instances...")
                self.tools.clear()

            logger.info("Server shutdown sequence complete")

        except Exception as e:
            logger.error(f"Error during shutdown: {str(e)}", exc_info=True)


# CRITICAL: Do NOT create global instances - let app.py handle instantiation
