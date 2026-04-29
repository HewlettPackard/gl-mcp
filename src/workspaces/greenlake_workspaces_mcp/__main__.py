#!/usr/bin/env python3

# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
workspaces MCP Server

This module serves as the entry point for the workspaces MCP server.
It initializes and runs the MCP server for With the HPE GreenLake for Workspace Management APIs you can view workspace information and create, update, or delete managed service provider tenants..
"""

# CRITICAL: Import logging config FIRST to configure logging before any other imports
# This prevents stdout pollution which breaks MCP JSON-RPC protocol
import greenlake_workspaces_mcp.config.logging  # noqa: F401

# Import main after logging is configured
from greenlake_workspaces_mcp.server.app import main

if __name__ == "__main__":
    # main() is synchronous – FastMCP calls asyncio.run() internally via mcp.run().
    # Do NOT wrap in asyncio.run() here.
    main()
