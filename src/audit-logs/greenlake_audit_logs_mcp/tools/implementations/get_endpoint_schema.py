# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
get_endpoint_schema tool implementation for audit-logs MCP server.

This tool retrieves detailed schema information for a specific API endpoint using endpoint identifier.
Generated for dynamic mode when OpenAPI spec has 2 endpoints (>= 50 threshold).
"""

from __future__ import annotations

from typing import Annotated, Any

from pydantic import Field

from greenlake_audit_logs_mcp.config.logging import get_logger
from greenlake_audit_logs_mcp.server.fastmcp_instance import mcp

logger = get_logger(__name__)


@mcp.tool(
    name="get_endpoint_schema",
    description="Retrieves detailed schema information for a specific audit-logs API endpoint including parameters, request/response models, and validation rules",
)
async def get_endpoint_schema(
    endpoint_identifier: Annotated[
        str,
        Field(
            description="The API endpoint identifier in METHOD:PATH format (e.g., 'GET:/api/v1/users/{id}')",
        ),
    ],
    include_examples: Annotated[
        bool,
        Field(
            description="Include example parameter values and request/response examples",
            default=False,
        ),
    ] = False,
) -> list[dict[str, Any]]:
    """Retrieves detailed schema information for a specific audit-logs API endpoint.

    Args:
        endpoint_identifier: Endpoint identifier in METHOD:PATH format.
        include_examples: Whether to include example parameter values.

    Returns:
        A list containing one result dict with the endpoint schema or an error message.
    """
    endpoint_identifier = endpoint_identifier.strip()

    if not endpoint_identifier:
        return [
            {
                "success": False,
                "error": "endpoint_identifier is required",
                "message": "Please provide an endpoint identifier in METHOD:PATH format",
            }
        ]

    # Create endpoint schema map for fast lookup
    endpoint_schemas: dict[str, dict[str, Any]] = {
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
                    "description": "Example: category eq 'User Management' and contains(description, 'logged out')\n\n**Filter Syntax**: Use OData-style filters with the field names shown in the examples above. String values must be enclosed in single quotes.",
                    "required": False,
                    "location": "query",
                    "schema": {
                        "type": "string",
                        "description": "Example: category eq 'User Management' and contains(description, 'logged out')\n\n**Filter Syntax**: Use OData-style filters with the field names shown in the examples above. String values must be enclosed in single quotes.",
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

    if include_examples:
        for param in schema["parameters"]:  # type: ignore[attr-defined]
            if "example" not in param:
                param["example"] = _generate_example_value(param["type"])

    return [{"success": True, "endpoint_identifier": endpoint_identifier, "schema": schema}]


def _generate_example_value(param_type: str) -> Any:
    """Generate example values for parameters based on type."""
    examples: dict[str, Any] = {
        "string": "example-value",
        "integer": 123,
        "number": 123.45,
        "boolean": True,
        "array": ["example1", "example2"],
        "object": {"key": "value"},
    }
    return examples.get(param_type, "example-value")
