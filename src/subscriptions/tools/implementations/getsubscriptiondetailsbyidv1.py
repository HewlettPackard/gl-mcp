# (c) Copyright 2025 Hewlett Packard Enterprise Development LP
"""
getsubscriptiondetailsbyidv1 tool implementation for subscriptions MCP server.

This tool Get detailed information for a single subscription by `id`. <br><br>**NOTE:** You need to have the view permission of device management to invoke this API. <br><br> Rate limits are enforced on this API. 20 requests per minute is supported per workspace. The API returns `429` if this threshold is breached..
"""

from typing import Any, Dict, List
from tools.base import BaseTool


class getsubscriptiondetailsbyidv1Tool(BaseTool):
    """Get detailed information for a single subscription by `id`. <br><br>**NOTE:** You need to have the view permission of device management to invoke this API. <br><br> Rate limits are enforced on this API. 20 requests per minute is supported per workspace. The API returns `429` if this threshold is breached."""

    @property
    def name(self) -> str:
        """Tool name."""
        return "getsubscriptiondetailsbyidv1"

    @property
    def description(self) -> str:
        """Tool description."""
        return "Get detailed information for a single subscription by `id`. <br><br>**NOTE:** You need to have the view permission of device management to invoke this API. <br><br> Rate limits are enforced on this API. 20 requests per minute is supported per workspace. The API returns `429` if this threshold is breached."

    @property
    def input_schema(self) -> Dict[str, Any]:
        """Input schema for the tool."""
        return {
            "type": "object",
            "properties": {
                "id": {"type": "string", "description": "The unique identifier of the subscription."},
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
        Execute the getsubscriptiondetailsbyidv1 tool.

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
            url = "/subscriptions/v1/subscriptions/{id}"
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
