# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
getsubscriptiondetailsbyidv1 tool for subscriptions MCP server.

Implements: GET /subscriptions/v1/subscriptions/{id}
"""

from __future__ import annotations
from typing import Annotated, Any
from urllib.parse import quote

from mcp.server.fastmcp import Context
from pydantic import Field

from greenlake_subscriptions_mcp.config.logging import get_logger
from greenlake_subscriptions_mcp.server.fastmcp_instance import mcp

logger = get_logger(__name__)


@mcp.tool(
    name="getsubscriptiondetailsbyidv1",
    description="Get detailed information for a single subscription by `id`. <br><br>**NOTE:** You need to have the view permission of device management to invoke this API. <br><br> Rate limits are enforced on this API. 20 requests per minute is supported per workspace. The API returns `429` if this threshold is breached.",
)
async def getsubscriptiondetailsbyidv1(  # noqa: E501
    ctx: Context,
    id: Annotated[
        str,
        Field(description="The unique identifier of the subscription."),
    ] = ...,
) -> list[dict[str, Any]]:
    """Get detailed information for a single subscription by `id`. <br><br>**NOTE:** You need to have the view permission of device management to invoke this API. <br><br> Rate limits are enforced on this API. 20 requests per minute is supported per workspace. The API returns `429` if this threshold is breached.

    Args:
        id: The unique identifier of the subscription.
    Returns:
        API response data as a list containing one result dict.
    """
    http_client = ctx.request_context.lifespan_context.http_client

    # Build URL – URL-encode path parameters to prevent path-traversal attacks
    url = "/subscriptions/v1/subscriptions/{id}"
    url = url.replace("{" + "id" + "}", quote(str(id), safe=""))

    # Collect query / body parameters; skip values that were not provided
    params: dict[str, Any] = {}

    try:
        response_data = await http_client.get(url, params=params)
        return [{"success": True, "result": response_data}]

    except ValueError as exc:
        logger.error(f"Validation error in getsubscriptiondetailsbyidv1: {exc}")
        return [{"success": False, "error": "validation_error", "message": str(exc)}]

    except Exception as exc:
        logger.error(f"Error in getsubscriptiondetailsbyidv1: {exc}", exc_info=True)
        return [{"success": False, "error": "request_failed", "message": str(exc)}]
