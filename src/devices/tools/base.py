# (c) Copyright 2025 Hewlett Packard Enterprise Development LP
"""
Base tool class for devices MCP server.

This module provides the base class for all MCP tools.
"""

from loguru import logger
from abc import ABC, abstractmethod
from typing import Any, Dict, List, TYPE_CHECKING

if TYPE_CHECKING:
    from utils.http_client import DevicesHttpClient


class BaseTool(ABC):
    """Base class for MCP tools."""

    def __init__(self, http_client: "DevicesHttpClient"):
        """
        Initialize the tool.

        Args:
            http_client: HTTP client for API requests
        """
        self.http_client = http_client
        self.logger = logger  # Use global loguru logger

    @property
    @abstractmethod
    def name(self) -> str:
        """Tool name."""
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        """Tool description."""
        pass

    @property
    @abstractmethod
    def input_schema(self) -> Dict[str, Any]:
        """Input schema for the tool."""
        pass

    @abstractmethod
    async def execute(self, arguments: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Execute the tool with given arguments.

        Args:
            arguments: Tool arguments

        Returns:
            Tool execution results
        """
        pass

    def validate_arguments(self, arguments: Dict[str, Any]) -> None:
        """
        Validate tool arguments.

        Args:
            arguments: Arguments to validate

        Raises:
            ValueError: If arguments are invalid
        """
        # Basic validation - subclasses can override for specific validation
        pass

    def format_error(self, error: Exception) -> Dict[str, Any]:
        """
        Format an error message.

        Args:
            error: Exception to format

        Returns:
            Formatted error result
        """
        return {"success": False, "tool": self.name, "error": type(error).__name__, "message": str(error)}

    def format_success(self, result: Any) -> Dict[str, Any]:
        """
        Format a successful result.

        Args:
            result: Result to format

        Returns:
            Formatted result
        """
        return {"success": True, "tool": self.name, "result": result}

    def format_validation_error(self, message: str) -> Dict[str, Any]:
        """
        Format a validation error.

        Args:
            message: Error message

        Returns:
            Formatted error result
        """
        return {"success": False, "tool": self.name, "error": "ValidationError", "message": message}

    def coerce_string_to_int(self, value: Any, param_name: str) -> int:
        """
        Coerce a string value to integer.
        This handles cases where LLM clients send integer parameters as strings.

        Args:
            value: Parameter value to coerce (must be string or int)
            param_name: Parameter name (for error messages)

        Returns:
            Integer value

        Raises:
            ValueError: If the value cannot be coerced to integer
        """
        if isinstance(value, int) and not isinstance(value, bool):
            return value

        if isinstance(value, str):
            try:
                return int(value)
            except (ValueError, TypeError) as e:
                raise ValueError(f"Parameter '{param_name}' must be an integer or integer string, got '{value}'") from e

        raise ValueError(f"Parameter '{param_name}' must be an integer or integer string, got {type(value).__name__}")
