# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
getdevicebyidv1 tool for devices MCP server.

Implements: GET /devices/v1/devices/{id}
"""

from __future__ import annotations
from typing import Annotated, Any
from urllib.parse import quote

from mcp.server.fastmcp import Context
from pydantic import Field

from greenlake_devices_mcp.config.logging import get_logger
from greenlake_devices_mcp.server.fastmcp_instance import mcp

logger = get_logger(__name__)


@mcp.tool(
    name="getdevicebyidv1",
    description="Get details on a specific device by passing its resourceId. <p><b>NOTE</b>: You need  view permissions for device management to invoke this API.</p> Rate limits are enforced on this API. 40 requests per minute is supported per workspace. The API returns `429` if this threshold is breached.",
)
async def getdevicebyidv1(  # noqa: E501
    ctx: Context,
    id: Annotated[
        str,
        Field(description="id parameter"),
    ] = ...,
) -> list[dict[str, Any]]:
    """Get details on a specific device by passing its resourceId. <p><b>NOTE</b>: You need  view permissions for device management to invoke this API.</p> Rate limits are enforced on this API. 40 requests per minute is supported per workspace. The API returns `429` if this threshold is breached.

    Args:
        id: id parameter
    Returns:
        API response data as a list containing one result dict.
    """
    http_client = ctx.request_context.lifespan_context.http_client

    # Build URL – URL-encode path parameters to prevent path-traversal attacks
    url = "/devices/v1/devices/{id}"
    url = url.replace("{" + "id" + "}", quote(str(id), safe=""))

    # Collect query / body parameters; skip values that were not provided
    params: dict[str, Any] = {}

    try:
        response_data = await http_client.get(url, params=params)
        return [{"success": True, "result": response_data}]

    except ValueError as exc:
        logger.error(f"Validation error in getdevicebyidv1: {exc}")
        return [{"success": False, "error": "validation_error", "message": str(exc)}]

    except Exception as exc:
        logger.error(f"Error in getdevicebyidv1: {exc}", exc_info=True)
        return [{"success": False, "error": "request_failed", "message": str(exc)}]
