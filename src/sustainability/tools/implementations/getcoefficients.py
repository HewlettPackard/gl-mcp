# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
getcoefficients tool for Sustainability_Insight_Center MCP server.

Implements: GET /sustainability-insight-ctr/v1beta1/coefficients
"""

from __future__ import annotations

from typing import Annotated, Any

from mcp.server.fastmcp import Context
from pydantic import Field

from config.logging import get_logger
from server.fastmcp_instance import mcp

logger = get_logger(__name__)


@mcp.tool(
    name="getcoefficients",
    description="Get a list of all costs (amount per kWh) and co2 coefficients of all locations. Supports filtering by locationId.",
)
async def getcoefficients(  # noqa: E501
    ctx: Context,
    offset: Annotated[
        int | str | None,
        Field(description="Zero-based resource offset to start the response from.\n\nExample: 10"),
    ] = None,
    limit: Annotated[
        int | str | None,
        Field(description="Number of entities to return.\n\nExample: 10", default=10),
    ] = 10,
    filter: Annotated[
        str | None,
        Field(description="Limit the coefficients operated on by this endpoint, returning only the subset of entities that match the filter. The filter grammar is a subset of OData 4.0 supporting \"eq\" operator only.\nCoefficients can be filtered by:\n- locationId\n\n\nExample: locationId eq '00000000-0000-0000-0000-0000000000000'\n\n**Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`.\n\nFilterable properties: associatedLocation, co2eGramsPerKwh, costPerKwh, costUsdPerKwh, createdAt, currency, generation, id, startTime, type, updatedAt"),
    ] = None,
) -> list[dict[str, Any]]:
    """Get a list of all costs (amount per kWh) and co2 coefficients of all locations. Supports filtering by locationId.

    Args:
        offset: Zero-based resource offset to start the response from.\n\nExample: 10
        limit: Number of entities to return.\n\nExample: 10
        filter: Limit the coefficients operated on by this endpoint, returning only the subset of entities that match the filter. The filter grammar is a subset of OData 4.0 supporting \"eq\" operator only.\nCoefficients can be filtered by:\n- locationId\n\n\nExample: locationId eq '00000000-0000-0000-0000-0000000000000'\n\n**Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`.\n\nFilterable properties: associatedLocation, co2eGramsPerKwh, costPerKwh, costUsdPerKwh, createdAt, currency, generation, id, startTime, type, updatedAt
    Returns:
        API response data as a list containing one result dict.
    """
    http_client = ctx.request_context.lifespan_context.http_client

    # Build URL – URL-encode path parameters to prevent path-traversal attacks
    url = "/sustainability-insight-ctr/v1beta1/coefficients"

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
    if filter is not None and filter is not ...:
        params["filter"] = filter

    try:
        response_data = await http_client.get(url, params=params)
        return [{"success": True, "result": response_data}]

    except ValueError as exc:
        logger.error(f"Validation error in getcoefficients: {exc}")
        return [{"success": False, "error": "validation_error", "message": str(exc)}]

    except Exception as exc:
        logger.error(f"Error in getcoefficients: {exc}", exc_info=True)
        return [{"success": False, "error": "request_failed", "message": str(exc)}]
