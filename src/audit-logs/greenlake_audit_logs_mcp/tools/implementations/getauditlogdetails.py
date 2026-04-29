# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
getauditlogdetails tool for audit-logs MCP server.

Implements: GET /audit-log/v1/logs/{id}/detail
"""

from __future__ import annotations
from typing import Annotated, Any
from urllib.parse import quote

from mcp.server.fastmcp import Context
from pydantic import Field

from greenlake_audit_logs_mcp.config.logging import get_logger
from greenlake_audit_logs_mcp.server.fastmcp_instance import mcp

logger = get_logger(__name__)


@mcp.tool(
    name="getauditlogdetails",
    description="Get additional detail of an audit log.",
)
async def getauditlogdetails(  # noqa: E501
    ctx: Context,
    id: Annotated[
        str,
        Field(
            description="Provide the ID of the audit log record that has the `hasDetails` value set to `true` to fetch the additional details."
        ),
    ] = ...,
) -> list[dict[str, Any]]:
    """Get additional detail of an audit log.

    Args:
        id: Provide the ID of the audit log record that has the `hasDetails` value set to `true` to fetch the additional details.
    Returns:
        API response data as a list containing one result dict.
    """
    http_client = ctx.request_context.lifespan_context.http_client

    # Build URL – URL-encode path parameters to prevent path-traversal attacks
    url = "/audit-log/v1/logs/{id}/detail"
    url = url.replace("{" + "id" + "}", quote(str(id), safe=""))

    # Collect query / body parameters; skip values that were not provided
    params: dict[str, Any] = {}

    try:
        response_data = await http_client.get(url, params=params)
        return [{"success": True, "result": response_data}]

    except ValueError as exc:
        logger.error(f"Validation error in getauditlogdetails: {exc}")
        return [{"success": False, "error": "validation_error", "message": str(exc)}]

    except Exception as exc:
        logger.error(f"Error in getauditlogdetails: {exc}", exc_info=True)
        return [{"success": False, "error": "request_failed", "message": str(exc)}]
