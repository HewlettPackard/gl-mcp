# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
get_endpoint_schema tool implementation for service-catalog MCP server.

This tool retrieves detailed schema information for a specific API endpoint using endpoint identifier.
Generated for dynamic mode when OpenAPI spec has 12 endpoints (>= 50 threshold).
"""

from __future__ import annotations

from typing import Annotated, Any

from pydantic import Field

from greenlake_service_catalog_mcp.config.logging import get_logger
from greenlake_service_catalog_mcp.server.fastmcp_instance import mcp

logger = get_logger(__name__)


@mcp.tool(
    name="get_endpoint_schema",
    description="Retrieves detailed schema information for a specific service-catalog API endpoint including parameters, request/response models, and validation rules",
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
    """Retrieves detailed schema information for a specific service-catalog API endpoint.

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
        "GET:/service-catalog/v1beta1/service-offer-regions": {
            "path": "/service-catalog/v1beta1/service-offer-regions",
            "method": "GET",
            "summary": "getserviceofferregions",
            "description": "getserviceofferregions",
            "operationId": "getserviceofferregions",
            "tags": [],
            "deprecated": False,
            "parameters": [
                {
                    "name": "next",
                    "type": "str",
                    "description": "Specifies the pagination cursor for the next page of service offer regions.\n\nExample: 64136af7-cd64-4b4e-88a8-150ab51a920d",
                    "required": False,
                    "location": "query",
                    "schema": {
                        "type": "string",
                        "description": "Specifies the pagination cursor for the next page of service offer regions.\n\nExample: 64136af7-cd64-4b4e-88a8-150ab51a920d",
                    },
                },
                {
                    "name": "limit",
                    "type": "int",
                    "description": "Specifies the number of results to be returned.",
                    "required": False,
                    "location": "query",
                    "default": 2000,
                    "schema": {
                        "type": "integer",
                        "description": "Specifies the number of results to be returned.",
                        "default": "2000",
                    },
                },
                {
                    "name": "filter",
                    "type": "str",
                    "description": "The `filter` query parameter is used to filter the set of resources returned in a `GET` request. The returned set of resources must match the criteria in the filter query parameter.<br><br> The value of the `filter` query parameter is a subset of [OData 4.0](https://www.odata.org/documentation/) filter expressions consisting of simple comparison operations joined by logical operators.<br><br>**Supported fields**: `serviceOfferId`, `status`, and `region`.<br>**Supported operand**: `eq`<br>**Supported operations**: `and`\n\nExamples:\n  - serviceOfferId eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050' and status eq 'ONBOARDED' and region eq 'us-east'\n    Return service offer regions with a given service offer ID and status and region\n  - region eq 'us-east'\n    Return service offer regions with a given region\n  - status eq 'ONBOARDED'\n    Return service offer regions with a given status\n  - serviceOfferId eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050'\n    Return service offer regions with a given service offer ID\n  - serviceOfferId eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050' and region eq 'us-east'\n    Return service offer regions with a given service offer ID and region\n  - serviceOfferId eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050' and status eq 'ONBOARDED'\n    Return service offer regions with a given service offer ID and status\n\n**Filter Syntax**: Use OData-style filters with the field names shown in the examples above. String values must be enclosed in single quotes.",
                    "required": False,
                    "location": "query",
                    "schema": {
                        "type": "string",
                        "description": "The `filter` query parameter is used to filter the set of resources returned in a `GET` request. The returned set of resources must match the criteria in the filter query parameter.<br><br> The value of the `filter` query parameter is a subset of [OData 4.0](https://www.odata.org/documentation/) filter expressions consisting of simple comparison operations joined by logical operators.<br><br>**Supported fields**: `serviceOfferId`, `status`, and `region`.<br>**Supported operand**: `eq`<br>**Supported operations**: `and`\n\nExamples:\n  - serviceOfferId eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050' and status eq 'ONBOARDED' and region eq 'us-east'\n    Return service offer regions with a given service offer ID and status and region\n  - region eq 'us-east'\n    Return service offer regions with a given region\n  - status eq 'ONBOARDED'\n    Return service offer regions with a given status\n  - serviceOfferId eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050'\n    Return service offer regions with a given service offer ID\n  - serviceOfferId eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050' and region eq 'us-east'\n    Return service offer regions with a given service offer ID and region\n  - serviceOfferId eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050' and status eq 'ONBOARDED'\n    Return service offer regions with a given service offer ID and status\n\n**Filter Syntax**: Use OData-style filters with the field names shown in the examples above. String values must be enclosed in single quotes.",
                    },
                },
            ],
            "security": [],
            "responses": {"200": {"description": "Successful response", "content_type": "application/json"}},
        },
        "GET:/service-catalog/v1beta1/service-provisions": {
            "path": "/service-catalog/v1beta1/service-provisions",
            "method": "GET",
            "summary": "getserviceprovisions",
            "description": "getserviceprovisions",
            "operationId": "getserviceprovisions",
            "tags": [],
            "deprecated": False,
            "parameters": [
                {
                    "name": "Hpe-workspace-id",
                    "type": "str",
                    "description": 'The workspace ID. Required if the "view all" parameter is false.',
                    "required": False,
                    "location": "query",
                    "default": "Id",
                    "schema": {
                        "type": "string",
                        "description": 'The workspace ID. Required if the "view all" parameter is false.',
                        "default": "Id",
                    },
                },
                {
                    "name": "next",
                    "type": "str",
                    "description": "Specify the start ID for the next page of service offers.",
                    "required": False,
                    "location": "query",
                    "schema": {
                        "type": "string",
                        "description": "Specify the start ID for the next page of service offers.",
                    },
                },
                {
                    "name": "limit",
                    "type": "int",
                    "description": "Specify the number of results to be returned.",
                    "required": False,
                    "location": "query",
                    "default": 2000,
                    "schema": {
                        "type": "integer",
                        "description": "Specify the number of results to be returned.",
                        "default": "2000",
                    },
                },
                {
                    "name": "filter",
                    "type": "str",
                    "description": "Limit the entities operated on by this endpoint by returning only the subset of entities that match the filter. The filter grammar is a subset of OData 4.0. <br> **Supported Fields:** `id`, `ServiceOfferId`, `workspaceId`, `serviceManagerProvisionId`, `serviceManagerId`, `serviceManagerInstanceId`, `status`, `organizationId`, `slug`. <br> **Supported operand:** `eq` <br> **Supported operations:** `and`\n\nExamples:\n  - serviceManagerId eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050' and serviceManagerInstanceId eq '62d242c7-7d53-448d-b7d0-baf0c591f024'\n    Return service provision for a given application ID and application instance ID.\n  - status eq 'PROVISION_INITIATED'\n    Return service provisions with a given status.\n  - organizationId eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050'\n    Return service provisions with a given organization ID.\n  - slug eq 'AC'\n    Return service provisions with a given slug.\n  - id eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050'\n    Return the service provision with a given ID.\n  - workspaceId eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050'\n    Return service provisions for a given workspace ID.\n  - serviceManagerProvisionId eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050'\n    Return service provisions for a given Application Customer ID.\n  - ServiceOfferId eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050' and region eq 'us-west'\n    Return service provisions for a given service offer ID and region.\n\n**Filter Syntax**: Use OData-style filters with the field names shown in the examples above. String values must be enclosed in single quotes.",
                    "required": False,
                    "location": "query",
                    "schema": {
                        "type": "string",
                        "description": "Limit the entities operated on by this endpoint by returning only the subset of entities that match the filter. The filter grammar is a subset of OData 4.0. <br> **Supported Fields:** `id`, `ServiceOfferId`, `workspaceId`, `serviceManagerProvisionId`, `serviceManagerId`, `serviceManagerInstanceId`, `status`, `organizationId`, `slug`. <br> **Supported operand:** `eq` <br> **Supported operations:** `and`\n\nExamples:\n  - serviceManagerId eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050' and serviceManagerInstanceId eq '62d242c7-7d53-448d-b7d0-baf0c591f024'\n    Return service provision for a given application ID and application instance ID.\n  - status eq 'PROVISION_INITIATED'\n    Return service provisions with a given status.\n  - organizationId eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050'\n    Return service provisions with a given organization ID.\n  - slug eq 'AC'\n    Return service provisions with a given slug.\n  - id eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050'\n    Return the service provision with a given ID.\n  - workspaceId eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050'\n    Return service provisions for a given workspace ID.\n  - serviceManagerProvisionId eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050'\n    Return service provisions for a given Application Customer ID.\n  - ServiceOfferId eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050' and region eq 'us-west'\n    Return service provisions for a given service offer ID and region.\n\n**Filter Syntax**: Use OData-style filters with the field names shown in the examples above. String values must be enclosed in single quotes.",
                    },
                },
                {
                    "name": "unredacted",
                    "type": "bool",
                    "description": "If true, returns the complete entry including sensitive fields.\n\nExample: true",
                    "required": False,
                    "location": "query",
                    "schema": {
                        "type": "boolean",
                        "description": "If true, returns the complete entry including sensitive fields.\n\nExample: true",
                    },
                },
                {
                    "name": "all",
                    "type": "bool",
                    "description": "If true, returns unredacted entries for all workspaces, including all provisioned service offers and their sensitive fields.\n\nExample: true",
                    "required": False,
                    "location": "query",
                    "schema": {
                        "type": "boolean",
                        "description": "If true, returns unredacted entries for all workspaces, including all provisioned service offers and their sensitive fields.\n\nExample: true",
                    },
                },
            ],
            "security": [],
            "responses": {"200": {"description": "Successful response", "content_type": "application/json"}},
        },
        "GET:/service-catalog/v1beta1/service-offers": {
            "path": "/service-catalog/v1beta1/service-offers",
            "method": "GET",
            "summary": "getserviceoffers",
            "description": "getserviceoffers",
            "operationId": "getserviceoffers",
            "tags": [],
            "deprecated": False,
            "parameters": [
                {
                    "name": "next",
                    "type": "str",
                    "description": "Specifies the pagination cursor for the next page of service offers.\n\nExample: 64136af7-cd64-4b4e-88a8-150ab51a920d",
                    "required": False,
                    "location": "query",
                    "schema": {
                        "type": "string",
                        "description": "Specifies the pagination cursor for the next page of service offers.\n\nExample: 64136af7-cd64-4b4e-88a8-150ab51a920d",
                    },
                },
                {
                    "name": "limit",
                    "type": "int",
                    "description": "Specifies the number of results to be returned.",
                    "required": False,
                    "location": "query",
                    "default": 2000,
                    "schema": {
                        "type": "integer",
                        "description": "Specifies the number of results to be returned.",
                        "default": "2000",
                    },
                },
                {
                    "name": "filter",
                    "type": "str",
                    "description": "The `filter` query parameter is used to filter the set of resources returned in a `GET` request. The returned set of resources must match the criteria in the filter query parameter.<br><br> The value of the `filter` query parameter is a subset of [OData 4.0](https://www.odata.org/documentation/) filter expressions consisting of simple comparison operations joined by logical operators.<br><br>**Supported fields**: `category`, `serviceManagerId`, `status`, `isDefault`, `slug`, and `staticLaunchUrl`.<br>**Supported operand**: `eq`<br>**Supported operations**: `and`\n\nExamples:\n  - slug eq 'GLP'\n    Return service offers with a given slug\n  - staticLaunchUrl eq '/Organization'\n    Return service offers for a given static launch URL\n  - status eq 'ONBOARDED'\n    Return service offers with a given status\n  - category eq 'COMPUTE'\n    Return service offers for a given category\n  - isDefault eq true\n    Return service offers that are service managers\n  - serviceManagerId eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050'\n    Return service offers for given service manager ID\n\n**Filter Syntax**: Use OData-style filters with the field names shown in the examples above. String values must be enclosed in single quotes.",
                    "required": False,
                    "location": "query",
                    "schema": {
                        "type": "string",
                        "description": "The `filter` query parameter is used to filter the set of resources returned in a `GET` request. The returned set of resources must match the criteria in the filter query parameter.<br><br> The value of the `filter` query parameter is a subset of [OData 4.0](https://www.odata.org/documentation/) filter expressions consisting of simple comparison operations joined by logical operators.<br><br>**Supported fields**: `category`, `serviceManagerId`, `status`, `isDefault`, `slug`, and `staticLaunchUrl`.<br>**Supported operand**: `eq`<br>**Supported operations**: `and`\n\nExamples:\n  - slug eq 'GLP'\n    Return service offers with a given slug\n  - staticLaunchUrl eq '/Organization'\n    Return service offers for a given static launch URL\n  - status eq 'ONBOARDED'\n    Return service offers with a given status\n  - category eq 'COMPUTE'\n    Return service offers for a given category\n  - isDefault eq true\n    Return service offers that are service managers\n  - serviceManagerId eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050'\n    Return service offers for given service manager ID\n\n**Filter Syntax**: Use OData-style filters with the field names shown in the examples above. String values must be enclosed in single quotes.",
                    },
                },
            ],
            "security": [],
            "responses": {"200": {"description": "Successful response", "content_type": "application/json"}},
        },
        "GET:/service-catalog/v1beta1/service-offer-regions/{id}": {
            "path": "/service-catalog/v1beta1/service-offer-regions/{id}",
            "method": "GET",
            "summary": "getserviceofferregion",
            "description": "getserviceofferregion",
            "operationId": "getserviceofferregion",
            "tags": [],
            "deprecated": False,
            "parameters": [
                {
                    "name": "id",
                    "type": "str",
                    "description": "The unique service offer region ID.\n\nExample: 3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "required": True,
                    "location": "query",
                    "schema": {
                        "type": "string",
                        "description": "The unique service offer region ID.\n\nExample: 3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    },
                },
            ],
            "security": [],
            "responses": {"200": {"description": "Successful response", "content_type": "application/json"}},
        },
        "GET:/service-catalog/v1/per-region-service-managers/{id}": {
            "path": "/service-catalog/v1/per-region-service-managers/{id}",
            "method": "GET",
            "summary": "service_managers_for_a_region_v1",
            "description": "service_managers_for_a_region_v1",
            "operationId": "service_managers_for_a_region_v1",
            "tags": [],
            "deprecated": False,
            "parameters": [
                {
                    "name": "id",
                    "type": "str",
                    "description": "HPE GreenLake platform defined region code.\n\nExamples:\n  - us-west\n  - us-east",
                    "required": True,
                    "location": "query",
                    "schema": {
                        "type": "string",
                        "description": "HPE GreenLake platform defined region code.\n\nExamples:\n  - us-west\n  - us-east",
                    },
                },
            ],
            "security": [],
            "responses": {"200": {"description": "Successful response", "content_type": "application/json"}},
        },
        "GET:/service-catalog/v1/service-manager-provisions": {
            "path": "/service-catalog/v1/service-manager-provisions",
            "method": "GET",
            "summary": "get_service_manager_provisions_v1",
            "description": "get_service_manager_provisions_v1",
            "operationId": "get_service_manager_provisions_v1",
            "tags": [],
            "deprecated": False,
            "parameters": [
                {
                    "name": "offset",
                    "type": "int",
                    "description": "Zero-based resource offset to start the response from.\n\nExample: 0",
                    "required": False,
                    "location": "query",
                    "schema": {
                        "type": "integer",
                        "description": "Zero-based resource offset to start the response from.\n\nExample: 0",
                    },
                },
                {
                    "name": "limit",
                    "type": "int",
                    "description": "The maximum number of records to return.\n\nExample: 10",
                    "required": False,
                    "location": "query",
                    "default": 2000,
                    "schema": {
                        "type": "integer",
                        "description": "The maximum number of records to return.\n\nExample: 10",
                        "default": "2000",
                    },
                },
                {
                    "name": "filter",
                    "type": "str",
                    "description": "Examples:\n  - status eq 'PROVISIONED'\n    Returns service managers that are provisioned.\n  - status eq 'UNPROVISIONED'\n    Returns service managers that are not provisioned.\n  - region eq 'us-west'\n    Returns service managers in a specified region.\n  - serviceManagerId eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050'\n    Returns service managers with a specific service manager ID.\n\n**Filter Syntax**: Use OData-style filters with the field names shown in the examples above. String values must be enclosed in single quotes.",
                    "required": False,
                    "location": "query",
                    "schema": {
                        "type": "string",
                        "description": "Examples:\n  - status eq 'PROVISIONED'\n    Returns service managers that are provisioned.\n  - status eq 'UNPROVISIONED'\n    Returns service managers that are not provisioned.\n  - region eq 'us-west'\n    Returns service managers in a specified region.\n  - serviceManagerId eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050'\n    Returns service managers with a specific service manager ID.\n\n**Filter Syntax**: Use OData-style filters with the field names shown in the examples above. String values must be enclosed in single quotes.",
                    },
                },
            ],
            "security": [],
            "responses": {"200": {"description": "Successful response", "content_type": "application/json"}},
        },
        "GET:/service-catalog/v1/service-managers": {
            "path": "/service-catalog/v1/service-managers",
            "method": "GET",
            "summary": "get_service_managers_v1",
            "description": "get_service_managers_v1",
            "operationId": "get_service_managers_v1",
            "tags": [],
            "deprecated": False,
            "parameters": [
                {
                    "name": "offset",
                    "type": "int",
                    "description": "Specify pagination offset\n\nExample: 0",
                    "required": False,
                    "location": "query",
                    "schema": {"type": "integer", "description": "Specify pagination offset\n\nExample: 0"},
                },
                {
                    "name": "limit",
                    "type": "int",
                    "description": "The maximum number of records to return.\n\nExample: 10",
                    "required": False,
                    "location": "query",
                    "default": 2000,
                    "schema": {
                        "type": "integer",
                        "description": "The maximum number of records to return.\n\nExample: 10",
                        "default": "2000",
                    },
                },
            ],
            "security": [],
            "responses": {"200": {"description": "Successful response", "content_type": "application/json"}},
        },
        "GET:/service-catalog/v1/service-manager-provisions/{id}": {
            "path": "/service-catalog/v1/service-manager-provisions/{id}",
            "method": "GET",
            "summary": "get_service_manager_provision_v1",
            "description": "get_service_manager_provision_v1",
            "operationId": "get_service_manager_provision_v1",
            "tags": [],
            "deprecated": False,
            "parameters": [
                {
                    "name": "id",
                    "type": "str",
                    "description": "Service manager provision ID",
                    "required": True,
                    "location": "query",
                    "schema": {"type": "string", "description": "Service manager provision ID"},
                },
            ],
            "security": [],
            "responses": {"200": {"description": "Successful response", "content_type": "application/json"}},
        },
        "GET:/service-catalog/v1/per-region-service-managers": {
            "path": "/service-catalog/v1/per-region-service-managers",
            "method": "GET",
            "summary": "per_region_service_managers_v1",
            "description": "per_region_service_managers_v1",
            "operationId": "per_region_service_managers_v1",
            "tags": [],
            "deprecated": False,
            "parameters": [
                {
                    "name": "offset",
                    "type": "int",
                    "description": "Zero-based resource offset to start the response from.\n\nExample: 0",
                    "required": False,
                    "location": "query",
                    "schema": {
                        "type": "integer",
                        "description": "Zero-based resource offset to start the response from.\n\nExample: 0",
                    },
                },
                {
                    "name": "limit",
                    "type": "int",
                    "description": "The maximum number of records to return.\n\nExample: 10",
                    "required": False,
                    "location": "query",
                    "default": 2000,
                    "schema": {
                        "type": "integer",
                        "description": "The maximum number of records to return.\n\nExample: 10",
                        "default": "2000",
                    },
                },
                {
                    "name": "filter",
                    "type": "str",
                    "description": "Limit the resources operated on by an endpoint and return only the subset of resources that match the filter using an [OData V4](https://www.odata.org/documentation/) formatted filter string. Service manager by region can be filtered by `mspsupported` See examples of filtering options.\n\nExamples:\n  - mspSupported eq false\n    Return service managers when msp supported equals false\n  - mspSupported eq true\n    Return service managers when msp supported equals true\n\n**Filter Syntax**: Use OData-style filters with the field names shown in the examples above. String values must be enclosed in single quotes.",
                    "required": False,
                    "location": "query",
                    "schema": {
                        "type": "string",
                        "description": "Limit the resources operated on by an endpoint and return only the subset of resources that match the filter using an [OData V4](https://www.odata.org/documentation/) formatted filter string. Service manager by region can be filtered by `mspsupported` See examples of filtering options.\n\nExamples:\n  - mspSupported eq false\n    Return service managers when msp supported equals false\n  - mspSupported eq true\n    Return service managers when msp supported equals true\n\n**Filter Syntax**: Use OData-style filters with the field names shown in the examples above. String values must be enclosed in single quotes.",
                    },
                },
            ],
            "security": [],
            "responses": {"200": {"description": "Successful response", "content_type": "application/json"}},
        },
        "GET:/service-catalog/v1beta1/service-provisions/{id}": {
            "path": "/service-catalog/v1beta1/service-provisions/{id}",
            "method": "GET",
            "summary": "getserviceprovision",
            "description": "getserviceprovision",
            "operationId": "getserviceprovision",
            "tags": [],
            "deprecated": False,
            "parameters": [
                {
                    "name": "id",
                    "type": "str",
                    "description": "The unique identifier of a service provision. The ID is returned by the `Get service provisions` endpoint.",
                    "required": True,
                    "location": "query",
                    "schema": {
                        "type": "string",
                        "description": "The unique identifier of a service provision. The ID is returned by the `Get service provisions` endpoint.",
                    },
                },
                {
                    "name": "unredacted",
                    "type": "bool",
                    "description": "If set to true, get the entire entry along with sensitive fields.\n\nExample: true",
                    "required": False,
                    "location": "query",
                    "schema": {
                        "type": "boolean",
                        "description": "If set to true, get the entire entry along with sensitive fields.\n\nExample: true",
                    },
                },
            ],
            "security": [],
            "responses": {"200": {"description": "Successful response", "content_type": "application/json"}},
        },
        "GET:/service-catalog/v1beta1/service-offers/{id}": {
            "path": "/service-catalog/v1beta1/service-offers/{id}",
            "method": "GET",
            "summary": "getserviceoffer",
            "description": "getserviceoffer",
            "operationId": "getserviceoffer",
            "tags": [],
            "deprecated": False,
            "parameters": [
                {
                    "name": "id",
                    "type": "str",
                    "description": "The unique identifier of the service offer.\n\nExample: 3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "required": True,
                    "location": "query",
                    "schema": {
                        "type": "string",
                        "description": "The unique identifier of the service offer.\n\nExample: 3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    },
                },
            ],
            "security": [],
            "responses": {"200": {"description": "Successful response", "content_type": "application/json"}},
        },
        "GET:/service-catalog/v1/service-managers/{id}": {
            "path": "/service-catalog/v1/service-managers/{id}",
            "method": "GET",
            "summary": "get_service_manager_v1",
            "description": "get_service_manager_v1",
            "operationId": "get_service_manager_v1",
            "tags": [],
            "deprecated": False,
            "parameters": [
                {
                    "name": "id",
                    "type": "str",
                    "description": "Service manager ID",
                    "required": True,
                    "location": "query",
                    "schema": {"type": "string", "description": "Service manager ID"},
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
