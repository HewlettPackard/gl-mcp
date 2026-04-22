# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
getserviceprovisions tool for service-catalog MCP server.

Implements: GET /service-catalog/v1beta1/service-provisions
"""

from __future__ import annotations
from typing import Annotated, Any

from mcp.server.fastmcp import Context
from pydantic import Field

from greenlake_service_catalog_mcp.config.logging import get_logger
from greenlake_service_catalog_mcp.server.fastmcp_instance import mcp

logger = get_logger(__name__)


@mcp.tool(
    name="getserviceprovisions",
    description="Retrieve a list of service provisions by applying filters.\nA service offer provides a distinct set of functionalities that can be independently identified and assigned access. Service offers are typically associated with roles and permissions, commerce, metering, quote-to-cash, and trial evaluations.\nA service provision occurs when a service offer is provisioned (added) to a workspace.\n<br><br>**Pagination**: This endpoint supports cursor-based pagination using the `next` query parameter. Provide the cursor in the `next` query parameter to retrieve the next page. \n",
)
async def getserviceprovisions(  # noqa: E501
    ctx: Context,
    hpe_workspace_id: Annotated[
        str | None,
        Field(description='The workspace ID. Required if the "view all" parameter is false.', default="Id"),
    ] = "Id",
    next: Annotated[
        str | None,
        Field(description="Specify the start ID for the next page of service offers."),
    ] = None,
    limit: Annotated[
        int | str | None,
        Field(description="Specify the number of results to be returned.", default=2000),
    ] = 2000,
    filter: Annotated[
        str | None,
        Field(
            description="Limit the entities operated on by this endpoint by returning only the subset of entities that match the filter. The filter grammar is a subset of OData 4.0. <br> **Supported Fields:** `id`, `ServiceOfferId`, `workspaceId`, `serviceManagerProvisionId`, `serviceManagerId`, `serviceManagerInstanceId`, `status`, `organizationId`, `slug`. <br> **Supported operand:** `eq` <br> **Supported operations:** `and`\n\nExamples:\n  - serviceManagerId eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050' and serviceManagerInstanceId eq '62d242c7-7d53-448d-b7d0-baf0c591f024'\n    Return service provision for a given application ID and application instance ID.\n  - status eq 'PROVISION_INITIATED'\n    Return service provisions with a given status.\n  - organizationId eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050'\n    Return service provisions with a given organization ID.\n  - slug eq 'AC'\n    Return service provisions with a given slug.\n  - id eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050'\n    Return the service provision with a given ID.\n  - workspaceId eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050'\n    Return service provisions for a given workspace ID.\n  - serviceManagerProvisionId eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050'\n    Return service provisions for a given Application Customer ID.\n  - ServiceOfferId eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050' and region eq 'us-west'\n    Return service provisions for a given service offer ID and region.\n\n**Filter Syntax**: Use OData-style filters with the field names shown in the examples above. String values must be enclosed in single quotes."
        ),
    ] = None,
    unredacted: Annotated[
        str | None,
        Field(description="If true, returns the complete entry including sensitive fields.\n\nExample: true"),
    ] = None,
    all: Annotated[
        str | None,
        Field(
            description="If true, returns unredacted entries for all workspaces, including all provisioned service offers and their sensitive fields.\n\nExample: true"
        ),
    ] = None,
) -> list[dict[str, Any]]:
    """Retrieve a list of service provisions by applying filters.\nA service offer provides a distinct set of functionalities that can be independently identified and assigned access. Service offers are typically associated with roles and permissions, commerce, metering, quote-to-cash, and trial evaluations.\nA service provision occurs when a service offer is provisioned (added) to a workspace.\n<br><br>**Pagination**: This endpoint supports cursor-based pagination using the `next` query parameter. Provide the cursor in the `next` query parameter to retrieve the next page. \n

    Args:
        Hpe-workspace-id: The workspace ID. Required if the \"view all\" parameter is false.
        next: Specify the start ID for the next page of service offers.
        limit: Specify the number of results to be returned.
        filter: Limit the entities operated on by this endpoint by returning only the subset of entities that match the filter. The filter grammar is a subset of OData 4.0. <br> **Supported Fields:** `id`, `ServiceOfferId`, `workspaceId`, `serviceManagerProvisionId`, `serviceManagerId`, `serviceManagerInstanceId`, `status`, `organizationId`, `slug`. <br> **Supported operand:** `eq` <br> **Supported operations:** `and`\n\nExamples:\n  - serviceManagerId eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050' and serviceManagerInstanceId eq '62d242c7-7d53-448d-b7d0-baf0c591f024'\n    Return service provision for a given application ID and application instance ID.\n  - status eq 'PROVISION_INITIATED'\n    Return service provisions with a given status.\n  - organizationId eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050'\n    Return service provisions with a given organization ID.\n  - slug eq 'AC'\n    Return service provisions with a given slug.\n  - id eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050'\n    Return the service provision with a given ID.\n  - workspaceId eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050'\n    Return service provisions for a given workspace ID.\n  - serviceManagerProvisionId eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050'\n    Return service provisions for a given Application Customer ID.\n  - ServiceOfferId eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050' and region eq 'us-west'\n    Return service provisions for a given service offer ID and region.\n\n**Filter Syntax**: Use OData-style filters with the field names shown in the examples above. String values must be enclosed in single quotes.
        unredacted: If true, returns the complete entry including sensitive fields.\n\nExample: true
        all: If true, returns unredacted entries for all workspaces, including all provisioned service offers and their sensitive fields.\n\nExample: true
    Returns:
        API response data as a list containing one result dict.
    """
    http_client = ctx.request_context.lifespan_context.http_client

    # Build URL – URL-encode path parameters to prevent path-traversal attacks
    url = "/service-catalog/v1beta1/service-provisions"

    # Collect query / body parameters; skip values that were not provided
    params: dict[str, Any] = {}
    if hpe_workspace_id is not None and hpe_workspace_id is not ...:
        params["Hpe-workspace-id"] = hpe_workspace_id
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
    if unredacted is not None and unredacted is not ...:
        params["unredacted"] = unredacted
    if all is not None and all is not ...:
        params["all"] = all

    try:
        response_data = await http_client.get(url, params=params)
        return [{"success": True, "result": response_data}]

    except ValueError as exc:
        logger.error(f"Validation error in getserviceprovisions: {exc}")
        return [{"success": False, "error": "validation_error", "message": str(exc)}]

    except Exception as exc:
        logger.error(f"Error in getserviceprovisions: {exc}", exc_info=True)
        return [{"success": False, "error": "request_failed", "message": str(exc)}]
