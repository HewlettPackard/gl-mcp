# Changelog - Subscriptions MCP Server

All notable changes to the HPE GreenLake Subscriptions MCP Server will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.1] - 2026-01-07

### Added

- **Initial release** of HPE GreenLake Subscriptions MCP Server
- **Authentication**: OAuth2 integration with subscription-aware permissions
- **Core Tools**:
  - `getsubscriptionsv1` - Get subscriptions with conditional filtering (supports filter, filter-tags, sort, select, limit, offset)
  - `getsubscriptiondetailsbyidv1` - Get detailed subscription information by ID
- **Dynamic Tools** (when `MCP_TOOL_MODE=dynamic`):
  - `list_endpoints` - Discover available API endpoints with filtering
  - `get_endpoint_schema` - Get detailed schema information for endpoints
  - `invoke_dynamic_tool` - Execute API calls with runtime parameter validation
- **Subscription Management**:
  - Read-only access to subscription information
  - Retrieve subscription details by ID
- **Search & Filtering**:
  - Filter by availableQuantity, contract, createdAt, endTime, id, isEval, key, productType, quantity, sku, skuDescription, startTime, subscriptionStatus, subscriptionType, tags, tier, type, updatedAt
  - Tag-based filtering with conditional expressions
  - Sorting, field selection, pagination with limit and offset
- **Output Formats**: JSON subscription data

### Security

- **OAuth2 Authentication** with automatic token management

### Technical Details

- **Python 3.10+** support
- **Model Context Protocol** v1.0 implementation
- **Rate Limiting** awareness (60/20 requests per minute)
