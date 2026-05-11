# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
get_endpoint_schema tool implementation for users MCP server.

This tool retrieves detailed schema information for a specific API endpoint using endpoint identifier.
Generated for dynamic mode when OpenAPI spec has 2 endpoints (>= 50 threshold).
"""

from __future__ import annotations

from typing import Annotated, Any

from pydantic import Field

from greenlake_users_mcp.config.logging import get_logger
from greenlake_users_mcp.server.fastmcp_instance import mcp

logger = get_logger(__name__)


@mcp.tool(
    name="get_endpoint_schema",
    description="Retrieves detailed schema information for a specific users API endpoint including parameters, request/response models, and validation rules",
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
    """Retrieves detailed schema information for a specific users API endpoint.

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
                    "description": "Filter data using a subset of OData 4.0 and return only the subset of resources that match the filter.\n\nSupported classes and examples include:\n- **Types**: timestamp, string\n- **Comparison**: eq, ne, gt, ge, lt\n- **Logical Expressions**: and, or, not\n\nThe Get users API can be filtered by:\n- id\n- username\n- userStatus\n- createdAt\n- updatedAt\n- lastLogin\n\nuserStatus can be one of the following:\n- UNVERIFIED\n- VERIFIED\n- BLOCKED\n- DELETE_IN_PROGRESS\n- DELETED\n- SUSPENDED\n\n**Note**: The userStatus filter is case-sensitive.\n\nExamples:\n  - updatedAt gt '2020-09-21T14:19:09.769747'\n    Returns users updated after 2020-09-21T14:19:09.769747\n  - userStatus ne 'UNVERIFIED'\n    Returns users that are not unverified.\n  - username eq 'user@example.com'\n    Returns the user with a specific username.\n  - createdAt gt '2020-09-21T14:19:09.769747'\n    Returns users created after 2020-09-21T14:19:09.769747\n  - username eq 'user@example.com'\n    Returns the user with a specific email.\n  - id eq '7600415a-8876-5722-9f3c-b0fd11112283'\n    Returns the user with a specific ID.\n  - lastLogin lt '2020-09-21T14:19:09.769747'\n    Returns users that logged in before 2020-09-21T14:19:09.769747\n\n**Filter Syntax**: Use OData-style filters with the field names shown in the examples above. String values must be enclosed in single quotes.",
                    "required": False,
                    "location": "query",
                    "schema": {
                        "type": "string",
                        "description": "Filter data using a subset of OData 4.0 and return only the subset of resources that match the filter.\n\nSupported classes and examples include:\n- **Types**: timestamp, string\n- **Comparison**: eq, ne, gt, ge, lt\n- **Logical Expressions**: and, or, not\n\nThe Get users API can be filtered by:\n- id\n- username\n- userStatus\n- createdAt\n- updatedAt\n- lastLogin\n\nuserStatus can be one of the following:\n- UNVERIFIED\n- VERIFIED\n- BLOCKED\n- DELETE_IN_PROGRESS\n- DELETED\n- SUSPENDED\n\n**Note**: The userStatus filter is case-sensitive.\n\nExamples:\n  - updatedAt gt '2020-09-21T14:19:09.769747'\n    Returns users updated after 2020-09-21T14:19:09.769747\n  - userStatus ne 'UNVERIFIED'\n    Returns users that are not unverified.\n  - username eq 'user@example.com'\n    Returns the user with a specific username.\n  - createdAt gt '2020-09-21T14:19:09.769747'\n    Returns users created after 2020-09-21T14:19:09.769747\n  - username eq 'user@example.com'\n    Returns the user with a specific email.\n  - id eq '7600415a-8876-5722-9f3c-b0fd11112283'\n    Returns the user with a specific ID.\n  - lastLogin lt '2020-09-21T14:19:09.769747'\n    Returns users that logged in before 2020-09-21T14:19:09.769747\n\n**Filter Syntax**: Use OData-style filters with the field names shown in the examples above. String values must be enclosed in single quotes.",
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
