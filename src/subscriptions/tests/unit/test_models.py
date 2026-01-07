# (c) Copyright 2025 Hewlett Packard Enterprise Development LP
"""Unit tests for generated Pydantic models."""

from __future__ import annotations

from typing import Any

import pytest
from pydantic import ValidationError as PydanticValidationError

from models import (
    BaseModel,
    BadRequestErrorDetail,
    AsyncOperationResource,
    AutoSubscriptionsPostRequest,
    V1Beta1SubscriptionsGetResponse,
    AutoSubscriptionSettings,
    HpeGreenLakeGeneralError,
    ErrorIssue,
    GeneralErrorDetail,
    HpeGreenLakeServerError,
    SubscriptionsPostRequest,
    AsyncResponse,
    V1Beta1SubscriptionDetail,
    HpeGreenLakeBadRequestError,
    AutoSubscriptionsResponseDto,
    AutoSubscriptionsResponseDtoWithTenant,
    ServerErrorDetail,
    SubscriptionsPatchRequest,
    RequestPostSubscription,
    Appointment,
    AutoSubscriptionsResponsePaginatedDto,
    RequestPostAutoSubscription,
    SubscriptionDetail,
    SubscriptionsGetResponse,
)

MODEL_TEST_MATRIX = [
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
                "name": "timeoutMinutes",
                "sanitized": "timeoutMinutes",
                "type": r"int",
                "required": False,
            },
            {
                "name": "result",
                "sanitized": "result",
                "type": r"Dict[str, Any]",
                "required": False,
            },
            {
                "name": "type",
                "sanitized": "type",
                "type": r"str",
                "required": True,
            },
            {
                "name": "id",
                "sanitized": "id",
                "type": r"str",
                "required": True,
            },
            {
                "name": "progressPercent",
                "sanitized": "progressPercent",
                "type": r"int",
                "required": False,
            },
            {
                "name": "resultType",
                "sanitized": "resultType",
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
                "name": "startedAt",
                "sanitized": "startedAt",
                "type": r"str",
                "required": False,
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
        "model": AutoSubscriptionsPostRequest,
        "name": "AutoSubscriptionsPostRequest",
        "fields": [
            {
                "name": "autoSubscriptionSettings",
                "sanitized": "autoSubscriptionSettings",
                "type": r"List[Dict[str, Any]]",
                "required": False,
            },
        ],
    },
    {
        "model": V1Beta1SubscriptionsGetResponse,
        "name": "V1Beta1SubscriptionsGetResponse",
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
        "model": AutoSubscriptionSettings,
        "name": "AutoSubscriptionSettings",
        "fields": [
            {
                "name": "deviceType",
                "sanitized": "deviceType",
                "type": r"str",
                "required": True,
            },
            {
                "name": "tier",
                "sanitized": "tier",
                "type": r"str",
                "required": True,
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
                "type": r"str",
                "required": True,
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
        ],
    },
    {
        "model": ErrorIssue,
        "name": "ErrorIssue",
        "fields": [
            {
                "name": "subject",
                "sanitized": "subject",
                "type": r"str",
                "required": False,
            },
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
        ],
    },
    {
        "model": GeneralErrorDetail,
        "name": "GeneralErrorDetail",
        "fields": [
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
            {
                "name": "source",
                "sanitized": "source",
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
        ],
    },
    {
        "model": SubscriptionsPostRequest,
        "name": "SubscriptionsPostRequest",
        "fields": [
            {
                "name": "subscriptions",
                "sanitized": "subscriptions",
                "type": r"List[Dict[str, Any]]",
                "required": True,
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
        "model": V1Beta1SubscriptionDetail,
        "name": "V1Beta1SubscriptionDetail",
        "fields": [
            {
                "name": "isEval",
                "sanitized": "isEval",
                "type": r"bool",
                "required": False,
            },
            {
                "name": "skuDescription",
                "sanitized": "skuDescription",
                "type": r"str",
                "required": False,
            },
            {
                "name": "quantity",
                "sanitized": "quantity",
                "type": r"str",
                "required": False,
            },
            {
                "name": "tags",
                "sanitized": "tags",
                "type": r"Dict[str, Any]",
                "required": False,
            },
            {
                "name": "type",
                "sanitized": "type",
                "type": r"str",
                "required": True,
            },
            {
                "name": "availableQuantity",
                "sanitized": "availableQuantity",
                "type": r"str",
                "required": False,
            },
            {
                "name": "createdAt",
                "sanitized": "createdAt",
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
                "name": "endTime",
                "sanitized": "endTime",
                "type": r"str",
                "required": False,
            },
            {
                "name": "productType",
                "sanitized": "productType",
                "type": r"str",
                "required": False,
            },
            {
                "name": "startTime",
                "sanitized": "startTime",
                "type": r"str",
                "required": False,
            },
            {
                "name": "tier",
                "sanitized": "tier",
                "type": r"str",
                "required": False,
            },
            {
                "name": "sku",
                "sanitized": "sku",
                "type": r"str",
                "required": False,
            },
            {
                "name": "subscriptionStatus",
                "sanitized": "subscriptionStatus",
                "type": r"str",
                "required": False,
            },
            {
                "name": "contract",
                "sanitized": "contract",
                "type": r"str",
                "required": False,
            },
            {
                "name": "subscriptionType",
                "sanitized": "subscriptionType",
                "type": r"str",
                "required": False,
            },
            {
                "name": "key",
                "sanitized": "key",
                "type": r"str",
                "required": False,
            },
            {
                "name": "id",
                "sanitized": "id",
                "type": r"str",
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
        ],
    },
    {
        "model": AutoSubscriptionsResponseDto,
        "name": "AutoSubscriptionsResponseDto",
        "fields": [
            {
                "name": "resourceUri",
                "sanitized": "resourceUri",
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
                "name": "updatedAt",
                "sanitized": "updatedAt",
                "type": r"str",
                "required": True,
            },
            {
                "name": "autoSubscriptionSettings",
                "sanitized": "autoSubscriptionSettings",
                "type": r"List[Dict[str, Any]]",
                "required": False,
            },
            {
                "name": "createdAt",
                "sanitized": "createdAt",
                "type": r"str",
                "required": True,
            },
            {
                "name": "generation",
                "sanitized": "generation",
                "type": r"int",
                "required": False,
            },
            {
                "name": "id",
                "sanitized": "id",
                "type": r"str",
                "required": True,
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
                "type": r"int",
                "required": False,
            },
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
            {
                "name": "tenantWorkspaceId",
                "sanitized": "tenantWorkspaceId",
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
                "name": "updatedAt",
                "sanitized": "updatedAt",
                "type": r"str",
                "required": True,
            },
            {
                "name": "autoSubscriptionSettings",
                "sanitized": "autoSubscriptionSettings",
                "type": r"List[Dict[str, Any]]",
                "required": False,
            },
            {
                "name": "createdAt",
                "sanitized": "createdAt",
                "type": r"str",
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
        "model": SubscriptionsPatchRequest,
        "name": "SubscriptionsPatchRequest",
        "fields": [
            {
                "name": "tags",
                "sanitized": "tags",
                "type": r"Dict[str, Any]",
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
                "type": r"Dict[str, Any]",
                "required": False,
            },
            {
                "name": "key",
                "sanitized": "key",
                "type": r"str",
                "required": True,
            },
        ],
    },
    {
        "model": Appointment,
        "name": "Appointment",
        "fields": [
            {
                "name": "subscriptionStart",
                "sanitized": "subscriptionStart",
                "type": r"str",
                "required": False,
            },
            {
                "name": "delayedActivation",
                "sanitized": "delayedActivation",
                "type": r"str",
                "required": False,
            },
            {
                "name": "subscriptionEnd",
                "sanitized": "subscriptionEnd",
                "type": r"str",
                "required": False,
            },
        ],
    },
    {
        "model": AutoSubscriptionsResponsePaginatedDto,
        "name": "AutoSubscriptionsResponsePaginatedDto",
        "fields": [
            {
                "name": "offset",
                "sanitized": "offset",
                "type": r"int",
                "required": False,
            },
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
        ],
    },
    {
        "model": RequestPostAutoSubscription,
        "name": "RequestPostAutoSubscription",
        "fields": [
            {
                "name": "tier",
                "sanitized": "tier",
                "type": r"str",
                "required": True,
            },
            {
                "name": "deviceType",
                "sanitized": "deviceType",
                "type": r"str",
                "required": True,
            },
        ],
    },
    {
        "model": SubscriptionDetail,
        "name": "SubscriptionDetail",
        "fields": [
            {
                "name": "aasType",
                "sanitized": "aasType",
                "type": r"str",
                "required": False,
            },
            {
                "name": "productSku",
                "sanitized": "productSku",
                "type": r"str",
                "required": False,
            },
            {
                "name": "productDescription",
                "sanitized": "productDescription",
                "type": r"str",
                "required": False,
            },
            {
                "name": "contract",
                "sanitized": "contract",
                "type": r"str",
                "required": False,
            },
            {
                "name": "po",
                "sanitized": "po",
                "type": r"str",
                "required": False,
            },
            {
                "name": "endUserName",
                "sanitized": "endUserName",
                "type": r"str",
                "required": False,
            },
            {
                "name": "key",
                "sanitized": "key",
                "type": r"str",
                "required": False,
            },
            {
                "name": "quantity",
                "sanitized": "quantity",
                "type": r"str",
                "required": False,
            },
            {
                "name": "appointment",
                "sanitized": "appointment",
                "type": r"Dict[str, Any]",
                "required": False,
            },
            {
                "name": "orderClass",
                "sanitized": "orderClass",
                "type": r"str",
                "required": False,
            },
            {
                "name": "evaluationType",
                "sanitized": "evaluationType",
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
                "name": "quote",
                "sanitized": "quote",
                "type": r"str",
                "required": False,
            },
        ],
    },
    {
        "model": SubscriptionsGetResponse,
        "name": "SubscriptionsGetResponse",
        "fields": [
            {
                "name": "offset",
                "sanitized": "offset",
                "type": r"int",
                "required": False,
            },
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
    # Generic list handler (fallback)
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
