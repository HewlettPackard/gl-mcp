# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
getdatasource tool for Sustainability_Insight_Center MCP server.

Implements: GET /sustainability-insight-ctr/v1beta1/datasources/{id}
"""

from __future__ import annotations

from typing import Annotated, Any
from urllib.parse import quote

from mcp.server.fastmcp import Context
from pydantic import Field

from config.logging import get_logger
from server.fastmcp_instance import mcp

logger = get_logger(__name__)


@mcp.tool(
    name="getdatasource",
    description="Get information such as name and data collection times for a SIC data source.",
)
async def getdatasource(  # noqa: E501
    ctx: Context,
    id: Annotated[
        str,
        Field(description="ID of the data source\n\nExample: 00000000-0000-0000-0000-0000000000000"),
    ] = ...,
) -> list[dict[str, Any]]:
    """Get information such as name and data collection times for a SIC data source.

    Args:
        id: ID of the data source\n\nExample: 00000000-0000-0000-0000-0000000000000
    Returns:
        API response data as a list containing one result dict.
    """
    http_client = ctx.request_context.lifespan_context.http_client

    # Build URL – URL-encode path parameters to prevent path-traversal attacks
    url = "/sustainability-insight-ctr/v1beta1/datasources/{id}"
    url = url.replace("{" + "id" + "}", quote(str(id), safe=""))

    # Collect query / body parameters; skip values that were not provided
    params: dict[str, Any] = {}

    try:
        response_data = await http_client.get(url, params=params)
        return [{"success": True, "result": response_data}]

    except ValueError as exc:
        logger.error(f"Validation error in getdatasource: {exc}")
        return [{"success": False, "error": "validation_error", "message": str(exc)}]

    except Exception as exc:
        logger.error(f"Error in getdatasource: {exc}", exc_info=True)
        return [{"success": False, "error": "request_failed", "message": str(exc)}]
