# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
getcoefficient tool for Sustainability_Insight_Center MCP server.

Implements: GET /sustainability-insight-ctr/v1beta1/coefficients/{id}
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
    name="getcoefficient",
    description="Get a single cost and co2 coefficient for an id",
)
async def getcoefficient(  # noqa: E501
    ctx: Context,
    id: Annotated[
        str,
        Field(description="UUID of the coefficient mapping\n\nExample: 00000000-0000-0000-0000-0000000000000"),
    ] = ...,
) -> list[dict[str, Any]]:
    """Get a single cost and co2 coefficient for an id

    Args:
        id: UUID of the coefficient mapping\n\nExample: 00000000-0000-0000-0000-0000000000000
    Returns:
        API response data as a list containing one result dict.
    """
    http_client = ctx.request_context.lifespan_context.http_client

    # Build URL – URL-encode path parameters to prevent path-traversal attacks
    url = "/sustainability-insight-ctr/v1beta1/coefficients/{id}"
    url = url.replace("{" + "id" + "}", quote(str(id), safe=""))

    # Collect query / body parameters; skip values that were not provided
    params: dict[str, Any] = {}

    try:
        response_data = await http_client.get(url, params=params)
        return [{"success": True, "result": response_data}]

    except ValueError as exc:
        logger.error(f"Validation error in getcoefficient: {exc}")
        return [{"success": False, "error": "validation_error", "message": str(exc)}]

    except Exception as exc:
        logger.error(f"Error in getcoefficient: {exc}", exc_info=True)
        return [{"success": False, "error": "request_failed", "message": str(exc)}]
