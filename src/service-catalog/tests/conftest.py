# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""Shared pytest fixtures for service-catalog MCP server."""

from __future__ import annotations

import asyncio
from collections.abc import Iterator
from unittest.mock import AsyncMock

import pytest

from greenlake_service_catalog_mcp.config.settings import Settings
from greenlake_service_catalog_mcp.utils.http_client import ServiceCatalogHttpClient
from tests.shared.http import make_json_response


def _value_for_field(field_name: str, alias: str) -> str:
    lowered = alias.lower()

    if "url" in lowered or "endpoint" in lowered:
        return "https://api.example.test"
    if "secret" in lowered or "token" in lowered:
        return "test-secret"
    if "timeout" in lowered or "retri" in lowered:
        return "2"
    if "_id" in lowered or lowered.endswith("id") or "client" in lowered:
        return f"test-{field_name.lower()}"
    if "tool_mode" in lowered or field_name == "mcp_tool_mode":
        return "static"  # Valid tool mode for tests

    return f"test-{field_name.lower()}"


@pytest.fixture(scope="session")
def event_loop() -> Iterator[asyncio.AbstractEventLoop]:
    """Provide an event loop for pytest-asyncio when asyncio mode is auto."""
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(autouse=True)
def configure_env(request: pytest.FixtureRequest, monkeypatch: pytest.MonkeyPatch) -> None:
    """Populate required environment variables expected by Settings.

    Skipped for integration tests which rely on real credentials from the environment.
    """
    if request.node.get_closest_marker("integration"):
        return
    for field_name, field in Settings.model_fields.items():
        alias = field.alias or field_name.upper()
        monkeypatch.setenv(alias, _value_for_field(field_name, alias))


@pytest.fixture(autouse=True)
def reset_singletons(request: pytest.FixtureRequest, monkeypatch: pytest.MonkeyPatch) -> Iterator[None]:
    """Reset settings and HTTP-client singletons before/after every test.

    Prevents state leakage between unit tests (mock env vars) and integration
    tests (real env vars). Also neutralises PYTEST_CURRENT_TEST / TESTING for
    integration tests so TokenManager performs real OAuth instead of returning
    the fake 'test_token_12345' token.
    """
    import greenlake_service_catalog_mcp.config.settings as settings_module
    import greenlake_service_catalog_mcp.utils.http_client as http_client_module

    if request.node.get_closest_marker("integration"):
        # Prevent is_testing=True caused by PYTEST_CURRENT_TEST env var
        monkeypatch.delenv("PYTEST_CURRENT_TEST", raising=False)
        monkeypatch.setenv("TESTING", "false")

    # Reset before test so whatever env vars are active take effect
    settings_module._settings = None
    http_client_module._http_client = None
    yield
    # Reset after to avoid leaking state into the next test
    settings_module._settings = None
    http_client_module._http_client = None


@pytest.fixture
def mock_http_client() -> AsyncMock:
    """Provide a mock HTTP client with coroutine-capable methods."""
    client = AsyncMock(spec=ServiceCatalogHttpClient)
    for method in ("get", "post", "put", "delete"):
        setattr(client, method, AsyncMock())
    client.close = AsyncMock()
    return client


@pytest.fixture
def json_response_factory():
    """Factory for creating mock HTTP responses."""
    return make_json_response
