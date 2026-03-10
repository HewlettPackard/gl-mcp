#!/usr/bin/env python3

# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
sustainability MCP Server

This module serves as the entry point for the sustainability MCP server.
It initializes and runs the MCP server for the HPE Sustainability Insight Center
which provides energy consumption, carbon footprint, and cost data for IT infrastructure.
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
