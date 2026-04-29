# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
getdevicesv1 tool for devices MCP server.

Implements: GET /devices/v1/devices
"""

from __future__ import annotations
from typing import Annotated, Any

from mcp.server.fastmcp import Context
from pydantic import Field

from greenlake_devices_mcp.config.logging import get_logger
from greenlake_devices_mcp.server.fastmcp_instance import mcp

logger = get_logger(__name__)


@mcp.tool(
    name="getdevicesv1",
    description="With this API, you can: <ul><li>Retrieve a list of devices managed in a workspace.</li> <li>Filter  devices based on conditional expressions.</li></ul><p><b>NOTE</b>: You need view  permissions for Devices and Subscription service to invoke this API.</p>  Rate limits are enforced on this API. 160 requests per minute is supported per workspace. The API returns `429` if this threshold is breached.",
)
async def getdevicesv1(  # noqa: E501
    ctx: Context,
    filter: Annotated[
        str | None,
        Field(
            description="Filter expressions consisting of simple comparison operations joined\nby logical operators.<br>\n| CLASS               |   EXAMPLES                                         |\n|---------------------|----------------------------------------------------|\n| Types               | integer, decimal, timestamp, string, boolean, null |\n| Comparison          | eq, ne, gt, ge, lt, le, in                         |\n| Logical Expressions | and, or, not                                       |\n\nThe following examples are not an exhaustive list of all possible filtering options.\n\n\nExamples:\n  - updatedAt le '2024-02-18T19:53:51.480Z'\n    Return devices where a property is lesser or equal to a value.\nExample syntax, \\<property> ge \\<value>.\n  - not serialNumber eq 'STIAPL6404'\n    Return devices where a property does not equal a value.\nExample syntax, not \\<property> eq \\<value>.\n  - deviceType in 'COMPUTE', 'STORAGE'\n    Return devices where a property is one of multiple values.\nExample syntax, \\<property> in \\<value>,\\<value>.\n  - deviceType eq 'STORAGE' and partNumber eq 'RTICXL6413'\n    Return devices that exactly satisfy multiple filter queries.\nExample syntax, \\<property> eq \\<value> and \\<property> eq \\<value>.\n  - serialNumber eq 'STIAPL6404' or partNumber eq 'RTICXL6413'\n    Return devices that exactly satisfy one of multiple filter queries.\nExample syntax, \\<property> eq \\<value> or \\<property> eq \\<value>.\n  - serialNumber eq 'STIAPL6404'\n    Return devices where a property equals a value.\nExample syntax, \\<property> eq \\<value>.\n  - createdAt ge ''2024-01-18T19:53:51.480Z''\n    Return devices where a property is greater or equal to a value.\nExample syntax, \\<property> ge \\<value>.\n\n**Filter Syntax**: Use OData-style filters with the field names shown in the examples above. String values must be enclosed in single quotes."
        ),
    ] = None,
    filter_tags: Annotated[
        str | None,
        Field(
            description="Filter expressions consisting of simple comparison operations joined\nby logical operators to be applied on the assigned tags or their\nvalues.<br>\n| CLASS               |   EXAMPLES      |\n|---------------------|-----------------|\n| Types               | string          |\n| Comparison          | eq, ne, in      |\n| Logical Expressions | and, or, not    |\n\n\nExamples:\n  - not 'city' eq 'Tokyo'\n    Return devices where a tag key does not equal a tag value.\nExample syntax, not \\<property> eq \\<value>.\n  - 'street' in 'Regent Street', 'Oxford Street', 'Piccadilly'\n    Return devices containing the tag key and at least one of the specified values.\nExample syntax, \\<property> in \\<value>,\\<value>.\n  - 'city' eq 'London' and 'street' eq 'Piccadilly'\n    Return devices that exactly satisfy multiple filter queries applied to tag keys.\nExample syntax, \\<property> eq \\<value> and \\<property> eq \\<value>.\n  - 'street' eq 'Oxford Street' or 'street' eq 'Piccadilly'\n    Return devices that satisfy any of multiple filter queries applied to tag keys.\nExample syntax, \\<property> eq \\<value> or \\<property> eq \\<value>.\n  - 'city' eq 'London'\n    Return devices where a tag key is equal to a tag value.\nExample syntax, \\<tagKey> eq \\<tagValue>.\n\n**Filter Syntax**: Use OData-style filters with the field names shown in the examples above. String values must be enclosed in single quotes."
        ),
    ] = None,
    sort: Annotated[
        str | None,
        Field(
            description="A comma separated list of sort expressions. A sort expression is a property name optionally followed by a direction indicator `asc` or `desc`. The default is ascending order.\n\nExample: serialNumber,macAddress desc"
        ),
    ] = None,
    select: Annotated[
        str | None,
        Field(
            description="A comma separated list of select properties to display in the response. The default is that all properties are returned.\n\nExample: serialNumber,macAddress"
        ),
    ] = None,
    limit: Annotated[
        int | str | None,
        Field(description="Specifies the number of results to be returned. The default value is 2000.", default=2000),
    ] = 2000,
    offset: Annotated[
        int | str | None,
        Field(
            description="Specifies the zero-based resource offset to start the response from. The default value is 0."
        ),
    ] = None,
) -> list[dict[str, Any]]:
    """With this API, you can: <ul><li>Retrieve a list of devices managed in a workspace.</li> <li>Filter  devices based on conditional expressions.</li></ul><p><b>NOTE</b>: You need view  permissions for Devices and Subscription service to invoke this API.</p>  Rate limits are enforced on this API. 160 requests per minute is supported per workspace. The API returns `429` if this threshold is breached.

    Args:
        filter: Filter expressions consisting of simple comparison operations joined\nby logical operators.<br>\n| CLASS               |   EXAMPLES                                         |\n|---------------------|----------------------------------------------------|\n| Types               | integer, decimal, timestamp, string, boolean, null |\n| Comparison          | eq, ne, gt, ge, lt, le, in                         |\n| Logical Expressions | and, or, not                                       |\n\nThe following examples are not an exhaustive list of all possible filtering options.\n\n\nExamples:\n  - updatedAt le '2024-02-18T19:53:51.480Z'\n    Return devices where a property is lesser or equal to a value.\nExample syntax, \\<property> ge \\<value>.\n  - not serialNumber eq 'STIAPL6404'\n    Return devices where a property does not equal a value.\nExample syntax, not \\<property> eq \\<value>.\n  - deviceType in 'COMPUTE', 'STORAGE'\n    Return devices where a property is one of multiple values.\nExample syntax, \\<property> in \\<value>,\\<value>.\n  - deviceType eq 'STORAGE' and partNumber eq 'RTICXL6413'\n    Return devices that exactly satisfy multiple filter queries.\nExample syntax, \\<property> eq \\<value> and \\<property> eq \\<value>.\n  - serialNumber eq 'STIAPL6404' or partNumber eq 'RTICXL6413'\n    Return devices that exactly satisfy one of multiple filter queries.\nExample syntax, \\<property> eq \\<value> or \\<property> eq \\<value>.\n  - serialNumber eq 'STIAPL6404'\n    Return devices where a property equals a value.\nExample syntax, \\<property> eq \\<value>.\n  - createdAt ge ''2024-01-18T19:53:51.480Z''\n    Return devices where a property is greater or equal to a value.\nExample syntax, \\<property> ge \\<value>.\n\n**Filter Syntax**: Use OData-style filters with the field names shown in the examples above. String values must be enclosed in single quotes.
        filter-tags: Filter expressions consisting of simple comparison operations joined\nby logical operators to be applied on the assigned tags or their\nvalues.<br>\n| CLASS               |   EXAMPLES      |\n|---------------------|-----------------|\n| Types               | string          |\n| Comparison          | eq, ne, in      |\n| Logical Expressions | and, or, not    |\n\n\nExamples:\n  - not 'city' eq 'Tokyo'\n    Return devices where a tag key does not equal a tag value.\nExample syntax, not \\<property> eq \\<value>.\n  - 'street' in 'Regent Street', 'Oxford Street', 'Piccadilly'\n    Return devices containing the tag key and at least one of the specified values.\nExample syntax, \\<property> in \\<value>,\\<value>.\n  - 'city' eq 'London' and 'street' eq 'Piccadilly'\n    Return devices that exactly satisfy multiple filter queries applied to tag keys.\nExample syntax, \\<property> eq \\<value> and \\<property> eq \\<value>.\n  - 'street' eq 'Oxford Street' or 'street' eq 'Piccadilly'\n    Return devices that satisfy any of multiple filter queries applied to tag keys.\nExample syntax, \\<property> eq \\<value> or \\<property> eq \\<value>.\n  - 'city' eq 'London'\n    Return devices where a tag key is equal to a tag value.\nExample syntax, \\<tagKey> eq \\<tagValue>.\n\n**Filter Syntax**: Use OData-style filters with the field names shown in the examples above. String values must be enclosed in single quotes.
        sort: A comma separated list of sort expressions. A sort expression is a property name optionally followed by a direction indicator `asc` or `desc`. The default is ascending order.\n\nExample: serialNumber,macAddress desc
        select: A comma separated list of select properties to display in the response. The default is that all properties are returned.\n\nExample: serialNumber,macAddress
        limit: Specifies the number of results to be returned. The default value is 2000.
        offset: Specifies the zero-based resource offset to start the response from. The default value is 0.
    Returns:
        API response data as a list containing one result dict.
    """
    http_client = ctx.request_context.lifespan_context.http_client

    # Build URL – URL-encode path parameters to prevent path-traversal attacks
    url = "/devices/v1/devices"

    # Collect query / body parameters; skip values that were not provided
    params: dict[str, Any] = {}
    if filter is not None and filter is not ...:
        params["filter"] = filter
    if filter_tags is not None and filter_tags is not ...:
        params["filter-tags"] = filter_tags
    if sort is not None and sort is not ...:
        params["sort"] = sort
    if select is not None and select is not ...:
        params["select"] = select
    if limit is not None and limit is not ...:
        # Coerce string supplied by LLM clients to int
        try:
            params["limit"] = int(limit)
        except (ValueError, TypeError) as exc:
            raise ValueError("'limit' must be an integer") from exc
    if offset is not None and offset is not ...:
        # Coerce string supplied by LLM clients to int
        try:
            params["offset"] = int(offset)
        except (ValueError, TypeError) as exc:
            raise ValueError("'offset' must be an integer") from exc

    try:
        response_data = await http_client.get(url, params=params)
        return [{"success": True, "result": response_data}]

    except ValueError as exc:
        logger.error(f"Validation error in getdevicesv1: {exc}")
        return [{"success": False, "error": "validation_error", "message": str(exc)}]

    except Exception as exc:
        logger.error(f"Error in getdevicesv1: {exc}", exc_info=True)
        return [{"success": False, "error": "request_failed", "message": str(exc)}]
