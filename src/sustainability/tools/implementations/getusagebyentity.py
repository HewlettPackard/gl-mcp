# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
getusagebyentity tool for Sustainability_Insight_Center MCP server.

Implements: GET /sustainability-insight-ctr/v1beta1/usage-by-entity
"""

from __future__ import annotations

from typing import Annotated, Any

from mcp.server.fastmcp import Context
from pydantic import Field

from config.logging import get_logger
from server.fastmcp_instance import mcp

logger = get_logger(__name__)


@mcp.tool(
    name="getusagebyentity",
    description="Retrieves an aggregated energy usage list grouped by individual entities over a defined time frame and supports filtering, sorting, and offset-based pagination.",
)
async def getusagebyentity(  # noqa: E501
    ctx: Context,
    filter: Annotated[
        str | None,
        Field(description="Limit the entities operated on by this endpoint, returning only the subset of entities that match the filter. The filter grammar is a subset of OData 4.0 supporting \"eq\", \"in\", and \"and\" operators only.\nUsage entities can be filtered by:\n- entityId\n- entityMake\n- entityModel\n- entityType\n- entitySerialNum\n- entityProductId\n- locationName\n- locationId\n- locationCity\n- locationState\n- locationCountry\n- name\n\n\nExamples:\n  - locationCountry eq 'DE'\n  - entityModel in ('ProLiant DL325 Gen11', 'ProLiant DL380 Gen10')\n\n**Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`.\n\nFilterable properties: co2eMetricTon, cost, costUsd, currency, entityId, entityMake, entityManufacturerTimestamp, entityModel, entityProductId, entitySerialNum, entityType, id, kwh, locationCity, locationCountry, locationId, locationName, locationState, name, tags, type"),
    ] = None,
    filter_tags: Annotated[
        str | None,
        Field(description="Limit the entities operated on by this endpoint, returning only the subset of entities that contain the tags. The filter grammar is a subset of OData 4.0 supporting \"eq\" and \"or\" operators only.\nThe tag key is on the left of the operator, the value is on the right.\n\n\nExamples:\n  - 'Tagged' eq ''\n  - 'OS' eq 'Linux' or 'OS' eq 'Windows'\n  - 'OS' eq 'Linux'\n\n**Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`.\n\nFilterable properties: co2eMetricTon, cost, costUsd, currency, entityId, entityMake, entityManufacturerTimestamp, entityModel, entityProductId, entitySerialNum, entityType, id, kwh, locationCity, locationCountry, locationId, locationName, locationState, name, tags, type"),
    ] = None,
    currency: Annotated[
        str | None,
        Field(description="The 3 letter currency code the cost returned will be in, case insensitive. Currency calculations are done via a factor queried at the beginning of the day. Defaults to USD.\n\n\nExample: CAD"),
    ] = None,
    sort: Annotated[
        str | None,
        Field(description="Odata 4.0 field to sort entities on. Allowed fields are the strings \"locationName\", \"locationCountry\", \"locationState\", \"entityId\", \"entityMake\", \"entityModel\", \"entityType\", \"entitySerialNum\", \"entityProductId\", \"name\". Must be of the format \"property order\".\n\nExamples:\n  - entityId desc\n  - name asc"),
    ] = None,
    offset: Annotated[
        int | str | None,
        Field(description="Zero-based resource offset to start the response from.\n\nExample: 10"),
    ] = None,
    limit: Annotated[
        int | str | None,
        Field(description="Number of usages to return.\n\nExample: 10", default=10),
    ] = 10,
    start_time: Annotated[
        str,
        Field(description="Start of the query's time range in ISO8601 format.\n\nExample: 2024-01-28T08:00:00Z"),
    ] = ...,
    end_time: Annotated[
        str,
        Field(description="End of the query's time range in ISO8601 format.\n\nExample: 2024-01-29T08:00:00Z"),
    ] = ...,
) -> list[dict[str, Any]]:
    """Retrieves an aggregated energy usage list grouped by individual entities over a defined time frame and supports filtering, sorting, and offset-based pagination.

    Args:
        filter: Limit the entities operated on by this endpoint, returning only the subset of entities that match the filter. The filter grammar is a subset of OData 4.0 supporting \"eq\", \"in\", and \"and\" operators only.\nUsage entities can be filtered by:\n- entityId\n- entityMake\n- entityModel\n- entityType\n- entitySerialNum\n- entityProductId\n- locationName\n- locationId\n- locationCity\n- locationState\n- locationCountry\n- name\n\n\nExamples:\n  - locationCountry eq 'DE'\n  - entityModel in ('ProLiant DL325 Gen11', 'ProLiant DL380 Gen10')\n\n**Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`.\n\nFilterable properties: co2eMetricTon, cost, costUsd, currency, entityId, entityMake, entityManufacturerTimestamp, entityModel, entityProductId, entitySerialNum, entityType, id, kwh, locationCity, locationCountry, locationId, locationName, locationState, name, tags, type
        filter-tags: Limit the entities operated on by this endpoint, returning only the subset of entities that contain the tags. The filter grammar is a subset of OData 4.0 supporting \"eq\" and \"or\" operators only.\nThe tag key is on the left of the operator, the value is on the right.\n\n\nExamples:\n  - 'Tagged' eq ''\n  - 'OS' eq 'Linux' or 'OS' eq 'Windows'\n  - 'OS' eq 'Linux'\n\n**Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`.\n\nFilterable properties: co2eMetricTon, cost, costUsd, currency, entityId, entityMake, entityManufacturerTimestamp, entityModel, entityProductId, entitySerialNum, entityType, id, kwh, locationCity, locationCountry, locationId, locationName, locationState, name, tags, type
        currency: The 3 letter currency code the cost returned will be in, case insensitive. Currency calculations are done via a factor queried at the beginning of the day. Defaults to USD.\n\n\nExample: CAD
        sort: Odata 4.0 field to sort entities on. Allowed fields are the strings \"locationName\", \"locationCountry\", \"locationState\", \"entityId\", \"entityMake\", \"entityModel\", \"entityType\", \"entitySerialNum\", \"entityProductId\", \"name\". Must be of the format \"property order\".\n\nExamples:\n  - entityId desc\n  - name asc
        offset: Zero-based resource offset to start the response from.\n\nExample: 10
        limit: Number of usages to return.\n\nExample: 10
        start-time: Start of the query's time range in ISO8601 format.\n\nExample: 2024-01-28T08:00:00Z
        end-time: End of the query's time range in ISO8601 format.\n\nExample: 2024-01-29T08:00:00Z
    Returns:
        API response data as a list containing one result dict.
    """
    http_client = ctx.request_context.lifespan_context.http_client

    # Build URL – URL-encode path parameters to prevent path-traversal attacks
    url = "/sustainability-insight-ctr/v1beta1/usage-by-entity"

    # Collect query / body parameters; skip values that were not provided
    params: dict[str, Any] = {}
    if filter is not None and filter is not ...:
        params["filter"] = filter
    if filter_tags is not None and filter_tags is not ...:
        params["filter-tags"] = filter_tags
    if currency is not None and currency is not ...:
        params["currency"] = currency
    if sort is not None and sort is not ...:
        params["sort"] = sort
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
    if start_time is not None and start_time is not ...:
        params["start-time"] = start_time
    if end_time is not None and end_time is not ...:
        params["end-time"] = end_time

    try:
        response_data = await http_client.get(url, params=params)
        return [{"success": True, "result": response_data}]

    except ValueError as exc:
        logger.error(f"Validation error in getusagebyentity: {exc}")
        return [{"success": False, "error": "validation_error", "message": str(exc)}]

    except Exception as exc:
        logger.error(f"Error in getusagebyentity: {exc}", exc_info=True)
        return [{"success": False, "error": "request_failed", "message": str(exc)}]
