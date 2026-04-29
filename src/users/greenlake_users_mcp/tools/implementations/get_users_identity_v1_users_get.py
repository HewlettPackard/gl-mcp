# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
get_users_identity_v1_users_get tool for users MCP server.

Implements: GET /identity/v1/users
"""

from __future__ import annotations
from typing import Annotated, Any

from mcp.server.fastmcp import Context
from pydantic import Field

from greenlake_users_mcp.config.logging import get_logger
from greenlake_users_mcp.server.fastmcp_instance import mcp

logger = get_logger(__name__)


@mcp.tool(
    name="get_users_identity_v1_users_get",
    description="Retrieve list of users with filtering, and pagination options. All users are returned when no filters are provided. \n**Note**: User view all permission is required to invoke this API. \nRate limit: 300 requests per minute per workspace, resulting in a `429` error if exceeded.\n",
)
async def get_users_identity_v1_users_get(  # noqa: E501
    ctx: Context,
    filter: Annotated[
        str | None,
        Field(
            description="Filter data using a subset of OData 4.0 and return only the subset of resources that match the filter.\n\nSupported classes and examples include:\n- **Types**: timestamp, string\n- **Comparison**: eq, ne, gt, ge, lt\n- **Logical Expressions**: and, or, not\n\nThe Get users API can be filtered by:\n- id\n- username\n- userStatus\n- createdAt\n- updatedAt\n- lastLogin\n\nuserStatus can be one of the following:\n- UNVERIFIED\n- VERIFIED\n- BLOCKED\n- DELETE_IN_PROGRESS\n- DELETED\n- SUSPENDED\n\n**Note**: The userStatus filter is case-sensitive.\n\nExamples:\n  - username eq 'user@example.com'\n    Returns the user with a specific username.\n  - createdAt gt '2020-09-21T14:19:09.769747'\n    Returns users created after 2020-09-21T14:19:09.769747\n  - username eq 'user@example.com'\n    Returns the user with a specific email.\n  - id eq '7600415a-8876-5722-9f3c-b0fd11112283'\n    Returns the user with a specific ID.\n  - lastLogin lt '2020-09-21T14:19:09.769747'\n    Returns users that logged in before 2020-09-21T14:19:09.769747\n  - updatedAt gt '2020-09-21T14:19:09.769747'\n    Returns users updated after 2020-09-21T14:19:09.769747\n  - userStatus ne 'UNVERIFIED'\n    Returns users that are not unverified.\n\n**Filter Syntax**: Use OData-style filters with the field names shown in the examples above. String values must be enclosed in single quotes."
        ),
    ] = None,
    offset: Annotated[
        int | str | None,
        Field(
            description="Specify pagination offset. An offset argument defines how many pages to skip before returning results."
        ),
    ] = None,
    limit: Annotated[
        int | str | None,
        Field(
            description="Specify the maximum number of entries per page. NOTE: The maximum value accepted is 600.",
            default=300,
        ),
    ] = 300,
) -> list[dict[str, Any]]:
    """Retrieve list of users with filtering, and pagination options. All users are returned when no filters are provided. \n**Note**: User view all permission is required to invoke this API. \nRate limit: 300 requests per minute per workspace, resulting in a `429` error if exceeded.\n

    Args:
        filter: Filter data using a subset of OData 4.0 and return only the subset of resources that match the filter.\n\nSupported classes and examples include:\n- **Types**: timestamp, string\n- **Comparison**: eq, ne, gt, ge, lt\n- **Logical Expressions**: and, or, not\n\nThe Get users API can be filtered by:\n- id\n- username\n- userStatus\n- createdAt\n- updatedAt\n- lastLogin\n\nuserStatus can be one of the following:\n- UNVERIFIED\n- VERIFIED\n- BLOCKED\n- DELETE_IN_PROGRESS\n- DELETED\n- SUSPENDED\n\n**Note**: The userStatus filter is case-sensitive.\n\nExamples:\n  - username eq 'user@example.com'\n    Returns the user with a specific username.\n  - createdAt gt '2020-09-21T14:19:09.769747'\n    Returns users created after 2020-09-21T14:19:09.769747\n  - username eq 'user@example.com'\n    Returns the user with a specific email.\n  - id eq '7600415a-8876-5722-9f3c-b0fd11112283'\n    Returns the user with a specific ID.\n  - lastLogin lt '2020-09-21T14:19:09.769747'\n    Returns users that logged in before 2020-09-21T14:19:09.769747\n  - updatedAt gt '2020-09-21T14:19:09.769747'\n    Returns users updated after 2020-09-21T14:19:09.769747\n  - userStatus ne 'UNVERIFIED'\n    Returns users that are not unverified.\n\n**Filter Syntax**: Use OData-style filters with the field names shown in the examples above. String values must be enclosed in single quotes.
        offset: Specify pagination offset. An offset argument defines how many pages to skip before returning results.
        limit: Specify the maximum number of entries per page. NOTE: The maximum value accepted is 600.
    Returns:
        API response data as a list containing one result dict.
    """
    http_client = ctx.request_context.lifespan_context.http_client

    # Build URL – URL-encode path parameters to prevent path-traversal attacks
    url = "/identity/v1/users"

    # Collect query / body parameters; skip values that were not provided
    params: dict[str, Any] = {}
    if filter is not None and filter is not ...:
        params["filter"] = filter
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

    try:
        response_data = await http_client.get(url, params=params)
        return [{"success": True, "result": response_data}]

    except ValueError as exc:
        logger.error(f"Validation error in get_users_identity_v1_users_get: {exc}")
        return [{"success": False, "error": "validation_error", "message": str(exc)}]

    except Exception as exc:
        logger.error(f"Error in get_users_identity_v1_users_get: {exc}", exc_info=True)
        return [{"success": False, "error": "request_failed", "message": str(exc)}]
