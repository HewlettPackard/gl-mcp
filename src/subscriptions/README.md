# subscriptions MCP Server

HPE GreenLake subscriptions MCP Server provides read-only access to the HPE GreenLake subscriptions APIs through the Model Context Protocol.

## Overview

This MCP server enables AI assistants and development tools to interact with HPE GreenLake subscriptions programmatically. It follows the standardized MCP server architecture with shared authentication components and HTTP client adapters.

### Key Features

- **Read-only API access** to subscriptions endpoints
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
   cd src/subscriptions
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
- Logs written to: `~/.hpe/mcp-logs/subscriptions/subscriptions-mcp.log`
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
# Check logs at: ~/.hpe/mcp-logs/subscriptions/
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
    "subscriptions": {
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
    "subscriptions": {
      "type": "stdio",
      "command": "uv",
      "args": ["run", "python", "__main__.py"],
      "cwd": "/path/to/mcp-generator/mcps/subscriptions",
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
    "subscriptions": {
      "type": "stdio", 
      "command": "uv",
      "args": ["run", "python", "__main__.py"],
      "cwd": "/path/to/mcp-generator/mcps/subscriptions",
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

### getsubscriptionsv1

- **Description**: Get subscriptions managed in a workspace. Filters can be passed to filter  the subscriptions based on conditional expressions.\<br\>\<br\>**NOTE:** You need to have  view permission for the **Devices and subscription service** to invoke this API. \<br\>\<br\> Rate limits are enforced on this API. 60 requests per minute is supported per workspace. API will result in `429` if this threshold is breached.
- **Method**: GET /subscriptions/v1/subscriptions
- **Parameters**:

- `filter` (str, optional): Filter expressions consisting of simple comparison operations joined 
by logical operators.\<br\>
| CLASS                |   EXAMPLES                                         |
|----------------------|----------------------------------------------------|
| Types                | integer, decimal, timestamp, string, boolean, null |
| Comparison           | eq, ne, gt, ge, lt, le, in                         |
| Logical Expressions  | and, or, not                                       |

Subscriptions can be filtered based on the following properties:
- `id`
- `subscriptionType`
- `subscriptionStatus`
- `key`
- `quantity`
- `availableQuantity`
- `sku`
- `skuDescription`
- `contract`
- `startTime`
- `endTime`
- `productType`
- `tier`
- `createdAt`
- `updatedAt`

The following is a non-exhaustive list of possible filtering options.


Examples:
  - startTime gt '2024-01-23T00:00:00.000Z' and endTime lt '2025-02-22T00:00:00.000Z' and not productType eq 'SERVICE'
    The AND, OR, and NOT operators can be combined to return results that satisfy all specified filter criteria.
  - updatedAt le '2024-02-18T19:53:51.480Z'
    Return subscriptions where a property is less than or equal to a value. Example syntax,
\<property\> le \<value\>.
  - tier ne 'BRIDGE'
    Return subscriptions where a property does not equate to a value. Example syntax, 
\<property\> ne \<value\>.
  - not key eq 'STIAPL6404'
    Return subscriptions where a property does not equal a value. Example syntax, 
not \<property\> eq \<value\>.
  - subscriptionType in 'CENTRAL_STORAGE', 'CENTRAL_CONTROLLER'
    Return subscriptions where the property is one of multiple values. Example syntax, 
\<property\> in \<value\>,\<value\>.
  - key eq 'STIQQ4L04' and subscriptionType eq 'CENTRAL_STORAGE'
    The AND operator returns results that meet all filter queries. In the example, the query only returns subscriptions with the exact key and with the specified subscription type. Example syntax,
\<property\> eq \<value\> and \<property\> eq \<value\>.
  - key eq 'STIQQ4L04' or subscriptionType eq 'CENTRAL_STORAGE'
    The OR operator returns results that meet any of the filter queries. In the example, the query returns subscriptions with the exact key or with the specified subscription type.
  - key eq 'STIAPL6404'
    Return subscriptions where a property equals a value. Example syntax, 
\<property\> eq \<value\>.
  - createdAt ge '2024-01-18T19:53:51.480Z'
    Return subscriptions where a property is greater or equal to a value. Example syntax,
\<property\> ge \<value\>.

**Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`.

Filterable properties: availableQuantity, contract, createdAt, endTime, id, isEval, key, productType, quantity, sku, skuDescription, startTime, subscriptionStatus, subscriptionType, tags, tier, type, updatedAt
- `filter-tags` (str, optional): Filter expressions consisting of simple comparison operations joined
by logical operators to be applied on the assigned tags or their
values.\<br\>
| CLASS               |   EXAMPLES      |
|---------------------|-----------------|
| Types               | string          |
| Comparison          | eq, ne          |
| Logical Expressions | and, or         |


Examples:
  - 'city' eq 'London' and 'street' eq 'Piccadilly'
    Return subscriptions containing the tag key and the corresponding value that satisfy all conditionals. Example syntax, 
\<property\> eq \<value\> and \<property\> eq \<value\>.
  - 'street' eq 'Oxford Street' or 'street' eq 'Piccadilly'
    Return subscriptions containing the tag key and the corresponding value that satisfy at least one of the conditionals. Example syntax, 
\<property\> eq \<value\> or \<property\> eq \<value\>.
  - 'city' eq 'London'
    Return subscriptions that have a pair of tags with the exact same tag key and tag value. Example syntax, 
\<tagKey\> eq \<tagValue\>.
  - 'city' ne 'London'
    Return subscriptions that have a pair of tags with the exact same tag key and the exact different tag value. Example syntax, 
\<tagKey\> ne \<tagValue\>.

**Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`.

Filterable properties: availableQuantity, contract, createdAt, endTime, id, isEval, key, productType, quantity, sku, skuDescription, startTime, subscriptionStatus, subscriptionType, tags, tier, type, updatedAt
- `sort` (str, optional): A comma separated list of sort expressions. A sort expression is a  property name optionally followed by a direction indicator `asc` or  `desc`. The default is ascending order.

Example: key, quote desc
- `select` (List[str], optional): A comma separated list of select properties to display in the response.  The default is that all properties are returned.

Example: id,key
- `limit` (int, optional): Specifies the number of results to be returned. The default value  is 50.
- `offset` (int, optional): Specifies the zero-based resource offset to start the response from. The default value is 0.


### getsubscriptiondetailsbyidv1

- **Description**: Get detailed information for a single subscription by `id`. \<br\>\<br\>**NOTE:** You need to have the view permission of device management to invoke this API. \<br\>\<br\> Rate limits are enforced on this API. 20 requests per minute is supported per workspace. The API returns `429` if this threshold is breached.
- **Method**: GET /subscriptions/v1/subscriptions/{id}
- **Parameters**:

- `id` (str, required): The unique identifier of the subscription.




## Typical Use Cases

This MCP server enables AI assistants to answer natural language questions about your HPE GreenLake subscriptions resources. Here are some example queries you can try:

**Subscription Tracking:**

- "Show me all active subscriptions"
- "What's the status of subscription ABC?"
- "List subscriptions expiring within 30 days"

These are just examples - you can ask questions in your own words, and the AI assistant will use the appropriate MCP tools to retrieve the information from HPE GreenLake.

## API Coverage

This MCP server implements read-only access to the following subscriptions API endpoints:

- `GET /subscriptions/v1/subscriptions` - Get subscriptions managed in a workspace. Filters can be passed to filter  the subscriptions based on conditional expressions.\<br\>\<br\>**NOTE:** You need to have  view permission for the **Devices and subscription service** to invoke this API. \<br\>\<br\> Rate limits are enforced on this API. 60 requests per minute is supported per workspace. API will result in `429` if this threshold is breached.
- `GET /subscriptions/v1/subscriptions/{id}` - Get detailed information for a single subscription by `id`. \<br\>\<br\>**NOTE:** You need to have the view permission of device management to invoke this API. \<br\>\<br\> Rate limits are enforced on this API. 20 requests per minute is supported per workspace. The API returns `429` if this threshold is breached.


API Version: 1.0.1


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
subscriptions/
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

**Integration smoke tests** require the variables above plus any tool arguments (`MCP_TEST_SUBSCRIPTIONS_<PARAM_NAME>`):

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

**Service**: subscriptions  
**API Version**: 1.0.1  
**MCP Server Version**: 0.1.0
