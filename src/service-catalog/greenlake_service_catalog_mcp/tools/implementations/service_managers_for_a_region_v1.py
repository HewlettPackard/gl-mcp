# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
service_managers_for_a_region_v1 tool for service-catalog MCP server.

Implements: GET /service-catalog/v1/per-region-service-managers/{id}
"""

from __future__ import annotations
from typing import Annotated, Any
from urllib.parse import quote

from mcp.server.fastmcp import Context
from pydantic import Field

from greenlake_service_catalog_mcp.config.logging import get_logger
from greenlake_service_catalog_mcp.server.fastmcp_instance import mcp

logger = get_logger(__name__)


@mcp.tool(
    name="service_managers_for_a_region_v1",
    description="Retrieve a list of service managers deployed to a particular region.",
)
async def service_managers_for_a_region_v1(  # noqa: E501
    ctx: Context,
    id: Annotated[
        str,
        Field(description="HPE GreenLake platform defined region code.\n\nExamples:\n  - us-west\n  - us-east"),
    ] = ...,
) -> list[dict[str, Any]]:
    """Retrieve a list of service managers deployed to a particular region.

    Args:
        id: HPE GreenLake platform defined region code.\n\nExamples:\n  - us-west\n  - us-east
    Returns:
        API response data as a list containing one result dict.
    """
    http_client = ctx.request_context.lifespan_context.http_client

    # Build URL – URL-encode path parameters to prevent path-traversal attacks
    url = "/service-catalog/v1/per-region-service-managers/{id}"
    url = url.replace("{" + "id" + "}", quote(str(id), safe=""))

    # Collect query / body parameters; skip values that were not provided
    params: dict[str, Any] = {}

    try:
        response_data = await http_client.get(url, params=params)
        return [{"success": True, "result": response_data}]

    except ValueError as exc:
        logger.error(f"Validation error in service_managers_for_a_region_v1: {exc}")
        return [{"success": False, "error": "validation_error", "message": str(exc)}]

    except Exception as exc:
        logger.error(f"Error in service_managers_for_a_region_v1: {exc}", exc_info=True)
        return [{"success": False, "error": "request_failed", "message": str(exc)}]
