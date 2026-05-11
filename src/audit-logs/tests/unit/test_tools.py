# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""Unit tests for all generated tools."""

from __future__ import annotations

from typing import Any
from unittest.mock import AsyncMock, MagicMock

import pytest
from greenlake_audit_logs_mcp.tools.implementations.getauditlogs import getauditlogs as _impl_getauditlogs
from greenlake_audit_logs_mcp.tools.implementations.getauditlogdetails import (
    getauditlogdetails as _impl_getauditlogdetails,
)

_TOOL_TEST_MATRIX: list[dict[str, Any]] = [
    {
        "func": _impl_getauditlogs,
        "name": "getauditlogs",
        "method": "get",
    },
    {
        "func": _impl_getauditlogdetails,
        "name": "getauditlogdetails",
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
