# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
get_endpoint_schema tool implementation for reporting MCP server.

This tool retrieves detailed schema information for a specific API endpoint using endpoint identifier.
Generated for dynamic mode when OpenAPI spec has 3 endpoints (>= 50 threshold).
"""

from typing import Any, Dict, List
from tools.base import BaseTool


class GetEndpointSchemaTool(BaseTool):
    """Retrieves detailed schema information for a specific reporting API endpoint including parameters, request/response models, and validation rules"""

    @property
    def name(self) -> str:
        """Tool name."""
        return "get_endpoint_schema"

    @property
    def description(self) -> str:
        """Tool description."""
        return "Retrieves detailed schema information for a specific reporting API endpoint including parameters, request/response models, and validation rules"

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
                        "GET:/reporting/v1/report-exports-metadata",
                        "GET:/reporting/v1/statuses",
                        "GET:/reporting/v1/statuses/{id}",
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
            endpoint_schemas: dict[str, dict[str, Any]] = {
                "GET:/reporting/v1/report-exports-metadata": {
                    "path": "/reporting/v1/report-exports-metadata",
                    "method": "GET",
                    "summary": "get_reporting_v1_report_exports_metadata",
                    "description": "get_reporting_v1_report_exports_metadata",
                    "operationId": "get_reporting_v1_report_exports_metadata",
                    "tags": [],
                    "deprecated": False,
                    "parameters": [
                        {
                            "name": "filter",
                            "type": "str",
                            "description": "Limit the resources operated on by an endpoint or when used with a multiple-GET endpoint,\nreturn only the subset of resources that match the filter. The filter grammar is a subset\nof OData 4.0.\n\n**NOTE:** The filter query parameter must use [URL encoding](https://en.wikipedia.org/wiki/URL_encoding).\nMost clients do this automatically with inputs provided to them specifically as query parameters. Encoding must be done manually for any query parameters provided as part of the URL.  \nThe reserved characters `!` `#` `$` `&` `'` `(` `)` `*` `+` `,` `/` `:` `;` `=` `?` `@` `[` `]` must be encoded with percent encoded equivalents.\n\nFor example: the value `P06760-B21+2M212504P8` must be encoded as `P06760-B21%2B2M212504P8` when it is used in a query parameter.\n\n| CLASS     |  EXAMPLES                                          |\n|-----------|----------------------------------------------------|\n| Types     | integer, decimal, timestamp, string, boolean, null |\n| Operations| eq, ne, gt, ge, lt, le, in                         |\n| Logic     | and, or, not                                       |\n\n\nExample: name ne Subscriptions and group eq Device inventory\n\n**Filter Syntax**: Use OData-style filters. String values must be enclosed in single quotes.\n\nFilterable properties: columns, filterCriteria, id, kind, name, type",
                            "required": True,
                            "location": "query",
                            "schema": {
                                "type": "string",
                                "description": "Limit the resources operated on by an endpoint or when used with a multiple-GET endpoint,\nreturn only the subset of resources that match the filter. The filter grammar is a subset\nof OData 4.0.\n\n**NOTE:** The filter query parameter must use [URL encoding](https://en.wikipedia.org/wiki/URL_encoding).\nMost clients do this automatically with inputs provided to them specifically as query parameters. Encoding must be done manually for any query parameters provided as part of the URL.  \nThe reserved characters `!` `#` `$` `&` `'` `(` `)` `*` `+` `,` `/` `:` `;` `=` `?` `@` `[` `]` must be encoded with percent encoded equivalents.\n\nFor example: the value `P06760-B21+2M212504P8` must be encoded as `P06760-B21%2B2M212504P8` when it is used in a query parameter.\n\n| CLASS     |  EXAMPLES                                          |\n|-----------|----------------------------------------------------|\n| Types     | integer, decimal, timestamp, string, boolean, null |\n| Operations| eq, ne, gt, ge, lt, le, in                         |\n| Logic     | and, or, not                                       |\n\n\nExample: name ne Subscriptions and group eq Device inventory\n\n**Filter Syntax**: Use OData-style filters. String values must be enclosed in single quotes.\n\nFilterable properties: columns, filterCriteria, id, kind, name, type",
                            },
                        },
                        {
                            "name": "select",
                            "type": "str",
                            "description": "The select query parameter is used to limit the properties returned for a resource. The value of the select query parameter is a comma-separated list of properties.\n\nExample: map[equals:map[description:Return activities where a property equals a value.\n summary:select with equality check value:select=name]]",
                            "required": True,
                            "location": "query",
                            "schema": {
                                "type": "string",
                                "description": "The select query parameter is used to limit the properties returned for a resource. The value of the select query parameter is a comma-separated list of properties.\n\nExample: map[equals:map[description:Return activities where a property equals a value.\n summary:select with equality check value:select=name]]",
                            },
                        },
                        {
                            "name": "sort",
                            "type": "str",
                            "description": "The order in which to return the resources in the collection. The value of the sort query parameter is a comma separated list of sort expressions. Each sort expression is a property name optionally followed by a direction indicator asc (ascending) or desc (descending). The first sort expression in the list defines the primary sort order, the second defines the secondary sort order, and so on. If a direction indicator is omitted, the default direction is ascending.\n\nExamples:\n  - name asc\n    Order ascending by name\n  - name,createdAt desc\n    Order resources ascending by name and then by descending by createdAt",
                            "required": True,
                            "location": "query",
                            "schema": {
                                "type": "string",
                                "description": "The order in which to return the resources in the collection. The value of the sort query parameter is a comma separated list of sort expressions. Each sort expression is a property name optionally followed by a direction indicator asc (ascending) or desc (descending). The first sort expression in the list defines the primary sort order, the second defines the secondary sort order, and so on. If a direction indicator is omitted, the default direction is ascending.\n\nExamples:\n  - name asc\n    Order ascending by name\n  - name,createdAt desc\n    Order resources ascending by name and then by descending by createdAt",
                            },
                        },
                        {
                            "name": "limit",
                            "type": "int",
                            "description": "The maximum number of reports to return.\n\nExample: 10",
                            "required": False,
                            "location": "query",
                            "default": 10,
                            "schema": {
                                "type": "integer",
                                "description": "The maximum number of reports to return.\n\nExample: 10",
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
                            "description": 'Example: type eq "REPORT"\n\n**Filter Syntax**: Use OData-style filters. String values must be enclosed in single quotes.\n\nFilterable properties: createdAt, description, id, isExpired, message, name, recipientEmailId, reportDownloadUrl, reportType, resourceUri, stage, startTime, status, statusTimestamp, type, userName',
                            "required": True,
                            "location": "query",
                            "schema": {
                                "type": "string",
                                "description": 'Example: type eq "REPORT"\n\n**Filter Syntax**: Use OData-style filters. String values must be enclosed in single quotes.\n\nFilterable properties: createdAt, description, id, isExpired, message, name, recipientEmailId, reportDownloadUrl, reportType, resourceUri, stage, startTime, status, statusTimestamp, type, userName',
                            },
                        },
                        {
                            "name": "sort",
                            "type": "str",
                            "description": "The order in which to return the resources in the collection.The value of the sort query parameter is a comma separated list of sort expressions. Each sort expression is a property name optionally followed by a direction indicator asc (ascending) or desc (descending).The first sort expression in the list defines the primary sort order, the second defines the secondary sort order, and so on. If a direction indicator is omitted the default direction is ascending.\n\nExamples:\n  - name asc\n    Order ascending by name\n  - name,createdAt desc\n    Order resources ascending by name and then by descending by createdAt",
                            "required": False,
                            "location": "query",
                            "schema": {
                                "type": "string",
                                "description": "The order in which to return the resources in the collection.The value of the sort query parameter is a comma separated list of sort expressions. Each sort expression is a property name optionally followed by a direction indicator asc (ascending) or desc (descending).The first sort expression in the list defines the primary sort order, the second defines the secondary sort order, and so on. If a direction indicator is omitted the default direction is ascending.\n\nExamples:\n  - name asc\n    Order ascending by name\n  - name,createdAt desc\n    Order resources ascending by name and then by descending by createdAt",
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
