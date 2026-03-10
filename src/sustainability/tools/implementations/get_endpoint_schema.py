# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
get_endpoint_schema tool implementation for Sustainability_Insight_Center MCP server.

This tool retrieves detailed schema information for a specific API endpoint using endpoint identifier.
Generated for dynamic mode when OpenAPI spec has 12 endpoints (>= 50 threshold).
"""

from typing import Any, Dict, List
from tools.base import BaseTool


class GetEndpointSchemaTool(BaseTool):
    """Retrieves detailed schema information for a specific Sustainability_Insight_Center API endpoint including parameters, request/response models, and validation rules"""
    
    @property
    def name(self) -> str:
        """Tool name."""
        return "get_endpoint_schema"
    
    @property
    def description(self) -> str:
        """Tool description."""
        return "Retrieves detailed schema information for a specific Sustainability_Insight_Center API endpoint including parameters, request/response models, and validation rules"
    
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
                        "GET:/sustainability-insight-ctr/v1beta1/ingests/{id}",
                        "GET:/sustainability-insight-ctr/v1beta1/usage-by-entity",
                        "GET:/sustainability-insight-ctr/v1beta1/coefficients",
                        "GET:/sustainability-insight-ctr/v1beta1/usage-totals",
                        "GET:/sustainability-insight-ctr/v1beta1/cloud-usage-totals",
                        "GET:/sustainability-insight-ctr/v1beta1/datasources/{id}",
                        "GET:/sustainability-insight-ctr/v1beta1/usage-series",
                        "GET:/sustainability-insight-ctr/v1beta1/cloud-usage-by-entity",
                        "GET:/sustainability-insight-ctr/v1beta1/cloud-usage-series",
                        "GET:/sustainability-insight-ctr/v1beta1/coefficients/{id}",
                        "GET:/sustainability-insight-ctr/v1beta1/datasources",
                        "GET:/sustainability-insight-ctr/v1beta1/ingests",
                    ]
                },
                "include_examples": {
                    "type": "boolean",
                    "description": "Include example parameter values and request/response examples",
                    "default": False
                },
                "include_validation": {
                    "type": "boolean",
                    "description": "Include detailed validation rules and constraints",
                    "default": True
                }
            },
            "required": ["endpoint_identifier"]
        }
    
    async def execute(self, arguments: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Execute the tool to get detailed endpoint schema."""
        try:
            # Extract arguments
            endpoint_identifier = arguments.get("endpoint_identifier", "").strip()
            include_examples = arguments.get("include_examples", False)
            # include_validation parameter available but not currently used
            
            if not endpoint_identifier:
                return [{
                    "success": False,
                    "error": "endpoint_identifier is required",
                    "message": "Please provide an endpoint identifier in METHOD:PATH format"
                }]
            
            # Create endpoint schema map for fast lookup
            endpoint_schemas: dict[str, dict[str, Any]] = {
                "GET:/sustainability-insight-ctr/v1beta1/ingests/{id}": {
                    "path": "/sustainability-insight-ctr/v1beta1/ingests/{id}",
                    "method": "GET",
                    "summary": "getingest",
                    "description": "getingest",
                    "operationId": "getingest",
                    "tags": [],
                    "deprecated": False,
                    "parameters": [
                        {
                            "name": "id",
                            "type": "str",
                            "description": "UUID of the record\n\nExample: 00000000-0000-0000-0000-0000000000000",
                            "required": True,
                            "location": "query",
                            "schema": {
                                "type": "string",
                                "description": "UUID of the record\n\nExample: 00000000-0000-0000-0000-0000000000000"
                            }
                        },
                    ],
                    "security": [],
                    "responses": {
                        "200": {
                            "description": "Successful response",
                            "content_type": "application/json"
                        }
                    }
                },
                "GET:/sustainability-insight-ctr/v1beta1/usage-by-entity": {
                    "path": "/sustainability-insight-ctr/v1beta1/usage-by-entity",
                    "method": "GET",
                    "summary": "getusagebyentity",
                    "description": "getusagebyentity",
                    "operationId": "getusagebyentity",
                    "tags": [],
                    "deprecated": False,
                    "parameters": [
                        {
                            "name": "filter",
                            "type": "str",
                            "description": "Limit the entities operated on by this endpoint, returning only the subset of entities that match the filter. The filter grammar is a subset of OData 4.0 supporting \"eq\", \"in\", and \"and\" operators only.\nUsage entities can be filtered by:\n- entityId\n- entityMake\n- entityModel\n- entityType\n- entitySerialNum\n- entityProductId\n- locationName\n- locationId\n- locationCity\n- locationState\n- locationCountry\n- name\n\n\nExamples:\n  - locationCountry eq 'DE'\n  - entityModel in ('ProLiant DL325 Gen11', 'ProLiant DL380 Gen10')\n\n**Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`.\n\nFilterable properties: co2eMetricTon, cost, costUsd, currency, entityId, entityMake, entityManufacturerTimestamp, entityModel, entityProductId, entitySerialNum, entityType, id, kwh, locationCity, locationCountry, locationId, locationName, locationState, name, tags, type",
                            "required": False,
                            "location": "query",
                            "schema": {
                                "type": "string",
                                "description": "Limit the entities operated on by this endpoint, returning only the subset of entities that match the filter. The filter grammar is a subset of OData 4.0 supporting \"eq\", \"in\", and \"and\" operators only.\nUsage entities can be filtered by:\n- entityId\n- entityMake\n- entityModel\n- entityType\n- entitySerialNum\n- entityProductId\n- locationName\n- locationId\n- locationCity\n- locationState\n- locationCountry\n- name\n\n\nExamples:\n  - locationCountry eq 'DE'\n  - entityModel in ('ProLiant DL325 Gen11', 'ProLiant DL380 Gen10')\n\n**Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`.\n\nFilterable properties: co2eMetricTon, cost, costUsd, currency, entityId, entityMake, entityManufacturerTimestamp, entityModel, entityProductId, entitySerialNum, entityType, id, kwh, locationCity, locationCountry, locationId, locationName, locationState, name, tags, type"
                            }
                        },
                        {
                            "name": "filter-tags",
                            "type": "str",
                            "description": "Limit the entities operated on by this endpoint, returning only the subset of entities that contain the tags. The filter grammar is a subset of OData 4.0 supporting \"eq\" and \"or\" operators only.\nThe tag key is on the left of the operator, the value is on the right.\n\n\nExamples:\n  - 'Tagged' eq ''\n  - 'OS' eq 'Linux' or 'OS' eq 'Windows'\n  - 'OS' eq 'Linux'\n\n**Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`.\n\nFilterable properties: co2eMetricTon, cost, costUsd, currency, entityId, entityMake, entityManufacturerTimestamp, entityModel, entityProductId, entitySerialNum, entityType, id, kwh, locationCity, locationCountry, locationId, locationName, locationState, name, tags, type",
                            "required": False,
                            "location": "query",
                            "schema": {
                                "type": "string",
                                "description": "Limit the entities operated on by this endpoint, returning only the subset of entities that contain the tags. The filter grammar is a subset of OData 4.0 supporting \"eq\" and \"or\" operators only.\nThe tag key is on the left of the operator, the value is on the right.\n\n\nExamples:\n  - 'Tagged' eq ''\n  - 'OS' eq 'Linux' or 'OS' eq 'Windows'\n  - 'OS' eq 'Linux'\n\n**Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`.\n\nFilterable properties: co2eMetricTon, cost, costUsd, currency, entityId, entityMake, entityManufacturerTimestamp, entityModel, entityProductId, entitySerialNum, entityType, id, kwh, locationCity, locationCountry, locationId, locationName, locationState, name, tags, type"
                            }
                        },
                        {
                            "name": "currency",
                            "type": "str",
                            "description": "The 3 letter currency code the cost returned will be in, case insensitive. Currency calculations are done via a factor queried at the beginning of the day. Defaults to USD.\n\n\nExample: CAD",
                            "required": False,
                            "location": "query",
                            "schema": {
                                "type": "string",
                                "description": "The 3 letter currency code the cost returned will be in, case insensitive. Currency calculations are done via a factor queried at the beginning of the day. Defaults to USD.\n\n\nExample: CAD"
                            }
                        },
                        {
                            "name": "sort",
                            "type": "str",
                            "description": "Odata 4.0 field to sort entities on. Allowed fields are the strings \"locationName\", \"locationCountry\", \"locationState\", \"entityId\", \"entityMake\", \"entityModel\", \"entityType\", \"entitySerialNum\", \"entityProductId\", \"name\". Must be of the format \"property order\".\n\nExamples:\n  - entityId desc\n  - name asc",
                            "required": False,
                            "location": "query",
                            "schema": {
                                "type": "string",
                                "description": "Odata 4.0 field to sort entities on. Allowed fields are the strings \"locationName\", \"locationCountry\", \"locationState\", \"entityId\", \"entityMake\", \"entityModel\", \"entityType\", \"entitySerialNum\", \"entityProductId\", \"name\". Must be of the format \"property order\".\n\nExamples:\n  - entityId desc\n  - name asc"
                            }
                        },
                        {
                            "name": "offset",
                            "type": "int",
                            "description": "Zero-based resource offset to start the response from.\n\nExample: 10",
                            "required": False,
                            "location": "query",
                            "schema": {
                                "type": "integer",
                                "description": "Zero-based resource offset to start the response from.\n\nExample: 10"
                            }
                        },
                        {
                            "name": "limit",
                            "type": "int",
                            "description": "Number of usages to return.\n\nExample: 10",
                            "required": False,
                            "location": "query",
                            "default": 10,
                            "schema": {
                                "type": "integer",
                                "description": "Number of usages to return.\n\nExample: 10",
                                "default": "10"
                            }
                        },
                        {
                            "name": "start-time",
                            "type": "str",
                            "description": "Start of the query's time range in ISO8601 format.\n\nExample: 2024-01-28T08:00:00Z",
                            "required": True,
                            "location": "query",
                            "schema": {
                                "type": "string",
                                "description": "Start of the query's time range in ISO8601 format.\n\nExample: 2024-01-28T08:00:00Z"
                            }
                        },
                        {
                            "name": "end-time",
                            "type": "str",
                            "description": "End of the query's time range in ISO8601 format.\n\nExample: 2024-01-29T08:00:00Z",
                            "required": True,
                            "location": "query",
                            "schema": {
                                "type": "string",
                                "description": "End of the query's time range in ISO8601 format.\n\nExample: 2024-01-29T08:00:00Z"
                            }
                        },
                    ],
                    "security": [],
                    "responses": {
                        "200": {
                            "description": "Successful response",
                            "content_type": "application/json"
                        }
                    }
                },
                "GET:/sustainability-insight-ctr/v1beta1/coefficients": {
                    "path": "/sustainability-insight-ctr/v1beta1/coefficients",
                    "method": "GET",
                    "summary": "getcoefficients",
                    "description": "getcoefficients",
                    "operationId": "getcoefficients",
                    "tags": [],
                    "deprecated": False,
                    "parameters": [
                        {
                            "name": "offset",
                            "type": "int",
                            "description": "Zero-based resource offset to start the response from.\n\nExample: 10",
                            "required": False,
                            "location": "query",
                            "schema": {
                                "type": "integer",
                                "description": "Zero-based resource offset to start the response from.\n\nExample: 10"
                            }
                        },
                        {
                            "name": "limit",
                            "type": "int",
                            "description": "Number of entities to return.\n\nExample: 10",
                            "required": False,
                            "location": "query",
                            "default": 10,
                            "schema": {
                                "type": "integer",
                                "description": "Number of entities to return.\n\nExample: 10",
                                "default": "10"
                            }
                        },
                        {
                            "name": "filter",
                            "type": "str",
                            "description": "Limit the coefficients operated on by this endpoint, returning only the subset of entities that match the filter. The filter grammar is a subset of OData 4.0 supporting \"eq\" operator only.\nCoefficients can be filtered by:\n- locationId\n\n\nExample: locationId eq '00000000-0000-0000-0000-0000000000000'\n\n**Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`.\n\nFilterable properties: associatedLocation, co2eGramsPerKwh, costPerKwh, costUsdPerKwh, createdAt, currency, generation, id, startTime, type, updatedAt",
                            "required": False,
                            "location": "query",
                            "schema": {
                                "type": "string",
                                "description": "Limit the coefficients operated on by this endpoint, returning only the subset of entities that match the filter. The filter grammar is a subset of OData 4.0 supporting \"eq\" operator only.\nCoefficients can be filtered by:\n- locationId\n\n\nExample: locationId eq '00000000-0000-0000-0000-0000000000000'\n\n**Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`.\n\nFilterable properties: associatedLocation, co2eGramsPerKwh, costPerKwh, costUsdPerKwh, createdAt, currency, generation, id, startTime, type, updatedAt"
                            }
                        },
                    ],
                    "security": [],
                    "responses": {
                        "200": {
                            "description": "Successful response",
                            "content_type": "application/json"
                        }
                    }
                },
                "GET:/sustainability-insight-ctr/v1beta1/usage-totals": {
                    "path": "/sustainability-insight-ctr/v1beta1/usage-totals",
                    "method": "GET",
                    "summary": "getusagetotals",
                    "description": "getusagetotals",
                    "operationId": "getusagetotals",
                    "tags": [],
                    "deprecated": False,
                    "parameters": [
                        {
                            "name": "filter",
                            "type": "str",
                            "description": "Limit the entities operated on by this endpoint, returning only the usage for entities that match the filter. The filter grammar is a subset of OData 4.0 supporting \"eq\", \"in\", and \"and\" operators only.\nUsage entities can be filtered by:\n- entityId\n- entityMake\n- entityModel\n- entityType\n- entitySerialNum\n- entityProductId\n- locationName\n- locationId\n- locationCity\n- locationState\n- locationCountry\n\n\nExamples:\n  - locationCountry eq 'DE'\n  - entityModel in ('ProLiant DL325 Gen11', 'ProLiant DL380 Gen10')\n\n**Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`.\n\nFilterable properties: co2eMetricTon, cost, costUsd, currency, kwh, type",
                            "required": False,
                            "location": "query",
                            "schema": {
                                "type": "string",
                                "description": "Limit the entities operated on by this endpoint, returning only the usage for entities that match the filter. The filter grammar is a subset of OData 4.0 supporting \"eq\", \"in\", and \"and\" operators only.\nUsage entities can be filtered by:\n- entityId\n- entityMake\n- entityModel\n- entityType\n- entitySerialNum\n- entityProductId\n- locationName\n- locationId\n- locationCity\n- locationState\n- locationCountry\n\n\nExamples:\n  - locationCountry eq 'DE'\n  - entityModel in ('ProLiant DL325 Gen11', 'ProLiant DL380 Gen10')\n\n**Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`.\n\nFilterable properties: co2eMetricTon, cost, costUsd, currency, kwh, type"
                            }
                        },
                        {
                            "name": "filter-tags",
                            "type": "str",
                            "description": "Limit the entities operated on by this endpoint, returning only the subset of entities that contain the tags. The filter grammar is a subset of OData 4.0 supporting \"eq\" and \"or\" operators only.\nThe tag key is on the left of the operator, the value is on the right.\n\n\nExamples:\n  - 'OS' eq 'Linux' or 'OS' eq 'Windows'\n  - 'OS' eq 'Linux'\n  - 'Tagged' eq ''\n\n**Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`.\n\nFilterable properties: co2eMetricTon, cost, costUsd, currency, kwh, type",
                            "required": False,
                            "location": "query",
                            "schema": {
                                "type": "string",
                                "description": "Limit the entities operated on by this endpoint, returning only the subset of entities that contain the tags. The filter grammar is a subset of OData 4.0 supporting \"eq\" and \"or\" operators only.\nThe tag key is on the left of the operator, the value is on the right.\n\n\nExamples:\n  - 'OS' eq 'Linux' or 'OS' eq 'Windows'\n  - 'OS' eq 'Linux'\n  - 'Tagged' eq ''\n\n**Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`.\n\nFilterable properties: co2eMetricTon, cost, costUsd, currency, kwh, type"
                            }
                        },
                        {
                            "name": "currency",
                            "type": "str",
                            "description": "The 3 letter currency code the cost returned will be in, case insensitive. Currency calculations are done via a factor queried at the beginning of the day. Defaults to USD.\n\n\nExample: CAD",
                            "required": False,
                            "location": "query",
                            "schema": {
                                "type": "string",
                                "description": "The 3 letter currency code the cost returned will be in, case insensitive. Currency calculations are done via a factor queried at the beginning of the day. Defaults to USD.\n\n\nExample: CAD"
                            }
                        },
                        {
                            "name": "start-time",
                            "type": "str",
                            "description": "Start of the query's time range in ISO8601 format.\n\nExample: 2024-01-28T08:00:00Z",
                            "required": True,
                            "location": "query",
                            "schema": {
                                "type": "string",
                                "description": "Start of the query's time range in ISO8601 format.\n\nExample: 2024-01-28T08:00:00Z"
                            }
                        },
                        {
                            "name": "end-time",
                            "type": "str",
                            "description": "End of the aggregate's time range in ISO8601 format.\n\nExample: 2024-01-29T08:00:00Z",
                            "required": True,
                            "location": "query",
                            "schema": {
                                "type": "string",
                                "description": "End of the aggregate's time range in ISO8601 format.\n\nExample: 2024-01-29T08:00:00Z"
                            }
                        },
                    ],
                    "security": [],
                    "responses": {
                        "200": {
                            "description": "Successful response",
                            "content_type": "application/json"
                        }
                    }
                },
                "GET:/sustainability-insight-ctr/v1beta1/cloud-usage-totals": {
                    "path": "/sustainability-insight-ctr/v1beta1/cloud-usage-totals",
                    "method": "GET",
                    "summary": "getcloudusagetotals",
                    "description": "getcloudusagetotals",
                    "operationId": "getcloudusagetotals",
                    "tags": [],
                    "deprecated": False,
                    "parameters": [
                        {
                            "name": "filter",
                            "type": "str",
                            "description": "Limit the cloud entities operated on by this endpoint, returning only the subset of entities that match the filter. The \nfilter grammar is a subset of OData 4.0 supporting \"eq\", \"in\", and \"and\" operators only.\n\nCloud entities can be filtered by:\n- entityId\n- serviceProvider\n- serviceName\n- serviceRegion\n- serviceAccount\n- name\n\n\nExamples:\n  - serviceProvider eq 'AWS'\n  - serviceRegion in ('EMEA', 'AMERICAS')\n\n**Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`.\n\nFilterable properties: co2eMetricTon, type",
                            "required": False,
                            "location": "query",
                            "schema": {
                                "type": "string",
                                "description": "Limit the cloud entities operated on by this endpoint, returning only the subset of entities that match the filter. The \nfilter grammar is a subset of OData 4.0 supporting \"eq\", \"in\", and \"and\" operators only.\n\nCloud entities can be filtered by:\n- entityId\n- serviceProvider\n- serviceName\n- serviceRegion\n- serviceAccount\n- name\n\n\nExamples:\n  - serviceProvider eq 'AWS'\n  - serviceRegion in ('EMEA', 'AMERICAS')\n\n**Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`.\n\nFilterable properties: co2eMetricTon, type"
                            }
                        },
                        {
                            "name": "start-time",
                            "type": "str",
                            "description": "Start of the query's time range in ISO8601 format.\n\nExample: 2024-01-28T08:00:00Z",
                            "required": True,
                            "location": "query",
                            "schema": {
                                "type": "string",
                                "description": "Start of the query's time range in ISO8601 format.\n\nExample: 2024-01-28T08:00:00Z"
                            }
                        },
                        {
                            "name": "end-time",
                            "type": "str",
                            "description": "End of the aggregate's time range in ISO8601 format.\n\nExample: 2024-01-29T08:00:00Z",
                            "required": True,
                            "location": "query",
                            "schema": {
                                "type": "string",
                                "description": "End of the aggregate's time range in ISO8601 format.\n\nExample: 2024-01-29T08:00:00Z"
                            }
                        },
                    ],
                    "security": [],
                    "responses": {
                        "200": {
                            "description": "Successful response",
                            "content_type": "application/json"
                        }
                    }
                },
                "GET:/sustainability-insight-ctr/v1beta1/datasources/{id}": {
                    "path": "/sustainability-insight-ctr/v1beta1/datasources/{id}",
                    "method": "GET",
                    "summary": "getdatasource",
                    "description": "getdatasource",
                    "operationId": "getdatasource",
                    "tags": [],
                    "deprecated": False,
                    "parameters": [
                        {
                            "name": "id",
                            "type": "str",
                            "description": "ID of the data source\n\nExample: 00000000-0000-0000-0000-0000000000000",
                            "required": True,
                            "location": "query",
                            "schema": {
                                "type": "string",
                                "description": "ID of the data source\n\nExample: 00000000-0000-0000-0000-0000000000000"
                            }
                        },
                    ],
                    "security": [],
                    "responses": {
                        "200": {
                            "description": "Successful response",
                            "content_type": "application/json"
                        }
                    }
                },
                "GET:/sustainability-insight-ctr/v1beta1/usage-series": {
                    "path": "/sustainability-insight-ctr/v1beta1/usage-series",
                    "method": "GET",
                    "summary": "getusagebyseries",
                    "description": "getusagebyseries",
                    "operationId": "getusagebyseries",
                    "tags": [],
                    "deprecated": False,
                    "parameters": [
                        {
                            "name": "filter",
                            "type": "str",
                            "description": "Limit the entities operated on by this endpoint, returning only the usage for entities that match the filter. The filter grammar is a subset of OData 4.0 supporting \"eq\", \"in\", and \"and\" operators only.\nUsage entities can be filtered by:\n- entityId\n- entityMake\n- entityModel\n- entityType\n- entitySerialNum\n- entityProductId\n- locationName\n- locationId\n- locationCity\n- locationState\n- locationCountry\n\n\nExamples:\n  - locationCountry eq 'DE'\n  - entityModel in ('ProLiant DL325 Gen11', 'ProLiant DL380 Gen10')\n\n**Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`.\n\nFilterable properties: co2eMetricTon, cost, costUsd, currency, id, kwh, timeBucket, type",
                            "required": False,
                            "location": "query",
                            "schema": {
                                "type": "string",
                                "description": "Limit the entities operated on by this endpoint, returning only the usage for entities that match the filter. The filter grammar is a subset of OData 4.0 supporting \"eq\", \"in\", and \"and\" operators only.\nUsage entities can be filtered by:\n- entityId\n- entityMake\n- entityModel\n- entityType\n- entitySerialNum\n- entityProductId\n- locationName\n- locationId\n- locationCity\n- locationState\n- locationCountry\n\n\nExamples:\n  - locationCountry eq 'DE'\n  - entityModel in ('ProLiant DL325 Gen11', 'ProLiant DL380 Gen10')\n\n**Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`.\n\nFilterable properties: co2eMetricTon, cost, costUsd, currency, id, kwh, timeBucket, type"
                            }
                        },
                        {
                            "name": "filter-tags",
                            "type": "str",
                            "description": "Limit the entities operated on by this endpoint, returning only the subset of entities that contain the tags. The filter grammar is a subset of OData 4.0 supporting \"eq\" and \"or\" operators only.\nThe tag key is on the left of the operator, the value is on the right.\n\n\nExamples:\n  - 'OS' eq 'Linux'\n  - 'Tagged' eq ''\n  - 'OS' eq 'Linux' or 'OS' eq 'Windows'\n\n**Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`.\n\nFilterable properties: co2eMetricTon, cost, costUsd, currency, id, kwh, timeBucket, type",
                            "required": False,
                            "location": "query",
                            "schema": {
                                "type": "string",
                                "description": "Limit the entities operated on by this endpoint, returning only the subset of entities that contain the tags. The filter grammar is a subset of OData 4.0 supporting \"eq\" and \"or\" operators only.\nThe tag key is on the left of the operator, the value is on the right.\n\n\nExamples:\n  - 'OS' eq 'Linux'\n  - 'Tagged' eq ''\n  - 'OS' eq 'Linux' or 'OS' eq 'Windows'\n\n**Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`.\n\nFilterable properties: co2eMetricTon, cost, costUsd, currency, id, kwh, timeBucket, type"
                            }
                        },
                        {
                            "name": "currency",
                            "type": "str",
                            "description": "The 3 letter currency code the cost returned will be in, case insensitive. Currency calculations are done via a factor queried at the beginning of the day. Defaults to USD.\n\n\nExample: CAD",
                            "required": False,
                            "location": "query",
                            "schema": {
                                "type": "string",
                                "description": "The 3 letter currency code the cost returned will be in, case insensitive. Currency calculations are done via a factor queried at the beginning of the day. Defaults to USD.\n\n\nExample: CAD"
                            }
                        },
                        {
                            "name": "interval",
                            "type": "str",
                            "description": "Interval of the created time series. Must be of the format \"integer unit\". Valid units are day(s), hour(s), week(s), month(s), and year(s).\n\nExamples:\n  - 2 hours\n  - 1 day",
                            "required": True,
                            "location": "query",
                            "schema": {
                                "type": "string",
                                "description": "Interval of the created time series. Must be of the format \"integer unit\". Valid units are day(s), hour(s), week(s), month(s), and year(s).\n\nExamples:\n  - 2 hours\n  - 1 day"
                            }
                        },
                        {
                            "name": "start-time",
                            "type": "str",
                            "description": "Start of the query's time range in ISO8601 format.\n\nExample: 2024-01-28T08:00:00Z",
                            "required": True,
                            "location": "query",
                            "schema": {
                                "type": "string",
                                "description": "Start of the query's time range in ISO8601 format.\n\nExample: 2024-01-28T08:00:00Z"
                            }
                        },
                        {
                            "name": "end-time",
                            "type": "str",
                            "description": "End of the query's time range in ISO8601 format.\n\nExample: 2024-01-29T08:00:00Z",
                            "required": True,
                            "location": "query",
                            "schema": {
                                "type": "string",
                                "description": "End of the query's time range in ISO8601 format.\n\nExample: 2024-01-29T08:00:00Z"
                            }
                        },
                    ],
                    "security": [],
                    "responses": {
                        "200": {
                            "description": "Successful response",
                            "content_type": "application/json"
                        }
                    }
                },
                "GET:/sustainability-insight-ctr/v1beta1/cloud-usage-by-entity": {
                    "path": "/sustainability-insight-ctr/v1beta1/cloud-usage-by-entity",
                    "method": "GET",
                    "summary": "getcloudusagebyentity",
                    "description": "getcloudusagebyentity",
                    "operationId": "getcloudusagebyentity",
                    "tags": [],
                    "deprecated": False,
                    "parameters": [
                        {
                            "name": "filter",
                            "type": "str",
                            "description": "Limit the cloud entities operated on by this endpoint, returning only the subset of entities that match the filter. The \nfilter grammar is a subset of OData 4.0 supporting \"eq\", \"in\", and \"and\" operators only.\n\nCloud entities can be filtered by:\n- entityId\n- serviceProvider\n- serviceName\n- serviceRegion\n- serviceAccount\n- name\n\n\nExamples:\n  - serviceProvider eq 'AWS'\n  - serviceRegion in ('EMEA', 'AMERICAS')\n\n**Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`.\n\nFilterable properties: co2eMetricTon, entityId, id, name, serviceAccount, serviceName, serviceProvider, serviceRegion, type",
                            "required": False,
                            "location": "query",
                            "schema": {
                                "type": "string",
                                "description": "Limit the cloud entities operated on by this endpoint, returning only the subset of entities that match the filter. The \nfilter grammar is a subset of OData 4.0 supporting \"eq\", \"in\", and \"and\" operators only.\n\nCloud entities can be filtered by:\n- entityId\n- serviceProvider\n- serviceName\n- serviceRegion\n- serviceAccount\n- name\n\n\nExamples:\n  - serviceProvider eq 'AWS'\n  - serviceRegion in ('EMEA', 'AMERICAS')\n\n**Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`.\n\nFilterable properties: co2eMetricTon, entityId, id, name, serviceAccount, serviceName, serviceProvider, serviceRegion, type"
                            }
                        },
                        {
                            "name": "sort",
                            "type": "str",
                            "description": "Odata 4.0 field to sort entities on. Allowed fields are the strings \"entityId\", \"serviceProvider\", \"serviceName\", \"serviceRegion\", \"serviceAccount\", \"name\". Must be of the format \"property order\".\n\nExamples:\n  - entityId desc\n  - serviceAccount asc",
                            "required": False,
                            "location": "query",
                            "schema": {
                                "type": "string",
                                "description": "Odata 4.0 field to sort entities on. Allowed fields are the strings \"entityId\", \"serviceProvider\", \"serviceName\", \"serviceRegion\", \"serviceAccount\", \"name\". Must be of the format \"property order\".\n\nExamples:\n  - entityId desc\n  - serviceAccount asc"
                            }
                        },
                        {
                            "name": "offset",
                            "type": "int",
                            "description": "Zero-based resource offset to start the response from.\n\nExample: 10",
                            "required": False,
                            "location": "query",
                            "schema": {
                                "type": "integer",
                                "description": "Zero-based resource offset to start the response from.\n\nExample: 10"
                            }
                        },
                        {
                            "name": "limit",
                            "type": "int",
                            "description": "Number of usages to return.\n\nExample: 10",
                            "required": False,
                            "location": "query",
                            "default": 10,
                            "schema": {
                                "type": "integer",
                                "description": "Number of usages to return.\n\nExample: 10",
                                "default": "10"
                            }
                        },
                        {
                            "name": "start-time",
                            "type": "str",
                            "description": "Start of the query's time range in ISO8601 format.\n\nExample: 2024-01-28T08:00:00Z",
                            "required": True,
                            "location": "query",
                            "schema": {
                                "type": "string",
                                "description": "Start of the query's time range in ISO8601 format.\n\nExample: 2024-01-28T08:00:00Z"
                            }
                        },
                        {
                            "name": "end-time",
                            "type": "str",
                            "description": "End of the query's time range in ISO8601 format.\n\nExample: 2024-01-29T08:00:00Z",
                            "required": True,
                            "location": "query",
                            "schema": {
                                "type": "string",
                                "description": "End of the query's time range in ISO8601 format.\n\nExample: 2024-01-29T08:00:00Z"
                            }
                        },
                    ],
                    "security": [],
                    "responses": {
                        "200": {
                            "description": "Successful response",
                            "content_type": "application/json"
                        }
                    }
                },
                "GET:/sustainability-insight-ctr/v1beta1/cloud-usage-series": {
                    "path": "/sustainability-insight-ctr/v1beta1/cloud-usage-series",
                    "method": "GET",
                    "summary": "getcloudusagebyseries",
                    "description": "getcloudusagebyseries",
                    "operationId": "getcloudusagebyseries",
                    "tags": [],
                    "deprecated": False,
                    "parameters": [
                        {
                            "name": "filter",
                            "type": "str",
                            "description": "Limit the cloud entities operated on by this endpoint, returning only the subset of entities that match the filter. The \nfilter grammar is a subset of OData 4.0 supporting \"eq\", \"in\", and \"and\" operators only.\n\nCloud entities can be filtered by:\n- entityId\n- serviceProvider\n- serviceName\n- serviceRegion\n- serviceAccount\n- name\n\n\nExamples:\n  - serviceRegion in ('EMEA', 'AMERICAS')\n  - serviceProvider eq 'AWS'\n\n**Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`.\n\nFilterable properties: co2eMetricTon, id, timeBucket, type",
                            "required": False,
                            "location": "query",
                            "schema": {
                                "type": "string",
                                "description": "Limit the cloud entities operated on by this endpoint, returning only the subset of entities that match the filter. The \nfilter grammar is a subset of OData 4.0 supporting \"eq\", \"in\", and \"and\" operators only.\n\nCloud entities can be filtered by:\n- entityId\n- serviceProvider\n- serviceName\n- serviceRegion\n- serviceAccount\n- name\n\n\nExamples:\n  - serviceRegion in ('EMEA', 'AMERICAS')\n  - serviceProvider eq 'AWS'\n\n**Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`.\n\nFilterable properties: co2eMetricTon, id, timeBucket, type"
                            }
                        },
                        {
                            "name": "interval",
                            "type": "str",
                            "description": "Interval of the created time series. Must be of the format \"integer unit\". Valid units are day(s), hour\n(s), week(s), month(s), and year(s). Cloud usage typically is measured in months, so the smaller time units are \nlikely to be approximations.\n\n\nExamples:\n  - 3 months\n  - 1 month",
                            "required": True,
                            "location": "query",
                            "schema": {
                                "type": "string",
                                "description": "Interval of the created time series. Must be of the format \"integer unit\". Valid units are day(s), hour\n(s), week(s), month(s), and year(s). Cloud usage typically is measured in months, so the smaller time units are \nlikely to be approximations.\n\n\nExamples:\n  - 3 months\n  - 1 month"
                            }
                        },
                        {
                            "name": "start-time",
                            "type": "str",
                            "description": "Start of the query's time range in ISO8601 format.\n\nExample: 2024-01-28T08:00:00Z",
                            "required": True,
                            "location": "query",
                            "schema": {
                                "type": "string",
                                "description": "Start of the query's time range in ISO8601 format.\n\nExample: 2024-01-28T08:00:00Z"
                            }
                        },
                        {
                            "name": "end-time",
                            "type": "str",
                            "description": "End of the query's time range in ISO8601 format.\n\nExample: 2024-01-29T08:00:00Z",
                            "required": True,
                            "location": "query",
                            "schema": {
                                "type": "string",
                                "description": "End of the query's time range in ISO8601 format.\n\nExample: 2024-01-29T08:00:00Z"
                            }
                        },
                    ],
                    "security": [],
                    "responses": {
                        "200": {
                            "description": "Successful response",
                            "content_type": "application/json"
                        }
                    }
                },
                "GET:/sustainability-insight-ctr/v1beta1/coefficients/{id}": {
                    "path": "/sustainability-insight-ctr/v1beta1/coefficients/{id}",
                    "method": "GET",
                    "summary": "getcoefficient",
                    "description": "getcoefficient",
                    "operationId": "getcoefficient",
                    "tags": [],
                    "deprecated": False,
                    "parameters": [
                        {
                            "name": "id",
                            "type": "str",
                            "description": "UUID of the coefficient mapping\n\nExample: 00000000-0000-0000-0000-0000000000000",
                            "required": True,
                            "location": "query",
                            "schema": {
                                "type": "string",
                                "description": "UUID of the coefficient mapping\n\nExample: 00000000-0000-0000-0000-0000000000000"
                            }
                        },
                    ],
                    "security": [],
                    "responses": {
                        "200": {
                            "description": "Successful response",
                            "content_type": "application/json"
                        }
                    }
                },
                "GET:/sustainability-insight-ctr/v1beta1/datasources": {
                    "path": "/sustainability-insight-ctr/v1beta1/datasources",
                    "method": "GET",
                    "summary": "getdatasources",
                    "description": "getdatasources",
                    "operationId": "getdatasources",
                    "tags": [],
                    "deprecated": False,
                    "parameters": [
                    ],
                    "security": [],
                    "responses": {
                        "200": {
                            "description": "Successful response",
                            "content_type": "application/json"
                        }
                    }
                },
                "GET:/sustainability-insight-ctr/v1beta1/ingests": {
                    "path": "/sustainability-insight-ctr/v1beta1/ingests",
                    "method": "GET",
                    "summary": "getingests",
                    "description": "getingests",
                    "operationId": "getingests",
                    "tags": [],
                    "deprecated": False,
                    "parameters": [
                        {
                            "name": "offset",
                            "type": "int",
                            "description": "Zero-based resource offset to start the response from.\n\nExample: 10",
                            "required": False,
                            "location": "query",
                            "schema": {
                                "type": "integer",
                                "description": "Zero-based resource offset to start the response from.\n\nExample: 10"
                            }
                        },
                        {
                            "name": "limit",
                            "type": "int",
                            "description": "Number of ingested records to return.\n\nExample: 10",
                            "required": False,
                            "location": "query",
                            "default": 10,
                            "schema": {
                                "type": "integer",
                                "description": "Number of ingested records to return.\n\nExample: 10",
                                "default": "10"
                            }
                        },
                    ],
                    "security": [],
                    "responses": {
                        "200": {
                            "description": "Successful response",
                            "content_type": "application/json"
                        }
                    }
                },
            }
            
            # Find the matching endpoint
            if endpoint_identifier not in endpoint_schemas:
                available_endpoints = list(endpoint_schemas.keys())
                return [{
                    "success": False,
                    "error": f"Endpoint not found: {endpoint_identifier}",
                    "message": f"Available endpoints: {', '.join(available_endpoints[:10])}{'...' if len(available_endpoints) > 10 else ''}"
                }]
            
            schema = endpoint_schemas[endpoint_identifier]
            
            # Add examples if requested
            if include_examples:
                for param in schema["parameters"]:  # type: ignore[attr-defined]
                    if "example" not in param:
                        param["example"] = self._generate_example_value(param["type"])
            
            return [{
                "success": True,
                "endpoint_identifier": endpoint_identifier,
                "schema": schema
            }]
            
        except Exception as e:
            return [{
                "success": False,
                "error": f"Failed to retrieve endpoint schema: {str(e)}",
                "message": "An error occurred while retrieving the endpoint schema"
            }]
    
    def _generate_example_value(self, param_type: str) -> Any:
        """Generate example values for parameters based on type."""
        examples = {
            "string": "example-value",
            "integer": 123,
            "number": 123.45,
            "boolean": True,
            "array": ["example1", "example2"],
            "object": {"key": "value"}
        }
        return examples.get(param_type, "example-value")
