# (c) Copyright 2025 Hewlett Packard Enterprise Development LP
"""
Application entry point for audit-logs MCP server.

This module initializes and runs the MCP server.
"""

import asyncio
import signal
import sys
from typing import Optional

# CRITICAL: Setup logging FIRST, before any other imports that might create loggers
# This ensures all loggers use stderr instead of stdout (required for MCP protocol)
from config.logging import setup_logging

setup_logging()

from mcp.server.stdio import stdio_server  # noqa: E402
from config.logging import get_logger, flush_logs  # noqa: E402
from server.mcp_server import MCPServer  # noqa: E402

logger = get_logger(__name__)

# Global reference to server instance for signal handlers
_server_instance: Optional[MCPServer] = None
_shutdown_event = asyncio.Event()


def handle_shutdown_signal(signum: int, frame) -> None:
    """
    Handle shutdown signals (SIGTERM, SIGINT) gracefully.

    This function is called when the process receives a termination signal.
    It triggers the shutdown event to initiate graceful shutdown.
    """
    signal_name = signal.Signals(signum).name
    logger.info(f"Received {signal_name} signal, initiating graceful shutdown...")
    _shutdown_event.set()


async def main() -> None:
    """Main application entry point with graceful shutdown handling."""
    global _server_instance

    # Register signal handlers for graceful shutdown
    signal.signal(signal.SIGTERM, handle_shutdown_signal)
    signal.signal(signal.SIGINT, handle_shutdown_signal)

    logger.info("Starting audit-logs MCP server...")

    try:
        # Create and initialize server instance
        _server_instance = MCPServer()
        await _server_instance.initialize()

        logger.info("MCP server initialized successfully")

        # Run the MCP server with stdio transport
        async with stdio_server() as (read_stream, write_stream):
            # Create a task to run the server
            server_task = asyncio.create_task(
                _server_instance.server.run(
                    read_stream,
                    write_stream,
                    _server_instance.server.create_initialization_options(),
                )
            )

            # Create a task to wait for shutdown signal
            shutdown_task = asyncio.create_task(_shutdown_event.wait())

            # Wait for either server completion or shutdown signal
            done, pending = await asyncio.wait({server_task, shutdown_task}, return_when=asyncio.FIRST_COMPLETED)

            # If shutdown was triggered, cancel the server task
            if shutdown_task in done:
                logger.info("Shutdown signal received, stopping server...")
                server_task.cancel()
                try:
                    await server_task
                except asyncio.CancelledError:
                    pass

            # Cancel any remaining tasks
            for task in pending:
                task.cancel()
                try:
                    await task
                except asyncio.CancelledError:
                    pass

    except Exception as e:
        logger.error(f"Server error: {str(e)}", exc_info=True)
        sys.exit(1)
    finally:
        # Always perform cleanup, even if an error occurred
        if _server_instance is not None:
            logger.info("Shutting down server components...")
            try:
                await _server_instance.shutdown()
                logger.info("Server shutdown complete")
            except Exception as e:
                logger.error(f"Error during shutdown: {str(e)}", exc_info=True)

        # Flush all log handlers to ensure logs are written
        flush_logs()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
    except Exception as e:
        logger.error(f"Fatal error: {e}", exc_info=True)
        sys.exit(1)
