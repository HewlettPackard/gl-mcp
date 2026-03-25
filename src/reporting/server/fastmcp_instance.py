# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
FastMCP server instance and application lifespan for reporting.

This module is the single source of truth for the FastMCP instance.
Keeping it separate from mcp_server.py breaks the potential circular-import
cycle: tools/ can import `mcp` from here without pulling in the rest of the
server package.
"""

from __future__ import annotations

from contextlib import asynccontextmanager
from dataclasses import dataclass
from typing import Any, AsyncIterator

from mcp.server.fastmcp import FastMCP


@dataclass
class AppContext:
    """
    Application-level context shared across all tool invocations.

    Passed via FastMCP's lifespan mechanism so every tool can access shared
    resources (HTTP client, caches, etc.) without global state or re-creation.
    """

    http_client: Any  # ReportingHttpClient


@asynccontextmanager
async def _lifespan(server: FastMCP) -> AsyncIterator[AppContext]:
    """
    Manage the lifecycle of shared application resources.

    Runs once at server startup (before any tool call) and once at shutdown.
    Yields an AppContext that FastMCP injects into every tool via ctx.request_context.lifespan_context.
    """
    # Lazy imports keep this module free of circular dependencies
    from utils.http_client import get_http_client  # noqa: PLC0415
    from config.logging import get_logger  # noqa: PLC0415

    log = get_logger(__name__)
    log.info("Initialising reporting HTTP client...")

    http_client = get_http_client()
    try:
        log.info("reporting MCP server ready")
        yield AppContext(http_client=http_client)
    finally:
        log.info("Shutting down reporting HTTP client...")
        await http_client.close()
        log.info("HTTP client closed")


# ---------------------------------------------------------------------------
# Module-level FastMCP instance
# ---------------------------------------------------------------------------
# Import this instance in tool modules to register tools with @mcp.tool().
# Example:
#   from server.fastmcp_instance import mcp
#
#   @mcp.tool()
#   async def list_reporting_items(ctx: Context, ...) -> ...:
#       http_client = ctx.request_context.lifespan_context.http_client
#       ...
# ---------------------------------------------------------------------------
mcp: FastMCP = FastMCP(
    "reporting-mcp",
    instructions=(
        ""
        "The HPE GreenLake for Reporting service provides a collection of RESTful APIs for generating reports, retrieving supported columns and filters, monitoring asynchronous operations, and querying the status of reports."
        ""
    ),
    lifespan=_lifespan,
)
