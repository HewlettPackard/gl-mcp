# (c) Copyright 2025 Hewlett Packard Enterprise Development LP
"""
Version information for subscriptions MCP server.

This module provides version and identification information used for
User-Agent headers and other metadata purposes.
"""

# Server identification
SERVER_NAME: str = "subscriptions"
SERVER_VERSION: str = "1.0.1"

# User-Agent string for API calls
# Format: HPE-GreenLake-MCP/{server-name}-{version}
USER_AGENT: str = f"HPE-GreenLake-MCP/{SERVER_NAME}-{SERVER_VERSION}"
