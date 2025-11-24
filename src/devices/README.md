# devices MCP Server

HPE GreenLake devices MCP Server provides read-only access to the HPE GreenLake devices APIs through the Model Context Protocol.

## Overview

This MCP server enables AI assistants and development tools to interact with HPE GreenLake devices programmatically. It follows the standardized MCP server architecture with shared authentication components and HTTP client adapters.

### Key Features

- **Read-only API access** to devices endpoints
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
   cd src/devices
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
- Logs written to: `~/.hpe/mcp-logs/devices/devices-mcp.log`
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
# Check logs at: ~/.hpe/mcp-logs/devices/
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
    "devices": {
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
    "devices": {
      "type": "stdio",
      "command": "uv",
      "args": ["run", "python", "__main__.py"],
      "cwd": "/path/to/mcp-generator/mcps/devices",
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
    "devices": {
      "type": "stdio", 
      "command": "uv",
      "args": ["run", "python", "__main__.py"],
      "cwd": "/path/to/mcp-generator/mcps/devices",
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

### getdevicesv1

- **Description**: With this API, you can: \<ul\>\<li\>Retrieve a list of devices managed in a workspace.\</li\> \<li\>Filter  devices based on conditional expressions.\</li\>\</ul\>\<p\>\<b\>NOTE\</b\>: You need view  permissions for Devices and Subscription service to invoke this API.\</p\>  Rate limits are enforced on this API. 160 requests per minute is supported per workspace. The API returns `429` if this threshold is breached.
- **Method**: GET /devices/v1/devices
- **Parameters**:

- `filter` (str, optional): Filter expressions consisting of simple comparison operations joined
by logical operators.\<br\>
| CLASS               |   EXAMPLES                                         |
|---------------------|----------------------------------------------------|
| Types               | integer, decimal, timestamp, string, boolean, null |
| Comparison          | eq, ne, gt, ge, lt, le, in                         |
| Logical Expressions | and, or, not                                       |

The following examples are not an exhaustive list of all possible filtering options.


Examples:
  - deviceType in 'COMPUTE', 'STORAGE'
    Return devices where a property is one of multiple values.
Example syntax, \<property\> in \<value\>,\<value\>.
  - deviceType eq 'STORAGE' and partNumber eq 'RTICXL6413'
    Return devices that exactly satisfy multiple filter queries.
Example syntax, \<property\> eq \<value\> and \<property\> eq \<value\>.
  - serialNumber eq 'STIAPL6404' or partNumber eq 'RTICXL6413'
    Return devices that exactly satisfy one of multiple filter queries.
Example syntax, \<property\> eq \<value\> or \<property\> eq \<value\>.
  - serialNumber eq 'STIAPL6404'
    Return devices where a property equals a value.
Example syntax, \<property\> eq \<value\>.
  - createdAt ge ''2024-01-18T19:53:51.480Z''
    Return devices where a property is greater or equal to a value.
Example syntax, \<property\> ge \<value\>.
  - updatedAt le '2024-02-18T19:53:51.480Z'
    Return devices where a property is lesser or equal to a value.
Example syntax, \<property\> ge \<value\>.
  - not serialNumber eq 'STIAPL6404'
    Return devices where a property does not equal a value.
Example syntax, not \<property\> eq \<value\>.

**Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`.

Filterable properties: application, archived, assignedState, createdAt, deviceType, id, location, macAddress, model, partNumber, region, serialNumber, subscription, tags, tenantWorkspaceId, type, updatedAt, warranty
- `filter-tags` (str, optional): Filter expressions consisting of simple comparison operations joined
by logical operators to be applied on the assigned tags or their
values.\<br\>
| CLASS               |   EXAMPLES      |
|---------------------|-----------------|
| Types               | string          |
| Comparison          | eq, ne, in      |
| Logical Expressions | and, or, not    |


Examples:
  - 'street' in 'Regent Street', 'Oxford Street', 'Piccadilly'
    Return devices containing the tag key and at least one of the specified values.
Example syntax, \<property\> in \<value\>,\<value\>.
  - 'city' eq 'London' and 'street' eq 'Piccadilly'
    Return devices that exactly satisfy multiple filter queries applied to tag keys.
Example syntax, \<property\> eq \<value\> and \<property\> eq \<value\>.
  - 'street' eq 'Oxford Street' or 'street' eq 'Piccadilly'
    Return devices that satisfy any of multiple filter queries applied to tag keys.
Example syntax, \<property\> eq \<value\> or \<property\> eq \<value\>.
  - 'city' eq 'London'
    Return devices where a tag key is equal to a tag value.
Example syntax, \<tagKey\> eq \<tagValue\>.
  - not 'city' eq 'Tokyo'
    Return devices where a tag key does not equal a tag value.
Example syntax, not \<property\> eq \<value\>.

**Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`.

Filterable properties: application, archived, assignedState, createdAt, deviceType, id, location, macAddress, model, partNumber, region, serialNumber, subscription, tags, tenantWorkspaceId, type, updatedAt, warranty
- `sort` (str, optional): A comma separated list of sort expressions. A sort expression is a property name optionally followed by a direction indicator `asc` or `desc`. The default is ascending order.

Example: serialNumber,macAddress desc
- `select` (List[str], optional): A comma separated list of select properties to display in the response. The default is that all properties are returned.

Example: serialNumber,macAddress
- `limit` (int, optional): Specifies the number of results to be returned. The default value is 2000.
- `offset` (int, optional): Specifies the zero-based resource offset to start the response from. The default value is 0.


### getdevicebyidv1

- **Description**: Get details on a specific device by passing its resourceId. \<p\>\<b\>NOTE\</b\>: You need  view permissions for device management to invoke this API.\</p\> Rate limits are enforced on this API. 40 requests per minute is supported per workspace. The API returns `429` if this threshold is breached.
- **Method**: GET /devices/v1/devices/{id}
- **Parameters**:

- `id` (str, required): id parameter




## Typical Use Cases

This MCP server enables AI assistants to answer natural language questions about your HPE GreenLake devices resources. Here are some example queries you can try:

**Device Inventory:**

- "List all devices in my workspace"
- "Show me servers with specific serial numbers"
- "Find devices by model or type"
- "Show me device health status"

These are just examples - you can ask questions in your own words, and the AI assistant will use the appropriate MCP tools to retrieve the information from HPE GreenLake.

## API Coverage

This MCP server implements read-only access to the following devices API endpoints:

- `GET /devices/v1/devices` - With this API, you can: \<ul\>\<li\>Retrieve a list of devices managed in a workspace.\</li\> \<li\>Filter  devices based on conditional expressions.\</li\>\</ul\>\<p\>\<b\>NOTE\</b\>: You need view  permissions for Devices and Subscription service to invoke this API.\</p\>  Rate limits are enforced on this API. 160 requests per minute is supported per workspace. The API returns `429` if this threshold is breached.
- `GET /devices/v1/devices/{id}` - Get details on a specific device by passing its resourceId. \<p\>\<b\>NOTE\</b\>: You need  view permissions for device management to invoke this API.\</p\> Rate limits are enforced on this API. 40 requests per minute is supported per workspace. The API returns `429` if this threshold is breached.


API Version: latest


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
devices/
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

**Integration smoke tests** require the variables above plus any tool arguments (`MCP_TEST_DEVICES_<PARAM_NAME>`):

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

---

**Service**: devices  
**API Version**: latest  
**MCP Server Version**: 1.0.0
