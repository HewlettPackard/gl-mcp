# (c) Copyright 2025 Hewlett Packard Enterprise Development LP
"""
Test for getsubscriptionsv1 tool in subscriptions MCP server.

This file contains tests for the getsubscriptionsv1 tool.
"""

import pytest

# Import getsubscriptionsv1Tool
from tools.implementations.getsubscriptionsv1 import getsubscriptionsv1Tool


class Testgetsubscriptionsv1Tool:
    """Test cases for getsubscriptionsv1Tool."""

    @pytest.fixture
    def tool_instance(self, mock_http_client):
        """Create tool instance for testing."""
        return getsubscriptionsv1Tool(mock_http_client)

    @pytest.fixture
    def valid_arguments(self):
        """Valid arguments for the tool."""
        return {
            "filter": "test-value",
            "filter-tags": "test-value",
            "sort": "test-value",
            "select": ["test-value"],
            "limit": 100,
            "offset": 100,
        }

    @pytest.fixture
    def invalid_arguments(self):
        """Invalid arguments for the tool."""
        # Check if there are any required parameters

        # For tools with only optional parameters, return None to skip invalid args test
        return None

    @pytest.fixture
    def api_success_response(self):
        """Mock API success response."""
        return {
            "items": [{"id": "item-1", "name": "Test Item 1", "created_at": "2024-01-01T00:00:00Z"}],
            "total": 1,
            "count": 1,
        }

    # PROPERTY TESTS
    def test_tool_name(self, tool_instance):
        """Test tool name property."""
        assert tool_instance.name == "getsubscriptionsv1"

    def test_tool_description(self, tool_instance):
        """Test tool description property."""
        description = tool_instance.description
        assert isinstance(description, str)
        assert len(description) > 0

    def test_input_schema(self, tool_instance):
        """Test input schema property."""
        schema = tool_instance.input_schema
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

    # VALIDATION TESTS
    def test_validate_valid_arguments(self, tool_instance, valid_arguments):
        """Test validation with valid arguments."""
        # Should not raise any exception
        tool_instance.validate_arguments(valid_arguments)

    def test_validate_invalid_arguments(self, tool_instance, invalid_arguments):
        """Test validation with invalid arguments."""

        # Skip for tools with only optional parameters
        if invalid_arguments is None:
            pytest.skip("No required parameters - cannot test invalid arguments")
        with pytest.raises(ValueError):
            tool_instance.validate_arguments(invalid_arguments)

    def test_validate_missing_required_arguments(self, tool_instance):
        """Test validation with missing required arguments."""

        # Skip for tools with no required parameters
        pytest.skip("No required parameters - cannot test missing required arguments")

    # EXECUTION TESTS
    @pytest.mark.asyncio
    async def test_execute_success(self, tool_instance, valid_arguments, api_success_response, mock_http_client):
        """Test successful tool execution."""
        # Setup mock
        mock_http_client.get.return_value = api_success_response

        # Execute tool
        result = await tool_instance.execute(valid_arguments)

        # Assertions
        assert isinstance(result, list)
        assert len(result) > 0
        assert all(isinstance(item, dict) for item in result)

        # Verify API call
        mock_http_client.get.assert_called_once()

    @pytest.mark.asyncio
    async def test_execute_validation_error(self, tool_instance, invalid_arguments):
        """Test tool execution with validation error."""

        # Skip for tools with only optional parameters
        if invalid_arguments is None:
            pytest.skip("No required parameters - cannot test validation errors")

        result = await tool_instance.execute(invalid_arguments)
        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0]["success"] is False

    @pytest.mark.asyncio
    async def test_execute_api_error(self, tool_instance, valid_arguments, mock_http_client):
        """Test tool execution with API error."""
        # Setup mock to raise exception
        mock_http_client.get.side_effect = Exception("API Error")

        # Execute tool
        result = await tool_instance.execute(valid_arguments)

        # Should return error result
        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0]["success"] is False
        assert result[0]["tool"] == "getsubscriptionsv1"
        assert result[0]["error"] == "Exception"
        assert result[0]["message"] == "API Error"
