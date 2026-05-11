# Changelog - Service Catalog MCP Server

All notable changes to the HPE GreenLake Service Catalog MCP Server will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.2] - 2026-05-11

### Added

- Added `X-HPE-Thirdparty` to all outbound requests (matching `User-Agent` as `{service}-mcp-server/{version}`), with template tests updated to verify it is always present.

## [1.0.1] - 2026-04-28

### Changed

- Renamed PyPI package from `service-catalog-mcp` to `greenlake-service-catalog-mcp` for consistent HPE GreenLake branding
- Moved source code into `greenlake_service_catalog_mcp/` package folder to resolve namespace collisions when multiple MCP servers are installed in the same Python environment

### Added

- Added `server.json` MCP Registry manifest to support publishing to the MCP Registry (`registry.modelcontextprotocol.io`)

## [1.0.0] - 2026-04-22

### Added

- **Initial release** of HPE GreenLake Service Catalog MCP Server
- **Authentication**: OAuth2 integration with automatic token management
- **Core Tools**:
  - `getserviceoffer` - Retrieve detailed information about a specific service offer by ID
  - `getserviceoffers` - Retrieve a list of service offers by applying filters
  - `getserviceofferregions` - Retrieve a list of service offer regions by applying filters
  - `getserviceofferregion` - Retrieve detailed information about a specific service offer region
  - `get_service_manager_provisions_v1` - Retrieve a list of all service manager provision entries
  - `get_service_manager_provision_v1` - Retrieve details for a specific service manager provision entry
  - `get_service_managers_v1` - Get a list of available service managers
  - `get_service_manager_v1` - Retrieve details for a specific service manager
  - `getserviceprovisions` - Retrieve a list of service provisions by applying filters
  - `getserviceprovision` - Fetch service provision details for an ID
  - `service_managers_for_a_region_v1` - Retrieve service managers deployed to a particular region
  - `per_region_service_managers_v1` - Retrieve service managers categorized by region
- **Dynamic Tools** (when `MCP_TOOL_MODE=dynamic`):
  - `list_endpoints` - Discover available API endpoints with filtering
  - `get_endpoint_schema` - Get detailed schema information for endpoints
  - `invoke_dynamic_tool` - Execute API calls with runtime parameter validation  
- **Filtering & Search**:
  - OData 4.0 filter support for service offers, provisions, and regions
  - Cursor-based pagination with `next` parameter
  - Service offer filtering by category, service manager ID, status, slug
  - Service provision filtering by workspace, status, organization
  - Service region filtering by region, service offer ID, status
- **Output Formats**: JSON service catalog information
- **Configuration**: Environment-based configuration with logging controls

### Security

- **OAuth2 Authentication** with automatic token management
- **Read-only access** to all service catalog endpoints

### Technical Details

- **Python 3.10+** support
- **Model Context Protocol** v1.0 implementation
