# (c) Copyright 2025 Hewlett Packard Enterprise Development LP
"""
get_workspace_detailed_info_workspaces_v1_workspaces_wo_5c14f2bc tool implementation for workspaces MCP server.

This tool Retrieve detailed workspace information..
"""

from typing import Any, Dict, List
from tools.base import BaseTool


class get_workspace_detailed_info_workspaces_v1_workspaces_wo_5c14f2bcTool(BaseTool):
    """Retrieve detailed workspace information."""

    @property
    def name(self) -> str:
        """Tool name."""
        return "get_workspace_detailed_info_workspaces_v1_workspaces_wo_5c14f2bc"

    @property
    def description(self) -> str:
        """Tool description."""
        return "Retrieve detailed workspace information."

    @property
    def input_schema(self) -> Dict[str, Any]:
        """Input schema for the tool."""
        return {
            "type": "object",
            "properties": {
                "workspaceId": {
                    "type": "string",
                    "description": "The unique identifier of the workspace.\n\nExample: 7600415a-8876-5722-9f3c-b0fd11112283",
                },
            },
            "required": [
                "workspaceId",
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

        if "workspaceId" not in arguments:
            raise ValueError("workspaceId is required")

        if arguments["workspaceId"] is None:
            raise ValueError("workspaceId cannot be None")

        if isinstance(arguments["workspaceId"], str) and arguments["workspaceId"].strip() == "":
            raise ValueError("workspaceId cannot be empty")

        # Add parameter-specific validation here
        pass

    async def execute(self, arguments: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Execute the get_workspace_detailed_info_workspaces_v1_workspaces_wo_5c14f2bc tool.

        Args:
            arguments: Tool arguments

        Returns:
            List of results
        """
        try:
            # Validate arguments
            self.validate_arguments(arguments)

            # Extract parameters
            # Parameter: workspaceId

            # Build URL with path parameters
            url = "/workspaces/v1/workspaces/{workspaceId}/contact"
            # Replace path parameter: workspaceId
            url = url.replace("{" + "workspaceId" + "}", str(arguments["workspaceId"]))

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
