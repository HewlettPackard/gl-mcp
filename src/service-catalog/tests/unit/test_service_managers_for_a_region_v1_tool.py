# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
Test for service_managers_for_a_region_v1 tool in service-catalog MCP server.

Tests the service_managers_for_a_region_v1 FastMCP tool function directly by mocking
the request Context so no real HTTP calls are made.
"""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock

import pytest

from greenlake_service_catalog_mcp.tools.implementations.service_managers_for_a_region_v1 import (
    service_managers_for_a_region_v1 as _impl_service_managers_for_a_region_v1,
)


def _make_mock_ctx(http_client: AsyncMock | None = None) -> MagicMock:
    """Return a MagicMock that looks like a FastMCP Context.

    The http_client is accessible via
    ``ctx.request_context.lifespan_context.http_client``.
    """
    ctx = MagicMock()
    ctx.request_context.lifespan_context.http_client = http_client or AsyncMock()
    return ctx


class TestServiceManagersForARegionV1Tool:
    """Test cases for the service_managers_for_a_region_v1 tool function."""

    @pytest.mark.asyncio
    async def test_returns_list(self):
        """Tool must always return a list containing one result dict."""
        ctx = _make_mock_ctx()
        ctx.request_context.lifespan_context.http_client.get.return_value = {}

        result = await _impl_service_managers_for_a_region_v1(ctx)

        assert isinstance(result, list)
        assert len(result) == 1

    @pytest.mark.asyncio
    async def test_success_response(self):
        """Successful API call must produce success=True with the API payload."""
        api_response = {"items": [{"id": "item-1", "name": "Test"}], "total": 1}
        ctx = _make_mock_ctx()
        ctx.request_context.lifespan_context.http_client.get.return_value = api_response

        result = await _impl_service_managers_for_a_region_v1(ctx)

        assert result[0]["success"] is True
        assert result[0]["result"] == api_response

    @pytest.mark.asyncio
    async def test_api_error_returns_failure(self):
        """Exceptions raised by the HTTP client must be caught and returned as failure dicts."""
        ctx = _make_mock_ctx()
        ctx.request_context.lifespan_context.http_client.get.side_effect = Exception("API Error")

        result = await _impl_service_managers_for_a_region_v1(ctx)

        assert result[0]["success"] is False
        assert "API Error" in result[0]["message"]

    @pytest.mark.asyncio
    async def test_http_client_called_once(self):
        """The HTTP client must be called exactly once per tool invocation."""
        ctx = _make_mock_ctx()
        ctx.request_context.lifespan_context.http_client.get.return_value = {}

        await _impl_service_managers_for_a_region_v1(ctx)

        ctx.request_context.lifespan_context.http_client.get.assert_called_once()
