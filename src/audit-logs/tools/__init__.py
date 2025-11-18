"""
Tools package for audit-logs MCP server.
"""

from .base import BaseTool
from .registry import get_tools, register_tool

__all__ = ["BaseTool", "get_tools", "register_tool"]
