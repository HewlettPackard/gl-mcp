# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
Base models for devices MCP server.

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


class DevicesPostRequest(BaseModel):
    """DevicesPostRequest model"""

    network: list[Any] = Field(alias="network", description="network field")

    storage: list[Any] = Field(alias="storage", description="storage field")

    compute: list[Any] = Field(alias="compute", description="compute field")


class DevicesPostRequestV2Beta1(BaseModel):
    """DevicesPostRequestV2Beta1 model"""

    deviceType: str = Field(alias="deviceType", description="The type of device.")

    location: Optional[dict[str, Any]] = Field(
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

    serialNumber: str = Field(alias="serialNumber", description="The serial number of the device.")

    tags: Optional[dict[str, Any]] = Field(default=None, alias="tags", description="tags field")


class BadRequestErrorDetail(BaseModel):
    """BadRequestErrorDetail model"""

    issues: list[Any] = Field(alias="issues", description="An array of request issues.")

    type: str = Field(alias="type", description="The type of error details.")


class GeneralErrorDetail(BaseModel):
    """GeneralErrorDetail model"""

    metadata: dict[str, Any] = Field(alias="metadata", description="Additional key pairs.")

    source: str = Field(alias="source", description="The source of the error.")

    type: str = Field(alias="type", description="The type of error.")


class RequestCompute(BaseModel):
    """RequestCompute model"""

    tags: Optional[dict[str, Any]] = Field(default=None, alias="tags", description="tags field")

    partNumber: str = Field(alias="partNumber", description="Identifier of a product component or part.")

    serialNumber: str = Field(alias="serialNumber", description="The serial number of the device.")


class ResponseLocation(BaseModel):
    """ResponseLocation model"""

    resourceUri: str = Field(alias="resourceUri", description="URI to the location of the device")

    id: str = Field(alias="id", description="Identifier of the location of the device")


class ResponseSubscription(BaseModel):
    """ResponseSubscription model"""

    resourceUri: str = Field(alias="resourceUri", description="URI to the the subscription")

    id: str = Field(alias="id", description="Unique identifier of the subscription assigned to the device")


class ErrorIssue(BaseModel):
    """ErrorIssue model"""

    source: Optional[str] = Field(default=None, alias="source", description="The part of the request with an issue.")

    subject: Optional[str] = Field(default=None, alias="subject", description="The issue key.")

    description: Optional[str] = Field(default=None, alias="description", description="An explanation of the issue.")


class HpeGreenLakeBadRequestError(BaseModel):
    """HpeGreenLakeBadRequestError model"""

    debugId: str = Field(alias="debugId", description="Unique identifier for the instance of this error")

    errorCode: str = Field(alias="errorCode", description="Unique machine-friendly identifier for the error")

    httpStatusCode: int = Field(alias="httpStatusCode", description="HTTP equivalent status code")

    message: str = Field(
        alias="message", description="A unique machine-friendly, but human-readable identifier for the error"
    )

    badRequestErrorDetails: Optional[list[Any]] = Field(
        default=None, alias="badRequestErrorDetails", description="badRequestErrorDetails field"
    )


class HpeGreenLakeGeneralError(BaseModel):
    """HpeGreenLakeGeneralError model"""

    generalErrorDetails: Optional[list[Any]] = Field(
        default=None, alias="generalErrorDetails", description="generalErrorDetails field"
    )

    httpStatusCode: int = Field(alias="httpStatusCode", description="HTTP equivalent status code")

    message: str = Field(
        alias="message", description="A unique machine-friendly, but human-readable identifier for the error"
    )

    debugId: str = Field(alias="debugId", description="Unique identifier for the instance of this error")

    errorCode: str = Field(alias="errorCode", description="Unique machine-friendly identifier for the error")


class DevicesGetResponse(BaseModel):
    """DevicesGetResponse model"""

    count: int = Field(alias="count", description="Number of items returned")

    items: list[Any] = Field(alias="items", description="items field")

    offset: Optional[int] = Field(default=None, alias="offset", description="Zero-based resource offset")

    total: Optional[int] = Field(
        default=None,
        alias="total",
        description="Total number of items in the collection that match the filter query, if one was provided in the request",
    )


class RequestNetwork(BaseModel):
    """RequestNetwork model"""

    macAddress: str = Field(alias="macAddress", description="The media access control (MAC) address of the device.")

    serialNumber: str = Field(alias="serialNumber", description="The serial number of the device.")

    tags: Optional[dict[str, Any]] = Field(default=None, alias="tags", description="tags field")


class ServerErrorDetail(BaseModel):
    """ServerErrorDetail model"""

    retryAfterSeconds: int = Field(alias="retryAfterSeconds", description="retryAfterSeconds field")

    type: str = Field(alias="type", description="type field")


class AsyncOperationResource(BaseModel):
    """AsyncOperationResource model"""

    resultType: Optional[str] = Field(
        default=None,
        alias="resultType",
        description="Relates individual devices to a result type. A result type declares if an operation was successful or unsuccessful.",
    )

    suggestedPollingIntervalSeconds: Optional[int] = Field(
        default=None,
        alias="suggestedPollingIntervalSeconds",
        description="The suggested time to wait (in minutes) before calling the operation again.",
    )

    timeoutMinutes: Optional[int] = Field(
        default=None, alias="timeoutMinutes", description="The number of minutes it took for the operation to time out."
    )

    result: Optional[dict[str, Any]] = Field(
        default=None,
        alias="result",
        description="An array that provides information on successful or unsuccessful operations.",
    )

    status: Optional[str] = Field(
        default=None, alias="status", description="The current status of an asynchronous operation."
    )

    progressPercent: Optional[int] = Field(
        default=None,
        alias="progressPercent",
        description="A number that indicates how close to completion the asynchronous operation is.",
    )

    type: str = Field(alias="type", description="The type of the resource")

    endedAt: Optional[str] = Field(
        default=None, alias="endedAt", description="Date and time the asynchronous operation ended in UTC format."
    )

    startedAt: Optional[str] = Field(
        default=None, alias="startedAt", description="Date and time the asynchronous operation began in UTC format."
    )

    id: str = Field(alias="id", description="The unique identifier of the device.")


class HpeGreenLakeServerError(BaseModel):
    """HpeGreenLakeServerError model"""

    errorCode: str = Field(alias="errorCode", description="Unique machine-friendly identifier for the error")

    httpStatusCode: int = Field(alias="httpStatusCode", description="HTTP equivalent status code")

    message: str = Field(
        alias="message", description="A unique machine-friendly, but human-readable identifier for the error"
    )

    serverErrorDetails: Optional[list[Any]] = Field(
        default=None, alias="serverErrorDetails", description="serverErrorDetails field"
    )

    debugId: str = Field(alias="debugId", description="Unique identifier for the instance of this error")


class RequestApplication(BaseModel):
    """RequestApplication model"""

    id: str = Field(alias="id", description="The unique identifier of the application.")


class PatchDevicesRequestV2(BaseModel):
    """PatchDevicesRequestV2 model"""

    application: Optional[dict[str, Any]] = Field(default=None, alias="application", description="application field")

    archived: Optional[bool] = Field(default=None, alias="archived", description="archived field")

    region: Optional[str] = Field(
        default=None, alias="region", description="The region of the application the device is provisioned in."
    )

    subscription: Optional[list[Any]] = Field(default=None, alias="subscription", description="subscription field")

    tags: Optional[dict[str, Any]] = Field(
        default=None,
        alias="tags",
        description="Provide a map of `tags` to create or delete for the given `DeviceID` (or multiple `DeviceID`'s). Tags are saved with the character casing preserved (uppercase, lowercase, mixed, and so on). For example, adding a new tag with the key `Location` will fail if the Device already has a tag with the key `LOCATION` as they are considered the same key. Tag keys and tag values can comprise letters, numbers, spaces (represented in UTF-8), and only the characters: `_`, `.`, `:`, `=`, `+`, `-`, and  `@`. **NOTE:** Do not store sensitive data, such as personally identifiable information, in tags.",
    )

    tenantWorkspaceId: Optional[str] = Field(
        default=None, alias="tenantWorkspaceId", description="The platform customer ID of the tenant."
    )


class AsyncResponse(BaseModel):
    """AsyncResponse model"""

    code: int = Field(alias="code", description="Three digit HTTP status code.")

    status: str = Field(alias="status", description="Three digit HTTPS status code and message.")

    transactionId: str = Field(alias="transactionId", description="The unique identifier of the transaction.")


class PatchDevicesRequest(BaseModel):
    """PatchDevicesRequest model"""

    region: Optional[str] = Field(
        default=None, alias="region", description="The region of the application the device is provisioned in."
    )

    subscription: Optional[list[Any]] = Field(default=None, alias="subscription", description="subscription field")

    tenantPlatformCustomerId: Optional[str] = Field(
        default=None, alias="tenantPlatformCustomerId", description="The platform customer ID of the tenant."
    )

    application: Optional[dict[str, Any]] = Field(default=None, alias="application", description="application field")


class RequestStorage(BaseModel):
    """RequestStorage model"""

    serialNumber: str = Field(alias="serialNumber", description="The serial number of the device.")

    tags: Optional[dict[str, Any]] = Field(default=None, alias="tags", description="tags field")

    partNumber: str = Field(alias="partNumber", description="The part number of the device.")


class RequestSubscription(BaseModel):
    """RequestSubscription model"""

    id: str = Field(alias="id", description="The unique identifier of the subscription.")


class ResponseApplication(BaseModel):
    """ResponseApplication model"""

    id: str = Field(alias="id", description="Identifier of the application provisioned on the device")

    resourceUri: str = Field(alias="resourceUri", description="URI to the application")


class DeviceDetail(BaseModel):
    """DeviceDetail model"""

    type: str = Field(alias="type", description="The type of the resource.")

    subscription: Optional[list[Any]] = Field(default=None, alias="subscription", description="subscription field")

    serialNumber: str = Field(alias="serialNumber", description="The serial number of the device.")

    warranty: Optional[dict[str, Any]] = Field(
        default=None, alias="warranty", description="The warranty information for the device."
    )

    deviceType: Optional[str] = Field(
        default=None, alias="deviceType", description="The category (type) the device belongs to."
    )

    tags: Optional[dict[str, Any]] = Field(default=None, alias="tags", description="tags field")

    tenantWorkspaceId: Optional[str] = Field(
        default=None,
        alias="tenantWorkspaceId",
        description="The unique identifier of the tenant workspace belonging to an MSP. This field is populated only for MSP-owned inventory tenants (the MSP owns the devices and subscriptions and also manages the workspace on behalf of their customers).",
    )

    model: Optional[str] = Field(default=None, alias="model", description="Hardware model of the device")

    assignedState: Optional[str] = Field(
        default=None,
        alias="assignedState",
        description="The current assignment state of the device.\n- `ASSIGNED_TO_ACTIVATE_CONFIG`—The device was moved to the custom activate configuration.\n- `ASSIGNED_TO_DEDICATED_PLATFORM`—The device is used in a dedicated platform workspace.\n- `ASSIGNED_TO_SERVICE`—The device is assigned to a service.\n- `UNASSIGNED`—The device is available for service provisioning.\n",
    )

    dedicatedPlatformWorkspace: Optional[dict[str, Any]] = Field(
        default=None, alias="dedicatedPlatformWorkspace", description="dedicatedPlatformWorkspace field"
    )

    secondaryName: Optional[str] = Field(
        default=None, alias="secondaryName", description="Secondary hostname of the device"
    )

    createdAt: Optional[str] = Field(
        default=None, alias="createdAt", description="Date and time the device was created in UTC."
    )

    location: Optional[dict[str, Any]] = Field(default=None, alias="location", description="location field")

    partNumber: str = Field(alias="partNumber", description="Identifier of the a device component or part.")

    macAddress: Optional[str] = Field(
        default=None, alias="macAddress", description="The media access control (MAC) address of the device"
    )

    updatedAt: Optional[str] = Field(
        default=None, alias="updatedAt", description="Date and time the device was last updated in UTC."
    )

    region: Optional[str] = Field(
        default=None, alias="region", description="The region of the application the device is provisioned in"
    )

    application: Optional[dict[str, Any]] = Field(default=None, alias="application", description="application field")

    id: str = Field(alias="id", description="The unique identifier of the device.")

    deviceName: Optional[str] = Field(default=None, alias="deviceName", description="Hostname of the device")

    archived: Optional[bool] = Field(
        default=None,
        alias="archived",
        description="A boolean that indicates whether the device has been archived or not. Archived devices are no longer in service.",
    )


class ResponseDedicatedPlatform(BaseModel):
    """ResponseDedicatedPlatform model"""

    id: str = Field(alias="id", description="Unique identifier of the dedicated platform workspace")


class ResponseSupportLevel(BaseModel):
    """The support levels are ranked to differentiate and display the support provided to customers."""

    serviceLevelRank: Optional[int] = Field(
        default=None,
        alias="serviceLevelRank",
        description="The rank of the support level. The lower the rank, the better the level.",
    )

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


class ResponseWarranty(BaseModel):
    """The warranty information for the device."""

    supportLevels: Optional[list[Any]] = Field(default=None, alias="supportLevels", description="supportLevels field")

    country: Optional[str] = Field(default=None, alias="country", description="country field")

    currentSupportLevel: Optional[dict[str, Any]] = Field(
        default=None,
        alias="currentSupportLevel",
        description="The support levels are ranked to differentiate and display the support provided to customers.",
    )
