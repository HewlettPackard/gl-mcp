# reporting MCP Server

HPE GreenLake reporting MCP Server provides read-only access to the HPE GreenLake reporting APIs through the Model Context Protocol.

## Overview

This MCP server enables AI assistants and development tools to interact with HPE GreenLake reporting programmatically. It follows the standardized MCP server architecture with shared authentication components and HTTP client adapters.

### Key Features

- **Read-only API access** to reporting endpoints
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
   cd src/reporting
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
- Logs written to: `~/.hpe/mcp-logs/reporting/reporting-mcp.log`
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
# Check logs at: ~/.hpe/mcp-logs/reporting/
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
    "reporting": {
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
    "reporting": {
      "type": "stdio",
      "command": "uv",
      "args": ["run", "python", "__main__.py"],
      "cwd": "/path/to/mcp-generator/mcps/reporting",
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
    "reporting": {
      "type": "stdio", 
      "command": "uv",
      "args": ["run", "python", "__main__.py"],
      "cwd": "/path/to/mcp-generator/mcps/reporting",
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

### get_reporting_v1_report_exports_metadata

- **Description**: This API is a support tool that assists with generating a report. Use it to find the supported columns, filter criteria, and values for a report type.  In a response, the API returns:

  - `columns`&mdash;An array containing the supported columns.
  - `filterCriteria`&mdash;An array comprising of filter names and their corresponding data types.
  - `supportedOperators`&mdash;A collection of supported operators assisting you in selecting the correct operator to use in a filter attribute. The following operators are supported:
    - `EQ`&mdash;Checks if a field is equal to a value.
    - `NE`&mdash;Checks if a field is not equal to a value.
    - `LT`&mdash;Checks if a field is less than a value.
    - `LE`&mdash;Checks if a field is less than or equal to a value.
    - `GT`&mdash;Checks if a field is greater than a value.
    - `GE`&mdash;Checks if a field is greater than or equals to a value.
    - `IN`&mdash;Checks if a value is in a list.

- **Method**: GET /reporting/v1/report-exports-metadata
- **Parameters**:

  - `filter` (str, required):  
    Limit the resources operated on by an endpoint or when used with a multiple-GET endpoint, return only the subset of resources that match the filter. The filter grammar is a subset of OData 4.0. **NOTE:** The filter query parameter must use [URL encoding](https://en.wikipedia.org/wiki/URL_encoding). Most clients do this automatically with inputs provided to them specifically as query parameters. Encoding must be done manually for any query parameters provided as part of the
    URL. The reserved characters `!` `#` `$` `&` `'` `(` `)` `*` `+` `,` `/` `:` `;` `=` `?` `@` `[` `]` must be encoded with percent encoded equivalents. For example: the value `P06760-B21+2M212504P8` must be encoded as `P06760-B21%2B2M212504P8` when it is used in a query parameter. | CLASS | EXAMPLES | |-----------|----------------------------------------------------| | Types | integer, decimal, timestamp, string, boolean, null | | Operations| eq, ne, gt, ge, lt, le, in | |
    Logic | and, or, not | Example: name ne Subscriptions and group eq Device inventory **Filter Syntax**: Use OData-style filters. String values must be enclosed in single quotes. Filterable properties: columns, filterCriteria, id, kind, name, type
  - `select` (str, required):  
    The select query parameter is used to limit the properties returned for a resource. The value of the select query parameter is a comma-separated list of properties.

Example: map[equals:map[description:Return activities where a property equals a value.
 summary:select with equality check value:select=name]]

- `sort` (str, required):  
    The order in which to return the resources in the collection. The value of the sort query parameter is a comma separated list of sort expressions. Each sort expression is a property name optionally followed by a direction indicator asc (ascending) or desc (descending). The first sort expression in the list defines the primary sort order, the second defines the secondary sort order, and so on. If a direction indicator is omitted, the default direction is ascending. Examples: -
    name asc Order ascending by name - name,createdAt desc Order resources ascending by name and then by descending by createdAt
- `limit` (int, optional):  
    The maximum number of reports to return.

Example: 10

- `offset` (int, optional):  
    Zero-based resource offset to start the response from.

Example: 20

### getreportingstatuses

- **Description**: This API is designed to fetch the status of all reports for a specific workspace. Only reports belonging to the workspace ID and username are returned. This API supports pagination, allowing you to use offset and limit parameters.

- **Method**: GET /reporting/v1/statuses
- **Parameters**:

  - `filter` (str, required):  
    Example: type eq "REPORT"

**Filter Syntax**: Use OData-style filters. String values must be enclosed in single quotes.

Filterable properties: createdAt, description, id, isExpired, message, name, recipientEmailId, reportDownloadUrl, reportType, resourceUri, stage, startTime, status, statusTimestamp, type, userName

- `sort` (str, optional):  
    The order in which to return the resources in the collection.The value of the sort query parameter is a comma separated list of sort expressions. Each sort expression is a property name optionally followed by a direction indicator asc (ascending) or desc (descending).The first sort expression in the list defines the primary sort order, the second defines the secondary sort order, and so on. If a direction indicator is omitted the default direction is ascending. Examples: -
    name asc Order ascending by name - name,createdAt desc Order resources ascending by name and then by descending by createdAt
- `limit` (int, optional):  
    The maximum number of reports to return.

Example: 50

- `offset` (int, optional):  
    Zero-based resource offset to start the response from.

Example: 20

### getreportingstatusbyid

- **Description**: Retrieve the status of a specific report by passing the report status ID.

- **Method**: GET /reporting/v1/statuses/{id}
- **Parameters**:

  - `id` (str, required):  
    The report status identifier.

Example: 3fa85f64-5717-4562-b3fc-2c963f66afa6

## Typical Use Cases

This MCP server enables AI assistants to answer natural language questions about your HPE GreenLake reporting resources. Here are some example queries you can try:

**reporting Queries:**

- "List all reporting resources"
- "Show me details for specific reporting items"
- "Find reporting by specific criteria"
- "Get status of reporting resources"
- "Show me recent reporting changes"

These are just examples - you can ask questions in your own words, and the AI assistant will use the appropriate MCP tools to retrieve the information from HPE GreenLake.

## API Coverage

This MCP server implements read-only access to the following reporting API endpoints:

- `GET /reporting/v1/report-exports-metadata` - This API is a support tool that assists with generating a report. Use it to find the supported columns, filter criteria, and values for a report type.  In a response, the API returns:

  - `columns`&mdash;An array containing the supported columns.
  - `filterCriteria`&mdash;An array comprising of filter names and their corresponding data types.
  - `supportedOperators`&mdash;A collection of supported operators assisting you in selecting the correct operator to use in a filter attribute. The following operators are supported:
    - `EQ`&mdash;Checks if a field is equal to a value.
    - `NE`&mdash;Checks if a field is not equal to a value.
    - `LT`&mdash;Checks if a field is less than a value.
    - `LE`&mdash;Checks if a field is less than or equal to a value.
    - `GT`&mdash;Checks if a field is greater than a value.
    - `GE`&mdash;Checks if a field is greater than or equals to a value.
    - `IN`&mdash;Checks if a value is in a list.

- `GET /reporting/v1/statuses` - This API is designed to fetch the status of all reports for a specific workspace. Only reports belonging to the workspace ID and username are returned. This API supports pagination, allowing you to use offset and limit parameters.

- `GET /reporting/v1/statuses/{id}` - Retrieve the status of a specific report by passing the report status ID.

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
reporting/
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

**Integration smoke tests** require the variables above plus any tool arguments (`MCP_TEST_REPORTING_<PARAM_NAME>`):

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
