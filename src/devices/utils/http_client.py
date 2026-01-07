# (c) Copyright 2025 Hewlett Packard Enterprise Development LP
"""
HTTP client for devices MCP server.

This module provides HTTP client functionality with authentication integration.
"""

from loguru import logger
from typing import Any, Dict, Optional

import httpx
from config.settings import settings

from auth.token_manager import TokenManager
from _version import USER_AGENT


class DevicesHttpClient:
    """HTTP client for devices API with authentication."""

    def __init__(self):
        """Initialize the HTTP client with lazy token authentication."""
        self.settings = settings
        self.base_url = settings.greenlake_api_base_url
        self.logger = logger  # Use global loguru logger
        self.token_manager = TokenManager(settings=self.settings)

        # HTTP client configuration
        self.client = httpx.AsyncClient(
            timeout=httpx.Timeout(self.settings.http_timeout),
            limits=httpx.Limits(max_connections=10, max_keepalive_connections=5),
        )

    async def get(
        self,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        additional_headers: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        """
        Make GET request to the API.

        Args:
            endpoint: API endpoint path
            params: Query parameters
            additional_headers: Additional headers to include in the request

        Returns:
            Response data as dictionary
        """
        url = f"{self.base_url}{endpoint}"
        headers = await self._get_auth_headers()

        # Merge additional headers if provided
        if additional_headers:
            headers.update(additional_headers)

        self.logger.debug(f"GET request to: {url}")

        try:
            response = await self.client.get(url, headers=headers, params=params)
            response.raise_for_status()
            return response.json()  # type: ignore[no-any-return]

        except httpx.HTTPStatusError as e:
            self.logger.error(f"HTTP error {e.response.status_code}: {e.response.text}")
            raise
        except Exception as e:
            self.logger.error(f"Request failed: {str(e)}")
            raise

    async def post(
        self, endpoint: str, data: Optional[Dict[str, Any]] = None, additional_headers: Optional[Dict[str, str]] = None
    ) -> Dict[str, Any]:
        """
        Make POST request to the API.

        Args:
            endpoint: API endpoint path
            data: Request body data
            additional_headers: Additional headers to include in the request

        Returns:
            Response data as dictionary
        """
        url = f"{self.base_url}{endpoint}"
        headers = await self._get_auth_headers()

        # Merge additional headers if provided
        if additional_headers:
            headers.update(additional_headers)

        self.logger.debug(f"POST request to: {url}")

        try:
            response = await self.client.post(url, headers=headers, json=data)
            response.raise_for_status()
            return response.json()  # type: ignore[no-any-return]

        except httpx.HTTPStatusError as e:
            self.logger.error(f"HTTP error {e.response.status_code}: {e.response.text}")
            raise
        except Exception as e:
            self.logger.error(f"Request failed: {str(e)}")
            raise

    async def put(
        self, endpoint: str, data: Optional[Dict[str, Any]] = None, additional_headers: Optional[Dict[str, str]] = None
    ) -> Dict[str, Any]:
        """
        Make PUT request to the API.

        Args:
            endpoint: API endpoint path
            data: Request body data
            additional_headers: Additional headers to include in the request

        Returns:
            Response data as dictionary
        """
        url = f"{self.base_url}{endpoint}"
        headers = await self._get_auth_headers()

        # Merge additional headers if provided
        if additional_headers:
            headers.update(additional_headers)

        self.logger.debug(f"PUT request to: {url}")

        try:
            response = await self.client.put(url, headers=headers, json=data)
            response.raise_for_status()
            return response.json()  # type: ignore[no-any-return]

        except httpx.HTTPStatusError as e:
            self.logger.error(f"HTTP error {e.response.status_code}: {e.response.text}")
            raise
        except Exception as e:
            self.logger.error(f"Request failed: {str(e)}")
            raise

    async def delete(self, endpoint: str, additional_headers: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        """
        Make DELETE request to the API.

        Args:
            endpoint: API endpoint path
            additional_headers: Additional headers to include in the request

        Returns:
            Response data as dictionary (may be empty for 204 responses)
        """
        url = f"{self.base_url}{endpoint}"
        headers = await self._get_auth_headers()

        # Merge additional headers if provided
        if additional_headers:
            headers.update(additional_headers)

        self.logger.debug(f"DELETE request to: {url}")

        try:
            response = await self.client.delete(url, headers=headers)
            response.raise_for_status()

            # Handle empty responses (like 204 No Content)
            if response.status_code == 204:
                return {}

            return response.json()  # type: ignore[no-any-return]

        except httpx.HTTPStatusError as e:
            self.logger.error(f"HTTP error {e.response.status_code}: {e.response.text}")
            raise
        except Exception as e:
            self.logger.error(f"Request failed: {str(e)}")
            raise

    async def _get_auth_headers(self) -> Dict[str, str]:
        """Get authentication headers with automatic token refresh.

        Returns:
            Dictionary with Authorization, Accept, and User-Agent headers
        """
        headers: Dict[str, str] = self.token_manager.get_auth_headers()
        headers["Accept"] = "application/json"
        headers["User-Agent"] = USER_AGENT
        return headers

    async def close(self):
        """Close the HTTP client."""
        await self.client.aclose()

    async def __aenter__(self):
        """Async context manager entry."""
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        await self.close()


# Global HTTP client instance - CRITICAL: Use lazy initialization
_http_client = None


def get_http_client() -> "DevicesHttpClient":
    """Get the global HTTP client instance (lazy initialization)."""
    global _http_client
    if _http_client is None:
        _http_client = DevicesHttpClient()
    return _http_client
