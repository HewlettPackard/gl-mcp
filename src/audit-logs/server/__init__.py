"""
Server package for audit-logs MCP server.
"""

from .app import main
from .mcp_server import MCPServer

__all__ = ["main", "MCPServer"]
