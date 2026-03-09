# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""Unit tests for generated Pydantic models."""

from __future__ import annotations

from typing import Any

import pytest
from pydantic import ValidationError as PydanticValidationError

from models import (
    BaseModel,
    AutoSubscriptionsPostRequest,
    AutoSubscriptionsResponseDtoWithTenant,
    ErrorIssue,
    RequestPostAutoSubscription,
    GeneralErrorDetail,
    HpeGreenLakeBadRequestError,
    AutoSubscriptionsResponsePaginatedDto,
    HpeGreenLakeGeneralError,
    ServerErrorDetail,
    V1Beta1SubscriptionDetail,
    AutoSubscriptionsResponseDto,
    BulkUnclaimId,
    SubscriptionsGetResponse,
    RequestPostSubscription,
    SubscriptionDetail,
    SubscriptionsPostRequest,
    SubscriptionsBulkUnclaimRequest,
    V1Beta1SubscriptionsGetResponse,
    AsyncOperationResource,
    AsyncResponse,
    AutoSubscriptionSettings,
    Appointment,
    HpeGreenLakeServerError,
    SubscriptionsPatchRequest,
    BadRequestErrorDetail,
)

MODEL_TEST_MATRIX = [
    {
        "model": AutoSubscriptionsPostRequest,
        "name": "AutoSubscriptionsPostRequest",
        "fields": [
            {
                "name": "autoSubscriptionSettings",
                "sanitized": "autoSubscriptionSettings",
                "type": r"array",
                "required": False,
            },
        ],
    },
    {
        "model": AutoSubscriptionsResponseDtoWithTenant,
        "name": "AutoSubscriptionsResponseDtoWithTenant",
        "fields": [
            {
                "name": "generation",
                "sanitized": "generation",
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
                "name": "resourceUri",
                "sanitized": "resourceUri",
                "type": r"string",
                "required": True,
            },
            {
                "name": "tenantWorkspaceId",
                "sanitized": "tenantWorkspaceId",
                "type": r"string",
                "required": False,
            },
            {
                "name": "type",
                "sanitized": "type",
                "type": r"string",
                "required": True,
            },
            {
                "name": "updatedAt",
                "sanitized": "updatedAt",
                "type": r"string",
                "required": True,
            },
            {
                "name": "autoSubscriptionSettings",
                "sanitized": "autoSubscriptionSettings",
                "type": r"array",
                "required": False,
            },
            {
                "name": "createdAt",
                "sanitized": "createdAt",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": ErrorIssue,
        "name": "ErrorIssue",
        "fields": [
            {
                "name": "subject",
                "sanitized": "subject",
                "type": r"string",
                "required": False,
            },
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
        ],
    },
    {
        "model": RequestPostAutoSubscription,
        "name": "RequestPostAutoSubscription",
        "fields": [
            {
                "name": "deviceType",
                "sanitized": "deviceType",
                "type": r"string",
                "required": True,
            },
            {
                "name": "tier",
                "sanitized": "tier",
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
                "name": "errorDetails",
                "sanitized": "errorDetails",
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
            {
                "name": "debugId",
                "sanitized": "debugId",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": AutoSubscriptionsResponsePaginatedDto,
        "name": "AutoSubscriptionsResponsePaginatedDto",
        "fields": [
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
        ],
    },
    {
        "model": HpeGreenLakeGeneralError,
        "name": "HpeGreenLakeGeneralError",
        "fields": [
            {
                "name": "message",
                "sanitized": "message",
                "type": r"string",
                "required": True,
            },
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
                "name": "errorDetails",
                "sanitized": "errorDetails",
                "type": r"array",
                "required": False,
            },
            {
                "name": "httpStatusCode",
                "sanitized": "httpStatusCode",
                "type": r"integer",
                "required": True,
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
        "model": V1Beta1SubscriptionDetail,
        "name": "V1Beta1SubscriptionDetail",
        "fields": [
            {
                "name": "po",
                "sanitized": "po",
                "type": r"string",
                "required": False,
            },
            {
                "name": "productType",
                "sanitized": "productType",
                "type": r"string",
                "required": False,
            },
            {
                "name": "tierDescription",
                "sanitized": "tierDescription",
                "type": r"string",
                "required": False,
            },
            {
                "name": "endTime",
                "sanitized": "endTime",
                "type": r"string",
                "required": False,
            },
            {
                "name": "resellerPo",
                "sanitized": "resellerPo",
                "type": r"string",
                "required": False,
            },
            {
                "name": "startTime",
                "sanitized": "startTime",
                "type": r"string",
                "required": False,
            },
            {
                "name": "availableQuantity",
                "sanitized": "availableQuantity",
                "type": r"string",
                "required": False,
            },
            {
                "name": "quote",
                "sanitized": "quote",
                "type": r"string",
                "required": False,
            },
            {
                "name": "key",
                "sanitized": "key",
                "type": r"string",
                "required": False,
            },
            {
                "name": "skuDescription",
                "sanitized": "skuDescription",
                "type": r"string",
                "required": False,
            },
            {
                "name": "tier",
                "sanitized": "tier",
                "type": r"string",
                "required": False,
            },
            {
                "name": "subscriptionType",
                "sanitized": "subscriptionType",
                "type": r"string",
                "required": False,
            },
            {
                "name": "sku",
                "sanitized": "sku",
                "type": r"string",
                "required": False,
            },
            {
                "name": "quantity",
                "sanitized": "quantity",
                "type": r"string",
                "required": False,
            },
            {
                "name": "createdAt",
                "sanitized": "createdAt",
                "type": r"string",
                "required": False,
            },
            {
                "name": "type",
                "sanitized": "type",
                "type": r"string",
                "required": True,
            },
            {
                "name": "contract",
                "sanitized": "contract",
                "type": r"string",
                "required": False,
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
                "name": "subscriptionStatus",
                "sanitized": "subscriptionStatus",
                "type": r"string",
                "required": False,
            },
            {
                "name": "isEval",
                "sanitized": "isEval",
                "type": r"boolean",
                "required": False,
            },
            {
                "name": "id",
                "sanitized": "id",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": AutoSubscriptionsResponseDto,
        "name": "AutoSubscriptionsResponseDto",
        "fields": [
            {
                "name": "autoSubscriptionSettings",
                "sanitized": "autoSubscriptionSettings",
                "type": r"array",
                "required": False,
            },
            {
                "name": "createdAt",
                "sanitized": "createdAt",
                "type": r"string",
                "required": True,
            },
            {
                "name": "generation",
                "sanitized": "generation",
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
                "name": "resourceUri",
                "sanitized": "resourceUri",
                "type": r"string",
                "required": True,
            },
            {
                "name": "type",
                "sanitized": "type",
                "type": r"string",
                "required": True,
            },
            {
                "name": "updatedAt",
                "sanitized": "updatedAt",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": BulkUnclaimId,
        "name": "BulkUnclaimId",
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
        "model": SubscriptionsGetResponse,
        "name": "SubscriptionsGetResponse",
        "fields": [
            {
                "name": "items",
                "sanitized": "items",
                "type": r"array",
                "required": True,
            },
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
        ],
    },
    {
        "model": RequestPostSubscription,
        "name": "RequestPostSubscription",
        "fields": [
            {
                "name": "tags",
                "sanitized": "tags",
                "type": r"object",
                "required": False,
            },
            {
                "name": "key",
                "sanitized": "key",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": SubscriptionDetail,
        "name": "SubscriptionDetail",
        "fields": [
            {
                "name": "po",
                "sanitized": "po",
                "type": r"string",
                "required": False,
            },
            {
                "name": "productSku",
                "sanitized": "productSku",
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
                "name": "orderClass",
                "sanitized": "orderClass",
                "type": r"string",
                "required": False,
            },
            {
                "name": "quantity",
                "sanitized": "quantity",
                "type": r"string",
                "required": False,
            },
            {
                "name": "productDescription",
                "sanitized": "productDescription",
                "type": r"string",
                "required": False,
            },
            {
                "name": "quote",
                "sanitized": "quote",
                "type": r"string",
                "required": False,
            },
            {
                "name": "aasType",
                "sanitized": "aasType",
                "type": r"string",
                "required": False,
            },
            {
                "name": "endUserName",
                "sanitized": "endUserName",
                "type": r"string",
                "required": False,
            },
            {
                "name": "evaluationType",
                "sanitized": "evaluationType",
                "type": r"string",
                "required": False,
            },
            {
                "name": "key",
                "sanitized": "key",
                "type": r"string",
                "required": False,
            },
            {
                "name": "appointment",
                "sanitized": "appointment",
                "type": r"object",
                "required": False,
            },
            {
                "name": "contract",
                "sanitized": "contract",
                "type": r"string",
                "required": False,
            },
        ],
    },
    {
        "model": SubscriptionsPostRequest,
        "name": "SubscriptionsPostRequest",
        "fields": [
            {
                "name": "subscriptions",
                "sanitized": "subscriptions",
                "type": r"array",
                "required": True,
            },
        ],
    },
    {
        "model": SubscriptionsBulkUnclaimRequest,
        "name": "SubscriptionsBulkUnclaimRequest",
        "fields": [
            {
                "name": "items",
                "sanitized": "items",
                "type": r"array",
                "required": True,
            },
        ],
    },
    {
        "model": V1Beta1SubscriptionsGetResponse,
        "name": "V1Beta1SubscriptionsGetResponse",
        "fields": [
            {
                "name": "items",
                "sanitized": "items",
                "type": r"array",
                "required": True,
            },
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
        ],
    },
    {
        "model": AsyncOperationResource,
        "name": "AsyncOperationResource",
        "fields": [
            {
                "name": "suggestedPollingIntervalSeconds",
                "sanitized": "suggestedPollingIntervalSeconds",
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
                "name": "timeoutMinutes",
                "sanitized": "timeoutMinutes",
                "type": r"integer",
                "required": False,
            },
            {
                "name": "startedAt",
                "sanitized": "startedAt",
                "type": r"string",
                "required": False,
            },
            {
                "name": "status",
                "sanitized": "status",
                "type": r"string",
                "required": False,
            },
            {
                "name": "endedAt",
                "sanitized": "endedAt",
                "type": r"string",
                "required": False,
            },
            {
                "name": "type",
                "sanitized": "type",
                "type": r"string",
                "required": True,
            },
            {
                "name": "id",
                "sanitized": "id",
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
                "name": "error",
                "sanitized": "error",
                "type": r"object",
                "required": False,
            },
            {
                "name": "result",
                "sanitized": "result",
                "type": r"object",
                "required": False,
            },
        ],
    },
    {
        "model": AsyncResponse,
        "name": "AsyncResponse",
        "fields": [
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
            {
                "name": "status",
                "sanitized": "status",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": AutoSubscriptionSettings,
        "name": "AutoSubscriptionSettings",
        "fields": [
            {
                "name": "deviceType",
                "sanitized": "deviceType",
                "type": r"string",
                "required": True,
            },
            {
                "name": "tier",
                "sanitized": "tier",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": Appointment,
        "name": "Appointment",
        "fields": [
            {
                "name": "subscriptionEnd",
                "sanitized": "subscriptionEnd",
                "type": r"string",
                "required": False,
            },
            {
                "name": "subscriptionStart",
                "sanitized": "subscriptionStart",
                "type": r"string",
                "required": False,
            },
            {
                "name": "delayedActivation",
                "sanitized": "delayedActivation",
                "type": r"string",
                "required": False,
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
                "type": r"string",
                "required": True,
            },
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
                "name": "errorDetails",
                "sanitized": "errorDetails",
                "type": r"array",
                "required": False,
            },
            {
                "name": "httpStatusCode",
                "sanitized": "httpStatusCode",
                "type": r"integer",
                "required": True,
            },
        ],
    },
    {
        "model": SubscriptionsPatchRequest,
        "name": "SubscriptionsPatchRequest",
        "fields": [
            {
                "name": "tags",
                "sanitized": "tags",
                "type": r"object",
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
