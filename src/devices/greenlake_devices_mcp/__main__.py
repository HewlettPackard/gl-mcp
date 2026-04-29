#!/usr/bin/env python3

# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
devices MCP Server

This module serves as the entry point for the devices MCP server.
It initializes and runs the MCP server for With the HPE GreenLake APIs for Device Management you can view, manage, and onboard devices in your workspace. The API allows you to invoke any operation or task that is available through the HPE GreenLake edge-to-cloud platform user interface..
"""

# CRITICAL: Import logging config FIRST to configure logging before any other imports
# This prevents stdout pollution which breaks MCP JSON-RPC protocol
import greenlake_devices_mcp.config.logging  # noqa: F401

# Import main after logging is configured
from greenlake_devices_mcp.server.app import main

if __name__ == "__main__":
    # main() is synchronous – FastMCP calls asyncio.run() internally via mcp.run().
    # Do NOT wrap in asyncio.run() here.
    main()
