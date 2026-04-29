#!/usr/bin/env python3

# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
audit-logs MCP Server

This module serves as the entry point for the audit-logs MCP server.
It initializes and runs the MCP server for The HPE GreenLake Audit Log Service offers a collection of RESTful APIs for publishing audit logs and querying both application-specific and overall platform logs..
"""

# CRITICAL: Import logging config FIRST to configure logging before any other imports
# This prevents stdout pollution which breaks MCP JSON-RPC protocol
import greenlake_audit_logs_mcp.config.logging  # noqa: F401

# Import main after logging is configured
from greenlake_audit_logs_mcp.server.app import main

if __name__ == "__main__":
    # main() is synchronous – FastMCP calls asyncio.run() internally via mcp.run().
    # Do NOT wrap in asyncio.run() here.
    main()
