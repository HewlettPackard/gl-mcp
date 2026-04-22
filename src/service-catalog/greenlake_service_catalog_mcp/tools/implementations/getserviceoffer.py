# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
getserviceoffer tool for service-catalog MCP server.

Implements: GET /service-catalog/v1beta1/service-offers/{id}
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
    name="getserviceoffer",
    description="Retrieve detailed information about a specific service offer by supplying its unique identifier in the request path.\nTo obtain valid service offer IDs, use the `Get service offers` endpoint to list available offers.\n",
)
async def getserviceoffer(  # noqa: E501
    ctx: Context,
    id: Annotated[
        str,
        Field(
            description="The unique identifier of the service offer.\n\nExample: 3fa85f64-5717-4562-b3fc-2c963f66afa6"
        ),
    ] = ...,
) -> list[dict[str, Any]]:
    """Retrieve detailed information about a specific service offer by supplying its unique identifier in the request path.\nTo obtain valid service offer IDs, use the `Get service offers` endpoint to list available offers.\n

    Args:
        id: The unique identifier of the service offer.\n\nExample: 3fa85f64-5717-4562-b3fc-2c963f66afa6
    Returns:
        API response data as a list containing one result dict.
    """
    http_client = ctx.request_context.lifespan_context.http_client

    # Build URL – URL-encode path parameters to prevent path-traversal attacks
    url = "/service-catalog/v1beta1/service-offers/{id}"
    url = url.replace("{" + "id" + "}", quote(str(id), safe=""))

    # Collect query / body parameters; skip values that were not provided
    params: dict[str, Any] = {}

    try:
        response_data = await http_client.get(url, params=params)
        return [{"success": True, "result": response_data}]

    except ValueError as exc:
        logger.error(f"Validation error in getserviceoffer: {exc}")
        return [{"success": False, "error": "validation_error", "message": str(exc)}]

    except Exception as exc:
        logger.error(f"Error in getserviceoffer: {exc}", exc_info=True)
        return [{"success": False, "error": "request_failed", "message": str(exc)}]
