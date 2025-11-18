# (c) Copyright 2025 Hewlett Packard Enterprise Development LP
"""
Logging configuration for subscriptions MCP server.

This module sets up structured logging for the MCP server using loguru.
CRITICAL: MCP protocol requires stdout for JSON-RPC messages only.
All diagnostic logs MUST go to stderr to avoid protocol corruption.
"""

from loguru import logger
import sys
from pathlib import Path
from typing import Optional
import os

# Get log level from environment (default: ERROR for production MCP servers)
LOG_LEVEL = os.getenv("GREENLAKE_LOG_LEVEL", "ERROR").upper()

# CRITICAL: Remove ALL default handlers immediately
# This prevents any accidental stdout logging from loguru's defaults
logger.remove()


def log_filter(record):
    """
    Filter to suppress DEBUG/INFO logs from noisy third-party libraries.

    This keeps WARNING/ERROR/CRITICAL logs from httpx, httpcore, etc. which are
    important for diagnosing HTTP connection issues, timeouts, and errors while
    suppressing verbose DEBUG/INFO logs about connection pooling and retries.

    Args:
        record: Loguru log record

    Returns:
        bool: True if the log should be emitted, False otherwise
    """
    noisy_libs = ["httpx", "httpcore", "urllib3", "asyncio"]

    # For noisy libraries, only allow WARNING (30) and above
    if any(record["name"].startswith(lib) for lib in noisy_libs):
        return record["level"].no >= 30  # WARNING=30, ERROR=40, CRITICAL=50

    # For all other loggers, use the configured log level
    return True


# Add stderr handler (REQUIRED for MCP protocol compliance)
# MCP servers MUST NOT write anything to stdout except JSON-RPC messages
logger.add(
    sys.stderr,
    level=LOG_LEVEL,
    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
    colorize=False,  # Disable colors for better compatibility
    filter=log_filter,
)

# Optional: Add file logging for debugging and audit purposes
# Logs are written to user's home directory for persistence
if os.getenv("GREENLAKE_FILE_LOGGING", "false").lower() == "true":
    log_dir = Path.home() / ".hpe" / "mcp-logs" / "subscriptions"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / "subscriptions-mcp.log"
    logger.add(
        log_file,
        rotation="10 MB",
        retention="7 days",
        level="DEBUG",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
        filter=log_filter,
    )


def setup_logging(level: Optional[str] = None) -> None:
    """
    Set up logging configuration for the MCP server.

    Args:
        level: Log level override (if provided, reconfigures the logger)
    """
    if level:
        # Remove existing handlers and reconfigure with new level
        logger.remove()
        logger.add(
            sys.stderr,
            level=level.upper(),
            format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
            colorize=False,
            filter=log_filter,
        )


def get_logger(name: str):
    """
    Get a logger instance.

    With loguru, this returns the global logger instance. The 'name' parameter
    is kept for API compatibility with standard library logging, but loguru
    automatically tracks the caller context.

    Args:
        name: Logger name (typically __name__, kept for compatibility)

    Returns:
        The loguru logger instance

    Example:
        >>> from config.logging import get_logger
        >>> logger = get_logger(__name__)
        >>> logger.info("Processing request")
    """
    return logger


def flush_logs() -> None:
    """
    Flush all log handlers to ensure pending logs are written.

    This is important during graceful shutdown to ensure all diagnostic
    information is persisted before the process exits.

    Called automatically by the graceful shutdown handler.
    """
    try:
        # Loguru's complete() flushes all handlers
        logger.complete()
    except Exception:
        # Silently ignore flush errors during shutdown
        pass
