# (c) Copyright 2025 Hewlett Packard Enterprise Development LP
"""
list_endpoints tool implementation for users MCP server.

This tool provides fast discovery of all available API endpoints as a simple list of endpoint identifiers.
Generated for dynamic mode when OpenAPI spec has 0 endpoints (>= 50 threshold).
"""

from typing import Any, Dict, List
from tools.base import BaseTool


class ListEndpointsTool(BaseTool):
    """Lists all available API endpoints as simple identifiers for fast discovery."""

    @property
    def name(self) -> str:
        """Tool name."""
        return "list_endpoints"

    @property
    def description(self) -> str:
        """Tool description."""
        return "Lists all available users API endpoints as simple identifiers (method:path format) for fast discovery and selection"

    @property
    def input_schema(self) -> Dict[str, Any]:
        """Input schema for the tool."""
        return {
            "type": "object",
            "properties": {
                "filter": {
                    "type": "string",
                    "description": "Optional filter to search for specific endpoints (case-insensitive substring match)",
                    "default": "",
                }
            },
            "required": [],
        }

    async def execute(self, arguments: Dict[str, Any]) -> List[str]:  # type: ignore[override]
        """Execute the tool to list all available endpoints as simple identifiers."""
        try:
            # Extract arguments with defaults
            filter_term = arguments.get("filter", "").lower()

            # Define all available endpoints in METHOD:PATH format
            all_endpoints: List[str] = [
                "GET:/identity/v1/users",
                "GET:/identity/v1/users/{id}",
            ]

            # Apply filter if provided
            if filter_term:
                filtered_endpoints = [endpoint for endpoint in all_endpoints if filter_term in endpoint.lower()]
            else:
                filtered_endpoints = all_endpoints

            # Sort endpoints for consistent ordering
            filtered_endpoints.sort()

            # Return as simple list of endpoint identifiers for fast discovery
            return filtered_endpoints

        except Exception as e:
            # Return error message for debugging
            return [f"ERROR: Failed to list endpoints: {str(e)}"]
