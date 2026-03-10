# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
invoke_dynamic_tool tool implementation for sustainability MCP server.

This tool can execute any API endpoint dynamically using endpoint identifier and schema validation.
Generated for dynamic mode when OpenAPI spec has 13 endpoints (>= 50 threshold).
"""

from typing import Any, Dict, List, cast
from urllib.parse import quote
from tools.base import BaseTool

# Headers that cannot be overridden by user input for security reasons
FORBIDDEN_HEADERS = frozenset(
    [
        "authorization",
        "host",
        "cookie",
        "set-cookie",
        "x-forwarded-for",
        "x-forwarded-host",
        "x-forwarded-proto",
        "x-real-ip",
        "proxy-authorization",
        "www-authenticate",
        "proxy-authenticate",
    ]
)


class InvokeDynamicTool(BaseTool):
    """Executes any sustainability API endpoint dynamically with schema validation."""

    @property
    def name(self) -> str:
        """Tool name."""
        return "invoke_dynamic_tool"

    @property
    def description(self) -> str:
        """Tool description."""
        return "Executes any sustainability API endpoint dynamically with parameter validation and schema support"

    @property
    def input_schema(self) -> Dict[str, Any]:
        """Input schema for the tool."""
        return {
            "type": "object",
            "properties": {
                "endpoint_identifier": {
                    "type": "string",
                    "description": "Endpoint identifier in METHOD:PATH format (e.g., 'GET:/sustainability-insight-ctr/v1beta1/usage-totals', 'POST:/sustainability-insight-ctr/v1beta1/forecast/energy')",
                    "pattern": "^(GET|POST):",
                },
                "parameters": {
                    "type": "object",
                    "description": "Request parameters (path and query parameters for GET, body parameters for POST)",
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
            raw_headers = arguments.get("headers", {})
            validate_schema = arguments.get("validate_schema", True)

            # Sanitize headers - strip security-sensitive headers to prevent injection
            headers = self._sanitize_headers(raw_headers)

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
                        "message": "Expected format: METHOD:PATH (e.g., 'GET:/sustainability-insight-ctr/v1beta1/usage-totals')",
                    }
                ]

            method, path = endpoint_identifier.split(":", 1)
            method = method.upper()

            # Get endpoint schema for validation
            endpoint_schemas: Dict[str, Any] = {
                "GET:/sustainability-insight-ctr/v1beta1/usage-by-entity": {
                    "path": "/sustainability-insight-ctr/v1beta1/usage-by-entity",
                    "method": "GET",
                    "summary": "getusagebyentity",
                    "description": "getusagebyentity",
                    "parameters": [
                        {"name": "start-time", "type": "str", "description": "start-time", "required": True, "location": "query"},
                        {"name": "end-time", "type": "str", "description": "end-time", "required": True, "location": "query"},
                        {"name": "filter", "type": "str", "description": "filter", "required": False, "location": "query"},
                        {"name": "filter-tags", "type": "str", "description": "filter-tags", "required": False, "location": "query"},
                        {"name": "currency", "type": "str", "description": "currency", "required": False, "location": "query"},
                        {"name": "sort", "type": "str", "description": "sort", "required": False, "location": "query"},
                        {"name": "offset", "type": "int", "description": "offset", "required": False, "location": "query"},
                        {"name": "limit", "type": "int", "description": "limit", "required": False, "location": "query"},
                    ],
                },
                "GET:/sustainability-insight-ctr/v1beta1/usage-totals": {
                    "path": "/sustainability-insight-ctr/v1beta1/usage-totals",
                    "method": "GET",
                    "summary": "getusagetotals",
                    "description": "getusagetotals",
                    "parameters": [
                        {"name": "start-time", "type": "str", "description": "start-time", "required": True, "location": "query"},
                        {"name": "end-time", "type": "str", "description": "end-time", "required": True, "location": "query"},
                        {"name": "filter", "type": "str", "description": "filter", "required": False, "location": "query"},
                        {"name": "filter-tags", "type": "str", "description": "filter-tags", "required": False, "location": "query"},
                        {"name": "currency", "type": "str", "description": "currency", "required": False, "location": "query"},
                    ],
                },
                "GET:/sustainability-insight-ctr/v1beta1/usage-series": {
                    "path": "/sustainability-insight-ctr/v1beta1/usage-series",
                    "method": "GET",
                    "summary": "getusageseries",
                    "description": "getusageseries",
                    "parameters": [
                        {"name": "start-time", "type": "str", "description": "start-time", "required": True, "location": "query"},
                        {"name": "end-time", "type": "str", "description": "end-time", "required": True, "location": "query"},
                        {"name": "interval", "type": "str", "description": "interval", "required": True, "location": "query"},
                        {"name": "filter", "type": "str", "description": "filter", "required": False, "location": "query"},
                        {"name": "filter-tags", "type": "str", "description": "filter-tags", "required": False, "location": "query"},
                        {"name": "currency", "type": "str", "description": "currency", "required": False, "location": "query"},
                    ],
                },
                "GET:/sustainability-insight-ctr/v1beta1/cloud-usage-by-entity": {
                    "path": "/sustainability-insight-ctr/v1beta1/cloud-usage-by-entity",
                    "method": "GET",
                    "summary": "getcloudusagebyentity",
                    "description": "getcloudusagebyentity",
                    "parameters": [
                        {"name": "start-time", "type": "str", "description": "start-time", "required": True, "location": "query"},
                        {"name": "end-time", "type": "str", "description": "end-time", "required": True, "location": "query"},
                        {"name": "filter", "type": "str", "description": "filter", "required": False, "location": "query"},
                        {"name": "sort", "type": "str", "description": "sort", "required": False, "location": "query"},
                        {"name": "offset", "type": "int", "description": "offset", "required": False, "location": "query"},
                        {"name": "limit", "type": "int", "description": "limit", "required": False, "location": "query"},
                    ],
                },
                "GET:/sustainability-insight-ctr/v1beta1/cloud-usage-totals": {
                    "path": "/sustainability-insight-ctr/v1beta1/cloud-usage-totals",
                    "method": "GET",
                    "summary": "getcloudusagetotals",
                    "description": "getcloudusagetotals",
                    "parameters": [
                        {"name": "start-time", "type": "str", "description": "start-time", "required": True, "location": "query"},
                        {"name": "end-time", "type": "str", "description": "end-time", "required": True, "location": "query"},
                        {"name": "filter", "type": "str", "description": "filter", "required": False, "location": "query"},
                    ],
                },
                "GET:/sustainability-insight-ctr/v1beta1/cloud-usage-series": {
                    "path": "/sustainability-insight-ctr/v1beta1/cloud-usage-series",
                    "method": "GET",
                    "summary": "getcloudusageseries",
                    "description": "getcloudusageseries",
                    "parameters": [
                        {"name": "start-time", "type": "str", "description": "start-time", "required": True, "location": "query"},
                        {"name": "end-time", "type": "str", "description": "end-time", "required": True, "location": "query"},
                        {"name": "interval", "type": "str", "description": "interval", "required": True, "location": "query"},
                        {"name": "filter", "type": "str", "description": "filter", "required": False, "location": "query"},
                    ],
                },
                "GET:/sustainability-insight-ctr/v1beta1/coefficients": {
                    "path": "/sustainability-insight-ctr/v1beta1/coefficients",
                    "method": "GET",
                    "summary": "getcoefficients",
                    "description": "getcoefficients",
                    "parameters": [
                        {"name": "filter", "type": "str", "description": "filter", "required": False, "location": "query"},
                        {"name": "filter-tags", "type": "str", "description": "filter-tags", "required": False, "location": "query"},
                        {"name": "currency", "type": "str", "description": "currency", "required": False, "location": "query"},
                        {"name": "offset", "type": "int", "description": "offset", "required": False, "location": "query"},
                        {"name": "limit", "type": "int", "description": "limit", "required": False, "location": "query"},
                    ],
                },
                "GET:/sustainability-insight-ctr/v1beta1/coefficients/{id}": {
                    "path": "/sustainability-insight-ctr/v1beta1/coefficients/{id}",
                    "method": "GET",
                    "summary": "getcoefficientbyid",
                    "description": "getcoefficientbyid",
                    "parameters": [
                        {"name": "id", "type": "str", "description": "id", "required": True, "location": "path"},
                    ],
                },
                "GET:/sustainability-insight-ctr/v1beta1/ingests": {
                    "path": "/sustainability-insight-ctr/v1beta1/ingests",
                    "method": "GET",
                    "summary": "getingests",
                    "description": "getingests",
                    "parameters": [
                        {"name": "offset", "type": "int", "description": "offset", "required": False, "location": "query"},
                        {"name": "limit", "type": "int", "description": "limit", "required": False, "location": "query"},
                    ],
                },
                "GET:/sustainability-insight-ctr/v1beta1/ingests/{id}": {
                    "path": "/sustainability-insight-ctr/v1beta1/ingests/{id}",
                    "method": "GET",
                    "summary": "getingestbyid",
                    "description": "getingestbyid",
                    "parameters": [
                        {"name": "id", "type": "str", "description": "id", "required": True, "location": "path"},
                    ],
                },
                "GET:/sustainability-insight-ctr/v1beta1/datasources": {
                    "path": "/sustainability-insight-ctr/v1beta1/datasources",
                    "method": "GET",
                    "summary": "getdatasources",
                    "description": "getdatasources",
                    "parameters": [
                        {"name": "offset", "type": "int", "description": "offset", "required": False, "location": "query"},
                        {"name": "limit", "type": "int", "description": "limit", "required": False, "location": "query"},
                    ],
                },
                "GET:/sustainability-insight-ctr/v1beta1/datasources/{id}": {
                    "path": "/sustainability-insight-ctr/v1beta1/datasources/{id}",
                    "method": "GET",
                    "summary": "getdatasourcebyid",
                    "description": "getdatasourcebyid",
                    "parameters": [
                        {"name": "id", "type": "str", "description": "id", "required": True, "location": "path"},
                    ],
                },
                "POST:/sustainability-insight-ctr/v1beta1/forecast/energy": {
                    "path": "/sustainability-insight-ctr/v1beta1/forecast/energy",
                    "method": "POST",
                    "summary": "forecastenergy",
                    "description": "forecastenergy",
                    "parameters": [
                        {"name": "timePeriodMonths", "type": "int", "description": "timePeriodMonths", "required": True, "location": "body"},
                        {"name": "currencyCode", "type": "str", "description": "currencyCode", "required": True, "location": "body"},
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
            if method == "GET":
                final_url, query_params = self._build_request_url(path, parameters, schema)
                response_data = await self.http_client.get(final_url, params=query_params, additional_headers=headers)
            elif method == "POST":
                final_url, body_params = self._build_request_body(path, parameters, schema)
                response_data = await self.http_client.post(final_url, data=body_params, additional_headers=headers)
            else:
                return [
                    {
                        "success": False,
                        "error": f"Unsupported HTTP method: {method}",
                        "message": "This MCP server only supports GET and POST methods",
                    }
                ]

            return [
                {
                    "success": True,
                    "endpoint_identifier": endpoint_identifier,
                    "request": {"url": final_url, "method": method, "headers": headers},
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
            if expected_type in ("integer", "int") and not isinstance(param_value, int):
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
                # Replace path parameter (URL-encoded to prevent path traversal)
                url = url.replace("{" + param_name + "}", quote(str(param_value), safe=""))
            else:
                # Query parameter - apply type coercion for integers
                if param_type in ("integer", "int"):
                    try:
                        param_value = self.coerce_string_to_int(param_value, param_name)
                    except ValueError:
                        pass
                query_params[param_name] = param_value

        return url, query_params

    def _build_request_body(
        self, base_path: str, parameters: Dict[str, Any], schema: Dict[str, Any]
    ) -> tuple[str, Dict[str, Any]]:
        """Build the final request URL and body for POST requests."""
        url = base_path
        body: Dict[str, Any] = {}

        schema_params = {p["name"]: p for p in schema.get("parameters", [])}

        for param_name, param_value in parameters.items():
            if param_name not in schema_params:
                continue

            param_def = schema_params[param_name]
            location = param_def.get("location", "body")
            param_type = param_def.get("type", "string")

            if location == "path":
                url = url.replace("{" + param_name + "}", quote(str(param_value), safe=""))
            elif location == "body":
                if param_type in ("integer", "int"):
                    try:
                        param_value = self.coerce_string_to_int(param_value, param_name)
                    except ValueError:
                        pass
                body[param_name] = param_value
            else:
                body[param_name] = param_value

        return url, body

    def _sanitize_headers(self, headers: Dict[str, Any]) -> Dict[str, str]:
        """
        Sanitize user-provided headers by removing security-sensitive headers.

        This prevents header injection attacks where a caller could override
        Authorization, Host, Cookie, or other security-critical headers.
        """
        if not headers or not isinstance(headers, dict):
            return {}

        sanitized: Dict[str, str] = {}
        for key, value in headers.items():
            # Normalize header name for comparison
            normalized_key = key.lower().strip()

            # Skip forbidden headers
            if normalized_key in FORBIDDEN_HEADERS:
                self.logger.warning(f"Stripped forbidden header from request: {key}")
                continue

            # Skip headers starting with x-forwarded- pattern
            if normalized_key.startswith("x-forwarded-"):
                self.logger.warning(f"Stripped x-forwarded header from request: {key}")
                continue

            sanitized[key] = str(value)

        return sanitized
