# (c) Copyright 2025 Hewlett Packard Enterprise Development LP
"""
get_user_detailed_identity_v1_users_id_get tool implementation for users MCP server.

This tool Retrieve a single user based on a given user ID..
"""

from typing import Any, Dict, List
from tools.base import BaseTool


class get_user_detailed_identity_v1_users_id_getTool(BaseTool):
    """Retrieve a single user based on a given user ID."""

    @property
    def name(self) -> str:
        """Tool name."""
        return "get_user_detailed_identity_v1_users_id_get"

    @property
    def description(self) -> str:
        """Tool description."""
        return "Retrieve a single user based on a given user ID."

    @property
    def input_schema(self) -> Dict[str, Any]:
        """Input schema for the tool."""
        return {
            "type": "object",
            "properties": {
                "id": {
                    "type": "string",
                    "description": "The unique identifier of the user.\n\nExample: 7600415a-8876-5722-9f3c-b0fd11112283",
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
        Execute the get_user_detailed_identity_v1_users_id_get tool.

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
            url = "/identity/v1/users/{id}"
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
