#!/usr/bin/env python3

# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
service-catalog MCP Server

This module serves as the entry point for the service-catalog MCP server.
It initializes and runs the MCP server for The HPE GreenLake for Service Catalog service offers a collection of RESTful APIs to fetch, provision service managers and to delete a service manager provisioned in a workspace..
"""

# CRITICAL: Import logging config FIRST to configure logging before any other imports
# This prevents stdout pollution which breaks MCP JSON-RPC protocol
import greenlake_service_catalog_mcp.config.logging  # noqa: F401

# Import main after logging is configured
from greenlake_service_catalog_mcp.server.app import main

if __name__ == "__main__":
    # main() is synchronous – FastMCP calls asyncio.run() internally via mcp.run().
    # Do NOT wrap in asyncio.run() here.
    main()
