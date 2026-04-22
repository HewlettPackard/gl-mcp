# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
get_service_manager_provision_v1 tool for service-catalog MCP server.

Implements: GET /service-catalog/v1/service-manager-provisions/{id}
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
    name="get_service_manager_provision_v1",
    description="Retrieve details for a specific service manager provision entry using the ID for the entry.",
)
async def get_service_manager_provision_v1(  # noqa: E501
    ctx: Context,
    id: Annotated[
        str,
        Field(description="Service manager provision ID"),
    ] = ...,
) -> list[dict[str, Any]]:
    """Retrieve details for a specific service manager provision entry using the ID for the entry.

    Args:
        id: Service manager provision ID
    Returns:
        API response data as a list containing one result dict.
    """
    http_client = ctx.request_context.lifespan_context.http_client

    # Build URL – URL-encode path parameters to prevent path-traversal attacks
    url = "/service-catalog/v1/service-manager-provisions/{id}"
    url = url.replace("{" + "id" + "}", quote(str(id), safe=""))

    # Collect query / body parameters; skip values that were not provided
    params: dict[str, Any] = {}

    try:
        response_data = await http_client.get(url, params=params)
        return [{"success": True, "result": response_data}]

    except ValueError as exc:
        logger.error(f"Validation error in get_service_manager_provision_v1: {exc}")
        return [{"success": False, "error": "validation_error", "message": str(exc)}]

    except Exception as exc:
        logger.error(f"Error in get_service_manager_provision_v1: {exc}", exc_info=True)
        return [{"success": False, "error": "request_failed", "message": str(exc)}]
