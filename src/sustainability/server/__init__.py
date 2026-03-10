"""
Server package for Sustainability_Insight_Center MCP server.
"""

from .app import main
from .fastmcp_instance import mcp
from .mcp_server import MCPServer

__all__ = ["main", "mcp", "MCPServer"]
