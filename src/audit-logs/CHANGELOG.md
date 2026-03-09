# Changelog - Audit Logs MCP Server

All notable changes to the HPE GreenLake Audit Logs MCP Server will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.2] - 2026-03-09

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

- **Initial release** of HPE GreenLake Audit Logs MCP Server
- **Authentication**: OAuth2 integration with automatic token refresh
- **Core Tools**:
  - `getauditlogs` - Retrieve audit logs with filtering capabilities
  - `getauditlogdetails` - Get detailed information for specific log entries
- **Dynamic Tools** (when `MCP_TOOL_MODE=dynamic`):
  - `list_endpoints` - Discover available API endpoints with filtering
  - `get_endpoint_schema` - Get detailed schema information for endpoints
  - `invoke_dynamic_tool` - Execute API calls with runtime parameter validation
- **Filtering Support**:
  - Filter by createdAt, category, description, additionalInfo/ipAddress, user/username, workspace/workspaceName, application/id, region, hasDetails
  - Support for eq, contains, in, lt, ge operators
  - Query parameter selection with select option
- **Output Formats**: JSON structured data with comprehensive event details
- **Configuration**: Environment-based configuration for credentials

### Security

- **OAuth2 Authentication** with automatic token management

### Technical Details

- **Python 3.10+** compatibility
- **Model Context Protocol** v1.0 compliance
- **Comprehensive logging** for debugging and monitoring
