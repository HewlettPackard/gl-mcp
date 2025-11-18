# (c) Copyright 2025 Hewlett Packard Enterprise Development LP
"""Utilities for testing MCP servers.

This module provides utility functions for setting up and tearing down MCP server
connections in tests, particularly for end-to-end testing.
"""

import asyncio
import json
import os
import subprocess
from typing import Any, Dict, Optional, Tuple

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


def check_credentials() -> Optional[str]:
    """Check if the necessary credentials are set.

    Returns:
        String with missing credential names if any, None if all required credentials are present.
    """
    missing = []

    # Check for GREENLAKE_* variables
    if not os.getenv("GREENLAKE_CLIENT_ID"):
        missing.append("GREENLAKE_CLIENT_ID")
    if not os.getenv("GREENLAKE_CLIENT_SECRET"):
        missing.append("GREENLAKE_CLIENT_SECRET")
    # Workspace ID and API Base URL are optional for some services

    return ", ".join(missing) if missing else None


def parse_response_content(content: Any) -> Dict[str, Any]:
    """Parse the content from a tool response.

    Handles both string content and content that might be a list of content items
    in newer MCP client versions.

    Args:
        content: The content from the tool response, either a string or a list of content items.

    Returns:
        The parsed JSON object as a dictionary.
    """
    if isinstance(content, list):
        # Extract the text from the first content item
        content_text = content[0].text
    else:
        # Use the content directly if it's a string
        content_text = content

    return json.loads(content_text)  # type: ignore[no-any-return]


async def create_mcp_session(
    module_path: str, env: Optional[Dict[str, str]] = None
) -> Tuple[Any, Any, Any, Any, subprocess.Popen]:
    """Create a new MCP session for testing.

    Args:
        module_path: The Python module path to the MCP server application.
        env: Environment variables to pass to the subprocess. If None, the current
             environment will be used.

    Returns:
        A tuple containing:
        - session: The MCP client session
        - session_cm: The session context manager
        - stdio_transport: The stdio transport
        - stdio_client_cm: The stdio client context manager
        - process: The subprocess running the MCP server
    """
    # Set up environment
    if env is None:
        env = os.environ.copy()

    # Enable insecure transport for OAuth in testing environments
    env["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    # Ensure GREENLAKE_* variables are set from current environment
    if not env.get("GREENLAKE_CLIENT_ID") and os.getenv("GREENLAKE_CLIENT_ID"):
        env["GREENLAKE_CLIENT_ID"] = os.getenv("GREENLAKE_CLIENT_ID")  # type: ignore[assignment]

    if not env.get("GREENLAKE_CLIENT_SECRET") and os.getenv("GREENLAKE_CLIENT_SECRET"):
        env["GREENLAKE_CLIENT_SECRET"] = os.getenv("GREENLAKE_CLIENT_SECRET")  # type: ignore[assignment]

    if not env.get("GREENLAKE_API_BASE_URL") and os.getenv("GREENLAKE_API_BASE_URL"):
        env["GREENLAKE_API_BASE_URL"] = os.getenv("GREENLAKE_API_BASE_URL")  # type: ignore[assignment]
    else:
        env["GREENLAKE_API_BASE_URL"] = "https://global.api.greenlake.hpe.com"

    if not env.get("GREENLAKE_WORKSPACE_ID") and os.getenv("GREENLAKE_WORKSPACE_ID"):
        env["GREENLAKE_WORKSPACE_ID"] = os.getenv("GREENLAKE_WORKSPACE_ID")  # type: ignore[assignment]
    elif not env.get("GREENLAKE_WORKSPACE_ID"):
        env["GREENLAKE_WORKSPACE_ID"] = "test-workspace-id"

    # Set up server parameters
    server_params = StdioServerParameters(command="python3", args=["-m", module_path], env=env)

    # Start the MCP server as a subprocess
    process = subprocess.Popen(
        [server_params.command] + server_params.args,
        env=server_params.env,
        stdout=subprocess.PIPE,
        stdin=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    # Give the server a moment to start
    await asyncio.sleep(1)

    # Connect to the server
    stdio_client_cm = stdio_client(server_params)
    stdio_transport = await stdio_client_cm.__aenter__()
    stdio, write = stdio_transport

    # Create session
    session_cm = ClientSession(stdio, write)
    session = await session_cm.__aenter__()

    # Initialize session
    await session.initialize()

    # Return resources for cleanup
    return session, session_cm, stdio_transport, stdio_client_cm, process


async def cleanup_mcp_session(
    session: Any,
    session_cm: Any,
    stdio_transport: Any,
    stdio_client_cm: Any,
    process: subprocess.Popen,
) -> None:
    """Clean up an MCP session created for testing.

    Args:
        session: The MCP client session
        session_cm: The session context manager
        stdio_transport: The stdio transport
        stdio_client_cm: The stdio client context manager
        process: The subprocess running the MCP server
    """
    try:
        # Terminate process first to avoid hanging on session cleanup
        if process:
            try:
                if process.poll() is None:
                    process.terminate()
                    try:
                        process.wait(timeout=2)
                    except (TimeoutError, subprocess.TimeoutExpired):
                        # Force kill if process doesn't terminate in time
                        if process.poll() is None:
                            process.kill()
            except Exception as e:
                print(f"Warning: Error during process termination: {str(e)}")

        # Close session
        if session and session_cm:
            try:
                await session_cm.__aexit__(None, None, None)
            except Exception as e:
                print(f"Warning: Error during session cleanup: {str(e)}")

        # Close stdio transport
        if stdio_transport and stdio_client_cm:
            try:
                await stdio_client_cm.__aexit__(None, None, None)
            except Exception as e:
                print(f"Warning: Error during stdio transport cleanup: {str(e)}")

    except Exception as e:
        print(f"Warning: Error during cleanup: {str(e)}")
