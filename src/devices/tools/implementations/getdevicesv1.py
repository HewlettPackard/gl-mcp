# (c) Copyright 2025 Hewlett Packard Enterprise Development LP
"""
getdevicesv1 tool implementation for devices MCP server.

This tool With this API, you can: <ul><li>Retrieve a list of devices managed in a workspace.</li> <li>Filter  devices based on conditional expressions.</li></ul><p><b>NOTE</b>: You need view  permissions for Devices and Subscription service to invoke this API.</p>  Rate limits are enforced on this API. 160 requests per minute is supported per workspace. The API returns `429` if this threshold is breached..
"""

from typing import Any, Dict, List
from tools.base import BaseTool


class getdevicesv1Tool(BaseTool):
    """With this API, you can: <ul><li>Retrieve a list of devices managed in a workspace.</li> <li>Filter  devices based on conditional expressions.</li></ul><p><b>NOTE</b>: You need view  permissions for Devices and Subscription service to invoke this API.</p>  Rate limits are enforced on this API. 160 requests per minute is supported per workspace. The API returns `429` if this threshold is breached."""

    @property
    def name(self) -> str:
        """Tool name."""
        return "getdevicesv1"

    @property
    def description(self) -> str:
        """Tool description."""
        return "With this API, you can: <ul><li>Retrieve a list of devices managed in a workspace.</li> <li>Filter  devices based on conditional expressions.</li></ul><p><b>NOTE</b>: You need view  permissions for Devices and Subscription service to invoke this API.</p>  Rate limits are enforced on this API. 160 requests per minute is supported per workspace. The API returns `429` if this threshold is breached."

    @property
    def input_schema(self) -> Dict[str, Any]:
        """Input schema for the tool."""
        return {
            "type": "object",
            "properties": {
                "filter": {
                    "type": "string",
                    "description": "Filter expressions consisting of simple comparison operations joined\nby logical operators.<br>\n| CLASS               |   EXAMPLES                                         |\n|---------------------|----------------------------------------------------|\n| Types               | integer, decimal, timestamp, string, boolean, null |\n| Comparison          | eq, ne, gt, ge, lt, le, in                         |\n| Logical Expressions | and, or, not                                       |\n\nThe following examples are not an exhaustive list of all possible filtering options.\n\n\nExamples:\n  - deviceType eq 'STORAGE' and partNumber eq 'RTICXL6413'\n    Return devices that exactly satisfy multiple filter queries.\nExample syntax, <property> eq <value> and <property> eq <value>.\n  - serialNumber eq 'STIAPL6404' or partNumber eq 'RTICXL6413'\n    Return devices that exactly satisfy one of multiple filter queries.\nExample syntax, <property> eq <value> or <property> eq <value>.\n  - serialNumber eq 'STIAPL6404'\n    Return devices where a property equals a value.\nExample syntax, <property> eq <value>.\n  - createdAt ge ''2024-01-18T19:53:51.480Z''\n    Return devices where a property is greater or equal to a value.\nExample syntax, <property> ge <value>.\n  - updatedAt le '2024-02-18T19:53:51.480Z'\n    Return devices where a property is lesser or equal to a value.\nExample syntax, <property> ge <value>.\n  - not serialNumber eq 'STIAPL6404'\n    Return devices where a property does not equal a value.\nExample syntax, not <property> eq <value>.\n  - deviceType in 'COMPUTE', 'STORAGE'\n    Return devices where a property is one of multiple values.\nExample syntax, <property> in <value>,<value>.\n\n**Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`.\n\nFilterable properties: application, archived, assignedState, createdAt, deviceType, id, location, macAddress, model, partNumber, region, serialNumber, subscription, tags, tenantWorkspaceId, type, updatedAt, warranty",
                },
                "filter-tags": {
                    "type": "string",
                    "description": "Filter expressions consisting of simple comparison operations joined\nby logical operators to be applied on the assigned tags or their\nvalues.<br>\n| CLASS               |   EXAMPLES      |\n|---------------------|-----------------|\n| Types               | string          |\n| Comparison          | eq, ne, in      |\n| Logical Expressions | and, or, not    |\n\n\nExamples:\n  - 'city' eq 'London'\n    Return devices where a tag key is equal to a tag value.\nExample syntax, <tagKey> eq <tagValue>.\n  - not 'city' eq 'Tokyo'\n    Return devices where a tag key does not equal a tag value.\nExample syntax, not <property> eq <value>.\n  - 'street' in 'Regent Street', 'Oxford Street', 'Piccadilly'\n    Return devices containing the tag key and at least one of the specified values.\nExample syntax, <property> in <value>,<value>.\n  - 'city' eq 'London' and 'street' eq 'Piccadilly'\n    Return devices that exactly satisfy multiple filter queries applied to tag keys.\nExample syntax, <property> eq <value> and <property> eq <value>.\n  - 'street' eq 'Oxford Street' or 'street' eq 'Piccadilly'\n    Return devices that satisfy any of multiple filter queries applied to tag keys.\nExample syntax, <property> eq <value> or <property> eq <value>.\n\n**Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`.\n\nFilterable properties: application, archived, assignedState, createdAt, deviceType, id, location, macAddress, model, partNumber, region, serialNumber, subscription, tags, tenantWorkspaceId, type, updatedAt, warranty",
                },
                "sort": {
                    "type": "string",
                    "description": "A comma separated list of sort expressions. A sort expression is a property name optionally followed by a direction indicator `asc` or `desc`. The default is ascending order.\n\nExample: serialNumber,macAddress desc",
                },
                "select": {
                    "type": "array",
                    "description": "A comma separated list of select properties to display in the response. The default is that all properties are returned.\n\nExample: serialNumber,macAddress",
                    "items": {"type": "string"},
                    "uniqueItems": True,
                },
                "limit": {
                    "type": ["integer", "string"],  # Accept both for LLM client compatibility
                    "description": "Specifies the number of results to be returned. The default value is 2000.",
                    "default": 2000,
                },
                "offset": {
                    "type": ["integer", "string"],  # Accept both for LLM client compatibility
                    "description": "Specifies the zero-based resource offset to start the response from. The default value is 0.",
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
        Execute the getdevicesv1 tool.

        Args:
            arguments: Tool arguments

        Returns:
            List of results
        """
        try:
            # Validate arguments
            self.validate_arguments(arguments)

            # Extract parameters
            # Parameter: filter
            # Parameter: filter-tags
            # Parameter: sort
            # Parameter: select
            # Parameter: limit
            # Parameter: offset

            # Build URL with path parameters
            url = "/devices/v1/devices"

            # Prepare query/body parameters
            params: Dict[str, Any] = {}
            # Parameter: filter
            param_value = arguments.get("filter")
            if param_value is not None:
                params["filter"] = param_value
            # Parameter: filter-tags
            param_value = arguments.get("filter-tags")
            if param_value is not None:
                params["filter-tags"] = param_value
            # Parameter: sort
            param_value = arguments.get("sort")
            if param_value is not None:
                params["sort"] = param_value
            # Parameter: select
            param_value = arguments.get("select")
            if param_value is not None:
                params["select"] = param_value
            # Parameter: limit (integer - will coerce strings)
            param_value = arguments.get("limit", 2000)
            # Coerce string to integer for LLM client compatibility
            if param_value is not None:
                param_value = self.coerce_string_to_int(param_value, "limit")
            if param_value is not None:
                params["limit"] = param_value
            # Parameter: offset (integer - will coerce strings)
            param_value = arguments.get("offset")
            # Coerce string to integer for LLM client compatibility
            if param_value is not None:
                param_value = self.coerce_string_to_int(param_value, "offset")
            if param_value is not None:
                params["offset"] = param_value

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
