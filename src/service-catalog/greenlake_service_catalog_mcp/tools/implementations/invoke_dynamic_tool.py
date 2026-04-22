# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
invoke_dynamic_tool tool implementation for service-catalog MCP server.

This tool can execute any API endpoint dynamically using endpoint identifier and schema validation.
Generated for dynamic mode when OpenAPI spec has 12 endpoints (>= 50 threshold).
"""

from __future__ import annotations

from typing import Annotated, Any
from urllib.parse import quote

from mcp.server.fastmcp import Context
from pydantic import Field

from greenlake_service_catalog_mcp.config.logging import get_logger
from greenlake_service_catalog_mcp.server.fastmcp_instance import mcp

logger = get_logger(__name__)


@mcp.tool(
    name="invoke_dynamic_tool",
    description="Executes any service-catalog API endpoint dynamically with parameter validation and schema support",
)
async def invoke_dynamic_tool(
    ctx: Context,
    endpoint_identifier: Annotated[
        str,
        Field(
            description="Endpoint identifier in METHOD:PATH format (e.g., 'GET:/api/v1/pets', 'GET:/api/v1/pets/{petId}')",
        ),
    ],
    parameters: Annotated[
        dict[str, Any] | None,
        Field(
            description="Request parameters (path and query parameters only)",
            default=None,
        ),
    ] = None,
    validate_schema: Annotated[
        bool,
        Field(
            description="Validate request parameters against OpenAPI schema before making the request",
            default=True,
        ),
    ] = True,
) -> list[dict[str, Any]]:
    """Executes any service-catalog API endpoint dynamically with parameter validation.

    Args:
        ctx: FastMCP context providing access to the shared HTTP client.
        endpoint_identifier: Endpoint identifier in METHOD:PATH format.
        parameters: Optional dict of path and/or query parameters.
        validate_schema: Whether to validate parameters against the OpenAPI schema.

    Returns:
        A list containing one result dict with the API response or an error message.
    """
    http_client = ctx.request_context.lifespan_context.http_client

    endpoint_identifier = endpoint_identifier.strip()
    params: dict[str, Any] = parameters or {}

    if not endpoint_identifier:
        return [
            {
                "success": False,
                "error": "endpoint_identifier is required",
                "message": "Please provide an endpoint identifier in METHOD:PATH format",
            }
        ]

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
    endpoint_schemas: dict[str, Any] = {
        "GET:/service-catalog/v1beta1/service-offer-regions": {
            "path": "/service-catalog/v1beta1/service-offer-regions",
            "method": "GET",
            "summary": "getserviceofferregions",
            "description": "getserviceofferregions",
            "parameters": [
                {"name": "next", "type": "str", "description": "next", "required": False, "location": "query"},
                {
                    "name": "limit",
                    "type": "int",
                    "description": "limit",
                    "required": False,
                    "location": "query",
                    "default": "2000",
                },
                {"name": "filter", "type": "str", "description": "filter", "required": False, "location": "query"},
            ],
        },
        "GET:/service-catalog/v1beta1/service-provisions": {
            "path": "/service-catalog/v1beta1/service-provisions",
            "method": "GET",
            "summary": "getserviceprovisions",
            "description": "getserviceprovisions",
            "parameters": [
                {
                    "name": "Hpe-workspace-id",
                    "type": "str",
                    "description": "Hpe-workspace-id",
                    "required": False,
                    "location": "header",
                    "default": "Id",
                },
                {"name": "next", "type": "str", "description": "next", "required": False, "location": "query"},
                {
                    "name": "limit",
                    "type": "int",
                    "description": "limit",
                    "required": False,
                    "location": "query",
                    "default": "2000",
                },
                {"name": "filter", "type": "str", "description": "filter", "required": False, "location": "query"},
                {
                    "name": "unredacted",
                    "type": "bool",
                    "description": "unredacted",
                    "required": False,
                    "location": "query",
                },
                {"name": "all", "type": "bool", "description": "all", "required": False, "location": "query"},
            ],
        },
        "GET:/service-catalog/v1beta1/service-offers": {
            "path": "/service-catalog/v1beta1/service-offers",
            "method": "GET",
            "summary": "getserviceoffers",
            "description": "getserviceoffers",
            "parameters": [
                {"name": "next", "type": "str", "description": "next", "required": False, "location": "query"},
                {
                    "name": "limit",
                    "type": "int",
                    "description": "limit",
                    "required": False,
                    "location": "query",
                    "default": "2000",
                },
                {"name": "filter", "type": "str", "description": "filter", "required": False, "location": "query"},
            ],
        },
        "GET:/service-catalog/v1beta1/service-offer-regions/{id}": {
            "path": "/service-catalog/v1beta1/service-offer-regions/{id}",
            "method": "GET",
            "summary": "getserviceofferregion",
            "description": "getserviceofferregion",
            "parameters": [
                {"name": "id", "type": "str", "description": "id", "required": True, "location": "path"},
            ],
        },
        "GET:/service-catalog/v1/per-region-service-managers/{id}": {
            "path": "/service-catalog/v1/per-region-service-managers/{id}",
            "method": "GET",
            "summary": "service_managers_for_a_region_v1",
            "description": "service_managers_for_a_region_v1",
            "parameters": [
                {"name": "id", "type": "str", "description": "id", "required": True, "location": "path"},
            ],
        },
        "GET:/service-catalog/v1/service-manager-provisions": {
            "path": "/service-catalog/v1/service-manager-provisions",
            "method": "GET",
            "summary": "get_service_manager_provisions_v1",
            "description": "get_service_manager_provisions_v1",
            "parameters": [
                {"name": "offset", "type": "int", "description": "offset", "required": False, "location": "query"},
                {
                    "name": "limit",
                    "type": "int",
                    "description": "limit",
                    "required": False,
                    "location": "query",
                    "default": "2000",
                },
                {"name": "filter", "type": "str", "description": "filter", "required": False, "location": "query"},
            ],
        },
        "GET:/service-catalog/v1/service-managers": {
            "path": "/service-catalog/v1/service-managers",
            "method": "GET",
            "summary": "get_service_managers_v1",
            "description": "get_service_managers_v1",
            "parameters": [
                {"name": "offset", "type": "int", "description": "offset", "required": False, "location": "query"},
                {
                    "name": "limit",
                    "type": "int",
                    "description": "limit",
                    "required": False,
                    "location": "query",
                    "default": "2000",
                },
            ],
        },
        "GET:/service-catalog/v1/service-manager-provisions/{id}": {
            "path": "/service-catalog/v1/service-manager-provisions/{id}",
            "method": "GET",
            "summary": "get_service_manager_provision_v1",
            "description": "get_service_manager_provision_v1",
            "parameters": [
                {"name": "id", "type": "str", "description": "id", "required": True, "location": "path"},
            ],
        },
        "GET:/service-catalog/v1/per-region-service-managers": {
            "path": "/service-catalog/v1/per-region-service-managers",
            "method": "GET",
            "summary": "per_region_service_managers_v1",
            "description": "per_region_service_managers_v1",
            "parameters": [
                {"name": "offset", "type": "int", "description": "offset", "required": False, "location": "query"},
                {
                    "name": "limit",
                    "type": "int",
                    "description": "limit",
                    "required": False,
                    "location": "query",
                    "default": "2000",
                },
                {"name": "filter", "type": "str", "description": "filter", "required": False, "location": "query"},
            ],
        },
        "GET:/service-catalog/v1beta1/service-provisions/{id}": {
            "path": "/service-catalog/v1beta1/service-provisions/{id}",
            "method": "GET",
            "summary": "getserviceprovision",
            "description": "getserviceprovision",
            "parameters": [
                {"name": "id", "type": "str", "description": "id", "required": True, "location": "path"},
                {
                    "name": "unredacted",
                    "type": "bool",
                    "description": "unredacted",
                    "required": False,
                    "location": "query",
                },
            ],
        },
        "GET:/service-catalog/v1beta1/service-offers/{id}": {
            "path": "/service-catalog/v1beta1/service-offers/{id}",
            "method": "GET",
            "summary": "getserviceoffer",
            "description": "getserviceoffer",
            "parameters": [
                {"name": "id", "type": "str", "description": "id", "required": True, "location": "path"},
            ],
        },
        "GET:/service-catalog/v1/service-managers/{id}": {
            "path": "/service-catalog/v1/service-managers/{id}",
            "method": "GET",
            "summary": "get_service_manager_v1",
            "description": "get_service_manager_v1",
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

    schema = endpoint_schemas[endpoint_identifier]

    if validate_schema:
        validation_errors = _validate_parameters(params, schema)
        if validation_errors:
            return [
                {
                    "success": False,
                    "error": "Parameter validation failed",
                    "validation_errors": validation_errors,
                    "schema": schema,
                }
            ]

    final_url, query_params = _build_request_url(path, params, schema)

    if method != "GET":
        return [
            {
                "success": False,
                "error": f"Unsupported HTTP method: {method}",
                "message": "This MCP server only supports read operations (GET methods)",
            }
        ]

    try:
        response_data = await http_client.get(final_url, params=query_params)
        return [
            {
                "success": True,
                "endpoint_identifier": endpoint_identifier,
                "request": {"url": final_url, "method": method, "query_params": query_params},
                "response": response_data,
            }
        ]
    except ValueError as exc:
        logger.error(f"Validation error in invoke_dynamic_tool: {exc}")
        return [{"success": False, "error": "validation_error", "message": str(exc)}]
    except Exception as exc:
        logger.error(f"Error in invoke_dynamic_tool: {exc}", exc_info=True)
        return [{"success": False, "error": "request_failed", "message": str(exc)}]


def _validate_parameters(parameters: dict[str, Any], schema: dict[str, Any]) -> list[str]:
    """Validate parameters against endpoint schema."""
    errors: list[str] = []
    schema_params = {p["name"]: p for p in schema.get("parameters", [])}

    # Check required parameters
    for param_name, param_def in schema_params.items():
        if param_def["required"] and param_name not in parameters:
            errors.append(f"Required parameter '{param_name}' is missing")

    # Basic type validation
    for param_name, param_value in parameters.items():
        if param_name not in schema_params:
            errors.append(f"Unknown parameter '{param_name}' not defined in schema")
            continue

        expected_type = schema_params[param_name]["type"]

        if expected_type == "integer" and not isinstance(param_value, int):
            try:
                int(param_value)
            except (ValueError, TypeError):
                errors.append(f"Parameter '{param_name}' should be an integer")
        elif expected_type == "boolean" and not isinstance(param_value, bool):
            if str(param_value).lower() not in ("true", "false", "1", "0"):
                errors.append(f"Parameter '{param_name}' should be a boolean")

    return errors


def _build_request_url(
    base_path: str, parameters: dict[str, Any], schema: dict[str, Any]
) -> tuple[str, dict[str, Any]]:
    """Build the final request URL and separate query parameters."""
    url = base_path
    query_params: dict[str, Any] = {}
    schema_params = {p["name"]: p for p in schema.get("parameters", [])}

    for param_name, param_value in parameters.items():
        if param_name not in schema_params:
            continue

        param_def = schema_params[param_name]
        location = param_def.get("location", "query")
        param_type = param_def.get("type", "string")

        if location == "path":
            # URL-encode path parameters to prevent path-traversal attacks
            url = url.replace("{" + param_name + "}", quote(str(param_value), safe=""))
        else:
            # Coerce integer parameters that may arrive as strings from LLM clients
            if param_type == "integer":
                try:
                    param_value = int(param_value)
                except (ValueError, TypeError):
                    pass
            query_params[param_name] = param_value

    return url, query_params
