# (c) Copyright 2025 Hewlett Packard Enterprise Development LP
"""
getauditlogdetails tool implementation for audit-logs MCP server.

This tool Get additional detail of an audit log..
"""

from typing import Any, Dict, List
from tools.base import BaseTool


class getauditlogdetailsTool(BaseTool):
    """Get additional detail of an audit log."""

    @property
    def name(self) -> str:
        """Tool name."""
        return "getauditlogdetails"

    @property
    def description(self) -> str:
        """Tool description."""
        return "Get additional detail of an audit log."

    @property
    def input_schema(self) -> Dict[str, Any]:
        """Input schema for the tool."""
        return {
            "type": "object",
            "properties": {
                "id": {
                    "type": "string",
                    "description": "Provide the ID of the audit log record that has the `hasDetails` value set to `true` to fetch the additional details.",
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

        # Add parameter-specific validation here
        pass

    async def execute(self, arguments: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Execute the getauditlogdetails tool.

        Args:
            arguments: Tool arguments

        Returns:
            List of results
        """
        try:
            # Validate arguments
            self.validate_arguments(arguments)

            # Extract parameters
            # Parameter: id

            # Build URL with path parameters
            url = "/audit-log/v1/logs/{id}/detail"
            # Replace path parameter: id
            url = url.replace("{" + "id" + "}", str(arguments["id"]))

            # Prepare query/body parameters
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
