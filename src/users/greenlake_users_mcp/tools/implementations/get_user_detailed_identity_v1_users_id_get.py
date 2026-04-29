# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
get_user_detailed_identity_v1_users_id_get tool for users MCP server.

Implements: GET /identity/v1/users/{id}
"""

from __future__ import annotations
from typing import Annotated, Any
from urllib.parse import quote

from mcp.server.fastmcp import Context
from pydantic import Field

from greenlake_users_mcp.config.logging import get_logger
from greenlake_users_mcp.server.fastmcp_instance import mcp

logger = get_logger(__name__)


@mcp.tool(
    name="get_user_detailed_identity_v1_users_id_get",
    description="Retrieve a single user based on a given user ID.",
)
async def get_user_detailed_identity_v1_users_id_get(  # noqa: E501
    ctx: Context,
    id: Annotated[
        str,
        Field(description="The unique identifier of the user.\n\nExample: 7600415a-8876-5722-9f3c-b0fd11112283"),
    ] = ...,
) -> list[dict[str, Any]]:
    """Retrieve a single user based on a given user ID.

    Args:
        id: The unique identifier of the user.\n\nExample: 7600415a-8876-5722-9f3c-b0fd11112283
    Returns:
        API response data as a list containing one result dict.
    """
    http_client = ctx.request_context.lifespan_context.http_client

    # Build URL – URL-encode path parameters to prevent path-traversal attacks
    url = "/identity/v1/users/{id}"
    url = url.replace("{" + "id" + "}", quote(str(id), safe=""))

    # Collect query / body parameters; skip values that were not provided
    params: dict[str, Any] = {}

    try:
        response_data = await http_client.get(url, params=params)
        return [{"success": True, "result": response_data}]

    except ValueError as exc:
        logger.error(f"Validation error in get_user_detailed_identity_v1_users_id_get: {exc}")
        return [{"success": False, "error": "validation_error", "message": str(exc)}]

    except Exception as exc:
        logger.error(f"Error in get_user_detailed_identity_v1_users_id_get: {exc}", exc_info=True)
        return [{"success": False, "error": "request_failed", "message": str(exc)}]
