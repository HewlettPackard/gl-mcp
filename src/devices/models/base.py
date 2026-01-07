# (c) Copyright 2025 Hewlett Packard Enterprise Development LP
"""
Base models for devices MCP server.

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


class PatchDevicesRequestV2(BaseModel):
    """PatchDevicesRequestV2 model"""

    tags: Optional[Dict[str, Any]] = Field(
        default=None,
        alias="tags",
        description="Provide a map of `tags` to create or delete for the given `DeviceID` (or multiple `DeviceID`'s). Tags are saved with the character casing preserved (uppercase, lowercase, mixed, and so on). For example, adding a new tag with the key `Location` will fail if the Device already has a tag with the key `LOCATION` as they are considered the same key. Tag keys and tag values can comprise letters, numbers, spaces (represented in UTF-8), and only the characters: `_`, `.`, `:`, `=`, `+`, `-`, and  `@`. **NOTE:** Do not store sensitive data, such as personally identifiable information, in tags.",
    )

    tenantWorkspaceId: Optional[str] = Field(
        default=None, alias="tenantWorkspaceId", description="The platform customer ID of the tenant."
    )

    application: Optional[Dict[str, Any]] = Field(default=None, alias="application", description="application field")

    archived: Optional[bool] = Field(default=None, alias="archived", description="archived field")

    region: Optional[str] = Field(
        default=None, alias="region", description="The region of the application the device is provisioned in."
    )

    subscription: Optional[List[Dict[str, Any]]] = Field(
        default=None, alias="subscription", description="subscription field"
    )


class RequestSubscription(BaseModel):
    """RequestSubscription model"""

    id: str = Field(alias="id", description="The unique identifier of the subscription.")


class DevicesGetResponse(BaseModel):
    """DevicesGetResponse model"""

    count: int = Field(alias="count", description="Number of items returned")

    items: List[Dict[str, Any]] = Field(alias="items", description="items field")

    offset: Optional[int] = Field(default=None, alias="offset", description="Zero-based resource offset")

    total: Optional[int] = Field(
        default=None,
        alias="total",
        description="Total number of items in the collection that match the filter query, if one was provided in the request",
    )


class ResponseApplication(BaseModel):
    """ResponseApplication model"""

    id: str = Field(alias="id", description="Identifier of the application provisioned on the device")

    resourceUri: str = Field(alias="resourceUri", description="URI to the application")


class RequestCompute(BaseModel):
    """RequestCompute model"""

    partNumber: str = Field(alias="partNumber", description="Identifier of a product component or part.")

    serialNumber: str = Field(alias="serialNumber", description="The serial number of the device.")

    tags: Optional[Dict[str, Any]] = Field(default=None, alias="tags", description="tags field")


class AsyncResponse(BaseModel):
    """AsyncResponse model"""

    code: int = Field(alias="code", description="Three digit HTTP status code.")

    status: str = Field(alias="status", description="Three digit HTTPS status code and message.")

    transactionId: str = Field(alias="transactionId", description="The unique identifier of the transaction.")


class ResponseLocation(BaseModel):
    """ResponseLocation model"""

    id: str = Field(alias="id", description="Identifier of the location of the device")

    resourceUri: str = Field(alias="resourceUri", description="URI to the location of the device")


class ResponseSubscription(BaseModel):
    """ResponseSubscription model"""

    id: str = Field(alias="id", description="Unique identifier of the subscription assigned to the device")

    resourceUri: str = Field(alias="resourceUri", description="URI to the the subscription")


class RequestNetwork(BaseModel):
    """RequestNetwork model"""

    macAddress: str = Field(alias="macAddress", description="The media access control (MAC) address of the device.")

    serialNumber: str = Field(alias="serialNumber", description="The serial number of the device.")

    tags: Optional[Dict[str, Any]] = Field(default=None, alias="tags", description="tags field")


class GeneralErrorDetail(BaseModel):
    """GeneralErrorDetail model"""

    type: str = Field(alias="type", description="The type of error.")

    metadata: Dict[str, Any] = Field(alias="metadata", description="Additional key pairs.")

    source: str = Field(alias="source", description="The source of the error.")


class AsyncOperationResource(BaseModel):
    """AsyncOperationResource model"""

    progressPercent: Optional[int] = Field(
        default=None,
        alias="progressPercent",
        description="A number that indicates how close to completion the asynchronous operation is.",
    )

    endedAt: Optional[str] = Field(
        default=None, alias="endedAt", description="Date and time the asynchronous operation ended in UTC format."
    )

    id: str = Field(alias="id", description="The unique identifier of the device.")

    result: Optional[Dict[str, Any]] = Field(
        default=None,
        alias="result",
        description="An array that provides information on successful or unsuccessful operations.",
    )

    suggestedPollingIntervalSeconds: Optional[int] = Field(
        default=None,
        alias="suggestedPollingIntervalSeconds",
        description="The suggested time to wait (in minutes) before calling the operation again.",
    )

    timeoutMinutes: Optional[int] = Field(
        default=None, alias="timeoutMinutes", description="The number of minutes it took for the operation to time out."
    )

    resultType: Optional[str] = Field(
        default=None,
        alias="resultType",
        description="Relates individual devices to a result type. A result type declares if an operation was successful or unsuccessful.",
    )

    startedAt: Optional[str] = Field(
        default=None, alias="startedAt", description="Date and time the asynchronous operation began in UTC format."
    )

    status: Optional[str] = Field(
        default=None, alias="status", description="The current status of an asynchronous operation."
    )

    type: str = Field(alias="type", description="The type of the resource")


class DevicesPostRequest(BaseModel):
    """DevicesPostRequest model"""

    network: List[Dict[str, Any]] = Field(alias="network", description="network field")

    storage: List[Dict[str, Any]] = Field(alias="storage", description="storage field")

    compute: List[Dict[str, Any]] = Field(alias="compute", description="compute field")


class HpeGreenLakeGeneralError(BaseModel):
    """HpeGreenLakeGeneralError model"""

    debugId: str = Field(alias="debugId", description="Unique identifier for the instance of this error")

    errorCode: str = Field(alias="errorCode", description="Unique machine-friendly identifier for the error")

    generalErrorDetails: Optional[List[Dict[str, Any]]] = Field(
        default=None, alias="generalErrorDetails", description="generalErrorDetails field"
    )

    httpStatusCode: int = Field(alias="httpStatusCode", description="HTTP equivalent status code")

    message: str = Field(
        alias="message", description="A unique machine-friendly, but human-readable identifier for the error"
    )


class HpeGreenLakeServerError(BaseModel):
    """HpeGreenLakeServerError model"""

    debugId: str = Field(alias="debugId", description="Unique identifier for the instance of this error")

    errorCode: str = Field(alias="errorCode", description="Unique machine-friendly identifier for the error")

    httpStatusCode: int = Field(alias="httpStatusCode", description="HTTP equivalent status code")

    message: str = Field(
        alias="message", description="A unique machine-friendly, but human-readable identifier for the error"
    )

    serverErrorDetails: Optional[List[Dict[str, Any]]] = Field(
        default=None, alias="serverErrorDetails", description="serverErrorDetails field"
    )


class ErrorIssue(BaseModel):
    """ErrorIssue model"""

    subject: Optional[str] = Field(default=None, alias="subject", description="The issue key.")

    description: Optional[str] = Field(default=None, alias="description", description="An explanation of the issue.")

    source: Optional[str] = Field(default=None, alias="source", description="The part of the request with an issue.")


class RequestStorage(BaseModel):
    """RequestStorage model"""

    partNumber: str = Field(alias="partNumber", description="The part number of the device.")

    serialNumber: str = Field(alias="serialNumber", description="The serial number of the device.")

    tags: Optional[Dict[str, Any]] = Field(default=None, alias="tags", description="tags field")


class RequestApplication(BaseModel):
    """RequestApplication model"""

    id: str = Field(alias="id", description="The unique identifier of the application.")


class ResponseSupportLevel(BaseModel):
    """The support levels are ranked to differentiate and display the support provided to customers."""

    startDate: Optional[int] = Field(
        default=None, alias="startDate", description="The start date of the support level."
    )

    contractLevel: Optional[str] = Field(
        default=None,
        alias="contractLevel",
        description="Sub-categorizes the support level for display to the customer.",
    )

    contractLevelRank: Optional[int] = Field(
        default=None,
        alias="contractLevelRank",
        description="The rank of the contract level within the support level. The lower the rank, the better the level.",
    )

    endDate: Optional[int] = Field(default=None, alias="endDate", description="The end date of the support level.")

    serviceLevel: Optional[str] = Field(
        default=None, alias="serviceLevel", description="The value used for differentiation."
    )

    serviceLevelRank: Optional[int] = Field(
        default=None,
        alias="serviceLevelRank",
        description="The rank of the support level. The lower the rank, the better the level.",
    )


class BadRequestErrorDetail(BaseModel):
    """BadRequestErrorDetail model"""

    issues: List[Dict[str, Any]] = Field(alias="issues", description="An array of request issues.")

    type: str = Field(alias="type", description="The type of error details.")


class ServerErrorDetail(BaseModel):
    """ServerErrorDetail model"""

    type: str = Field(alias="type", description="type field")

    retryAfterSeconds: int = Field(alias="retryAfterSeconds", description="retryAfterSeconds field")


class DeviceDetail(BaseModel):
    """DeviceDetail model"""

    assignedState: Optional[str] = Field(
        default=None,
        alias="assignedState",
        description="The current assignment state of the device.\n- `ASSIGNED_TO_ACTIVATE_CONFIG`—The device was moved to the custom activate configuration.\n- `ASSIGNED_TO_DEDICATED_PLATFORM`—The device is used in a dedicated platform workspace.\n- `ASSIGNED_TO_SERVICE`—The device is assigned to a service.\n- `UNASSIGNED`—The device is available for service provisioning.\n",
    )

    createdAt: Optional[str] = Field(
        default=None, alias="createdAt", description="Date and time the device was created in UTC."
    )

    deviceType: Optional[str] = Field(
        default=None, alias="deviceType", description="The category (type) the device belongs to."
    )

    id: str = Field(alias="id", description="The unique identifier of the device.")

    partNumber: str = Field(alias="partNumber", description="Identifier of the a device component or part.")

    warranty: Optional[Dict[str, Any]] = Field(
        default=None, alias="warranty", description="The warranty information for the device."
    )

    location: Optional[Dict[str, Any]] = Field(default=None, alias="location", description="location field")

    macAddress: Optional[str] = Field(
        default=None, alias="macAddress", description="The media access control (MAC) address of the device"
    )

    archived: Optional[bool] = Field(
        default=None,
        alias="archived",
        description="A boolean that indicates whether the device has been archived or not. Archived devices are no longer in service.",
    )

    tenantWorkspaceId: Optional[str] = Field(
        default=None,
        alias="tenantWorkspaceId",
        description="The unique identifier of the tenant workspace belonging to an MSP. This field is populated only for MSP-owned inventory tenants (the MSP owns the devices and subscriptions and also manages the workspace on behalf of their customers).",
    )

    serialNumber: str = Field(alias="serialNumber", description="The serial number of the device.")

    application: Optional[Dict[str, Any]] = Field(default=None, alias="application", description="application field")

    tags: Optional[Dict[str, Any]] = Field(default=None, alias="tags", description="tags field")

    type: str = Field(alias="type", description="The type of the resource.")

    region: Optional[str] = Field(
        default=None, alias="region", description="The region of the application the device is provisioned in"
    )

    updatedAt: Optional[str] = Field(
        default=None, alias="updatedAt", description="Date and time the device was last updated in UTC."
    )

    subscription: Optional[List[Dict[str, Any]]] = Field(
        default=None, alias="subscription", description="subscription field"
    )

    model: Optional[str] = Field(default=None, alias="model", description="Hardware model of the device")


class ResponseWarranty(BaseModel):
    """The warranty information for the device."""

    country: Optional[str] = Field(default=None, alias="country", description="country field")

    currentSupportLevel: Optional[Dict[str, Any]] = Field(
        default=None,
        alias="currentSupportLevel",
        description="The support levels are ranked to differentiate and display the support provided to customers.",
    )

    supportLevels: Optional[List[Dict[str, Any]]] = Field(
        default=None, alias="supportLevels", description="supportLevels field"
    )


class DevicesPostRequestV2Beta1(BaseModel):
    """DevicesPostRequestV2Beta1 model"""

    serialNumber: str = Field(alias="serialNumber", description="The serial number of the device.")

    tags: Optional[Dict[str, Any]] = Field(default=None, alias="tags", description="tags field")

    deviceType: str = Field(alias="deviceType", description="The type of device.")

    location: Optional[Dict[str, Any]] = Field(
        default=None, alias="location", description="The location ID of the device."
    )

    macAddress: Optional[str] = Field(
        default=None,
        alias="macAddress",
        description="The media access control (MAC) address of the device. This is required for claiming `NETWORK` devices.",
    )

    partNumber: Optional[str] = Field(
        default=None,
        alias="partNumber",
        description="The part number of the device. This is required for claiming `COMPUTE` or `STORAGE` devices.",
    )


class HpeGreenLakeBadRequestError(BaseModel):
    """HpeGreenLakeBadRequestError model"""

    httpStatusCode: int = Field(alias="httpStatusCode", description="HTTP equivalent status code")

    message: str = Field(
        alias="message", description="A unique machine-friendly, but human-readable identifier for the error"
    )

    badRequestErrorDetails: Optional[List[Dict[str, Any]]] = Field(
        default=None, alias="badRequestErrorDetails", description="badRequestErrorDetails field"
    )

    debugId: str = Field(alias="debugId", description="Unique identifier for the instance of this error")

    errorCode: str = Field(alias="errorCode", description="Unique machine-friendly identifier for the error")


class PatchDevicesRequest(BaseModel):
    """PatchDevicesRequest model"""

    subscription: Optional[List[Dict[str, Any]]] = Field(
        default=None, alias="subscription", description="subscription field"
    )

    tenantPlatformCustomerId: Optional[str] = Field(
        default=None, alias="tenantPlatformCustomerId", description="The platform customer ID of the tenant."
    )

    application: Optional[Dict[str, Any]] = Field(default=None, alias="application", description="application field")

    region: Optional[str] = Field(
        default=None, alias="region", description="The region of the application the device is provisioned in."
    )
