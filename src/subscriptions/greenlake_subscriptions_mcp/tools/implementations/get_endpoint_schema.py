# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
get_endpoint_schema tool implementation for subscriptions MCP server.

This tool retrieves detailed schema information for a specific API endpoint using endpoint identifier.
Generated for dynamic mode when OpenAPI spec has 2 endpoints (>= 50 threshold).
"""

from __future__ import annotations

from typing import Annotated, Any

from pydantic import Field

from greenlake_subscriptions_mcp.config.logging import get_logger
from greenlake_subscriptions_mcp.server.fastmcp_instance import mcp

logger = get_logger(__name__)


@mcp.tool(
    name="get_endpoint_schema",
    description="Retrieves detailed schema information for a specific subscriptions API endpoint including parameters, request/response models, and validation rules",
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
    """Retrieves detailed schema information for a specific subscriptions API endpoint.

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
        "GET:/subscriptions/v1/subscriptions": {
            "path": "/subscriptions/v1/subscriptions",
            "method": "GET",
            "summary": "getsubscriptionsv1",
            "description": "getsubscriptionsv1",
            "operationId": "getsubscriptionsv1",
            "tags": [],
            "deprecated": False,
            "parameters": [
                {
                    "name": "filter",
                    "type": "str",
                    "description": "Filter expressions consisting of simple comparison operations joined \nby logical operators.<br>\n| CLASS                |   EXAMPLES                                         |\n|----------------------|----------------------------------------------------|\n| Types                | integer, decimal, timestamp, string, boolean, null |\n| Comparison           | eq, ne, gt, ge, lt, le, in                         |\n| Logical Expressions  | and, or, not                                       |\n\nSubscriptions can be filtered based on the following properties:\n- `id`\n- `subscriptionType`\n- `subscriptionStatus`\n- `key`\n- `quantity`\n- `availableQuantity`\n- `sku`\n- `skuDescription`\n- `contract`\n- `startTime`\n- `endTime`\n- `productType`\n- `tier`\n- `tierDescription`\n- `quote`\n- `po`\n- `resellerPo`\n- `createdAt`\n- `updatedAt`\n\nThe following is a non-exhaustive list of possible filtering options.\n\n\nExamples:\n  - subscriptionType in 'CENTRAL_STORAGE', 'CENTRAL_CONTROLLER'\n    Return subscriptions where the property is one of multiple values. Example syntax, \n\\<property> in \\<value>,\\<value>.\n  - not key eq 'STIAPL6404'\n    Return subscriptions where a property does not equal a value. Example syntax, \nnot \\<property> eq \\<value>.\n  - key eq 'STIQQ4L04' and subscriptionType eq 'CENTRAL_STORAGE'\n    The AND operator returns results that meet all filter queries. In the example, the query only returns subscriptions with the exact key and with the specified subscription type. Example syntax,\n\\<property> eq \\<value> and \\<property> eq \\<value>.\n  - key eq 'STIAPL6404'\n    Return subscriptions where a property equals a value. Example syntax, \n\\<property> eq \\<value>.\n  - createdAt ge '2024-01-18T19:53:51.480Z'\n    Return subscriptions where a property is greater or equal to a value. Example syntax,\n\\<property> ge \\<value>.\n  - updatedAt le '2024-02-18T19:53:51.480Z'\n    Return subscriptions where a property is less than or equal to a value. Example syntax,\n\\<property> le \\<value>.\n  - key eq 'STIQQ4L04' or subscriptionType eq 'CENTRAL_STORAGE'\n    The OR operator returns results that meet any of the filter queries. In the example, the query returns subscriptions with the exact key or with the specified subscription type.\n  - startTime gt '2024-01-23T00:00:00.000Z' and endTime lt '2025-02-22T00:00:00.000Z' and not productType eq 'SERVICE'\n    The AND, OR, and NOT operators can be combined to return results that satisfy all specified filter criteria.\n  - tier ne 'BRIDGE'\n    Return subscriptions where a property does not equate to a value. Example syntax, \n\\<property> ne \\<value>.\n\n**Filter Syntax**: Use OData-style filters with the field names shown in the examples above. String values must be enclosed in single quotes.",
                    "required": False,
                    "location": "query",
                    "schema": {
                        "type": "string",
                        "description": "Filter expressions consisting of simple comparison operations joined \nby logical operators.<br>\n| CLASS                |   EXAMPLES                                         |\n|----------------------|----------------------------------------------------|\n| Types                | integer, decimal, timestamp, string, boolean, null |\n| Comparison           | eq, ne, gt, ge, lt, le, in                         |\n| Logical Expressions  | and, or, not                                       |\n\nSubscriptions can be filtered based on the following properties:\n- `id`\n- `subscriptionType`\n- `subscriptionStatus`\n- `key`\n- `quantity`\n- `availableQuantity`\n- `sku`\n- `skuDescription`\n- `contract`\n- `startTime`\n- `endTime`\n- `productType`\n- `tier`\n- `tierDescription`\n- `quote`\n- `po`\n- `resellerPo`\n- `createdAt`\n- `updatedAt`\n\nThe following is a non-exhaustive list of possible filtering options.\n\n\nExamples:\n  - subscriptionType in 'CENTRAL_STORAGE', 'CENTRAL_CONTROLLER'\n    Return subscriptions where the property is one of multiple values. Example syntax, \n\\<property> in \\<value>,\\<value>.\n  - not key eq 'STIAPL6404'\n    Return subscriptions where a property does not equal a value. Example syntax, \nnot \\<property> eq \\<value>.\n  - key eq 'STIQQ4L04' and subscriptionType eq 'CENTRAL_STORAGE'\n    The AND operator returns results that meet all filter queries. In the example, the query only returns subscriptions with the exact key and with the specified subscription type. Example syntax,\n\\<property> eq \\<value> and \\<property> eq \\<value>.\n  - key eq 'STIAPL6404'\n    Return subscriptions where a property equals a value. Example syntax, \n\\<property> eq \\<value>.\n  - createdAt ge '2024-01-18T19:53:51.480Z'\n    Return subscriptions where a property is greater or equal to a value. Example syntax,\n\\<property> ge \\<value>.\n  - updatedAt le '2024-02-18T19:53:51.480Z'\n    Return subscriptions where a property is less than or equal to a value. Example syntax,\n\\<property> le \\<value>.\n  - key eq 'STIQQ4L04' or subscriptionType eq 'CENTRAL_STORAGE'\n    The OR operator returns results that meet any of the filter queries. In the example, the query returns subscriptions with the exact key or with the specified subscription type.\n  - startTime gt '2024-01-23T00:00:00.000Z' and endTime lt '2025-02-22T00:00:00.000Z' and not productType eq 'SERVICE'\n    The AND, OR, and NOT operators can be combined to return results that satisfy all specified filter criteria.\n  - tier ne 'BRIDGE'\n    Return subscriptions where a property does not equate to a value. Example syntax, \n\\<property> ne \\<value>.\n\n**Filter Syntax**: Use OData-style filters with the field names shown in the examples above. String values must be enclosed in single quotes.",
                    },
                },
                {
                    "name": "filter-tags",
                    "type": "str",
                    "description": "Filter expressions consisting of simple comparison operations joined\nby logical operators to be applied on the assigned tags or their\nvalues.<br>\n| CLASS               |   EXAMPLES      |\n|---------------------|-----------------|\n| Types               | string          |\n| Comparison          | eq, ne          |\n| Logical Expressions | and, or         |\n\n\nExamples:\n  - 'street' eq 'Oxford Street' or 'street' eq 'Piccadilly'\n    Return subscriptions containing the tag key and the corresponding value that satisfy at least one of the conditionals. Example syntax, \n\\<property> eq \\<value> or \\<property> eq \\<value>.\n  - 'city' eq 'London'\n    Return subscriptions that have a pair of tags with the exact same tag key and tag value. Example syntax, \n\\<tagKey> eq \\<tagValue>.\n  - 'city' ne 'London'\n    Return subscriptions that have a pair of tags with the exact same tag key and the exact different tag value. Example syntax, \n\\<tagKey> ne \\<tagValue>.\n  - 'city' eq 'London' and 'street' eq 'Piccadilly'\n    Return subscriptions containing the tag key and the corresponding value that satisfy all conditionals. Example syntax, \n\\<property> eq \\<value> and \\<property> eq \\<value>.\n\n**Filter Syntax**: Use OData-style filters with the field names shown in the examples above. String values must be enclosed in single quotes.",
                    "required": False,
                    "location": "query",
                    "schema": {
                        "type": "string",
                        "description": "Filter expressions consisting of simple comparison operations joined\nby logical operators to be applied on the assigned tags or their\nvalues.<br>\n| CLASS               |   EXAMPLES      |\n|---------------------|-----------------|\n| Types               | string          |\n| Comparison          | eq, ne          |\n| Logical Expressions | and, or         |\n\n\nExamples:\n  - 'street' eq 'Oxford Street' or 'street' eq 'Piccadilly'\n    Return subscriptions containing the tag key and the corresponding value that satisfy at least one of the conditionals. Example syntax, \n\\<property> eq \\<value> or \\<property> eq \\<value>.\n  - 'city' eq 'London'\n    Return subscriptions that have a pair of tags with the exact same tag key and tag value. Example syntax, \n\\<tagKey> eq \\<tagValue>.\n  - 'city' ne 'London'\n    Return subscriptions that have a pair of tags with the exact same tag key and the exact different tag value. Example syntax, \n\\<tagKey> ne \\<tagValue>.\n  - 'city' eq 'London' and 'street' eq 'Piccadilly'\n    Return subscriptions containing the tag key and the corresponding value that satisfy all conditionals. Example syntax, \n\\<property> eq \\<value> and \\<property> eq \\<value>.\n\n**Filter Syntax**: Use OData-style filters with the field names shown in the examples above. String values must be enclosed in single quotes.",
                    },
                },
                {
                    "name": "sort",
                    "type": "str",
                    "description": "A comma separated list of sort expressions. A sort expression is a  property name optionally followed by a direction indicator `asc` or  `desc`. The default is ascending order.\n\nExample: key, quote desc",
                    "required": False,
                    "location": "query",
                    "schema": {
                        "type": "string",
                        "description": "A comma separated list of sort expressions. A sort expression is a  property name optionally followed by a direction indicator `asc` or  `desc`. The default is ascending order.\n\nExample: key, quote desc",
                    },
                },
                {
                    "name": "select",
                    "type": "list[str]",
                    "description": "A comma separated list of select properties to display in the response.  The default is that all properties are returned.\n\nExample: id,key",
                    "required": False,
                    "location": "query",
                    "schema": {
                        "type": "array",
                        "description": "A comma separated list of select properties to display in the response.  The default is that all properties are returned.\n\nExample: id,key",
                    },
                },
                {
                    "name": "limit",
                    "type": "int",
                    "description": "Specifies the number of results to be returned. The default value  is 50.",
                    "required": False,
                    "location": "query",
                    "default": 50,
                    "schema": {
                        "type": "integer",
                        "description": "Specifies the number of results to be returned. The default value  is 50.",
                        "default": "50",
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
        "GET:/subscriptions/v1/subscriptions/{id}": {
            "path": "/subscriptions/v1/subscriptions/{id}",
            "method": "GET",
            "summary": "getsubscriptiondetailsbyidv1",
            "description": "getsubscriptiondetailsbyidv1",
            "operationId": "getsubscriptiondetailsbyidv1",
            "tags": [],
            "deprecated": False,
            "parameters": [
                {
                    "name": "id",
                    "type": "str",
                    "description": "The unique identifier of the subscription.",
                    "required": True,
                    "location": "query",
                    "schema": {"type": "string", "description": "The unique identifier of the subscription."},
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
