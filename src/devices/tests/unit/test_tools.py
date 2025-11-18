# (c) Copyright 2025 Hewlett Packard Enterprise Development LP
"""Unit tests for generated tools."""

from __future__ import annotations

from typing import Any, Dict, List, cast

import pytest
from tools.implementations.getdevicesv1 import getdevicesv1Tool
from tools.implementations.getdevicebyidv1 import getdevicebyidv1Tool

# Build test matrix - de-duplicate by (name, path) to handle cases where
# multiple endpoints map to the same tool name
_TOOL_TEST_MATRIX_RAW = [
    {
        "class": getdevicesv1Tool,
        "name": "getdevicesv1",
        "method": "get",
        "path": "/devices/v1/devices",
        "parameters": [
            {
                "name": "filter",
                "in": "query",
                "required": False,
                "type": "str",
                "default": None,
            },
            {
                "name": "filter-tags",
                "in": "query",
                "required": False,
                "type": "str",
                "default": None,
            },
            {
                "name": "sort",
                "in": "query",
                "required": False,
                "type": "str",
                "default": None,
            },
            {
                "name": "select",
                "in": "query",
                "required": False,
                "type": "List[str]",
                "default": None,
            },
            {
                "name": "limit",
                "in": "query",
                "required": False,
                "type": "int",
                "default": 2000,
            },
            {
                "name": "offset",
                "in": "query",
                "required": False,
                "type": "int",
                "default": None,
            },
        ],
    },
    {
        "class": getdevicebyidv1Tool,
        "name": "getdevicebyidv1",
        "method": "get",
        "path": "/devices/v1/devices/{id}",
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
