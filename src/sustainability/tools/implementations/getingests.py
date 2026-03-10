# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
getingests tool for Sustainability_Insight_Center MCP server.

Implements: GET /sustainability-insight-ctr/v1beta1/ingests
"""

from __future__ import annotations

from typing import Annotated, Any

from mcp.server.fastmcp import Context
from pydantic import Field

from config.logging import get_logger
from server.fastmcp_instance import mcp

logger = get_logger(__name__)


@mcp.tool(
    name="getingests",
    description="This returns the associated metadata of each uploaded 3rd party device measurement.",
)
async def getingests(  # noqa: E501
    ctx: Context,
    offset: Annotated[
        int | str | None,
        Field(description="Zero-based resource offset to start the response from.\n\nExample: 10"),
    ] = None,
    limit: Annotated[
        int | str | None,
        Field(description="Number of ingested records to return.\n\nExample: 10", default=10),
    ] = 10,
) -> list[dict[str, Any]]:
    """This returns the associated metadata of each uploaded 3rd party device measurement.

    Args:
        offset: Zero-based resource offset to start the response from.\n\nExample: 10
        limit: Number of ingested records to return.\n\nExample: 10
    Returns:
        API response data as a list containing one result dict.
    """
    http_client = ctx.request_context.lifespan_context.http_client

    # Build URL – URL-encode path parameters to prevent path-traversal attacks
    url = "/sustainability-insight-ctr/v1beta1/ingests"

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

    try:
        response_data = await http_client.get(url, params=params)
        return [{"success": True, "result": response_data}]

    except ValueError as exc:
        logger.error(f"Validation error in getingests: {exc}")
        return [{"success": False, "error": "validation_error", "message": str(exc)}]

    except Exception as exc:
        logger.error(f"Error in getingests: {exc}", exc_info=True)
        return [{"success": False, "error": "request_failed", "message": str(exc)}]
