# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
getreportingstatuses tool for reporting MCP server.

Implements: GET /reporting/v1/statuses
"""

from __future__ import annotations
import re
from typing import Annotated, Any

from mcp.server.fastmcp import Context
from pydantic import Field

from greenlake_reporting_mcp.config.logging import get_logger
from greenlake_reporting_mcp.server.fastmcp_instance import mcp

logger = get_logger(__name__)


def _normalize_filter_quotes(filter_expr: str) -> str:
    """Wrap unquoted numeric values in single quotes for OData filter expressions.

    LLMs sometimes omit quotes around numeric filter values (e.g., ``quantity eq 5``
    instead of ``quantity eq '5'``), which causes 400 Bad Request from the API.
    This function normalises those bare numeric values while leaving booleans,
    already-quoted strings, and other tokens untouched.
    """
    return re.sub(
        r"\b(eq|ne|gt|ge|lt|le)\s+(-?\d+(?:\.\d+)?)\b",
        r"\1 '\2'",
        filter_expr,
    )


@mcp.tool(
    name="getreportingstatuses",
    description="This API is designed to fetch the status of all reports for a specific workspace. Only reports belonging to the workspace ID and username are returned. This API supports pagination, allowing you to use offset and limit parameters.\n",
)
async def getreportingstatuses(  # noqa: E501
    ctx: Context,
    filter: Annotated[
        str,
        Field(
            description='Example: type eq "REPORT"\n\n**Filter Syntax**: Use OData-style filters with the field names shown in the examples above. String values must be enclosed in double quotes.'
        ),
    ] = ...,
    sort: Annotated[
        str | None,
        Field(
            description="The order in which to return the resources in the collection.The value of the sort query parameter is a comma separated list of sort expressions. Each sort expression is a property name optionally followed by a direction indicator asc (ascending) or desc (descending).The first sort expression in the list defines the primary sort order, the second defines the secondary sort order, and so on. If a direction indicator is omitted the default direction is ascending.\n\nExamples:\n  - name,createdAt desc\n    Order resources ascending by name and then by descending by createdAt\n  - name asc\n    Order ascending by name"
        ),
    ] = None,
    limit: Annotated[
        int | str | None,
        Field(description="The maximum number of reports to return.\n\nExample: 50", default=10),
    ] = 10,
    offset: Annotated[
        int | str | None,
        Field(description="Zero-based resource offset to start the response from.\n\nExample: 20"),
    ] = None,
) -> list[dict[str, Any]]:
    """This API is designed to fetch the status of all reports for a specific workspace. Only reports belonging to the workspace ID and username are returned. This API supports pagination, allowing you to use offset and limit parameters.\n

    Args:
        filter: Example: type eq \"REPORT\"\n\n**Filter Syntax**: Use OData-style filters with the field names shown in the examples above. String values must be enclosed in double quotes.
        sort: The order in which to return the resources in the collection.The value of the sort query parameter is a comma separated list of sort expressions. Each sort expression is a property name optionally followed by a direction indicator asc (ascending) or desc (descending).The first sort expression in the list defines the primary sort order, the second defines the secondary sort order, and so on. If a direction indicator is omitted the default direction is ascending.\n\nExamples:\n  - name,createdAt desc\n    Order resources ascending by name and then by descending by createdAt\n  - name asc\n    Order ascending by name
        limit: The maximum number of reports to return.\n\nExample: 50
        offset: Zero-based resource offset to start the response from.\n\nExample: 20
    Returns:
        API response data as a list containing one result dict.
    """
    http_client = ctx.request_context.lifespan_context.http_client

    # Build URL – URL-encode path parameters to prevent path-traversal attacks
    url = "/reporting/v1/statuses"

    # Collect query / body parameters; skip values that were not provided
    params: dict[str, Any] = {}
    if filter is not None and filter is not ...:
        params["filter"] = _normalize_filter_quotes(filter)
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
        logger.error(f"Validation error in getreportingstatuses: {exc}")
        return [{"success": False, "error": "validation_error", "message": str(exc)}]

    except Exception as exc:
        logger.error(f"Error in getreportingstatuses: {exc}", exc_info=True)
        return [{"success": False, "error": "request_failed", "message": str(exc)}]
