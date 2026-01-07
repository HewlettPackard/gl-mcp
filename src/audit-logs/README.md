# audit-logs MCP Server

HPE GreenLake audit-logs MCP Server provides read-only access to the HPE GreenLake audit-logs APIs through the Model Context Protocol.

## Overview

This MCP server enables AI assistants and development tools to interact with HPE GreenLake audit-logs programmatically. It follows the standardized MCP server architecture with shared authentication components and HTTP client adapters.

### Key Features

- **Read-only API access** to audit-logs endpoints
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
   cd src/audit-logs
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
- Logs written to: `~/.hpe/mcp-logs/audit-logs/audit-logs-mcp.log`
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
# Check logs at: ~/.hpe/mcp-logs/audit-logs/
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
    "audit-logs": {
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
    "audit-logs": {
      "type": "stdio",
      "command": "uv",
      "args": ["run", "python", "__main__.py"],
      "cwd": "/path/to/mcp-generator/mcps/audit-logs",
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
    "audit-logs": {
      "type": "stdio", 
      "command": "uv",
      "args": ["run", "python", "__main__.py"],
      "cwd": "/path/to/mcp-generator/mcps/audit-logs",
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

### getauditlogdetails

- **Description**: Get additional detail of an audit log.
- **Method**: GET /audit-log/v1/logs/{id}/detail
- **Parameters**:

- `id` (str, required): Provide the ID of the audit log record that has the `hasDetails` value set to `true` to fetch the additional details.


### getauditlogs

- **Description**: The audit logs can be filtered using a variety of parameters. Queries should be separated by `and` and can utilize `eq`, `contains`, and `in` operators to construct the final query. Each query should follow the format:
* key eq 'value' for equality operation.
* contains(key, 'value') for contains operation.
* key in ('value1', 'value2') for in operation.

| Filter parameter         | Supported Operators | Type                    | Example                                                                                         |
|--------------------------|---------------------|-------------------------|-------------------------------------------------------------------------------------------------|
| createdAt                | lt, ge              | RFC timestamp in string | createdAt ge '2024-02-16T07:54:55.0Z'                                                           |
| category                 | eq, in              | string                  | category eq 'User Management' category in ('Device Management', 'User Activity')                |
| description              | eq, contains        | string                  | contains(description, 'Logged in') description eq 'User test@test.com logged in via ping mode.' |
| additionalInfo/ipAddress | eq, contains        | IP string               | additionalInfo/ipAddress eq '192.168.12.12' contains(additionalInfo/ipAddress, '192.168')       |
| user/username            | eq, contains        | email in string         | user/username eq 'test@test.com' contains(user/username, '@gmail.com')                          |
| workspace/workspaceName  | eq, contains        | string                  | workspace/workspaceName eq 'Example workspace' contains(workspace/workspaceName, 'Example')     |
| application/id           | eq                  | UUID in string          | application/id eq '12312-123123-123123-123121'                                                  |
| region                   | eq                  | region code in string   | region eq 'us-west'                                                                             |
| hasDetails               | eq                  | boolean                 | hasDetails eq 'true'                                                                              |

- **Method**: GET /audit-log/v1/logs
- **Parameters**:

- `filter` (str, optional): Example: category eq 'User Management' and contains(description, 'logged out')

**Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`.

Filterable properties: additionalInfo, application, category, createdAt, description, generation, hasDetails, id, region, type, updatedAt, user, workspace
- `select` (str, optional): Use the `select` query parameter to restrict the number of properties included in the audit log response.
The supported select parameters:
 * additionalInfo
 * createdAt
 * category
 * hasDetails
 * workspace/workspaceName
 * description
 * user/username


Example: createdAt, user/username, category
- `all` (str, optional): Provide a free-text search to perform a comprehensive search across all properties for audit logs.

Example: logged in user
- `limit` (int, optional): How many items to return at one time (max 2000)
- `offset` (int, optional): Specifies the zero-based resource offset to start the response from.




## Typical Use Cases

This MCP server enables AI assistants to answer natural language questions about your HPE GreenLake audit-logs resources. Here are some example queries you can try:

**Audit and Compliance:**

- "Show me recent login events"
- "List all administrative actions from the last 7 days"
- "Find failed authentication attempts"
- "Show me who modified resource X"
- "Track changes to workspace configuration"

These are just examples - you can ask questions in your own words, and the AI assistant will use the appropriate MCP tools to retrieve the information from HPE GreenLake.

## API Coverage

This MCP server implements read-only access to the following audit-logs API endpoints:

- `GET /audit-log/v1/logs/{id}/detail` - Get additional detail of an audit log.
- `GET /audit-log/v1/logs` - The audit logs can be filtered using a variety of parameters. Queries should be separated by `and` and can utilize `eq`, `contains`, and `in` operators to construct the final query. Each query should follow the format:
* key eq 'value' for equality operation.
* contains(key, 'value') for contains operation.
* key in ('value1', 'value2') for in operation.

| Filter parameter         | Supported Operators | Type                    | Example                                                                                         |
|--------------------------|---------------------|-------------------------|-------------------------------------------------------------------------------------------------|
| createdAt                | lt, ge              | RFC timestamp in string | createdAt ge '2024-02-16T07:54:55.0Z'                                                           |
| category                 | eq, in              | string                  | category eq 'User Management' category in ('Device Management', 'User Activity')                |
| description              | eq, contains        | string                  | contains(description, 'Logged in') description eq 'User test@test.com logged in via ping mode.' |
| additionalInfo/ipAddress | eq, contains        | IP string               | additionalInfo/ipAddress eq '192.168.12.12' contains(additionalInfo/ipAddress, '192.168')       |
| user/username            | eq, contains        | email in string         | user/username eq 'test@test.com' contains(user/username, '@gmail.com')                          |
| workspace/workspaceName  | eq, contains        | string                  | workspace/workspaceName eq 'Example workspace' contains(workspace/workspaceName, 'Example')     |
| application/id           | eq                  | UUID in string          | application/id eq '12312-123123-123123-123121'                                                  |
| region                   | eq                  | region code in string   | region eq 'us-west'                                                                             |
| hasDetails               | eq                  | boolean                 | hasDetails eq 'true'                                                                              |



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
audit-logs/
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

**Integration smoke tests** require the variables above plus any tool arguments (`MCP_TEST_AUDIT_LOGS_<PARAM_NAME>`):

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
