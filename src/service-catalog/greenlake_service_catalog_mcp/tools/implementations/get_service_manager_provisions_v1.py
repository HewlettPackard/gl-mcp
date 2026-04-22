# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
get_service_manager_provisions_v1 tool for service-catalog MCP server.

Implements: GET /service-catalog/v1/service-manager-provisions
"""

from __future__ import annotations
from typing import Annotated, Any

from mcp.server.fastmcp import Context
from pydantic import Field

from greenlake_service_catalog_mcp.config.logging import get_logger
from greenlake_service_catalog_mcp.server.fastmcp_instance import mcp

logger = get_logger(__name__)


@mcp.tool(
    name="get_service_manager_provisions_v1",
    description="Retrieve a list of all service manager provision entries.",
)
async def get_service_manager_provisions_v1(  # noqa: E501
    ctx: Context,
    offset: Annotated[
        int | str | None,
        Field(description="Zero-based resource offset to start the response from.\n\nExample: 0"),
    ] = None,
    limit: Annotated[
        int | str | None,
        Field(description="The maximum number of records to return.\n\nExample: 10", default=2000),
    ] = 2000,
    filter: Annotated[
        str | None,
        Field(
            description="Examples:\n  - status eq 'PROVISIONED'\n    Returns service managers that are provisioned.\n  - status eq 'UNPROVISIONED'\n    Returns service managers that are not provisioned.\n  - region eq 'us-west'\n    Returns service managers in a specified region.\n  - serviceManagerId eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050'\n    Returns service managers with a specific service manager ID.\n\n**Filter Syntax**: Use OData-style filters with the field names shown in the examples above. String values must be enclosed in single quotes."
        ),
    ] = None,
) -> list[dict[str, Any]]:
    """Retrieve a list of all service manager provision entries.

    Args:
        offset: Zero-based resource offset to start the response from.\n\nExample: 0
        limit: The maximum number of records to return.\n\nExample: 10
        filter: Examples:\n  - status eq 'PROVISIONED'\n    Returns service managers that are provisioned.\n  - status eq 'UNPROVISIONED'\n    Returns service managers that are not provisioned.\n  - region eq 'us-west'\n    Returns service managers in a specified region.\n  - serviceManagerId eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050'\n    Returns service managers with a specific service manager ID.\n\n**Filter Syntax**: Use OData-style filters with the field names shown in the examples above. String values must be enclosed in single quotes.
    Returns:
        API response data as a list containing one result dict.
    """
    http_client = ctx.request_context.lifespan_context.http_client

    # Build URL – URL-encode path parameters to prevent path-traversal attacks
    url = "/service-catalog/v1/service-manager-provisions"

    # Collect query / body parameters; skip values that were not provided
    params: dict[str, Any] = {}
    if offset is not None and offset is not ...:
        # Coerce string supplied by LLM clients to int
        try:
            params["offset"] = int(offset)
        except (ValueError, TypeError) as exc:
            raise ValueError("'offset' must be an integer") from exc
    if limit is not None and limit is not ...:
        # Coerce string supplied by LLM clients to int
        try:
            params["limit"] = int(limit)
        except (ValueError, TypeError) as exc:
            raise ValueError("'limit' must be an integer") from exc
    if filter is not None and filter is not ...:
        params["filter"] = filter

    try:
        response_data = await http_client.get(url, params=params)
        return [{"success": True, "result": response_data}]

    except ValueError as exc:
        logger.error(f"Validation error in get_service_manager_provisions_v1: {exc}")
        return [{"success": False, "error": "validation_error", "message": str(exc)}]

    except Exception as exc:
        logger.error(f"Error in get_service_manager_provisions_v1: {exc}", exc_info=True)
        return [{"success": False, "error": "request_failed", "message": str(exc)}]
