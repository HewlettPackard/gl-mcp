# (c) Copyright 2025 Hewlett Packard Enterprise Development LP
"""
get_endpoint_schema tool implementation for devices MCP server.

This tool retrieves detailed schema information for a specific API endpoint using endpoint identifier.
Generated for dynamic mode when OpenAPI spec has 0 endpoints (>= 50 threshold).
"""

from typing import Any, Dict, List
from tools.base import BaseTool


class GetEndpointSchemaTool(BaseTool):
    """Retrieves detailed schema information for a specific devices API endpoint including parameters, request/response models, and validation rules"""

    @property
    def name(self) -> str:
        """Tool name."""
        return "get_endpoint_schema"

    @property
    def description(self) -> str:
        """Tool description."""
        return "Retrieves detailed schema information for a specific devices API endpoint including parameters, request/response models, and validation rules"

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
                        "GET:/devices/v1/devices",
                        "GET:/devices/v1/devices/{id}",
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
                            "description": "Filter expressions consisting of simple comparison operations joined\nby logical operators.<br>\n| CLASS               |   EXAMPLES                                         |\n|---------------------|----------------------------------------------------|\n| Types               | integer, decimal, timestamp, string, boolean, null |\n| Comparison          | eq, ne, gt, ge, lt, le, in                         |\n| Logical Expressions | and, or, not                                       |\n\nThe following examples are not an exhaustive list of all possible filtering options.\n\n\nExamples:\n  - deviceType in 'COMPUTE', 'STORAGE'\n    Return devices where a property is one of multiple values.\nExample syntax, <property> in <value>,<value>.\n  - deviceType eq 'STORAGE' and partNumber eq 'RTICXL6413'\n    Return devices that exactly satisfy multiple filter queries.\nExample syntax, <property> eq <value> and <property> eq <value>.\n  - serialNumber eq 'STIAPL6404' or partNumber eq 'RTICXL6413'\n    Return devices that exactly satisfy one of multiple filter queries.\nExample syntax, <property> eq <value> or <property> eq <value>.\n  - serialNumber eq 'STIAPL6404'\n    Return devices where a property equals a value.\nExample syntax, <property> eq <value>.\n  - createdAt ge ''2024-01-18T19:53:51.480Z''\n    Return devices where a property is greater or equal to a value.\nExample syntax, <property> ge <value>.\n  - updatedAt le '2024-02-18T19:53:51.480Z'\n    Return devices where a property is lesser or equal to a value.\nExample syntax, <property> ge <value>.\n  - not serialNumber eq 'STIAPL6404'\n    Return devices where a property does not equal a value.\nExample syntax, not <property> eq <value>.\n\n**Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`.\n\nFilterable properties: application, archived, assignedState, createdAt, deviceType, id, location, macAddress, model, partNumber, region, serialNumber, subscription, tags, tenantWorkspaceId, type, updatedAt, warranty",
                            "required": False,
                            "location": "query",
                            "schema": {
                                "type": "string",
                                "description": "Filter expressions consisting of simple comparison operations joined\nby logical operators.<br>\n| CLASS               |   EXAMPLES                                         |\n|---------------------|----------------------------------------------------|\n| Types               | integer, decimal, timestamp, string, boolean, null |\n| Comparison          | eq, ne, gt, ge, lt, le, in                         |\n| Logical Expressions | and, or, not                                       |\n\nThe following examples are not an exhaustive list of all possible filtering options.\n\n\nExamples:\n  - deviceType in 'COMPUTE', 'STORAGE'\n    Return devices where a property is one of multiple values.\nExample syntax, <property> in <value>,<value>.\n  - deviceType eq 'STORAGE' and partNumber eq 'RTICXL6413'\n    Return devices that exactly satisfy multiple filter queries.\nExample syntax, <property> eq <value> and <property> eq <value>.\n  - serialNumber eq 'STIAPL6404' or partNumber eq 'RTICXL6413'\n    Return devices that exactly satisfy one of multiple filter queries.\nExample syntax, <property> eq <value> or <property> eq <value>.\n  - serialNumber eq 'STIAPL6404'\n    Return devices where a property equals a value.\nExample syntax, <property> eq <value>.\n  - createdAt ge ''2024-01-18T19:53:51.480Z''\n    Return devices where a property is greater or equal to a value.\nExample syntax, <property> ge <value>.\n  - updatedAt le '2024-02-18T19:53:51.480Z'\n    Return devices where a property is lesser or equal to a value.\nExample syntax, <property> ge <value>.\n  - not serialNumber eq 'STIAPL6404'\n    Return devices where a property does not equal a value.\nExample syntax, not <property> eq <value>.\n\n**Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`.\n\nFilterable properties: application, archived, assignedState, createdAt, deviceType, id, location, macAddress, model, partNumber, region, serialNumber, subscription, tags, tenantWorkspaceId, type, updatedAt, warranty",
                            },
                        },
                        {
                            "name": "filter-tags",
                            "type": "str",
                            "description": "Filter expressions consisting of simple comparison operations joined\nby logical operators to be applied on the assigned tags or their\nvalues.<br>\n| CLASS               |   EXAMPLES      |\n|---------------------|-----------------|\n| Types               | string          |\n| Comparison          | eq, ne, in      |\n| Logical Expressions | and, or, not    |\n\n\nExamples:\n  - 'street' in 'Regent Street', 'Oxford Street', 'Piccadilly'\n    Return devices containing the tag key and at least one of the specified values.\nExample syntax, <property> in <value>,<value>.\n  - 'city' eq 'London' and 'street' eq 'Piccadilly'\n    Return devices that exactly satisfy multiple filter queries applied to tag keys.\nExample syntax, <property> eq <value> and <property> eq <value>.\n  - 'street' eq 'Oxford Street' or 'street' eq 'Piccadilly'\n    Return devices that satisfy any of multiple filter queries applied to tag keys.\nExample syntax, <property> eq <value> or <property> eq <value>.\n  - 'city' eq 'London'\n    Return devices where a tag key is equal to a tag value.\nExample syntax, <tagKey> eq <tagValue>.\n  - not 'city' eq 'Tokyo'\n    Return devices where a tag key does not equal a tag value.\nExample syntax, not <property> eq <value>.\n\n**Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`.\n\nFilterable properties: application, archived, assignedState, createdAt, deviceType, id, location, macAddress, model, partNumber, region, serialNumber, subscription, tags, tenantWorkspaceId, type, updatedAt, warranty",
                            "required": False,
                            "location": "query",
                            "schema": {
                                "type": "string",
                                "description": "Filter expressions consisting of simple comparison operations joined\nby logical operators to be applied on the assigned tags or their\nvalues.<br>\n| CLASS               |   EXAMPLES      |\n|---------------------|-----------------|\n| Types               | string          |\n| Comparison          | eq, ne, in      |\n| Logical Expressions | and, or, not    |\n\n\nExamples:\n  - 'street' in 'Regent Street', 'Oxford Street', 'Piccadilly'\n    Return devices containing the tag key and at least one of the specified values.\nExample syntax, <property> in <value>,<value>.\n  - 'city' eq 'London' and 'street' eq 'Piccadilly'\n    Return devices that exactly satisfy multiple filter queries applied to tag keys.\nExample syntax, <property> eq <value> and <property> eq <value>.\n  - 'street' eq 'Oxford Street' or 'street' eq 'Piccadilly'\n    Return devices that satisfy any of multiple filter queries applied to tag keys.\nExample syntax, <property> eq <value> or <property> eq <value>.\n  - 'city' eq 'London'\n    Return devices where a tag key is equal to a tag value.\nExample syntax, <tagKey> eq <tagValue>.\n  - not 'city' eq 'Tokyo'\n    Return devices where a tag key does not equal a tag value.\nExample syntax, not <property> eq <value>.\n\n**Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`.\n\nFilterable properties: application, archived, assignedState, createdAt, deviceType, id, location, macAddress, model, partNumber, region, serialNumber, subscription, tags, tenantWorkspaceId, type, updatedAt, warranty",
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
                            "type": "List[str]",
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
