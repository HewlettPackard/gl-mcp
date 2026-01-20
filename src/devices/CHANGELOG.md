# Changelog - Devices MCP Server

All notable changes to the HPE GreenLake Devices MCP Server will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.1] - 2026-01-07

### Added

- **Initial release** of HPE GreenLake Devices MCP Server
- **Authentication**: OAuth2 integration with automatic token management
- **Core Tools**:
  - `getdevicesv1` - Retrieve and filter devices managed in workspace (supports filter, filter-tags, sort, select, limit, offset)
  - `getdevicebyidv1` - Get details on specific device by resource ID
- **Dynamic Tools** (when `MCP_TOOL_MODE=dynamic`):
  - `list_endpoints` - Discover available API endpoints with filtering
  - `get_endpoint_schema` - Get detailed schema information for endpoints
  - `invoke_dynamic_tool` - Execute API calls with runtime parameter validation  
- **Device Management**:
  - Read-only access to device information
  - Device lookup by resource ID
- **Filtering & Search**:
  - Filter by application, archived, assignedState, createdAt, deviceType, id, location, macAddress, model, partNumber, region, serialNumber, subscription, tags, tenantWorkspaceId, type, updatedAt, warranty
  - Tag-based filtering with conditional expressions
  - Sorting and field selection capabilities
- **Output Formats**: JSON device information
- **Configuration**: Environment-based configuration

### Security

- **OAuth2 Authentication** with automatic token management

### Technical Details

- **Python 3.10+** support
- **Model Context Protocol** v1.0 implementation
- **Rate Limiting** awareness (160/40 requests per minute)

