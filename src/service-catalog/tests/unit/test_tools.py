# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""Unit tests for all generated tools."""

from __future__ import annotations

from typing import Any
from unittest.mock import AsyncMock, MagicMock

import pytest
from greenlake_service_catalog_mcp.tools.implementations.getserviceofferregions import (
    getserviceofferregions as _impl_getserviceofferregions,
)
from greenlake_service_catalog_mcp.tools.implementations.getserviceprovisions import (
    getserviceprovisions as _impl_getserviceprovisions,
)
from greenlake_service_catalog_mcp.tools.implementations.getserviceoffers import (
    getserviceoffers as _impl_getserviceoffers,
)
from greenlake_service_catalog_mcp.tools.implementations.getserviceofferregion import (
    getserviceofferregion as _impl_getserviceofferregion,
)
from greenlake_service_catalog_mcp.tools.implementations.service_managers_for_a_region_v1 import (
    service_managers_for_a_region_v1 as _impl_service_managers_for_a_region_v1,
)
from greenlake_service_catalog_mcp.tools.implementations.get_service_manager_provisions_v1 import (
    get_service_manager_provisions_v1 as _impl_get_service_manager_provisions_v1,
)
from greenlake_service_catalog_mcp.tools.implementations.get_service_managers_v1 import (
    get_service_managers_v1 as _impl_get_service_managers_v1,
)
from greenlake_service_catalog_mcp.tools.implementations.get_service_manager_provision_v1 import (
    get_service_manager_provision_v1 as _impl_get_service_manager_provision_v1,
)
from greenlake_service_catalog_mcp.tools.implementations.per_region_service_managers_v1 import (
    per_region_service_managers_v1 as _impl_per_region_service_managers_v1,
)
from greenlake_service_catalog_mcp.tools.implementations.getserviceprovision import (
    getserviceprovision as _impl_getserviceprovision,
)
from greenlake_service_catalog_mcp.tools.implementations.getserviceoffer import getserviceoffer as _impl_getserviceoffer
from greenlake_service_catalog_mcp.tools.implementations.get_service_manager_v1 import (
    get_service_manager_v1 as _impl_get_service_manager_v1,
)

_TOOL_TEST_MATRIX: list[dict[str, Any]] = [
    {
        "func": _impl_getserviceofferregions,
        "name": "getserviceofferregions",
        "method": "get",
    },
    {
        "func": _impl_getserviceprovisions,
        "name": "getserviceprovisions",
        "method": "get",
    },
    {
        "func": _impl_getserviceoffers,
        "name": "getserviceoffers",
        "method": "get",
    },
    {
        "func": _impl_getserviceofferregion,
        "name": "getserviceofferregion",
        "method": "get",
    },
    {
        "func": _impl_service_managers_for_a_region_v1,
        "name": "service_managers_for_a_region_v1",
        "method": "get",
    },
    {
        "func": _impl_get_service_manager_provisions_v1,
        "name": "get_service_manager_provisions_v1",
        "method": "get",
    },
    {
        "func": _impl_get_service_managers_v1,
        "name": "get_service_managers_v1",
        "method": "get",
    },
    {
        "func": _impl_get_service_manager_provision_v1,
        "name": "get_service_manager_provision_v1",
        "method": "get",
    },
    {
        "func": _impl_per_region_service_managers_v1,
        "name": "per_region_service_managers_v1",
        "method": "get",
    },
    {
        "func": _impl_getserviceprovision,
        "name": "getserviceprovision",
        "method": "get",
    },
    {
        "func": _impl_getserviceoffer,
        "name": "getserviceoffer",
        "method": "get",
    },
    {
        "func": _impl_get_service_manager_v1,
        "name": "get_service_manager_v1",
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
