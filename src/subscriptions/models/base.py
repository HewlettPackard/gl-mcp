# (c) Copyright 2025 Hewlett Packard Enterprise Development LP
"""
Base models for subscriptions MCP server.

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


class BadRequestErrorDetail(BaseModel):
    """BadRequestErrorDetail model"""

    type: str = Field(alias="type", description="The type of error details.")

    issues: List[Dict[str, Any]] = Field(alias="issues", description="An array of bad request issues.")


class AsyncOperationResource(BaseModel):
    """AsyncOperationResource model"""

    status: Optional[str] = Field(
        default=None, alias="status", description="The current status of the asynchronous operation."
    )

    timeoutMinutes: Optional[int] = Field(
        default=None, alias="timeoutMinutes", description="The number of minutes before the operation will time out."
    )

    result: Optional[Dict[str, Any]] = Field(
        default=None,
        alias="result",
        description="An array that provides information on successful or unsuccessful operations.",
    )

    type: str = Field(alias="type", description="The type of the resource.")

    id: str = Field(alias="id", description="The unique identifier of the asynchronous operation.")

    progressPercent: Optional[int] = Field(
        default=None, alias="progressPercent", description="Percentage completion of the asynchronous operation."
    )

    resultType: Optional[str] = Field(
        default=None,
        alias="resultType",
        description="Relates individual subscriptions to a result category that indicates successfull or unsuccessful operations",
    )

    suggestedPollingIntervalSeconds: Optional[int] = Field(
        default=None,
        alias="suggestedPollingIntervalSeconds",
        description="The suggested time to wait (in minutes) before calling the operation again.",
    )

    startedAt: Optional[str] = Field(
        default=None, alias="startedAt", description="Time the asynchronous operation started."
    )

    endedAt: Optional[str] = Field(default=None, alias="endedAt", description="Time the asynchronous operation ended.")


class AutoSubscriptionsPostRequest(BaseModel):
    """AutoSubscriptionsPostRequest model"""

    autoSubscriptionSettings: Optional[List[Dict[str, Any]]] = Field(
        default=None, alias="autoSubscriptionSettings", description="autoSubscriptionSettings field"
    )


class V1Beta1SubscriptionsGetResponse(BaseModel):
    """V1Beta1SubscriptionsGetResponse model"""

    total: Optional[int] = Field(
        default=None,
        alias="total",
        description="Total number of items in the collection that match the filter query, if one was provided in the request otherwise total number of items for a given resource.",
    )

    count: int = Field(alias="count", description="The number of items returned.")

    items: List[Dict[str, Any]] = Field(alias="items", description="items field")

    offset: Optional[int] = Field(default=None, alias="offset", description="Zero-based resource offset.")


class AutoSubscriptionSettings(BaseModel):
    """AutoSubscriptionSettings model"""

    deviceType: str = Field(alias="deviceType", description="deviceType field")

    tier: str = Field(alias="tier", description="tier field")


class HpeGreenLakeGeneralError(BaseModel):
    """HpeGreenLakeGeneralError model"""

    message: str = Field(alias="message", description="A user-friendly error message.")

    debugId: str = Field(alias="debugId", description="A unique identifier for the instance of this error.")

    errorCode: str = Field(
        alias="errorCode", description="A unique machine-friendly, but human-readable identifier for the error."
    )

    generalErrorDetails: Optional[List[Dict[str, Any]]] = Field(
        default=None, alias="generalErrorDetails", description="generalErrorDetails field"
    )

    httpStatusCode: int = Field(alias="httpStatusCode", description="The HTTP equivalent status code.")


class ErrorIssue(BaseModel):
    """ErrorIssue model"""

    subject: Optional[str] = Field(default=None, alias="subject", description="The specific issue key.")

    description: Optional[str] = Field(
        default=None, alias="description", description="A brief explanation of the error."
    )

    source: Optional[str] = Field(default=None, alias="source", description="The source of the error.")


class GeneralErrorDetail(BaseModel):
    """GeneralErrorDetail model"""

    type: str = Field(alias="type", description="The type of error.")

    metadata: Dict[str, Any] = Field(alias="metadata", description="Additional key pairs.")

    source: str = Field(alias="source", description="The source of the error.")


class HpeGreenLakeServerError(BaseModel):
    """HpeGreenLakeServerError model"""

    errorCode: str = Field(
        alias="errorCode", description="A unique machine-friendly, but human-readable identifier for the error."
    )

    httpStatusCode: int = Field(alias="httpStatusCode", description="The HTTP equivalent status code.")

    message: str = Field(alias="message", description="A user-friendly error message.")

    serverErrorDetails: Optional[List[Dict[str, Any]]] = Field(
        default=None, alias="serverErrorDetails", description="serverErrorDetails field"
    )

    debugId: str = Field(alias="debugId", description="A unique identifier for the instance of this error.")


class SubscriptionsPostRequest(BaseModel):
    """SubscriptionsPostRequest model"""

    subscriptions: List[Dict[str, Any]] = Field(alias="subscriptions", description="An array of subscription keys.")


class AsyncResponse(BaseModel):
    """AsyncResponse model"""

    status: str = Field(alias="status", description="Three digit HTTPS status code and message.")

    transactionId: str = Field(alias="transactionId", description="transactionId field")

    code: int = Field(alias="code", description="Three digit HTTP status code.")


class V1Beta1SubscriptionDetail(BaseModel):
    """V1Beta1SubscriptionDetail model"""

    isEval: Optional[bool] = Field(
        default=None,
        alias="isEval",
        description="A boolean that states if the subscription is an evaluation subscription or not.",
    )

    skuDescription: Optional[str] = Field(
        default=None, alias="skuDescription", description="A description of the stock keeping unit."
    )

    quantity: Optional[str] = Field(default=None, alias="quantity", description="Total quantity of the subscription")

    tags: Optional[Dict[str, Any]] = Field(default=None, alias="tags", description="tags field")

    type: str = Field(alias="type", description="The type of the resource.")

    availableQuantity: Optional[str] = Field(
        default=None, alias="availableQuantity", description="Available quantity of the subscription."
    )

    createdAt: Optional[str] = Field(default=None, alias="createdAt", description="Time of subscription creation.")

    updatedAt: Optional[str] = Field(
        default=None, alias="updatedAt", description="Time when subscription was last updated."
    )

    endTime: Optional[str] = Field(default=None, alias="endTime", description="End time of the subscription.")

    productType: Optional[str] = Field(
        default=None, alias="productType", description="Product type of the subscription."
    )

    startTime: Optional[str] = Field(default=None, alias="startTime", description="Start time of the subscription.")

    tier: Optional[str] = Field(default=None, alias="tier", description="Tier of the subscription.")

    sku: Optional[str] = Field(default=None, alias="sku", description="The stock keeping unit (SKU).")

    subscriptionStatus: Optional[str] = Field(
        default=None,
        alias="subscriptionStatus",
        description="The status of the subscription. This property indicates if the subscription is started, ended, suspended, cancelled, or locked.",
    )

    contract: Optional[str] = Field(default=None, alias="contract", description="contract field")

    subscriptionType: Optional[str] = Field(
        default=None, alias="subscriptionType", description="Type of the subscription."
    )

    key: Optional[str] = Field(default=None, alias="key", description="The subscription key.")

    id: str = Field(alias="id", description="The primary unique identifier of the subscription.")


class HpeGreenLakeBadRequestError(BaseModel):
    """HpeGreenLakeBadRequestError model"""

    errorCode: str = Field(
        alias="errorCode", description="A unique machine-friendly, but human-readable identifier for the error."
    )

    httpStatusCode: int = Field(alias="httpStatusCode", description="The HTTP equivalent status code.")

    message: str = Field(alias="message", description="A user-friendly error message.")

    badRequestErrorDetails: Optional[List[Dict[str, Any]]] = Field(
        default=None, alias="badRequestErrorDetails", description="badRequestErrorDetails field"
    )

    debugId: str = Field(alias="debugId", description="A unique identifier for the instance of this error.")


class AutoSubscriptionsResponseDto(BaseModel):
    """AutoSubscriptionsResponseDto model"""

    resourceUri: str = Field(alias="resourceUri", description="URI to the auto-subscription.")

    type: str = Field(alias="type", description="The type of the resource.")

    updatedAt: str = Field(alias="updatedAt", description="The time of last auto-subscription update.")

    autoSubscriptionSettings: Optional[List[Dict[str, Any]]] = Field(
        default=None, alias="autoSubscriptionSettings", description="autoSubscriptionSettings field"
    )

    createdAt: str = Field(alias="createdAt", description="The time of auto-subscription creation.")

    generation: Optional[int] = Field(
        default=None, alias="generation", description="Monotonically increasing update counter."
    )

    id: str = Field(alias="id", description="The unique identifier of the auto-subscription.")


class AutoSubscriptionsResponseDtoWithTenant(BaseModel):
    """AutoSubscriptionsResponseDtoWithTenant model"""

    generation: Optional[int] = Field(
        default=None, alias="generation", description="Monotonically increasing update counter."
    )

    id: str = Field(alias="id", description="The unique identifier of the tenant.")

    resourceUri: str = Field(alias="resourceUri", description="URI to the auto-subscription.")

    tenantWorkspaceId: Optional[str] = Field(
        default=None, alias="tenantWorkspaceId", description="The unique identifier of a tenant workspace."
    )

    type: str = Field(alias="type", description="Type of the resource")

    updatedAt: str = Field(alias="updatedAt", description="Time of last auto-subscription update.")

    autoSubscriptionSettings: Optional[List[Dict[str, Any]]] = Field(
        default=None, alias="autoSubscriptionSettings", description="autoSubscriptionSettings field"
    )

    createdAt: str = Field(alias="createdAt", description="Time of auto-subscription creation.")


class ServerErrorDetail(BaseModel):
    """ServerErrorDetail model"""

    retryAfterSeconds: int = Field(alias="retryAfterSeconds", description="retryAfterSeconds field")

    type: str = Field(alias="type", description="type field")


class SubscriptionsPatchRequest(BaseModel):
    """SubscriptionsPatchRequest model"""

    tags: Dict[str, Any] = Field(alias="tags", description="tags field")


class RequestPostSubscription(BaseModel):
    """RequestPostSubscription model"""

    tags: Optional[Dict[str, Any]] = Field(default=None, alias="tags", description="tags field")

    key: str = Field(alias="key", description="A subscription key.")


class Appointment(BaseModel):
    """Appointment model"""

    subscriptionStart: Optional[str] = Field(
        default=None, alias="subscriptionStart", description="Start date of the subscription."
    )

    delayedActivation: Optional[str] = Field(
        default=None, alias="delayedActivation", description="Delayed activation date of the subscription."
    )

    subscriptionEnd: Optional[str] = Field(
        default=None, alias="subscriptionEnd", description="End date of the subscription."
    )


class AutoSubscriptionsResponsePaginatedDto(BaseModel):
    """AutoSubscriptionsResponsePaginatedDto model"""

    offset: Optional[int] = Field(default=None, alias="offset", description="Zero-based resource offset.")

    total: Optional[int] = Field(
        default=None,
        alias="total",
        description="Total number of items in the collection that match the filter query, if one was provided in the request otherwise total number of items for a given resource.",
    )

    count: int = Field(alias="count", description="Number of items returned.")

    items: List[Dict[str, Any]] = Field(alias="items", description="items field")


class RequestPostAutoSubscription(BaseModel):
    """RequestPostAutoSubscription model"""

    tier: str = Field(alias="tier", description="tier field")

    deviceType: str = Field(alias="deviceType", description="deviceType field")


class SubscriptionDetail(BaseModel):
    """SubscriptionDetail model"""

    aasType: Optional[str] = Field(
        default=None,
        alias="aasType",
        description="Defines the as a service (aaS) type. For example, infrastructure as a service (IAAS).",
    )

    productSku: Optional[str] = Field(
        default=None, alias="productSku", description="The product stock keeping unit (SKU)."
    )

    productDescription: Optional[str] = Field(
        default=None, alias="productDescription", description="A description of the product stock keeping unit."
    )

    contract: Optional[str] = Field(default=None, alias="contract", description="contract field")

    po: Optional[str] = Field(default=None, alias="po", description="The purchase order number.")

    endUserName: Optional[str] = Field(
        default=None, alias="endUserName", description="The customer name to which the subscription belongs."
    )

    key: Optional[str] = Field(default=None, alias="key", description="The subscription key.")

    quantity: Optional[str] = Field(default=None, alias="quantity", description="Total quantity of the subscription.")

    appointment: Optional[Dict[str, Any]] = Field(default=None, alias="appointment", description="appointment field")

    orderClass: Optional[str] = Field(default=None, alias="orderClass", description="The ordering system source.")

    evaluationType: Optional[str] = Field(default=None, alias="evaluationType", description="The type of license.")

    id: str = Field(alias="id", description="The unique identifier for the subscription.")

    quote: Optional[str] = Field(
        default=None,
        alias="quote",
        description="A unique number that identifies an order and all its attached subscriptions.",
    )


class SubscriptionsGetResponse(BaseModel):
    """SubscriptionsGetResponse model"""

    offset: Optional[int] = Field(default=None, alias="offset", description="Zero-based resource offset.")

    total: Optional[int] = Field(
        default=None,
        alias="total",
        description="Total number of items in the collection that match the filter query, if one was provided in the request otherwise total number of items for a given resource.",
    )

    count: int = Field(alias="count", description="Number of items returned.")

    items: List[Dict[str, Any]] = Field(alias="items", description="items field")
