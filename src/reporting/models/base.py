# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
Base models for reporting MCP server.

This module provides base Pydantic models and common types used throughout the service.
"""

from datetime import datetime
from typing import Any, Dict, List, Literal, Optional, Union  # noqa: F401
from pydantic import BaseModel as PydanticBaseModel, Field, ConfigDict


class BaseModel(PydanticBaseModel):
    """Base model with common configuration."""

    model_config = ConfigDict(
        # Enable validation on assignment
        validate_assignment=True,
        # Use enum values instead of enum names
        use_enum_values=True,
        # Allow population by field name and alias
        populate_by_name=True,
        # Validate default values
        validate_default=True,
        # Extra fields are forbidden
        extra="forbid",
    )


class BaseRequest(BaseModel):
    """Base request model with common pagination and filtering."""

    # Pagination parameters
    limit: Optional[int] = Field(default=None, ge=1, le=1000, description="Maximum number of items to return")

    offset: Optional[int] = Field(default=None, ge=0, description="Number of items to skip")

    # Filtering parameters
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

    # Response metadata
    total: Optional[int] = Field(default=None, description="Total number of items available")

    count: Optional[int] = Field(default=None, description="Number of items in this response")

    offset: Optional[int] = Field(default=None, description="Offset of the first item in this response")

    @classmethod
    def from_api_response(cls, data: Dict[str, Any]) -> "BaseResponse":
        """
        Create response model from API response data.

        Args:
            data: Raw API response data

        Returns:
            Parsed response model
        """
        # This method should be overridden in subclasses
        # to handle service-specific response parsing
        return cls(**data)


# Common types used across services
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


# SERVICE-SPECIFIC MODELS GENERATED FROM OPENAPI SCHEMAS


class error(BaseModel):
    """error model"""

    debugId: str = Field(alias="debugId", description="Unique identifier for the instance of this error")

    errorCode: str = Field(
        alias="errorCode", description="A unique machine-friendly, but human-readable identifier for the error"
    )

    httpStatusCode: int = Field(alias="httpStatusCode", description="HTTP equivalent status code")

    message: str = Field(alias="message", description="User-friendly error message")


class filterCriteria(BaseModel):
    """filterCriteria model"""

    key: Optional[str] = Field(default=None, alias="key", description="key field")

    operator: Optional[str] = Field(default=None, alias="operator", description="operator field")

    value: Optional[str] = Field(default=None, alias="value", description="value field")


class generateDocResponse(BaseModel):
    """generateDocResponse model"""

    count: int = Field(alias="count", description="Number of items returned")

    items: List[Any] = Field(alias="items", description="items field")

    offset: int = Field(alias="offset", description="Zero-based resource offset to start the response from")

    total: int = Field(
        alias="total",
        description="Total number of items in the collection that match the filter query, if one was provided in the request.",
    )


class delivery(BaseModel):
    """delivery model"""

    email: Optional[Dict[str, Any]] = Field(default=None, alias="email", description="email field")

    format: Optional[str] = Field(default=None, alias="format", description="The file type of the report.")


class enrollment(BaseModel):
    """enrollment model"""

    delivery: Optional[Dict[str, Any]] = Field(default=None, alias="delivery", description="delivery field")


class generateResponse(BaseModel):
    """generateResponse model"""

    name: Optional[str] = Field(default=None, alias="name", description="The name of the resource")

    id: Optional[str] = Field(default=None, alias="id", description="UUID of generated resource")


class queryElements(BaseModel):
    """queryElements model"""

    columns: Optional[List[Any]] = Field(
        default=None, alias="columns", description="An array containing the supported columns."
    )

    filterCriteria: Optional[List[Any]] = Field(
        default=None,
        alias="filterCriteria",
        description="An array comprising of filter names and their corresponding data types.",
    )


class reportDefinition(BaseModel):
    """reportDefinition model"""

    enrollment: Optional[Dict[str, Any]] = Field(default=None, alias="enrollment", description="enrollment field")

    queryElements: Optional[Dict[str, Any]] = Field(
        default=None, alias="queryElements", description="queryElements field"
    )


class reportDoc(BaseModel):
    """reportDoc model"""

    kind: str = Field(alias="kind", description="kind field")

    name: str = Field(alias="name", description="The name of the report.")

    type: str = Field(alias="type", description="The type of the resource.")

    columns: List[Any] = Field(alias="columns", description="columns field")

    filterCriteria: List[Any] = Field(alias="filterCriteria", description="filterCriteria field")

    id: str = Field(alias="id", description="The unique identifier of the report.")


class generateReportBody(BaseModel):
    """generateReportBody model"""

    definition: Optional[Dict[str, Any]] = Field(default=None, alias="definition", description="definition field")

    description: Optional[str] = Field(default=None, alias="description", description="A short summary of the report.")

    kind: Optional[str] = Field(default=None, alias="kind", description="kind field")

    name: Optional[str] = Field(default=None, alias="name", description="The name of the report.")

    type: Optional[str] = Field(default=None, alias="type", description="The type of the resource.")


class asyncOperationResponse(BaseModel):
    """asyncOperationResponse model"""

    id: str = Field(alias="id", description="The primary identifier for the resource.")

    results: Optional[List[Any]] = Field(
        default=None,
        alias="results",
        description="List of references to resources (other than the source resource) which were created, updated, or deleted during the operation.",
    )

    error: Optional[Dict[str, Any]] = Field(default=None, alias="error", description="error field")

    sourceResourceUri: str = Field(
        alias="sourceResourceUri",
        description="The URI reference to the resource or resource collection that initiated the operation",
    )

    progressPercent: int = Field(
        alias="progressPercent", description="Percent progress of the operation as an integer value of 0 to 100."
    )

    type: str = Field(alias="type", description="The type of the resource.")

    startedAt: Optional[str] = Field(
        default=None, alias="startedAt", description="The date and time the operation entered the `RUNNING` state."
    )

    logMessages: List[Any] = Field(
        alias="logMessages", description="List of progress update objects. This array can be empty."
    )

    state: str = Field(alias="state", description="The state of the operation.")

    endedAt: Optional[str] = Field(
        default=None,
        alias="endedAt",
        description="The date and time the operation completed in the `SUCCEEDED`, `FAILED`, or `CANCELLED` states.",
    )
