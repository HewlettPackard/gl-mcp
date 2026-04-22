# Changelog - Service Catalog MCP Server

All notable changes to the HPE GreenLake Service Catalog MCP Server will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
