# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
getsubscriptionsv1 tool for subscriptions MCP server.

Implements: GET /subscriptions/v1/subscriptions
"""

from __future__ import annotations
import re
from typing import Annotated, Any

from mcp.server.fastmcp import Context
from pydantic import Field

from greenlake_subscriptions_mcp.config.logging import get_logger
from greenlake_subscriptions_mcp.server.fastmcp_instance import mcp

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
    name="getsubscriptionsv1",
    description="Get subscriptions managed in a workspace. Filters can be passed to filter  the subscriptions based on conditional expressions.<br><br>**NOTE:** You need to have  view permission for the **Devices and subscription service** to invoke this API. <br><br> Rate limits are enforced on this API. 60 requests per minute is supported per workspace. API will result in `429` if this threshold is breached.",
)
async def getsubscriptionsv1(  # noqa: E501
    ctx: Context,
    filter: Annotated[
        str | None,
        Field(
            description="Filter expressions consisting of simple comparison operations joined \nby logical operators.<br>\n| CLASS                |   EXAMPLES                                         |\n|----------------------|----------------------------------------------------|\n| Types                | integer, decimal, timestamp, string, boolean, null |\n| Comparison           | eq, ne, gt, ge, lt, le, in                         |\n| Logical Expressions  | and, or, not                                       |\n\nSubscriptions can be filtered based on the following properties:\n- `id`\n- `subscriptionType`\n- `subscriptionStatus`\n- `key`\n- `quantity`\n- `availableQuantity`\n- `sku`\n- `skuDescription`\n- `contract`\n- `startTime`\n- `endTime`\n- `productType`\n- `tier`\n- `tierDescription`\n- `quote`\n- `po`\n- `resellerPo`\n- `createdAt`\n- `updatedAt`\n\nThe following is a non-exhaustive list of possible filtering options.\n\n\nExamples:\n  - subscriptionType in 'CENTRAL_STORAGE', 'CENTRAL_CONTROLLER'\n    Return subscriptions where the property is one of multiple values. Example syntax, \n\\<property> in \\<value>,\\<value>.\n  - not key eq 'STIAPL6404'\n    Return subscriptions where a property does not equal a value. Example syntax, \nnot \\<property> eq \\<value>.\n  - key eq 'STIQQ4L04' and subscriptionType eq 'CENTRAL_STORAGE'\n    The AND operator returns results that meet all filter queries. In the example, the query only returns subscriptions with the exact key and with the specified subscription type. Example syntax,\n\\<property> eq \\<value> and \\<property> eq \\<value>.\n  - key eq 'STIAPL6404'\n    Return subscriptions where a property equals a value. Example syntax, \n\\<property> eq \\<value>.\n  - createdAt ge '2024-01-18T19:53:51.480Z'\n    Return subscriptions where a property is greater or equal to a value. Example syntax,\n\\<property> ge \\<value>.\n  - updatedAt le '2024-02-18T19:53:51.480Z'\n    Return subscriptions where a property is less than or equal to a value. Example syntax,\n\\<property> le \\<value>.\n  - key eq 'STIQQ4L04' or subscriptionType eq 'CENTRAL_STORAGE'\n    The OR operator returns results that meet any of the filter queries. In the example, the query returns subscriptions with the exact key or with the specified subscription type.\n  - startTime gt '2024-01-23T00:00:00.000Z' and endTime lt '2025-02-22T00:00:00.000Z' and not productType eq 'SERVICE'\n    The AND, OR, and NOT operators can be combined to return results that satisfy all specified filter criteria.\n  - tier ne 'BRIDGE'\n    Return subscriptions where a property does not equate to a value. Example syntax, \n\\<property> ne \\<value>.\n\n**Filter Syntax**: Use OData-style filters with the field names shown in the examples above. String values must be enclosed in single quotes."
        ),
    ] = None,
    filter_tags: Annotated[
        str | None,
        Field(
            description="Filter expressions consisting of simple comparison operations joined\nby logical operators to be applied on the assigned tags or their\nvalues.<br>\n| CLASS               |   EXAMPLES      |\n|---------------------|-----------------|\n| Types               | string          |\n| Comparison          | eq, ne          |\n| Logical Expressions | and, or         |\n\n\nExamples:\n  - 'street' eq 'Oxford Street' or 'street' eq 'Piccadilly'\n    Return subscriptions containing the tag key and the corresponding value that satisfy at least one of the conditionals. Example syntax, \n\\<property> eq \\<value> or \\<property> eq \\<value>.\n  - 'city' eq 'London'\n    Return subscriptions that have a pair of tags with the exact same tag key and tag value. Example syntax, \n\\<tagKey> eq \\<tagValue>.\n  - 'city' ne 'London'\n    Return subscriptions that have a pair of tags with the exact same tag key and the exact different tag value. Example syntax, \n\\<tagKey> ne \\<tagValue>.\n  - 'city' eq 'London' and 'street' eq 'Piccadilly'\n    Return subscriptions containing the tag key and the corresponding value that satisfy all conditionals. Example syntax, \n\\<property> eq \\<value> and \\<property> eq \\<value>.\n\n**Filter Syntax**: Use OData-style filters with the field names shown in the examples above. String values must be enclosed in single quotes."
        ),
    ] = None,
    sort: Annotated[
        str | None,
        Field(
            description="A comma separated list of sort expressions. A sort expression is a  property name optionally followed by a direction indicator `asc` or  `desc`. The default is ascending order.\n\nExample: key, quote desc"
        ),
    ] = None,
    select: Annotated[
        str | None,
        Field(
            description="A comma separated list of select properties to display in the response.  The default is that all properties are returned.\n\nExample: id,key"
        ),
    ] = None,
    limit: Annotated[
        int | str | None,
        Field(description="Specifies the number of results to be returned. The default value  is 50.", default=50),
    ] = 50,
    offset: Annotated[
        int | str | None,
        Field(
            description="Specifies the zero-based resource offset to start the response from. The default value is 0."
        ),
    ] = None,
) -> list[dict[str, Any]]:
    """Get subscriptions managed in a workspace. Filters can be passed to filter  the subscriptions based on conditional expressions.<br><br>**NOTE:** You need to have  view permission for the **Devices and subscription service** to invoke this API. <br><br> Rate limits are enforced on this API. 60 requests per minute is supported per workspace. API will result in `429` if this threshold is breached.

    Args:
        filter: Filter expressions consisting of simple comparison operations joined \nby logical operators.<br>\n| CLASS                |   EXAMPLES                                         |\n|----------------------|----------------------------------------------------|\n| Types                | integer, decimal, timestamp, string, boolean, null |\n| Comparison           | eq, ne, gt, ge, lt, le, in                         |\n| Logical Expressions  | and, or, not                                       |\n\nSubscriptions can be filtered based on the following properties:\n- `id`\n- `subscriptionType`\n- `subscriptionStatus`\n- `key`\n- `quantity`\n- `availableQuantity`\n- `sku`\n- `skuDescription`\n- `contract`\n- `startTime`\n- `endTime`\n- `productType`\n- `tier`\n- `tierDescription`\n- `quote`\n- `po`\n- `resellerPo`\n- `createdAt`\n- `updatedAt`\n\nThe following is a non-exhaustive list of possible filtering options.\n\n\nExamples:\n  - subscriptionType in 'CENTRAL_STORAGE', 'CENTRAL_CONTROLLER'\n    Return subscriptions where the property is one of multiple values. Example syntax, \n\\<property> in \\<value>,\\<value>.\n  - not key eq 'STIAPL6404'\n    Return subscriptions where a property does not equal a value. Example syntax, \nnot \\<property> eq \\<value>.\n  - key eq 'STIQQ4L04' and subscriptionType eq 'CENTRAL_STORAGE'\n    The AND operator returns results that meet all filter queries. In the example, the query only returns subscriptions with the exact key and with the specified subscription type. Example syntax,\n\\<property> eq \\<value> and \\<property> eq \\<value>.\n  - key eq 'STIAPL6404'\n    Return subscriptions where a property equals a value. Example syntax, \n\\<property> eq \\<value>.\n  - createdAt ge '2024-01-18T19:53:51.480Z'\n    Return subscriptions where a property is greater or equal to a value. Example syntax,\n\\<property> ge \\<value>.\n  - updatedAt le '2024-02-18T19:53:51.480Z'\n    Return subscriptions where a property is less than or equal to a value. Example syntax,\n\\<property> le \\<value>.\n  - key eq 'STIQQ4L04' or subscriptionType eq 'CENTRAL_STORAGE'\n    The OR operator returns results that meet any of the filter queries. In the example, the query returns subscriptions with the exact key or with the specified subscription type.\n  - startTime gt '2024-01-23T00:00:00.000Z' and endTime lt '2025-02-22T00:00:00.000Z' and not productType eq 'SERVICE'\n    The AND, OR, and NOT operators can be combined to return results that satisfy all specified filter criteria.\n  - tier ne 'BRIDGE'\n    Return subscriptions where a property does not equate to a value. Example syntax, \n\\<property> ne \\<value>.\n\n**Filter Syntax**: Use OData-style filters with the field names shown in the examples above. String values must be enclosed in single quotes.
        filter-tags: Filter expressions consisting of simple comparison operations joined\nby logical operators to be applied on the assigned tags or their\nvalues.<br>\n| CLASS               |   EXAMPLES      |\n|---------------------|-----------------|\n| Types               | string          |\n| Comparison          | eq, ne          |\n| Logical Expressions | and, or         |\n\n\nExamples:\n  - 'street' eq 'Oxford Street' or 'street' eq 'Piccadilly'\n    Return subscriptions containing the tag key and the corresponding value that satisfy at least one of the conditionals. Example syntax, \n\\<property> eq \\<value> or \\<property> eq \\<value>.\n  - 'city' eq 'London'\n    Return subscriptions that have a pair of tags with the exact same tag key and tag value. Example syntax, \n\\<tagKey> eq \\<tagValue>.\n  - 'city' ne 'London'\n    Return subscriptions that have a pair of tags with the exact same tag key and the exact different tag value. Example syntax, \n\\<tagKey> ne \\<tagValue>.\n  - 'city' eq 'London' and 'street' eq 'Piccadilly'\n    Return subscriptions containing the tag key and the corresponding value that satisfy all conditionals. Example syntax, \n\\<property> eq \\<value> and \\<property> eq \\<value>.\n\n**Filter Syntax**: Use OData-style filters with the field names shown in the examples above. String values must be enclosed in single quotes.
        sort: A comma separated list of sort expressions. A sort expression is a  property name optionally followed by a direction indicator `asc` or  `desc`. The default is ascending order.\n\nExample: key, quote desc
        select: A comma separated list of select properties to display in the response.  The default is that all properties are returned.\n\nExample: id,key
        limit: Specifies the number of results to be returned. The default value  is 50.
        offset: Specifies the zero-based resource offset to start the response from. The default value is 0.
    Returns:
        API response data as a list containing one result dict.
    """
    http_client = ctx.request_context.lifespan_context.http_client

    # Build URL – URL-encode path parameters to prevent path-traversal attacks
    url = "/subscriptions/v1/subscriptions"

    # Collect query / body parameters; skip values that were not provided
    params: dict[str, Any] = {}
    if filter is not None and filter is not ...:
        params["filter"] = _normalize_filter_quotes(filter)
    if filter_tags is not None and filter_tags is not ...:
        params["filter-tags"] = _normalize_filter_quotes(filter_tags)
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
        logger.error(f"Validation error in getsubscriptionsv1: {exc}")
        return [{"success": False, "error": "validation_error", "message": str(exc)}]

    except Exception as exc:
        logger.error(f"Error in getsubscriptionsv1: {exc}", exc_info=True)
        return [{"success": False, "error": "request_failed", "message": str(exc)}]
