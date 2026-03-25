# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
get_reporting_v1_report_exports_metadata tool for reporting MCP server.

Implements: GET /reporting/v1/report-exports-metadata
"""

from __future__ import annotations

from typing import Annotated, Any

from mcp.server.fastmcp import Context
from pydantic import Field

from config.logging import get_logger
from server.fastmcp_instance import mcp

logger = get_logger(__name__)


@mcp.tool(
    name="get_reporting_v1_report_exports_metadata",
    description="This API is a support tool that assists with generating a report. Use it to find the supported columns, filter criteria, and values for a report type.  In a response, the API returns:\n\n  - `columns`&mdash;An array containing the supported columns.\n  - `filterCriteria`&mdash;An array comprising of filter names and their corresponding data types.\n  - `supportedOperators`&mdash;A collection of supported operators assisting you in selecting the correct operator to use in a filter attribute. The following operators are supported:\n    - `EQ`&mdash;Checks if a field is equal to a value.\n    - `NE`&mdash;Checks if a field is not equal to a value.\n    - `LT`&mdash;Checks if a field is less than a value.\n    - `LE`&mdash;Checks if a field is less than or equal to a value.\n    - `GT`&mdash;Checks if a field is greater than a value.\n    - `GE`&mdash;Checks if a field is greater than or equals to a value.\n    - `IN`&mdash;Checks if a value is in a list.\n",
)
async def get_reporting_v1_report_exports_metadata(  # noqa: E501
    ctx: Context,
    filter: Annotated[
        str,
        Field(
            description="Limit the resources operated on by an endpoint or when used with a multiple-GET endpoint,\nreturn only the subset of resources that match the filter. The filter grammar is a subset\nof OData 4.0.\n\n**NOTE:** The filter query parameter must use [URL encoding](https://en.wikipedia.org/wiki/URL_encoding).\nMost clients do this automatically with inputs provided to them specifically as query parameters. Encoding must be done manually for any query parameters provided as part of the URL.  \nThe reserved characters `!` `#` `$` `&` `'` `(` `)` `*` `+` `,` `/` `:` `;` `=` `?` `@` `[` `]` must be encoded with percent encoded equivalents.\n\nFor example: the value `P06760-B21+2M212504P8` must be encoded as `P06760-B21%2B2M212504P8` when it is used in a query parameter.\n\n| CLASS     |  EXAMPLES                                          |\n|-----------|----------------------------------------------------|\n| Types     | integer, decimal, timestamp, string, boolean, null |\n| Operations| eq, ne, gt, ge, lt, le, in                         |\n| Logic     | and, or, not                                       |\n\n\nExample: name ne Subscriptions and group eq Device inventory\n\n**Filter Syntax**: Use OData-style filters. String values must be enclosed in single quotes.\n\nFilterable properties: columns, filterCriteria, id, kind, name, type"
        ),
    ] = ...,
    select: Annotated[
        str,
        Field(
            description="The select query parameter is used to limit the properties returned for a resource. The value of the select query parameter is a comma-separated list of properties.\n\nExample: map[equals:map[description:Return activities where a property equals a value.\n summary:select with equality check value:select=name]]"
        ),
    ] = ...,
    sort: Annotated[
        str,
        Field(
            description="The order in which to return the resources in the collection. The value of the sort query parameter is a comma separated list of sort expressions. Each sort expression is a property name optionally followed by a direction indicator asc (ascending) or desc (descending). The first sort expression in the list defines the primary sort order, the second defines the secondary sort order, and so on. If a direction indicator is omitted, the default direction is ascending.\n\nExamples:\n  - name asc\n    Order ascending by name\n  - name,createdAt desc\n    Order resources ascending by name and then by descending by createdAt"
        ),
    ] = ...,
    limit: Annotated[
        int | str | None,
        Field(description="The maximum number of reports to return.\n\nExample: 10", default=10),
    ] = 10,
    offset: Annotated[
        int | str | None,
        Field(description="Zero-based resource offset to start the response from.\n\nExample: 20"),
    ] = None,
) -> list[dict[str, Any]]:
    """This API is a support tool that assists with generating a report. Use it to find the supported columns, filter criteria, and values for a report type.  In a response, the API returns:\n\n  - `columns`&mdash;An array containing the supported columns.\n  - `filterCriteria`&mdash;An array comprising of filter names and their corresponding data types.\n  - `supportedOperators`&mdash;A collection of supported operators assisting you in selecting the correct operator to use in a filter attribute. The following operators are supported:\n    - `EQ`&mdash;Checks if a field is equal to a value.\n    - `NE`&mdash;Checks if a field is not equal to a value.\n    - `LT`&mdash;Checks if a field is less than a value.\n    - `LE`&mdash;Checks if a field is less than or equal to a value.\n    - `GT`&mdash;Checks if a field is greater than a value.\n    - `GE`&mdash;Checks if a field is greater than or equals to a value.\n    - `IN`&mdash;Checks if a value is in a list.\n

    Args:
        filter: Limit the resources operated on by an endpoint or when used with a multiple-GET endpoint,\nreturn only the subset of resources that match the filter. The filter grammar is a subset\nof OData 4.0.\n\n**NOTE:** The filter query parameter must use [URL encoding](https://en.wikipedia.org/wiki/URL_encoding).\nMost clients do this automatically with inputs provided to them specifically as query parameters. Encoding must be done manually for any query parameters provided as part of the URL.  \nThe reserved characters `!` `#` `$` `&` `'` `(` `)` `*` `+` `,` `/` `:` `;` `=` `?` `@` `[` `]` must be encoded with percent encoded equivalents.\n\nFor example: the value `P06760-B21+2M212504P8` must be encoded as `P06760-B21%2B2M212504P8` when it is used in a query parameter.\n\n| CLASS     |  EXAMPLES                                          |\n|-----------|----------------------------------------------------|\n| Types     | integer, decimal, timestamp, string, boolean, null |\n| Operations| eq, ne, gt, ge, lt, le, in                         |\n| Logic     | and, or, not                                       |\n\n\nExample: name ne Subscriptions and group eq Device inventory\n\n**Filter Syntax**: Use OData-style filters. String values must be enclosed in single quotes.\n\nFilterable properties: columns, filterCriteria, id, kind, name, type
        select: The select query parameter is used to limit the properties returned for a resource. The value of the select query parameter is a comma-separated list of properties.\n\nExample: map[equals:map[description:Return activities where a property equals a value.\n summary:select with equality check value:select=name]]
        sort: The order in which to return the resources in the collection. The value of the sort query parameter is a comma separated list of sort expressions. Each sort expression is a property name optionally followed by a direction indicator asc (ascending) or desc (descending). The first sort expression in the list defines the primary sort order, the second defines the secondary sort order, and so on. If a direction indicator is omitted, the default direction is ascending.\n\nExamples:\n  - name asc\n    Order ascending by name\n  - name,createdAt desc\n    Order resources ascending by name and then by descending by createdAt
        limit: The maximum number of reports to return.\n\nExample: 10
        offset: Zero-based resource offset to start the response from.\n\nExample: 20
    Returns:
        API response data as a list containing one result dict.
    """
    http_client = ctx.request_context.lifespan_context.http_client

    # Build URL – URL-encode path parameters to prevent path-traversal attacks
    url = "/reporting/v1/report-exports-metadata"

    # Collect query / body parameters; skip values that were not provided
    params: dict[str, Any] = {}
    if filter is not None and filter is not ...:
        params["filter"] = filter
    if select is not None and select is not ...:
        params["select"] = select
    if sort is not None and sort is not ...:
        params["sort"] = sort
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
        logger.error(f"Validation error in get_reporting_v1_report_exports_metadata: {exc}")
        return [{"success": False, "error": "validation_error", "message": str(exc)}]

    except Exception as exc:
        logger.error(f"Error in get_reporting_v1_report_exports_metadata: {exc}", exc_info=True)
        return [{"success": False, "error": "request_failed", "message": str(exc)}]
