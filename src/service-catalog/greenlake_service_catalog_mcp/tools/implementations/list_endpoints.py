# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
list_endpoints tool implementation for service-catalog MCP server.

This tool provides fast discovery of all available API endpoints as a simple list of endpoint identifiers.
Generated for dynamic mode when OpenAPI spec has 12 endpoints (>= 50 threshold).
"""

from __future__ import annotations

import json
from typing import Annotated

from pydantic import Field

from greenlake_service_catalog_mcp.config.logging import get_logger
from greenlake_service_catalog_mcp.server.fastmcp_instance import mcp

logger = get_logger(__name__)


@mcp.tool(
    name="list_endpoints",
    description="Lists all available service-catalog API endpoints with metadata (method:path, operation name, type) for fast discovery and selection. Each endpoint includes a 'type' field: 'list' for collection endpoints, 'detail' for single-resource endpoints that require path parameters.",
)
async def list_endpoints(
    filter: Annotated[  # noqa: A002
        str | None,
        Field(
            description="Optional filter to search for specific endpoints (case-insensitive substring match)",
            default=None,
        ),
    ] = None,
) -> str:
    """Lists all available service-catalog API endpoints with metadata for fast discovery.

    Returns a JSON-encoded array of endpoint objects with 'endpoint' (METHOD:PATH),
    'summary' (operation name), and 'type' ('list' for collection endpoints,
    'detail' for single-resource endpoints requiring path parameters).

    Args:
        filter: Optional case-insensitive substring filter applied to endpoint identifiers and summaries.

    Returns:
        JSON string containing a sorted list of endpoint objects.
    """
    filter_term = (filter or "").lower()

    all_endpoints: list[dict[str, str]] = [
        {
            "endpoint": "GET:/service-catalog/v1beta1/service-offer-regions",
            "summary": "getserviceofferregions",
            "type": "list",
        },
        {
            "endpoint": "GET:/service-catalog/v1beta1/service-provisions",
            "summary": "getserviceprovisions",
            "type": "list",
        },
        {"endpoint": "GET:/service-catalog/v1beta1/service-offers", "summary": "getserviceoffers", "type": "list"},
        {
            "endpoint": "GET:/service-catalog/v1beta1/service-offer-regions/{id}",
            "summary": "getserviceofferregion",
            "type": "detail",
        },
        {
            "endpoint": "GET:/service-catalog/v1/per-region-service-managers/{id}",
            "summary": "service_managers_for_a_region_v1",
            "type": "detail",
        },
        {
            "endpoint": "GET:/service-catalog/v1/service-manager-provisions",
            "summary": "get_service_manager_provisions_v1",
            "type": "list",
        },
        {"endpoint": "GET:/service-catalog/v1/service-managers", "summary": "get_service_managers_v1", "type": "list"},
        {
            "endpoint": "GET:/service-catalog/v1/service-manager-provisions/{id}",
            "summary": "get_service_manager_provision_v1",
            "type": "detail",
        },
        {
            "endpoint": "GET:/service-catalog/v1/per-region-service-managers",
            "summary": "per_region_service_managers_v1",
            "type": "list",
        },
        {
            "endpoint": "GET:/service-catalog/v1beta1/service-provisions/{id}",
            "summary": "getserviceprovision",
            "type": "detail",
        },
        {
            "endpoint": "GET:/service-catalog/v1beta1/service-offers/{id}",
            "summary": "getserviceoffer",
            "type": "detail",
        },
        {
            "endpoint": "GET:/service-catalog/v1/service-managers/{id}",
            "summary": "get_service_manager_v1",
            "type": "detail",
        },
    ]

    if filter_term:
        filtered = [
            ep
            for ep in all_endpoints
            if filter_term in ep["endpoint"].lower() or filter_term in ep.get("summary", "").lower()
        ]
    else:
        filtered = all_endpoints

    filtered.sort(key=lambda ep: ep["endpoint"])
    return json.dumps(filtered)
