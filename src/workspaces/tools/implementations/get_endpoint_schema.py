# (c) Copyright 2025 Hewlett Packard Enterprise Development LP
"""
get_endpoint_schema tool implementation for workspaces MCP server.

This tool retrieves detailed schema information for a specific API endpoint using endpoint identifier.
Generated for dynamic mode when OpenAPI spec has 0 endpoints (>= 50 threshold).
"""

from typing import Any, Dict, List
from tools.base import BaseTool


class GetEndpointSchemaTool(BaseTool):
    """Retrieves detailed schema information for a specific workspaces API endpoint including parameters, request/response models, and validation rules"""

    @property
    def name(self) -> str:
        """Tool name."""
        return "get_endpoint_schema"

    @property
    def description(self) -> str:
        """Tool description."""
        return "Retrieves detailed schema information for a specific workspaces API endpoint including parameters, request/response models, and validation rules"

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
                        "GET:/workspaces/v1/workspaces/{workspaceId}",
                        "GET:/workspaces/v1/workspaces/{workspaceId}/contact",
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
                "GET:/workspaces/v1/workspaces/{workspaceId}": {
                    "path": "/workspaces/v1/workspaces/{workspaceId}",
                    "method": "GET",
                    "summary": "get_workspace_workspaces_v1_workspaces_workspaceid_get",
                    "description": "get_workspace_workspaces_v1_workspaces_workspaceid_get",
                    "operationId": "get_workspace_workspaces_v1_workspaces_workspaceid_get",
                    "tags": [],
                    "deprecated": False,
                    "parameters": [
                        {
                            "name": "workspaceId",
                            "type": "str",
                            "description": "The unique identifier of the workspace.\n\nExample: 7600415a-8876-5722-9f3c-b0fd11112283",
                            "required": True,
                            "location": "query",
                            "schema": {
                                "type": "string",
                                "description": "The unique identifier of the workspace.\n\nExample: 7600415a-8876-5722-9f3c-b0fd11112283",
                            },
                        },
                    ],
                    "security": [],
                    "responses": {"200": {"description": "Successful response", "content_type": "application/json"}},
                },
                "GET:/workspaces/v1/workspaces/{workspaceId}/contact": {
                    "path": "/workspaces/v1/workspaces/{workspaceId}/contact",
                    "method": "GET",
                    "summary": "get_workspace_detailed_info_workspaces_v1_workspaces_wo_5c14f2bc",
                    "description": "get_workspace_detailed_info_workspaces_v1_workspaces_wo_5c14f2bc",
                    "operationId": "get_workspace_detailed_info_workspaces_v1_workspaces_wo_5c14f2bc",
                    "tags": [],
                    "deprecated": False,
                    "parameters": [
                        {
                            "name": "workspaceId",
                            "type": "str",
                            "description": "The unique identifier of the workspace.\n\nExample: 7600415a-8876-5722-9f3c-b0fd11112283",
                            "required": True,
                            "location": "query",
                            "schema": {
                                "type": "string",
                                "description": "The unique identifier of the workspace.\n\nExample: 7600415a-8876-5722-9f3c-b0fd11112283",
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
