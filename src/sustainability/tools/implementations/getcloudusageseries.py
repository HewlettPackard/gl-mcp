# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
getcloudusageseries tool implementation for sustainability MCP server.

This tool gets public cloud sustainability data grouped by time buckets.
"""

from typing import Any, Dict, List
from tools.base import BaseTool


class getcloudusageseriesTool(BaseTool):
    """Get public cloud sustainability data grouped by time buckets. Returns time series of CO2 emissions for cloud services."""

    @property
    def name(self) -> str:
        """Tool name."""
        return "getcloudusageseries"

    @property
    def description(self) -> str:
        """Tool description."""
        return "Get public cloud sustainability data grouped by time buckets. Returns time series of CO2 emissions for cloud services."

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
                "interval": {
                    "type": "string",
                    "description": "Time bucket interval in format 'integer unit' (e.g. '1 day', '2 hours', '1 month', '1 year').",
                },
                "filter": {
                    "type": "string",
                    "description": "Filter expression for narrowing results.",
                },
            },
            "required": [
                "start-time",
                "end-time",
                "interval",
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

        if "interval" not in arguments:
            raise ValueError("interval is required")

        if arguments["interval"] is None:
            raise ValueError("interval cannot be None")

        if isinstance(arguments["interval"], str) and arguments["interval"].strip() == "":
            raise ValueError("interval cannot be empty")

    async def execute(self, arguments: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Execute the getcloudusageseries tool.

        Args:
            arguments: Tool arguments

        Returns:
            List of results
        """
        try:
            # Validate arguments
            self.validate_arguments(arguments)

            # Build URL
            url = "/sustainability-insight-ctr/v1beta1/cloud-usage-series"

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
            # Parameter: interval
            param_value = arguments.get("interval")
            if param_value is not None:
                params["interval"] = param_value
            # Parameter: filter
            param_value = arguments.get("filter")
            if param_value is not None:
                params["filter"] = param_value

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
