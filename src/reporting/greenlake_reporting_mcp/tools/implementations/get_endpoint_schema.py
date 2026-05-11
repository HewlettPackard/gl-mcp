# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
get_endpoint_schema tool implementation for reporting MCP server.

This tool retrieves detailed schema information for a specific API endpoint using endpoint identifier.
Generated for dynamic mode when OpenAPI spec has 2 endpoints (>= 50 threshold).
"""

from __future__ import annotations

from typing import Annotated, Any

from pydantic import Field

from greenlake_reporting_mcp.config.logging import get_logger
from greenlake_reporting_mcp.server.fastmcp_instance import mcp

logger = get_logger(__name__)


@mcp.tool(
    name="get_endpoint_schema",
    description="Retrieves detailed schema information for a specific reporting API endpoint including parameters, request/response models, and validation rules",
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
    """Retrieves detailed schema information for a specific reporting API endpoint.

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
        "GET:/reporting/v1/statuses/{id}": {
            "path": "/reporting/v1/statuses/{id}",
            "method": "GET",
            "summary": "getreportingstatusbyid",
            "description": "getreportingstatusbyid",
            "operationId": "getreportingstatusbyid",
            "tags": [],
            "deprecated": False,
            "parameters": [
                {
                    "name": "id",
                    "type": "str",
                    "description": "The report status identifier.\n\nExample: 3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "required": True,
                    "location": "query",
                    "schema": {
                        "type": "string",
                        "description": "The report status identifier.\n\nExample: 3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    },
                },
            ],
            "security": [],
            "responses": {"200": {"description": "Successful response", "content_type": "application/json"}},
        },
        "GET:/reporting/v1/statuses": {
            "path": "/reporting/v1/statuses",
            "method": "GET",
            "summary": "getreportingstatuses",
            "description": "getreportingstatuses",
            "operationId": "getreportingstatuses",
            "tags": [],
            "deprecated": False,
            "parameters": [
                {
                    "name": "filter",
                    "type": "str",
                    "description": 'Example: type eq "REPORT"\n\n**Filter Syntax**: Use OData-style filters with the field names shown in the examples above. String values must be enclosed in double quotes.',
                    "required": True,
                    "location": "query",
                    "schema": {
                        "type": "string",
                        "description": 'Example: type eq "REPORT"\n\n**Filter Syntax**: Use OData-style filters with the field names shown in the examples above. String values must be enclosed in double quotes.',
                    },
                },
                {
                    "name": "sort",
                    "type": "str",
                    "description": "The order in which to return the resources in the collection.The value of the sort query parameter is a comma separated list of sort expressions. Each sort expression is a property name optionally followed by a direction indicator asc (ascending) or desc (descending).The first sort expression in the list defines the primary sort order, the second defines the secondary sort order, and so on. If a direction indicator is omitted the default direction is ascending.\n\nExamples:\n  - name,createdAt desc\n    Order resources ascending by name and then by descending by createdAt\n  - name asc\n    Order ascending by name",
                    "required": False,
                    "location": "query",
                    "schema": {
                        "type": "string",
                        "description": "The order in which to return the resources in the collection.The value of the sort query parameter is a comma separated list of sort expressions. Each sort expression is a property name optionally followed by a direction indicator asc (ascending) or desc (descending).The first sort expression in the list defines the primary sort order, the second defines the secondary sort order, and so on. If a direction indicator is omitted the default direction is ascending.\n\nExamples:\n  - name,createdAt desc\n    Order resources ascending by name and then by descending by createdAt\n  - name asc\n    Order ascending by name",
                    },
                },
                {
                    "name": "limit",
                    "type": "int",
                    "description": "The maximum number of reports to return.\n\nExample: 50",
                    "required": False,
                    "location": "query",
                    "default": 10,
                    "schema": {
                        "type": "integer",
                        "description": "The maximum number of reports to return.\n\nExample: 50",
                        "default": "10",
                    },
                },
                {
                    "name": "offset",
                    "type": "int",
                    "description": "Zero-based resource offset to start the response from.\n\nExample: 20",
                    "required": False,
                    "location": "query",
                    "schema": {
                        "type": "integer",
                        "description": "Zero-based resource offset to start the response from.\n\nExample: 20",
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
