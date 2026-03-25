#!/usr/bin/env python3

# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
reporting MCP Server

This module serves as the entry point for the reporting MCP server.
It initializes and runs the MCP server for The HPE GreenLake for Reporting service provides a collection of RESTful APIs for generating reports, retrieving supported columns and filters, monitoring asynchronous operations, and querying the status of reports..
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
