# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
get_endpoint_schema tool implementation for sustainability MCP server.

This tool retrieves detailed schema information for a specific API endpoint using endpoint identifier.
Generated for dynamic mode when OpenAPI spec has 13 endpoints (>= 50 threshold).
"""

from typing import Any, Dict, List
from tools.base import BaseTool


class GetEndpointSchemaTool(BaseTool):
    """Retrieves detailed schema information for a specific sustainability API endpoint including parameters, request/response models, and validation rules"""

    @property
    def name(self) -> str:
        """Tool name."""
        return "get_endpoint_schema"

    @property
    def description(self) -> str:
        """Tool description."""
        return "Retrieves detailed schema information for a specific sustainability API endpoint including parameters, request/response models, and validation rules"

    @property
    def input_schema(self) -> Dict[str, Any]:
        """Input schema for the tool."""
        return {
            "type": "object",
            "properties": {
                "endpoint_identifier": {
                    "type": "string",
                    "description": "The API endpoint identifier in METHOD:PATH format (e.g., 'GET:/sustainability-insight-ctr/v1beta1/usage-totals')",
                    "examples": [
                        "GET:/sustainability-insight-ctr/v1beta1/usage-by-entity",
                        "GET:/sustainability-insight-ctr/v1beta1/coefficients/{id}",
                        "POST:/sustainability-insight-ctr/v1beta1/forecast/energy",
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
                "GET:/sustainability-insight-ctr/v1beta1/usage-by-entity": {
                    "path": "/sustainability-insight-ctr/v1beta1/usage-by-entity",
                    "method": "GET",
                    "summary": "getusagebyentity",
                    "description": "Get energy usage data grouped by entity (device). Returns energy consumption (kWh), carbon footprint (CO2e metric tons), and estimated energy cost per entity with location details.",
                    "operationId": "getusagebyentity",
                    "tags": ["usage"],
                    "deprecated": False,
                    "parameters": [
                        {
                            "name": "start-time",
                            "type": "str",
                            "description": "Start time in ISO 8601 format (e.g. '2024-01-01T00:00:00Z')",
                            "required": True,
                            "location": "query",
                            "schema": {"type": "string", "description": "ISO 8601 datetime"},
                        },
                        {
                            "name": "end-time",
                            "type": "str",
                            "description": "End time in ISO 8601 format (e.g. '2024-01-31T23:59:59Z')",
                            "required": True,
                            "location": "query",
                            "schema": {"type": "string", "description": "ISO 8601 datetime"},
                        },
                        {
                            "name": "filter",
                            "type": "str",
                            "description": "OData-style filter expression. Filterable fields: entityId, entityMake, entityModel, entityType, entitySerialNum, entityProductId, locationName, locationId, locationCity, locationState, locationCountry, name. Examples: \"entityType eq 'Server'\", \"contains(locationCity, 'Houston')\"",
                            "required": False,
                            "location": "query",
                            "schema": {"type": "string"},
                        },
                        {
                            "name": "filter-tags",
                            "type": "str",
                            "description": "Filter by tags. Format: \"'key' eq 'value'\"",
                            "required": False,
                            "location": "query",
                            "schema": {"type": "string"},
                        },
                        {
                            "name": "currency",
                            "type": "str",
                            "description": "Currency code for energy cost (e.g. 'USD', 'EUR', 'GBP')",
                            "required": False,
                            "location": "query",
                            "schema": {"type": "string"},
                        },
                        {
                            "name": "sort",
                            "type": "str",
                            "description": "Sort order for results",
                            "required": False,
                            "location": "query",
                            "schema": {"type": "string"},
                        },
                        {
                            "name": "offset",
                            "type": "int",
                            "description": "Zero-based resource offset to start the response from",
                            "required": False,
                            "location": "query",
                            "schema": {"type": "integer"},
                        },
                        {
                            "name": "limit",
                            "type": "int",
                            "description": "How many items to return at one time",
                            "required": False,
                            "location": "query",
                            "schema": {"type": "integer"},
                        },
                    ],
                    "security": [],
                    "responses": {"200": {"description": "Successful response", "content_type": "application/json"}},
                },
                "GET:/sustainability-insight-ctr/v1beta1/usage-totals": {
                    "path": "/sustainability-insight-ctr/v1beta1/usage-totals",
                    "method": "GET",
                    "summary": "getusagetotals",
                    "description": "Get total aggregated energy usage across all entities for a defined time frame.",
                    "operationId": "getusagetotals",
                    "tags": ["usage"],
                    "deprecated": False,
                    "parameters": [
                        {
                            "name": "start-time",
                            "type": "str",
                            "description": "Start time in ISO 8601 format",
                            "required": True,
                            "location": "query",
                            "schema": {"type": "string"},
                        },
                        {
                            "name": "end-time",
                            "type": "str",
                            "description": "End time in ISO 8601 format",
                            "required": True,
                            "location": "query",
                            "schema": {"type": "string"},
                        },
                        {
                            "name": "filter",
                            "type": "str",
                            "description": "OData-style filter expression",
                            "required": False,
                            "location": "query",
                            "schema": {"type": "string"},
                        },
                        {
                            "name": "filter-tags",
                            "type": "str",
                            "description": "Filter by tags",
                            "required": False,
                            "location": "query",
                            "schema": {"type": "string"},
                        },
                        {
                            "name": "currency",
                            "type": "str",
                            "description": "Currency code for energy cost",
                            "required": False,
                            "location": "query",
                            "schema": {"type": "string"},
                        },
                    ],
                    "security": [],
                    "responses": {"200": {"description": "Successful response", "content_type": "application/json"}},
                },
                "GET:/sustainability-insight-ctr/v1beta1/usage-series": {
                    "path": "/sustainability-insight-ctr/v1beta1/usage-series",
                    "method": "GET",
                    "summary": "getusageseries",
                    "description": "Get energy usage data grouped by time buckets.",
                    "operationId": "getusageseries",
                    "tags": ["usage"],
                    "deprecated": False,
                    "parameters": [
                        {
                            "name": "start-time",
                            "type": "str",
                            "description": "Start time in ISO 8601 format",
                            "required": True,
                            "location": "query",
                            "schema": {"type": "string"},
                        },
                        {
                            "name": "end-time",
                            "type": "str",
                            "description": "End time in ISO 8601 format",
                            "required": True,
                            "location": "query",
                            "schema": {"type": "string"},
                        },
                        {
                            "name": "interval",
                            "type": "str",
                            "description": "Time interval for bucketing. Format: 'integer unit' (e.g. '1 day', '2 hours', '1 month', '1 year')",
                            "required": True,
                            "location": "query",
                            "schema": {"type": "string"},
                        },
                        {
                            "name": "filter",
                            "type": "str",
                            "description": "OData-style filter expression",
                            "required": False,
                            "location": "query",
                            "schema": {"type": "string"},
                        },
                        {
                            "name": "filter-tags",
                            "type": "str",
                            "description": "Filter by tags",
                            "required": False,
                            "location": "query",
                            "schema": {"type": "string"},
                        },
                        {
                            "name": "currency",
                            "type": "str",
                            "description": "Currency code for energy cost",
                            "required": False,
                            "location": "query",
                            "schema": {"type": "string"},
                        },
                    ],
                    "security": [],
                    "responses": {"200": {"description": "Successful response", "content_type": "application/json"}},
                },
                "GET:/sustainability-insight-ctr/v1beta1/cloud-usage-by-entity": {
                    "path": "/sustainability-insight-ctr/v1beta1/cloud-usage-by-entity",
                    "method": "GET",
                    "summary": "getcloudusagebyentity",
                    "description": "Get public cloud sustainability data grouped by entity.",
                    "operationId": "getcloudusagebyentity",
                    "tags": ["cloud-usage"],
                    "deprecated": False,
                    "parameters": [
                        {
                            "name": "start-time",
                            "type": "str",
                            "description": "Start time in ISO 8601 format",
                            "required": True,
                            "location": "query",
                            "schema": {"type": "string"},
                        },
                        {
                            "name": "end-time",
                            "type": "str",
                            "description": "End time in ISO 8601 format",
                            "required": True,
                            "location": "query",
                            "schema": {"type": "string"},
                        },
                        {
                            "name": "filter",
                            "type": "str",
                            "description": "OData-style filter expression. Filterable fields: entityId, serviceProvider, serviceName, serviceRegion, serviceAccount, name",
                            "required": False,
                            "location": "query",
                            "schema": {"type": "string"},
                        },
                        {
                            "name": "sort",
                            "type": "str",
                            "description": "Sort order for results",
                            "required": False,
                            "location": "query",
                            "schema": {"type": "string"},
                        },
                        {
                            "name": "offset",
                            "type": "int",
                            "description": "Zero-based resource offset",
                            "required": False,
                            "location": "query",
                            "schema": {"type": "integer"},
                        },
                        {
                            "name": "limit",
                            "type": "int",
                            "description": "How many items to return",
                            "required": False,
                            "location": "query",
                            "schema": {"type": "integer"},
                        },
                    ],
                    "security": [],
                    "responses": {"200": {"description": "Successful response", "content_type": "application/json"}},
                },
                "GET:/sustainability-insight-ctr/v1beta1/cloud-usage-totals": {
                    "path": "/sustainability-insight-ctr/v1beta1/cloud-usage-totals",
                    "method": "GET",
                    "summary": "getcloudusagetotals",
                    "description": "Get total aggregated public cloud sustainability data.",
                    "operationId": "getcloudusagetotals",
                    "tags": ["cloud-usage"],
                    "deprecated": False,
                    "parameters": [
                        {
                            "name": "start-time",
                            "type": "str",
                            "description": "Start time in ISO 8601 format",
                            "required": True,
                            "location": "query",
                            "schema": {"type": "string"},
                        },
                        {
                            "name": "end-time",
                            "type": "str",
                            "description": "End time in ISO 8601 format",
                            "required": True,
                            "location": "query",
                            "schema": {"type": "string"},
                        },
                        {
                            "name": "filter",
                            "type": "str",
                            "description": "OData-style filter expression",
                            "required": False,
                            "location": "query",
                            "schema": {"type": "string"},
                        },
                    ],
                    "security": [],
                    "responses": {"200": {"description": "Successful response", "content_type": "application/json"}},
                },
                "GET:/sustainability-insight-ctr/v1beta1/cloud-usage-series": {
                    "path": "/sustainability-insight-ctr/v1beta1/cloud-usage-series",
                    "method": "GET",
                    "summary": "getcloudusageseries",
                    "description": "Get public cloud sustainability data grouped by time buckets.",
                    "operationId": "getcloudusageseries",
                    "tags": ["cloud-usage"],
                    "deprecated": False,
                    "parameters": [
                        {
                            "name": "start-time",
                            "type": "str",
                            "description": "Start time in ISO 8601 format",
                            "required": True,
                            "location": "query",
                            "schema": {"type": "string"},
                        },
                        {
                            "name": "end-time",
                            "type": "str",
                            "description": "End time in ISO 8601 format",
                            "required": True,
                            "location": "query",
                            "schema": {"type": "string"},
                        },
                        {
                            "name": "interval",
                            "type": "str",
                            "description": "Time interval for bucketing. Format: 'integer unit' (e.g. '1 day', '1 month')",
                            "required": True,
                            "location": "query",
                            "schema": {"type": "string"},
                        },
                        {
                            "name": "filter",
                            "type": "str",
                            "description": "OData-style filter expression",
                            "required": False,
                            "location": "query",
                            "schema": {"type": "string"},
                        },
                    ],
                    "security": [],
                    "responses": {"200": {"description": "Successful response", "content_type": "application/json"}},
                },
                "GET:/sustainability-insight-ctr/v1beta1/coefficients": {
                    "path": "/sustainability-insight-ctr/v1beta1/coefficients",
                    "method": "GET",
                    "summary": "getcoefficients",
                    "description": "Get cost and CO2 coefficients per location.",
                    "operationId": "getcoefficients",
                    "tags": ["coefficients"],
                    "deprecated": False,
                    "parameters": [
                        {
                            "name": "filter",
                            "type": "str",
                            "description": "OData-style filter expression. Filterable field: locationId",
                            "required": False,
                            "location": "query",
                            "schema": {"type": "string"},
                        },
                        {
                            "name": "filter-tags",
                            "type": "str",
                            "description": "Filter by tags",
                            "required": False,
                            "location": "query",
                            "schema": {"type": "string"},
                        },
                        {
                            "name": "currency",
                            "type": "str",
                            "description": "Currency code",
                            "required": False,
                            "location": "query",
                            "schema": {"type": "string"},
                        },
                        {
                            "name": "offset",
                            "type": "int",
                            "description": "Zero-based resource offset",
                            "required": False,
                            "location": "query",
                            "schema": {"type": "integer"},
                        },
                        {
                            "name": "limit",
                            "type": "int",
                            "description": "How many items to return",
                            "required": False,
                            "location": "query",
                            "schema": {"type": "integer"},
                        },
                    ],
                    "security": [],
                    "responses": {"200": {"description": "Successful response", "content_type": "application/json"}},
                },
                "GET:/sustainability-insight-ctr/v1beta1/coefficients/{id}": {
                    "path": "/sustainability-insight-ctr/v1beta1/coefficients/{id}",
                    "method": "GET",
                    "summary": "getcoefficientbyid",
                    "description": "Get a specific cost and CO2 coefficient by ID.",
                    "operationId": "getcoefficientbyid",
                    "tags": ["coefficients"],
                    "deprecated": False,
                    "parameters": [
                        {
                            "name": "id",
                            "type": "str",
                            "description": "UUID of the coefficient",
                            "required": True,
                            "location": "path",
                            "schema": {"type": "string"},
                        },
                    ],
                    "security": [],
                    "responses": {"200": {"description": "Successful response", "content_type": "application/json"}},
                },
                "GET:/sustainability-insight-ctr/v1beta1/ingests": {
                    "path": "/sustainability-insight-ctr/v1beta1/ingests",
                    "method": "GET",
                    "summary": "getingests",
                    "description": "Get metadata for all uploaded device measurement data imports.",
                    "operationId": "getingests",
                    "tags": ["ingests"],
                    "deprecated": False,
                    "parameters": [
                        {
                            "name": "offset",
                            "type": "int",
                            "description": "Zero-based resource offset",
                            "required": False,
                            "location": "query",
                            "schema": {"type": "integer"},
                        },
                        {
                            "name": "limit",
                            "type": "int",
                            "description": "How many items to return",
                            "required": False,
                            "location": "query",
                            "schema": {"type": "integer"},
                        },
                    ],
                    "security": [],
                    "responses": {"200": {"description": "Successful response", "content_type": "application/json"}},
                },
                "GET:/sustainability-insight-ctr/v1beta1/ingests/{id}": {
                    "path": "/sustainability-insight-ctr/v1beta1/ingests/{id}",
                    "method": "GET",
                    "summary": "getingestbyid",
                    "description": "Get metadata for a specific uploaded device measurement by ID.",
                    "operationId": "getingestbyid",
                    "tags": ["ingests"],
                    "deprecated": False,
                    "parameters": [
                        {
                            "name": "id",
                            "type": "str",
                            "description": "UUID of the ingest",
                            "required": True,
                            "location": "path",
                            "schema": {"type": "string"},
                        },
                    ],
                    "security": [],
                    "responses": {"200": {"description": "Successful response", "content_type": "application/json"}},
                },
                "GET:/sustainability-insight-ctr/v1beta1/datasources": {
                    "path": "/sustainability-insight-ctr/v1beta1/datasources",
                    "method": "GET",
                    "summary": "getdatasources",
                    "description": "Get all data sources connected to Sustainability Insight Center.",
                    "operationId": "getdatasources",
                    "tags": ["datasources"],
                    "deprecated": False,
                    "parameters": [
                        {
                            "name": "offset",
                            "type": "int",
                            "description": "Zero-based resource offset",
                            "required": False,
                            "location": "query",
                            "schema": {"type": "integer"},
                        },
                        {
                            "name": "limit",
                            "type": "int",
                            "description": "How many items to return",
                            "required": False,
                            "location": "query",
                            "schema": {"type": "integer"},
                        },
                    ],
                    "security": [],
                    "responses": {"200": {"description": "Successful response", "content_type": "application/json"}},
                },
                "GET:/sustainability-insight-ctr/v1beta1/datasources/{id}": {
                    "path": "/sustainability-insight-ctr/v1beta1/datasources/{id}",
                    "method": "GET",
                    "summary": "getdatasourcebyid",
                    "description": "Get details of a specific data source by ID.",
                    "operationId": "getdatasourcebyid",
                    "tags": ["datasources"],
                    "deprecated": False,
                    "parameters": [
                        {
                            "name": "id",
                            "type": "str",
                            "description": "UUID of the data source",
                            "required": True,
                            "location": "path",
                            "schema": {"type": "string"},
                        },
                    ],
                    "security": [],
                    "responses": {"200": {"description": "Successful response", "content_type": "application/json"}},
                },
                "POST:/sustainability-insight-ctr/v1beta1/forecast/energy": {
                    "path": "/sustainability-insight-ctr/v1beta1/forecast/energy",
                    "method": "POST",
                    "summary": "forecastenergy",
                    "description": "Get forecasted energy consumption, CO2 emissions, and costs with confidence intervals.",
                    "operationId": "forecastenergy",
                    "tags": ["forecast"],
                    "deprecated": False,
                    "parameters": [
                        {
                            "name": "timePeriodMonths",
                            "type": "int",
                            "description": "Number of months to forecast (1-6)",
                            "required": True,
                            "location": "body",
                            "schema": {"type": "integer", "minimum": 1, "maximum": 6},
                        },
                        {
                            "name": "currencyCode",
                            "type": "str",
                            "description": "Currency code for energy cost (e.g. 'USD')",
                            "required": True,
                            "location": "body",
                            "schema": {"type": "string"},
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
            "str": "example-value",
            "integer": 123,
            "int": 123,
            "number": 123.45,
            "boolean": True,
            "array": ["example1", "example2"],
            "object": {"key": "value"},
        }
        return examples.get(param_type, "example-value")
