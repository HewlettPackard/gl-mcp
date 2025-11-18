#!/usr/bin/env python3
"""
subscriptions MCP Server

This module serves as the entry point for the subscriptions MCP server.
It initializes and runs the MCP server for With the HPE GreenLake APIs for Subscription Management you can add subscriptions, get subscription information, and update auto-subscription settings for your HPE GreenLake workspace..
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
