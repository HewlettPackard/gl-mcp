# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""Unit tests for generated Pydantic models."""

from __future__ import annotations

from typing import Any

import pytest
from pydantic import ValidationError as PydanticValidationError

from models import (
    BaseModel,
    ResponseApplication,
    ResponseLocation,
    HpeGreenLakeBadRequestError,
    ResponseSubscription,
    HpeGreenLakeServerError,
    RequestCompute,
    RequestNetwork,
    RequestSubscription,
    PatchDevicesRequest,
    ErrorIssue,
    AsyncOperationResource,
    AsyncResponse,
    BadRequestErrorDetail,
    DevicesGetResponse,
    DevicesPostRequest,
    DevicesPostRequestV2Beta1,
    HpeGreenLakeGeneralError,
    ResponseSupportLevel,
    PatchDevicesRequestV2,
    ResponseDedicatedPlatform,
    GeneralErrorDetail,
    RequestApplication,
    ResponseWarranty,
    ServerErrorDetail,
    RequestStorage,
    DeviceDetail,
)

MODEL_TEST_MATRIX = [
    {
        "model": ResponseApplication,
        "name": "ResponseApplication",
        "fields": [
            {
                "name": "id",
                "sanitized": "id",
                "type": r"string",
                "required": True,
            },
            {
                "name": "resourceUri",
                "sanitized": "resourceUri",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": ResponseLocation,
        "name": "ResponseLocation",
        "fields": [
            {
                "name": "id",
                "sanitized": "id",
                "type": r"string",
                "required": True,
            },
            {
                "name": "resourceUri",
                "sanitized": "resourceUri",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": HpeGreenLakeBadRequestError,
        "name": "HpeGreenLakeBadRequestError",
        "fields": [
            {
                "name": "errorCode",
                "sanitized": "errorCode",
                "type": r"string",
                "required": True,
            },
            {
                "name": "httpStatusCode",
                "sanitized": "httpStatusCode",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "message",
                "sanitized": "message",
                "type": r"string",
                "required": True,
            },
            {
                "name": "badRequestErrorDetails",
                "sanitized": "badRequestErrorDetails",
                "type": r"array",
                "required": False,
            },
            {
                "name": "debugId",
                "sanitized": "debugId",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": ResponseSubscription,
        "name": "ResponseSubscription",
        "fields": [
            {
                "name": "id",
                "sanitized": "id",
                "type": r"string",
                "required": True,
            },
            {
                "name": "resourceUri",
                "sanitized": "resourceUri",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": HpeGreenLakeServerError,
        "name": "HpeGreenLakeServerError",
        "fields": [
            {
                "name": "debugId",
                "sanitized": "debugId",
                "type": r"string",
                "required": True,
            },
            {
                "name": "errorCode",
                "sanitized": "errorCode",
                "type": r"string",
                "required": True,
            },
            {
                "name": "httpStatusCode",
                "sanitized": "httpStatusCode",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "message",
                "sanitized": "message",
                "type": r"string",
                "required": True,
            },
            {
                "name": "serverErrorDetails",
                "sanitized": "serverErrorDetails",
                "type": r"array",
                "required": False,
            },
        ],
    },
    {
        "model": RequestCompute,
        "name": "RequestCompute",
        "fields": [
            {
                "name": "partNumber",
                "sanitized": "partNumber",
                "type": r"string",
                "required": True,
            },
            {
                "name": "serialNumber",
                "sanitized": "serialNumber",
                "type": r"string",
                "required": True,
            },
            {
                "name": "tags",
                "sanitized": "tags",
                "type": r"object",
                "required": False,
            },
        ],
    },
    {
        "model": RequestNetwork,
        "name": "RequestNetwork",
        "fields": [
            {
                "name": "tags",
                "sanitized": "tags",
                "type": r"object",
                "required": False,
            },
            {
                "name": "macAddress",
                "sanitized": "macAddress",
                "type": r"string",
                "required": True,
            },
            {
                "name": "serialNumber",
                "sanitized": "serialNumber",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": RequestSubscription,
        "name": "RequestSubscription",
        "fields": [
            {
                "name": "id",
                "sanitized": "id",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": PatchDevicesRequest,
        "name": "PatchDevicesRequest",
        "fields": [
            {
                "name": "subscription",
                "sanitized": "subscription",
                "type": r"array",
                "required": False,
            },
            {
                "name": "tenantPlatformCustomerId",
                "sanitized": "tenantPlatformCustomerId",
                "type": r"string",
                "required": False,
            },
            {
                "name": "application",
                "sanitized": "application",
                "type": r"object",
                "required": False,
            },
            {
                "name": "region",
                "sanitized": "region",
                "type": r"string",
                "required": False,
            },
        ],
    },
    {
        "model": ErrorIssue,
        "name": "ErrorIssue",
        "fields": [
            {
                "name": "description",
                "sanitized": "description",
                "type": r"string",
                "required": False,
            },
            {
                "name": "source",
                "sanitized": "source",
                "type": r"string",
                "required": False,
            },
            {
                "name": "subject",
                "sanitized": "subject",
                "type": r"string",
                "required": False,
            },
        ],
    },
    {
        "model": AsyncOperationResource,
        "name": "AsyncOperationResource",
        "fields": [
            {
                "name": "status",
                "sanitized": "status",
                "type": r"string",
                "required": False,
            },
            {
                "name": "timeoutMinutes",
                "sanitized": "timeoutMinutes",
                "type": r"integer",
                "required": False,
            },
            {
                "name": "id",
                "sanitized": "id",
                "type": r"string",
                "required": True,
            },
            {
                "name": "suggestedPollingIntervalSeconds",
                "sanitized": "suggestedPollingIntervalSeconds",
                "type": r"integer",
                "required": False,
            },
            {
                "name": "endedAt",
                "sanitized": "endedAt",
                "type": r"string",
                "required": False,
            },
            {
                "name": "result",
                "sanitized": "result",
                "type": r"object",
                "required": False,
            },
            {
                "name": "type",
                "sanitized": "type",
                "type": r"string",
                "required": True,
            },
            {
                "name": "progressPercent",
                "sanitized": "progressPercent",
                "type": r"integer",
                "required": False,
            },
            {
                "name": "resultType",
                "sanitized": "resultType",
                "type": r"string",
                "required": False,
            },
            {
                "name": "startedAt",
                "sanitized": "startedAt",
                "type": r"string",
                "required": False,
            },
        ],
    },
    {
        "model": AsyncResponse,
        "name": "AsyncResponse",
        "fields": [
            {
                "name": "status",
                "sanitized": "status",
                "type": r"string",
                "required": True,
            },
            {
                "name": "transactionId",
                "sanitized": "transactionId",
                "type": r"string",
                "required": True,
            },
            {
                "name": "code",
                "sanitized": "code",
                "type": r"integer",
                "required": True,
            },
        ],
    },
    {
        "model": BadRequestErrorDetail,
        "name": "BadRequestErrorDetail",
        "fields": [
            {
                "name": "issues",
                "sanitized": "issues",
                "type": r"array",
                "required": True,
            },
            {
                "name": "type",
                "sanitized": "type",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": DevicesGetResponse,
        "name": "DevicesGetResponse",
        "fields": [
            {
                "name": "offset",
                "sanitized": "offset",
                "type": r"integer",
                "required": False,
            },
            {
                "name": "total",
                "sanitized": "total",
                "type": r"integer",
                "required": False,
            },
            {
                "name": "count",
                "sanitized": "count",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "items",
                "sanitized": "items",
                "type": r"array",
                "required": True,
            },
        ],
    },
    {
        "model": DevicesPostRequest,
        "name": "DevicesPostRequest",
        "fields": [
            {
                "name": "compute",
                "sanitized": "compute",
                "type": r"array",
                "required": True,
            },
            {
                "name": "network",
                "sanitized": "network",
                "type": r"array",
                "required": True,
            },
            {
                "name": "storage",
                "sanitized": "storage",
                "type": r"array",
                "required": True,
            },
        ],
    },
    {
        "model": DevicesPostRequestV2Beta1,
        "name": "DevicesPostRequestV2Beta1",
        "fields": [
            {
                "name": "macAddress",
                "sanitized": "macAddress",
                "type": r"string",
                "required": False,
            },
            {
                "name": "partNumber",
                "sanitized": "partNumber",
                "type": r"string",
                "required": False,
            },
            {
                "name": "serialNumber",
                "sanitized": "serialNumber",
                "type": r"string",
                "required": True,
            },
            {
                "name": "tags",
                "sanitized": "tags",
                "type": r"object",
                "required": False,
            },
            {
                "name": "deviceType",
                "sanitized": "deviceType",
                "type": r"string",
                "required": True,
            },
            {
                "name": "location",
                "sanitized": "location",
                "type": r"object",
                "required": False,
            },
        ],
    },
    {
        "model": HpeGreenLakeGeneralError,
        "name": "HpeGreenLakeGeneralError",
        "fields": [
            {
                "name": "debugId",
                "sanitized": "debugId",
                "type": r"string",
                "required": True,
            },
            {
                "name": "errorCode",
                "sanitized": "errorCode",
                "type": r"string",
                "required": True,
            },
            {
                "name": "generalErrorDetails",
                "sanitized": "generalErrorDetails",
                "type": r"array",
                "required": False,
            },
            {
                "name": "httpStatusCode",
                "sanitized": "httpStatusCode",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "message",
                "sanitized": "message",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": ResponseSupportLevel,
        "name": "ResponseSupportLevel",
        "fields": [
            {
                "name": "serviceLevel",
                "sanitized": "serviceLevel",
                "type": r"string",
                "required": False,
            },
            {
                "name": "serviceLevelRank",
                "sanitized": "serviceLevelRank",
                "type": r"integer",
                "required": False,
            },
            {
                "name": "startDate",
                "sanitized": "startDate",
                "type": r"integer",
                "required": False,
            },
            {
                "name": "contractLevel",
                "sanitized": "contractLevel",
                "type": r"string",
                "required": False,
            },
            {
                "name": "contractLevelRank",
                "sanitized": "contractLevelRank",
                "type": r"integer",
                "required": False,
            },
            {
                "name": "endDate",
                "sanitized": "endDate",
                "type": r"integer",
                "required": False,
            },
        ],
    },
    {
        "model": PatchDevicesRequestV2,
        "name": "PatchDevicesRequestV2",
        "fields": [
            {
                "name": "tags",
                "sanitized": "tags",
                "type": r"object",
                "required": False,
            },
            {
                "name": "tenantWorkspaceId",
                "sanitized": "tenantWorkspaceId",
                "type": r"string",
                "required": False,
            },
            {
                "name": "application",
                "sanitized": "application",
                "type": r"object",
                "required": False,
            },
            {
                "name": "archived",
                "sanitized": "archived",
                "type": r"boolean",
                "required": False,
            },
            {
                "name": "region",
                "sanitized": "region",
                "type": r"string",
                "required": False,
            },
            {
                "name": "subscription",
                "sanitized": "subscription",
                "type": r"array",
                "required": False,
            },
        ],
    },
    {
        "model": ResponseDedicatedPlatform,
        "name": "ResponseDedicatedPlatform",
        "fields": [
            {
                "name": "id",
                "sanitized": "id",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": GeneralErrorDetail,
        "name": "GeneralErrorDetail",
        "fields": [
            {
                "name": "metadata",
                "sanitized": "metadata",
                "type": r"object",
                "required": True,
            },
            {
                "name": "source",
                "sanitized": "source",
                "type": r"string",
                "required": True,
            },
            {
                "name": "type",
                "sanitized": "type",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": RequestApplication,
        "name": "RequestApplication",
        "fields": [
            {
                "name": "id",
                "sanitized": "id",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": ResponseWarranty,
        "name": "ResponseWarranty",
        "fields": [
            {
                "name": "country",
                "sanitized": "country",
                "type": r"string",
                "required": False,
            },
            {
                "name": "currentSupportLevel",
                "sanitized": "currentSupportLevel",
                "type": r"object",
                "required": False,
            },
            {
                "name": "supportLevels",
                "sanitized": "supportLevels",
                "type": r"array",
                "required": False,
            },
        ],
    },
    {
        "model": ServerErrorDetail,
        "name": "ServerErrorDetail",
        "fields": [
            {
                "name": "retryAfterSeconds",
                "sanitized": "retryAfterSeconds",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "type",
                "sanitized": "type",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": RequestStorage,
        "name": "RequestStorage",
        "fields": [
            {
                "name": "serialNumber",
                "sanitized": "serialNumber",
                "type": r"string",
                "required": True,
            },
            {
                "name": "tags",
                "sanitized": "tags",
                "type": r"object",
                "required": False,
            },
            {
                "name": "partNumber",
                "sanitized": "partNumber",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": DeviceDetail,
        "name": "DeviceDetail",
        "fields": [
            {
                "name": "subscription",
                "sanitized": "subscription",
                "type": r"array",
                "required": False,
            },
            {
                "name": "application",
                "sanitized": "application",
                "type": r"object",
                "required": False,
            },
            {
                "name": "deviceName",
                "sanitized": "deviceName",
                "type": r"string",
                "required": False,
            },
            {
                "name": "dedicatedPlatformWorkspace",
                "sanitized": "dedicatedPlatformWorkspace",
                "type": r"object",
                "required": False,
            },
            {
                "name": "deviceType",
                "sanitized": "deviceType",
                "type": r"string",
                "required": False,
            },
            {
                "name": "id",
                "sanitized": "id",
                "type": r"string",
                "required": True,
            },
            {
                "name": "updatedAt",
                "sanitized": "updatedAt",
                "type": r"string",
                "required": False,
            },
            {
                "name": "tags",
                "sanitized": "tags",
                "type": r"object",
                "required": False,
            },
            {
                "name": "type",
                "sanitized": "type",
                "type": r"string",
                "required": True,
            },
            {
                "name": "serialNumber",
                "sanitized": "serialNumber",
                "type": r"string",
                "required": True,
            },
            {
                "name": "createdAt",
                "sanitized": "createdAt",
                "type": r"string",
                "required": False,
            },
            {
                "name": "warranty",
                "sanitized": "warranty",
                "type": r"object",
                "required": False,
            },
            {
                "name": "archived",
                "sanitized": "archived",
                "type": r"boolean",
                "required": False,
            },
            {
                "name": "assignedState",
                "sanitized": "assignedState",
                "type": r"string",
                "required": False,
            },
            {
                "name": "region",
                "sanitized": "region",
                "type": r"string",
                "required": False,
            },
            {
                "name": "location",
                "sanitized": "location",
                "type": r"object",
                "required": False,
            },
            {
                "name": "secondaryName",
                "sanitized": "secondaryName",
                "type": r"string",
                "required": False,
            },
            {
                "name": "partNumber",
                "sanitized": "partNumber",
                "type": r"string",
                "required": True,
            },
            {
                "name": "macAddress",
                "sanitized": "macAddress",
                "type": r"string",
                "required": False,
            },
            {
                "name": "model",
                "sanitized": "model",
                "type": r"string",
                "required": False,
            },
            {
                "name": "tenantWorkspaceId",
                "sanitized": "tenantWorkspaceId",
                "type": r"string",
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
    # Handle List[int] and List[integer]
    if "list[int" in normalized:
        return [1]
    # Handle List[float] and List[number]
    if "list[float" in normalized or "list[number" in normalized:
        return [1.0]
    # Handle List[bool] or List[boolean]
    if "list[bool" in normalized:
        return [True]
    # Handle List[str] or List[string]
    if "list[str" in normalized:
        return ["example"]
    # Generic list/array handler (fallback) - handles both OpenAPI "array" and Python "list"
    if "list" in normalized or "sequence" in normalized or "array" in normalized:
        return ["example"]
    if "dict" in normalized or "mapping" in normalized or "object" in normalized:
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
