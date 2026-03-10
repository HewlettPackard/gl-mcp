# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""Unit tests for generated Pydantic models."""

from __future__ import annotations

from typing import Any

import pytest
from pydantic import ValidationError as PydanticValidationError

from models import (
    BaseModel,
    UsageByEntity,
    UsageTotals,
    UsageSeries,
    CloudUsageByEntity,
    CloudUsageTotals,
    CloudUsageSeries,
    Coefficient,
    Ingest,
    DataSource,
    ForecastEnergyResponse,
    PaginatedResponse,
    Error,
)

MODEL_TEST_MATRIX = [
    {
        "model": UsageByEntity,
        "name": "UsageByEntity",
        "fields": [
            {"name": "id", "sanitized": "id", "type": r"string", "required": False},
            {"name": "type", "sanitized": "type", "type": r"string", "required": False},
            {"name": "entityId", "sanitized": "entityId", "type": r"string", "required": False},
            {"name": "entityMake", "sanitized": "entityMake", "type": r"string", "required": False},
            {"name": "entityModel", "sanitized": "entityModel", "type": r"string", "required": False},
            {"name": "entityType", "sanitized": "entityType", "type": r"string", "required": False},
            {"name": "entitySerialNum", "sanitized": "entitySerialNum", "type": r"string", "required": False},
            {"name": "entityProductId", "sanitized": "entityProductId", "type": r"string", "required": False},
            {"name": "entityManufactureTimestamp", "sanitized": "entityManufactureTimestamp", "type": r"string", "required": False},
            {"name": "locationName", "sanitized": "locationName", "type": r"string", "required": False},
            {"name": "locationId", "sanitized": "locationId", "type": r"string", "required": False},
            {"name": "locationCity", "sanitized": "locationCity", "type": r"string", "required": False},
            {"name": "locationState", "sanitized": "locationState", "type": r"string", "required": False},
            {"name": "locationCountry", "sanitized": "locationCountry", "type": r"string", "required": False},
            {"name": "tags", "sanitized": "tags", "type": r"list[dict]", "required": False},
            {"name": "name", "sanitized": "name", "type": r"string", "required": False},
            {"name": "cost", "sanitized": "cost", "type": r"number", "required": False},
            {"name": "costUsd", "sanitized": "costUsd", "type": r"number", "required": False},
            {"name": "currency", "sanitized": "currency", "type": r"string", "required": False},
            {"name": "co2eMetricTon", "sanitized": "co2eMetricTon", "type": r"number", "required": False},
            {"name": "kwh", "sanitized": "kwh", "type": r"number", "required": False},
        ],
    },
    {
        "model": UsageTotals,
        "name": "UsageTotals",
        "fields": [
            {"name": "type", "sanitized": "type", "type": r"string", "required": False},
            {"name": "cost", "sanitized": "cost", "type": r"number", "required": False},
            {"name": "costUsd", "sanitized": "costUsd", "type": r"number", "required": False},
            {"name": "currency", "sanitized": "currency", "type": r"string", "required": False},
            {"name": "co2eMetricTon", "sanitized": "co2eMetricTon", "type": r"number", "required": False},
            {"name": "kwh", "sanitized": "kwh", "type": r"number", "required": False},
        ],
    },
    {
        "model": UsageSeries,
        "name": "UsageSeries",
        "fields": [
            {"name": "id", "sanitized": "id", "type": r"string", "required": False},
            {"name": "type", "sanitized": "type", "type": r"string", "required": False},
            {"name": "timeBucket", "sanitized": "timeBucket", "type": r"string", "required": False},
            {"name": "cost", "sanitized": "cost", "type": r"number", "required": False},
            {"name": "currency", "sanitized": "currency", "type": r"string", "required": False},
            {"name": "costUsd", "sanitized": "costUsd", "type": r"number", "required": False},
            {"name": "co2eMetricTon", "sanitized": "co2eMetricTon", "type": r"number", "required": False},
            {"name": "kwh", "sanitized": "kwh", "type": r"number", "required": False},
        ],
    },
    {
        "model": CloudUsageByEntity,
        "name": "CloudUsageByEntity",
        "fields": [
            {"name": "id", "sanitized": "id", "type": r"string", "required": False},
            {"name": "type", "sanitized": "type", "type": r"string", "required": False},
            {"name": "serviceProvider", "sanitized": "serviceProvider", "type": r"string", "required": False},
            {"name": "serviceName", "sanitized": "serviceName", "type": r"string", "required": False},
            {"name": "serviceRegion", "sanitized": "serviceRegion", "type": r"string", "required": False},
            {"name": "serviceAccount", "sanitized": "serviceAccount", "type": r"string", "required": False},
            {"name": "name", "sanitized": "name", "type": r"string", "required": False},
            {"name": "co2eMetricTon", "sanitized": "co2eMetricTon", "type": r"number", "required": False},
        ],
    },
    {
        "model": CloudUsageTotals,
        "name": "CloudUsageTotals",
        "fields": [
            {"name": "type", "sanitized": "type", "type": r"string", "required": False},
            {"name": "co2eMetricTon", "sanitized": "co2eMetricTon", "type": r"number", "required": False},
        ],
    },
    {
        "model": CloudUsageSeries,
        "name": "CloudUsageSeries",
        "fields": [
            {"name": "id", "sanitized": "id", "type": r"string", "required": False},
            {"name": "type", "sanitized": "type", "type": r"string", "required": False},
            {"name": "timeBucket", "sanitized": "timeBucket", "type": r"string", "required": False},
            {"name": "co2eMetricTon", "sanitized": "co2eMetricTon", "type": r"number", "required": False},
        ],
    },
    {
        "model": Coefficient,
        "name": "Coefficient",
        "fields": [
            {"name": "id", "sanitized": "id", "type": r"string", "required": False},
            {"name": "type", "sanitized": "type", "type": r"string", "required": False},
            {"name": "associatedLocation", "sanitized": "associatedLocation", "type": r"object", "required": False},
            {"name": "startTime", "sanitized": "startTime", "type": r"string", "required": False},
            {"name": "co2eGramsPerKwh", "sanitized": "co2eGramsPerKwh", "type": r"number", "required": False},
            {"name": "costUsdPerKwh", "sanitized": "costUsdPerKwh", "type": r"number", "required": False},
            {"name": "costPerKwh", "sanitized": "costPerKwh", "type": r"number", "required": False},
            {"name": "currency", "sanitized": "currency", "type": r"string", "required": False},
            {"name": "generation", "sanitized": "generation", "type": r"integer", "required": False},
            {"name": "createdAt", "sanitized": "createdAt", "type": r"string", "required": False},
            {"name": "updatedAt", "sanitized": "updatedAt", "type": r"string", "required": False},
        ],
    },
    {
        "model": Ingest,
        "name": "Ingest",
        "fields": [
            {"name": "id", "sanitized": "id", "type": r"string", "required": False},
            {"name": "type", "sanitized": "type", "type": r"string", "required": False},
            {"name": "name", "sanitized": "name", "type": r"string", "required": False},
            {"name": "description", "sanitized": "description", "type": r"string", "required": False},
            {"name": "generation", "sanitized": "generation", "type": r"integer", "required": False},
            {"name": "createdAt", "sanitized": "createdAt", "type": r"string", "required": False},
            {"name": "updatedAt", "sanitized": "updatedAt", "type": r"string", "required": False},
        ],
    },
    {
        "model": DataSource,
        "name": "DataSource",
        "fields": [
            {"name": "id", "sanitized": "id", "type": r"string", "required": False},
            {"name": "type", "sanitized": "type", "type": r"string", "required": False},
            {"name": "name", "sanitized": "name", "type": r"string", "required": False},
            {"name": "provider", "sanitized": "provider", "type": r"string", "required": False},
            {"name": "lastCollectionTime", "sanitized": "lastCollectionTime", "type": r"string", "required": False},
            {"name": "firstCollectionTime", "sanitized": "firstCollectionTime", "type": r"string", "required": False},
            {"name": "generation", "sanitized": "generation", "type": r"integer", "required": False},
            {"name": "createdAt", "sanitized": "createdAt", "type": r"string", "required": False},
            {"name": "updatedAt", "sanitized": "updatedAt", "type": r"string", "required": False},
        ],
    },
    {
        "model": ForecastEnergyResponse,
        "name": "ForecastEnergyResponse",
        "fields": [
            {"name": "pastSeries", "sanitized": "pastSeries", "type": r"list[dict]", "required": False},
            {"name": "forecasts", "sanitized": "forecasts", "type": r"list[dict]", "required": False},
            {"name": "sustainabilityJourney", "sanitized": "sustainabilityJourney", "type": r"object", "required": False},
        ],
    },
    {
        "model": PaginatedResponse,
        "name": "PaginatedResponse",
        "fields": [
            {"name": "items", "sanitized": "items", "type": r"array", "required": True},
            {"name": "count", "sanitized": "count", "type": r"integer", "required": True},
            {"name": "offset", "sanitized": "offset", "type": r"integer", "required": False},
            {"name": "total", "sanitized": "total", "type": r"integer", "required": False},
        ],
    },
    {
        "model": Error,
        "name": "Error",
        "fields": [
            {"name": "httpStatusCode", "sanitized": "httpStatusCode", "type": r"integer", "required": False},
            {"name": "message", "sanitized": "message", "type": r"string", "required": False},
            {"name": "debugId", "sanitized": "debugId", "type": r"string", "required": False},
            {"name": "errorCode", "sanitized": "errorCode", "type": r"string", "required": False},
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
