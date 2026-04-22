# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
getserviceoffers tool for service-catalog MCP server.

Implements: GET /service-catalog/v1beta1/service-offers
"""

from __future__ import annotations
from typing import Annotated, Any

from mcp.server.fastmcp import Context
from pydantic import Field

from greenlake_service_catalog_mcp.config.logging import get_logger
from greenlake_service_catalog_mcp.server.fastmcp_instance import mcp

logger = get_logger(__name__)


@mcp.tool(
    name="getserviceoffers",
    description="Retrieve a list of service offers by applying filters. \nA service offer provides a distinct set of functionality that can be independently identified and assigned access.\n<br><br>**Pagination:** This API supports cursor-based pagination. Provide the cursor in the `next` query parameter to retrieve the next page.\n",
)
async def getserviceoffers(  # noqa: E501
    ctx: Context,
    next: Annotated[
        str | None,
        Field(
            description="Specifies the pagination cursor for the next page of service offers.\n\nExample: 64136af7-cd64-4b4e-88a8-150ab51a920d"
        ),
    ] = None,
    limit: Annotated[
        int | str | None,
        Field(description="Specifies the number of results to be returned.", default=2000),
    ] = 2000,
    filter: Annotated[
        str | None,
        Field(
            description="The `filter` query parameter is used to filter the set of resources returned in a `GET` request. The returned set of resources must match the criteria in the filter query parameter.<br><br> The value of the `filter` query parameter is a subset of [OData 4.0](https://www.odata.org/documentation/) filter expressions consisting of simple comparison operations joined by logical operators.<br><br>**Supported fields**: `category`, `serviceManagerId`, `status`, `isDefault`, `slug`, and `staticLaunchUrl`.<br>**Supported operand**: `eq`<br>**Supported operations**: `and`\n\nExamples:\n  - slug eq 'GLP'\n    Return service offers with a given slug\n  - staticLaunchUrl eq '/Organization'\n    Return service offers for a given static launch URL\n  - status eq 'ONBOARDED'\n    Return service offers with a given status\n  - category eq 'COMPUTE'\n    Return service offers for a given category\n  - isDefault eq true\n    Return service offers that are service managers\n  - serviceManagerId eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050'\n    Return service offers for given service manager ID\n\n**Filter Syntax**: Use OData-style filters with the field names shown in the examples above. String values must be enclosed in single quotes."
        ),
    ] = None,
) -> list[dict[str, Any]]:
    """Retrieve a list of service offers by applying filters. \nA service offer provides a distinct set of functionality that can be independently identified and assigned access.\n<br><br>**Pagination:** This API supports cursor-based pagination. Provide the cursor in the `next` query parameter to retrieve the next page.\n

    Args:
        next: Specifies the pagination cursor for the next page of service offers.\n\nExample: 64136af7-cd64-4b4e-88a8-150ab51a920d
        limit: Specifies the number of results to be returned.
        filter: The `filter` query parameter is used to filter the set of resources returned in a `GET` request. The returned set of resources must match the criteria in the filter query parameter.<br><br> The value of the `filter` query parameter is a subset of [OData 4.0](https://www.odata.org/documentation/) filter expressions consisting of simple comparison operations joined by logical operators.<br><br>**Supported fields**: `category`, `serviceManagerId`, `status`, `isDefault`, `slug`, and `staticLaunchUrl`.<br>**Supported operand**: `eq`<br>**Supported operations**: `and`\n\nExamples:\n  - slug eq 'GLP'\n    Return service offers with a given slug\n  - staticLaunchUrl eq '/Organization'\n    Return service offers for a given static launch URL\n  - status eq 'ONBOARDED'\n    Return service offers with a given status\n  - category eq 'COMPUTE'\n    Return service offers for a given category\n  - isDefault eq true\n    Return service offers that are service managers\n  - serviceManagerId eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050'\n    Return service offers for given service manager ID\n\n**Filter Syntax**: Use OData-style filters with the field names shown in the examples above. String values must be enclosed in single quotes.
    Returns:
        API response data as a list containing one result dict.
    """
    http_client = ctx.request_context.lifespan_context.http_client

    # Build URL – URL-encode path parameters to prevent path-traversal attacks
    url = "/service-catalog/v1beta1/service-offers"

    # Collect query / body parameters; skip values that were not provided
    params: dict[str, Any] = {}
    if next is not None and next is not ...:
        params["next"] = next
    if limit is not None and limit is not ...:
        # Coerce string supplied by LLM clients to int
        try:
            params["limit"] = int(limit)
        except (ValueError, TypeError) as exc:
            raise ValueError("'limit' must be an integer") from exc
    if filter is not None and filter is not ...:
        params["filter"] = filter

    try:
        response_data = await http_client.get(url, params=params)
        return [{"success": True, "result": response_data}]

    except ValueError as exc:
        logger.error(f"Validation error in getserviceoffers: {exc}")
        return [{"success": False, "error": "validation_error", "message": str(exc)}]

    except Exception as exc:
        logger.error(f"Error in getserviceoffers: {exc}", exc_info=True)
        return [{"success": False, "error": "request_failed", "message": str(exc)}]
