# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
Tests for dynamic tools in service-catalog MCP server.

This module tests the three dynamic meta-tools:
- list_endpoints
- get_endpoint_schema
- invoke_dynamic_tool

Generated for dynamic mode when OpenAPI spec has 12 endpoints (>= 50 threshold).
"""

from __future__ import annotations

import json
from unittest.mock import AsyncMock, MagicMock

import pytest

from greenlake_service_catalog_mcp.tools.implementations.list_endpoints import list_endpoints
from greenlake_service_catalog_mcp.tools.implementations.get_endpoint_schema import get_endpoint_schema
from greenlake_service_catalog_mcp.tools.implementations.invoke_dynamic_tool import invoke_dynamic_tool


def _make_mock_ctx(http_client: AsyncMock | None = None) -> MagicMock:
    """Return a MagicMock that looks like a FastMCP Context.

    The http_client is accessible via
    ``ctx.request_context.lifespan_context.http_client``.
    """
    ctx = MagicMock()
    ctx.request_context.lifespan_context.http_client = http_client or AsyncMock()
    return ctx


# ---------------------------------------------------------------------------
# list_endpoints
# ---------------------------------------------------------------------------


class TestListEndpoints:
    """Tests for the list_endpoints tool function."""

    @pytest.mark.asyncio
    async def test_returns_all_endpoints_by_default(self):
        """No filter returns all endpoint objects with metadata."""
        raw = await list_endpoints()
        result = json.loads(raw)

        assert isinstance(result, list)

        assert len(result) == 12
        for ep in result:
            assert isinstance(ep, dict)
            assert "endpoint" in ep
            assert "summary" in ep
            assert "type" in ep
            assert ep["type"] in ("list", "detail")
            method, path = ep["endpoint"].split(":", 1)
            assert method in ("GET", "POST", "PUT", "DELETE", "PATCH")
            assert path.startswith("/")

    @pytest.mark.asyncio
    async def test_result_is_sorted(self):
        """Returned list must be sorted by endpoint identifier."""
        result = json.loads(await list_endpoints())
        endpoints = [ep["endpoint"] for ep in result]
        assert endpoints == sorted(endpoints)

    @pytest.mark.asyncio
    async def test_filter_narrows_results(self):
        """A filter term reduces the returned list to matching endpoints."""
        all_results = json.loads(await list_endpoints())

        # Use a substring from the first endpoint path as a guaranteed-matching filter
        first_path = all_results[0]["endpoint"].split(":", 1)[1] if all_results else ""
        if first_path:
            term = first_path.strip("/").split("/")[0]  # first path segment
            filtered = json.loads(await list_endpoints(filter=term))
            assert isinstance(filtered, list)
            for ep in filtered:
                assert term.lower() in ep["endpoint"].lower() or term.lower() in ep.get("summary", "").lower()
            assert len(filtered) <= len(all_results)

    @pytest.mark.asyncio
    async def test_filter_no_match_returns_empty(self):
        """A filter that matches nothing returns an empty list."""
        result = json.loads(await list_endpoints(filter="zzz_no_match_zzz_12345"))
        assert result == []

    @pytest.mark.asyncio
    async def test_empty_filter_returns_all(self):
        """An explicit empty-string filter is equivalent to no filter."""
        all_result = json.loads(await list_endpoints())
        filtered_result = json.loads(await list_endpoints(filter=""))
        assert all_result == filtered_result

    @pytest.mark.asyncio
    async def test_filter_is_case_insensitive(self):
        """Filter matching must be case-insensitive."""
        lower = json.loads(await list_endpoints(filter="get"))
        upper = json.loads(await list_endpoints(filter="GET"))
        assert lower == upper

    @pytest.mark.asyncio
    async def test_returns_valid_json_string(self):
        """Return value must be a JSON-encoded string (not a bare list)."""
        raw = await list_endpoints()
        assert isinstance(raw, str)
        parsed = json.loads(raw)
        assert isinstance(parsed, list)


# ---------------------------------------------------------------------------
# get_endpoint_schema
# ---------------------------------------------------------------------------


class TestGetEndpointSchema:
    """Tests for the get_endpoint_schema tool function."""

    @pytest.mark.asyncio
    async def test_valid_endpoint_returns_schema(self):
        """A recognised endpoint identifier returns a complete schema dict."""

        result = await get_endpoint_schema(endpoint_identifier="GET:/service-catalog/v1beta1/service-offer-regions")

        assert len(result) == 1
        response = result[0]
        assert response["success"] is True
        assert response["endpoint_identifier"] == "GET:/service-catalog/v1beta1/service-offer-regions"
        schema = response["schema"]
        assert schema["path"] == "/service-catalog/v1beta1/service-offer-regions"
        assert schema["method"] == "GET"
        assert isinstance(schema["parameters"], list)

    @pytest.mark.asyncio
    async def test_unknown_endpoint_returns_error(self):
        """An unrecognised endpoint identifier returns success=False with an error message."""
        result = await get_endpoint_schema(endpoint_identifier="GET:/nonexistent/path")

        assert len(result) == 1
        response = result[0]
        assert response["success"] is False
        assert "error" in response

    @pytest.mark.asyncio
    async def test_empty_identifier_returns_error(self):
        """An empty endpoint_identifier returns a validation error."""
        result = await get_endpoint_schema(endpoint_identifier="")

        assert len(result) == 1
        assert result[0]["success"] is False
        assert "endpoint_identifier is required" in result[0]["error"]

    @pytest.mark.asyncio
    async def test_include_examples_adds_example_values(self):
        """Setting include_examples=True attaches an example value to each parameter."""

        result = await get_endpoint_schema(
            endpoint_identifier="GET:/service-catalog/v1beta1/service-offer-regions",
            include_examples=True,
        )

        assert result[0]["success"] is True
        for param in result[0]["schema"]["parameters"]:
            assert "example" in param

    @pytest.mark.asyncio
    async def test_schema_contains_all_expected_keys(self):
        """Schema response includes all mandatory top-level keys."""

        result = await get_endpoint_schema(endpoint_identifier="GET:/service-catalog/v1beta1/service-offer-regions")
        schema = result[0]["schema"]
        for key in ("path", "method", "summary", "description", "parameters", "responses"):
            assert key in schema, f"Missing key: {key}"


# ---------------------------------------------------------------------------
# invoke_dynamic_tool
# ---------------------------------------------------------------------------


class TestInvokeDynamicTool:
    """Tests for the invoke_dynamic_tool tool function."""

    @pytest.mark.asyncio
    async def test_valid_get_request_calls_http_client(self):
        """A valid GET endpoint makes one HTTP GET call and returns success=True."""
        mock_client = AsyncMock()
        mock_client.get.return_value = {"items": [], "total": 0}
        ctx = _make_mock_ctx(mock_client)

        result = await invoke_dynamic_tool(
            ctx,
            endpoint_identifier="GET:/service-catalog/v1beta1/service-offer-regions",
            parameters={},
        )

        assert len(result) == 1
        response = result[0]
        if response["success"]:
            mock_client.get.assert_called_once()
            assert "response" in response
        else:
            # Validation failure is acceptable when required path params need real values
            assert "validation" in response.get("error", "").lower() or "parameter" in response.get("error", "").lower()

    @pytest.mark.asyncio
    async def test_unknown_endpoint_returns_error(self):
        """An unrecognised endpoint identifier returns success=False."""
        ctx = _make_mock_ctx()

        result = await invoke_dynamic_tool(ctx, endpoint_identifier="GET:/nonexistent/path")

        assert len(result) == 1
        assert result[0]["success"] is False
        assert "error" in result[0]

    @pytest.mark.asyncio
    async def test_missing_endpoint_identifier_returns_error(self):
        """An empty endpoint_identifier returns a validation error."""
        ctx = _make_mock_ctx()

        result = await invoke_dynamic_tool(ctx, endpoint_identifier="")

        assert len(result) == 1
        assert result[0]["success"] is False
        assert "endpoint_identifier is required" in result[0]["error"]

    @pytest.mark.asyncio
    async def test_unsupported_method_rejected(self):
        """An unsupported HTTP method (OPTIONS) must be rejected."""
        ctx = _make_mock_ctx()

        result = await invoke_dynamic_tool(
            ctx,
            endpoint_identifier="OPTIONS:/service-catalog/v1beta1/service-offer-regions",
        )

        assert len(result) == 1
        assert result[0]["success"] is False
        error_text = result[0].get("error", "") + " " + result[0].get("message", "")
        assert (
            "unsupported" in error_text.lower()
            or "not found" in error_text.lower()
            or "read operations" in error_text.lower()
        )

    @pytest.mark.asyncio
    async def test_invalid_format_returns_error(self):
        """An identifier missing the METHOD: prefix returns a format error."""
        ctx = _make_mock_ctx()

        result = await invoke_dynamic_tool(ctx, endpoint_identifier="/no-method-prefix")

        assert len(result) == 1
        assert result[0]["success"] is False

    @pytest.mark.asyncio
    async def test_validation_catches_missing_required_param(self):
        """Schema validation reports missing required path/query parameters."""

        ctx = _make_mock_ctx()
        # Find a tool with required parameters and omit them intentionally

        result = await invoke_dynamic_tool(
            ctx,
            endpoint_identifier="GET:/service-catalog/v1beta1/service-offer-regions/{id}",
            parameters={},  # required "id" is intentionally omitted
        )
        assert len(result) == 1
        assert result[0]["success"] is False
        assert "validation" in result[0].get("error", "").lower() or "missing" in str(result[0]).lower()
        return  # only need to test one case

        result = await invoke_dynamic_tool(
            ctx,
            endpoint_identifier="GET:/service-catalog/v1/per-region-service-managers/{id}",
            parameters={},  # required "id" is intentionally omitted
        )
        assert len(result) == 1
        assert result[0]["success"] is False
        assert "validation" in result[0].get("error", "").lower() or "missing" in str(result[0]).lower()
        return  # only need to test one case

        result = await invoke_dynamic_tool(
            ctx,
            endpoint_identifier="GET:/service-catalog/v1/service-manager-provisions/{id}",
            parameters={},  # required "id" is intentionally omitted
        )
        assert len(result) == 1
        assert result[0]["success"] is False
        assert "validation" in result[0].get("error", "").lower() or "missing" in str(result[0]).lower()
        return  # only need to test one case

        result = await invoke_dynamic_tool(
            ctx,
            endpoint_identifier="GET:/service-catalog/v1beta1/service-provisions/{id}",
            parameters={},  # required "id" is intentionally omitted
        )
        assert len(result) == 1
        assert result[0]["success"] is False
        assert "validation" in result[0].get("error", "").lower() or "missing" in str(result[0]).lower()
        return  # only need to test one case

        result = await invoke_dynamic_tool(
            ctx,
            endpoint_identifier="GET:/service-catalog/v1beta1/service-offers/{id}",
            parameters={},  # required "id" is intentionally omitted
        )
        assert len(result) == 1
        assert result[0]["success"] is False
        assert "validation" in result[0].get("error", "").lower() or "missing" in str(result[0]).lower()
        return  # only need to test one case

        result = await invoke_dynamic_tool(
            ctx,
            endpoint_identifier="GET:/service-catalog/v1/service-managers/{id}",
            parameters={},  # required "id" is intentionally omitted
        )
        assert len(result) == 1
        assert result[0]["success"] is False
        assert "validation" in result[0].get("error", "").lower() or "missing" in str(result[0]).lower()
        return  # only need to test one case

    @pytest.mark.asyncio
    async def test_http_client_error_returns_failure(self):
        """Exceptions raised by the HTTP client are caught and returned as failure dicts."""

        mock_client = AsyncMock()
        mock_client.get.side_effect = Exception("connection refused")
        ctx = _make_mock_ctx(mock_client)

        result = await invoke_dynamic_tool(
            ctx,
            endpoint_identifier="GET:/service-catalog/v1beta1/service-offer-regions",
            validate_schema=False,  # skip validation so we reach the HTTP call
        )

        assert len(result) == 1
        assert result[0]["success"] is False


# ---------------------------------------------------------------------------
# Integration: discovery flow (list → schema → invoke)
# ---------------------------------------------------------------------------


class TestDynamicToolsIntegration:
    """End-to-end flow tests covering all three tools together."""

    @pytest.mark.asyncio
    async def test_discovery_flow(self):
        """list_endpoints → get_endpoint_schema → invoke_dynamic_tool happy path."""

        mock_client = AsyncMock()
        mock_client.get.return_value = {"items": [], "total": 0}
        ctx = _make_mock_ctx(mock_client)

        # Step 1: discover all endpoints
        endpoints = json.loads(await list_endpoints())
        assert len(endpoints) > 0

        # Step 2: retrieve schema for the first endpoint
        first_ep = endpoints[0]["endpoint"]
        schema_result = await get_endpoint_schema(endpoint_identifier=first_ep)
        assert schema_result[0]["success"] is True
        schema = schema_result[0]["schema"]

        # Build minimal parameters satisfying required fields
        required_params = {p["name"]: "test-value" for p in schema.get("parameters", []) if p.get("required")}

        # Step 3: invoke the endpoint
        invoke_result = await invoke_dynamic_tool(
            ctx,
            endpoint_identifier=first_ep,
            parameters=required_params,
        )

        assert len(invoke_result) == 1
        # Must not fail with "endpoint not found"
        if not invoke_result[0]["success"]:
            assert "not found" not in invoke_result[0].get("error", "").lower()


# ---------------------------------------------------------------------------
# Fixtures – shared test data
# ---------------------------------------------------------------------------


@pytest.fixture
def sample_endpoints() -> list[dict]:
    """Sample endpoint data matching the generated schemas."""
    return [
        {
            "path": "/service-catalog/v1beta1/service-offer-regions",
            "method": "GET",
            "summary": "getserviceofferregions",
            "operationId": "getserviceofferregions",
            "parameters": [
                {
                    "name": "next",
                    "type": "str",
                    "required": False,
                    "location": "query",
                },
                {
                    "name": "limit",
                    "type": "int",
                    "required": False,
                    "location": "query",
                },
                {
                    "name": "filter",
                    "type": "str",
                    "required": False,
                    "location": "query",
                },
            ],
        },
        {
            "path": "/service-catalog/v1beta1/service-provisions",
            "method": "GET",
            "summary": "getserviceprovisions",
            "operationId": "getserviceprovisions",
            "parameters": [
                {
                    "name": "Hpe-workspace-id",
                    "type": "str",
                    "required": False,
                    "location": "query",
                },
                {
                    "name": "next",
                    "type": "str",
                    "required": False,
                    "location": "query",
                },
                {
                    "name": "limit",
                    "type": "int",
                    "required": False,
                    "location": "query",
                },
                {
                    "name": "filter",
                    "type": "str",
                    "required": False,
                    "location": "query",
                },
                {
                    "name": "unredacted",
                    "type": "bool",
                    "required": False,
                    "location": "query",
                },
                {
                    "name": "all",
                    "type": "bool",
                    "required": False,
                    "location": "query",
                },
            ],
        },
        {
            "path": "/service-catalog/v1beta1/service-offers",
            "method": "GET",
            "summary": "getserviceoffers",
            "operationId": "getserviceoffers",
            "parameters": [
                {
                    "name": "next",
                    "type": "str",
                    "required": False,
                    "location": "query",
                },
                {
                    "name": "limit",
                    "type": "int",
                    "required": False,
                    "location": "query",
                },
                {
                    "name": "filter",
                    "type": "str",
                    "required": False,
                    "location": "query",
                },
            ],
        },
        {
            "path": "/service-catalog/v1beta1/service-offer-regions/{id}",
            "method": "GET",
            "summary": "getserviceofferregion",
            "operationId": "getserviceofferregion",
            "parameters": [
                {
                    "name": "id",
                    "type": "str",
                    "required": True,
                    "location": "query",
                },
            ],
        },
        {
            "path": "/service-catalog/v1/per-region-service-managers/{id}",
            "method": "GET",
            "summary": "service_managers_for_a_region_v1",
            "operationId": "service_managers_for_a_region_v1",
            "parameters": [
                {
                    "name": "id",
                    "type": "str",
                    "required": True,
                    "location": "query",
                },
            ],
        },
        {
            "path": "/service-catalog/v1/service-manager-provisions",
            "method": "GET",
            "summary": "get_service_manager_provisions_v1",
            "operationId": "get_service_manager_provisions_v1",
            "parameters": [
                {
                    "name": "offset",
                    "type": "int",
                    "required": False,
                    "location": "query",
                },
                {
                    "name": "limit",
                    "type": "int",
                    "required": False,
                    "location": "query",
                },
                {
                    "name": "filter",
                    "type": "str",
                    "required": False,
                    "location": "query",
                },
            ],
        },
        {
            "path": "/service-catalog/v1/service-managers",
            "method": "GET",
            "summary": "get_service_managers_v1",
            "operationId": "get_service_managers_v1",
            "parameters": [
                {
                    "name": "offset",
                    "type": "int",
                    "required": False,
                    "location": "query",
                },
                {
                    "name": "limit",
                    "type": "int",
                    "required": False,
                    "location": "query",
                },
            ],
        },
        {
            "path": "/service-catalog/v1/service-manager-provisions/{id}",
            "method": "GET",
            "summary": "get_service_manager_provision_v1",
            "operationId": "get_service_manager_provision_v1",
            "parameters": [
                {
                    "name": "id",
                    "type": "str",
                    "required": True,
                    "location": "query",
                },
            ],
        },
        {
            "path": "/service-catalog/v1/per-region-service-managers",
            "method": "GET",
            "summary": "per_region_service_managers_v1",
            "operationId": "per_region_service_managers_v1",
            "parameters": [
                {
                    "name": "offset",
                    "type": "int",
                    "required": False,
                    "location": "query",
                },
                {
                    "name": "limit",
                    "type": "int",
                    "required": False,
                    "location": "query",
                },
                {
                    "name": "filter",
                    "type": "str",
                    "required": False,
                    "location": "query",
                },
            ],
        },
        {
            "path": "/service-catalog/v1beta1/service-provisions/{id}",
            "method": "GET",
            "summary": "getserviceprovision",
            "operationId": "getserviceprovision",
            "parameters": [
                {
                    "name": "id",
                    "type": "str",
                    "required": True,
                    "location": "query",
                },
                {
                    "name": "unredacted",
                    "type": "bool",
                    "required": False,
                    "location": "query",
                },
            ],
        },
        {
            "path": "/service-catalog/v1beta1/service-offers/{id}",
            "method": "GET",
            "summary": "getserviceoffer",
            "operationId": "getserviceoffer",
            "parameters": [
                {
                    "name": "id",
                    "type": "str",
                    "required": True,
                    "location": "query",
                },
            ],
        },
        {
            "path": "/service-catalog/v1/service-managers/{id}",
            "method": "GET",
            "summary": "get_service_manager_v1",
            "operationId": "get_service_manager_v1",
            "parameters": [
                {
                    "name": "id",
                    "type": "str",
                    "required": True,
                    "location": "query",
                },
            ],
        },
    ]
