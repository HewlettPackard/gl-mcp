#!/usr/bin/env python3
"""
devices MCP Server

This module serves as the entry point for the devices MCP server.
It initializes and runs the MCP server for With the HPE GreenLake APIs for Device Management you can view, manage, and onboard devices in your workspace. The API allows you to invoke any operation or task that is available through the HPE GreenLake edge-to-cloud platform user interface..
"""

import asyncio

# CRITICAL: Import logging config FIRST to configure logging before any other imports
# This prevents stdout pollution which breaks MCP JSON-RPC protocol
import config.logging  # noqa: F401

# Import main after logging is configured
from server.app import main

if __name__ == "__main__":
    # Logging is already configured in server.app module
    # No need to configure it here to avoid stdout pollution

    # Run the MCP server
    asyncio.run(main())
