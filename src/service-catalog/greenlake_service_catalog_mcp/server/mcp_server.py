# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
MCP server implementation for service-catalog.

This module provides the MCPServer wrapper class used for testing and programmatic
lifecycle control.  In production the server is driven entirely through the
module-level ``mcp`` FastMCP instance defined in server.fastmcp_instance; this
class is kept for backward-compatibility and test isolation.
"""

from __future__ import annotations

from typing import Any

from mcp.types import Tool

from greenlake_service_catalog_mcp.config.logging import get_logger
from greenlake_service_catalog_mcp.server.fastmcp_instance import mcp  # noqa: F401  (re-exported for convenience)
from greenlake_service_catalog_mcp.tools.registry import get_tool_classes
from greenlake_service_catalog_mcp.utils.http_client import get_http_client

logger = get_logger(__name__)


class MCPServer:
    """
    Thin wrapper around FastMCP for testing and programmatic lifecycle control.

    In normal operation FastMCP drives the server via the lifespan context in
    fastmcp_instance.py.  Instantiate this class in tests that need to inspect
    tool objects without running the full FastMCP runtime.
    """

    def __init__(self) -> None:
        # Canonical FastMCP instance – use this for everything
        self.mcp = mcp
        # Kept for backward-compatibility with code that references self.server
        self.server = mcp
        self.tools: dict[str, Any] = {}
        self.http_client: Any = None

    async def initialize(self) -> None:
        """
        Eagerly initialise HTTP client and trigger tool registrations.

        Only needed in tests or when you require direct access to the registered
        tool list without running the full FastMCP runtime.  In production,
        FastMCP's lifespan context manager handles initialisation transparently
        – see server.fastmcp_instance._lifespan.
        """
        if self.http_client is None:
            self.http_client = get_http_client()

        # Import tool modules – each @mcp.tool() decorator fires on import and
        # registers the function with the FastMCP instance.
        get_tool_classes()

        # Populate self.tools for test introspection by reading back what
        # FastMCP registered.  We access the private tool manager because
        # FastMCP has no sync public API for listing tools outside a running
        # session.  This is intentionally limited to test/introspection use.
        try:
            raw = self.mcp._tool_manager._tools  # type: ignore[attr-defined]
            self.tools = dict(raw)
        except AttributeError:
            self.tools = {}

        logger.info(f"MCPServer initialised with {len(self.tools)} tools")

    async def get_tools(self) -> list[Tool]:
        """Return registered tools as MCP protocol Tool objects.

        FastMCP's internal ``FunctionTool`` objects expose
        ``to_tool_definition()`` which produces the canonical
        ``mcp.types.Tool``.  A minimal fallback is used for any tool whose
        internal representation differs across FastMCP versions.
        """
        result: list[Tool] = []
        for name, tool in self.tools.items():
            try:
                # FastMCP FunctionTool public conversion helper
                result.append(tool.to_tool_definition())
            except AttributeError:
                result.append(
                    Tool(
                        name=name,
                        description=getattr(tool, "description", "") or "",
                        inputSchema={"type": "object", "properties": {}},
                    )
                )
        return result

    async def shutdown(self) -> None:
        """Gracefully shut down server components."""
        if self.http_client is not None:
            logger.info("Closing HTTP client...")
            try:
                await self.http_client.close()
            except Exception as exc:
                logger.error(f"Error closing HTTP client: {exc}")
        self.tools.clear()
        logger.info("MCPServer shutdown complete")


# CRITICAL: Do NOT create global instances – app.py drives the server lifecycle
