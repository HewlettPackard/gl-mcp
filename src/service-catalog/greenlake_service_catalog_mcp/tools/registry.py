# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
Tool registry for service-catalog MCP server.

Importing this module (or calling ``get_tool_classes()``) triggers the side-effect
imports that execute every ``@mcp.tool()`` decorator, which registers all tools
with the FastMCP instance defined in ``server.fastmcp_instance``.
"""

from __future__ import annotations

from loguru import logger

from greenlake_service_catalog_mcp.config.settings import get_settings


def get_tool_classes(mode: str | None = None) -> list:
    """
    Import tool modules so that ``@mcp.tool()`` decorators fire.

    This function has *no* meaningful return value – the registrations happen as a
    side effect of the imports.  It is called by ``server.app`` and by
    ``MCPServer.initialize()`` to ensure tools are wired up before the server
    starts serving requests.

    Args:
        mode: ``"static"`` for one tool per endpoint (default),
              ``"dynamic"`` for the 3 meta-tools.  ``None`` reads from settings.

    Returns:
        Empty list (tools are registered as FastMCP functions, not class objects).
    """
    if mode is None:
        mode = get_settings().mcp_tool_mode

    try:
        if mode == "dynamic":
            from greenlake_service_catalog_mcp.tools.implementations.list_endpoints import list_endpoints  # noqa: F401
            from greenlake_service_catalog_mcp.tools.implementations.get_endpoint_schema import get_endpoint_schema  # noqa: F401
            from greenlake_service_catalog_mcp.tools.implementations.invoke_dynamic_tool import invoke_dynamic_tool  # noqa: F401

            logger.info("Dynamic mode: 3 meta-tools registered")
        else:
            # Static mode: import every per-endpoint tool module.
            # The @mcp.tool() decorators inside each module fire on import and
            # register the function with the FastMCP instance.
            import greenlake_service_catalog_mcp.tools.implementations.getserviceofferregions  # noqa: F401 (triggers @mcp.tool registration)
            import greenlake_service_catalog_mcp.tools.implementations.getserviceprovisions  # noqa: F401 (triggers @mcp.tool registration)
            import greenlake_service_catalog_mcp.tools.implementations.getserviceoffers  # noqa: F401 (triggers @mcp.tool registration)
            import greenlake_service_catalog_mcp.tools.implementations.getserviceofferregion  # noqa: F401 (triggers @mcp.tool registration)
            import greenlake_service_catalog_mcp.tools.implementations.service_managers_for_a_region_v1  # noqa: F401 (triggers @mcp.tool registration)
            import greenlake_service_catalog_mcp.tools.implementations.get_service_manager_provisions_v1  # noqa: F401 (triggers @mcp.tool registration)
            import greenlake_service_catalog_mcp.tools.implementations.get_service_managers_v1  # noqa: F401 (triggers @mcp.tool registration)
            import greenlake_service_catalog_mcp.tools.implementations.get_service_manager_provision_v1  # noqa: F401 (triggers @mcp.tool registration)
            import greenlake_service_catalog_mcp.tools.implementations.per_region_service_managers_v1  # noqa: F401 (triggers @mcp.tool registration)
            import greenlake_service_catalog_mcp.tools.implementations.getserviceprovision  # noqa: F401 (triggers @mcp.tool registration)
            import greenlake_service_catalog_mcp.tools.implementations.getserviceoffer  # noqa: F401 (triggers @mcp.tool registration)
            import greenlake_service_catalog_mcp.tools.implementations.get_service_manager_v1  # noqa: F401 (triggers @mcp.tool registration)

            logger.info("Static mode: 12 endpoint tools registered")
    except ImportError as exc:
        logger.error(f"Failed to import tool module: {exc}")

    return []


def get_static_tools() -> list:
    """Trigger static tool registrations (one tool per endpoint)."""
    return get_tool_classes(mode="static")


def get_dynamic_tools() -> list:
    """Trigger dynamic meta-tool registrations."""
    return get_tool_classes(mode="dynamic")


def set_tool_mode(mode: str) -> None:
    """
    Persist a tool mode override for this process.

    Args:
        mode: ``"static"`` or ``"dynamic"``
    """
    settings = get_settings()
    settings.mcp_tool_mode = mode
    logger.info(f"Tool mode set to: {mode}")


def get_tool_mode() -> str:
    """Return the current tool mode (``"static"`` or ``"dynamic"``)."""
    return get_settings().mcp_tool_mode


# ---------------------------------------------------------------------------
# Backwards-compatibility shim
# ---------------------------------------------------------------------------

#: Alias kept so that code importing ``get_tools`` still works.
get_tools = get_tool_classes
