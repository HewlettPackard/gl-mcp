# (c) Copyright 2025 Hewlett Packard Enterprise Development LP
"""HTTP helper utilities for users test suite."""

from __future__ import annotations

import json
from typing import Any
from unittest.mock import MagicMock


def make_json_response(payload: Any, status_code: int = 200) -> MagicMock:
    """Create a MagicMock representing an HTTPX response."""
    response = MagicMock()
    response.status_code = status_code
    response.json.return_value = payload
    response.text = json.dumps(payload)
    return response
