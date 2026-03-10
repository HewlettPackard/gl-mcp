# sustainability MCP Server

HPE GreenLake Sustainability Insight Center MCP Server provides read-only access to the HPE GreenLake sustainability APIs through the Model Context Protocol.

## Overview

This MCP server enables AI assistants and development tools to interact with HPE GreenLake Sustainability Insight Center programmatically. It follows the standardized MCP server architecture with shared authentication components and HTTP client adapters.

### Key Features

- **Read-only API access** to sustainability endpoints
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
   cd src/sustainability
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
| `GREENLAKE_API_BASE_URL` | Yes | Base URL for GreenLake APIs | `https://global.api.greenlake.hpe.com` |
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
- Logs written to: `~/.hpe/mcp-logs/sustainability/sustainability-mcp.log`
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
# Check logs at: ~/.hpe/mcp-logs/sustainability/
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
    "sustainability": {
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
    "sustainability": {
      "type": "stdio",
      "command": "uv",
      "args": ["run", "python", "__main__.py"],
      "cwd": "/path/to/mcp-generator/mcps/sustainability",
      "env": {
        "GREENLAKE_API_BASE_URL": "https://global.api.greenlake.hpe.com",
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
    "sustainability": {
      "type": "stdio", 
      "command": "uv",
      "args": ["run", "python", "__main__.py"],
      "cwd": "/path/to/mcp-generator/mcps/sustainability",
      "env": {
        "GREENLAKE_API_BASE_URL": "https://global.api.greenlake.hpe.com",
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

### getusagebyentity

- **Description**: Get energy usage data grouped by entity (device). Returns energy consumption (kWh), carbon footprint (CO2e metric tons), and estimated energy cost per entity with location details.
- **Method**: GET /sustainability-insight-ctr/v1beta1/usage-by-entity
- **Parameters**:

  - `start-time` (str, required): Start time in ISO 8601 format (e.g. '2024-01-01T00:00:00Z').
  - `end-time` (str, required): End time in ISO 8601 format (e.g. '2024-01-31T23:59:59Z').
  - `filter` (str, optional): Filter expression for narrowing results.
  - `filter-tags` (str, optional): Filter by tags.
  - `currency` (str, optional): Currency code for energy cost (e.g. 'USD').
  - `sort` (str, optional): Sort order for results.
  - `offset` (int, optional): Specifies the zero-based resource offset to start the response from.
  - `limit` (int, optional): How many items to return at one time.

### getusagetotals

- **Description**: Get total aggregated energy usage across all entities for a defined time frame. Returns total energy consumption (kWh), carbon footprint (CO2e metric tons), and estimated energy cost.
- **Method**: GET /sustainability-insight-ctr/v1beta1/usage-totals
- **Parameters**:

  - `start-time` (str, required): Start time in ISO 8601 format (e.g. '2024-01-01T00:00:00Z').
  - `end-time` (str, required): End time in ISO 8601 format (e.g. '2024-01-31T23:59:59Z').
  - `filter` (str, optional): Filter expression for narrowing results.
  - `filter-tags` (str, optional): Filter by tags.
  - `currency` (str, optional): Currency code for energy cost (e.g. 'USD').

### getusageseries

- **Description**: Get energy usage data grouped by time buckets. Returns time series of energy consumption (kWh), carbon footprint (CO2e metric tons), and cost. The interval parameter format is 'integer unit' (e.g. '1 day', '2 hours', '1 month', '1 year').
- **Method**: GET /sustainability-insight-ctr/v1beta1/usage-series
- **Parameters**:

  - `start-time` (str, required): Start time in ISO 8601 format (e.g. '2024-01-01T00:00:00Z').
  - `end-time` (str, required): End time in ISO 8601 format (e.g. '2024-01-31T23:59:59Z').
  - `interval` (str, required): Time bucket interval in format 'integer unit' (e.g. '1 day', '2 hours', '1 month', '1 year').
  - `filter` (str, optional): Filter expression for narrowing results.
  - `filter-tags` (str, optional): Filter by tags.
  - `currency` (str, optional): Currency code for energy cost (e.g. 'USD').

### getcloudusagebyentity

- **Description**: Get public cloud sustainability data grouped by entity. Returns CO2 emissions data for cloud services (AWS, Azure, etc.) per service account and region.
- **Method**: GET /sustainability-insight-ctr/v1beta1/cloud-usage-by-entity
- **Parameters**:

  - `start-time` (str, required): Start time in ISO 8601 format (e.g. '2024-01-01T00:00:00Z').
  - `end-time` (str, required): End time in ISO 8601 format (e.g. '2024-01-31T23:59:59Z').
  - `filter` (str, optional): Filter expression for narrowing results.
  - `sort` (str, optional): Sort order for results.
  - `offset` (int, optional): Specifies the zero-based resource offset to start the response from.
  - `limit` (int, optional): How many items to return at one time.

### getcloudusagetotals

- **Description**: Get total aggregated public cloud sustainability data. Returns total CO2 emissions (metric tons) across all cloud entities.
- **Method**: GET /sustainability-insight-ctr/v1beta1/cloud-usage-totals
- **Parameters**:

  - `start-time` (str, required): Start time in ISO 8601 format (e.g. '2024-01-01T00:00:00Z').
  - `end-time` (str, required): End time in ISO 8601 format (e.g. '2024-01-31T23:59:59Z').
  - `filter` (str, optional): Filter expression for narrowing results.

### getcloudusageseries

- **Description**: Get public cloud sustainability data grouped by time buckets. Returns time series of CO2 emissions for cloud services.
- **Method**: GET /sustainability-insight-ctr/v1beta1/cloud-usage-series
- **Parameters**:

  - `start-time` (str, required): Start time in ISO 8601 format (e.g. '2024-01-01T00:00:00Z').
  - `end-time` (str, required): End time in ISO 8601 format (e.g. '2024-01-31T23:59:59Z').
  - `interval` (str, required): Time bucket interval in format 'integer unit' (e.g. '1 day', '2 hours', '1 month', '1 year').
  - `filter` (str, optional): Filter expression for narrowing results.

### getcoefficients

- **Description**: Get cost and CO2 coefficients. Returns the configured energy cost (per kWh) and CO2 emission rate (grams per kWh) for each location.
- **Method**: GET /sustainability-insight-ctr/v1beta1/coefficients
- **Parameters**:

  - `filter` (str, optional): Filter expression (only locationId is filterable).
  - `filter-tags` (str, optional): Filter by tags.
  - `currency` (str, optional): Currency code for energy cost (e.g. 'USD').
  - `offset` (int, optional): Specifies the zero-based resource offset to start the response from.
  - `limit` (int, optional): How many items to return at one time.

### getcoefficientbyid

- **Description**: Get a specific cost and CO2 coefficient by ID.
- **Method**: GET /sustainability-insight-ctr/v1beta1/coefficients/{id}
- **Parameters**:

  - `id` (str, required): The UUID of the coefficient to retrieve.

### getingests

- **Description**: Get metadata for all uploaded device measurement data imports.
- **Method**: GET /sustainability-insight-ctr/v1beta1/ingests
- **Parameters**:

  - `offset` (int, optional): Specifies the zero-based resource offset to start the response from.
  - `limit` (int, optional): How many items to return at one time.

### getingestbyid

- **Description**: Get metadata for a specific uploaded device measurement by ID.
- **Method**: GET /sustainability-insight-ctr/v1beta1/ingests/{id}
- **Parameters**:

  - `id` (str, required): The UUID of the ingest record to retrieve.

### getdatasources

- **Description**: Get all HPE Sustainability Insight Center data sources. Returns information about connected data sources including collection times.
- **Method**: GET /sustainability-insight-ctr/v1beta1/datasources
- **Parameters**:

  - `offset` (int, optional): Specifies the zero-based resource offset to start the response from.
  - `limit` (int, optional): How many items to return at one time.

### getdatasourcebyid

- **Description**: Get details of a specific data source by ID.
- **Method**: GET /sustainability-insight-ctr/v1beta1/datasources/{id}
- **Parameters**:

  - `id` (str, required): The UUID of the data source to retrieve.

### forecastenergy

- **Description**: Get forecasted energy consumption (kWh), CO2 emissions, and costs with confidence intervals for 1 to 6 months into the future. Also returns 3 months of historical data and sustainability journey comparison.
- **Method**: POST /sustainability-insight-ctr/v1beta1/forecast/energy
- **Parameters**:

  - `timePeriodMonths` (int, required): Number of months to forecast (1-6).
  - `currencyCode` (str, required): Currency code for energy cost (e.g. 'USD').

## Typical Use Cases

This MCP server enables AI assistants to answer natural language questions about your HPE GreenLake sustainability resources. Here are some example queries you can try:

**Energy Consumption:**

- "What is the total energy consumption for the last month?"
- "Show me energy usage per device for Q1 2024"
- "Which devices consume the most energy?"
- "Give me a daily energy usage breakdown for January"

**Carbon Footprint:**

- "What is our total CO2 footprint for this quarter?"
- "Show me carbon emissions trends over the past 6 months"
- "Which cloud services have the highest carbon emissions?"
- "Compare on-premises vs cloud carbon footprint"

**Cloud Sustainability:**

- "Show me AWS carbon emissions by service"
- "What are the cloud CO2 totals for the last month?"
- "Give me a monthly cloud emissions time series"

**Cost Analysis:**

- "What is the total energy cost in USD for the last quarter?"
- "Show me the energy cost coefficients for each location"
- "Forecast energy costs for the next 3 months"

**Forecasting:**

- "Forecast our energy consumption for the next 6 months"
- "What is the expected CO2 emissions trend?"
- "Show me predicted energy costs with confidence intervals"

**Data Management:**

- "List all configured data sources"
- "Show me the available device measurement ingests"
- "What are the current CO2 and cost coefficients?"

These are just examples - you can ask questions in your own words, and the AI assistant will use the appropriate MCP tools to retrieve the information from HPE GreenLake.

## API Coverage

This MCP server implements read-only access to the following sustainability API endpoints:

- `GET /sustainability-insight-ctr/v1beta1/usage-by-entity` - Get energy usage data grouped by entity (device)
- `GET /sustainability-insight-ctr/v1beta1/usage-totals` - Get total aggregated energy usage
- `GET /sustainability-insight-ctr/v1beta1/usage-series` - Get energy usage time series data
- `GET /sustainability-insight-ctr/v1beta1/cloud-usage-by-entity` - Get cloud sustainability data per entity
- `GET /sustainability-insight-ctr/v1beta1/cloud-usage-totals` - Get aggregated cloud sustainability totals
- `GET /sustainability-insight-ctr/v1beta1/cloud-usage-series` - Get cloud sustainability time series
- `GET /sustainability-insight-ctr/v1beta1/coefficients` - List cost and CO2 coefficients
- `GET /sustainability-insight-ctr/v1beta1/coefficients/{id}` - Get a specific coefficient
- `GET /sustainability-insight-ctr/v1beta1/ingests` - List device measurement ingests
- `GET /sustainability-insight-ctr/v1beta1/ingests/{id}` - Get a specific ingest
- `GET /sustainability-insight-ctr/v1beta1/datasources` - List data sources
- `GET /sustainability-insight-ctr/v1beta1/datasources/{id}` - Get a specific data source
- `POST /sustainability-insight-ctr/v1beta1/forecast/energy` - Generate energy consumption forecasts

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
sustainability/
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
│       └── *.py            # 13 static tools + 3 dynamic tools
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
export GREENLAKE_API_BASE_URL=https://global.api.greenlake.hpe.com
```

**Run the full test suite** (unit + integration when credentials are present):

```bash
make test
```

**Run unit-only checks:**

```bash
make test-unit
```

**Integration smoke tests** require the variables above plus any tool arguments (`MCP_TEST_SUSTAINABILITY_<PARAM_NAME>`):

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
