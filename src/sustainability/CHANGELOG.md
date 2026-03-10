# Changelog - Sustainability Insight Center MCP Server

All notable changes to the HPE GreenLake Sustainability Insight Center MCP Server will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-03-10

### Added

- **Initial release** of HPE GreenLake Sustainability Insight Center MCP Server
- **Generated** by mcp-generator v1.1.1 from SIC OpenAPI specification
- **Authentication**: OAuth2 integration with automatic token refresh
- **Core Tools**:
  - `getusagebyentity` - Aggregated energy usage grouped by individual entities
  - `getusagetotals` - Total energy consumption, CO2 emissions, and costs
  - `getusagebyseries` - Energy usage as time series data
  - `getcloudusagebyentity` - Public cloud usage grouped by cloud entities
  - `getcloudusagetotals` - Total public cloud energy and emissions
  - `getcloudusagebyseries` - Public cloud usage as time series data
  - `getcoefficients` - List energy cost and CO2 emission coefficients
  - `getcoefficient` - Get a specific coefficient by ID
  - `getingests` - List data ingestion records
  - `getingest` - Get a specific ingest by ID
  - `getdatasources` - List data source configurations
  - `getdatasource` - Get a specific data source by ID
- **Dynamic Tools** (when `MCP_TOOL_MODE=dynamic`):
  - `list_endpoints` - Discover available API endpoints with filtering
  - `get_endpoint_schema` - Get detailed schema information for endpoints
  - `invoke_dynamic_tool` - Execute API calls with runtime parameter validation
- **Filtering Support**:
  - OData 4.0 subset (eq, in, and operators)
  - Tag-based filtering via filter-tags parameter
  - ISO 8601 time range queries (start-time, end-time)
  - Offset-based pagination with configurable limits
  - Multi-currency cost reporting (30+ currency codes)
- **Output Formats**: JSON structured data with energy, emissions, and cost metrics

### Security

- **OAuth2 Authentication** with automatic token management
- **URL-encoded path parameters** to prevent path-traversal attacks
- **Header sanitization** in dynamic tools to prevent injection attacks

### Technical Details

- **Python 3.10+** compatibility
- **Model Context Protocol** v1.0 compliance
- **FastMCP architecture** with lifespan context management
- **Comprehensive logging** via loguru to stderr
- **323 unit tests** with 89% code coverage
