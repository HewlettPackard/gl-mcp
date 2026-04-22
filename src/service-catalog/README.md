# service-catalog MCP Server

HPE GreenLake service-catalog MCP Server provides read-only access to the HPE GreenLake service-catalog APIs through the Model Context Protocol.

## Overview

This MCP server enables AI assistants and development tools to interact with HPE GreenLake service-catalog programmatically. It follows the standardized MCP server architecture with shared authentication components and HTTP client adapters.

### Key Features

- **Read-only API access** to service-catalog endpoints
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

<!-- @begin:pypi -->
**From PyPI (recommended):**

```bash
pip install greenlake-service-catalog-mcp
```

After installation, run the server with:

```bash
python -m greenlake_service_catalog_mcp
```

<!-- @end -->

<!-- @begin:source -->
**From source (development):**

1. Navigate to the service directory:

   ```bash
   cd src/service-catalog
   ```

2. Install dependencies:

   ```bash
   uv sync
   ```

3. Configure environment variables (see Configuration section)

4. Configure in your MCP client (see MCP Client Configuration section below)

<!-- @end -->

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
- Logs written to: `~/.hpe/mcp-logs/service-catalog/service-catalog-mcp.log`
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
# Check logs at: ~/.hpe/mcp-logs/service-catalog/
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
    "service-catalog": {
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

<!-- @begin:pypi -->
**Using PyPI package:**

```json
{
  "servers": {
    "service-catalog": {
      "type": "stdio",
      "command": "python",
      "args": ["-m", "greenlake_service_catalog_mcp"],
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

<!-- @end -->

<!-- @begin:source -->
**Using uv (from source):**

```json
{
  "servers": {
    "service-catalog": {
      "type": "stdio",
      "command": "uv",
      "args": ["run", "python", "__main__.py"],
      "cwd": "/path/to/gl-mcp/src/service-catalog",
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

<!-- @end -->

### Claude Desktop

Add to your `claude_desktop_config.json`:

<!-- @begin:pypi -->
**Using PyPI package:**

```json
{
  "mcpServers": {
    "service-catalog": {
      "command": "python",
      "args": ["-m", "greenlake_service_catalog_mcp"],
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

<!-- @end -->

<!-- @begin:source -->
**Using uv (from source):**

```json
{
  "mcpServers": {
    "service-catalog": {
      "command": "uv",
      "args": ["run", "python", "__main__.py"],
      "cwd": "/path/to/gl-mcp/src/service-catalog",
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

<!-- @end -->

## Available Tools

This server provides the following MCP tools:

### getserviceofferregions

- **Description**: Retrieve a list of service offer regions by applying filters.
Each service offer region represents a service offer provisioned in a specific region.
\<br\>\<br\>**Pagination:** This API supports cursor-based pagination. Provide the cursor in the `next` query parameter to retrieve the next page.

- **Method**: GET /service-catalog/v1beta1/service-offer-regions
- **Parameters**:

  - `next` (str, optional):  
    Specifies the pagination cursor for the next page of service offer regions.

Example: 64136af7-cd64-4b4e-88a8-150ab51a920d

- `limit` (int, optional):  
    Specifies the number of results to be returned.
- `filter` (str, optional):  
    The `filter` query parameter is used to filter the set of resources returned in a `GET` request. The returned set of resources must match the criteria in the filter query parameter.\<br\>\<br\> The value of the `filter` query parameter is a subset of [OData 4.0](https://www.odata.org/documentation/) filter expressions consisting of simple comparison operations joined by logical operators.\<br\>\<br\>**Supported fields**: `serviceOfferId`, `status`, and
    `region`.\<br\>**Supported operand**: `eq`\<br\>**Supported operations**: `and` Examples: - serviceOfferId eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050' and status eq 'ONBOARDED' and region eq 'us-east' Return service offer regions with a given service offer ID and status and region - region eq 'us-east' Return service offer regions with a given region - status eq 'ONBOARDED' Return service offer regions with a given status - serviceOfferId eq
    '767c0c92-5ecc-4952-85d6-06d2bcaaf050' Return service offer regions with a given service offer ID - serviceOfferId eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050' and region eq 'us-east' Return service offer regions with a given service offer ID and region - serviceOfferId eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050' and status eq 'ONBOARDED' Return service offer regions with a given service offer ID and status **Filter Syntax**: Use OData-style filters with the field names shown in
    the examples above. String values must be enclosed in single quotes.

### getserviceprovisions

- **Description**: Retrieve a list of service provisions by applying filters.
A service offer provides a distinct set of functionalities that can be independently identified and assigned access. Service offers are typically associated with roles and permissions, commerce, metering, quote-to-cash, and trial evaluations.
A service provision occurs when a service offer is provisioned (added) to a workspace.
\<br\>\<br\>**Pagination**: This endpoint supports cursor-based pagination using the `next` query parameter. Provide the cursor in the `next` query parameter to retrieve the next page.

- **Method**: GET /service-catalog/v1beta1/service-provisions
- **Parameters**:

  - `Hpe-workspace-id` (str, optional):  
    The workspace ID. Required if the "view all" parameter is false.
  - `next` (str, optional):  
    Specify the start ID for the next page of service offers.
  - `limit` (int, optional):  
    Specify the number of results to be returned.
  - `filter` (str, optional):  
    Limit the entities operated on by this endpoint by returning only the subset of entities that match the filter. The filter grammar is a subset of OData 4.0. \<br\> **Supported Fields:** `id`, `ServiceOfferId`, `workspaceId`, `serviceManagerProvisionId`, `serviceManagerId`, `serviceManagerInstanceId`, `status`, `organizationId`, `slug`. \<br\> **Supported operand:** `eq` \<br\> **Supported operations:** `and` Examples: - serviceManagerId eq
    '767c0c92-5ecc-4952-85d6-06d2bcaaf050' and serviceManagerInstanceId eq '62d242c7-7d53-448d-b7d0-baf0c591f024' Return service provision for a given application ID and application instance ID. - status eq 'PROVISION_INITIATED' Return service provisions with a given status. - organizationId eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050' Return service provisions with a given organization ID. - slug eq 'AC' Return service provisions with a given slug. - id eq
    '767c0c92-5ecc-4952-85d6-06d2bcaaf050' Return the service provision with a given ID. - workspaceId eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050' Return service provisions for a given workspace ID. - serviceManagerProvisionId eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050' Return service provisions for a given Application Customer ID. - ServiceOfferId eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050' and region eq 'us-west' Return service provisions for a given service offer ID and region.
    **Filter Syntax**: Use OData-style filters with the field names shown in the examples above. String values must be enclosed in single quotes.
  - `unredacted` (bool, optional):  
    If true, returns the complete entry including sensitive fields.

Example: true

- `all` (bool, optional):  
    If true, returns unredacted entries for all workspaces, including all provisioned service offers and their sensitive fields.

Example: true

### getserviceoffers

- **Description**: Retrieve a list of service offers by applying filters.
A service offer provides a distinct set of functionality that can be independently identified and assigned access.
\<br\>\<br\>**Pagination:** This API supports cursor-based pagination. Provide the cursor in the `next` query parameter to retrieve the next page.

- **Method**: GET /service-catalog/v1beta1/service-offers
- **Parameters**:

  - `next` (str, optional):  
    Specifies the pagination cursor for the next page of service offers.

Example: 64136af7-cd64-4b4e-88a8-150ab51a920d

- `limit` (int, optional):  
    Specifies the number of results to be returned.
- `filter` (str, optional):  
    The `filter` query parameter is used to filter the set of resources returned in a `GET` request. The returned set of resources must match the criteria in the filter query parameter.\<br\>\<br\> The value of the `filter` query parameter is a subset of [OData 4.0](https://www.odata.org/documentation/) filter expressions consisting of simple comparison operations joined by logical operators.\<br\>\<br\>**Supported fields**: `category`, `serviceManagerId`, `status`, `isDefault`,
    `slug`, and `staticLaunchUrl`.\<br\>**Supported operand**: `eq`\<br\>**Supported operations**: `and` Examples: - slug eq 'GLP' Return service offers with a given slug - staticLaunchUrl eq '/Organization' Return service offers for a given static launch URL - status eq 'ONBOARDED' Return service offers with a given status - category eq 'COMPUTE' Return service offers for a given category - isDefault eq true Return service offers that are service managers - serviceManagerId eq
    '767c0c92-5ecc-4952-85d6-06d2bcaaf050' Return service offers for given service manager ID **Filter Syntax**: Use OData-style filters with the field names shown in the examples above. String values must be enclosed in single quotes.

### getserviceofferregion

- **Description**: Retrieve detailed information about a specific service offer region by providing its unique identifier in the request path.
To obtain valid service offer region IDs, use the `Get service offer regions` endpoint to list available regions.

- **Method**: GET /service-catalog/v1beta1/service-offer-regions/{id}
- **Parameters**:

  - `id` (str, required):  
    The unique service offer region ID.

Example: 3fa85f64-5717-4562-b3fc-2c963f66afa6

### service_managers_for_a_region_v1

- **Description**: Retrieve a list of service managers deployed to a particular region.
- **Method**: GET /service-catalog/v1/per-region-service-managers/{id}
- **Parameters**:

  - `id` (str, required):  
    HPE GreenLake platform defined region code.

Examples:

- us-west
- us-east

### get_service_manager_provisions_v1

- **Description**: Retrieve a list of all service manager provision entries.
- **Method**: GET /service-catalog/v1/service-manager-provisions
- **Parameters**:

  - `offset` (int, optional):  
    Zero-based resource offset to start the response from.

Example: 0

- `limit` (int, optional):  
    The maximum number of records to return.

Example: 10

- `filter` (str, optional):  
    Examples: - status eq 'PROVISIONED' Returns service managers that are provisioned. - status eq 'UNPROVISIONED' Returns service managers that are not provisioned. - region eq 'us-west' Returns service managers in a specified region. - serviceManagerId eq '767c0c92-5ecc-4952-85d6-06d2bcaaf050' Returns service managers with a specific service manager ID. **Filter Syntax**: Use OData-style filters with the field names shown in the examples above. String values must be enclosed in
    single quotes.

### get_service_managers_v1

- **Description**: Get a list of available service managers.
- **Method**: GET /service-catalog/v1/service-managers
- **Parameters**:

  - `offset` (int, optional):  
    Specify pagination offset

Example: 0

- `limit` (int, optional):  
    The maximum number of records to return.

Example: 10

### get_service_manager_provision_v1

- **Description**: Retrieve details for a specific service manager provision entry using the ID for the entry.
- **Method**: GET /service-catalog/v1/service-manager-provisions/{id}
- **Parameters**:

  - `id` (str, required):  
    Service manager provision ID

### per_region_service_managers_v1

- **Description**: Retrieve a list of available service managers categorized by region.
- **Method**: GET /service-catalog/v1/per-region-service-managers
- **Parameters**:

  - `offset` (int, optional):  
    Zero-based resource offset to start the response from.

Example: 0

- `limit` (int, optional):  
    The maximum number of records to return.

Example: 10

- `filter` (str, optional):  
    Limit the resources operated on by an endpoint and return only the subset of resources that match the filter using an [OData V4](https://www.odata.org/documentation/) formatted filter string. Service manager by region can be filtered by `mspsupported` See examples of filtering options. Examples: - mspSupported eq false Return service managers when msp supported equals false - mspSupported eq true Return service managers when msp supported equals true **Filter Syntax**: Use
    OData-style filters with the field names shown in the examples above. String values must be enclosed in single quotes.

### getserviceprovision

- **Description**: Fetch service provision details for an ID.
- **Method**: GET /service-catalog/v1beta1/service-provisions/{id}
- **Parameters**:

  - `id` (str, required):  
    The unique identifier of a service provision. The ID is returned by the `Get service provisions` endpoint.
  - `unredacted` (bool, optional):  
    If set to true, get the entire entry along with sensitive fields.

Example: true

### getserviceoffer

- **Description**: Retrieve detailed information about a specific service offer by supplying its unique identifier in the request path.
To obtain valid service offer IDs, use the `Get service offers` endpoint to list available offers.

- **Method**: GET /service-catalog/v1beta1/service-offers/{id}
- **Parameters**:

  - `id` (str, required):  
    The unique identifier of the service offer.

Example: 3fa85f64-5717-4562-b3fc-2c963f66afa6

### get_service_manager_v1

- **Description**: Retrieve details for a specific service manager by passing the service manager ID.
- **Method**: GET /service-catalog/v1/service-managers/{id}
- **Parameters**:

  - `id` (str, required):  
    Service manager ID

## Typical Use Cases

This MCP server enables AI assistants to answer natural language questions about your HPE GreenLake service-catalog resources. Here are some example queries you can try:

**service-catalog Queries:**

- "List all service-catalog resources"
- "Show me details for specific service-catalog items"
- "Find service-catalog by specific criteria"
- "Get status of service-catalog resources"
- "Show me recent service-catalog changes"

These are just examples - you can ask questions in your own words, and the AI assistant will use the appropriate MCP tools to retrieve the information from HPE GreenLake.

## API Coverage

This MCP server implements read-only access to the following service-catalog API endpoints:

- `GET /service-catalog/v1beta1/service-offer-regions` - Retrieve a list of service offer regions by applying filters.
Each service offer region represents a service offer provisioned in a specific region.
\<br\>\<br\>**Pagination:** This API supports cursor-based pagination. Provide the cursor in the `next` query parameter to retrieve the next page.

- `GET /service-catalog/v1beta1/service-provisions` - Retrieve a list of service provisions by applying filters.
A service offer provides a distinct set of functionalities that can be independently identified and assigned access. Service offers are typically associated with roles and permissions, commerce, metering, quote-to-cash, and trial evaluations.
A service provision occurs when a service offer is provisioned (added) to a workspace.
\<br\>\<br\>**Pagination**: This endpoint supports cursor-based pagination using the `next` query parameter. Provide the cursor in the `next` query parameter to retrieve the next page.

- `GET /service-catalog/v1beta1/service-offers` - Retrieve a list of service offers by applying filters.
A service offer provides a distinct set of functionality that can be independently identified and assigned access.
\<br\>\<br\>**Pagination:** This API supports cursor-based pagination. Provide the cursor in the `next` query parameter to retrieve the next page.

- `GET /service-catalog/v1beta1/service-offer-regions/{id}` - Retrieve detailed information about a specific service offer region by providing its unique identifier in the request path.
To obtain valid service offer region IDs, use the `Get service offer regions` endpoint to list available regions.

- `GET /service-catalog/v1/per-region-service-managers/{id}` - Retrieve a list of service managers deployed to a particular region.
- `GET /service-catalog/v1/service-manager-provisions` - Retrieve a list of all service manager provision entries.
- `GET /service-catalog/v1/service-managers` - Get a list of available service managers.
- `GET /service-catalog/v1/service-manager-provisions/{id}` - Retrieve details for a specific service manager provision entry using the ID for the entry.
- `GET /service-catalog/v1/per-region-service-managers` - Retrieve a list of available service managers categorized by region.
- `GET /service-catalog/v1beta1/service-provisions/{id}` - Fetch service provision details for an ID.
- `GET /service-catalog/v1beta1/service-offers/{id}` - Retrieve detailed information about a specific service offer by supplying its unique identifier in the request path.
To obtain valid service offer IDs, use the `Get service offers` endpoint to list available offers.

- `GET /service-catalog/v1/service-managers/{id}` - Retrieve details for a specific service manager by passing the service manager ID.

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
service-catalog/
├── pyproject.toml          # Dependencies and configuration
├── README.md               # This file
├── Makefile                # Development commands
├── greenlake_service_catalog_mcp/           # Python package
│   ├── __init__.py
│   ├── __main__.py         # Entry point
│   ├── _version.py         # Version constants
│   ├── auth/               # Authentication components
│   │   ├── __init__.py
│   │   ├── oauth2_provider.py  # OAuth2 client credentials
│   │   └── token_manager.py    # Token lifecycle management
│   ├── config/             # Configuration management
│   │   ├── __init__.py
│   │   ├── logging.py      # Logging configuration
│   │   └── settings.py     # Application settings
│   ├── models/             # Data models
│   │   ├── __init__.py
│   │   └── base.py         # Base model classes
│   ├── server/             # MCP server implementation
│   │   ├── __init__.py
│   │   ├── app.py          # Application factory
│   │   ├── fastmcp_instance.py # FastMCP singleton
│   │   └── mcp_server.py   # MCP server core
│   ├── tools/              # MCP tools
│   │   ├── __init__.py
│   │   ├── base.py         # Base tool class
│   │   ├── registry.py     # Tool registration
│   │   └── implementations/
│   │       └── *.py        # Tool implementations
│   └── utils/              # Utility modules
│       ├── __init__.py
│       └── http_client.py  # HTTP client utilities
└── tests/                  # Test suite
    ├── conftest.py         # Shared fixtures
    ├── shared/
    │   └── http.py         # Testing helpers
    ├── unit/
    │   └── test_*.py       # Unit tests
    └── integration/
        └── test_live_tools.py
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

**Integration smoke tests** require the variables above plus any tool arguments (`MCP_TEST_SERVICE_CATALOG_<PARAM_NAME>`):

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
<!-- @begin:source -->
- Check uv dependencies are installed
<!-- @end -->
<!-- @begin:pypi -->
- Check that the package is installed: `pip show greenlake-service-catalog-mcp`
<!-- @end -->
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
