# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
getcoefficients tool implementation for sustainability MCP server.

This tool gets cost and CO2 coefficients.
"""

from typing import Any, Dict, List
from tools.base import BaseTool


class getcoefficientsTool(BaseTool):
    """Get cost and CO2 coefficients. Returns the configured energy cost (per kWh) and CO2 emission rate (grams per kWh) for each location."""

    @property
    def name(self) -> str:
        """Tool name."""
        return "getcoefficients"

    @property
    def description(self) -> str:
        """Tool description."""
        return "Get cost and CO2 coefficients. Returns the configured energy cost (per kWh) and CO2 emission rate (grams per kWh) for each location."

    @property
    def input_schema(self) -> Dict[str, Any]:
        """Input schema for the tool."""
        return {
            "type": "object",
            "properties": {
                "filter": {
                    "type": "string",
                    "description": "Filter expression (only locationId is filterable).",
                },
                "filter-tags": {
                    "type": "string",
                    "description": "Filter by tags.",
                },
                "currency": {
                    "type": "string",
                    "description": "Currency code for energy cost (e.g. 'USD').",
                },
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
        Execute the getcoefficients tool.

        Args:
            arguments: Tool arguments

        Returns:
            List of results
        """
        try:
            # Validate arguments
            self.validate_arguments(arguments)

            # Build URL
            url = "/sustainability-insight-ctr/v1beta1/coefficients"

            # Prepare query parameters
            params: Dict[str, Any] = {}
            # Parameter: filter
            param_value = arguments.get("filter")
            if param_value is not None:
                params["filter"] = param_value
            # Parameter: filter-tags
            param_value = arguments.get("filter-tags")
            if param_value is not None:
                params["filter-tags"] = param_value
            # Parameter: currency
            param_value = arguments.get("currency")
            if param_value is not None:
                params["currency"] = param_value
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
