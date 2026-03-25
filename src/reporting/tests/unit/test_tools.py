# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""Unit tests for all generated tools."""

from __future__ import annotations

from typing import Any
from unittest.mock import AsyncMock, MagicMock

import pytest
from tools.implementations.get_reporting_v1_report_exports_metadata import get_reporting_v1_report_exports_metadata
from tools.implementations.getreportingstatuses import getreportingstatuses
from tools.implementations.getreportingstatusbyid import getreportingstatusbyid

_TOOL_TEST_MATRIX: list[dict[str, Any]] = [
    {
        "func": get_reporting_v1_report_exports_metadata,
        "name": "get_reporting_v1_report_exports_metadata",
        "method": "get",
    },
    {
        "func": getreportingstatuses,
        "name": "getreportingstatuses",
        "method": "get",
    },
    {
        "func": getreportingstatusbyid,
        "name": "getreportingstatusbyid",
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
