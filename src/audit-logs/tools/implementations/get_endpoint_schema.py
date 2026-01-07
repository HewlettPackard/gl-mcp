# (c) Copyright 2025 Hewlett Packard Enterprise Development LP
"""
get_endpoint_schema tool implementation for audit-logs MCP server.

This tool retrieves detailed schema information for a specific API endpoint using endpoint identifier.
Generated for dynamic mode when OpenAPI spec has 0 endpoints (>= 50 threshold).
"""

from typing import Any, Dict, List
from tools.base import BaseTool


class GetEndpointSchemaTool(BaseTool):
    """Retrieves detailed schema information for a specific audit-logs API endpoint including parameters, request/response models, and validation rules"""

    @property
    def name(self) -> str:
        """Tool name."""
        return "get_endpoint_schema"

    @property
    def description(self) -> str:
        """Tool description."""
        return "Retrieves detailed schema information for a specific audit-logs API endpoint including parameters, request/response models, and validation rules"

    @property
    def input_schema(self) -> Dict[str, Any]:
        """Input schema for the tool."""
        return {
            "type": "object",
            "properties": {
                "endpoint_identifier": {
                    "type": "string",
                    "description": "The API endpoint identifier in METHOD:PATH format (e.g., 'GET:/api/v1/users/{id}')",
                    "examples": [
                        "GET:/audit-log/v1/logs/{id}/detail",
                        "GET:/audit-log/v1/logs",
                    ],
                },
                "include_examples": {
                    "type": "boolean",
                    "description": "Include example parameter values and request/response examples",
                    "default": False,
                },
                "include_validation": {
                    "type": "boolean",
                    "description": "Include detailed validation rules and constraints",
                    "default": True,
                },
            },
            "required": ["endpoint_identifier"],
        }

    async def execute(self, arguments: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Execute the tool to get detailed endpoint schema."""
        try:
            # Extract arguments
            endpoint_identifier = arguments.get("endpoint_identifier", "").strip()
            include_examples = arguments.get("include_examples", False)
            # include_validation parameter available but not currently used

            if not endpoint_identifier:
                return [
                    {
                        "success": False,
                        "error": "endpoint_identifier is required",
                        "message": "Please provide an endpoint identifier in METHOD:PATH format",
                    }
                ]

            # Create endpoint schema map for fast lookup
            endpoint_schemas: Dict[str, Any] = {
                "GET:/audit-log/v1/logs/{id}/detail": {
                    "path": "/audit-log/v1/logs/{id}/detail",
                    "method": "GET",
                    "summary": "getauditlogdetails",
                    "description": "getauditlogdetails",
                    "operationId": "getauditlogdetails",
                    "tags": [],
                    "deprecated": False,
                    "parameters": [
                        {
                            "name": "id",
                            "type": "str",
                            "description": "Provide the ID of the audit log record that has the `hasDetails` value set to `true` to fetch the additional details.",
                            "required": True,
                            "location": "query",
                            "schema": {
                                "type": "string",
                                "description": "Provide the ID of the audit log record that has the `hasDetails` value set to `true` to fetch the additional details.",
                            },
                        },
                    ],
                    "security": [],
                    "responses": {"200": {"description": "Successful response", "content_type": "application/json"}},
                },
                "GET:/audit-log/v1/logs": {
                    "path": "/audit-log/v1/logs",
                    "method": "GET",
                    "summary": "getauditlogs",
                    "description": "getauditlogs",
                    "operationId": "getauditlogs",
                    "tags": [],
                    "deprecated": False,
                    "parameters": [
                        {
                            "name": "filter",
                            "type": "str",
                            "description": "Example: category eq 'User Management' and contains(description, 'logged out')\n\n**Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`.\n\nFilterable properties: additionalInfo, application, category, createdAt, description, generation, hasDetails, id, region, type, updatedAt, user, workspace",
                            "required": False,
                            "location": "query",
                            "schema": {
                                "type": "string",
                                "description": "Example: category eq 'User Management' and contains(description, 'logged out')\n\n**Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`.\n\nFilterable properties: additionalInfo, application, category, createdAt, description, generation, hasDetails, id, region, type, updatedAt, user, workspace",
                            },
                        },
                        {
                            "name": "select",
                            "type": "str",
                            "description": "Use the `select` query parameter to restrict the number of properties included in the audit log response.\nThe supported select parameters:\n * additionalInfo\n * createdAt\n * category\n * hasDetails\n * workspace/workspaceName\n * description\n * user/username\n\n\nExample: createdAt, user/username, category",
                            "required": False,
                            "location": "query",
                            "schema": {
                                "type": "string",
                                "description": "Use the `select` query parameter to restrict the number of properties included in the audit log response.\nThe supported select parameters:\n * additionalInfo\n * createdAt\n * category\n * hasDetails\n * workspace/workspaceName\n * description\n * user/username\n\n\nExample: createdAt, user/username, category",
                            },
                        },
                        {
                            "name": "all",
                            "type": "str",
                            "description": "Provide a free-text search to perform a comprehensive search across all properties for audit logs.\n\nExample: logged in user",
                            "required": False,
                            "location": "query",
                            "schema": {
                                "type": "string",
                                "description": "Provide a free-text search to perform a comprehensive search across all properties for audit logs.\n\nExample: logged in user",
                            },
                        },
                        {
                            "name": "limit",
                            "type": "int",
                            "description": "How many items to return at one time (max 2000)",
                            "required": False,
                            "location": "query",
                            "default": 50,
                            "schema": {
                                "type": "integer",
                                "description": "How many items to return at one time (max 2000)",
                                "default": "50",
                            },
                        },
                        {
                            "name": "offset",
                            "type": "int",
                            "description": "Specifies the zero-based resource offset to start the response from.",
                            "required": False,
                            "location": "query",
                            "schema": {
                                "type": "integer",
                                "description": "Specifies the zero-based resource offset to start the response from.",
                            },
                        },
                    ],
                    "security": [],
                    "responses": {"200": {"description": "Successful response", "content_type": "application/json"}},
                },
            }

            # Find the matching endpoint
            if endpoint_identifier not in endpoint_schemas:
                available_endpoints = list(endpoint_schemas.keys())
                return [
                    {
                        "success": False,
                        "error": f"Endpoint not found: {endpoint_identifier}",
                        "message": f"Available endpoints: {', '.join(available_endpoints[:10])}{'...' if len(available_endpoints) > 10 else ''}",
                    }
                ]

            schema = endpoint_schemas[endpoint_identifier]

            # Add examples if requested
            if include_examples:
                for param in schema["parameters"]:  # type: ignore[attr-defined]
                    if "example" not in param:
                        param["example"] = self._generate_example_value(param["type"])

            return [{"success": True, "endpoint_identifier": endpoint_identifier, "schema": schema}]

        except Exception as e:
            return [
                {
                    "success": False,
                    "error": f"Failed to retrieve endpoint schema: {str(e)}",
                    "message": "An error occurred while retrieving the endpoint schema",
                }
            ]

    def _generate_example_value(self, param_type: str) -> Any:
        """Generate example values for parameters based on type."""
        examples = {
            "string": "example-value",
            "integer": 123,
            "number": 123.45,
            "boolean": True,
            "array": ["example1", "example2"],
            "object": {"key": "value"},
        }
        return examples.get(param_type, "example-value")
