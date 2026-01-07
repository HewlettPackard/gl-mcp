# (c) Copyright 2025 Hewlett Packard Enterprise Development LP
"""
get_users_identity_v1_users_get tool implementation for users MCP server.

This tool Retrieve list of users with filtering, and pagination options. All users are returned when no filters are provided.
**Note**: User view all permission is required to invoke this API.
Rate limit: 300 requests per minute per workspace, resulting in a `429` error if exceeded.
.
"""

from typing import Any, Dict, List
from tools.base import BaseTool


class get_users_identity_v1_users_getTool(BaseTool):
    """Retrieve list of users with filtering, and pagination options. All users are returned when no filters are provided. \n**Note**: User view all permission is required to invoke this API. \nRate limit: 300 requests per minute per workspace, resulting in a `429` error if exceeded.\n"""

    @property
    def name(self) -> str:
        """Tool name."""
        return "get_users_identity_v1_users_get"

    @property
    def description(self) -> str:
        """Tool description."""
        return "Retrieve list of users with filtering, and pagination options. All users are returned when no filters are provided. \n**Note**: User view all permission is required to invoke this API. \nRate limit: 300 requests per minute per workspace, resulting in a `429` error if exceeded.\n"

    @property
    def input_schema(self) -> Dict[str, Any]:
        """Input schema for the tool."""
        return {
            "type": "object",
            "properties": {
                "filter": {
                    "type": "string",
                    "description": "Filter data using a subset of OData 4.0 and return only the subset of resources that match the filter.\n\nSupported classes and examples include:\n- **Types**: timestamp, string\n- **Comparison**: eq, ne, gt, ge, lt\n- **Logical Expressions**: and, or, not\n\nThe Get users API can be filtered by:\n- id\n- username\n- userStatus\n- createdAt\n- updatedAt\n- lastLogin\n\nuserStatus can be one of the following:\n- UNVERIFIED\n- VERIFIED\n- BLOCKED\n- DELETE_IN_PROGRESS\n- DELETED\n- SUSPENDED\n\n**Note**: The userStatus filter is case-sensitive.\n\nExamples:\n  - userStatus ne 'UNVERIFIED'\n    Returns users that are not unverified.\n  - username eq 'user@example.com'\n    Returns the user with a specific username.\n  - createdAt gt '2020-09-21T14:19:09.769747'\n    Returns users created after 2020-09-21T14:19:09.769747\n  - username eq 'user@example.com'\n    Returns the user with a specific email.\n  - id eq '7600415a-8876-5722-9f3c-b0fd11112283'\n    Returns the user with a specific ID.\n  - lastLogin lt '2020-09-21T14:19:09.769747'\n    Returns users that logged in before 2020-09-21T14:19:09.769747\n  - updatedAt gt '2020-09-21T14:19:09.769747'\n    Returns users updated after 2020-09-21T14:19:09.769747\n\n**Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`.\n\nFilterable properties: createdAt, generation, id, lastLogin, resourceUri, type, updatedAt, userStatus, username",
                },
                "offset": {
                    "type": ["integer", "string"],  # Accept both for LLM client compatibility
                    "description": "Specify pagination offset. An offset argument defines how many pages to skip before returning results.",
                },
                "limit": {
                    "type": ["integer", "string"],  # Accept both for LLM client compatibility
                    "description": "Specify the maximum number of entries per page. NOTE: The maximum value accepted is 600.",
                    "default": 300,
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
        Execute the get_users_identity_v1_users_get tool.

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
            # Parameter: offset
            # Parameter: limit

            # Build URL with path parameters
            url = "/identity/v1/users"

            # Prepare query/body parameters
            params: Dict[str, Any] = {}
            # Parameter: filter
            param_value = arguments.get("filter")
            if param_value is not None:
                params["filter"] = param_value
            # Parameter: offset (integer - will coerce strings)
            param_value = arguments.get("offset")
            # Coerce string to integer for LLM client compatibility
            if param_value is not None:
                param_value = self.coerce_string_to_int(param_value, "offset")
            if param_value is not None:
                params["offset"] = param_value
            # Parameter: limit (integer - will coerce strings)
            param_value = arguments.get("limit", 300)
            # Coerce string to integer for LLM client compatibility
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
