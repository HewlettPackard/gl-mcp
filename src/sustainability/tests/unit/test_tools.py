# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""Unit tests for all generated tools."""

from __future__ import annotations

from typing import Any
from unittest.mock import AsyncMock, MagicMock

import pytest
from tools.implementations.getingest import getingest
from tools.implementations.getusagebyentity import getusagebyentity
from tools.implementations.getcoefficients import getcoefficients
from tools.implementations.getusagetotals import getusagetotals
from tools.implementations.getcloudusagetotals import getcloudusagetotals
from tools.implementations.getdatasource import getdatasource
from tools.implementations.getusagebyseries import getusagebyseries
from tools.implementations.getcloudusagebyentity import getcloudusagebyentity
from tools.implementations.getcloudusagebyseries import getcloudusagebyseries
from tools.implementations.getcoefficient import getcoefficient
from tools.implementations.getdatasources import getdatasources
from tools.implementations.getingests import getingests

_TOOL_TEST_MATRIX: list[dict[str, Any]] = [
    {
        "func": getingest,
        "name": "getingest",
        "method": "get",
    },
    {
        "func": getusagebyentity,
        "name": "getusagebyentity",
        "method": "get",
    },
    {
        "func": getcoefficients,
        "name": "getcoefficients",
        "method": "get",
    },
    {
        "func": getusagetotals,
        "name": "getusagetotals",
        "method": "get",
    },
    {
        "func": getcloudusagetotals,
        "name": "getcloudusagetotals",
        "method": "get",
    },
    {
        "func": getdatasource,
        "name": "getdatasource",
        "method": "get",
    },
    {
        "func": getusagebyseries,
        "name": "getusagebyseries",
        "method": "get",
    },
    {
        "func": getcloudusagebyentity,
        "name": "getcloudusagebyentity",
        "method": "get",
    },
    {
        "func": getcloudusagebyseries,
        "name": "getcloudusagebyseries",
        "method": "get",
    },
    {
        "func": getcoefficient,
        "name": "getcoefficient",
        "method": "get",
    },
    {
        "func": getdatasources,
        "name": "getdatasources",
        "method": "get",
    },
    {
        "func": getingests,
        "name": "getingests",
        "method": "get",
    },
]


if not _TOOL_TEST_MATRIX:
    pytest.skip("No endpoint tools were generated; skipping tool unit tests.", allow_module_level=True)


def _make_mock_ctx(http_client: AsyncMock | None = None) -> MagicMock:
    """Return a MagicMock that looks like a FastMCP Context."""
    ctx = MagicMock()
    ctx.request_context.lifespan_context.http_client = http_client or AsyncMock()
    return ctx


@pytest.mark.asyncio
@pytest.mark.parametrize("config", _TOOL_TEST_MATRIX, ids=lambda c: c["name"])
async def test_execute_success(config: dict[str, Any]) -> None:
    """Every tool must return a success result when the API responds normally."""
    mock_client = AsyncMock()
    getattr(mock_client, config["method"]).return_value = {"status": "ok"}
    ctx = _make_mock_ctx(mock_client)

    result = await config["func"](ctx)

    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0]["success"] is True
    getattr(mock_client, config["method"]).assert_awaited_once()


@pytest.mark.asyncio
@pytest.mark.parametrize("config", _TOOL_TEST_MATRIX, ids=lambda c: c["name"])
async def test_execute_handles_errors(config: dict[str, Any]) -> None:
    """Every tool must catch exceptions and return a failure dict."""
    mock_client = AsyncMock()
    getattr(mock_client, config["method"]).side_effect = RuntimeError("boom")
    ctx = _make_mock_ctx(mock_client)

    result = await config["func"](ctx)

    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0]["success"] is False
    assert "boom" in result[0]["message"]
