# (c) Copyright 2025 Hewlett Packard Enterprise Development LP
"""
Tests for dynamic tools in subscriptions MCP server.

This module tests the three dynamic tools:
- list_endpoints
- get_endpoint_schema
- invoke_dynamic_tool

Generated for dynamic mode when OpenAPI spec has 2 endpoints (>= 50 threshold).
"""

import pytest
from unittest.mock import AsyncMock, patch
from tools.implementations.list_endpoints import ListEndpointsTool
from tools.implementations.get_endpoint_schema import GetEndpointSchemaTool
from tools.implementations.invoke_dynamic_tool import InvokeDynamicTool


class TestListEndpointsTool:
    """Tests for the list endpoints tool."""

    @pytest.fixture
    def mock_http_client(self):
        """Mock HTTP client."""
        client = AsyncMock()
        client.base_url = "https://global.api.greenlake.hpe.com"
        return client

    @pytest.fixture
    def tool(self, mock_http_client):
        """Create list endpoints tool instance."""
        return ListEndpointsTool(mock_http_client)

    def test_tool_properties(self, tool):
        """Test basic tool properties."""
        assert tool.name == "list_endpoints"
        assert "subscriptions" in tool.description
        assert "endpoints" in tool.description.lower()

        # Test input schema
        schema = tool.input_schema
        assert schema["type"] == "object"
        assert "filter" in schema["properties"]
        assert schema["required"] == []

    @pytest.mark.asyncio
    async def test_execute_default_parameters(self, tool):
        """Test execution with default parameters - should return list of endpoint identifiers."""
        result = await tool.execute({})

        # Should return a list of strings
        assert isinstance(result, list)

        assert all(isinstance(endpoint, str) for endpoint in result)

        # Should be in METHOD:PATH format
        for endpoint in result:
            assert ":" in endpoint
            method, path = endpoint.split(":", 1)
            assert method in ["GET", "POST", "PUT", "DELETE", "PATCH"]
            assert path.startswith("/")

    @pytest.mark.asyncio
    async def test_execute_with_filter(self, tool):
        """Test execution with filter parameter."""
        # Test filtering
        result = await tool.execute({"filter": "users"})

        assert isinstance(result, list)
        # All results should contain the filter term
        for endpoint in result:
            assert "users" in endpoint.lower()

    @pytest.mark.asyncio
    async def test_execute_empty_filter(self, tool):
        """Test execution with empty filter."""
        result = await tool.execute({"filter": ""})

        assert isinstance(result, list)

        # Should return all endpoints when filter is empty
        assert len(result) > 0

        # All should be strings in METHOD:PATH format
        for endpoint in result:
            assert isinstance(endpoint, str)
            assert ":" in endpoint

    @pytest.mark.asyncio
    async def test_execute_with_filter_success(self, tool):
        """Test execution with filter parameter."""
        result = await tool.execute({"filter": "user"})

        assert isinstance(result, list)
        # All results should contain the filter term
        for endpoint in result:
            assert isinstance(endpoint, str)
            assert "user" in endpoint.lower()

    @pytest.mark.asyncio
    async def test_execute_with_method_filter(self, tool):
        """Test execution with method filter - method filtering not supported in optimized mode."""
        # The list_endpoints tool only supports path/summary filtering, not method filtering
        # Method filtering would be handled by the caller after getting the list
        result = await tool.execute({"filter": "GET"})

        assert isinstance(result, list)
        # Should return endpoints that contain "GET" in their identifier
        for endpoint in result:
            assert isinstance(endpoint, str)
            assert "GET" in endpoint


class TestGetEndpointSchemaTool:
    """Tests for the get endpoint schema tool."""

    @pytest.fixture
    def mock_http_client(self):
        """Mock HTTP client."""
        client = AsyncMock()
        client.base_url = "https://global.api.greenlake.hpe.com"
        return client

    @pytest.fixture
    def tool(self, mock_http_client):
        """Create get endpoint schema tool instance."""
        return GetEndpointSchemaTool(mock_http_client)

    def test_tool_properties(self, tool):
        """Test basic tool properties."""
        assert tool.name == "get_endpoint_schema"
        assert "subscriptions" in tool.description
        assert "schema" in tool.description.lower()

        # Test input schema
        schema = tool.input_schema
        assert schema["type"] == "object"
        assert "endpoint_identifier" in schema["properties"]
        assert "include_examples" in schema["properties"]
        assert "include_validation" in schema["properties"]
        assert set(schema["required"]) == {"endpoint_identifier"}

    @pytest.mark.asyncio
    async def test_execute_valid_endpoint(self, tool):
        """Test execution with valid endpoint."""

        # Use first available endpoint from the API
        result = await tool.execute({"endpoint_identifier": "GET:/subscriptions/v1/subscriptions"})

        assert len(result) == 1
        response = result[0]
        assert response["success"] is True
        assert "endpoint_identifier" in response
        assert "schema" in response

        schema = response["schema"]
        assert "path" in schema
        assert "method" in schema
        assert "parameters" in schema

    @pytest.mark.asyncio
    async def test_execute_invalid_endpoint(self, tool):
        """Test execution with invalid endpoint."""
        result = await tool.execute({"endpoint_identifier": "GET:/nonexistent"})

        assert len(result) == 1
        response = result[0]
        assert response["success"] is False
        assert "error" in response

    @pytest.mark.asyncio
    async def test_execute_with_examples(self, tool):
        """Test execution with examples enabled."""

        result = await tool.execute(
            {"endpoint_identifier": "GET:/subscriptions/v1/subscriptions", "include_examples": True}
        )

        assert len(result) == 1
        response = result[0]
        assert response["success"] is True
        assert "schema" in response
        # Check that parameters have examples when requested
        schema = response["schema"]
        if schema.get("parameters"):
            for param in schema["parameters"]:
                assert "example" in param or param.get("required") is False

    @pytest.mark.asyncio
    async def test_execute_missing_required_params(self, tool):
        """Test execution with missing required parameters."""
        result = await tool.execute({})

        assert len(result) == 1
        response = result[0]
        assert response["success"] is False
        assert "endpoint_identifier is required" in response["error"]


class TestInvokeDynamicTool:
    """Tests for the execute dynamic tool."""

    @pytest.fixture
    def tool(self, mock_http_client):
        """Create execute dynamic tool instance."""
        return InvokeDynamicTool(mock_http_client)

    @pytest.fixture
    def mock_http_client(self):
        """Mock HTTP client."""
        client = AsyncMock()
        client.base_url = "https://global.api.greenlake.hpe.com"
        return client

    def test_tool_properties(self, tool):
        """Test basic tool properties."""
        assert tool.name == "invoke_dynamic_tool"
        assert "subscriptions" in tool.description
        assert "execute" in tool.description.lower()

        # Test input schema
        schema = tool.input_schema
        assert schema["type"] == "object"
        assert "endpoint_identifier" in schema["properties"]
        assert "parameters" in schema["properties"]
        assert "headers" in schema["properties"]
        assert set(schema["required"]) == {"endpoint_identifier"}

    @pytest.mark.asyncio
    async def test_execute_valid_get_request(self, tool, mock_http_client):
        """Test execution of a valid GET request."""

        # Mock successful response
        mock_http_client.get.return_value = {"status": "success", "data": {"test": "data"}}

        # Use an endpoint and provide mock parameters for any path parameters
        # Most endpoints have path parameters, so we provide common mock values
        test_parameters = {
            "group-id": "test-group",
            "compliance-id": "test-compliance",
            "id": "test-id",
            "webhook_id": "test-webhook",
            "delivery_id": "test-delivery",
            "device-id": "test-device",
            "location_id": "test-location",
            "history-id": "test-history",
        }

        # Patch the http_client
        with patch.object(tool, "http_client", mock_http_client):
            result = await tool.execute(
                {"endpoint_identifier": "GET:/subscriptions/v1/subscriptions", "parameters": test_parameters}
            )

        assert len(result) == 1
        response = result[0]

        # Check if the request was successful or failed due to parameter validation
        if response["success"]:
            assert "response" in response
            # Verify HTTP client was called
            mock_http_client.get.assert_called_once()
        else:
            # If it failed due to parameter validation, that's expected for complex endpoints
            # The test is verifying the tool can handle the request structure correctly
            assert (
                "validation" in response.get("error", "").lower()
                or "parameter" in response.get("error", "").lower()
                or "required" in response.get("error", "").lower()
            )

    @pytest.mark.asyncio
    async def test_execute_invalid_endpoint(self, tool):
        """Test execution with invalid endpoint."""
        result = await tool.execute({"endpoint_identifier": "GET:/nonexistent", "parameters": {}})

        assert len(result) == 1
        response = result[0]
        assert response["success"] is False
        assert "error" in response

    @pytest.mark.asyncio
    async def test_execute_missing_required_params(self, tool):
        """Test execution with missing required parameters."""
        result = await tool.execute({})

        assert len(result) == 1
        response = result[0]
        assert response["success"] is False
        assert "endpoint_identifier is required" in response["error"]

    @pytest.mark.asyncio
    async def test_execute_unsupported_method(self, tool):
        """Test execution with unsupported HTTP method."""
        # Use a valid endpoint path but with POST method (not allowed in MCP read-only servers)
        result = await tool.execute(
            {
                "endpoint_identifier": "POST:/subscriptions/v1/subscriptions",  # Valid path but unsupported method
                "parameters": {},
            }
        )

        assert len(result) == 1
        response = result[0]
        assert response["success"] is False
        # Should mention unsupported method or read operations
        error_text = response.get("error", "") + " " + response.get("message", "")
        assert (
            "read operations" in error_text.lower()
            or "unsupported" in error_text.lower()
            or "not found" in error_text.lower()
        )


class TestDynamicToolsIntegration:
    """Integration tests for all three dynamic tools working together."""

    @pytest.fixture
    def mock_http_client(self):
        """Mock HTTP client."""
        client = AsyncMock()
        client.base_url = "https://global.api.greenlake.hpe.com"
        return client

    @pytest.fixture
    def list_tool(self, mock_http_client):
        return ListEndpointsTool(mock_http_client)

    @pytest.fixture
    def schema_tool(self, mock_http_client):
        return GetEndpointSchemaTool(mock_http_client)

    @pytest.fixture
    def execute_tool(self, mock_http_client):
        return InvokeDynamicTool(mock_http_client)

    @pytest.mark.asyncio
    async def test_discovery_flow(self, list_tool, schema_tool, execute_tool):
        """Test the complete discovery and execution flow."""
        # Step 1: List endpoints to discover available APIs
        endpoints = await list_tool.execute({})
        assert isinstance(endpoints, list)

        assert len(endpoints) > 0

        # Step 2: Get detailed schema for first endpoint
        first_endpoint = endpoints[0]
        endpoint_identifier = first_endpoint  # Already in METHOD:PATH format
        schema_result = await schema_tool.execute({"endpoint_identifier": endpoint_identifier})

        assert len(schema_result) == 1
        assert schema_result[0]["success"] is True

        # Step 3: Verify execute tool recognizes the endpoint
        execute_result = await execute_tool.execute({"endpoint_identifier": endpoint_identifier, "parameters": {}})

        # Should not fail with "endpoint not found" error
        assert len(execute_result) == 1
        # May fail with other errors (like auth) but not "endpoint not found"
        if not execute_result[0]["success"]:
            assert "not found" not in execute_result[0]["error"].lower()


# Sample test data for dynamic tools
@pytest.fixture
def sample_endpoints():
    """Sample endpoint data for testing."""
    return [
        {
            "path": "/subscriptions/v1/subscriptions",
            "method": "GET",
            "summary": "getsubscriptionsv1",
            "operationId": "getsubscriptionsv1",
            "parameters": [
                {"name": "filter", "type": "str", "required": False, "location": "query"},
                {"name": "filter-tags", "type": "str", "required": False, "location": "query"},
                {"name": "sort", "type": "str", "required": False, "location": "query"},
                {"name": "select", "type": "List[str]", "required": False, "location": "query"},
                {"name": "limit", "type": "int", "required": False, "location": "query"},
                {"name": "offset", "type": "int", "required": False, "location": "query"},
            ],
        },
        {
            "path": "/subscriptions/v1/subscriptions/{id}",
            "method": "GET",
            "summary": "getsubscriptiondetailsbyidv1",
            "operationId": "getsubscriptiondetailsbyidv1",
            "parameters": [
                {"name": "id", "type": "str", "required": True, "location": "query"},
            ],
        },
    ]


@pytest.fixture
def sample_tool_arguments():
    """Sample arguments for testing dynamic tools."""
    return {
        "list_endpoints": {"filter": "", "method": "", "include_deprecated": True},
        "get_endpoint_schema": {
            "endpoint_identifier": "GET:/subscriptions/v1/subscriptions",
            "include_examples": True,
            "include_validation": True,
        },
        "execute_dynamic_tool": {
            "endpoint_identifier": "GET:/subscriptions/v1/subscriptions",
            "parameters": {},
            "headers": {},
        },
    }
