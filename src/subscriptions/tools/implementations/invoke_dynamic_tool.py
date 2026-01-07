# (c) Copyright 2025 Hewlett Packard Enterprise Development LP
"""
invoke_dynamic_tool tool implementation for subscriptions MCP server.

This tool can execute any API endpoint dynamically using endpoint identifier and schema validation.
Generated for dynamic mode when OpenAPI spec has 2 endpoints (>= 50 threshold).
"""

from typing import Any, Dict, List, cast
from tools.base import BaseTool


class InvokeDynamicTool(BaseTool):
    """Executes any subscriptions API endpoint dynamically with schema validation."""

    @property
    def name(self) -> str:
        """Tool name."""
        return "invoke_dynamic_tool"

    @property
    def description(self) -> str:
        """Tool description."""
        return "Executes any subscriptions API endpoint dynamically with parameter validation and schema support"

    @property
    def input_schema(self) -> Dict[str, Any]:
        """Input schema for the tool."""
        return {
            "type": "object",
            "properties": {
                "endpoint_identifier": {
                    "type": "string",
                    "description": "Endpoint identifier in METHOD:PATH format (e.g., 'GET:/users/{id}', 'GET:/compute/volumes')",
                    "pattern": "^GET:",
                },
                "parameters": {
                    "type": "object",
                    "description": "Request parameters (path and query parameters only)",
                    "default": {},
                },
                "headers": {
                    "type": "object",
                    "description": "Additional HTTP headers to include in the request",
                    "default": {},
                },
                "validate_schema": {
                    "type": "boolean",
                    "description": "Validate request parameters against OpenAPI schema",
                    "default": True,
                },
            },
            "required": ["endpoint_identifier"],
        }

    async def execute(self, arguments: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Execute an API endpoint dynamically using endpoint identifier."""
        try:
            # Extract arguments
            endpoint_identifier = arguments.get("endpoint_identifier", "").strip()
            parameters = cast(Dict[str, Any], arguments.get("parameters", {}))
            headers = arguments.get("headers", {})
            validate_schema = arguments.get("validate_schema", True)

            if not endpoint_identifier:
                return [
                    {
                        "success": False,
                        "error": "endpoint_identifier is required",
                        "message": "Please provide an endpoint identifier in METHOD:PATH format",
                    }
                ]

            # Parse endpoint identifier
            if ":" not in endpoint_identifier:
                return [
                    {
                        "success": False,
                        "error": "Invalid endpoint identifier format",
                        "message": "Expected format: METHOD:PATH (e.g., 'GET:/api/v1/users')",
                    }
                ]

            method, path = endpoint_identifier.split(":", 1)
            method = method.upper()

            # Get endpoint schema for validation
            endpoint_schemas: Dict[str, Any] = {
                "GET:/subscriptions/v1/subscriptions": {
                    "path": "/subscriptions/v1/subscriptions",
                    "method": "GET",
                    "summary": "getsubscriptionsv1",
                    "description": "getsubscriptionsv1",
                    "parameters": [
                        {
                            "name": "filter",
                            "type": "str",
                            "description": "filter",
                            "required": False,
                            "location": "query",
                        },
                        {
                            "name": "filter-tags",
                            "type": "str",
                            "description": "filter-tags",
                            "required": False,
                            "location": "query",
                        },
                        {"name": "sort", "type": "str", "description": "sort", "required": False, "location": "query"},
                        {
                            "name": "select",
                            "type": "List[str]",
                            "description": "select",
                            "required": False,
                            "location": "query",
                        },
                        {
                            "name": "limit",
                            "type": "int",
                            "description": "limit",
                            "required": False,
                            "location": "query",
                            "default": "50",
                        },
                        {
                            "name": "offset",
                            "type": "int",
                            "description": "offset",
                            "required": False,
                            "location": "query",
                        },
                    ],
                },
                "GET:/subscriptions/v1/subscriptions/{id}": {
                    "path": "/subscriptions/v1/subscriptions/{id}",
                    "method": "GET",
                    "summary": "getsubscriptiondetailsbyidv1",
                    "description": "getsubscriptiondetailsbyidv1",
                    "parameters": [
                        {"name": "id", "type": "str", "description": "id", "required": True, "location": "path"},
                    ],
                },
            }

            if endpoint_identifier not in endpoint_schemas:
                available_endpoints = list(endpoint_schemas.keys())
                return [
                    {
                        "success": False,
                        "error": f"Endpoint not found: {endpoint_identifier}",
                        "message": f"Available endpoints: {', '.join(available_endpoints[:5])}{'...' if len(available_endpoints) > 5 else ''}",
                    }
                ]

            schema = cast(Dict[str, Any], endpoint_schemas[endpoint_identifier])

            # Validate parameters if requested
            if validate_schema:
                validation_errors = self._validate_parameters(parameters, schema)
                if validation_errors:
                    return [
                        {
                            "success": False,
                            "error": "Parameter validation failed",
                            "validation_errors": validation_errors,
                            "schema": schema,
                        }
                    ]

            # Build final URL and separate path/query parameters
            final_url, query_params = self._build_request_url(path, parameters, schema)

            # Execute the request (read-only operations only)
            if method == "GET":
                response_data = await self.http_client.get(final_url, params=query_params, additional_headers=headers)
            else:
                return [
                    {
                        "success": False,
                        "error": f"Unsupported HTTP method: {method}",
                        "message": "This MCP server only supports read operations (GET methods)",
                    }
                ]

            return [
                {
                    "success": True,
                    "endpoint_identifier": endpoint_identifier,
                    "request": {"url": final_url, "method": method, "query_params": query_params, "headers": headers},
                    "response": response_data,
                }
            ]

        except Exception as e:
            return [
                {
                    "success": False,
                    "error": f"Request failed: {str(e)}",
                    "message": "An error occurred while executing the API request",
                }
            ]

    def _validate_parameters(self, parameters: Dict[str, Any], schema: Dict[str, Any]) -> List[str]:
        """Validate parameters against endpoint schema."""
        errors = []
        schema_params = {p["name"]: p for p in schema.get("parameters", [])}

        # Check required parameters
        for param_name, param_def in schema_params.items():
            if param_def["required"] and param_name not in parameters:
                errors.append(f"Required parameter '{param_name}' is missing")

        # Validate parameter types (basic validation)
        for param_name, param_value in parameters.items():
            if param_name not in schema_params:
                errors.append(f"Unknown parameter '{param_name}' not defined in schema")
                continue

            param_def = schema_params[param_name]
            expected_type = param_def["type"]

            # Basic type validation
            if expected_type == "integer" and not isinstance(param_value, int):
                try:
                    int(param_value)
                except (ValueError, TypeError):
                    errors.append(f"Parameter '{param_name}' should be an integer")
            elif expected_type == "boolean" and not isinstance(param_value, bool):
                if str(param_value).lower() not in ["true", "false", "1", "0"]:
                    errors.append(f"Parameter '{param_name}' should be a boolean")

        return errors

    def _build_request_url(
        self, base_path: str, parameters: Dict[str, Any], schema: Dict[str, Any]
    ) -> tuple[str, Dict[str, Any]]:
        """Build the final request URL and separate query parameters."""
        url = base_path
        query_params: Dict[str, Any] = {}

        schema_params = {p["name"]: p for p in schema.get("parameters", [])}

        for param_name, param_value in parameters.items():
            if param_name not in schema_params:
                continue

            param_def = schema_params[param_name]
            location = param_def.get("location", "query")
            param_type = param_def.get("type", "string")

            if location == "path":
                # Replace path parameter
                url = url.replace("{" + param_name + "}", str(param_value))
            else:
                # Query parameter - apply type coercion for integers
                if param_type == "integer":
                    try:
                        param_value = self.coerce_string_to_int(param_value, param_name)
                    except ValueError:
                        # If coercion fails, use original value (validation will catch it)
                        pass
                query_params[param_name] = param_value

        return url, query_params
