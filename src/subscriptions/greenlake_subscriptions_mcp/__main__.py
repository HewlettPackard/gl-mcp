#!/usr/bin/env python3

# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
subscriptions MCP Server

This module serves as the entry point for the subscriptions MCP server.
It initializes and runs the MCP server for With the HPE GreenLake APIs for Subscription Management you can add subscriptions, unclaim subscriptions, get subscription information, and update auto-subscription settings for your HPE GreenLake workspace..
"""

# CRITICAL: Import logging config FIRST to configure logging before any other imports
# This prevents stdout pollution which breaks MCP JSON-RPC protocol
import greenlake_subscriptions_mcp.config.logging  # noqa: F401

# Import main after logging is configured
from greenlake_subscriptions_mcp.server.app import main

if __name__ == "__main__":
    # main() is synchronous – FastMCP calls asyncio.run() internally via mcp.run().
    # Do NOT wrap in asyncio.run() here.
    main()
