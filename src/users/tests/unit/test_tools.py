# (c) Copyright 2025 Hewlett Packard Enterprise Development LP
"""Unit tests for generated tools."""

from __future__ import annotations

from typing import Any, Dict, List, cast

import pytest
from tools.implementations.get_users_identity_v1_users_get import get_users_identity_v1_users_getTool
from tools.implementations.get_user_detailed_identity_v1_users_id_get import (
    get_user_detailed_identity_v1_users_id_getTool,
)

# Build test matrix - de-duplicate by (name, path) to handle cases where
# multiple endpoints map to the same tool name
_TOOL_TEST_MATRIX_RAW = [
    {
        "class": get_users_identity_v1_users_getTool,
        "name": "get_users_identity_v1_users_get",
        "method": "get",
        "path": "/identity/v1/users",
        "parameters": [
            {
                "name": "filter",
                "in": "query",
                "required": False,
                "type": "str",
                "default": None,
            },
            {
                "name": "offset",
                "in": "query",
                "required": False,
                "type": "int",
                "default": None,
            },
            {
                "name": "limit",
                "in": "query",
                "required": False,
                "type": "int",
                "default": 300,
            },
        ],
    },
    {
        "class": get_user_detailed_identity_v1_users_id_getTool,
        "name": "get_user_detailed_identity_v1_users_id_get",
        "method": "get",
        "path": "/identity/v1/users/{id}",
        "parameters": [
            {
                "name": "id",
                "in": "path",
                "required": True,
                "type": "str",
                "default": None,
            },
        ],
    },
]

# De-duplicate by class name - keep last occurrence which overwrites the tool file
_seen_classes: set[type] = set()
TOOL_TEST_MATRIX: list[dict[str, Any]] = []
for tool_config in reversed(_TOOL_TEST_MATRIX_RAW):
    tool_class = cast(type, tool_config["class"])
    if tool_class not in _seen_classes:
        _seen_classes.add(tool_class)
        TOOL_TEST_MATRIX.insert(0, tool_config)


if not TOOL_TEST_MATRIX:
    pytest.skip("No endpoint tools were generated; skipping tool unit tests.", allow_module_level=True)


def _sample_value(parameter: dict[str, Any]) -> Any:
    if parameter["default"] is not None:
        return parameter["default"]

    match parameter["type"]:
        case "int":
            return 1
        case "float":
            return 1.0
        case "bool":
            return True
        case "list":
            return ["example"]
    return "example"


def _build_arguments(config: dict[str, Any]) -> dict[str, Any]:
    arguments: dict[str, Any] = {}
    for parameter in config["parameters"]:
        if parameter["required"]:
            arguments[parameter["name"]] = _sample_value(parameter)
    return arguments


@pytest.mark.asyncio
@pytest.mark.parametrize("config", TOOL_TEST_MATRIX, ids=lambda cfg: cfg["name"])
async def test_execute_success(config, mock_http_client):
    tool = config["class"](mock_http_client)
    getattr(mock_http_client, config["method"]).return_value = {"status": "ok"}

    result = await tool.execute(_build_arguments(config))

    assert result
    assert result[0]["success"] is True
    getattr(mock_http_client, config["method"]).assert_awaited_once()


REQUIRED_PARAM_CASES: List[Dict[str, Any]] = [
    config
    for config in TOOL_TEST_MATRIX
    if any(param["required"] for param in config["parameters"])  # type: ignore[attr-defined]
]


@pytest.mark.asyncio
@pytest.mark.parametrize("config", REQUIRED_PARAM_CASES, ids=lambda cfg: cfg["name"])
async def test_execute_requires_arguments(config, mock_http_client):
    if not any(param["required"] for param in config["parameters"]):
        pytest.skip("Tool has no required parameters.")

    tool = config["class"](mock_http_client)

    result = await tool.execute({})

    assert result[0]["success"] is False
    assert result[0]["error"] == "ValidationError"


@pytest.mark.asyncio
@pytest.mark.parametrize("config", TOOL_TEST_MATRIX, ids=lambda cfg: cfg["name"])
async def test_execute_handles_errors(config, mock_http_client):
    tool = config["class"](mock_http_client)
    getattr(mock_http_client, config["method"]).side_effect = RuntimeError("boom")

    result = await tool.execute(_build_arguments(config))

    assert result[0]["success"] is False
    assert result[0]["error"] == "RuntimeError"
