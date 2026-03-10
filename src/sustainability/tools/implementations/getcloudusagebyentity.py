# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
getcloudusagebyentity tool for Sustainability_Insight_Center MCP server.

Implements: GET /sustainability-insight-ctr/v1beta1/cloud-usage-by-entity
"""

from __future__ import annotations

from typing import Annotated, Any

from mcp.server.fastmcp import Context
from pydantic import Field

from config.logging import get_logger
from server.fastmcp_instance import mcp

logger = get_logger(__name__)


@mcp.tool(
    name="getcloudusagebyentity",
    description="Retrieves aggregated carbon footprint usage in a list grouped by individual cloud entities, i.e., cloud services, over a \ndefined time frame and supports filtering, sorting, and offset-based pagination.\n",
)
async def getcloudusagebyentity(  # noqa: E501
    ctx: Context,
    filter: Annotated[
        str | None,
        Field(description="Limit the cloud entities operated on by this endpoint, returning only the subset of entities that match the filter. The \nfilter grammar is a subset of OData 4.0 supporting \"eq\", \"in\", and \"and\" operators only.\n\nCloud entities can be filtered by:\n- entityId\n- serviceProvider\n- serviceName\n- serviceRegion\n- serviceAccount\n- name\n\n\nExamples:\n  - serviceProvider eq 'AWS'\n  - serviceRegion in ('EMEA', 'AMERICAS')\n\n**Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`.\n\nFilterable properties: co2eMetricTon, entityId, id, name, serviceAccount, serviceName, serviceProvider, serviceRegion, type"),
    ] = None,
    sort: Annotated[
        str | None,
        Field(description="Odata 4.0 field to sort entities on. Allowed fields are the strings \"entityId\", \"serviceProvider\", \"serviceName\", \"serviceRegion\", \"serviceAccount\", \"name\". Must be of the format \"property order\".\n\nExamples:\n  - entityId desc\n  - serviceAccount asc"),
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
    """Retrieves aggregated carbon footprint usage in a list grouped by individual cloud entities, i.e., cloud services, over a \ndefined time frame and supports filtering, sorting, and offset-based pagination.\n

    Args:
        filter: Limit the cloud entities operated on by this endpoint, returning only the subset of entities that match the filter. The \nfilter grammar is a subset of OData 4.0 supporting \"eq\", \"in\", and \"and\" operators only.\n\nCloud entities can be filtered by:\n- entityId\n- serviceProvider\n- serviceName\n- serviceRegion\n- serviceAccount\n- name\n\n\nExamples:\n  - serviceProvider eq 'AWS'\n  - serviceRegion in ('EMEA', 'AMERICAS')\n\n**Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`.\n\nFilterable properties: co2eMetricTon, entityId, id, name, serviceAccount, serviceName, serviceProvider, serviceRegion, type
        sort: Odata 4.0 field to sort entities on. Allowed fields are the strings \"entityId\", \"serviceProvider\", \"serviceName\", \"serviceRegion\", \"serviceAccount\", \"name\". Must be of the format \"property order\".\n\nExamples:\n  - entityId desc\n  - serviceAccount asc
        offset: Zero-based resource offset to start the response from.\n\nExample: 10
        limit: Number of usages to return.\n\nExample: 10
        start-time: Start of the query's time range in ISO8601 format.\n\nExample: 2024-01-28T08:00:00Z
        end-time: End of the query's time range in ISO8601 format.\n\nExample: 2024-01-29T08:00:00Z
    Returns:
        API response data as a list containing one result dict.
    """
    http_client = ctx.request_context.lifespan_context.http_client

    # Build URL – URL-encode path parameters to prevent path-traversal attacks
    url = "/sustainability-insight-ctr/v1beta1/cloud-usage-by-entity"

    # Collect query / body parameters; skip values that were not provided
    params: dict[str, Any] = {}
    if filter is not None and filter is not ...:
        params["filter"] = filter
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
        logger.error(f"Validation error in getcloudusagebyentity: {exc}")
        return [{"success": False, "error": "validation_error", "message": str(exc)}]

    except Exception as exc:
        logger.error(f"Error in getcloudusagebyentity: {exc}", exc_info=True)
        return [{"success": False, "error": "request_failed", "message": str(exc)}]
