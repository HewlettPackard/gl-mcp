# (c) Copyright 2025 Hewlett Packard Enterprise Development LP
"""
getsubscriptionsv1 tool implementation for subscriptions MCP server.

This tool Get subscriptions managed in a workspace. Filters can be passed to filter  the subscriptions based on conditional expressions.<br><br>**NOTE:** You need to have  view permission for the **Devices and subscription service** to invoke this API. <br><br> Rate limits are enforced on this API. 60 requests per minute is supported per workspace. API will result in `429` if this threshold is breached..
"""

from typing import Any, Dict, List
from tools.base import BaseTool


class getsubscriptionsv1Tool(BaseTool):
    """Get subscriptions managed in a workspace. Filters can be passed to filter  the subscriptions based on conditional expressions.<br><br>**NOTE:** You need to have  view permission for the **Devices and subscription service** to invoke this API. <br><br> Rate limits are enforced on this API. 60 requests per minute is supported per workspace. API will result in `429` if this threshold is breached."""

    @property
    def name(self) -> str:
        """Tool name."""
        return "getsubscriptionsv1"

    @property
    def description(self) -> str:
        """Tool description."""
        return "Get subscriptions managed in a workspace. Filters can be passed to filter  the subscriptions based on conditional expressions.<br><br>**NOTE:** You need to have  view permission for the **Devices and subscription service** to invoke this API. <br><br> Rate limits are enforced on this API. 60 requests per minute is supported per workspace. API will result in `429` if this threshold is breached."

    @property
    def input_schema(self) -> Dict[str, Any]:
        """Input schema for the tool."""
        return {
            "type": "object",
            "properties": {
                "filter": {
                    "type": "string",
                    "description": "Filter expressions consisting of simple comparison operations joined \nby logical operators.<br>\n| CLASS                |   EXAMPLES                                         |\n|----------------------|----------------------------------------------------|\n| Types                | integer, decimal, timestamp, string, boolean, null |\n| Comparison           | eq, ne, gt, ge, lt, le, in                         |\n| Logical Expressions  | and, or, not                                       |\n\nSubscriptions can be filtered based on the following properties:\n- `id`\n- `subscriptionType`\n- `subscriptionStatus`\n- `key`\n- `quantity`\n- `availableQuantity`\n- `sku`\n- `skuDescription`\n- `contract`\n- `startTime`\n- `endTime`\n- `productType`\n- `tier`\n- `createdAt`\n- `updatedAt`\n\nThe following is a non-exhaustive list of possible filtering options.\n\n\nExamples:\n  - tier ne 'BRIDGE'\n    Return subscriptions where a property does not equate to a value. Example syntax, \n<property> ne <value>.\n  - subscriptionType in 'CENTRAL_STORAGE', 'CENTRAL_CONTROLLER'\n    Return subscriptions where the property is one of multiple values. Example syntax, \n<property> in <value>,<value>.\n  - key eq 'STIQQ4L04' and subscriptionType eq 'CENTRAL_STORAGE'\n    The AND operator returns results that meet all filter queries. In the example, the query only returns subscriptions with the exact key and with the specified subscription type. Example syntax,\n<property> eq <value> and <property> eq <value>.\n  - createdAt ge '2024-01-18T19:53:51.480Z'\n    Return subscriptions where a property is greater or equal to a value. Example syntax,\n<property> ge <value>.\n  - updatedAt le '2024-02-18T19:53:51.480Z'\n    Return subscriptions where a property is less than or equal to a value. Example syntax,\n<property> le <value>.\n  - not key eq 'STIAPL6404'\n    Return subscriptions where a property does not equal a value. Example syntax, \nnot <property> eq <value>.\n  - key eq 'STIQQ4L04' or subscriptionType eq 'CENTRAL_STORAGE'\n    The OR operator returns results that meet any of the filter queries. In the example, the query returns subscriptions with the exact key or with the specified subscription type.\n  - key eq 'STIAPL6404'\n    Return subscriptions where a property equals a value. Example syntax, \n<property> eq <value>.\n  - startTime gt '2024-01-23T00:00:00.000Z' and endTime lt '2025-02-22T00:00:00.000Z' and not productType eq 'SERVICE'\n    The AND, OR, and NOT operators can be combined to return results that satisfy all specified filter criteria.\n\n**Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`.\n\nFilterable properties: availableQuantity, contract, createdAt, endTime, id, isEval, key, productType, quantity, sku, skuDescription, startTime, subscriptionStatus, subscriptionType, tags, tier, type, updatedAt",
                },
                "filter-tags": {
                    "type": "string",
                    "description": "Filter expressions consisting of simple comparison operations joined\nby logical operators to be applied on the assigned tags or their\nvalues.<br>\n| CLASS               |   EXAMPLES      |\n|---------------------|-----------------|\n| Types               | string          |\n| Comparison          | eq, ne          |\n| Logical Expressions | and, or         |\n\n\nExamples:\n  - 'city' eq 'London'\n    Return subscriptions that have a pair of tags with the exact same tag key and tag value. Example syntax, \n<tagKey> eq <tagValue>.\n  - 'city' ne 'London'\n    Return subscriptions that have a pair of tags with the exact same tag key and the exact different tag value. Example syntax, \n<tagKey> ne <tagValue>.\n  - 'city' eq 'London' and 'street' eq 'Piccadilly'\n    Return subscriptions containing the tag key and the corresponding value that satisfy all conditionals. Example syntax, \n<property> eq <value> and <property> eq <value>.\n  - 'street' eq 'Oxford Street' or 'street' eq 'Piccadilly'\n    Return subscriptions containing the tag key and the corresponding value that satisfy at least one of the conditionals. Example syntax, \n<property> eq <value> or <property> eq <value>.\n\n**Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`.\n\nFilterable properties: availableQuantity, contract, createdAt, endTime, id, isEval, key, productType, quantity, sku, skuDescription, startTime, subscriptionStatus, subscriptionType, tags, tier, type, updatedAt",
                },
                "sort": {
                    "type": "string",
                    "description": "A comma separated list of sort expressions. A sort expression is a  property name optionally followed by a direction indicator `asc` or  `desc`. The default is ascending order.\n\nExample: key, quote desc",
                },
                "select": {
                    "type": "array",
                    "description": "A comma separated list of select properties to display in the response.  The default is that all properties are returned.\n\nExample: id,key",
                    "items": {"type": "string"},
                    "uniqueItems": True,
                },
                "limit": {
                    "type": ["integer", "string"],  # Accept both for LLM client compatibility
                    "description": "Specifies the number of results to be returned. The default value  is 50.",
                    "default": 50,
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
        Execute the getsubscriptionsv1 tool.

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
            url = "/subscriptions/v1/subscriptions"

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
            param_value = arguments.get("limit", 50)
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
