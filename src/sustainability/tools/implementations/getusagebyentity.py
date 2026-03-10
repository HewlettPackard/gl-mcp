# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
getusagebyentity tool implementation for sustainability MCP server.

This tool gets energy usage data grouped by entity (device).
"""

from typing import Any, Dict, List
from tools.base import BaseTool


class getusagebyentityTool(BaseTool):
    """Get energy usage data grouped by entity (device). Returns energy consumption (kWh), carbon footprint (CO2e metric tons), and estimated energy cost per entity with location details."""

    @property
    def name(self) -> str:
        """Tool name."""
        return "getusagebyentity"

    @property
    def description(self) -> str:
        """Tool description."""
        return "Get energy usage data grouped by entity (device). Returns energy consumption (kWh), carbon footprint (CO2e metric tons), and estimated energy cost per entity with location details."

    @property
    def input_schema(self) -> Dict[str, Any]:
        """Input schema for the tool."""
        return {
            "type": "object",
            "properties": {
                "start-time": {
                    "type": "string",
                    "description": "Start time in ISO 8601 format (e.g. '2024-01-01T00:00:00Z').",
                },
                "end-time": {
                    "type": "string",
                    "description": "End time in ISO 8601 format (e.g. '2024-01-31T23:59:59Z').",
                },
                "filter": {
                    "type": "string",
                    "description": "Filter expression for narrowing results.",
                },
                "filter-tags": {
                    "type": "string",
                    "description": "Filter by tags.",
                },
                "currency": {
                    "type": "string",
                    "description": "Currency code for energy cost (e.g. 'USD').",
                },
                "sort": {
                    "type": "string",
                    "description": "Sort order for results.",
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
            "required": [
                "start-time",
                "end-time",
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

        if "start-time" not in arguments:
            raise ValueError("start-time is required")

        if arguments["start-time"] is None:
            raise ValueError("start-time cannot be None")

        if isinstance(arguments["start-time"], str) and arguments["start-time"].strip() == "":
            raise ValueError("start-time cannot be empty")

        if "end-time" not in arguments:
            raise ValueError("end-time is required")

        if arguments["end-time"] is None:
            raise ValueError("end-time cannot be None")

        if isinstance(arguments["end-time"], str) and arguments["end-time"].strip() == "":
            raise ValueError("end-time cannot be empty")

    async def execute(self, arguments: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Execute the getusagebyentity tool.

        Args:
            arguments: Tool arguments

        Returns:
            List of results
        """
        try:
            # Validate arguments
            self.validate_arguments(arguments)

            # Build URL
            url = "/sustainability-insight-ctr/v1beta1/usage-by-entity"

            # Prepare query parameters
            params: Dict[str, Any] = {}
            # Parameter: start-time
            param_value = arguments.get("start-time")
            if param_value is not None:
                params["start-time"] = param_value
            # Parameter: end-time
            param_value = arguments.get("end-time")
            if param_value is not None:
                params["end-time"] = param_value
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
            # Parameter: sort
            param_value = arguments.get("sort")
            if param_value is not None:
                params["sort"] = param_value
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
