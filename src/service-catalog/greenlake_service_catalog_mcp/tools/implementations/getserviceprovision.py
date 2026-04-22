# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
getserviceprovision tool for service-catalog MCP server.

Implements: GET /service-catalog/v1beta1/service-provisions/{id}
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
    name="getserviceprovision",
    description="Fetch service provision details for an ID.",
)
async def getserviceprovision(  # noqa: E501
    ctx: Context,
    id: Annotated[
        str,
        Field(
            description="The unique identifier of a service provision. The ID is returned by the `Get service provisions` endpoint."
        ),
    ] = ...,
    unredacted: Annotated[
        str | None,
        Field(description="If set to true, get the entire entry along with sensitive fields.\n\nExample: true"),
    ] = None,
) -> list[dict[str, Any]]:
    """Fetch service provision details for an ID.

    Args:
        id: The unique identifier of a service provision. The ID is returned by the `Get service provisions` endpoint.
        unredacted: If set to true, get the entire entry along with sensitive fields.\n\nExample: true
    Returns:
        API response data as a list containing one result dict.
    """
    http_client = ctx.request_context.lifespan_context.http_client

    # Build URL – URL-encode path parameters to prevent path-traversal attacks
    url = "/service-catalog/v1beta1/service-provisions/{id}"
    url = url.replace("{" + "id" + "}", quote(str(id), safe=""))

    # Collect query / body parameters; skip values that were not provided
    params: dict[str, Any] = {}
    if unredacted is not None and unredacted is not ...:
        params["unredacted"] = unredacted

    try:
        response_data = await http_client.get(url, params=params)
        return [{"success": True, "result": response_data}]

    except ValueError as exc:
        logger.error(f"Validation error in getserviceprovision: {exc}")
        return [{"success": False, "error": "validation_error", "message": str(exc)}]

    except Exception as exc:
        logger.error(f"Error in getserviceprovision: {exc}", exc_info=True)
        return [{"success": False, "error": "request_failed", "message": str(exc)}]
