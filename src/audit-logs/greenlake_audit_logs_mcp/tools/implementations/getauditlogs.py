# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
getauditlogs tool for audit-logs MCP server.

Implements: GET /audit-log/v1/logs
"""

from __future__ import annotations
from typing import Annotated, Any

from mcp.server.fastmcp import Context
from pydantic import Field

from greenlake_audit_logs_mcp.config.logging import get_logger
from greenlake_audit_logs_mcp.server.fastmcp_instance import mcp

logger = get_logger(__name__)


@mcp.tool(
    name="getauditlogs",
    description="The audit logs can be filtered using a variety of parameters. Queries should be separated by `and` and can utilize `eq`, `contains`, and `in` operators to construct the final query. Each query should follow the format:\n* key eq 'value' for equality operation.\n* contains(key, 'value') for contains operation.\n* key in ('value1', 'value2') for in operation.\n\n| Filter parameter         | Supported Operators | Type                    | Example                                                                                         |\n|--------------------------|---------------------|-------------------------|-------------------------------------------------------------------------------------------------|\n| createdAt                | lt, ge              | RFC timestamp in string | createdAt ge '2024-02-16T07:54:55.0Z'                                                           |\n| category                 | eq, in              | string                  | category eq 'User Management' category in ('Device Management', 'User Activity')                |\n| description              | eq, contains        | string                  | contains(description, 'Logged in') description eq 'User test@test.com logged in via ping mode.' |\n| additionalInfo/ipAddress | eq, contains        | IP string               | additionalInfo/ipAddress eq '192.168.12.12' contains(additionalInfo/ipAddress, '192.168')       |\n| user/username            | eq, contains        | email in string         | user/username eq 'test@test.com' contains(user/username, '@gmail.com')                          |\n| workspace/workspaceName  | eq, contains        | string                  | workspace/workspaceName eq 'Example workspace' contains(workspace/workspaceName, 'Example')     |\n| application/id           | eq                  | UUID in string          | application/id eq '12312-123123-123123-123121'                                                  |\n| region                   | eq                  | region code in string   | region eq 'us-west'                                                                             |\n| hasDetails               | eq                  | boolean                 | hasDetails eq 'true'                                                                              |\n",
)
async def getauditlogs(  # noqa: E501
    ctx: Context,
    filter: Annotated[
        str | None,
        Field(
            description="Example: category eq 'User Management' and contains(description, 'logged out')\n\n**Filter Syntax**: Use OData-style filters with the field names shown in the examples above. String values must be enclosed in single quotes."
        ),
    ] = None,
    select: Annotated[
        str | None,
        Field(
            description="Use the `select` query parameter to restrict the number of properties included in the audit log response.\nThe supported select parameters:\n * additionalInfo\n * createdAt\n * category\n * hasDetails\n * workspace/workspaceName\n * description\n * user/username\n\n\nExample: createdAt, user/username, category"
        ),
    ] = None,
    all: Annotated[
        str | None,
        Field(
            description="Provide a free-text search to perform a comprehensive search across all properties for audit logs.\n\nExample: logged in user"
        ),
    ] = None,
    limit: Annotated[
        int | str | None,
        Field(description="How many items to return at one time (max 2000)", default=50),
    ] = 50,
    offset: Annotated[
        int | str | None,
        Field(description="Specifies the zero-based resource offset to start the response from."),
    ] = None,
) -> list[dict[str, Any]]:
    """The audit logs can be filtered using a variety of parameters. Queries should be separated by `and` and can utilize `eq`, `contains`, and `in` operators to construct the final query. Each query should follow the format:\n* key eq 'value' for equality operation.\n* contains(key, 'value') for contains operation.\n* key in ('value1', 'value2') for in operation.\n\n| Filter parameter         | Supported Operators | Type                    | Example                                                                                         |\n|--------------------------|---------------------|-------------------------|-------------------------------------------------------------------------------------------------|\n| createdAt                | lt, ge              | RFC timestamp in string | createdAt ge '2024-02-16T07:54:55.0Z'                                                           |\n| category                 | eq, in              | string                  | category eq 'User Management' category in ('Device Management', 'User Activity')                |\n| description              | eq, contains        | string                  | contains(description, 'Logged in') description eq 'User test@test.com logged in via ping mode.' |\n| additionalInfo/ipAddress | eq, contains        | IP string               | additionalInfo/ipAddress eq '192.168.12.12' contains(additionalInfo/ipAddress, '192.168')       |\n| user/username            | eq, contains        | email in string         | user/username eq 'test@test.com' contains(user/username, '@gmail.com')                          |\n| workspace/workspaceName  | eq, contains        | string                  | workspace/workspaceName eq 'Example workspace' contains(workspace/workspaceName, 'Example')     |\n| application/id           | eq                  | UUID in string          | application/id eq '12312-123123-123123-123121'                                                  |\n| region                   | eq                  | region code in string   | region eq 'us-west'                                                                             |\n| hasDetails               | eq                  | boolean                 | hasDetails eq 'true'                                                                              |\n

    Args:
        filter: Example: category eq 'User Management' and contains(description, 'logged out')\n\n**Filter Syntax**: Use OData-style filters with the field names shown in the examples above. String values must be enclosed in single quotes.
        select: Use the `select` query parameter to restrict the number of properties included in the audit log response.\nThe supported select parameters:\n * additionalInfo\n * createdAt\n * category\n * hasDetails\n * workspace/workspaceName\n * description\n * user/username\n\n\nExample: createdAt, user/username, category
        all: Provide a free-text search to perform a comprehensive search across all properties for audit logs.\n\nExample: logged in user
        limit: How many items to return at one time (max 2000)
        offset: Specifies the zero-based resource offset to start the response from.
    Returns:
        API response data as a list containing one result dict.
    """
    http_client = ctx.request_context.lifespan_context.http_client

    # Build URL – URL-encode path parameters to prevent path-traversal attacks
    url = "/audit-log/v1/logs"

    # Collect query / body parameters; skip values that were not provided
    params: dict[str, Any] = {}
    if filter is not None and filter is not ...:
        params["filter"] = filter
    if select is not None and select is not ...:
        params["select"] = select
    if all is not None and all is not ...:
        params["all"] = all
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
        logger.error(f"Validation error in getauditlogs: {exc}")
        return [{"success": False, "error": "validation_error", "message": str(exc)}]

    except Exception as exc:
        logger.error(f"Error in getauditlogs: {exc}", exc_info=True)
        return [{"success": False, "error": "request_failed", "message": str(exc)}]
