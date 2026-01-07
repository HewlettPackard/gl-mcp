# (c) Copyright 2025 Hewlett Packard Enterprise Development LP
"""
Tests for version information module in devices MCP server.

This file contains tests for version constants and User-Agent string generation.
"""


def test_version_module_imports():
    """Test that version module can be imported and has required constants."""
    from _version import SERVER_NAME, SERVER_VERSION, USER_AGENT

    assert SERVER_NAME is not None
    assert SERVER_VERSION is not None
    assert USER_AGENT is not None


def test_server_name_format():
    """Test that server name is in kebab-case format."""
    from _version import SERVER_NAME

    # Server name should be a non-empty string
    assert isinstance(SERVER_NAME, str)
    assert len(SERVER_NAME) > 0

    # Kebab-case validation: lowercase letters, numbers, and hyphens only
    assert all(c.islower() or c.isdigit() or c == "-" for c in SERVER_NAME)
    assert not SERVER_NAME.startswith("-")
    assert not SERVER_NAME.endswith("-")


def test_server_version_format():
    """Test that server version is a valid version string."""
    from _version import SERVER_VERSION

    # Version should be a non-empty string
    assert isinstance(SERVER_VERSION, str)
    assert len(SERVER_VERSION) > 0

    # Should have at least one dot (e.g., "1.0" or "1.0.0")
    parts = SERVER_VERSION.split(".")
    assert len(parts) >= 2, f"Version '{SERVER_VERSION}' should have at least major.minor format"

    # Each part should be numeric (except for pre-release suffixes)
    major = parts[0]
    minor = parts[1]
    assert major.isdigit(), f"Major version '{major}' should be numeric"
    assert minor.isdigit(), f"Minor version '{minor}' should be numeric"


def test_user_agent_format():
    """Test that User-Agent string follows the expected format."""
    from _version import USER_AGENT, SERVER_NAME, SERVER_VERSION

    # User-Agent should follow format: HPE-GreenLake-MCP/{server-name}-{version}
    assert isinstance(USER_AGENT, str)
    assert USER_AGENT.startswith("HPE-GreenLake-MCP/")

    # Extract the service identifier part
    prefix = "HPE-GreenLake-MCP/"
    service_identifier = USER_AGENT[len(prefix) :]

    # Should contain server name and version
    assert SERVER_NAME in service_identifier
    assert SERVER_VERSION in service_identifier

    # Should be in format: {server-name}-{version}
    expected = f"{SERVER_NAME}-{SERVER_VERSION}"
    assert service_identifier == expected, f"Expected '{expected}', got '{service_identifier}'"


def test_user_agent_no_spaces():
    """Test that User-Agent string contains no spaces."""
    from _version import USER_AGENT

    assert " " not in USER_AGENT, "User-Agent should not contain spaces"


def test_user_agent_immutable():
    """Test that version constants are strings (immutable)."""
    from _version import SERVER_NAME, SERVER_VERSION, USER_AGENT

    assert isinstance(SERVER_NAME, str)
    assert isinstance(SERVER_VERSION, str)
    assert isinstance(USER_AGENT, str)


def test_user_agent_construction():
    """Test that User-Agent is constructed correctly from components."""
    from _version import SERVER_NAME, SERVER_VERSION, USER_AGENT

    # Manually construct what the User-Agent should be
    expected_user_agent = f"HPE-GreenLake-MCP/{SERVER_NAME}-{SERVER_VERSION}"

    assert USER_AGENT == expected_user_agent
