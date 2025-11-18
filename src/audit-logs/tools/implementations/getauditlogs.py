# (c) Copyright 2025 Hewlett Packard Enterprise Development LP
"""
getauditlogs tool implementation for audit-logs MCP server.

This tool The audit logs can be filtered using a variety of parameters. Queries should be separated by `and` and can utilize `eq`, `contains`, and `in` operators to construct the final query. Each query should follow the format:
* key eq 'value' for equality operation.
* contains(key, 'value') for contains operation.
* key in ('value1', 'value2') for in operation.

| Filter parameter         | Supported Operators | Type                    | Example                                                                                         |
|--------------------------|---------------------|-------------------------|-------------------------------------------------------------------------------------------------|
| createdAt                | lt, ge              | RFC timestamp in string | createdAt ge '2024-02-16T07:54:55.0Z'                                                           |
| category                 | eq, in              | string                  | category eq 'User Management' category in ('Device Management', 'User Activity')                |
| description              | eq, contains        | string                  | contains(description, 'Logged in') description eq 'User test@test.com logged in via ping mode.' |
| additionalInfo/ipAddress | eq, contains        | IP string               | additionalInfo/ipAddress eq '192.168.12.12' contains(additionalInfo/ipAddress, '192.168')       |
| user/username            | eq, contains        | email in string         | user/username eq 'test@test.com' contains(user/username, '@gmail.com')                          |
| workspace/workspaceName  | eq, contains        | string                  | workspace/workspaceName eq 'Example workspace' contains(workspace/workspaceName, 'Example')     |
| application/id           | eq                  | UUID in string          | application/id eq '12312-123123-123123-123121'                                                  |
| region                   | eq                  | region code in string   | region eq 'us-west'                                                                             |
| hasDetails               | eq                  | boolean                 | hasDetails eq 'true'                                                                              |
.
"""

from typing import Any, Dict, List
from tools.base import BaseTool


class getauditlogsTool(BaseTool):
    """The audit logs can be filtered using a variety of parameters. Queries should be separated by `and` and can utilize `eq`, `contains`, and `in` operators to construct the final query. Each query should follow the format:\n* key eq 'value' for equality operation.\n* contains(key, 'value') for contains operation.\n* key in ('value1', 'value2') for in operation.\n\n| Filter parameter         | Supported Operators | Type                    | Example                                                                                         |\n|--------------------------|---------------------|-------------------------|-------------------------------------------------------------------------------------------------|\n| createdAt                | lt, ge              | RFC timestamp in string | createdAt ge '2024-02-16T07:54:55.0Z'                                                           |\n| category                 | eq, in              | string                  | category eq 'User Management' category in ('Device Management', 'User Activity')                |\n| description              | eq, contains        | string                  | contains(description, 'Logged in') description eq 'User test@test.com logged in via ping mode.' |\n| additionalInfo/ipAddress | eq, contains        | IP string               | additionalInfo/ipAddress eq '192.168.12.12' contains(additionalInfo/ipAddress, '192.168')       |\n| user/username            | eq, contains        | email in string         | user/username eq 'test@test.com' contains(user/username, '@gmail.com')                          |\n| workspace/workspaceName  | eq, contains        | string                  | workspace/workspaceName eq 'Example workspace' contains(workspace/workspaceName, 'Example')     |\n| application/id           | eq                  | UUID in string          | application/id eq '12312-123123-123123-123121'                                                  |\n| region                   | eq                  | region code in string   | region eq 'us-west'                                                                             |\n| hasDetails               | eq                  | boolean                 | hasDetails eq 'true'                                                                              |\n"""

    @property
    def name(self) -> str:
        """Tool name."""
        return "getauditlogs"

    @property
    def description(self) -> str:
        """Tool description."""
        return "The audit logs can be filtered using a variety of parameters. Queries should be separated by `and` and can utilize `eq`, `contains`, and `in` operators to construct the final query. Each query should follow the format:\n* key eq 'value' for equality operation.\n* contains(key, 'value') for contains operation.\n* key in ('value1', 'value2') for in operation.\n\n| Filter parameter         | Supported Operators | Type                    | Example                                                                                         |\n|--------------------------|---------------------|-------------------------|-------------------------------------------------------------------------------------------------|\n| createdAt                | lt, ge              | RFC timestamp in string | createdAt ge '2024-02-16T07:54:55.0Z'                                                           |\n| category                 | eq, in              | string                  | category eq 'User Management' category in ('Device Management', 'User Activity')                |\n| description              | eq, contains        | string                  | contains(description, 'Logged in') description eq 'User test@test.com logged in via ping mode.' |\n| additionalInfo/ipAddress | eq, contains        | IP string               | additionalInfo/ipAddress eq '192.168.12.12' contains(additionalInfo/ipAddress, '192.168')       |\n| user/username            | eq, contains        | email in string         | user/username eq 'test@test.com' contains(user/username, '@gmail.com')                          |\n| workspace/workspaceName  | eq, contains        | string                  | workspace/workspaceName eq 'Example workspace' contains(workspace/workspaceName, 'Example')     |\n| application/id           | eq                  | UUID in string          | application/id eq '12312-123123-123123-123121'                                                  |\n| region                   | eq                  | region code in string   | region eq 'us-west'                                                                             |\n| hasDetails               | eq                  | boolean                 | hasDetails eq 'true'                                                                              |\n"

    @property
    def input_schema(self) -> Dict[str, Any]:
        """Input schema for the tool."""
        return {
            "type": "object",
            "properties": {
                "filter": {
                    "type": "string",
                    "description": "Example: category eq 'User Management' and contains(description, 'logged out')\n\n**Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`.\n\nFilterable properties: additionalInfo, application, category, createdAt, description, generation, hasDetails, id, region, type, updatedAt, user, workspace",
                },
                "select": {
                    "type": "string",
                    "description": "Use the `select` query parameter to restrict the number of properties included in the audit log response.\nThe supported select parameters:\n * additionalInfo\n * createdAt\n * category\n * hasDetails\n * workspace/workspaceName\n * description\n * user/username\n\n\nExample: createdAt, user/username, category",
                },
                "all": {
                    "type": "string",
                    "description": "Provide a free-text search to perform a comprehensive search across all properties for audit logs.\n\nExample: logged in user",
                },
                "limit": {
                    "type": ["integer", "string"],  # Accept both for LLM client compatibility
                    "description": "How many items to return at one time (max 2000)",
                    "default": 50,
                },
                "offset": {
                    "type": ["integer", "string"],  # Accept both for LLM client compatibility
                    "description": "Specifies the zero-based resource offset to start the response from.",
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
        Execute the getauditlogs tool.

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
            # Parameter: select
            # Parameter: all
            # Parameter: limit
            # Parameter: offset

            # Build URL with path parameters
            url = "/audit-log/v1/logs"

            # Prepare query/body parameters
            params: Dict[str, Any] = {}
            # Parameter: filter
            param_value = arguments.get("filter")
            if param_value is not None:
                params["filter"] = param_value
            # Parameter: select
            param_value = arguments.get("select")
            if param_value is not None:
                params["select"] = param_value
            # Parameter: all
            param_value = arguments.get("all")
            if param_value is not None:
                params["all"] = param_value
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
