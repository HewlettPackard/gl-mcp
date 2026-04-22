# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
FastMCP server instance and application lifespan for service-catalog.

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

    http_client: Any  # ServiceCatalogHttpClient


@asynccontextmanager
async def _lifespan(server: FastMCP) -> AsyncIterator[AppContext]:
    """
    Manage the lifecycle of shared application resources.

    Runs once at server startup (before any tool call) and once at shutdown.
    Yields an AppContext that FastMCP injects into every tool via ctx.request_context.lifespan_context.
    """
    # Lazy imports keep this module free of circular dependencies
    from greenlake_service_catalog_mcp.utils.http_client import get_http_client  # noqa: PLC0415
    from greenlake_service_catalog_mcp.config.logging import get_logger  # noqa: PLC0415

    log = get_logger(__name__)
    log.info("Initialising service-catalog HTTP client...")

    http_client = get_http_client()
    try:
        log.info("service-catalog MCP server ready")
        yield AppContext(http_client=http_client)
    finally:
        log.info("Shutting down service-catalog HTTP client...")
        await http_client.close()
        log.info("HTTP client closed")


# ---------------------------------------------------------------------------
# Module-level FastMCP instance
# ---------------------------------------------------------------------------
# Import this instance in tool modules to register tools with @mcp.tool().
# Example:
#   from greenlake_service_catalog_mcp.server.fastmcp_instance import mcp
#
#   @mcp.tool()
#   async def list_service_catalog_items(ctx: Context, ...) -> ...:
#       http_client = ctx.request_context.lifespan_context.http_client
#       ...
# ---------------------------------------------------------------------------
mcp: FastMCP = FastMCP(
    "service-catalog-mcp",
    instructions=(
        ""
        "The HPE GreenLake for Service Catalog service offers a collection of RESTful APIs to fetch, provision service managers and to delete a service manager provisioned in a workspace."
        ""
    ),
    lifespan=_lifespan,
)
