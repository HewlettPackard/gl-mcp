# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""Unit tests for generated tools."""

from __future__ import annotations

from typing import Any, Dict, List, cast

import pytest
from tools.implementations.getusagebyentity import getusagebyentityTool
from tools.implementations.getusagetotals import getusagetotalsTool
from tools.implementations.getusageseries import getusageseriesTool
from tools.implementations.getcloudusagebyentity import getcloudusagebyentityTool
from tools.implementations.getcloudusagetotals import getcloudusagetotalsTool
from tools.implementations.getcloudusageseries import getcloudusageseriesTool
from tools.implementations.getcoefficients import getcoefficientsTool
from tools.implementations.getcoefficientbyid import getcoefficientbyidTool
from tools.implementations.getingests import getingestsTool
from tools.implementations.getingestbyid import getingestbyidTool
from tools.implementations.getdatasources import getdatasourcesTool
from tools.implementations.getdatasourcebyid import getdatasourcebyidTool
from tools.implementations.forecastenergy import forecastenergyTool

_TOOL_TEST_MATRIX_RAW = [
    {
        "class": getusagebyentityTool,
        "name": "getusagebyentity",
        "method": "get",
        "path": "/sustainability-insight-ctr/v1beta1/usage-by-entity",
        "parameters": [
            {"name": "start-time", "in": "query", "required": True, "type": "str", "default": None},
            {"name": "end-time", "in": "query", "required": True, "type": "str", "default": None},
            {"name": "filter", "in": "query", "required": False, "type": "str", "default": None},
            {"name": "filter-tags", "in": "query", "required": False, "type": "str", "default": None},
            {"name": "currency", "in": "query", "required": False, "type": "str", "default": None},
            {"name": "sort", "in": "query", "required": False, "type": "str", "default": None},
            {"name": "offset", "in": "query", "required": False, "type": "int", "default": None},
            {"name": "limit", "in": "query", "required": False, "type": "int", "default": None},
        ],
    },
    {
        "class": getusagetotalsTool,
        "name": "getusagetotals",
        "method": "get",
        "path": "/sustainability-insight-ctr/v1beta1/usage-totals",
        "parameters": [
            {"name": "start-time", "in": "query", "required": True, "type": "str", "default": None},
            {"name": "end-time", "in": "query", "required": True, "type": "str", "default": None},
            {"name": "filter", "in": "query", "required": False, "type": "str", "default": None},
            {"name": "filter-tags", "in": "query", "required": False, "type": "str", "default": None},
            {"name": "currency", "in": "query", "required": False, "type": "str", "default": None},
        ],
    },
    {
        "class": getusageseriesTool,
        "name": "getusageseries",
        "method": "get",
        "path": "/sustainability-insight-ctr/v1beta1/usage-series",
        "parameters": [
            {"name": "start-time", "in": "query", "required": True, "type": "str", "default": None},
            {"name": "end-time", "in": "query", "required": True, "type": "str", "default": None},
            {"name": "interval", "in": "query", "required": True, "type": "str", "default": None},
            {"name": "filter", "in": "query", "required": False, "type": "str", "default": None},
            {"name": "filter-tags", "in": "query", "required": False, "type": "str", "default": None},
            {"name": "currency", "in": "query", "required": False, "type": "str", "default": None},
        ],
    },
    {
        "class": getcloudusagebyentityTool,
        "name": "getcloudusagebyentity",
        "method": "get",
        "path": "/sustainability-insight-ctr/v1beta1/cloud-usage-by-entity",
        "parameters": [
            {"name": "start-time", "in": "query", "required": True, "type": "str", "default": None},
            {"name": "end-time", "in": "query", "required": True, "type": "str", "default": None},
            {"name": "filter", "in": "query", "required": False, "type": "str", "default": None},
            {"name": "sort", "in": "query", "required": False, "type": "str", "default": None},
            {"name": "offset", "in": "query", "required": False, "type": "int", "default": None},
            {"name": "limit", "in": "query", "required": False, "type": "int", "default": None},
        ],
    },
    {
        "class": getcloudusagetotalsTool,
        "name": "getcloudusagetotals",
        "method": "get",
        "path": "/sustainability-insight-ctr/v1beta1/cloud-usage-totals",
        "parameters": [
            {"name": "start-time", "in": "query", "required": True, "type": "str", "default": None},
            {"name": "end-time", "in": "query", "required": True, "type": "str", "default": None},
            {"name": "filter", "in": "query", "required": False, "type": "str", "default": None},
        ],
    },
    {
        "class": getcloudusageseriesTool,
        "name": "getcloudusageseries",
        "method": "get",
        "path": "/sustainability-insight-ctr/v1beta1/cloud-usage-series",
        "parameters": [
            {"name": "start-time", "in": "query", "required": True, "type": "str", "default": None},
            {"name": "end-time", "in": "query", "required": True, "type": "str", "default": None},
            {"name": "interval", "in": "query", "required": True, "type": "str", "default": None},
            {"name": "filter", "in": "query", "required": False, "type": "str", "default": None},
        ],
    },
    {
        "class": getcoefficientsTool,
        "name": "getcoefficients",
        "method": "get",
        "path": "/sustainability-insight-ctr/v1beta1/coefficients",
        "parameters": [
            {"name": "filter", "in": "query", "required": False, "type": "str", "default": None},
            {"name": "filter-tags", "in": "query", "required": False, "type": "str", "default": None},
            {"name": "currency", "in": "query", "required": False, "type": "str", "default": None},
            {"name": "offset", "in": "query", "required": False, "type": "int", "default": None},
            {"name": "limit", "in": "query", "required": False, "type": "int", "default": None},
        ],
    },
    {
        "class": getcoefficientbyidTool,
        "name": "getcoefficientbyid",
        "method": "get",
        "path": "/sustainability-insight-ctr/v1beta1/coefficients/{id}",
        "parameters": [
            {"name": "id", "in": "path", "required": True, "type": "str", "default": None},
        ],
    },
    {
        "class": getingestsTool,
        "name": "getingests",
        "method": "get",
        "path": "/sustainability-insight-ctr/v1beta1/ingests",
        "parameters": [
            {"name": "offset", "in": "query", "required": False, "type": "int", "default": None},
            {"name": "limit", "in": "query", "required": False, "type": "int", "default": None},
        ],
    },
    {
        "class": getingestbyidTool,
        "name": "getingestbyid",
        "method": "get",
        "path": "/sustainability-insight-ctr/v1beta1/ingests/{id}",
        "parameters": [
            {"name": "id", "in": "path", "required": True, "type": "str", "default": None},
        ],
    },
    {
        "class": getdatasourcesTool,
        "name": "getdatasources",
        "method": "get",
        "path": "/sustainability-insight-ctr/v1beta1/datasources",
        "parameters": [
            {"name": "offset", "in": "query", "required": False, "type": "int", "default": None},
            {"name": "limit", "in": "query", "required": False, "type": "int", "default": None},
        ],
    },
    {
        "class": getdatasourcebyidTool,
        "name": "getdatasourcebyid",
        "method": "get",
        "path": "/sustainability-insight-ctr/v1beta1/datasources/{id}",
        "parameters": [
            {"name": "id", "in": "path", "required": True, "type": "str", "default": None},
        ],
    },
    {
        "class": forecastenergyTool,
        "name": "forecastenergy",
        "method": "post",
        "path": "/sustainability-insight-ctr/v1beta1/forecast/energy",
        "parameters": [
            {"name": "timePeriodMonths", "in": "body", "required": True, "type": "int", "default": None},
            {"name": "currencyCode", "in": "body", "required": True, "type": "str", "default": None},
        ],
    },
]

# De-duplicate by class name
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
    if any(param["required"] for param in config["parameters"])
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
