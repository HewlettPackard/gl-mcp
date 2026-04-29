# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
get_endpoint_schema tool implementation for devices MCP server.

This tool retrieves detailed schema information for a specific API endpoint using endpoint identifier.
Generated for dynamic mode when OpenAPI spec has 2 endpoints (>= 50 threshold).
"""

from __future__ import annotations

from typing import Annotated, Any

from pydantic import Field

from greenlake_devices_mcp.config.logging import get_logger
from greenlake_devices_mcp.server.fastmcp_instance import mcp

logger = get_logger(__name__)


@mcp.tool(
    name="get_endpoint_schema",
    description="Retrieves detailed schema information for a specific devices API endpoint including parameters, request/response models, and validation rules",
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
    """Retrieves detailed schema information for a specific devices API endpoint.

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
        "GET:/devices/v1/devices": {
            "path": "/devices/v1/devices",
            "method": "GET",
            "summary": "getdevicesv1",
            "description": "getdevicesv1",
            "operationId": "getdevicesv1",
            "tags": [],
            "deprecated": False,
            "parameters": [
                {
                    "name": "filter",
                    "type": "str",
                    "description": "Filter expressions consisting of simple comparison operations joined\nby logical operators.<br>\n| CLASS               |   EXAMPLES                                         |\n|---------------------|----------------------------------------------------|\n| Types               | integer, decimal, timestamp, string, boolean, null |\n| Comparison          | eq, ne, gt, ge, lt, le, in                         |\n| Logical Expressions | and, or, not                                       |\n\nThe following examples are not an exhaustive list of all possible filtering options.\n\n\nExamples:\n  - updatedAt le '2024-02-18T19:53:51.480Z'\n    Return devices where a property is lesser or equal to a value.\nExample syntax, \\<property> ge \\<value>.\n  - not serialNumber eq 'STIAPL6404'\n    Return devices where a property does not equal a value.\nExample syntax, not \\<property> eq \\<value>.\n  - deviceType in 'COMPUTE', 'STORAGE'\n    Return devices where a property is one of multiple values.\nExample syntax, \\<property> in \\<value>,\\<value>.\n  - deviceType eq 'STORAGE' and partNumber eq 'RTICXL6413'\n    Return devices that exactly satisfy multiple filter queries.\nExample syntax, \\<property> eq \\<value> and \\<property> eq \\<value>.\n  - serialNumber eq 'STIAPL6404' or partNumber eq 'RTICXL6413'\n    Return devices that exactly satisfy one of multiple filter queries.\nExample syntax, \\<property> eq \\<value> or \\<property> eq \\<value>.\n  - serialNumber eq 'STIAPL6404'\n    Return devices where a property equals a value.\nExample syntax, \\<property> eq \\<value>.\n  - createdAt ge ''2024-01-18T19:53:51.480Z''\n    Return devices where a property is greater or equal to a value.\nExample syntax, \\<property> ge \\<value>.\n\n**Filter Syntax**: Use OData-style filters with the field names shown in the examples above. String values must be enclosed in single quotes.",
                    "required": False,
                    "location": "query",
                    "schema": {
                        "type": "string",
                        "description": "Filter expressions consisting of simple comparison operations joined\nby logical operators.<br>\n| CLASS               |   EXAMPLES                                         |\n|---------------------|----------------------------------------------------|\n| Types               | integer, decimal, timestamp, string, boolean, null |\n| Comparison          | eq, ne, gt, ge, lt, le, in                         |\n| Logical Expressions | and, or, not                                       |\n\nThe following examples are not an exhaustive list of all possible filtering options.\n\n\nExamples:\n  - updatedAt le '2024-02-18T19:53:51.480Z'\n    Return devices where a property is lesser or equal to a value.\nExample syntax, \\<property> ge \\<value>.\n  - not serialNumber eq 'STIAPL6404'\n    Return devices where a property does not equal a value.\nExample syntax, not \\<property> eq \\<value>.\n  - deviceType in 'COMPUTE', 'STORAGE'\n    Return devices where a property is one of multiple values.\nExample syntax, \\<property> in \\<value>,\\<value>.\n  - deviceType eq 'STORAGE' and partNumber eq 'RTICXL6413'\n    Return devices that exactly satisfy multiple filter queries.\nExample syntax, \\<property> eq \\<value> and \\<property> eq \\<value>.\n  - serialNumber eq 'STIAPL6404' or partNumber eq 'RTICXL6413'\n    Return devices that exactly satisfy one of multiple filter queries.\nExample syntax, \\<property> eq \\<value> or \\<property> eq \\<value>.\n  - serialNumber eq 'STIAPL6404'\n    Return devices where a property equals a value.\nExample syntax, \\<property> eq \\<value>.\n  - createdAt ge ''2024-01-18T19:53:51.480Z''\n    Return devices where a property is greater or equal to a value.\nExample syntax, \\<property> ge \\<value>.\n\n**Filter Syntax**: Use OData-style filters with the field names shown in the examples above. String values must be enclosed in single quotes.",
                    },
                },
                {
                    "name": "filter-tags",
                    "type": "str",
                    "description": "Filter expressions consisting of simple comparison operations joined\nby logical operators to be applied on the assigned tags or their\nvalues.<br>\n| CLASS               |   EXAMPLES      |\n|---------------------|-----------------|\n| Types               | string          |\n| Comparison          | eq, ne, in      |\n| Logical Expressions | and, or, not    |\n\n\nExamples:\n  - not 'city' eq 'Tokyo'\n    Return devices where a tag key does not equal a tag value.\nExample syntax, not \\<property> eq \\<value>.\n  - 'street' in 'Regent Street', 'Oxford Street', 'Piccadilly'\n    Return devices containing the tag key and at least one of the specified values.\nExample syntax, \\<property> in \\<value>,\\<value>.\n  - 'city' eq 'London' and 'street' eq 'Piccadilly'\n    Return devices that exactly satisfy multiple filter queries applied to tag keys.\nExample syntax, \\<property> eq \\<value> and \\<property> eq \\<value>.\n  - 'street' eq 'Oxford Street' or 'street' eq 'Piccadilly'\n    Return devices that satisfy any of multiple filter queries applied to tag keys.\nExample syntax, \\<property> eq \\<value> or \\<property> eq \\<value>.\n  - 'city' eq 'London'\n    Return devices where a tag key is equal to a tag value.\nExample syntax, \\<tagKey> eq \\<tagValue>.\n\n**Filter Syntax**: Use OData-style filters with the field names shown in the examples above. String values must be enclosed in single quotes.",
                    "required": False,
                    "location": "query",
                    "schema": {
                        "type": "string",
                        "description": "Filter expressions consisting of simple comparison operations joined\nby logical operators to be applied on the assigned tags or their\nvalues.<br>\n| CLASS               |   EXAMPLES      |\n|---------------------|-----------------|\n| Types               | string          |\n| Comparison          | eq, ne, in      |\n| Logical Expressions | and, or, not    |\n\n\nExamples:\n  - not 'city' eq 'Tokyo'\n    Return devices where a tag key does not equal a tag value.\nExample syntax, not \\<property> eq \\<value>.\n  - 'street' in 'Regent Street', 'Oxford Street', 'Piccadilly'\n    Return devices containing the tag key and at least one of the specified values.\nExample syntax, \\<property> in \\<value>,\\<value>.\n  - 'city' eq 'London' and 'street' eq 'Piccadilly'\n    Return devices that exactly satisfy multiple filter queries applied to tag keys.\nExample syntax, \\<property> eq \\<value> and \\<property> eq \\<value>.\n  - 'street' eq 'Oxford Street' or 'street' eq 'Piccadilly'\n    Return devices that satisfy any of multiple filter queries applied to tag keys.\nExample syntax, \\<property> eq \\<value> or \\<property> eq \\<value>.\n  - 'city' eq 'London'\n    Return devices where a tag key is equal to a tag value.\nExample syntax, \\<tagKey> eq \\<tagValue>.\n\n**Filter Syntax**: Use OData-style filters with the field names shown in the examples above. String values must be enclosed in single quotes.",
                    },
                },
                {
                    "name": "sort",
                    "type": "str",
                    "description": "A comma separated list of sort expressions. A sort expression is a property name optionally followed by a direction indicator `asc` or `desc`. The default is ascending order.\n\nExample: serialNumber,macAddress desc",
                    "required": False,
                    "location": "query",
                    "schema": {
                        "type": "string",
                        "description": "A comma separated list of sort expressions. A sort expression is a property name optionally followed by a direction indicator `asc` or `desc`. The default is ascending order.\n\nExample: serialNumber,macAddress desc",
                    },
                },
                {
                    "name": "select",
                    "type": "list[str]",
                    "description": "A comma separated list of select properties to display in the response. The default is that all properties are returned.\n\nExample: serialNumber,macAddress",
                    "required": False,
                    "location": "query",
                    "schema": {
                        "type": "array",
                        "description": "A comma separated list of select properties to display in the response. The default is that all properties are returned.\n\nExample: serialNumber,macAddress",
                    },
                },
                {
                    "name": "limit",
                    "type": "int",
                    "description": "Specifies the number of results to be returned. The default value is 2000.",
                    "required": False,
                    "location": "query",
                    "default": 2000,
                    "schema": {
                        "type": "integer",
                        "description": "Specifies the number of results to be returned. The default value is 2000.",
                        "default": "2000",
                    },
                },
                {
                    "name": "offset",
                    "type": "int",
                    "description": "Specifies the zero-based resource offset to start the response from. The default value is 0.",
                    "required": False,
                    "location": "query",
                    "schema": {
                        "type": "integer",
                        "description": "Specifies the zero-based resource offset to start the response from. The default value is 0.",
                    },
                },
            ],
            "security": [],
            "responses": {"200": {"description": "Successful response", "content_type": "application/json"}},
        },
        "GET:/devices/v1/devices/{id}": {
            "path": "/devices/v1/devices/{id}",
            "method": "GET",
            "summary": "getdevicebyidv1",
            "description": "getdevicebyidv1",
            "operationId": "getdevicebyidv1",
            "tags": [],
            "deprecated": False,
            "parameters": [
                {
                    "name": "id",
                    "type": "str",
                    "description": "id",
                    "required": True,
                    "location": "query",
                    "schema": {"type": "string", "description": "id"},
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
