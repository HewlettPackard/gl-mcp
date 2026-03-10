# Changelog - Sustainability MCP Server

All notable changes to the HPE GreenLake Sustainability Insight Center MCP Server will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-03-10

### Added

- **Initial release** of HPE GreenLake Sustainability Insight Center MCP Server
- **Authentication**: OAuth2 integration with automatic token refresh
- **Core Tools**:
  - `getusagebyentity` - Retrieve energy usage data per entity with filtering and pagination
  - `getusagetotals` - Get aggregated energy usage totals
  - `getusageseries` - Get energy usage time series data
  - `getcloudusagebyentity` - Retrieve cloud sustainability data per entity
  - `getcloudusagetotals` - Get aggregated cloud sustainability totals
  - `getcloudusageseries` - Get cloud sustainability time series data
  - `getcoefficients` - List cost and CO2 coefficients
  - `getcoefficientbyid` - Get a specific coefficient by ID
  - `getingests` - List uploaded device measurement ingests
  - `getingestbyid` - Get a specific ingest by ID
  - `getdatasources` - List data sources
  - `getdatasourcebyid` - Get a specific data source by ID
  - `forecastenergy` - Generate energy consumption forecasts
- **Dynamic Tools** (when `MCP_TOOL_MODE=dynamic`):
  - `list_endpoints` - Discover available API endpoints with filtering
  - `get_endpoint_schema` - Get detailed schema information for endpoints
  - `invoke_dynamic_tool` - Execute API calls with runtime parameter validation
- **Filtering Support**: OData-style filtering for usage and coefficient queries
- **Output Formats**: JSON structured data with comprehensive sustainability metrics
- **Configuration**: Environment-based configuration for credentials

### Security

- **OAuth2 Authentication** with automatic token management
- Path parameters use URL encoding for proper handling of special characters
- Dynamic tools sanitize user-provided headers to prevent injection attacks

### Technical Details

- **Python 3.10+** compatibility
- **Model Context Protocol** v1.0 compliance
- **Comprehensive logging** for debugging and monitoring
