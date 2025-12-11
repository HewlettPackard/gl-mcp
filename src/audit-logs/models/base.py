# (c) Copyright 2025 Hewlett Packard Enterprise Development LP
"""
Base models for audit-logs MCP server.

This module provides base Pydantic models and common types used throughout the service.
"""

from datetime import datetime
from typing import Any, Dict, List, Optional, Literal, Union  # noqa: F401
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


class AuditLogDetails(BaseModel):
    """AuditLogDetails model"""

    type: str = Field(alias="type", description="resource type")

    body: List[str] = Field(alias="body", description="body field")

    header: str = Field(alias="header", description="header field")

    id: str = Field(alias="id", description="audit log id")


class AuditLogs(BaseModel):
    """AuditLogs model"""

    items: List[Dict[str, Any]] = Field(alias="items", description="items field")

    remainingRecords: Optional[bool] = Field(
        default=None,
        alias="remainingRecords",
        description="This boolean flag shows whether there are more records available",
    )

    total: int = Field(alias="total", description="Total number of items in the collection.")

    count: int = Field(alias="count", description="Number of returned items")

    offset: Optional[int] = Field(
        default=None,
        alias="offset",
        description="Specifies the offset of the returned page. Only when offset based pagination is used.",
    )


class ErrorGeneralDetails(BaseModel):
    """ErrorGeneralDetails model"""

    errorDetails: Optional[List[str]] = Field(
        default=None, alias="errorDetails", description="Additional detailed information about the error."
    )


class ErrorNotFoundDetails(BaseModel):
    """ErrorNotFoundDetails model"""

    errorDetails: Optional[List[str]] = Field(
        default=None, alias="errorDetails", description="Additional detailed information about the error."
    )


class AuditLog(BaseModel):
    """AuditLog model"""

    application: Optional[Dict[str, Any]] = Field(default=None, alias="application", description="application field")

    updatedAt: Optional[str] = Field(default=None, alias="updatedAt", description="The time the audit log was updated.")

    workspace: Optional[Dict[str, Any]] = Field(default=None, alias="workspace", description="workspace field")

    description: Optional[str] = Field(
        default=None,
        alias="description",
        description="A short description of the changes such as subscription assignment, firmware upgrade, and configuration updates.",
    )

    region: Optional[str] = Field(
        default=None, alias="region", description="The region code associated with the application."
    )

    createdAt: Optional[str] = Field(default=None, alias="createdAt", description="The time the audit log was created.")

    id: str = Field(alias="id", description="Unique audit log ID")

    category: Optional[str] = Field(default=None, alias="category", description="The category of the audit log.")

    generation: Optional[int] = Field(
        default=None, alias="generation", description="if any update happened then field count will get increased."
    )

    user: Optional[Dict[str, Any]] = Field(default=None, alias="user", description="user field")

    additionalInfo: Optional[Dict[str, Any]] = Field(
        default=None, alias="additionalInfo", description="Returns additional attributes."
    )

    hasDetails: Optional[bool] = Field(
        default=None,
        alias="hasDetails",
        description="If set to `true`, additional details are available for the audit log.",
    )

    type: str = Field(alias="type", description="Resource type")


class ErrorBadRequestDetails(BaseModel):
    """ErrorBadRequestDetails model"""

    errorDetails: Optional[List[str]] = Field(
        default=None, alias="errorDetails", description="Additional detailed information about the error."
    )


class ErrorRetryDetails(BaseModel):
    """ErrorRetryDetails model"""

    errorDetails: Optional[List[str]] = Field(
        default=None, alias="errorDetails", description="Additional detailed information about the error."
    )


class PaginatedApiResponse(BaseModel):
    """PaginatedApiResponse model"""

    count: int = Field(alias="count", description="Number of returned items")

    offset: Optional[int] = Field(
        default=None,
        alias="offset",
        description="Specifies the offset of the returned page. Only when offset based pagination is used.",
    )

    remainingRecords: Optional[bool] = Field(
        default=None,
        alias="remainingRecords",
        description="This boolean flag shows whether there are more records available",
    )

    total: int = Field(alias="total", description="Total number of items in the collection.")


class Error(BaseModel):
    """Error model"""

    message: str = Field(alias="message", description="User-friendly error message.")

    debugId: str = Field(alias="debugId", description="Unique identifier for the instance of this error.")

    errorCode: str = Field(alias="errorCode", description="Unique machine-friendly identifier for the error.")

    httpStatusCode: int = Field(alias="httpStatusCode", description="HTTP status code for the error.")
