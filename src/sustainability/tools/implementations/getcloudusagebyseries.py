# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
getcloudusagebyseries tool for Sustainability_Insight_Center MCP server.

Implements: GET /sustainability-insight-ctr/v1beta1/cloud-usage-series
"""

from __future__ import annotations

from typing import Annotated, Any

from mcp.server.fastmcp import Context
from pydantic import Field

from config.logging import get_logger
from server.fastmcp_instance import mcp

logger = get_logger(__name__)


@mcp.tool(
    name="getcloudusagebyseries",
    description="Retrieves aggregated carbon footprint usage statistics grouped by time bucket over a defined time frame and \nsupports filtering by entities. Behavior is non-deterministic if the time range does not divide evenly by your selected \ninterval.\n",
)
async def getcloudusagebyseries(  # noqa: E501
    ctx: Context,
    filter: Annotated[
        str | None,
        Field(description="Limit the cloud entities operated on by this endpoint, returning only the subset of entities that match the filter. The \nfilter grammar is a subset of OData 4.0 supporting \"eq\", \"in\", and \"and\" operators only.\n\nCloud entities can be filtered by:\n- entityId\n- serviceProvider\n- serviceName\n- serviceRegion\n- serviceAccount\n- name\n\n\nExamples:\n  - serviceRegion in ('EMEA', 'AMERICAS')\n  - serviceProvider eq 'AWS'\n\n**Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`.\n\nFilterable properties: co2eMetricTon, id, timeBucket, type"),
    ] = None,
    interval: Annotated[
        str,
        Field(description="Interval of the created time series. Must be of the format \"integer unit\". Valid units are day(s), hour\n(s), week(s), month(s), and year(s). Cloud usage typically is measured in months, so the smaller time units are \nlikely to be approximations.\n\n\nExamples:\n  - 3 months\n  - 1 month"),
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
    """Retrieves aggregated carbon footprint usage statistics grouped by time bucket over a defined time frame and \nsupports filtering by entities. Behavior is non-deterministic if the time range does not divide evenly by your selected \ninterval.\n

    Args:
        filter: Limit the cloud entities operated on by this endpoint, returning only the subset of entities that match the filter. The \nfilter grammar is a subset of OData 4.0 supporting \"eq\", \"in\", and \"and\" operators only.\n\nCloud entities can be filtered by:\n- entityId\n- serviceProvider\n- serviceName\n- serviceRegion\n- serviceAccount\n- name\n\n\nExamples:\n  - serviceRegion in ('EMEA', 'AMERICAS')\n  - serviceProvider eq 'AWS'\n\n**Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`.\n\nFilterable properties: co2eMetricTon, id, timeBucket, type
        interval: Interval of the created time series. Must be of the format \"integer unit\". Valid units are day(s), hour\n(s), week(s), month(s), and year(s). Cloud usage typically is measured in months, so the smaller time units are \nlikely to be approximations.\n\n\nExamples:\n  - 3 months\n  - 1 month
        start-time: Start of the query's time range in ISO8601 format.\n\nExample: 2024-01-28T08:00:00Z
        end-time: End of the query's time range in ISO8601 format.\n\nExample: 2024-01-29T08:00:00Z
    Returns:
        API response data as a list containing one result dict.
    """
    http_client = ctx.request_context.lifespan_context.http_client

    # Build URL – URL-encode path parameters to prevent path-traversal attacks
    url = "/sustainability-insight-ctr/v1beta1/cloud-usage-series"

    # Collect query / body parameters; skip values that were not provided
    params: dict[str, Any] = {}
    if filter is not None and filter is not ...:
        params["filter"] = filter
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
        logger.error(f"Validation error in getcloudusagebyseries: {exc}")
        return [{"success": False, "error": "validation_error", "message": str(exc)}]

    except Exception as exc:
        logger.error(f"Error in getcloudusagebyseries: {exc}", exc_info=True)
        return [{"success": False, "error": "request_failed", "message": str(exc)}]
