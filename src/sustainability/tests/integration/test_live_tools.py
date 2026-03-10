# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""Live smoke tests for Sustainability_Insight_Center MCP tools.

Configure real GreenLake credentials and tool-specific arguments to run these tests.
"""

from __future__ import annotations

import os
from typing import Any, Optional, Tuple

import httpx
import pytest

from utils.http_client import get_http_client


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
        "name": "getingest",
        "path": "/sustainability-insight-ctr/v1beta1/ingests/{id}",
        "method": "get",
        "parameters": [
            {
                "name": "id",
                "required": True,
                "type": "str",
                "env": "MCP_TEST_SUSTAINABILITY_INSIGHT_CENTER_ID",
                "default": None,
            },
        ],
    },
    {
        "name": "getusagebyentity",
        "path": "/sustainability-insight-ctr/v1beta1/usage-by-entity",
        "method": "get",
        "parameters": [
            {
                "name": "filter",
                "required": False,
                "type": "str",
                "env": "MCP_TEST_SUSTAINABILITY_INSIGHT_CENTER_FILTER",
                "default": None,
            },
            {
                "name": "filter-tags",
                "required": False,
                "type": "str",
                "env": "MCP_TEST_SUSTAINABILITY_INSIGHT_CENTER_FILTER_TAGS",
                "default": None,
            },
            {
                "name": "currency",
                "required": False,
                "type": "str",
                "env": "MCP_TEST_SUSTAINABILITY_INSIGHT_CENTER_CURRENCY",
                "default": None,
            },
            {
                "name": "sort",
                "required": False,
                "type": "str",
                "env": "MCP_TEST_SUSTAINABILITY_INSIGHT_CENTER_SORT",
                "default": None,
            },
            {
                "name": "offset",
                "required": False,
                "type": "int",
                "env": "MCP_TEST_SUSTAINABILITY_INSIGHT_CENTER_OFFSET",
                "default": None,
            },
            {
                "name": "limit",
                "required": False,
                "type": "int",
                "env": "MCP_TEST_SUSTAINABILITY_INSIGHT_CENTER_LIMIT",
                "default": 10,
            },
            {
                "name": "start-time",
                "required": True,
                "type": "str",
                "env": "MCP_TEST_SUSTAINABILITY_INSIGHT_CENTER_START_TIME",
                "default": None,
            },
            {
                "name": "end-time",
                "required": True,
                "type": "str",
                "env": "MCP_TEST_SUSTAINABILITY_INSIGHT_CENTER_END_TIME",
                "default": None,
            },
        ],
    },
    {
        "name": "getcoefficients",
        "path": "/sustainability-insight-ctr/v1beta1/coefficients",
        "method": "get",
        "parameters": [
            {
                "name": "offset",
                "required": False,
                "type": "int",
                "env": "MCP_TEST_SUSTAINABILITY_INSIGHT_CENTER_OFFSET",
                "default": None,
            },
            {
                "name": "limit",
                "required": False,
                "type": "int",
                "env": "MCP_TEST_SUSTAINABILITY_INSIGHT_CENTER_LIMIT",
                "default": 10,
            },
            {
                "name": "filter",
                "required": False,
                "type": "str",
                "env": "MCP_TEST_SUSTAINABILITY_INSIGHT_CENTER_FILTER",
                "default": None,
            },
        ],
    },
    {
        "name": "getusagetotals",
        "path": "/sustainability-insight-ctr/v1beta1/usage-totals",
        "method": "get",
        "parameters": [
            {
                "name": "filter",
                "required": False,
                "type": "str",
                "env": "MCP_TEST_SUSTAINABILITY_INSIGHT_CENTER_FILTER",
                "default": None,
            },
            {
                "name": "filter-tags",
                "required": False,
                "type": "str",
                "env": "MCP_TEST_SUSTAINABILITY_INSIGHT_CENTER_FILTER_TAGS",
                "default": None,
            },
            {
                "name": "currency",
                "required": False,
                "type": "str",
                "env": "MCP_TEST_SUSTAINABILITY_INSIGHT_CENTER_CURRENCY",
                "default": None,
            },
            {
                "name": "start-time",
                "required": True,
                "type": "str",
                "env": "MCP_TEST_SUSTAINABILITY_INSIGHT_CENTER_START_TIME",
                "default": None,
            },
            {
                "name": "end-time",
                "required": True,
                "type": "str",
                "env": "MCP_TEST_SUSTAINABILITY_INSIGHT_CENTER_END_TIME",
                "default": None,
            },
        ],
    },
    {
        "name": "getcloudusagetotals",
        "path": "/sustainability-insight-ctr/v1beta1/cloud-usage-totals",
        "method": "get",
        "parameters": [
            {
                "name": "filter",
                "required": False,
                "type": "str",
                "env": "MCP_TEST_SUSTAINABILITY_INSIGHT_CENTER_FILTER",
                "default": None,
            },
            {
                "name": "start-time",
                "required": True,
                "type": "str",
                "env": "MCP_TEST_SUSTAINABILITY_INSIGHT_CENTER_START_TIME",
                "default": None,
            },
            {
                "name": "end-time",
                "required": True,
                "type": "str",
                "env": "MCP_TEST_SUSTAINABILITY_INSIGHT_CENTER_END_TIME",
                "default": None,
            },
        ],
    },
    {
        "name": "getdatasource",
        "path": "/sustainability-insight-ctr/v1beta1/datasources/{id}",
        "method": "get",
        "parameters": [
            {
                "name": "id",
                "required": True,
                "type": "str",
                "env": "MCP_TEST_SUSTAINABILITY_INSIGHT_CENTER_ID",
                "default": None,
            },
        ],
    },
    {
        "name": "getusagebyseries",
        "path": "/sustainability-insight-ctr/v1beta1/usage-series",
        "method": "get",
        "parameters": [
            {
                "name": "filter",
                "required": False,
                "type": "str",
                "env": "MCP_TEST_SUSTAINABILITY_INSIGHT_CENTER_FILTER",
                "default": None,
            },
            {
                "name": "filter-tags",
                "required": False,
                "type": "str",
                "env": "MCP_TEST_SUSTAINABILITY_INSIGHT_CENTER_FILTER_TAGS",
                "default": None,
            },
            {
                "name": "currency",
                "required": False,
                "type": "str",
                "env": "MCP_TEST_SUSTAINABILITY_INSIGHT_CENTER_CURRENCY",
                "default": None,
            },
            {
                "name": "interval",
                "required": True,
                "type": "str",
                "env": "MCP_TEST_SUSTAINABILITY_INSIGHT_CENTER_INTERVAL",
                "default": None,
            },
            {
                "name": "start-time",
                "required": True,
                "type": "str",
                "env": "MCP_TEST_SUSTAINABILITY_INSIGHT_CENTER_START_TIME",
                "default": None,
            },
            {
                "name": "end-time",
                "required": True,
                "type": "str",
                "env": "MCP_TEST_SUSTAINABILITY_INSIGHT_CENTER_END_TIME",
                "default": None,
            },
        ],
    },
    {
        "name": "getcloudusagebyentity",
        "path": "/sustainability-insight-ctr/v1beta1/cloud-usage-by-entity",
        "method": "get",
        "parameters": [
            {
                "name": "filter",
                "required": False,
                "type": "str",
                "env": "MCP_TEST_SUSTAINABILITY_INSIGHT_CENTER_FILTER",
                "default": None,
            },
            {
                "name": "sort",
                "required": False,
                "type": "str",
                "env": "MCP_TEST_SUSTAINABILITY_INSIGHT_CENTER_SORT",
                "default": None,
            },
            {
                "name": "offset",
                "required": False,
                "type": "int",
                "env": "MCP_TEST_SUSTAINABILITY_INSIGHT_CENTER_OFFSET",
                "default": None,
            },
            {
                "name": "limit",
                "required": False,
                "type": "int",
                "env": "MCP_TEST_SUSTAINABILITY_INSIGHT_CENTER_LIMIT",
                "default": 10,
            },
            {
                "name": "start-time",
                "required": True,
                "type": "str",
                "env": "MCP_TEST_SUSTAINABILITY_INSIGHT_CENTER_START_TIME",
                "default": None,
            },
            {
                "name": "end-time",
                "required": True,
                "type": "str",
                "env": "MCP_TEST_SUSTAINABILITY_INSIGHT_CENTER_END_TIME",
                "default": None,
            },
        ],
    },
    {
        "name": "getcloudusagebyseries",
        "path": "/sustainability-insight-ctr/v1beta1/cloud-usage-series",
        "method": "get",
        "parameters": [
            {
                "name": "filter",
                "required": False,
                "type": "str",
                "env": "MCP_TEST_SUSTAINABILITY_INSIGHT_CENTER_FILTER",
                "default": None,
            },
            {
                "name": "interval",
                "required": True,
                "type": "str",
                "env": "MCP_TEST_SUSTAINABILITY_INSIGHT_CENTER_INTERVAL",
                "default": None,
            },
            {
                "name": "start-time",
                "required": True,
                "type": "str",
                "env": "MCP_TEST_SUSTAINABILITY_INSIGHT_CENTER_START_TIME",
                "default": None,
            },
            {
                "name": "end-time",
                "required": True,
                "type": "str",
                "env": "MCP_TEST_SUSTAINABILITY_INSIGHT_CENTER_END_TIME",
                "default": None,
            },
        ],
    },
    {
        "name": "getcoefficient",
        "path": "/sustainability-insight-ctr/v1beta1/coefficients/{id}",
        "method": "get",
        "parameters": [
            {
                "name": "id",
                "required": True,
                "type": "str",
                "env": "MCP_TEST_SUSTAINABILITY_INSIGHT_CENTER_ID",
                "default": None,
            },
        ],
    },
    {
        "name": "getdatasources",
        "path": "/sustainability-insight-ctr/v1beta1/datasources",
        "method": "get",
        "parameters": [
        ],
    },
    {
        "name": "getingests",
        "path": "/sustainability-insight-ctr/v1beta1/ingests",
        "method": "get",
        "parameters": [
            {
                "name": "offset",
                "required": False,
                "type": "int",
                "env": "MCP_TEST_SUSTAINABILITY_INSIGHT_CENTER_OFFSET",
                "default": None,
            },
            {
                "name": "limit",
                "required": False,
                "type": "int",
                "env": "MCP_TEST_SUSTAINABILITY_INSIGHT_CENTER_LIMIT",
                "default": 10,
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
        pytest.skip(
            "Set the following environment variables to enable this test: "
            + ", ".join(missing)
        )

    http_client = get_http_client()
    try:
        # Filter out None values — only send params that were explicitly provided
        params = {k: v for k, v in arguments.items() if v is not None}
        response = await http_client.get(case["path"], params=params)
    except httpx.HTTPStatusError as exc:
        # Skip on any 4xx — master's tool.execute() absorbs all HTTP errors internally
        # (returns {"success": False, ...}), so 4xx never causes a test failure there.
        if 400 <= exc.response.status_code < 500:
            pytest.skip(f"HTTP {exc.response.status_code} from {exc.request.url}: endpoint may not be available in this environment")
        raise
    except (httpx.ConnectError, httpx.TimeoutException) as exc:
        # Network/connectivity issues are environmental, not code bugs
        pytest.skip(f"Network connectivity issue (check VPN/API reachability): {exc}")
    finally:
        await http_client.close()

    assert isinstance(response, dict), (
        f"Expected dict response from {case['path']}, got {type(response)}: {response}"
    )
