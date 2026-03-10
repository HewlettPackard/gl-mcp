# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
getdatasources tool for Sustainability_Insight_Center MCP server.

Implements: GET /sustainability-insight-ctr/v1beta1/datasources
"""

from __future__ import annotations

from typing import Annotated, Any

from mcp.server.fastmcp import Context
from pydantic import Field

from config.logging import get_logger
from server.fastmcp_instance import mcp

logger = get_logger(__name__)


@mcp.tool(
    name="getdatasources",
    description="This returns information such as name and data collection times for each SIC data source.",
)
async def getdatasources(  # noqa: E501
    ctx: Context,
) -> list[dict[str, Any]]:
    """This returns information such as name and data collection times for each SIC data source.

    Returns:
        API response data as a list containing one result dict.
    """
    http_client = ctx.request_context.lifespan_context.http_client

    # Build URL – URL-encode path parameters to prevent path-traversal attacks
    url = "/sustainability-insight-ctr/v1beta1/datasources"

    # Collect query / body parameters; skip values that were not provided
    params: dict[str, Any] = {}

    try:
        response_data = await http_client.get(url, params=params)
        return [{"success": True, "result": response_data}]

    except ValueError as exc:
        logger.error(f"Validation error in getdatasources: {exc}")
        return [{"success": False, "error": "validation_error", "message": str(exc)}]

    except Exception as exc:
        logger.error(f"Error in getdatasources: {exc}", exc_info=True)
        return [{"success": False, "error": "request_failed", "message": str(exc)}]
