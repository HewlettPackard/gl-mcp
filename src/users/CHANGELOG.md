# Changelog - Users MCP Server

All notable changes to the HPE GreenLake Users MCP Server will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.1] - 2026-01-07

### Added

- **Initial release** of HPE GreenLake Users MCP Server
- **Authentication**: OAuth2 integration with automatic token management
- **Core Tools**:
  - `get_users_identity_v1_users_get` - Retrieve list of users with filtering and pagination (supports filter, offset, limit)
  - `get_user_detailed_identity_v1_users_id_get` - Retrieve single user by ID
- **Dynamic Tools** (when `MCP_TOOL_MODE=dynamic`):
  - `list_endpoints` - Discover available API endpoints with filtering
  - `get_endpoint_schema` - Get detailed schema information for endpoints
  - `invoke_dynamic_tool` - Execute API calls with runtime parameter validation  
- **User Management**:
  - Read-only access to user information
  - User lookup by ID
- **Search & Filtering**:
  - Filter by createdAt, generation, id, lastLogin, resourceUri, type, updatedAt, userStatus, username
  - User status filtering (UNVERIFIED, VERIFIED, BLOCKED, DELETE_IN_PROGRESS, DELETED, SUSPENDED)
  - Pagination support with offset and limit
- **Output Formats**: JSON user data

### Security

- **OAuth2 Authentication** with automatic token management

### Technical Details

- **Python 3.10+** support
- **Model Context Protocol** v1.0 implementation
- **Rate Limiting** awareness (300 requests per minute)
