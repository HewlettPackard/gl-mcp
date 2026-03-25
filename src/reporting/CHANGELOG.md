# Changelog - Reporting MCP Server

All notable changes to the HPE GreenLake Reporting MCP Server will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-03-24

### Added

- **Initial release** of HPE GreenLake Reporting MCP Server
- **Authentication**: OAuth2 integration with automatic token management
- **Core Tools**:
  - `getreportingstatuses` - This API is designed to fetch the status of all reports for a specific workspace. filter of type is required for all requests:  Example: type eq "REPORT"
  - `getreportingstatusbyid` - Retrieve the status of a specific report by passing the report status ID.
- **Dynamic Tools** (when `MCP_TOOL_MODE=dynamic`):
  - `list_endpoints` - Discover available API endpoints with filtering
  - `get_endpoint_schema` - Get detailed schema information for endpoints
  - `invoke_dynamic_tool` - Execute API calls with runtime parameter validation  
- **Filtering & Search**:
  - Filter by type.
- **Output Formats**: JSON report information
- **Configuration**: Environment-based configuration

### Security

- **OAuth2 Authentication** with automatic token management

### Technical Details

- **Python 3.10+** support
- **Model Context Protocol** v1.0 implementation
