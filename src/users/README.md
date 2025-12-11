# users MCP Server

HPE GreenLake users MCP Server provides read-only access to the HPE GreenLake users APIs through the Model Context Protocol.

## Overview

This MCP server enables AI assistants and development tools to interact with HPE GreenLake users programmatically. It follows the standardized MCP server architecture with shared authentication components and HTTP client adapters.

### Key Features

- **Read-only API access** to users endpoints
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
   cd src/users
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
- Logs written to: `~/.hpe/mcp-logs/users/users-mcp.log`
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
# Check logs at: ~/.hpe/mcp-logs/users/
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
    "users": {
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
    "users": {
      "type": "stdio",
      "command": "uv",
      "args": ["run", "python", "__main__.py"],
      "cwd": "/path/to/mcp-generator/mcps/users",
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
    "users": {
      "type": "stdio", 
      "command": "uv",
      "args": ["run", "python", "__main__.py"],
      "cwd": "/path/to/mcp-generator/mcps/users",
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

### get_user_detailed_identity_v1_users_id_get

- **Description**: Retrieve a single user based on a given user ID.
- **Method**: GET /identity/v1/users/{id}
- **Parameters**:

- `id` (str, required): The unique identifier of the user.

Example: 7600415a-8876-5722-9f3c-b0fd11112283


### get_users_identity_v1_users_get

- **Description**: Retrieve list of users with filtering, and pagination options. All users are returned when no filters are provided. 
**Note**: User view all permission is required to invoke this API. 
Rate limit: 300 requests per minute per workspace, resulting in a `429` error if exceeded.

- **Method**: GET /identity/v1/users
- **Parameters**:

- `filter` (str, optional): Filter data using a subset of OData 4.0 and return only the subset of resources that match the filter.

Supported classes and examples include:
- **Types**: timestamp, string
- **Comparison**: eq, ne, gt, ge, lt
- **Logical Expressions**: and, or, not

The Get users API can be filtered by:
- id
- username
- userStatus
- createdAt
- updatedAt
- lastLogin

userStatus can be one of the following:
- UNVERIFIED
- VERIFIED
- BLOCKED
- DELETE_IN_PROGRESS
- DELETED
- SUSPENDED

**Note**: The userStatus filter is case-sensitive.

Examples:
  - lastLogin lt '2020-09-21T14:19:09.769747'
    Returns users that logged in before 2020-09-21T14:19:09.769747
  - updatedAt gt '2020-09-21T14:19:09.769747'
    Returns users updated after 2020-09-21T14:19:09.769747
  - userStatus ne 'UNVERIFIED'
    Returns users that are not unverified.
  - username eq 'user@example.com'
    Returns the user with a specific username.
  - createdAt gt '2020-09-21T14:19:09.769747'
    Returns users created after 2020-09-21T14:19:09.769747
  - username eq 'user@example.com'
    Returns the user with a specific email.
  - id eq '7600415a-8876-5722-9f3c-b0fd11112283'
    Returns the user with a specific ID.

**Important**: All filter values must be enclosed in single quotes, including numbers and booleans. Examples: `quantity eq '10'`, `hasDetails eq 'true'`, `name eq 'example'`.

Filterable properties: createdAt, generation, id, lastLogin, resourceUri, type, updatedAt, userStatus, username
- `offset` (int, optional): Specify pagination offset. An offset argument defines how many pages to skip before returning results.
- `limit` (int, optional): Specify the maximum number of entries per page. NOTE: The maximum value accepted is 600.




## Typical Use Cases

This MCP server enables AI assistants to answer natural language questions about your HPE GreenLake users resources. Here are some example queries you can try:

**User Management:**

- "List all users in my workspace"
- "Find users with email domain @hpe.com"
- "Who has access to my workspace?"
- "Show me recently added users"

These are just examples - you can ask questions in your own words, and the AI assistant will use the appropriate MCP tools to retrieve the information from HPE GreenLake.

## API Coverage

This MCP server implements read-only access to the following users API endpoints:

- `GET /identity/v1/users/{id}` - Retrieve a single user based on a given user ID.
- `GET /identity/v1/users` - Retrieve list of users with filtering, and pagination options. All users are returned when no filters are provided. 
**Note**: User view all permission is required to invoke this API. 
Rate limit: 300 requests per minute per workspace, resulting in a `429` error if exceeded.



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
users/
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

**Integration smoke tests** require the variables above plus any tool arguments (`MCP_TEST_USERS_<PARAM_NAME>`):

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

**Service**: users  
**API Version**: 1.0.1  
**MCP Server Version**: 0.1.0
