# (c) Copyright 2025 Hewlett Packard Enterprise Development LP
"""Unit tests for generated Pydantic models."""

from __future__ import annotations

from typing import Any

import pytest
from pydantic import ValidationError as PydanticValidationError

from models import (
    BaseModel,
    Message,
    NBUser,
    NBUserPaginate,
    NBUserPreferences,
    StandardErrorResponse,
    UserLanguages,
    UserStatus,
    Body_invite_user_to_account_identity_v1_users_post,
)

MODEL_TEST_MATRIX = [
    {
        "model": Message,
        "name": "Message",
        "fields": [
            {
                "name": "message",
                "sanitized": "message",
                "type": r"str",
                "required": True,
            },
        ],
    },
    {
        "model": NBUser,
        "name": "NBUser",
        "fields": [
            {
                "name": "username",
                "sanitized": "username",
                "type": r"str",
                "required": True,
            },
            {
                "name": "lastLogin",
                "sanitized": "lastLogin",
                "type": r"str",
                "required": False,
            },
            {
                "name": "updatedAt",
                "sanitized": "updatedAt",
                "type": r"str",
                "required": False,
            },
            {
                "name": "userStatus",
                "sanitized": "userStatus",
                "type": r"str",
                "required": False,
            },
            {
                "name": "generation",
                "sanitized": "generation",
                "type": r"int",
                "required": False,
            },
            {
                "name": "resourceUri",
                "sanitized": "resourceUri",
                "type": r"str",
                "required": False,
            },
            {
                "name": "id",
                "sanitized": "id",
                "type": r"str",
                "required": True,
            },
            {
                "name": "createdAt",
                "sanitized": "createdAt",
                "type": r"str",
                "required": False,
            },
            {
                "name": "type",
                "sanitized": "type",
                "type": r"str",
                "required": True,
            },
        ],
    },
    {
        "model": NBUserPaginate,
        "name": "NBUserPaginate",
        "fields": [
            {
                "name": "items",
                "sanitized": "items",
                "type": r"List[Dict[str, Any]]",
                "required": True,
            },
            {
                "name": "offset",
                "sanitized": "offset",
                "type": r"int",
                "required": True,
            },
            {
                "name": "total",
                "sanitized": "total",
                "type": r"int",
                "required": True,
            },
            {
                "name": "count",
                "sanitized": "count",
                "type": r"int",
                "required": True,
            },
        ],
    },
    {
        "model": NBUserPreferences,
        "name": "NBUserPreferences",
        "fields": [
            {
                "name": "idleTimeout",
                "sanitized": "idleTimeout",
                "type": r"int",
                "required": False,
            },
            {
                "name": "language",
                "sanitized": "language",
                "type": r"str",
                "required": False,
            },
        ],
    },
    {
        "model": StandardErrorResponse,
        "name": "StandardErrorResponse",
        "fields": [
            {
                "name": "debugId",
                "sanitized": "debugId",
                "type": r"str",
                "required": True,
            },
            {
                "name": "errorCode",
                "sanitized": "errorCode",
                "type": r"str",
                "required": True,
            },
            {
                "name": "httpStatusCode",
                "sanitized": "httpStatusCode",
                "type": r"int",
                "required": True,
            },
            {
                "name": "message",
                "sanitized": "message",
                "type": r"str",
                "required": True,
            },
        ],
    },
    {
        "model": UserLanguages,
        "name": "UserLanguages",
        "fields": [],
    },
    {
        "model": UserStatus,
        "name": "UserStatus",
        "fields": [],
    },
    {
        "model": Body_invite_user_to_account_identity_v1_users_post,
        "name": "Body_invite_user_to_account_identity_v1_users_post",
        "fields": [
            {
                "name": "email",
                "sanitized": "email",
                "type": r"str",
                "required": False,
            },
            {
                "name": "sendWelcomeEmail",
                "sanitized": "sendWelcomeEmail",
                "type": r"bool",
                "required": False,
            },
        ],
    },
]


if not MODEL_TEST_MATRIX:
    pytest.skip("No models were generated; skipping model unit tests.", allow_module_level=True)


def _value_for_type(type_name: str) -> Any:
    normalized = type_name.lower()

    # Handle Literal types - extract the literal value
    if "literal[" in normalized:
        import re

        # Try to extract string literal: Literal["value"] or Literal['value']
        match = re.search(r"literal\[[\"\'](.+?)[\"\']\]", type_name, re.IGNORECASE)
        if match:
            return match.group(1)
        # Try to extract numeric literal: Literal[1] or Literal[1.5]
        match = re.search(r"literal\[(\d+\.?\d*)\]", type_name, re.IGNORECASE)
        if match:
            value = match.group(1)
            # Return int if no decimal point, float otherwise
            return int(value) if "." not in value else float(value)
        return "example"

    # Handle List[Union[Dict[...], ...]] - return list with dict
    if "list[union[dict" in normalized:
        return [{"key": "value"}]
    # Handle List[Dict[...]] specifically
    if "list[dict" in normalized or "list[mapping" in normalized:
        return [{"key": "value"}]
    if "list" in normalized or "sequence" in normalized:
        return ["example"]
    if "dict" in normalized or "mapping" in normalized:
        return {"key": "value"}
    if "int" in normalized or "integer" in normalized:
        return 1
    if "float" in normalized or "number" in normalized:
        return 1.0
    if "bool" in normalized:
        return True
    if "datetime" in normalized or "date" in normalized:
        return "2024-01-01T00:00:00Z"

    return "example"


@pytest.mark.parametrize("config", MODEL_TEST_MATRIX, ids=lambda cfg: cfg["name"])
def test_model_accepts_valid_payload(config):
    payload = {field["name"]: _value_for_type(field["type"]) for field in config["fields"]}

    model = config["model"].model_validate(payload)

    assert isinstance(model, BaseModel)
    for field in config["fields"]:
        assert getattr(model, field["sanitized"]) == payload[field["name"]]


REQUIRED_FIELD_CASES: list[tuple[dict[str, Any], list[dict[str, Any]]]] = [
    (config, [field for field in config["fields"] if field["required"]])  # type: ignore[attr-defined]
    for config in MODEL_TEST_MATRIX
]

REQUIRED_FIELD_CASE_IDS: list[str] = [case[0]["name"] for case in REQUIRED_FIELD_CASES]


@pytest.mark.parametrize("config,required_fields", REQUIRED_FIELD_CASES, ids=REQUIRED_FIELD_CASE_IDS)
def test_model_requires_mandatory_fields(config, required_fields):
    if not required_fields:
        pytest.skip("Model has no required fields.")

    payload = {field["name"]: _value_for_type(field["type"]) for field in config["fields"] if not field["required"]}

    with pytest.raises(PydanticValidationError):
        config["model"].model_validate(payload)
