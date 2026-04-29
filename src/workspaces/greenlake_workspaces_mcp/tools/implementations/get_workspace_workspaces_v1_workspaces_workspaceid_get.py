# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
get_workspace_workspaces_v1_workspaces_workspaceid_get tool for workspaces MCP server.

Implements: GET /workspaces/v1/workspaces/{workspaceId}
"""

from __future__ import annotations
from typing import Annotated, Any
from urllib.parse import quote

from mcp.server.fastmcp import Context
from pydantic import Field

from greenlake_workspaces_mcp.config.logging import get_logger
from greenlake_workspaces_mcp.server.fastmcp_instance import mcp

logger = get_logger(__name__)


@mcp.tool(
    name="get_workspace_workspaces_v1_workspaces_workspaceid_get",
    description="Retrieve basic workspace information for a provided workspace identifier.",
)
async def get_workspace_workspaces_v1_workspaces_workspaceid_get(  # noqa: E501
    ctx: Context,
    workspaceId: Annotated[
        str,
        Field(description="The unique identifier of the workspace.\n\nExample: 7600415a-8876-5722-9f3c-b0fd11112283"),
    ] = ...,
) -> list[dict[str, Any]]:
    """Retrieve basic workspace information for a provided workspace identifier.

    Args:
        workspaceId: The unique identifier of the workspace.\n\nExample: 7600415a-8876-5722-9f3c-b0fd11112283
    Returns:
        API response data as a list containing one result dict.
    """
    http_client = ctx.request_context.lifespan_context.http_client

    # Build URL – URL-encode path parameters to prevent path-traversal attacks
    url = "/workspaces/v1/workspaces/{workspaceId}"
    url = url.replace("{" + "workspaceId" + "}", quote(str(workspaceId), safe=""))

    # Collect query / body parameters; skip values that were not provided
    params: dict[str, Any] = {}

    try:
        response_data = await http_client.get(url, params=params)
        return [{"success": True, "result": response_data}]

    except ValueError as exc:
        logger.error(f"Validation error in get_workspace_workspaces_v1_workspaces_workspaceid_get: {exc}")
        return [{"success": False, "error": "validation_error", "message": str(exc)}]

    except Exception as exc:
        logger.error(f"Error in get_workspace_workspaces_v1_workspaces_workspaceid_get: {exc}", exc_info=True)
        return [{"success": False, "error": "request_failed", "message": str(exc)}]
