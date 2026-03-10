# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
Base models for sustainability MCP server.

This module provides base Pydantic models and common types used throughout the service.
"""

from datetime import datetime
from typing import Any, Dict, List, Optional, Literal, Union  # noqa: F401
from pydantic import BaseModel as PydanticBaseModel, Field, ConfigDict


class BaseModel(PydanticBaseModel):
    """Base model with common configuration."""

    model_config = ConfigDict(
        validate_assignment=True,
        use_enum_values=True,
        populate_by_name=True,
        validate_default=True,
        extra="forbid",
    )


class BaseRequest(BaseModel):
    """Base request model with common pagination and filtering."""

    limit: Optional[int] = Field(default=None, ge=1, le=1000, description="Maximum number of items to return")
    offset: Optional[int] = Field(default=None, ge=0, description="Number of items to skip")
    filter_expression: Optional[str] = Field(default=None, description="OData-style filter expression")

    def to_query_params(self) -> Dict[str, str]:
        """Convert request to query parameters."""
        params = {}
        if self.limit is not None:
            params["limit"] = str(self.limit)
        if self.offset is not None:
            params["offset"] = str(self.offset)
        if self.filter_expression:
            params["filter"] = self.filter_expression
        return params


class BaseResponse(BaseModel):
    """Base response model with common metadata."""

    total: Optional[int] = Field(default=None, description="Total number of items available")
    count: Optional[int] = Field(default=None, description="Number of items in this response")
    offset: Optional[int] = Field(default=None, description="Offset of the first item in this response")

    @classmethod
    def from_api_response(cls, data: Dict[str, Any]) -> "BaseResponse":
        """Create response model from API response data."""
        return cls(**data)


class ErrorDetail(BaseModel):
    """Error detail model."""

    code: str = Field(description="Error code")
    message: str = Field(description="Error message")
    details: Optional[Dict[str, Any]] = Field(default=None, description="Additional error details")


class ResourceMetadata(BaseModel):
    """Common resource metadata."""

    created_at: Optional[datetime] = Field(default=None, description="Resource creation timestamp")
    updated_at: Optional[datetime] = Field(default=None, description="Resource last update timestamp")
    created_by: Optional[str] = Field(default=None, description="User who created the resource")
    updated_by: Optional[str] = Field(default=None, description="User who last updated the resource")


# SERVICE-SPECIFIC MODELS FOR SUSTAINABILITY INSIGHT CENTER


class UsageByEntity(BaseModel):
    """Energy usage data for a single entity."""

    id: Optional[str] = Field(default=None, alias="id", description="Entity identifier")
    type: Optional[str] = Field(default=None, alias="type", description="Resource type")
    entityId: Optional[str] = Field(default=None, alias="entityId", description="Entity ID (e.g. serial number)")
    entityMake: Optional[str] = Field(default=None, alias="entityMake", description="Entity manufacturer")
    entityModel: Optional[str] = Field(default=None, alias="entityModel", description="Entity model name")
    entityType: Optional[str] = Field(default=None, alias="entityType", description="Entity type (e.g. COMPUTE)")
    entitySerialNum: Optional[str] = Field(default=None, alias="entitySerialNum", description="Entity serial number")
    entityProductId: Optional[str] = Field(default=None, alias="entityProductId", description="Entity product ID")
    entityManufactureTimestamp: Optional[str] = Field(
        default=None, alias="entityManufactureTimestamp", description="Manufacturing timestamp"
    )
    locationName: Optional[str] = Field(default=None, alias="locationName", description="Location name")
    locationId: Optional[str] = Field(default=None, alias="locationId", description="Location UUID")
    locationCity: Optional[str] = Field(default=None, alias="locationCity", description="Location city")
    locationState: Optional[str] = Field(default=None, alias="locationState", description="Location state/province")
    locationCountry: Optional[str] = Field(default=None, alias="locationCountry", description="Location country")
    tags: Optional[List[Dict[str, Any]]] = Field(default=None, alias="tags", description="Entity tags")
    name: Optional[str] = Field(default=None, alias="name", description="Entity name")
    cost: Optional[float] = Field(default=None, alias="cost", description="Estimated energy cost")
    costUsd: Optional[float] = Field(default=None, alias="costUsd", description="Deprecated: use cost instead")
    currency: Optional[str] = Field(default=None, alias="currency", description="Currency code")
    co2eMetricTon: Optional[float] = Field(
        default=None, alias="co2eMetricTon", description="CO2 equivalent in metric tons"
    )
    kwh: Optional[float] = Field(default=None, alias="kwh", description="Energy consumption in kWh")


class UsageTotals(BaseModel):
    """Aggregated energy usage totals."""

    type: Optional[str] = Field(default=None, alias="type", description="Resource type")
    cost: Optional[float] = Field(default=None, alias="cost", description="Estimated energy cost")
    costUsd: Optional[float] = Field(default=None, alias="costUsd", description="Deprecated: use cost instead")
    currency: Optional[str] = Field(default=None, alias="currency", description="Currency code")
    co2eMetricTon: Optional[float] = Field(
        default=None, alias="co2eMetricTon", description="CO2 equivalent in metric tons"
    )
    kwh: Optional[float] = Field(default=None, alias="kwh", description="Energy consumption in kWh")


class UsageSeries(BaseModel):
    """Energy usage time series data point."""

    id: Optional[str] = Field(default=None, alias="id", description="Time bucket identifier")
    type: Optional[str] = Field(default=None, alias="type", description="Resource type")
    timeBucket: Optional[str] = Field(default=None, alias="timeBucket", description="Time bucket timestamp")
    cost: Optional[float] = Field(default=None, alias="cost", description="Estimated energy cost")
    currency: Optional[str] = Field(default=None, alias="currency", description="Currency code")
    costUsd: Optional[float] = Field(default=None, alias="costUsd", description="Deprecated: use cost instead")
    co2eMetricTon: Optional[float] = Field(
        default=None, alias="co2eMetricTon", description="CO2 equivalent in metric tons"
    )
    kwh: Optional[float] = Field(default=None, alias="kwh", description="Energy consumption in kWh")


class CloudUsageByEntity(BaseModel):
    """Cloud sustainability data for a single entity."""

    id: Optional[str] = Field(default=None, alias="id", description="Entity identifier")
    type: Optional[str] = Field(default=None, alias="type", description="Resource type")
    serviceProvider: Optional[str] = Field(default=None, alias="serviceProvider", description="Cloud provider (e.g. aws)")
    serviceName: Optional[str] = Field(default=None, alias="serviceName", description="Cloud service name (e.g. s3)")
    serviceRegion: Optional[str] = Field(default=None, alias="serviceRegion", description="Cloud service region")
    serviceAccount: Optional[str] = Field(default=None, alias="serviceAccount", description="Cloud account ID")
    name: Optional[str] = Field(default=None, alias="name", description="Entity name")
    co2eMetricTon: Optional[float] = Field(
        default=None, alias="co2eMetricTon", description="CO2 equivalent in metric tons"
    )


class CloudUsageTotals(BaseModel):
    """Aggregated cloud sustainability totals."""

    type: Optional[str] = Field(default=None, alias="type", description="Resource type")
    co2eMetricTon: Optional[float] = Field(
        default=None, alias="co2eMetricTon", description="CO2 equivalent in metric tons"
    )


class CloudUsageSeries(BaseModel):
    """Cloud sustainability time series data point."""

    id: Optional[str] = Field(default=None, alias="id", description="Time bucket identifier")
    type: Optional[str] = Field(default=None, alias="type", description="Resource type")
    timeBucket: Optional[str] = Field(default=None, alias="timeBucket", description="Time bucket timestamp")
    co2eMetricTon: Optional[float] = Field(
        default=None, alias="co2eMetricTon", description="CO2 equivalent in metric tons"
    )


class Coefficient(BaseModel):
    """Cost and CO2 coefficient."""

    id: Optional[str] = Field(default=None, alias="id", description="Coefficient UUID")
    type: Optional[str] = Field(default=None, alias="type", description="Resource type")
    associatedLocation: Optional[Dict[str, Any]] = Field(
        default=None, alias="associatedLocation", description="Associated location details"
    )
    startTime: Optional[str] = Field(default=None, alias="startTime", description="Coefficient effective start time")
    co2eGramsPerKwh: Optional[float] = Field(
        default=None, alias="co2eGramsPerKwh", description="CO2 grams per kWh"
    )
    costUsdPerKwh: Optional[float] = Field(
        default=None, alias="costUsdPerKwh", description="Deprecated: use costPerKwh"
    )
    costPerKwh: Optional[float] = Field(default=None, alias="costPerKwh", description="Cost per kWh")
    currency: Optional[Any] = Field(default=None, alias="currency", description="Currency information")
    generation: Optional[int] = Field(default=None, alias="generation", description="Generation counter")
    createdAt: Optional[str] = Field(default=None, alias="createdAt", description="Creation timestamp")
    updatedAt: Optional[str] = Field(default=None, alias="updatedAt", description="Last update timestamp")


class Ingest(BaseModel):
    """Metadata for uploaded device measurements."""

    id: Optional[str] = Field(default=None, alias="id", description="Ingest UUID")
    type: Optional[str] = Field(default=None, alias="type", description="Resource type")
    name: Optional[str] = Field(default=None, alias="name", description="Ingest name")
    description: Optional[str] = Field(default=None, alias="description", description="Ingest description")
    generation: Optional[int] = Field(default=None, alias="generation", description="Generation counter")
    createdAt: Optional[str] = Field(default=None, alias="createdAt", description="Creation timestamp")
    updatedAt: Optional[str] = Field(default=None, alias="updatedAt", description="Last update timestamp")


class DataSource(BaseModel):
    """Data source information."""

    id: Optional[str] = Field(default=None, alias="id", description="Data source UUID")
    type: Optional[str] = Field(default=None, alias="type", description="Resource type")
    name: Optional[str] = Field(default=None, alias="name", description="Data source name")
    provider: Optional[str] = Field(default=None, alias="provider", description="Data source provider")
    lastCollectionTime: Optional[str] = Field(
        default=None, alias="lastCollectionTime", description="Last data collection timestamp"
    )
    firstCollectionTime: Optional[str] = Field(
        default=None, alias="firstCollectionTime", description="First data collection timestamp"
    )
    generation: Optional[int] = Field(default=None, alias="generation", description="Generation counter")
    createdAt: Optional[str] = Field(default=None, alias="createdAt", description="Creation timestamp")
    updatedAt: Optional[str] = Field(default=None, alias="updatedAt", description="Last update timestamp")


class ForecastMetric(BaseModel):
    """Forecast metric with confidence intervals."""

    forecast: Optional[float] = Field(default=None, alias="forecast", description="Forecasted value")
    lowerBound: Optional[float] = Field(default=None, alias="lowerBound", description="Lower confidence bound")
    upperBound: Optional[float] = Field(default=None, alias="upperBound", description="Upper confidence bound")


class ForecastCostMetric(BaseModel):
    """Forecast cost metric with confidence intervals and currency unit."""

    forecast: Optional[float] = Field(default=None, alias="forecast", description="Forecasted cost value")
    lowerBound: Optional[float] = Field(default=None, alias="lowerBound", description="Lower confidence bound")
    upperBound: Optional[float] = Field(default=None, alias="upperBound", description="Upper confidence bound")
    unit: Optional[str] = Field(default=None, alias="unit", description="Currency code")


class ForecastDataPoint(BaseModel):
    """Single forecast data point."""

    startDate: Optional[str] = Field(default=None, alias="startDate", description="Forecast period start date")
    co2eMt: Optional[Dict[str, Any]] = Field(default=None, alias="co2eMt", description="CO2 forecast with bounds")
    energyKwh: Optional[Dict[str, Any]] = Field(
        default=None, alias="energyKwh", description="Energy forecast with bounds"
    )
    cost: Optional[Dict[str, Any]] = Field(default=None, alias="cost", description="Cost forecast with bounds")


class PastSeriesDataPoint(BaseModel):
    """Historical data point for forecast context."""

    startDate: Optional[str] = Field(default=None, alias="startDate", description="Period start date")
    energyKwh: Optional[float] = Field(default=None, alias="energyKwh", description="Energy consumption in kWh")
    co2eMt: Optional[float] = Field(default=None, alias="co2eMt", description="CO2 equivalent in metric tons")
    cost: Optional[Dict[str, Any]] = Field(default=None, alias="cost", description="Cost with value and unit")


class SustainabilityJourney(BaseModel):
    """Sustainability journey comparison data."""

    actual: Optional[float] = Field(default=None, alias="actual", description="Actual latest value")
    expected: Optional[float] = Field(default=None, alias="expected", description="Expected forecasted value")
    lowerBound: Optional[float] = Field(default=None, alias="lowerBound", description="Lower confidence bound")
    upperBound: Optional[float] = Field(default=None, alias="upperBound", description="Upper confidence bound")
    startDate: Optional[str] = Field(default=None, alias="startDate", description="Comparison period start date")


class ForecastEnergyResponse(BaseModel):
    """Response from the forecast energy endpoint."""

    pastSeries: Optional[List[Dict[str, Any]]] = Field(
        default=None, alias="pastSeries", description="Historical data points"
    )
    forecasts: Optional[List[Dict[str, Any]]] = Field(
        default=None, alias="forecasts", description="Forecast data points"
    )
    sustainabilityJourney: Optional[Dict[str, Any]] = Field(
        default=None, alias="sustainabilityJourney", description="Sustainability journey summary"
    )


class PaginatedResponse(BaseModel):
    """Paginated API response."""

    items: List[Any] = Field(alias="items", description="Response items")
    count: int = Field(alias="count", description="Number of returned items")
    offset: Optional[int] = Field(default=None, alias="offset", description="Current offset")
    total: Optional[int] = Field(default=None, alias="total", description="Total number of items")


class Error(BaseModel):
    """Error response model."""

    httpStatusCode: Optional[int] = Field(default=None, alias="httpStatusCode", description="HTTP status code")
    message: Optional[str] = Field(default=None, alias="message", description="Error message")
    debugId: Optional[str] = Field(default=None, alias="debugId", description="Debug identifier")
    errorCode: Optional[str] = Field(default=None, alias="errorCode", description="Machine-friendly error code")
