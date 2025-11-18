# (c) Copyright 2025 Hewlett Packard Enterprise Development LP
"""
Tool registry for workspaces MCP server.

This module handles tool discovery and registration with support for both static and dynamic modes.
"""

from loguru import logger
from typing import List, Optional, Type
from tools.base import BaseTool
from config.settings import get_settings


def get_tools(mode: Optional[str] = None) -> List[Type[BaseTool]]:
    """
    Get all available tool classes based on the specified mode.

    Args:
        mode: Tool mode - "static" for individual endpoint tools, "dynamic" for meta-tools.
              If None, uses MCP_TOOL_MODE from settings (defaults to "static")

    Returns:
        List of tool classes
    """
    if mode is None:
        mode = get_settings().mcp_tool_mode

    tools = []

    try:
        if mode == "dynamic":
            # Dynamic mode: Import the 3 generic dynamic meta-tools
            from tools.implementations.list_endpoints import ListEndpointsTool
            from tools.implementations.get_endpoint_schema import GetEndpointSchemaTool
            from tools.implementations.invoke_dynamic_tool import InvokeDynamicTool

            tools.extend([ListEndpointsTool, GetEndpointSchemaTool, InvokeDynamicTool])
            logger.info("Using dynamic mode with 3 meta-tools")
        else:
            # Static mode: Import one tool per endpoint (default)
            from tools.implementations.get_workspace_workspaces_v1_workspaces_workspaceid_get import (
                get_workspace_workspaces_v1_workspaces_workspaceid_getTool,
            )
            from tools.implementations.get_workspace_detailed_info_workspaces_v1_workspaces_wo_5c14f2bc import (
                get_workspace_detailed_info_workspaces_v1_workspaces_wo_5c14f2bcTool,
            )

            tools.extend(
                [
                    get_workspace_workspaces_v1_workspaces_workspaceid_getTool,
                    get_workspace_detailed_info_workspaces_v1_workspaces_wo_5c14f2bcTool,
                ]
            )
            logger.info(f"Using static mode with {len(tools)} endpoint-specific tools")

    except ImportError as e:
        logger.error(f"Failed to import tools: {str(e)}")
        # Fallback to dynamic discovery
        tools = discover_tools()

    return tools


def get_static_tools() -> List[Type[BaseTool]]:
    """
    Get static tools (one tool per endpoint).

    Returns:
        List of static tool classes
    """
    return get_tools(mode="static")


def get_dynamic_tools() -> List[Type[BaseTool]]:
    """
    Get dynamic tools (3 meta-tools for all endpoints).

    Returns:
        List of dynamic tool classes
    """
    return get_tools(mode="dynamic")


def set_tool_mode(mode: str) -> None:
    """
    Set the tool mode for this session.

    Args:
        mode: "static" or "dynamic"

    Raises:
        pydantic.ValidationError: If mode is not 'static' or 'dynamic' (validated by Settings)
    """
    # Update the settings instance (validation happens in Settings.validate_tool_mode)
    settings = get_settings()
    settings.mcp_tool_mode = mode
    logger.info(f"Tool mode set to: {mode}")


def get_tool_mode() -> str:
    """
    Get the current tool mode.

    Returns:
        Current tool mode ("static" or "dynamic")
    """
    return get_settings().mcp_tool_mode


def register_tool(tool_class: Type[BaseTool]) -> None:
    """
    Register a tool class.

    This function can be used for manual tool registration if needed.

    Args:
        tool_class: Tool class to register
    """
    # This could be extended to maintain a registry of tools
    # For now, it's a placeholder for future enhancement
    pass


# DYNAMIC TOOL DISCOVERY (OPTIONAL)
def discover_tools(mode: Optional[str] = None) -> List[Type[BaseTool]]:
    """
    Dynamically discover tools from the implementations package.

    This is an alternative to manual imports in get_tools().

    Returns:
        List of discovered tool classes
    """
    import importlib
    from pathlib import Path

    tools: List[Type[BaseTool]] = []
    implementations_dir = Path(__file__).parent / "implementations"

    if not implementations_dir.exists():
        logger.warning("Implementations directory not found")
        return tools

    try:
        for file_path in implementations_dir.glob("*.py"):
            if file_path.name.startswith("__"):
                continue

            module_name = f"tools.implementations.{file_path.stem}"

            try:
                module = importlib.import_module(module_name)

                # Look for classes that inherit from BaseTool
                for attr_name in dir(module):
                    attr = getattr(module, attr_name)

                    if isinstance(attr, type) and issubclass(attr, BaseTool) and attr is not BaseTool:
                        tools.append(attr)
                        logger.debug(f"Discovered tool: {attr.__name__}")

            except ImportError as e:
                logger.error(f"Failed to import {module_name}: {str(e)}")
                continue

    except Exception as e:
        logger.error(f"Tool discovery failed: {str(e)}")

    return tools
