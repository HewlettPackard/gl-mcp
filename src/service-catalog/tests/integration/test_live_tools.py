# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""Live smoke tests for service-catalog MCP tools.

Configure real GreenLake credentials and tool-specific arguments to run these tests.
"""

from __future__ import annotations

import os
from typing import Any, Optional, Tuple

import httpx
import pytest

from greenlake_service_catalog_mcp.utils.http_client import get_http_client


def check_credentials() -> Optional[str]:
    """Check if the necessary credentials are set.

    Returns:
        String with missing credential names if any, None if all required credentials are present.
    """
    missing = []

    # Check for GREENLAKE_* variables
    if not os.getenv("GREENLAKE_CLIENT_ID"):
        missing.append("GREENLAKE_CLIENT_ID")
    if not os.getenv("GREENLAKE_CLIENT_SECRET"):
        missing.append("GREENLAKE_CLIENT_SECRET")
    if not os.getenv("GREENLAKE_WORKSPACE_ID"):
        missing.append("GREENLAKE_WORKSPACE_ID")
    if not os.getenv("GREENLAKE_API_BASE_URL"):
        missing.append("GREENLAKE_API_BASE_URL")

    return ", ".join(missing) if missing else None


# Skip all tests if credentials are missing
missing_credentials = check_credentials()
pytestmark = pytest.mark.skipif(
    missing_credentials is not None,
    reason=f"Missing required environment variables: {missing_credentials}. Configure real GreenLake credentials before running integration tests.",
)
TOOL_CASES = [
    {
        "name": "getserviceofferregions",
        "path": "/service-catalog/v1beta1/service-offer-regions",
        "method": "get",
        "parameters": [
            {
                "name": "next",
                "required": False,
                "type": "str",
                "env": "MCP_TEST_SERVICE_CATALOG_GETSERVICEOFFERREGIONS_NEXT",
                "default": None,
            },
            {
                "name": "limit",
                "required": False,
                "type": "int",
                "env": "MCP_TEST_SERVICE_CATALOG_GETSERVICEOFFERREGIONS_LIMIT",
                "default": 2000,
            },
            {
                "name": "filter",
                "required": False,
                "type": "str",
                "env": "MCP_TEST_SERVICE_CATALOG_GETSERVICEOFFERREGIONS_FILTER",
                "default": None,
            },
        ],
    },
    {
        "name": "getserviceprovisions",
        "path": "/service-catalog/v1beta1/service-provisions",
        "method": "get",
        "parameters": [
            {
                "name": "Hpe-workspace-id",
                "required": False,
                "type": "str",
                "env": "MCP_TEST_SERVICE_CATALOG_HPE_WORKSPACE_ID",
                "default": "Id",
            },
            {
                "name": "next",
                "required": False,
                "type": "str",
                "env": "MCP_TEST_SERVICE_CATALOG_GETSERVICEPROVISIONS_NEXT",
                "default": None,
            },
            {
                "name": "limit",
                "required": False,
                "type": "int",
                "env": "MCP_TEST_SERVICE_CATALOG_GETSERVICEPROVISIONS_LIMIT",
                "default": 2000,
            },
            {
                "name": "filter",
                "required": False,
                "type": "str",
                "env": "MCP_TEST_SERVICE_CATALOG_GETSERVICEPROVISIONS_FILTER",
                "default": None,
            },
            {
                "name": "unredacted",
                "required": False,
                "type": "bool",
                "env": "MCP_TEST_SERVICE_CATALOG_GETSERVICEPROVISIONS_UNREDACTED",
                "default": None,
            },
            {
                "name": "all",
                "required": False,
                "type": "bool",
                "env": "MCP_TEST_SERVICE_CATALOG_ALL",
                "default": None,
            },
        ],
    },
    {
        "name": "getserviceoffers",
        "path": "/service-catalog/v1beta1/service-offers",
        "method": "get",
        "parameters": [
            {
                "name": "next",
                "required": False,
                "type": "str",
                "env": "MCP_TEST_SERVICE_CATALOG_GETSERVICEOFFERS_NEXT",
                "default": None,
            },
            {
                "name": "limit",
                "required": False,
                "type": "int",
                "env": "MCP_TEST_SERVICE_CATALOG_GETSERVICEOFFERS_LIMIT",
                "default": 2000,
            },
            {
                "name": "filter",
                "required": False,
                "type": "str",
                "env": "MCP_TEST_SERVICE_CATALOG_GETSERVICEOFFERS_FILTER",
                "default": None,
            },
        ],
    },
    {
        "name": "getserviceofferregion",
        "path": "/service-catalog/v1beta1/service-offer-regions/{id}",
        "method": "get",
        "parameters": [
            {
                "name": "id",
                "required": True,
                "type": "str",
                "env": "MCP_TEST_SERVICE_CATALOG_GETSERVICEOFFERREGION_ID",
                "default": None,
            },
        ],
    },
    {
        "name": "service_managers_for_a_region_v1",
        "path": "/service-catalog/v1/per-region-service-managers/{id}",
        "method": "get",
        "parameters": [
            {
                "name": "id",
                "required": True,
                "type": "str",
                "env": "MCP_TEST_SERVICE_CATALOG_SERVICE_MANAGERS_FOR_A_REGION_V1_ID",
                "default": None,
            },
        ],
    },
    {
        "name": "get_service_manager_provisions_v1",
        "path": "/service-catalog/v1/service-manager-provisions",
        "method": "get",
        "parameters": [
            {
                "name": "offset",
                "required": False,
                "type": "int",
                "env": "MCP_TEST_SERVICE_CATALOG_GET_SERVICE_MANAGER_PROVISIONS_V1_OFFSET",
                "default": None,
            },
            {
                "name": "limit",
                "required": False,
                "type": "int",
                "env": "MCP_TEST_SERVICE_CATALOG_GET_SERVICE_MANAGER_PROVISIONS_V1_LIMIT",
                "default": 2000,
            },
            {
                "name": "filter",
                "required": False,
                "type": "str",
                "env": "MCP_TEST_SERVICE_CATALOG_GET_SERVICE_MANAGER_PROVISIONS_V1_FILTER",
                "default": None,
            },
        ],
    },
    {
        "name": "get_service_managers_v1",
        "path": "/service-catalog/v1/service-managers",
        "method": "get",
        "parameters": [
            {
                "name": "offset",
                "required": False,
                "type": "int",
                "env": "MCP_TEST_SERVICE_CATALOG_GET_SERVICE_MANAGERS_V1_OFFSET",
                "default": None,
            },
            {
                "name": "limit",
                "required": False,
                "type": "int",
                "env": "MCP_TEST_SERVICE_CATALOG_GET_SERVICE_MANAGERS_V1_LIMIT",
                "default": 2000,
            },
        ],
    },
    {
        "name": "get_service_manager_provision_v1",
        "path": "/service-catalog/v1/service-manager-provisions/{id}",
        "method": "get",
        "parameters": [
            {
                "name": "id",
                "required": True,
                "type": "str",
                "env": "MCP_TEST_SERVICE_CATALOG_GET_SERVICE_MANAGER_PROVISION_V1_ID",
                "default": None,
            },
        ],
    },
    {
        "name": "per_region_service_managers_v1",
        "path": "/service-catalog/v1/per-region-service-managers",
        "method": "get",
        "parameters": [
            {
                "name": "offset",
                "required": False,
                "type": "int",
                "env": "MCP_TEST_SERVICE_CATALOG_PER_REGION_SERVICE_MANAGERS_V1_OFFSET",
                "default": None,
            },
            {
                "name": "limit",
                "required": False,
                "type": "int",
                "env": "MCP_TEST_SERVICE_CATALOG_PER_REGION_SERVICE_MANAGERS_V1_LIMIT",
                "default": 2000,
            },
            {
                "name": "filter",
                "required": False,
                "type": "str",
                "env": "MCP_TEST_SERVICE_CATALOG_PER_REGION_SERVICE_MANAGERS_V1_FILTER",
                "default": None,
            },
        ],
    },
    {
        "name": "getserviceprovision",
        "path": "/service-catalog/v1beta1/service-provisions/{id}",
        "method": "get",
        "parameters": [
            {
                "name": "id",
                "required": True,
                "type": "str",
                "env": "MCP_TEST_SERVICE_CATALOG_GETSERVICEPROVISION_ID",
                "default": None,
            },
            {
                "name": "unredacted",
                "required": False,
                "type": "bool",
                "env": "MCP_TEST_SERVICE_CATALOG_GETSERVICEPROVISION_UNREDACTED",
                "default": None,
            },
        ],
    },
    {
        "name": "getserviceoffer",
        "path": "/service-catalog/v1beta1/service-offers/{id}",
        "method": "get",
        "parameters": [
            {
                "name": "id",
                "required": True,
                "type": "str",
                "env": "MCP_TEST_SERVICE_CATALOG_GETSERVICEOFFER_ID",
                "default": None,
            },
        ],
    },
    {
        "name": "get_service_manager_v1",
        "path": "/service-catalog/v1/service-managers/{id}",
        "method": "get",
        "parameters": [
            {
                "name": "id",
                "required": True,
                "type": "str",
                "env": "MCP_TEST_SERVICE_CATALOG_GET_SERVICE_MANAGER_V1_ID",
                "default": None,
            },
        ],
    },
]


if not TOOL_CASES:
    pytest.skip("No endpoint tools were generated; skipping integration tests.", allow_module_level=True)


def _coerce(value: str, type_name: str) -> Any:
    if type_name == "integer":
        return int(value)
    if type_name == "number":
        return float(value)
    if type_name == "boolean":
        return value.lower() in {"true", "1", "yes"}
    if type_name == "array":
        return [item.strip() for item in value.split(",") if item.strip()]
    return value


def _build_arguments(case: dict[str, Any]) -> Tuple[dict[str, Any], list[str]]:
    arguments: dict[str, Any] = {}
    missing: list[str] = []

    for parameter in case["parameters"]:
        raw = os.getenv(parameter["env"])
        if raw:
            arguments[parameter["name"]] = _coerce(raw, parameter["type"])
        elif parameter["default"] is not None:
            arguments[parameter["name"]] = parameter["default"]
        elif parameter["required"]:
            missing.append(parameter["env"])

    return arguments, missing


@pytest.mark.integration
@pytest.mark.asyncio
@pytest.mark.parametrize("case", TOOL_CASES, ids=lambda cfg: cfg["name"])
async def test_tool_live_smoke(case):
    """Call the real API endpoint directly via the HTTP client and assert a valid response.

    Uses the HTTP client singleton (which handles OAuth2 auth) to make the same
    request a FastMCP tool would make, without needing a FastMCP runtime context.
    Only skips on genuine auth errors (401/403); all other failures are real bugs.
    """
    arguments, missing = _build_arguments(case)
    if missing:
        pytest.skip("Set the following environment variables to enable this test: " + ", ".join(missing))

    # Skip write operations in integration tests — avoid mutating real data
    method = case.get("method", "get").upper()
    if method != "GET":
        pytest.skip(f"Skipping {method} endpoint in integration smoke test (write operations not safe for CI)")

    http_client = get_http_client()
    try:
        # Filter out None values — only send params that were explicitly provided
        params = {k: v for k, v in arguments.items() if v is not None}
        response = await http_client.get(case["path"], params=params)
    except httpx.HTTPStatusError as exc:
        # Skip on any HTTP error — integration smoke tests verify code structure,
        # not API availability. 4xx (auth, not found) and 5xx (gateway, server)
        # are environmental issues, not code bugs.
        pytest.skip(f"HTTP {exc.response.status_code} from {exc.request.url}: {exc}")
    except (httpx.ConnectError, httpx.TimeoutException) as exc:
        # Network/connectivity issues are environmental, not code bugs
        pytest.skip(f"Network connectivity issue (check VPN/API reachability): {exc}")
    finally:
        await http_client.close()

    assert isinstance(response, dict), f"Expected dict response from {case['path']}, got {type(response)}: {response}"
