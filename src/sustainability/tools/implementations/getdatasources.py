# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
getdatasources tool implementation for sustainability MCP server.

This tool gets all HPE Sustainability Insight Center data sources.
"""

from typing import Any, Dict, List
from tools.base import BaseTool


class getdatasourcesTool(BaseTool):
    """Get all HPE Sustainability Insight Center data sources. Returns information about connected data sources including collection times."""

    @property
    def name(self) -> str:
        """Tool name."""
        return "getdatasources"

    @property
    def description(self) -> str:
        """Tool description."""
        return "Get all HPE Sustainability Insight Center data sources. Returns information about connected data sources including collection times."

    @property
    def input_schema(self) -> Dict[str, Any]:
        """Input schema for the tool."""
        return {
            "type": "object",
            "properties": {
                "offset": {
                    "type": ["integer", "string"],
                    "description": "Specifies the zero-based resource offset to start the response from.",
                },
                "limit": {
                    "type": ["integer", "string"],
                    "description": "How many items to return at one time.",
                },
            },
            "required": [],
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

        # Add parameter-specific validation here
        pass

    async def execute(self, arguments: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Execute the getdatasources tool.

        Args:
            arguments: Tool arguments

        Returns:
            List of results
        """
        try:
            # Validate arguments
            self.validate_arguments(arguments)

            # Build URL
            url = "/sustainability-insight-ctr/v1beta1/datasources"

            # Prepare query parameters
            params: Dict[str, Any] = {}
            # Parameter: offset (integer - will coerce strings)
            param_value = arguments.get("offset")
            if param_value is not None:
                param_value = self.coerce_string_to_int(param_value, "offset")
            if param_value is not None:
                params["offset"] = param_value
            # Parameter: limit (integer - will coerce strings)
            param_value = arguments.get("limit")
            if param_value is not None:
                param_value = self.coerce_string_to_int(param_value, "limit")
            if param_value is not None:
                params["limit"] = param_value

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
