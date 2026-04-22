# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
getserviceofferregions tool for service-catalog MCP server.

Implements: GET /service-catalog/v1beta1/service-offer-regions
"""

from __future__ import annotations
from typing import Annotated, Any

from mcp.server.fastmcp import Context
from pydantic import Field

from greenlake_service_catalog_mcp.config.logging import get_logger
from greenlake_service_catalog_mcp.server.fastmcp_instance import mcp

logger = get_logger(__name__)


@mcp.tool(
    name="getserviceofferregions",
    description="Retrieve a list of service offer regions by applying filters.\nEach service offer region represents a service offer provisioned in a specific region.\n<br><br>**Pagination:** This API supports cursor-based pagination. Provide the cursor in the `next` query parameter to retrieve the next page.\n",
)
async def getserviceofferregions(  # noqa: E501
    ctx: Context,
    next: Annotated[
        str | None,
        Field(
            description="Specifies the pagination cursor for the next page of service offer regions.\n\nExample: 64136af7-cd64-4b4e-88a8-150ab51a920d"
        ),
    ] = None,
    limit: Annotated[
        int | str | None,
        Field(description="Specifies the number of results to be returned.", default=2000),
    ] = 2000,
    filter: Annotated[
        str | None,
        Field(
            description="The `filter` query parameter is used to filter the set of resources returned in a `GET` request. The returned set of resources must match the criteria in the filter query parameter.<br><br> The value of the `filter` query parameter is a subset of [OData 4.0](https://www.odata.org/documentation/) filter expressions consisting of simple comparison operations joined by logical operators.<br><br>**Supported fields**: `serviceOfferId`, `status`, and `region`.<br>**Supported operand**: `eq`<br>**Supported operations**: `and`\n\nExamples:\n  - serviceOfferId eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050' and status eq 'ONBOARDED' and region eq 'us-east'\n    Return service offer regions with a given service offer ID and status and region\n  - region eq 'us-east'\n    Return service offer regions with a given region\n  - status eq 'ONBOARDED'\n    Return service offer regions with a given status\n  - serviceOfferId eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050'\n    Return service offer regions with a given service offer ID\n  - serviceOfferId eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050' and region eq 'us-east'\n    Return service offer regions with a given service offer ID and region\n  - serviceOfferId eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050' and status eq 'ONBOARDED'\n    Return service offer regions with a given service offer ID and status\n\n**Filter Syntax**: Use OData-style filters with the field names shown in the examples above. String values must be enclosed in single quotes."
        ),
    ] = None,
) -> list[dict[str, Any]]:
    """Retrieve a list of service offer regions by applying filters.\nEach service offer region represents a service offer provisioned in a specific region.\n<br><br>**Pagination:** This API supports cursor-based pagination. Provide the cursor in the `next` query parameter to retrieve the next page.\n

    Args:
        next: Specifies the pagination cursor for the next page of service offer regions.\n\nExample: 64136af7-cd64-4b4e-88a8-150ab51a920d
        limit: Specifies the number of results to be returned.
        filter: The `filter` query parameter is used to filter the set of resources returned in a `GET` request. The returned set of resources must match the criteria in the filter query parameter.<br><br> The value of the `filter` query parameter is a subset of [OData 4.0](https://www.odata.org/documentation/) filter expressions consisting of simple comparison operations joined by logical operators.<br><br>**Supported fields**: `serviceOfferId`, `status`, and `region`.<br>**Supported operand**: `eq`<br>**Supported operations**: `and`\n\nExamples:\n  - serviceOfferId eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050' and status eq 'ONBOARDED' and region eq 'us-east'\n    Return service offer regions with a given service offer ID and status and region\n  - region eq 'us-east'\n    Return service offer regions with a given region\n  - status eq 'ONBOARDED'\n    Return service offer regions with a given status\n  - serviceOfferId eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050'\n    Return service offer regions with a given service offer ID\n  - serviceOfferId eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050' and region eq 'us-east'\n    Return service offer regions with a given service offer ID and region\n  - serviceOfferId eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050' and status eq 'ONBOARDED'\n    Return service offer regions with a given service offer ID and status\n\n**Filter Syntax**: Use OData-style filters with the field names shown in the examples above. String values must be enclosed in single quotes.
    Returns:
        API response data as a list containing one result dict.
    """
    http_client = ctx.request_context.lifespan_context.http_client

    # Build URL – URL-encode path parameters to prevent path-traversal attacks
    url = "/service-catalog/v1beta1/service-offer-regions"

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
        logger.error(f"Validation error in getserviceofferregions: {exc}")
        return [{"success": False, "error": "validation_error", "message": str(exc)}]

    except Exception as exc:
        logger.error(f"Error in getserviceofferregions: {exc}", exc_info=True)
        return [{"success": False, "error": "request_failed", "message": str(exc)}]
