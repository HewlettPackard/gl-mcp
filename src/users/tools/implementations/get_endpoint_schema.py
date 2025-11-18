# (c) Copyright 2025 Hewlett Packard Enterprise Development LP
"""
get_endpoint_schema tool implementation for users MCP server.

This tool retrieves detailed schema information for a specific API endpoint using endpoint identifier.
Generated for dynamic mode when OpenAPI spec has 0 endpoints (>= 50 threshold).
"""

from typing import Any, Dict, List
from tools.base import BaseTool


class GetEndpointSchemaTool(BaseTool):
    """Retrieves detailed schema information for a specific users API endpoint including parameters, request/response models, and validation rules"""

    @property
    def name(self) -> str:
        """Tool name."""
        return "get_endpoint_schema"

    @property
    def description(self) -> str:
        """Tool description."""
        return "Retrieves detailed schema information for a specific users API endpoint including parameters, request/response models, and validation rules"

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
                        "GET:/identity/v1/users",
                        "GET:/identity/v1/users/{id}",
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
                "GET:/identity/v1/users": {
                    "path": "/identity/v1/users",
                    "method": "GET",
                    "summary": "get_users_identity_v1_users_get",
                    "description": "get_users_identity_v1_users_get",
                    "operationId": "get_users_identity_v1_users_get",
                    "tags": [],
                    "deprecated": False,
                    "parameters": [
                        {
                            "name": "filter",
                            "type": "str",
                            "description": "Filter data using a subset of OData 4.0 and return only the subset of resources that match the filter.\n\nSupported classes and examples include:\n- **Types**: timestamp, string\n- **Comparison**: eq, ne, gt, ge, lt\n- **Logical Expressions**: and, or, not\n\nThe Get users API can be filtered by:\n- id\n- username\n- userStatus\n- createdAt\n- updatedAt\n- lastLogin\n\nuserStatus can be one of the following:\n- UNVERIFIED\n- VERIFIED\n- BLOCKED\n- DELETE_IN_PROGRESS\n- DELETED\n- SUSPENDED\n\n**Note**: The userStatus filter is case-sensitive.\n\nExamples:\n  - updatedAt gt '2020-09-21T14:19:09.769747'\n    Returns users updated after 2020-09-21T14:19:09.769747\n  - userStatus ne 'UNVERIFIED'\n    Returns users that are not unverified.\n  - username eq 'user@example.com'\n    Returns the user with a specific username.\n  - createdAt gt '2020-09-21T14:19:09.769747'\n    Returns users created after 2020-09-21T14:19:09.769747\n  - username eq 'user@example.com'\n    Returns the user with a specific email.\n  - id eq '7600415a-8876-5722-9f3c-b0fd11112283'\n    Returns the user with a specific ID.\n  - lastLogin lt '2020-09-21T14:19:09.769747'\n    Returns users that logged in before 2020-09-21T14:19:09.769747\n\n**Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`.\n\nFilterable properties: createdAt, generation, id, lastLogin, resourceUri, type, updatedAt, userStatus, username",
                            "required": False,
                            "location": "query",
                            "schema": {
                                "type": "string",
                                "description": "Filter data using a subset of OData 4.0 and return only the subset of resources that match the filter.\n\nSupported classes and examples include:\n- **Types**: timestamp, string\n- **Comparison**: eq, ne, gt, ge, lt\n- **Logical Expressions**: and, or, not\n\nThe Get users API can be filtered by:\n- id\n- username\n- userStatus\n- createdAt\n- updatedAt\n- lastLogin\n\nuserStatus can be one of the following:\n- UNVERIFIED\n- VERIFIED\n- BLOCKED\n- DELETE_IN_PROGRESS\n- DELETED\n- SUSPENDED\n\n**Note**: The userStatus filter is case-sensitive.\n\nExamples:\n  - updatedAt gt '2020-09-21T14:19:09.769747'\n    Returns users updated after 2020-09-21T14:19:09.769747\n  - userStatus ne 'UNVERIFIED'\n    Returns users that are not unverified.\n  - username eq 'user@example.com'\n    Returns the user with a specific username.\n  - createdAt gt '2020-09-21T14:19:09.769747'\n    Returns users created after 2020-09-21T14:19:09.769747\n  - username eq 'user@example.com'\n    Returns the user with a specific email.\n  - id eq '7600415a-8876-5722-9f3c-b0fd11112283'\n    Returns the user with a specific ID.\n  - lastLogin lt '2020-09-21T14:19:09.769747'\n    Returns users that logged in before 2020-09-21T14:19:09.769747\n\n**Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`.\n\nFilterable properties: createdAt, generation, id, lastLogin, resourceUri, type, updatedAt, userStatus, username",
                            },
                        },
                        {
                            "name": "offset",
                            "type": "int",
                            "description": "Specify pagination offset. An offset argument defines how many pages to skip before returning results.",
                            "required": False,
                            "location": "query",
                            "schema": {
                                "type": "integer",
                                "description": "Specify pagination offset. An offset argument defines how many pages to skip before returning results.",
                            },
                        },
                        {
                            "name": "limit",
                            "type": "int",
                            "description": "Specify the maximum number of entries per page. NOTE: The maximum value accepted is 600.",
                            "required": False,
                            "location": "query",
                            "default": 300,
                            "schema": {
                                "type": "integer",
                                "description": "Specify the maximum number of entries per page. NOTE: The maximum value accepted is 600.",
                                "default": "300",
                            },
                        },
                    ],
                    "security": [],
                    "responses": {"200": {"description": "Successful response", "content_type": "application/json"}},
                },
                "GET:/identity/v1/users/{id}": {
                    "path": "/identity/v1/users/{id}",
                    "method": "GET",
                    "summary": "get_user_detailed_identity_v1_users_id_get",
                    "description": "get_user_detailed_identity_v1_users_id_get",
                    "operationId": "get_user_detailed_identity_v1_users_id_get",
                    "tags": [],
                    "deprecated": False,
                    "parameters": [
                        {
                            "name": "id",
                            "type": "str",
                            "description": "The unique identifier of the user.\n\nExample: 7600415a-8876-5722-9f3c-b0fd11112283",
                            "required": True,
                            "location": "query",
                            "schema": {
                                "type": "string",
                                "description": "The unique identifier of the user.\n\nExample: 7600415a-8876-5722-9f3c-b0fd11112283",
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
