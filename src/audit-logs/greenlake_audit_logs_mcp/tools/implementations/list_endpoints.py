# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
list_endpoints tool implementation for audit-logs MCP server.

This tool provides fast discovery of all available API endpoints as a simple list of endpoint identifiers.
Generated for dynamic mode when OpenAPI spec has 2 endpoints (>= 50 threshold).
"""

from __future__ import annotations

import json
from typing import Annotated

from pydantic import Field

from greenlake_audit_logs_mcp.config.logging import get_logger
from greenlake_audit_logs_mcp.server.fastmcp_instance import mcp

logger = get_logger(__name__)


@mcp.tool(
    name="list_endpoints",
    description="Lists all available audit-logs API endpoints with metadata (method:path, operation name, type) for fast discovery and selection. Each endpoint includes a 'type' field: 'list' for collection endpoints, 'detail' for single-resource endpoints that require path parameters.",
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
    """Lists all available audit-logs API endpoints with metadata for fast discovery.

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
        {"endpoint": "GET:/audit-log/v1/logs", "summary": "getauditlogs", "type": "list"},
        {"endpoint": "GET:/audit-log/v1/logs/{id}/detail", "summary": "getauditlogdetails", "type": "detail"},
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
