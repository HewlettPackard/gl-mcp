# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
getreportingstatusbyid tool for reporting MCP server.

Implements: GET /reporting/v1/statuses/{id}
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
    name="getreportingstatusbyid",
    description="Retrieve the status of a specific report by passing the report status ID.\n",
)
async def getreportingstatusbyid(  # noqa: E501
    ctx: Context,
    id: Annotated[
        str,
        Field(description="The report status identifier.\n\nExample: 3fa85f64-5717-4562-b3fc-2c963f66afa6"),
    ] = ...,
) -> list[dict[str, Any]]:
    """Retrieve the status of a specific report by passing the report status ID.\n

    Args:
        id: The report status identifier.\n\nExample: 3fa85f64-5717-4562-b3fc-2c963f66afa6
    Returns:
        API response data as a list containing one result dict.
    """
    http_client = ctx.request_context.lifespan_context.http_client

    # Build URL – URL-encode path parameters to prevent path-traversal attacks
    url = "/reporting/v1/statuses/{id}"
    url = url.replace("{" + "id" + "}", quote(str(id), safe=""))

    # Collect query / body parameters; skip values that were not provided
    params: dict[str, Any] = {}

    try:
        response_data = await http_client.get(url, params=params)
        return [{"success": True, "result": response_data}]

    except ValueError as exc:
        logger.error(f"Validation error in getreportingstatusbyid: {exc}")
        return [{"success": False, "error": "validation_error", "message": str(exc)}]

    except Exception as exc:
        logger.error(f"Error in getreportingstatusbyid: {exc}", exc_info=True)
        return [{"success": False, "error": "request_failed", "message": str(exc)}]
