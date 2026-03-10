# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
getusagebyseries tool for Sustainability_Insight_Center MCP server.

Implements: GET /sustainability-insight-ctr/v1beta1/usage-series
"""

from __future__ import annotations

from typing import Annotated, Any

from mcp.server.fastmcp import Context
from pydantic import Field

from config.logging import get_logger
from server.fastmcp_instance import mcp

logger = get_logger(__name__)


@mcp.tool(
    name="getusagebyseries",
    description="Retrieves aggregated energy usage statistics grouped by time bucket over a defined time frame and supports filtering by entities. Behavior is non-deterministic if the time range does not divide evenly by your selected interval.",
)
async def getusagebyseries(  # noqa: E501
    ctx: Context,
    filter: Annotated[
        str | None,
        Field(description="Limit the entities operated on by this endpoint, returning only the usage for entities that match the filter. The filter grammar is a subset of OData 4.0 supporting \"eq\", \"in\", and \"and\" operators only.\nUsage entities can be filtered by:\n- entityId\n- entityMake\n- entityModel\n- entityType\n- entitySerialNum\n- entityProductId\n- locationName\n- locationId\n- locationCity\n- locationState\n- locationCountry\n\n\nExamples:\n  - locationCountry eq 'DE'\n  - entityModel in ('ProLiant DL325 Gen11', 'ProLiant DL380 Gen10')\n\n**Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`.\n\nFilterable properties: co2eMetricTon, cost, costUsd, currency, id, kwh, timeBucket, type"),
    ] = None,
    filter_tags: Annotated[
        str | None,
        Field(description="Limit the entities operated on by this endpoint, returning only the subset of entities that contain the tags. The filter grammar is a subset of OData 4.0 supporting \"eq\" and \"or\" operators only.\nThe tag key is on the left of the operator, the value is on the right.\n\n\nExamples:\n  - 'OS' eq 'Linux'\n  - 'Tagged' eq ''\n  - 'OS' eq 'Linux' or 'OS' eq 'Windows'\n\n**Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`.\n\nFilterable properties: co2eMetricTon, cost, costUsd, currency, id, kwh, timeBucket, type"),
    ] = None,
    currency: Annotated[
        str | None,
        Field(description="The 3 letter currency code the cost returned will be in, case insensitive. Currency calculations are done via a factor queried at the beginning of the day. Defaults to USD.\n\n\nExample: CAD"),
    ] = None,
    interval: Annotated[
        str,
        Field(description="Interval of the created time series. Must be of the format \"integer unit\". Valid units are day(s), hour(s), week(s), month(s), and year(s).\n\nExamples:\n  - 2 hours\n  - 1 day"),
    ] = ...,
    start_time: Annotated[
        str,
        Field(description="Start of the query's time range in ISO8601 format.\n\nExample: 2024-01-28T08:00:00Z"),
    ] = ...,
    end_time: Annotated[
        str,
        Field(description="End of the query's time range in ISO8601 format.\n\nExample: 2024-01-29T08:00:00Z"),
    ] = ...,
) -> list[dict[str, Any]]:
    """Retrieves aggregated energy usage statistics grouped by time bucket over a defined time frame and supports filtering by entities. Behavior is non-deterministic if the time range does not divide evenly by your selected interval.

    Args:
        filter: Limit the entities operated on by this endpoint, returning only the usage for entities that match the filter. The filter grammar is a subset of OData 4.0 supporting \"eq\", \"in\", and \"and\" operators only.\nUsage entities can be filtered by:\n- entityId\n- entityMake\n- entityModel\n- entityType\n- entitySerialNum\n- entityProductId\n- locationName\n- locationId\n- locationCity\n- locationState\n- locationCountry\n\n\nExamples:\n  - locationCountry eq 'DE'\n  - entityModel in ('ProLiant DL325 Gen11', 'ProLiant DL380 Gen10')\n\n**Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`.\n\nFilterable properties: co2eMetricTon, cost, costUsd, currency, id, kwh, timeBucket, type
        filter-tags: Limit the entities operated on by this endpoint, returning only the subset of entities that contain the tags. The filter grammar is a subset of OData 4.0 supporting \"eq\" and \"or\" operators only.\nThe tag key is on the left of the operator, the value is on the right.\n\n\nExamples:\n  - 'OS' eq 'Linux'\n  - 'Tagged' eq ''\n  - 'OS' eq 'Linux' or 'OS' eq 'Windows'\n\n**Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`.\n\nFilterable properties: co2eMetricTon, cost, costUsd, currency, id, kwh, timeBucket, type
        currency: The 3 letter currency code the cost returned will be in, case insensitive. Currency calculations are done via a factor queried at the beginning of the day. Defaults to USD.\n\n\nExample: CAD
        interval: Interval of the created time series. Must be of the format \"integer unit\". Valid units are day(s), hour(s), week(s), month(s), and year(s).\n\nExamples:\n  - 2 hours\n  - 1 day
        start-time: Start of the query's time range in ISO8601 format.\n\nExample: 2024-01-28T08:00:00Z
        end-time: End of the query's time range in ISO8601 format.\n\nExample: 2024-01-29T08:00:00Z
    Returns:
        API response data as a list containing one result dict.
    """
    http_client = ctx.request_context.lifespan_context.http_client

    # Build URL – URL-encode path parameters to prevent path-traversal attacks
    url = "/sustainability-insight-ctr/v1beta1/usage-series"

    # Collect query / body parameters; skip values that were not provided
    params: dict[str, Any] = {}
    if filter is not None and filter is not ...:
        params["filter"] = filter
    if filter_tags is not None and filter_tags is not ...:
        params["filter-tags"] = filter_tags
    if currency is not None and currency is not ...:
        params["currency"] = currency
    if interval is not None and interval is not ...:
        params["interval"] = interval
    if start_time is not None and start_time is not ...:
        params["start-time"] = start_time
    if end_time is not None and end_time is not ...:
        params["end-time"] = end_time

    try:
        response_data = await http_client.get(url, params=params)
        return [{"success": True, "result": response_data}]

    except ValueError as exc:
        logger.error(f"Validation error in getusagebyseries: {exc}")
        return [{"success": False, "error": "validation_error", "message": str(exc)}]

    except Exception as exc:
        logger.error(f"Error in getusagebyseries: {exc}", exc_info=True)
        return [{"success": False, "error": "request_failed", "message": str(exc)}]
