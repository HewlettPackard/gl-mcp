# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
invoke_dynamic_tool tool implementation for audit-logs MCP server.

This tool can execute any API endpoint dynamically using endpoint identifier and schema validation.
Generated for dynamic mode when OpenAPI spec has 2 endpoints (>= 50 threshold).
"""

from __future__ import annotations

import re
from typing import Annotated, Any
from urllib.parse import quote

from mcp.server.fastmcp import Context
from pydantic import Field

from greenlake_audit_logs_mcp.config.logging import get_logger
from greenlake_audit_logs_mcp.server.fastmcp_instance import mcp

logger = get_logger(__name__)


def _normalize_filter_quotes(filter_expr: str) -> str:
    """Wrap unquoted numeric values in single quotes for OData filter expressions.

    LLMs sometimes omit quotes around numeric filter values (e.g., ``quantity eq 5``
    instead of ``quantity eq '5'``), which causes 400 Bad Request from the API.
    This function normalises those bare numeric values while leaving booleans,
    already-quoted strings, and other tokens untouched.
    """
    return re.sub(
        r"\b(eq|ne|gt|ge|lt|le)\s+(-?\d+(?:\.\d+)?)\b",
        r"\1 '\2'",
        filter_expr,
    )


@mcp.tool(
    name="invoke_dynamic_tool",
    description="Executes any audit-logs API endpoint dynamically with parameter validation and schema support",
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
    """Executes any audit-logs API endpoint dynamically with parameter validation.

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
        "GET:/audit-log/v1/logs": {
            "path": "/audit-log/v1/logs",
            "method": "GET",
            "summary": "getauditlogs",
            "description": "getauditlogs",
            "parameters": [
                {"name": "filter", "type": "str", "description": "filter", "required": False, "location": "query"},
                {"name": "select", "type": "str", "description": "select", "required": False, "location": "query"},
                {"name": "all", "type": "str", "description": "all", "required": False, "location": "query"},
                {
                    "name": "limit",
                    "type": "int",
                    "description": "limit",
                    "required": False,
                    "location": "query",
                    "default": "50",
                },
                {"name": "offset", "type": "int", "description": "offset", "required": False, "location": "query"},
            ],
        },
        "GET:/audit-log/v1/logs/{id}/detail": {
            "path": "/audit-log/v1/logs/{id}/detail",
            "method": "GET",
            "summary": "getauditlogdetails",
            "description": "getauditlogdetails",
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
            # Normalize unquoted numeric values in OData filter expressions
            if param_name in ("filter", "filter-tags") and isinstance(param_value, str):
                param_value = _normalize_filter_quotes(param_value)
            query_params[param_name] = param_value

    return url, query_params
