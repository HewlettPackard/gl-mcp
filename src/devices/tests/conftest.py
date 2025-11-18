# (c) Copyright 2025 Hewlett Packard Enterprise Development LP
"""Shared pytest fixtures for devices MCP server."""

from __future__ import annotations

import asyncio
from collections.abc import Iterator
from unittest.mock import AsyncMock

import pytest

from config.settings import Settings
from utils.http_client import DevicesHttpClient
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
def configure_env(monkeypatch: pytest.MonkeyPatch) -> None:
    """Populate required environment variables expected by Settings."""
    for field_name, field in Settings.model_fields.items():
        alias = field.alias or field_name.upper()
        monkeypatch.setenv(alias, _value_for_field(field_name, alias))


@pytest.fixture
def mock_http_client() -> AsyncMock:
    """Provide a mock HTTP client with coroutine-capable methods."""
    client = AsyncMock(spec=DevicesHttpClient)
    for method in ("get", "post", "put", "delete"):
        setattr(client, method, AsyncMock())
    client.close = AsyncMock()
    return client


@pytest.fixture
def json_response_factory():
    """Factory for creating mock HTTP responses."""
    return make_json_response
