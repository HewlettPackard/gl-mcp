# (c) Copyright 2025 Hewlett Packard Enterprise Development LP
"""Unit tests for generated Pydantic models."""

from __future__ import annotations

from typing import Any

import pytest
from pydantic import ValidationError as PydanticValidationError

from models import (
    BaseModel,
    RequestSubscription,
    ErrorIssue,
    ResponseApplication,
    DevicesPostRequestV2Beta1,
    RequestApplication,
    GeneralErrorDetail,
    RequestNetwork,
    ResponseLocation,
    ResponseWarranty,
    ServerErrorDetail,
    PatchDevicesRequest,
    AsyncResponse,
    DevicesGetResponse,
    ResponseSupportLevel,
    AsyncOperationResource,
    DeviceDetail,
    HpeGreenLakeBadRequestError,
    HpeGreenLakeServerError,
    RequestStorage,
    ResponseSubscription,
    RequestCompute,
    DevicesPostRequest,
    PatchDevicesRequestV2,
    BadRequestErrorDetail,
    HpeGreenLakeGeneralError,
)

MODEL_TEST_MATRIX = [
    {
        "model": RequestSubscription,
        "name": "RequestSubscription",
        "fields": [
            {
                "name": "id",
                "sanitized": "id",
                "type": r"str",
                "required": True,
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
                "type": r"str",
                "required": False,
            },
            {
                "name": "source",
                "sanitized": "source",
                "type": r"str",
                "required": False,
            },
            {
                "name": "subject",
                "sanitized": "subject",
                "type": r"str",
                "required": False,
            },
        ],
    },
    {
        "model": ResponseApplication,
        "name": "ResponseApplication",
        "fields": [
            {
                "name": "id",
                "sanitized": "id",
                "type": r"str",
                "required": True,
            },
            {
                "name": "resourceUri",
                "sanitized": "resourceUri",
                "type": r"str",
                "required": True,
            },
        ],
    },
    {
        "model": DevicesPostRequestV2Beta1,
        "name": "DevicesPostRequestV2Beta1",
        "fields": [
            {
                "name": "partNumber",
                "sanitized": "partNumber",
                "type": r"str",
                "required": False,
            },
            {
                "name": "serialNumber",
                "sanitized": "serialNumber",
                "type": r"str",
                "required": True,
            },
            {
                "name": "tags",
                "sanitized": "tags",
                "type": r"Dict[str, Any]",
                "required": False,
            },
            {
                "name": "deviceType",
                "sanitized": "deviceType",
                "type": r"str",
                "required": True,
            },
            {
                "name": "location",
                "sanitized": "location",
                "type": r"Dict[str, Any]",
                "required": False,
            },
            {
                "name": "macAddress",
                "sanitized": "macAddress",
                "type": r"str",
                "required": False,
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
                "type": r"str",
                "required": True,
            },
        ],
    },
    {
        "model": GeneralErrorDetail,
        "name": "GeneralErrorDetail",
        "fields": [
            {
                "name": "source",
                "sanitized": "source",
                "type": r"str",
                "required": True,
            },
            {
                "name": "type",
                "sanitized": "type",
                "type": r"str",
                "required": True,
            },
            {
                "name": "metadata",
                "sanitized": "metadata",
                "type": r"Dict[str, Any]",
                "required": True,
            },
        ],
    },
    {
        "model": RequestNetwork,
        "name": "RequestNetwork",
        "fields": [
            {
                "name": "macAddress",
                "sanitized": "macAddress",
                "type": r"str",
                "required": True,
            },
            {
                "name": "serialNumber",
                "sanitized": "serialNumber",
                "type": r"str",
                "required": True,
            },
            {
                "name": "tags",
                "sanitized": "tags",
                "type": r"Dict[str, Any]",
                "required": False,
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
                "type": r"str",
                "required": True,
            },
            {
                "name": "resourceUri",
                "sanitized": "resourceUri",
                "type": r"str",
                "required": True,
            },
        ],
    },
    {
        "model": ResponseWarranty,
        "name": "ResponseWarranty",
        "fields": [
            {
                "name": "currentSupportLevel",
                "sanitized": "currentSupportLevel",
                "type": r"Dict[str, Any]",
                "required": False,
            },
            {
                "name": "supportLevels",
                "sanitized": "supportLevels",
                "type": r"List[Dict[str, Any]]",
                "required": False,
            },
            {
                "name": "country",
                "sanitized": "country",
                "type": r"str",
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
                "type": r"int",
                "required": True,
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
        "model": PatchDevicesRequest,
        "name": "PatchDevicesRequest",
        "fields": [
            {
                "name": "region",
                "sanitized": "region",
                "type": r"str",
                "required": False,
            },
            {
                "name": "subscription",
                "sanitized": "subscription",
                "type": r"List[Dict[str, Any]]",
                "required": False,
            },
            {
                "name": "tenantPlatformCustomerId",
                "sanitized": "tenantPlatformCustomerId",
                "type": r"str",
                "required": False,
            },
            {
                "name": "application",
                "sanitized": "application",
                "type": r"Dict[str, Any]",
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
                "type": r"str",
                "required": True,
            },
            {
                "name": "transactionId",
                "sanitized": "transactionId",
                "type": r"str",
                "required": True,
            },
            {
                "name": "code",
                "sanitized": "code",
                "type": r"int",
                "required": True,
            },
        ],
    },
    {
        "model": DevicesGetResponse,
        "name": "DevicesGetResponse",
        "fields": [
            {
                "name": "total",
                "sanitized": "total",
                "type": r"int",
                "required": False,
            },
            {
                "name": "count",
                "sanitized": "count",
                "type": r"int",
                "required": True,
            },
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
                "required": False,
            },
        ],
    },
    {
        "model": ResponseSupportLevel,
        "name": "ResponseSupportLevel",
        "fields": [
            {
                "name": "startDate",
                "sanitized": "startDate",
                "type": r"int",
                "required": False,
            },
            {
                "name": "contractLevel",
                "sanitized": "contractLevel",
                "type": r"str",
                "required": False,
            },
            {
                "name": "contractLevelRank",
                "sanitized": "contractLevelRank",
                "type": r"int",
                "required": False,
            },
            {
                "name": "endDate",
                "sanitized": "endDate",
                "type": r"int",
                "required": False,
            },
            {
                "name": "serviceLevel",
                "sanitized": "serviceLevel",
                "type": r"str",
                "required": False,
            },
            {
                "name": "serviceLevelRank",
                "sanitized": "serviceLevelRank",
                "type": r"int",
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
                "type": r"str",
                "required": False,
            },
            {
                "name": "suggestedPollingIntervalSeconds",
                "sanitized": "suggestedPollingIntervalSeconds",
                "type": r"int",
                "required": False,
            },
            {
                "name": "progressPercent",
                "sanitized": "progressPercent",
                "type": r"int",
                "required": False,
            },
            {
                "name": "startedAt",
                "sanitized": "startedAt",
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
                "name": "result",
                "sanitized": "result",
                "type": r"Dict[str, Any]",
                "required": False,
            },
            {
                "name": "resultType",
                "sanitized": "resultType",
                "type": r"str",
                "required": False,
            },
            {
                "name": "timeoutMinutes",
                "sanitized": "timeoutMinutes",
                "type": r"int",
                "required": False,
            },
            {
                "name": "type",
                "sanitized": "type",
                "type": r"str",
                "required": True,
            },
            {
                "name": "endedAt",
                "sanitized": "endedAt",
                "type": r"str",
                "required": False,
            },
        ],
    },
    {
        "model": DeviceDetail,
        "name": "DeviceDetail",
        "fields": [
            {
                "name": "partNumber",
                "sanitized": "partNumber",
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
                "name": "location",
                "sanitized": "location",
                "type": r"Dict[str, Any]",
                "required": False,
            },
            {
                "name": "id",
                "sanitized": "id",
                "type": r"str",
                "required": True,
            },
            {
                "name": "tags",
                "sanitized": "tags",
                "type": r"Dict[str, Any]",
                "required": False,
            },
            {
                "name": "application",
                "sanitized": "application",
                "type": r"Dict[str, Any]",
                "required": False,
            },
            {
                "name": "assignedState",
                "sanitized": "assignedState",
                "type": r"str",
                "required": False,
            },
            {
                "name": "region",
                "sanitized": "region",
                "type": r"str",
                "required": False,
            },
            {
                "name": "subscription",
                "sanitized": "subscription",
                "type": r"List[Dict[str, Any]]",
                "required": False,
            },
            {
                "name": "model",
                "sanitized": "model",
                "type": r"str",
                "required": False,
            },
            {
                "name": "archived",
                "sanitized": "archived",
                "type": r"bool",
                "required": False,
            },
            {
                "name": "serialNumber",
                "sanitized": "serialNumber",
                "type": r"str",
                "required": True,
            },
            {
                "name": "macAddress",
                "sanitized": "macAddress",
                "type": r"str",
                "required": False,
            },
            {
                "name": "warranty",
                "sanitized": "warranty",
                "type": r"Dict[str, Any]",
                "required": False,
            },
            {
                "name": "updatedAt",
                "sanitized": "updatedAt",
                "type": r"str",
                "required": False,
            },
            {
                "name": "deviceType",
                "sanitized": "deviceType",
                "type": r"str",
                "required": False,
            },
            {
                "name": "type",
                "sanitized": "type",
                "type": r"str",
                "required": True,
            },
            {
                "name": "tenantWorkspaceId",
                "sanitized": "tenantWorkspaceId",
                "type": r"str",
                "required": False,
            },
        ],
    },
    {
        "model": HpeGreenLakeBadRequestError,
        "name": "HpeGreenLakeBadRequestError",
        "fields": [
            {
                "name": "badRequestErrorDetails",
                "sanitized": "badRequestErrorDetails",
                "type": r"List[Dict[str, Any]]",
                "required": False,
            },
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
        "model": HpeGreenLakeServerError,
        "name": "HpeGreenLakeServerError",
        "fields": [
            {
                "name": "message",
                "sanitized": "message",
                "type": r"str",
                "required": True,
            },
            {
                "name": "serverErrorDetails",
                "sanitized": "serverErrorDetails",
                "type": r"List[Dict[str, Any]]",
                "required": False,
            },
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
        ],
    },
    {
        "model": RequestStorage,
        "name": "RequestStorage",
        "fields": [
            {
                "name": "partNumber",
                "sanitized": "partNumber",
                "type": r"str",
                "required": True,
            },
            {
                "name": "serialNumber",
                "sanitized": "serialNumber",
                "type": r"str",
                "required": True,
            },
            {
                "name": "tags",
                "sanitized": "tags",
                "type": r"Dict[str, Any]",
                "required": False,
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
                "type": r"str",
                "required": True,
            },
            {
                "name": "resourceUri",
                "sanitized": "resourceUri",
                "type": r"str",
                "required": True,
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
                "type": r"str",
                "required": True,
            },
            {
                "name": "serialNumber",
                "sanitized": "serialNumber",
                "type": r"str",
                "required": True,
            },
            {
                "name": "tags",
                "sanitized": "tags",
                "type": r"Dict[str, Any]",
                "required": False,
            },
        ],
    },
    {
        "model": DevicesPostRequest,
        "name": "DevicesPostRequest",
        "fields": [
            {
                "name": "network",
                "sanitized": "network",
                "type": r"List[Dict[str, Any]]",
                "required": True,
            },
            {
                "name": "storage",
                "sanitized": "storage",
                "type": r"List[Dict[str, Any]]",
                "required": True,
            },
            {
                "name": "compute",
                "sanitized": "compute",
                "type": r"List[Dict[str, Any]]",
                "required": True,
            },
        ],
    },
    {
        "model": PatchDevicesRequestV2,
        "name": "PatchDevicesRequestV2",
        "fields": [
            {
                "name": "application",
                "sanitized": "application",
                "type": r"Dict[str, Any]",
                "required": False,
            },
            {
                "name": "archived",
                "sanitized": "archived",
                "type": r"bool",
                "required": False,
            },
            {
                "name": "region",
                "sanitized": "region",
                "type": r"str",
                "required": False,
            },
            {
                "name": "subscription",
                "sanitized": "subscription",
                "type": r"List[Dict[str, Any]]",
                "required": False,
            },
            {
                "name": "tags",
                "sanitized": "tags",
                "type": r"Dict[str, Any]",
                "required": False,
            },
            {
                "name": "tenantWorkspaceId",
                "sanitized": "tenantWorkspaceId",
                "type": r"str",
                "required": False,
            },
        ],
    },
    {
        "model": BadRequestErrorDetail,
        "name": "BadRequestErrorDetail",
        "fields": [
            {
                "name": "type",
                "sanitized": "type",
                "type": r"str",
                "required": True,
            },
            {
                "name": "issues",
                "sanitized": "issues",
                "type": r"List[Dict[str, Any]]",
                "required": True,
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
                "name": "generalErrorDetails",
                "sanitized": "generalErrorDetails",
                "type": r"List[Dict[str, Any]]",
                "required": False,
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
