# Sustainability_Insight_Center MCP Server

HPE GreenLake Sustainability_Insight_Center MCP Server provides read-only access to the HPE GreenLake Sustainability_Insight_Center APIs through the Model Context Protocol.

## Overview

This MCP server enables AI assistants and development tools to interact with HPE GreenLake Sustainability_Insight_Center programmatically. It follows the standardized MCP server architecture with shared authentication components and HTTP client adapters.

### Key Features

- **Read-only API access** to Sustainability_Insight_Center endpoints
- **Shared authentication** using OAuth2 with automatic token management
- **Standardized architecture** following HPE GreenLake MCP patterns
- **Type-safe implementations** using Pydantic models
- **Comprehensive logging** and error handling

## Quick Start

### Prerequisites

- Python 3.10 or higher
- [uv](https://github.com/astral-sh/uv) package manager
- HPE GreenLake workspace with API credentials

### Installation

1. Navigate to the service directory:

   ```bash
   cd src/sustainability-insight-center
   ```

2. Install dependencies:

   ```bash
   uv sync
   ```

3. Configure environment variables (see Configuration section)

4. Configure in your MCP client (see MCP Client Configuration section below)

## Configuration

Set the following environment variables:

| Variable | Required | Description | Example |
|----------|----------|-------------|---------|
| `GREENLAKE_API_BASE_URL` | Yes | Base URL for GreenLake APIs (regional) | `https://us-west.api.greenlake.hpe.com` |
| `GREENLAKE_AUTH_BASE_URL` | No | Base URL for OAuth2 token endpoint (always global) | `https://global.api.greenlake.hpe.com` (default) |
| `GREENLAKE_CLIENT_ID` | Yes | OAuth2 client ID | `your-client-id` |
| `GREENLAKE_CLIENT_SECRET` | Yes | OAuth2 client secret | `your-client-secret` |
| `GREENLAKE_WORKSPACE_ID` | Yes | Workspace identifier (token issuer auto-generated from this) | `your-workspace-id` |
| `MCP_TOOL_MODE` | No | Tool operation mode (see Tool Modes section) | `static` (default) or `dynamic` |
| `GREENLAKE_LOG_LEVEL` | No | Logging level for stderr output | `ERROR` (default), `WARNING`, `INFO`, `DEBUG` |
| `GREENLAKE_FILE_LOGGING` | No | Enable file logging to disk | `false` (default) or `true` |

## Logging

This MCP server uses [loguru](https://github.com/Delgan/loguru) for structured logging with strict MCP protocol compliance.

### Log Destinations

**stderr (Default)**:

- All diagnostic logs go to stderr (MCP protocol requirement)
- Controlled by `GREENLAKE_LOG_LEVEL` (default: `ERROR`)
- stdout is reserved exclusively for JSON-RPC messages

**File logging (Optional)**:

- Enable with `GREENLAKE_FILE_LOGGING=true`
- Logs written to: `~/.hpe/mcp-logs/sustainability-insight-center/sustainability-insight-center-mcp.log`
- Features:
  - Automatic rotation at 10 MB
  - 7-day retention policy
  - Always logs at DEBUG level for comprehensive diagnostics
  - Includes detailed context (module, function, line number)

### Configuration Examples

**Production (minimal logging)**:

```bash
export GREENLAKE_LOG_LEVEL=ERROR
# File logging disabled by default
```

**Development (verbose logging)**:

```bash
export GREENLAKE_LOG_LEVEL=DEBUG
export GREENLAKE_FILE_LOGGING=true
```

**Debugging specific issues**:

```bash
export GREENLAKE_LOG_LEVEL=INFO
export GREENLAKE_FILE_LOGGING=true
# Check logs at: ~/.hpe/mcp-logs/sustainability-insight-center/
```

### Log Filtering

The server automatically filters noisy third-party library logs:

- `httpx`, `httpcore`, `urllib3`, `asyncio` are limited to WARNING level and above
- This preserves important error messages (connection failures, timeouts, SSL issues)
- While suppressing verbose DEBUG/INFO output (connection pooling, retries)

## Tool Modes

This MCP server supports two different tool operation modes that can be switched at runtime:

### Static Mode (Default)

- **Individual tools**: Each API endpoint becomes a dedicated MCP tool
- **Type-safe**: Explicit tool definitions with compile-time validation  
- **Discoverable**: Tools appear individually in MCP client interfaces
- **Best for**: Smaller APIs with focused functionality

### Dynamic Mode

- **Meta-tools**: 3 generic tools that can handle any API endpoint
- **Runtime discovery**: Endpoints are discovered and validated at runtime
- **Memory efficient**: Lower overhead for large APIs
- **Best for**: Large APIs with many endpoints

**Tools available in dynamic mode:**

- `list_endpoints` - Discover available API endpoints with optional filtering
- `get_endpoint_schema` - Get detailed schema information for specific endpoints  
- `invoke_dynamic_tool` - Execute API calls with runtime parameter validation

### Switching Modes

Configure the `MCP_TOOL_MODE` environment variable in your MCP client configuration:

```json
{
  "servers": {
    "sustainability-insight-center": {
      "env": {
        "MCP_TOOL_MODE": "static"  // or "dynamic"
      }
    }
  }
}
```

- `static` - Individual tools per endpoint (default)
- `dynamic` - 3 generic meta-tools for all endpoints

## MCP Client Configuration

### VS Code

Add to your `.vscode/mcp.json`:

```json
{
  "servers": {
    "sustainability-insight-center": {
      "type": "stdio",
      "command": "uv",
      "args": ["run", "python", "__main__.py"],
      "cwd": "/path/to/mcp-generator/mcps/sustainability-insight-center",
      "env": {
        "GREENLAKE_API_BASE_URL": "https://us-west.api.greenlake.hpe.com",
        "GREENLAKE_AUTH_BASE_URL": "https://global.api.greenlake.hpe.com",
        "GREENLAKE_CLIENT_ID": "your-client-id",
        "GREENLAKE_CLIENT_SECRET": "your-client-secret",
        "GREENLAKE_WORKSPACE_ID": "your-workspace-id",
        "MCP_TOOL_MODE": "static",
        "GREENLAKE_LOG_LEVEL": "INFO",
        "GREENLAKE_FILE_LOGGING": "false"
      }
    }
  }
}
```

### Claude Desktop

Add to your `claude_desktop_config.json`:

```json
{
  "servers": {
    "sustainability-insight-center": {
      "type": "stdio", 
      "command": "uv",
      "args": ["run", "python", "__main__.py"],
      "cwd": "/path/to/mcp-generator/mcps/sustainability-insight-center",
      "env": {
        "GREENLAKE_API_BASE_URL": "https://us-west.api.greenlake.hpe.com",
        "GREENLAKE_AUTH_BASE_URL": "https://global.api.greenlake.hpe.com",
        "GREENLAKE_CLIENT_ID": "your-client-id",
        "GREENLAKE_CLIENT_SECRET": "your-client-secret", 
        "GREENLAKE_WORKSPACE_ID": "your-workspace-id",
        "MCP_TOOL_MODE": "static",
        "GREENLAKE_LOG_LEVEL": "INFO",
        "GREENLAKE_FILE_LOGGING": "false"
      }
    }
  }
}
```

## Available Tools

This server provides the following MCP tools:

### getingest

- **Description**: Get metadata for an ingested 3rd party device measurement.
- **Method**: GET /sustainability-insight-ctr/v1beta1/ingests/{id}
- **Parameters**:

  - `id` (str, required):  
    UUID of the record

Example: 00000000-0000-0000-0000-0000000000000


### getusagebyentity

- **Description**: Retrieves an aggregated energy usage list grouped by individual entities over a defined time frame and supports filtering, sorting, and offset-based pagination.
- **Method**: GET /sustainability-insight-ctr/v1beta1/usage-by-entity
- **Parameters**:

  - `filter` (str, optional):  
    Limit the entities operated on by this endpoint, returning only the subset of entities that match the filter. The filter grammar is a subset of OData 4.0 supporting "eq", "in", and "and" operators only. Usage entities can be filtered by: - entityId - entityMake - entityModel - entityType - entitySerialNum - entityProductId - locationName - locationId - locationCity - locationState - locationCountry - name Examples: - locationCountry eq 'DE' - entityModel in ('ProLiant DL325
    Gen11', 'ProLiant DL380 Gen10') **Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`. Filterable properties: co2eMetricTon, cost, costUsd, currency, entityId, entityMake, entityManufacturerTimestamp, entityModel, entityProductId, entitySerialNum, entityType, id, kwh, locationCity, locationCountry, locationId, locationName, locationState, name, tags, type
  - `filter-tags` (str, optional):  
    Limit the entities operated on by this endpoint, returning only the subset of entities that contain the tags. The filter grammar is a subset of OData 4.0 supporting "eq" and "or" operators only. The tag key is on the left of the operator, the value is on the right. Examples: - 'Tagged' eq '' - 'OS' eq 'Linux' or 'OS' eq 'Windows' - 'OS' eq 'Linux' **Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`,
    `hasDetails eq 'true'`, `name eq 'example'`. Filterable properties: co2eMetricTon, cost, costUsd, currency, entityId, entityMake, entityManufacturerTimestamp, entityModel, entityProductId, entitySerialNum, entityType, id, kwh, locationCity, locationCountry, locationId, locationName, locationState, name, tags, type
  - `currency` (str, optional):  
    The 3 letter currency code the cost returned will be in, case insensitive. Currency calculations are done via a factor queried at the beginning of the day. Defaults to USD.


Example: CAD
  - `sort` (str, optional):  
    Odata 4.0 field to sort entities on. Allowed fields are the strings "locationName", "locationCountry", "locationState", "entityId", "entityMake", "entityModel", "entityType", "entitySerialNum", "entityProductId", "name". Must be of the format "property order".

Examples:
  - entityId desc
  - name asc
  - `offset` (int, optional):  
    Zero-based resource offset to start the response from.

Example: 10
  - `limit` (int, optional):  
    Number of usages to return.

Example: 10
  - `start-time` (str, required):  
    Start of the query's time range in ISO8601 format.

Example: 2024-01-28T08:00:00Z
  - `end-time` (str, required):  
    End of the query's time range in ISO8601 format.

Example: 2024-01-29T08:00:00Z


### getcoefficients

- **Description**: Get a list of all costs (amount per kWh) and co2 coefficients of all locations. Supports filtering by locationId.
- **Method**: GET /sustainability-insight-ctr/v1beta1/coefficients
- **Parameters**:

  - `offset` (int, optional):  
    Zero-based resource offset to start the response from.

Example: 10
  - `limit` (int, optional):  
    Number of entities to return.

Example: 10
  - `filter` (str, optional):  
    Limit the coefficients operated on by this endpoint, returning only the subset of entities that match the filter. The filter grammar is a subset of OData 4.0 supporting "eq" operator only. Coefficients can be filtered by: - locationId Example: locationId eq '00000000-0000-0000-0000-0000000000000' **Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`.
    Filterable properties: associatedLocation, co2eGramsPerKwh, costPerKwh, costUsdPerKwh, createdAt, currency, generation, id, startTime, type, updatedAt


### getusagetotals

- **Description**: Returns the total aggregated power cost, power consumption, and carbon emissions over a defined time frame and supports filtering by entities.
- **Method**: GET /sustainability-insight-ctr/v1beta1/usage-totals
- **Parameters**:

  - `filter` (str, optional):  
    Limit the entities operated on by this endpoint, returning only the usage for entities that match the filter. The filter grammar is a subset of OData 4.0 supporting "eq", "in", and "and" operators only. Usage entities can be filtered by: - entityId - entityMake - entityModel - entityType - entitySerialNum - entityProductId - locationName - locationId - locationCity - locationState - locationCountry Examples: - locationCountry eq 'DE' - entityModel in ('ProLiant DL325 Gen11',
    'ProLiant DL380 Gen10') **Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`. Filterable properties: co2eMetricTon, cost, costUsd, currency, kwh, type
  - `filter-tags` (str, optional):  
    Limit the entities operated on by this endpoint, returning only the subset of entities that contain the tags. The filter grammar is a subset of OData 4.0 supporting "eq" and "or" operators only. The tag key is on the left of the operator, the value is on the right. Examples: - 'OS' eq 'Linux' or 'OS' eq 'Windows' - 'OS' eq 'Linux' - 'Tagged' eq '' **Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`,
    `hasDetails eq 'true'`, `name eq 'example'`. Filterable properties: co2eMetricTon, cost, costUsd, currency, kwh, type
  - `currency` (str, optional):  
    The 3 letter currency code the cost returned will be in, case insensitive. Currency calculations are done via a factor queried at the beginning of the day. Defaults to USD.


Example: CAD
  - `start-time` (str, required):  
    Start of the query's time range in ISO8601 format.

Example: 2024-01-28T08:00:00Z
  - `end-time` (str, required):  
    End of the aggregate's time range in ISO8601 format.

Example: 2024-01-29T08:00:00Z


### getcloudusagetotals

- **Description**: Returns the total carbon footprint over a defined time frame and supports filtering by cloud entities.
- **Method**: GET /sustainability-insight-ctr/v1beta1/cloud-usage-totals
- **Parameters**:

  - `filter` (str, optional):  
    Limit the cloud entities operated on by this endpoint, returning only the subset of entities that match the filter. The filter grammar is a subset of OData 4.0 supporting "eq", "in", and "and" operators only. Cloud entities can be filtered by: - entityId - serviceProvider - serviceName - serviceRegion - serviceAccount - name Examples: - serviceProvider eq 'AWS' - serviceRegion in ('EMEA', 'AMERICAS') **Important**: All filter values must be enclosed in single quotes,
    including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`. Filterable properties: co2eMetricTon, type
  - `start-time` (str, required):  
    Start of the query's time range in ISO8601 format.

Example: 2024-01-28T08:00:00Z
  - `end-time` (str, required):  
    End of the aggregate's time range in ISO8601 format.

Example: 2024-01-29T08:00:00Z


### getdatasource

- **Description**: Get information such as name and data collection times for a SIC data source.
- **Method**: GET /sustainability-insight-ctr/v1beta1/datasources/{id}
- **Parameters**:

  - `id` (str, required):  
    ID of the data source

Example: 00000000-0000-0000-0000-0000000000000


### getusagebyseries

- **Description**: Retrieves aggregated energy usage statistics grouped by time bucket over a defined time frame and supports filtering by entities. Behavior is non-deterministic if the time range does not divide evenly by your selected interval.
- **Method**: GET /sustainability-insight-ctr/v1beta1/usage-series
- **Parameters**:

  - `filter` (str, optional):  
    Limit the entities operated on by this endpoint, returning only the usage for entities that match the filter. The filter grammar is a subset of OData 4.0 supporting "eq", "in", and "and" operators only. Usage entities can be filtered by: - entityId - entityMake - entityModel - entityType - entitySerialNum - entityProductId - locationName - locationId - locationCity - locationState - locationCountry Examples: - locationCountry eq 'DE' - entityModel in ('ProLiant DL325 Gen11',
    'ProLiant DL380 Gen10') **Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`. Filterable properties: co2eMetricTon, cost, costUsd, currency, id, kwh, timeBucket, type
  - `filter-tags` (str, optional):  
    Limit the entities operated on by this endpoint, returning only the subset of entities that contain the tags. The filter grammar is a subset of OData 4.0 supporting "eq" and "or" operators only. The tag key is on the left of the operator, the value is on the right. Examples: - 'OS' eq 'Linux' - 'Tagged' eq '' - 'OS' eq 'Linux' or 'OS' eq 'Windows' **Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`,
    `hasDetails eq 'true'`, `name eq 'example'`. Filterable properties: co2eMetricTon, cost, costUsd, currency, id, kwh, timeBucket, type
  - `currency` (str, optional):  
    The 3 letter currency code the cost returned will be in, case insensitive. Currency calculations are done via a factor queried at the beginning of the day. Defaults to USD.


Example: CAD
  - `interval` (str, required):  
    Interval of the created time series. Must be of the format "integer unit". Valid units are day(s), hour(s), week(s), month(s), and year(s).

Examples:
  - 2 hours
  - 1 day
  - `start-time` (str, required):  
    Start of the query's time range in ISO8601 format.

Example: 2024-01-28T08:00:00Z
  - `end-time` (str, required):  
    End of the query's time range in ISO8601 format.

Example: 2024-01-29T08:00:00Z


### getcloudusagebyentity

- **Description**: Retrieves aggregated carbon footprint usage in a list grouped by individual cloud entities, i.e., cloud services, over a 
defined time frame and supports filtering, sorting, and offset-based pagination.

- **Method**: GET /sustainability-insight-ctr/v1beta1/cloud-usage-by-entity
- **Parameters**:

  - `filter` (str, optional):  
    Limit the cloud entities operated on by this endpoint, returning only the subset of entities that match the filter. The filter grammar is a subset of OData 4.0 supporting "eq", "in", and "and" operators only. Cloud entities can be filtered by: - entityId - serviceProvider - serviceName - serviceRegion - serviceAccount - name Examples: - serviceProvider eq 'AWS' - serviceRegion in ('EMEA', 'AMERICAS') **Important**: All filter values must be enclosed in single quotes,
    including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`. Filterable properties: co2eMetricTon, entityId, id, name, serviceAccount, serviceName, serviceProvider, serviceRegion, type
  - `sort` (str, optional):  
    Odata 4.0 field to sort entities on. Allowed fields are the strings "entityId", "serviceProvider", "serviceName", "serviceRegion", "serviceAccount", "name". Must be of the format "property order".

Examples:
  - entityId desc
  - serviceAccount asc
  - `offset` (int, optional):  
    Zero-based resource offset to start the response from.

Example: 10
  - `limit` (int, optional):  
    Number of usages to return.

Example: 10
  - `start-time` (str, required):  
    Start of the query's time range in ISO8601 format.

Example: 2024-01-28T08:00:00Z
  - `end-time` (str, required):  
    End of the query's time range in ISO8601 format.

Example: 2024-01-29T08:00:00Z


### getcloudusagebyseries

- **Description**: Retrieves aggregated carbon footprint usage statistics grouped by time bucket over a defined time frame and 
supports filtering by entities. Behavior is non-deterministic if the time range does not divide evenly by your selected 
interval.

- **Method**: GET /sustainability-insight-ctr/v1beta1/cloud-usage-series
- **Parameters**:

  - `filter` (str, optional):  
    Limit the cloud entities operated on by this endpoint, returning only the subset of entities that match the filter. The filter grammar is a subset of OData 4.0 supporting "eq", "in", and "and" operators only. Cloud entities can be filtered by: - entityId - serviceProvider - serviceName - serviceRegion - serviceAccount - name Examples: - serviceRegion in ('EMEA', 'AMERICAS') - serviceProvider eq 'AWS' **Important**: All filter values must be enclosed in single quotes,
    including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`. Filterable properties: co2eMetricTon, id, timeBucket, type
  - `interval` (str, required):  
    Interval of the created time series. Must be of the format "integer unit". Valid units are day(s), hour
(s), week(s), month(s), and year(s). Cloud usage typically is measured in months, so the smaller time units are 
likely to be approximations.


Examples:
  - 3 months
  - 1 month
  - `start-time` (str, required):  
    Start of the query's time range in ISO8601 format.

Example: 2024-01-28T08:00:00Z
  - `end-time` (str, required):  
    End of the query's time range in ISO8601 format.

Example: 2024-01-29T08:00:00Z


### getcoefficient

- **Description**: Get a single cost and co2 coefficient for an id
- **Method**: GET /sustainability-insight-ctr/v1beta1/coefficients/{id}
- **Parameters**:

  - `id` (str, required):  
    UUID of the coefficient mapping

Example: 00000000-0000-0000-0000-0000000000000


### getdatasources

- **Description**: This returns information such as name and data collection times for each SIC data source.
- **Method**: GET /sustainability-insight-ctr/v1beta1/datasources
- **Parameters**:

  - None


### getingests

- **Description**: This returns the associated metadata of each uploaded 3rd party device measurement.
- **Method**: GET /sustainability-insight-ctr/v1beta1/ingests
- **Parameters**:

  - `offset` (int, optional):  
    Zero-based resource offset to start the response from.

Example: 10
  - `limit` (int, optional):  
    Number of ingested records to return.

Example: 10




## Typical Use Cases

This MCP server enables AI assistants to answer natural language questions about your HPE GreenLake Sustainability_Insight_Center resources. Here are some example queries you can try:

**Sustainability_Insight_Center Queries:**

- "List all sustainability_insight_center resources"
- "Show me details for specific sustainability_insight_center items"
- "Find sustainability_insight_center by specific criteria"
- "Get status of sustainability_insight_center resources"
- "Show me recent sustainability_insight_center changes"

These are just examples - you can ask questions in your own words, and the AI assistant will use the appropriate MCP tools to retrieve the information from HPE GreenLake.

## API Coverage

This MCP server implements read-only access to the following Sustainability_Insight_Center API endpoints:

- `GET /sustainability-insight-ctr/v1beta1/ingests/{id}` - Get metadata for an ingested 3rd party device measurement.
- `GET /sustainability-insight-ctr/v1beta1/usage-by-entity` - Retrieves an aggregated energy usage list grouped by individual entities over a defined time frame and supports filtering, sorting, and offset-based pagination.
- `GET /sustainability-insight-ctr/v1beta1/coefficients` - Get a list of all costs (amount per kWh) and co2 coefficients of all locations. Supports filtering by locationId.
- `GET /sustainability-insight-ctr/v1beta1/usage-totals` - Returns the total aggregated power cost, power consumption, and carbon emissions over a defined time frame and supports filtering by entities.
- `GET /sustainability-insight-ctr/v1beta1/cloud-usage-totals` - Returns the total carbon footprint over a defined time frame and supports filtering by cloud entities.
- `GET /sustainability-insight-ctr/v1beta1/datasources/{id}` - Get information such as name and data collection times for a SIC data source.
- `GET /sustainability-insight-ctr/v1beta1/usage-series` - Retrieves aggregated energy usage statistics grouped by time bucket over a defined time frame and supports filtering by entities. Behavior is non-deterministic if the time range does not divide evenly by your selected interval.
- `GET /sustainability-insight-ctr/v1beta1/cloud-usage-by-entity` - Retrieves aggregated carbon footprint usage in a list grouped by individual cloud entities, i.e., cloud services, over a 
defined time frame and supports filtering, sorting, and offset-based pagination.

- `GET /sustainability-insight-ctr/v1beta1/cloud-usage-series` - Retrieves aggregated carbon footprint usage statistics grouped by time bucket over a defined time frame and 
supports filtering by entities. Behavior is non-deterministic if the time range does not divide evenly by your selected 
interval.

- `GET /sustainability-insight-ctr/v1beta1/coefficients/{id}` - Get a single cost and co2 coefficient for an id
- `GET /sustainability-insight-ctr/v1beta1/datasources` - This returns information such as name and data collection times for each SIC data source.
- `GET /sustainability-insight-ctr/v1beta1/ingests` - This returns the associated metadata of each uploaded 3rd party device measurement.


## Development

### Commands

```bash
make help          # Show available commands
make install       # Install dependencies
make test          # Run tests
make clean         # Clean build artifacts
```

### Project Structure

```text
sustainability-insight-center/
├── __main__.py             # Entry point
├── pyproject.toml          # Dependencies and configuration
├── README.md               # This file
├── Makefile                # Development commands
├── auth/                   # Authentication components
│   ├── __init__.py
│   ├── oauth2_provider.py  # OAuth2 client credentials
│   └── token_manager.py    # Token lifecycle management
├── config/                 # Configuration management
│   ├── __init__.py
│   ├── logging.py          # Logging configuration
│   └── settings.py         # Application settings
├── models/                 # Data models
│   ├── __init__.py
│   └── base.py             # Base model classes
├── server/                 # MCP server implementation
│   ├── __init__.py
│   ├── app.py              # Application factory
│   └── mcp_server.py       # MCP server core
├── tools/                  # MCP tools
│   ├── __init__.py
│   ├── base.py             # Base tool class
│   ├── registry.py         # Tool registration
│   └── implementations/    # Tool implementations
│       ├── __init__.py
│       └── example_tool.py # Example tool template
├── tests/                  # Test suite
│   ├── __init__.py
│   ├── conftest.py         # Shared fixtures
│   ├── shared/
│   │   └── http.py        # Testing helpers
│   ├── unit/
│   │   ├── __init__.py
│   │   └── test_*.py      # Unit tests
│   └── integration/
│       ├── __init__.py
│       └── test_live_tools.py
└── utils/                  # Utility modules
    ├── __init__.py
    └── http_client.py      # HTTP client utilities
```

### Adding New Tools

1. Create a new tool file in `tools/implementations/`
2. Inherit from `BaseTool` and implement required methods
3. Add the tool to `tools/registry.py`
4. Write tests in `tests/`
5. Update this README

## Testing

The test suite reads credentials from environment variables. Export the following variables before running integration tests:

```bash
export GREENLAKE_CLIENT_ID=your-client-id
export GREENLAKE_CLIENT_SECRET=your-client-secret
export GREENLAKE_WORKSPACE_ID=your-workspace-id
export GREENLAKE_API_BASE_URL=https://us-west.api.greenlake.hpe.com
export GREENLAKE_AUTH_BASE_URL=https://global.api.greenlake.hpe.com
```

**Run the full test suite** (unit + integration when credentials are present):

```bash
make test
```

**Run unit-only checks:**

```bash
make test-unit
```

**Integration smoke tests** require the variables above plus any tool arguments (`MCP_TEST_SUSTAINABILITY_INSIGHT_CENTER_<PARAM_NAME>`):

```bash
make test-integration
```

The generated suite provides:

- Unit tests for tools, server wiring, and models
- Shared fixtures and helpers for deterministic behaviour
- Integration tests guarded by environment variable checks
- Coverage reporting within the unit suite

## Troubleshooting

### Common Issues

**Server won't start:**

- Verify environment variables are set
- Check uv dependencies are installed
- Review log output for specific errors

**Authentication failures:**

- Verify client credentials are valid
- Check workspace ID is correct
- Ensure network connectivity to GreenLake

**Tool execution errors:**

- Check API endpoint availability
- Verify request parameters
- Review error logs for details

## Contributing

1. Fork the repository
2. Create a feature branch
3. Implement changes following project standards
4. Add tests for new functionality
5. Submit a pull request

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](../../LICENSE) file for details.
