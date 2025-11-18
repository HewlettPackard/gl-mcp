# (c) Copyright 2025 Hewlett Packard Enterprise Development LP
"""
Test for get_workspace_detailed_info_workspaces_v1_workspaces_wo_5c14f2bc tool in workspaces MCP server.

This file contains tests for the get_workspace_detailed_info_workspaces_v1_workspaces_wo_5c14f2bc tool.
"""

import pytest

# Import get_workspace_detailed_info_workspaces_v1_workspaces_wo_5c14f2bcTool
from tools.implementations.get_workspace_detailed_info_workspaces_v1_workspaces_wo_5c14f2bc import (
    get_workspace_detailed_info_workspaces_v1_workspaces_wo_5c14f2bcTool,
)


class Testget_workspace_detailed_info_workspaces_v1_workspaces_wo_5c14f2bcTool:
    """Test cases for get_workspace_detailed_info_workspaces_v1_workspaces_wo_5c14f2bcTool."""

    @pytest.fixture
    def tool_instance(self, mock_http_client):
        """Create tool instance for testing."""
        return get_workspace_detailed_info_workspaces_v1_workspaces_wo_5c14f2bcTool(mock_http_client)

    @pytest.fixture
    def valid_arguments(self):
        """Valid arguments for the tool."""
        return {
            "workspaceId": "test-value",
        }

    @pytest.fixture
    def invalid_arguments(self):
        """Invalid arguments for the tool."""
        # Check if there are any required parameters

        # For tools with required parameters, test with None values
        return {
            "workspaceId": None,  # Invalid value
        }

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
        assert tool_instance.name == "get_workspace_detailed_info_workspaces_v1_workspaces_wo_5c14f2bc"

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

        with pytest.raises(ValueError):
            tool_instance.validate_arguments(invalid_arguments)

    def test_validate_missing_required_arguments(self, tool_instance):
        """Test validation with missing required arguments."""

        # When no arguments are provided, validation should fail for the first required parameter
        args = {}
        with pytest.raises(ValueError):
            tool_instance.validate_arguments(args)

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

        result = await tool_instance.execute(invalid_arguments)

        # Should return error result
        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0]["success"] is False
        assert result[0]["error"] == "ValidationError"

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
        assert result[0]["tool"] == "get_workspace_detailed_info_workspaces_v1_workspaces_wo_5c14f2bc"
        assert result[0]["error"] == "Exception"
        assert result[0]["message"] == "API Error"
