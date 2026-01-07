# (c) Copyright 2025 Hewlett Packard Enterprise Development LP
"""
Base models for workspaces MCP server.

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


class NBTenantWorkspacePaginate(BaseModel):
    """NBTenantWorkspacePaginate model"""

    items: List[Dict[str, Any]] = Field(alias="items", description="List of Workspaces")

    offset: int = Field(alias="offset", description="Specifies the offset of the returned page")

    total: int = Field(alias="total", description="The total number of items in the result set")

    count: int = Field(alias="count", description="The number of returned items")


class StandardErrorResponse(BaseModel):
    """Standard GreenLake error response model"""

    errorCode: str = Field(alias="errorCode", description="HPE GreenLake standard error code")

    httpStatusCode: int = Field(alias="httpStatusCode", description="HTTP status code")

    message: str = Field(alias="message", description="A user-friendly error message.")

    debugId: str = Field(
        alias="debugId", description="A unique identifier for this error used to help with troubleshooting."
    )


class NBCcsAddressV2(BaseModel):
    """NBCcsAddressV2 model"""

    city: Optional[str] = Field(default=None, alias="city", description="city field")

    countryCode: str = Field(alias="countryCode", description="Only country is mandatory.")

    stateOrRegion: Optional[str] = Field(default=None, alias="stateOrRegion", description="State or region")

    streetAddress: Optional[str] = Field(default=None, alias="streetAddress", description="Street address")

    streetAddressComplement: Optional[str] = Field(
        default=None, alias="streetAddressComplement", description="Apt or suite or building"
    )

    zip: Optional[str] = Field(default=None, alias="zip", description="zip field")


class NBCcsAddress(BaseModel):
    """NBCcsAddress model"""

    city: Optional[str] = Field(default=None, alias="city", description="city field")

    countryCode: Optional[str] = Field(default=None, alias="countryCode", description="Country code")

    stateOrRegion: Optional[str] = Field(default=None, alias="stateOrRegion", description="State or region")

    streetAddress: Optional[str] = Field(default=None, alias="streetAddress", description="Street address")

    streetAddressComplement: Optional[str] = Field(
        default=None, alias="streetAddressComplement", description="Apt or suite or building"
    )

    zip: Optional[str] = Field(default=None, alias="zip", description="zip field")


class NBContactWorkspace(BaseModel):
    """NBContactWorkspace model"""

    resourceUri: Optional[str] = Field(default=None, alias="resourceUri", description="Full path of the resource")

    address: Optional[str] = Field(default=None, alias="address", description="Company address.")

    email: Optional[str] = Field(
        default=None, alias="email", description="The primary email address associated with the workspace."
    )

    phoneNumber: Optional[str] = Field(
        default=None, alias="phoneNumber", description="The phone number associated with this workspace."
    )


class CountryCode(BaseModel):
    """An enumeration."""


class Message(BaseModel):
    """Message model"""

    message: str = Field(alias="message", description="Message")


class NBBasicTenant(BaseModel):
    """NBBasicTenant model"""

    type: str = Field(alias="type", description="Type of data")

    id: str = Field(alias="id", description="Resource unique identification")

    updatedAt: Optional[str] = Field(
        default=None, alias="updatedAt", description="The time the resource was last updated."
    )

    resourceUri: Optional[str] = Field(default=None, alias="resourceUri", description="Full path of the resource")

    workspaceName: str = Field(alias="workspaceName", description="Company name of the workspace.")

    generation: Optional[int] = Field(default=None, alias="generation", description="Resource history of updates")

    createdAt: Optional[str] = Field(default=None, alias="createdAt", description="The time the resource was created.")

    createdBy: Optional[str] = Field(
        default=None, alias="createdBy", description="Email address of the user that created the account."
    )

    inventoryOwnership: Optional[str] = Field(
        default=None, alias="inventoryOwnership", description="Devices and Subscriptions Ownership for this tenant."
    )


class NBContactTenant(BaseModel):
    """NBContactTenant model"""

    resourceUri: Optional[str] = Field(default=None, alias="resourceUri", description="Full path of the resource")

    workspaceName: str = Field(alias="workspaceName", description="Name of the tenant.")

    address: Optional[str] = Field(default=None, alias="address", description="Company Address.")

    description: Optional[str] = Field(default=None, alias="description", description="A description of the tenant.")

    email: Optional[str] = Field(
        default=None, alias="email", description="The primary email address associated with the workspace."
    )

    inventoryOwnership: Optional[str] = Field(
        default=None,
        alias="inventoryOwnership",
        description='Devices and Subscriptions Ownership for this tenant. If not specified, the tenant is created with the default value of "MSP_OWNED_INVENTORY".',
    )

    phoneNumber: Optional[str] = Field(
        default=None, alias="phoneNumber", description="The phone number associated with this workspace."
    )


class NBTenantInventoryOwnership(BaseModel):
    """An enumeration."""


class NBBasicWorkspace(BaseModel):
    """NBBasicWorkspace model"""

    generation: Optional[int] = Field(default=None, alias="generation", description="Resource history of updates")

    id: str = Field(alias="id", description="Resource unique identification")

    resourceUri: Optional[str] = Field(default=None, alias="resourceUri", description="Full path of the resource")

    type: str = Field(alias="type", description="Type of data")

    updatedAt: Optional[str] = Field(
        default=None, alias="updatedAt", description="The time the resource was last updated."
    )

    workspaceName: str = Field(alias="workspaceName", description="Company name of the workspace.")

    createdAt: Optional[str] = Field(default=None, alias="createdAt", description="The time the resource was created.")

    createdBy: Optional[str] = Field(
        default=None, alias="createdBy", description="Email address of the user that created the account."
    )
