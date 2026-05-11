# Changelog - Workspaces MCP Server

All notable changes to the HPE GreenLake Workspaces MCP Server will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.1] - 2026-05-11

### Added

- Added `X-HPE-Thirdparty` to all outbound requests (matching `User-Agent` as `{service}-mcp-server/{version}`), with template tests updated to verify it is always present.

## [1.1.0] - 2026-04-28

### Changed

- Renamed PyPI package from `workspaces-mcp` to `greenlake-workspaces-mcp` for consistent HPE GreenLake branding
- Moved source code into `greenlake_workspaces_mcp/` package folder to resolve namespace collisions when multiple MCP servers are installed in the same Python environment

### Added

- Added `server.json` MCP Registry manifest to support publishing to the MCP Registry (`registry.modelcontextprotocol.io`)

## [1.0.2] - 2026-03-02

### Changed

- Path parameters in generated tools now use URL encoding for proper handling of special characters
- Static tools (example_tool.py template) use urllib.parse.quote(value, safe="")
- Dynamic tools (invoke_dynamic_tool.py template) use urllib.parse.quote(value, safe="")

### Security

- Dynamic tools now sanitize user-provided headers to prevent injection attacks
- Added FORBIDDEN_HEADERS constant listing security-sensitive headers
- Added _sanitize_headers() method to strip Authorization, Host, Cookie, X-Forwarded-* headers
- Prevents callers from overriding security-critical headers in API requests

## [1.0.1] - 2026-01-07

### Added

- **Initial release** of HPE GreenLake Workspaces MCP Server
- **Authentication**: OAuth2 integration with automatic token management
- **Core Tools**:
  - `get_workspace_workspaces_v1_workspaces_workspaceid_get` - Retrieve basic workspace information by ID
  - `get_workspace_detailed_info_workspaces_v1_workspaces_wo_5c14f2bc` - Retrieve detailed workspace information
- **Dynamic Tools** (when `MCP_TOOL_MODE=dynamic`):
  - `list_endpoints` - Discover available API endpoints with filtering
  - `get_endpoint_schema` - Get detailed schema information for endpoints
  - `invoke_dynamic_tool` - Execute API calls with runtime parameter validation  
- **Workspace Management**:
  - Basic workspace information retrieval
  - Detailed workspace contact information
  - Workspace identification and metadata
- **Output Formats**: JSON workspace information
- **Configuration**: Environment-based configuration

### Security

- **OAuth2 Authentication** with automatic token management

### Technical Details

- **Python 3.10+** support
- **Model Context Protocol** v1.0 implementation
- **Read-Only API Access** to workspace endpoints
