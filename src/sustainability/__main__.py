#!/usr/bin/env python3

# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
Sustainability_Insight_Center MCP Server

This module serves as the entry point for the Sustainability_Insight_Center MCP server.
It initializes and runs the MCP server for The HPE Sustainability Insight Center API enables users to manage power consumption data that helps to reduce costs and achieve IT sustainability goals..
"""

# CRITICAL: Import logging config FIRST to configure logging before any other imports
# This prevents stdout pollution which breaks MCP JSON-RPC protocol
import config.logging  # noqa: F401

# Import main after logging is configured
from server.app import main

if __name__ == "__main__":
    # main() is synchronous – FastMCP calls asyncio.run() internally via mcp.run().
    # Do NOT wrap in asyncio.run() here.
    main()
