# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
Application entry point for service-catalog MCP server.

Starts the FastMCP server with stdio transport. FastMCP handles the event loop,
signal handling (SIGTERM/SIGINT), and the application lifespan (HTTP client
setup/teardown) defined in server.fastmcp_instance.
"""

import sys

# CRITICAL: Setup logging FIRST, before any other imports that might create loggers.
# All loggers must write to stderr so stdout is kept clean for the MCP protocol.
from greenlake_service_catalog_mcp.config.logging import setup_logging

setup_logging()

from greenlake_service_catalog_mcp.config.logging import get_logger, flush_logs  # noqa: E402
from greenlake_service_catalog_mcp.server.fastmcp_instance import mcp  # noqa: E402

from greenlake_service_catalog_mcp.tools.registry import get_tool_classes  # noqa: E402

logger = get_logger(__name__)


def main() -> None:
    """Run the service-catalog MCP server over stdio."""
    logger.info("Starting service-catalog MCP server (stdio transport)...")
    # Calling get_tool_classes() triggers the side-effect imports that execute every
    # @mcp.tool() decorator, registering all tools with the FastMCP instance before
    # the server starts serving requests.
    get_tool_classes()
    try:
        # mcp.run() is synchronous – it calls asyncio.run() internally,
        # handles SIGTERM/SIGINT gracefully, and invokes the lifespan context.
        mcp.run(transport="stdio")
    except KeyboardInterrupt:
        # FastMCP already handles Ctrl-C; this is a safety catch.
        pass
    except Exception as exc:
        logger.error(f"Fatal server error: {exc}", exc_info=True)
        sys.exit(1)
    finally:
        flush_logs()


if __name__ == "__main__":
    main()
