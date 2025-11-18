# (c) Copyright 2025 Hewlett Packard Enterprise Development LP
"""Live smoke tests for users MCP tools.

Configure real GreenLake credentials and tool-specific arguments to run these tests.
"""

from __future__ import annotations

import os
from typing import Any, Optional, Tuple

import pytest

from tools.registry import get_static_tools
from utils.http_client import UsersHttpClient


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
        "name": "get_users_identity_v1_users_get",
        "method": "get",
        "parameters": [
            {
                "name": "filter",
                "required": False,
                "type": "str",
                "env": "MCP_TEST_USERS_FILTER",
                "default": None,
            },
            {
                "name": "offset",
                "required": False,
                "type": "int",
                "env": "MCP_TEST_USERS_OFFSET",
                "default": None,
            },
            {
                "name": "limit",
                "required": False,
                "type": "int",
                "env": "MCP_TEST_USERS_LIMIT",
                "default": 300,
            },
        ],
    },
    {
        "name": "get_user_detailed_identity_v1_users_id_get",
        "method": "get",
        "parameters": [
            {
                "name": "id",
                "required": True,
                "type": "str",
                "env": "MCP_TEST_USERS_ID",
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
    arguments, missing = _build_arguments(case)
    if missing:
        pytest.skip("Set the following environment variables to enable this test: " + ", ".join(missing))

    tool_class = None
    for candidate in get_static_tools():
        if candidate.__name__.startswith(case["name"]):
            tool_class = candidate
            break

    if tool_class is None:
        pytest.skip(f"Tool implementation for {case['name']} not found.")

    http_client = UsersHttpClient()
    tool = tool_class(http_client)

    try:
        result = await tool.execute(arguments)
    finally:
        await http_client.close()

    assert isinstance(result, list)
    assert result and "success" in result[0]
