# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
getdatasourcebyid tool implementation for sustainability MCP server.

This tool gets details of a specific data source by ID.
"""

from typing import Any, Dict, List
from urllib.parse import quote
from tools.base import BaseTool


class getdatasourcebyidTool(BaseTool):
    """Get details of a specific data source by ID."""

    @property
    def name(self) -> str:
        """Tool name."""
        return "getdatasourcebyid"

    @property
    def description(self) -> str:
        """Tool description."""
        return "Get details of a specific data source by ID."

    @property
    def input_schema(self) -> Dict[str, Any]:
        """Input schema for the tool."""
        return {
            "type": "object",
            "properties": {
                "id": {
                    "type": "string",
                    "description": "The UUID of the data source to retrieve.",
                },
            },
            "required": [
                "id",
            ],
            "additionalProperties": False,
        }

    def validate_arguments(self, arguments: Dict[str, Any]) -> None:
        """
        Validate tool arguments.

        Args:
            arguments: Arguments to validate

        Raises:
            ValueError: If arguments are invalid
        """
        super().validate_arguments(arguments)

        if "id" not in arguments:
            raise ValueError("id is required")

        if arguments["id"] is None:
            raise ValueError("id cannot be None")

        if isinstance(arguments["id"], str) and arguments["id"].strip() == "":
            raise ValueError("id cannot be empty")

    async def execute(self, arguments: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Execute the getdatasourcebyid tool.

        Args:
            arguments: Tool arguments

        Returns:
            List of results
        """
        try:
            # Validate arguments
            self.validate_arguments(arguments)

            # Build URL with path parameters
            url = "/sustainability-insight-ctr/v1beta1/datasources/{id}"
            # Replace path parameter: id (URL-encoded to prevent path traversal)
            url = url.replace("{" + "id" + "}", quote(str(arguments["id"]), safe=""))

            # Prepare query parameters
            params: Dict[str, Any] = {}

            # Make API request
            response_data = await self.http_client.get(url, params=params)

            # Format response for MCP
            return [self.format_success(response_data)]

        except ValueError as e:
            self.logger.error(f"Validation error in {self.name}: {str(e)}")
            return [self.format_validation_error(str(e))]

        except Exception as e:
            self.logger.error(f"Error executing {self.name}: {str(e)}", exc_info=True)
            return [self.format_error(e)]
