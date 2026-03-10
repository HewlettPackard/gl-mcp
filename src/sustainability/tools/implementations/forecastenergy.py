# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
forecastenergy tool implementation for sustainability MCP server.

This tool gets forecasted energy consumption, CO2 emissions, and costs.
"""

from typing import Any, Dict, List
from tools.base import BaseTool


class forecastenergyTool(BaseTool):
    """Get forecasted energy consumption (kWh), CO2 emissions, and costs with confidence intervals for 1 to 6 months into the future. Also returns 3 months of historical data and sustainability journey comparison."""

    @property
    def name(self) -> str:
        """Tool name."""
        return "forecastenergy"

    @property
    def description(self) -> str:
        """Tool description."""
        return "Get forecasted energy consumption (kWh), CO2 emissions, and costs with confidence intervals for 1 to 6 months into the future. Also returns 3 months of historical data and sustainability journey comparison."

    @property
    def input_schema(self) -> Dict[str, Any]:
        """Input schema for the tool."""
        return {
            "type": "object",
            "properties": {
                "timePeriodMonths": {
                    "type": ["integer", "string"],
                    "description": "Number of months to forecast (1-6).",
                },
                "currencyCode": {
                    "type": "string",
                    "description": "Currency code for energy cost (e.g. 'USD').",
                },
            },
            "required": [
                "timePeriodMonths",
                "currencyCode",
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

        if "timePeriodMonths" not in arguments:
            raise ValueError("timePeriodMonths is required")

        if arguments["timePeriodMonths"] is None:
            raise ValueError("timePeriodMonths cannot be None")

        if "currencyCode" not in arguments:
            raise ValueError("currencyCode is required")

        if arguments["currencyCode"] is None:
            raise ValueError("currencyCode cannot be None")

        if isinstance(arguments["currencyCode"], str) and arguments["currencyCode"].strip() == "":
            raise ValueError("currencyCode cannot be empty")

    async def execute(self, arguments: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Execute the forecastenergy tool.

        Args:
            arguments: Tool arguments

        Returns:
            List of results
        """
        try:
            # Validate arguments
            self.validate_arguments(arguments)

            # Build URL
            url = "/sustainability-insight-ctr/v1beta1/forecast/energy"

            # Prepare request body
            body: Dict[str, Any] = {}
            # Parameter: timePeriodMonths (integer - will coerce strings)
            param_value = arguments.get("timePeriodMonths")
            if param_value is not None:
                param_value = self.coerce_string_to_int(param_value, "timePeriodMonths")
            if param_value is not None:
                body["timePeriodMonths"] = param_value
            # Parameter: currencyCode
            param_value = arguments.get("currencyCode")
            if param_value is not None:
                body["currencyCode"] = param_value

            # Make API request (POST)
            response_data = await self.http_client.post(url, data=body)

            # Format response for MCP
            return [self.format_success(response_data)]

        except ValueError as e:
            self.logger.error(f"Validation error in {self.name}: {str(e)}")
            return [self.format_validation_error(str(e))]

        except Exception as e:
            self.logger.error(f"Error executing {self.name}: {str(e)}", exc_info=True)
            return [self.format_error(e)]
