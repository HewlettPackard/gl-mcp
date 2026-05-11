# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
Base models for service-catalog MCP server.

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


class Service_offer_management_RecentService(BaseModel):
    """Service_offer_management_RecentService model"""

    serviceOffer: str = Field(alias="serviceOffer", description="serviceOffer field")

    type: str = Field(alias="type", description="Resource Type")

    id: str = Field(alias="id", description="Service Offer identifier")

    lastAccessedTime: Optional[str] = Field(
        default=None,
        alias="lastAccessedTime",
        description="Most recent date and time at which service offer was launched",
    )

    regionalProvisions: Optional[list[Any]] = Field(
        default=None, alias="regionalProvisions", description="regionalProvisions field"
    )


class Service_offer_management_ServiceOfferMediaVideoDetails(BaseModel):
    """Service_offer_management_ServiceOfferMediaVideoDetails model"""

    description: str = Field(alias="description", description="summary about the media")

    video: str = Field(alias="video", description="S3/minio URL")


class Service_offer_management_CategoryWithFeaturedServiceOffers(BaseModel):
    """Service_offer_management_CategoryWithFeaturedServiceOffers model"""

    servicesWithRegions: Optional[list[Any]] = Field(
        default=None, alias="servicesWithRegions", description="servicesWithRegions field"
    )

    type: str = Field(alias="type", description="Type of resource")

    id: str = Field(
        alias="id",
        description="The category to which a service offer belongs, such as compute, networking, or storage.",
    )


class Service_offer_management_CategoryWithServiceOffers(BaseModel):
    """Service_offer_management_CategoryWithServiceOffers model"""

    id: str = Field(
        alias="id",
        description="The category to which a service offer belongs, such as compute, networking, or storage.",
    )

    servicesWithRegions: list[Any] = Field(alias="servicesWithRegions", description="servicesWithRegions field")

    type: str = Field(alias="type", description="Type of resource")


class Service_offer_management_PreConditionFailedError(BaseModel):
    """Service_offer_management_PreConditionFailedError model"""

    message: str = Field(alias="message", description="A user-friendly error message.")

    debugId: str = Field(alias="debugId", description="A unique identifier for the instance of this error.")

    errorCode: str = Field(alias="errorCode", description="A unique machine-friendly identifier for the error.")

    errorDetails: list[Any] = Field(alias="errorDetails", description="Additional detailed information about the error")

    httpStatusCode: int = Field(alias="httpStatusCode", description="The HTTP equivalent status code")


class Service_Manager_Management_UnauthorizedError(BaseModel):
    """Service_Manager_Management_UnauthorizedError model"""

    debugId: str = Field(alias="debugId", description="A unique identifier for the instance of this error.")

    errorCode: str = Field(
        alias="errorCode", description="A unique machine-friendly, but human-readable identifier for the error."
    )

    httpStatusCode: int = Field(alias="httpStatusCode", description="The HTTP equivalent status code.")

    message: str = Field(alias="message", description="A user-friendly error message.")


class Service_Manager_Management_ConflictError(BaseModel):
    """Service_Manager_Management_ConflictError model"""

    errorCode: str = Field(
        alias="errorCode", description="A unique machine-friendly, but human-readable identifier for the error."
    )

    httpStatusCode: int = Field(alias="httpStatusCode", description="The HTTP equivalent status code.")

    message: str = Field(alias="message", description="A user-friendly error message.")

    debugId: str = Field(alias="debugId", description="A unique identifier for the instance of this error.")


class Service_offer_management_DetailedProvision(BaseModel):
    """Service_offer_management_DetailedProvision model"""

    serviceManagerProvision: Optional[str] = Field(
        default=None, alias="serviceManagerProvision", description="serviceManagerProvision field"
    )

    serviceOffer: Optional[str] = Field(default=None, alias="serviceOffer", description="serviceOffer field")

    serviceProvision: Optional[str] = Field(
        default=None, alias="serviceProvision", description="serviceProvision field"
    )


class Service_offer_management_OperationalMode(BaseModel):
    """The operational mode of the service offer."""


class Service_Manager_Management_ServiceManagerProvisionCreateBase(BaseModel):
    """Service manager provision request details"""

    region: str = Field(alias="region", description="HPE GreenLake platform defined region code.")

    serviceManagerId: str = Field(alias="serviceManagerId", description="The unique identifier of the service manager.")


class Service_offer_management_Region(BaseModel):
    """Service_offer_management_Region model"""

    id: Optional[str] = Field(
        default=None,
        alias="id",
        description="The code name for a geographical region supported by the HPE GreenLake cloud.",
    )

    name: Optional[str] = Field(
        default=None, alias="name", description="The human-readable name for the geographical region."
    )

    type: Optional[str] = Field(default=None, alias="type", description="The resource type identifier for the region.")


class Service_offer_management_ServiceOfferResourceLink(BaseModel):
    """Service_offer_management_ServiceOfferResourceLink model"""

    id: Optional[str] = Field(default=None, alias="id", description="The unique identifier for the service offer.")

    resourceUri: Optional[str] = Field(
        default=None, alias="resourceUri", description="The URI reference to the service offer resource."
    )


class Service_offer_management_ForbiddenError(BaseModel):
    """Service_offer_management_ForbiddenError model"""

    errorDetails: Optional[list[Any]] = Field(
        default=None, alias="errorDetails", description="Additional detailed information about the error"
    )

    httpStatusCode: int = Field(alias="httpStatusCode", description="The HTTP equivalent status code")

    message: str = Field(alias="message", description="A user-friendly error message.")

    debugId: str = Field(alias="debugId", description="A unique identifier for the instance of this error.")

    errorCode: str = Field(alias="errorCode", description="A unique machine-friendly identifier for the error.")


class Service_Manager_Management_ServiceManagerProvisionReadList(BaseModel):
    """List of service managers provisioned details."""

    count: int = Field(alias="count", description="Number of items returned")

    items: list[Any] = Field(alias="items", description="items field")

    offset: int = Field(alias="offset", description="Zero-based resource offset")

    total: Optional[int] = Field(
        default=None,
        alias="total",
        description="Total count of items in the collection after applying the provided query parameters.",
    )


class Service_provision_management_ForbiddenError(BaseModel):
    """Service_provision_management_ForbiddenError model"""

    message: str = Field(alias="message", description="A user-friendly error message")

    debugId: str = Field(
        alias="debugId", description="A unique identifier for the instance of this error. Maybe same as trace ID."
    )

    errorCode: str = Field(
        alias="errorCode",
        description="A unique machine-friendly identifier for the error from a global list of enumerated identifier strings",
    )

    httpStatusCode: int = Field(alias="httpStatusCode", description="The HTTP equivalent status code")


class Service_Manager_Management_BadRequestError(BaseModel):
    """Service_Manager_Management_BadRequestError model"""

    httpStatusCode: int = Field(alias="httpStatusCode", description="The HTTP equivalent status code.")

    message: str = Field(alias="message", description="A user-friendly error message.")

    debugId: str = Field(alias="debugId", description="A unique identifier for the instance of this error.")

    errorCode: str = Field(
        alias="errorCode", description="A unique machine-friendly, but human-readable identifier for the error."
    )


class Service_offer_management_Category(BaseModel):
    """The category to which a service offer belongs, such as compute, networking, or storage."""


class Service_provision_management_BadRequestError(BaseModel):
    """Service_provision_management_BadRequestError model"""

    debugId: str = Field(
        alias="debugId", description="A unique identifier for the instance of this error. Maybe same as trace ID."
    )

    errorCode: str = Field(
        alias="errorCode",
        description="A unique machine-friendly identifier for the error from a global list of enumerated identifier strings",
    )

    errorDetails: list[Any] = Field(alias="errorDetails", description="Additional detailed information about the error")

    httpStatusCode: int = Field(alias="httpStatusCode", description="The HTTP equivalent status code")

    message: str = Field(alias="message", description="A user-friendly error message")


class Service_offer_management_WorkspaceTypes(BaseModel):
    """The type of workspace. For example, a managed service provider (MSP) or standalone workspace."""


class Service_provision_management_ServiceOfferResourceLink(BaseModel):
    """Service_provision_management_ServiceOfferResourceLink model"""

    resourceUri: Optional[str] = Field(default=None, alias="resourceUri", description="The URI of the resource.")

    id: Optional[str] = Field(default=None, alias="id", description="The unique identifier of a service offer.")

    name: Optional[str] = Field(default=None, alias="name", description="The name of the service offer")


class Service_provision_management_AccountType(BaseModel):
    """The type of workspace associated with the account."""


class Service_offer_management_ServiceOfferRead(BaseModel):
    """Service_offer_management_ServiceOfferRead model"""

    documentationUrl: str = Field(alias="documentationUrl", description="An HTTPS URL to the documentation.")

    brokerUri: str = Field(
        alias="brokerUri",
        description="HPE Internal. Applies only to internal service offers. It is the relative path starting with API group (the API group is sufficient). The base URI is the API gateway for the HPE GreenLake cloud cluster. This is the application API endpoint exposed by application to be called from HPE GreenLake cloud.",
    )

    categories: list[Any] = Field(alias="categories", description="The categories to which the service offer belongs.")

    capabilities: list[Any] = Field(
        alias="capabilities", description="A list of key features or functionalities provided by the service offer."
    )

    createdAt: str = Field(alias="createdAt", description="Date and time at which the service offer was created.")

    slug: str = Field(alias="slug", description="A short identifier for the service offer.")

    languagesSupported: list[Any] = Field(
        alias="languagesSupported", description="The ISO codes for languages supported by this service offer."
    )

    preProvisionMessage: str = Field(
        alias="preProvisionMessage",
        description="A message displayed to users before provisioning the service offer, such as warnings or important information.",
    )

    testDriveUrl: str = Field(alias="testDriveUrl", description="An HTTPS URL to test drive.")

    evalUrl: str = Field(
        alias="evalUrl", description="The URL to sign up for a time-limited evaluation or trial of the service offer."
    )

    overview: str = Field(alias="overview", description="A brief overview of the service offer.")

    name: str = Field(alias="name", description="The name of the service offer.")

    termsOfServiceUrl: str = Field(alias="termsOfServiceUrl", description="An HTTPS URL to the terms of service.")

    serviceManager: dict[str, Any] = Field(alias="serviceManager", description="serviceManager field")

    id: str = Field(alias="id", description="The unique identifier for the service offer.")

    resourceUri: str = Field(alias="resourceUri", description="The URI reference to this resource.")

    staticLaunchUrl: str = Field(
        alias="staticLaunchUrl", description="The relative URL used to launch the service offer."
    )

    serviceOfferType: str = Field(alias="serviceOfferType", description="serviceOfferType field")

    shortDescription: str = Field(
        alias="shortDescription", description="A short description or tagline for the service offer."
    )

    generation: Optional[str] = Field(
        default=None, alias="generation", description="A monotonically increasing update counter."
    )

    status: str = Field(alias="status", description="status field")

    contactSalesUrl: str = Field(alias="contactSalesUrl", description="The HTTPS URL for contacting the sales team.")

    featuresSupported: list[Any] = Field(
        alias="featuresSupported",
        description="The features supported by this service offer, such as deep linking or RBAC.",
    )

    isDefault: Optional[str] = Field(
        default=None,
        alias="isDefault",
        description="Indicates whether this service offer is the default for its service manager.",
    )

    updatedAt: Optional[str] = Field(
        default=None, alias="updatedAt", description="Date and time at which the service offer was last updated."
    )


class Service_Manager_Management_ValidationError(BaseModel):
    """Service_Manager_Management_ValidationError model"""

    errorCode: str = Field(
        alias="errorCode", description="A unique machine-friendly, but human-readable identifier for the error."
    )

    httpStatusCode: int = Field(alias="httpStatusCode", description="The HTTP equivalent status code.")

    message: str = Field(alias="message", description="A user-friendly error message.")

    debugId: str = Field(alias="debugId", description="A unique identifier for the instance of this error.")


class Service_provision_management_ServiceManagerResourceLink(BaseModel):
    """Service_provision_management_ServiceManagerResourceLink model"""

    resourceUri: Optional[str] = Field(default=None, alias="resourceUri", description="The URI of the resource.")

    id: Optional[str] = Field(default=None, alias="id", description="The unique identifier for the service manager.")


class Service_provision_management_ServiceProvision(BaseModel):
    """Service_provision_management_ServiceProvision model"""

    resourceUri: str = Field(alias="resourceUri", description="The URI of the resource.")

    serviceManagerInstanceId: Optional[str] = Field(
        default=None,
        alias="serviceManagerInstanceId",
        description="The unique identifier of a service manager instance. This is the application instance ID of an application related to a service offer.",
    )

    workspace: dict[str, Any] = Field(alias="workspace", description="workspace field")

    updatedAt: str = Field(alias="updatedAt", description="Date and time at which the service offer was updated.")

    serviceOffer: dict[str, Any] = Field(alias="serviceOffer", description="serviceOffer field")

    provisionStatus: Optional[str] = Field(
        default=None, alias="provisionStatus", description="The current status of provisioning."
    )

    serviceManagerProvision: Optional[dict[str, Any]] = Field(
        default=None, alias="serviceManagerProvision", description="serviceManagerProvision field"
    )

    type: str = Field(alias="type", description="The type of the resource.")

    reason: Optional[str] = Field(
        default=None, alias="reason", description="The reason the service provision creation failed."
    )

    retryCount: int = Field(alias="retryCount", description="The number of times the operation has been retried.")

    createdAt: str = Field(alias="createdAt", description="Date and time at which the service offer was created.")

    createdBy: Optional[str] = Field(
        default=None, alias="createdBy", description="The email address of the user who created the service provision."
    )

    id: str = Field(alias="id", description="The unique service provision identifier.")

    region: str = Field(alias="region", description="The HPE GreenLake-defined region code.")

    serviceManager: Optional[dict[str, Any]] = Field(
        default=None, alias="serviceManager", description="serviceManager field"
    )

    generation: int = Field(alias="generation", description="A monotonically increasing update counter.")


class Service_Manager_Management_ForbiddenError(BaseModel):
    """Service_Manager_Management_ForbiddenError model"""

    debugId: str = Field(alias="debugId", description="A unique identifier for the instance of this error.")

    errorCode: str = Field(
        alias="errorCode", description="A unique machine-friendly, but human-readable identifier for the error."
    )

    httpStatusCode: int = Field(alias="httpStatusCode", description="The HTTP equivalent status code.")

    message: str = Field(alias="message", description="A user-friendly error message.")


class Service_Manager_Management_ServiceManagerProvisionCreateResponse(BaseModel):
    """Service manager provision details when provision is initiated."""

    region: str = Field(alias="region", description="region field")

    resourceUri: str = Field(alias="resourceUri", description="URI to the service manager provision resource")

    serviceManager: dict[str, Any] = Field(
        alias="serviceManager", description="A reference to a service manager resource."
    )

    type: str = Field(alias="type", description="Type of resource")

    createdBy: str = Field(
        alias="createdBy", description="The HPE GreenLake platform username that provisioned the service manager."
    )

    generation: int = Field(alias="generation", description="Monotonically increasing update")

    id: str = Field(alias="id", description="id field")


class Service_Manager_Management_ServiceManagersPerRegion(BaseModel):
    """List of service managers grouped by region."""

    count: int = Field(alias="count", description="Number of items returned")

    items: list[Any] = Field(alias="items", description="items field")

    offset: int = Field(alias="offset", description="Zero-based resource offset")

    total: Optional[int] = Field(
        default=None,
        alias="total",
        description="Total number of items  that match the filter query, if one was provided in the request",
    )


class Service_offer_management_ServiceManagerProvisionResourceLink(BaseModel):
    """Service_offer_management_ServiceManagerProvisionResourceLink model"""

    id: Optional[str] = Field(
        default=None, alias="id", description="The unique identifier for the service manager provision."
    )

    resourceUri: Optional[str] = Field(
        default=None, alias="resourceUri", description="The URI reference to the service manager provision resource."
    )


class Service_provision_management_ServiceProvisionCreateBase(BaseModel):
    """Service_provision_management_ServiceProvisionCreateBase model"""

    region: str = Field(alias="region", description="The HPE GreenLake-defined region code.")

    serviceOfferId: str = Field(alias="serviceOfferId", description="The unique identifier for the service offer.")


class Service_provision_management_Error(BaseModel):
    """Service_provision_management_Error model"""

    errorCode: str = Field(
        alias="errorCode",
        description="A unique machine-friendly identifier for the error from a global list of enumerated identifier strings",
    )

    httpStatusCode: int = Field(alias="httpStatusCode", description="The HTTP equivalent status code")

    message: str = Field(alias="message", description="A user-friendly error message")

    debugId: str = Field(
        alias="debugId", description="A unique identifier for the instance of this error. Maybe same as trace ID."
    )

    errorDetails: Optional[list[Any]] = Field(
        default=None, alias="errorDetails", description="Additional detailed information about the error"
    )


class Service_provision_management_WorkspaceTransferStatus(BaseModel):
    """The status of a workspace transfer from one type to another."""


class Service_offer_management_ValidationError(BaseModel):
    """Service_offer_management_ValidationError model"""

    debugId: str = Field(alias="debugId", description="A unique identifier for the instance of this error.")

    errorCode: str = Field(alias="errorCode", description="A unique machine-friendly identifier for the error.")

    errorDetails: Optional[list[Any]] = Field(
        default=None, alias="errorDetails", description="Additional detailed information about the error"
    )

    httpStatusCode: int = Field(alias="httpStatusCode", description="The HTTP equivalent status code")

    message: str = Field(alias="message", description="A user-friendly error message.")


class Service_offer_management_ServiceProvision(BaseModel):
    """Service_offer_management_ServiceProvision model"""

    provisionStatus: Optional[str] = Field(
        default=None,
        alias="provisionStatus",
        description="The current provisioning status of the service, such as provisioned or failed.",
    )

    serviceManagerProvision: Optional[dict[str, Any]] = Field(
        default=None, alias="serviceManagerProvision", description="serviceManagerProvision field"
    )

    workspace: dict[str, Any] = Field(alias="workspace", description="workspace field")

    id: str = Field(alias="id", description="Service provision identifier")

    updatedAt: Optional[str] = Field(
        default=None, alias="updatedAt", description="Date and time at which the service offer was updated."
    )

    generation: int = Field(alias="generation", description="Generated/updated version")

    reason: Optional[str] = Field(default=None, alias="reason", description="reason field")

    resourceUri: str = Field(alias="resourceUri", description="resourceUri field")

    serviceManagerInstanceId: Optional[str] = Field(
        default=None, alias="serviceManagerInstanceId", description="serviceManagerInstanceId field"
    )

    createdBy: Optional[str] = Field(default=None, alias="createdBy", description="createdBy field")

    region: str = Field(alias="region", description="region field")

    serviceManager: Optional[dict[str, Any]] = Field(
        default=None, alias="serviceManager", description="serviceManager field"
    )

    createdAt: Optional[str] = Field(
        default=None, alias="createdAt", description="Date and time at which the service offer was created or upgraded."
    )

    serviceOffer: dict[str, Any] = Field(alias="serviceOffer", description="serviceOffer field")


class Service_offer_management_ServiceOfferRegionRead(BaseModel):
    """Service_offer_management_ServiceOfferRegionRead model"""

    type: str = Field(alias="type", description="The type of the resource.")

    generation: int = Field(alias="generation", description="A monotonically increasing update counter.")

    serviceOffer: Optional[dict[str, Any]] = Field(default=None, alias="serviceOffer", description="serviceOffer field")

    updatedAt: str = Field(alias="updatedAt", description="Date and time at which the service offer was updated.")

    status: str = Field(alias="status", description="The current status of the service offer.")

    id: str = Field(alias="id", description="The unique identifier for the service offer region.")

    createdAt: str = Field(alias="createdAt", description="Date and time at which the service offer was created.")

    region: str = Field(
        alias="region", description="The code name of the region where this service offer is available."
    )

    resourceUri: Optional[str] = Field(
        default=None, alias="resourceUri", description="The URI reference to this resource."
    )


class Service_Manager_Management_ServiceManagerReadList(BaseModel):
    """List of service managers"""

    items: list[Any] = Field(alias="items", description="items field")

    offset: int = Field(alias="offset", description="Zero-based resource offset")

    total: Optional[int] = Field(
        default=None,
        alias="total",
        description="Total count of items in the collection after applying the provided query parameters.",
    )

    count: int = Field(alias="count", description="Number of items returned")


class Service_offer_management_ServiceManagerProvision(BaseModel):
    """Service manager provision details"""

    serviceManager: dict[str, Any] = Field(alias="serviceManager", description="serviceManager field")

    resourceUri: str = Field(alias="resourceUri", description="URI to the service manager provision resource")

    generation: int = Field(alias="generation", description="Monotonically increasing update counter.")

    reason: str = Field(alias="reason", description="Reason for failure")

    region: str = Field(alias="region", description="region field")

    updatedAt: str = Field(alias="updatedAt", description="Date and time at which the service offer was updated.")

    id: str = Field(alias="id", description="id field")

    serviceManagerInstanceId: str = Field(
        alias="serviceManagerInstanceId", description="serviceManagerInstanceId field"
    )

    workspaceTransferStatus: Optional[str] = Field(
        default=None, alias="workspaceTransferStatus", description="workspaceTransferStatus field"
    )

    createdAt: str = Field(
        alias="createdAt", description="Date and time at which the service offer was created or upgraded."
    )

    provisionStatus: str = Field(alias="provisionStatus", description="provisionStatus field")


class Service_offer_management_RecentServiceV2(BaseModel):
    """Service_offer_management_RecentServiceV2 model"""

    serviceProvision: Optional[str] = Field(
        default=None, alias="serviceProvision", description="serviceProvision field"
    )

    type: str = Field(alias="type", description="Resource Type")

    id: str = Field(alias="id", description="Id of service-manager-provision entry or service-provision entry")

    lastAccessedTime: str = Field(
        alias="lastAccessedTime", description="Most recent date and time at which service was launched"
    )

    region: str = Field(alias="region", description="region field")

    serviceManagerProvision: Optional[str] = Field(
        default=None, alias="serviceManagerProvision", description="serviceManagerProvision field"
    )

    serviceOffer: str = Field(alias="serviceOffer", description="serviceOffer field")


class Service_offer_management_ServiceOfferStatus(BaseModel):
    """The current status of the service offer."""


class Service_offer_management_MSPConversionStatus(BaseModel):
    """The status of a MSP conversion process."""


class Service_offer_management_SupportedFeature(BaseModel):
    """Indicates a feature supported by the service offer. \nExamples include deep linking, evaluation, provisioning, and RBAC support.\n"""


class Service_offer_management_ServiceProvisionPartialInfo(BaseModel):
    """Service provision abraged information. Typically used when only fully provisioned entries are needed."""

    updatedAt: Optional[str] = Field(
        default=None, alias="updatedAt", description="Date and time at which the service offer was updated."
    )

    createdAt: Optional[str] = Field(
        default=None, alias="createdAt", description="Date and time at which the service offer was created or upgraded."
    )

    createdBy: Optional[str] = Field(default=None, alias="createdBy", description="createdBy field")

    generation: int = Field(alias="generation", description="Generated/updated version")

    id: str = Field(alias="id", description="Service provision identifier")

    region: str = Field(alias="region", description="region field")

    resourceUri: str = Field(alias="resourceUri", description="resourceUri field")

    serviceManagerInstanceId: str = Field(
        alias="serviceManagerInstanceId", description="serviceManagerInstanceId field"
    )


class Service_Manager_Management_ServiceManagerRead(BaseModel):
    """Service manager details"""

    type: str = Field(alias="type", description="Type of resource")

    generation: int = Field(alias="generation", description="Monotonically increasing update counter.")

    workspaceTransferSupported: Optional[bool] = Field(
        default=None,
        alias="workspaceTransferSupported",
        description="Service Manager supports Workspace Transfer or not",
    )

    honorUnprovisionResponse: bool = Field(alias="honorUnprovisionResponse", description="Honor Unprovision or not")

    resourceUri: str = Field(alias="resourceUri", description="URI to the service manager resource")

    workspaceOpModesSupported: Optional[str] = Field(
        default=None, alias="workspaceOpModesSupported", description="Types of tenants supported by the service manager"
    )

    mspOnlySupported: Optional[bool] = Field(
        default=None,
        alias="mspOnlySupported",
        description="Service Manager supports only Managed Service Provider (MSP) or not",
    )

    standaloneSupported: bool = Field(
        alias="standaloneSupported", description="Service manager supports Standalone or not"
    )

    id: str = Field(alias="id", description="The unique ID of the service manager.")

    createdAt: str = Field(alias="createdAt", description="Date and time the service was created.")

    mspSupported: bool = Field(
        alias="mspSupported", description="Service manager supports Managed Service Provider (MSP) or not"
    )

    updatedAt: str = Field(alias="updatedAt", description="Date and time the service manager metadata was updated.")

    name: str = Field(alias="name", description="Name of the service manager")

    description: Optional[str] = Field(
        default=None, alias="description", description="Description of the service manager."
    )

    tenantOnlySupported: bool = Field(
        alias="tenantOnlySupported", description="Service manager supports Tenant only Supported or not"
    )


class Service_Manager_Management_ServiceManagersForARegion(BaseModel):
    """List of service managers for a specified region."""

    regionName: str = Field(
        alias="regionName", description="The name of geographical region where the service manager is available."
    )

    serviceManagers: list[Any] = Field(alias="serviceManagers", description="serviceManagers field")

    type: str = Field(alias="type", description="Type of resource")

    generation: int = Field(alias="generation", description="Monotonically increasing update counter.")

    id: str = Field(
        alias="id", description="HPE GreenLake platform defined region where the service manager is available."
    )


class Service_offer_management_TooManyRequestsError(BaseModel):
    """Service_offer_management_TooManyRequestsError model"""

    message: str = Field(alias="message", description="A user-friendly error message.")

    debugId: str = Field(alias="debugId", description="A unique identifier for the instance of this error.")

    errorCode: str = Field(alias="errorCode", description="A unique machine-friendly identifier for the error.")

    errorDetails: Optional[list[Any]] = Field(
        default=None, alias="errorDetails", description="Additional detailed information about the error"
    )

    httpStatusCode: int = Field(alias="httpStatusCode", description="The HTTP equivalent status code")


class Service_provision_management_PreConditionFailedError(BaseModel):
    """Service_provision_management_PreConditionFailedError model"""

    message: str = Field(alias="message", description="A user-friendly error message")

    debugId: str = Field(
        alias="debugId", description="A unique identifier for the instance of this error. Maybe same as trace ID."
    )

    errorCode: str = Field(
        alias="errorCode",
        description="A unique machine-friendly identifier for the error from a global list of enumerated identifier strings",
    )

    httpStatusCode: int = Field(alias="httpStatusCode", description="The HTTP equivalent status code")


class Service_offer_management_DetailedServiceOffer(BaseModel):
    """Service_offer_management_DetailedServiceOffer model"""

    type: str = Field(alias="type", description="Type of resource")

    availableRegions: list[Any] = Field(
        alias="availableRegions",
        description="Names of the regions where the Service Offer is available for the logged in user/customer.",
    )

    id: str = Field(alias="id", description="Region with Detailed Provisions identifier")

    orgSingletonServiceProvisions: list[Any] = Field(
        alias="orgSingletonServiceProvisions",
        description="Service-provision entry for the organization that the current workspace belongs to.",
    )

    provisions: list[Any] = Field(alias="provisions", description="Data pertaining to service and app provisions")

    serviceManager: Optional[dict[str, Any]] = Field(
        default=None, alias="serviceManager", description="serviceManager field"
    )

    serviceOffer: Optional[str] = Field(default=None, alias="serviceOffer", description="serviceOffer field")


class Service_offer_management_FeaturedServiceOffers(BaseModel):
    """Featured Services Offers list grouped by Category"""

    items: list[Any] = Field(alias="items", description="items field")

    next: str = Field(alias="next", description="next field")

    total: int = Field(alias="total", description="Total Count")

    count: int = Field(alias="count", description="Count Per Page")


class Service_provision_management_NotFoundError(BaseModel):
    """Service_provision_management_NotFoundError model"""

    debugId: str = Field(
        alias="debugId", description="A unique identifier for the instance of this error. Maybe same as trace ID."
    )

    errorCode: str = Field(
        alias="errorCode",
        description="A unique machine-friendly identifier for the error from a global list of enumerated identifier strings",
    )

    httpStatusCode: int = Field(alias="httpStatusCode", description="The HTTP equivalent status code")

    message: str = Field(alias="message", description="A user-friendly error message")


class Service_provision_management_InternalError(BaseModel):
    """Service_provision_management_InternalError model"""

    httpStatusCode: int = Field(alias="httpStatusCode", description="The HTTP equivalent status code")

    message: str = Field(alias="message", description="A user-friendly error message")

    debugId: str = Field(
        alias="debugId", description="A unique identifier for the instance of this error. Maybe same as trace ID."
    )

    errorCode: str = Field(
        alias="errorCode",
        description="A unique machine-friendly identifier for the error from a global list of enumerated identifier strings",
    )

    errorDetails: Optional[list[Any]] = Field(
        default=None, alias="errorDetails", description="Additional detailed information about the error"
    )


class Service_offer_management_ServiceOfferRegionsList(BaseModel):
    """Service_offer_management_ServiceOfferRegionsList model"""

    count: int = Field(alias="count", description="The number of returned items per page.")

    items: list[Any] = Field(alias="items", description="items field")

    next: str = Field(alias="next", description="Cursor for the next page of resources.")

    total: int = Field(alias="total", description="Total number of items in the result set.")


class Service_offer_management_BadRequestError(BaseModel):
    """Service_offer_management_BadRequestError model"""

    message: str = Field(alias="message", description="A user-friendly error message.")

    debugId: str = Field(alias="debugId", description="A unique identifier for the instance of this error.")

    errorCode: str = Field(alias="errorCode", description="A unique machine-friendly identifier for the error.")

    errorDetails: list[Any] = Field(alias="errorDetails", description="Additional detailed information about the error")

    httpStatusCode: int = Field(alias="httpStatusCode", description="The HTTP equivalent status code")


class Service_provision_management_ProvisionStatus(BaseModel):
    """The current status of provisioning."""


class Service_provision_management_ConflictError(BaseModel):
    """Service_provision_management_ConflictError model"""

    message: str = Field(alias="message", description="A user-friendly error message")

    debugId: str = Field(
        alias="debugId", description="A unique identifier for the instance of this error. Maybe same as trace ID."
    )

    errorCode: str = Field(
        alias="errorCode",
        description="A unique machine-friendly identifier for the error from a global list of enumerated identifier strings",
    )

    httpStatusCode: int = Field(alias="httpStatusCode", description="The HTTP equivalent status code")


class Service_offer_management_ServiceOfferCatalog(BaseModel):
    """List of Service Offers and available-regions grouped by Category"""

    total: int = Field(alias="total", description="Total Count")

    count: int = Field(alias="count", description="Count Per Page")

    items: list[Any] = Field(alias="items", description="items field")

    next: str = Field(alias="next", description="next field")


class Service_offer_management_WorkspaceOpMode(BaseModel):
    """The operational mode of the workspace, indicating where the service offer is visible or provisionable."""


class Service_Manager_Management_MSPConversionStatus(BaseModel):
    """The current status of Managed Service Provider conversion."""


class Service_provision_management_UnauthorizedError(BaseModel):
    """Service_provision_management_UnauthorizedError model"""

    errorCode: str = Field(
        alias="errorCode",
        description="A unique machine-friendly identifier for the error from a global list of enumerated identifier strings",
    )

    httpStatusCode: int = Field(alias="httpStatusCode", description="The HTTP equivalent status code")

    message: str = Field(alias="message", description="A user-friendly error message")

    debugId: str = Field(
        alias="debugId", description="A unique identifier for the instance of this error. Maybe same as trace ID."
    )


class Service_offer_management_ServiceManagerResourceLink(BaseModel):
    """Service_offer_management_ServiceManagerResourceLink model"""

    resourceUri: Optional[str] = Field(
        default=None, alias="resourceUri", description="The URI reference to the service manager resource."
    )

    id: Optional[str] = Field(default=None, alias="id", description="The unique identifier for the service manager.")


class Service_offer_management_MyServices(BaseModel):
    """Service_offer_management_MyServices model"""

    total: int = Field(alias="total", description="Total Count")

    count: int = Field(alias="count", description="Count Per Page")

    items: list[Any] = Field(alias="items", description="Data pertaining to service and app provisions")

    next: str = Field(alias="next", description="next field")


class Service_offer_management_ServiceOfferMediaImageDetails(BaseModel):
    """Service_offer_management_ServiceOfferMediaImageDetails model"""

    description: str = Field(alias="description", description="summary about the media")

    image: str = Field(alias="image", description="S3/minio URL")


class Service_offer_management_ServiceOfferWithAvailableRegions(BaseModel):
    """Service_offer_management_ServiceOfferWithAvailableRegions model"""

    serviceOffer: dict[str, Any] = Field(alias="serviceOffer", description="serviceOffer field")

    type: Optional[str] = Field(default=None, alias="type", description="The resource type for this object.")

    availableRegions: list[Any] = Field(
        alias="availableRegions",
        description="The list of regions where this service offer is available to the current user or customer.",
    )

    id: Optional[str] = Field(
        default=None, alias="id", description="The unique identifier for the service offer with available regions."
    )


class Service_provision_management_ValidationError(BaseModel):
    """Service_provision_management_ValidationError model"""

    message: str = Field(alias="message", description="A user-friendly error message")

    debugId: str = Field(
        alias="debugId", description="A unique identifier for the instance of this error. Maybe same as trace ID."
    )

    errorCode: str = Field(
        alias="errorCode",
        description="A unique machine-friendly identifier for the error from a global list of enumerated identifier strings",
    )

    httpStatusCode: int = Field(alias="httpStatusCode", description="The HTTP equivalent status code")


class Service_Manager_Management_PreConditionFailedError(BaseModel):
    """Service_Manager_Management_PreConditionFailedError model"""

    message: str = Field(alias="message", description="A user-friendly error message.")

    debugId: str = Field(alias="debugId", description="A unique identifier for the instance of this error.")

    errorCode: str = Field(
        alias="errorCode", description="A unique machine-friendly, but human-readable identifier for the error."
    )

    httpStatusCode: int = Field(alias="httpStatusCode", description="The HTTP equivalent status code.")


class Service_provision_management_ServiceProvisionList(BaseModel):
    """Service_provision_management_ServiceProvisionList model"""

    count: int = Field(alias="count", description="The number of items returned.")

    items: list[Any] = Field(alias="items", description="items field")

    next: str = Field(alias="next", description="Cursor for the next page of resources.")

    total: int = Field(alias="total", description="Total number of items in the result set.")


class Service_offer_management_WorkspaceTransferStatus(BaseModel):
    """The status of a workspace transfer, indicating the progress of moving a workspace from one type to another."""


class Service_provision_management_MspConversionStatus(BaseModel):
    """The current status of MSP conversion. Indicates whether a workspace has been converted to MSP."""


class Service_Manager_Management_ServiceManagerProvisionRead(BaseModel):
    """Service manager provisioned details"""

    generation: int = Field(alias="generation", description="Monotonically increasing update counter.")

    resourceUri: str = Field(alias="resourceUri", description="URI to the service manager provision resource")

    createdBy: str = Field(
        alias="createdBy", description="The HPE GreenLake platform username that provisioned the service manager."
    )

    type: str = Field(alias="type", description="Type of resource")

    provisionStatus: str = Field(alias="provisionStatus", description="provisionStatus field")

    region: str = Field(alias="region", description="region field")

    createdAt: str = Field(alias="createdAt", description="Date and time the service offer was created or upgraded.")

    id: str = Field(alias="id", description="id field")

    updatedAt: str = Field(alias="updatedAt", description="Date and time the service offer was updated.")

    serviceManager: dict[str, Any] = Field(
        alias="serviceManager", description="A reference to a service manager resource."
    )


class Service_provision_management_BaseError(BaseModel):
    """Service_provision_management_BaseError model"""

    httpStatusCode: int = Field(alias="httpStatusCode", description="The HTTP equivalent status code")

    message: str = Field(alias="message", description="A user-friendly error message")

    debugId: str = Field(
        alias="debugId", description="A unique identifier for the instance of this error. Maybe same as trace ID."
    )

    errorCode: str = Field(
        alias="errorCode",
        description="A unique machine-friendly identifier for the error from a global list of enumerated identifier strings",
    )


class Service_Manager_Management_BaseError(BaseModel):
    """Service_Manager_Management_BaseError model"""

    errorCode: str = Field(
        alias="errorCode", description="A unique machine-friendly, but human-readable identifier for the error."
    )

    httpStatusCode: int = Field(alias="httpStatusCode", description="The HTTP equivalent status code.")

    message: str = Field(alias="message", description="A user-friendly error message.")

    debugId: str = Field(alias="debugId", description="A unique identifier for the instance of this error.")


class Service_provision_management_OperationalMode(BaseModel):
    """Indicates where the service offer can be viewed or provisioned."""


class Service_provision_management_WorkspaceResourceLink(BaseModel):
    """Service_provision_management_WorkspaceResourceLink model"""

    resourceUri: Optional[str] = Field(default=None, alias="resourceUri", description="The URI of the resource.")

    workspaceTransferStatus: Optional[str] = Field(
        default=None,
        alias="workspaceTransferStatus",
        description="The status of a workspace transfer from one type to another.",
    )

    id: Optional[str] = Field(default=None, alias="id", description="The workspace ID.")

    mspId: Optional[str] = Field(
        default=None, alias="mspId", description="The unique identifier of an MSP tenant account."
    )

    name: Optional[str] = Field(default=None, alias="name", description="The workspace name.")

    organizationId: Optional[str] = Field(
        default=None,
        alias="organizationId",
        description="The organization ID. Each HPE GreenLake Organization operates as a distinct tenant with its own identity directory and unique organization ID.",
    )


class Service_offer_management_RecentServices(BaseModel):
    """Service_offer_management_RecentServices model"""

    items: list[Any] = Field(alias="items", description="Service offer with provisions and last accessed timestamp")

    next: str = Field(alias="next", description="next field")

    total: int = Field(alias="total", description="Total Count")

    count: int = Field(alias="count", description="Count Per Page")


class Service_offer_management_ServiceOfferPartialInfo(BaseModel):
    """Service offer abraged information. Typically used when only available service-offers in a workspace are to be reported."""

    categories: list[Any] = Field(alias="categories", description="Types of categories")

    id: str = Field(alias="id", description="Identifier of service offer")

    name: str = Field(
        alias="name",
        description="Name of the Service Offer. In case of an app-provision, name of service-manager will be picked. If absent, name of app will be picked.",
    )

    resourceUri: str = Field(alias="resourceUri", description="Resource URI")

    serviceManager: Optional[dict[str, Any]] = Field(
        default=None, alias="serviceManager", description="serviceManager field"
    )

    slug: str = Field(
        alias="slug",
        description="Short identifier for a service offer. In case of an app-provision, slug will be picked from service-manager. If absent, slug will be picked from application.",
    )

    staticLaunchUrl: str = Field(alias="staticLaunchUrl", description="Relative URLs to launch")


class Service_Manager_Management_ProvisionStatus(BaseModel):
    """The current provisioning status."""


class Service_Manager_Management_Error(BaseModel):
    """Service_Manager_Management_Error model"""

    httpStatusCode: int = Field(alias="httpStatusCode", description="The HTTP equivalent status code.")

    message: str = Field(alias="message", description="A user-friendly error message.")

    debugId: str = Field(alias="debugId", description="A unique identifier for the instance of this error.")

    errorCode: str = Field(
        alias="errorCode", description="A unique machine-friendly, but human-readable identifier for the error."
    )


class Service_provision_management_ServiceManagerProvisionResourceLink(BaseModel):
    """Service_provision_management_ServiceManagerProvisionResourceLink model"""

    provisionStatus: Optional[str] = Field(
        default=None, alias="provisionStatus", description="The current status of provisioning."
    )

    reason: Optional[str] = Field(default=None, alias="reason", description="Reason for failure in provisioning")

    resourceUri: Optional[str] = Field(default=None, alias="resourceUri", description="The URI of the resource.")

    accountType: Optional[str] = Field(
        default=None, alias="accountType", description="The type of workspace associated with the account."
    )

    id: Optional[str] = Field(
        default=None, alias="id", description="The unique identifier for the provisioned service manager."
    )

    mspConversionStatus: Optional[str] = Field(
        default=None,
        alias="mspConversionStatus",
        description="The current status of MSP conversion. Indicates whether a workspace has been converted to MSP.",
    )

    operationalMode: Optional[str] = Field(
        default=None,
        alias="operationalMode",
        description="Indicates where the service offer can be viewed or provisioned.",
    )


class Service_offer_management_RegionalProvision(BaseModel):
    """Service_offer_management_RegionalProvision model"""

    serviceProvision: Optional[str] = Field(
        default=None, alias="serviceProvision", description="serviceProvision field"
    )

    type: Optional[str] = Field(default=None, alias="type", description="Resource Type")

    id: Optional[str] = Field(default=None, alias="id", description="Region as provision identifier")

    serviceManagerProvision: Optional[str] = Field(
        default=None, alias="serviceManagerProvision", description="serviceManagerProvision field"
    )


class Service_offer_management_ServiceOfferList(BaseModel):
    """Service_offer_management_ServiceOfferList model"""

    items: list[Any] = Field(alias="items", description="items field")

    next: str = Field(alias="next", description="Cursor for the next page of resources.")

    total: int = Field(alias="total", description="The total number of items in the result set.")

    count: int = Field(alias="count", description="The number of returned items per page.")


class Service_offer_management_WorkspaceResourceLink(BaseModel):
    """Service_offer_management_WorkspaceResourceLink model"""

    resourceUri: Optional[str] = Field(
        default=None, alias="resourceUri", description="The URI reference to this resource."
    )

    workspaceTransferStatus: Optional[str] = Field(
        default=None, alias="workspaceTransferStatus", description="workspaceTransferStatus field"
    )

    id: Optional[str] = Field(default=None, alias="id", description="The unique identifier for the workspace.")

    name: Optional[str] = Field(default=None, alias="name", description="The display name of the workspace.")

    organizationId: Optional[str] = Field(
        default=None, alias="organizationId", description="The unique identifier of the organization."
    )


class Service_Manager_Management_ServiceManagerResourceLink(BaseModel):
    """A reference to a service manager resource."""

    id: Optional[str] = Field(default=None, alias="id", description="id field")

    resourceUri: Optional[str] = Field(
        default=None, alias="resourceUri", description="URI to the service manager resource"
    )


class Service_offer_management_ServiceOfferPartialDetails(BaseModel):
    """Partial details for a service offer"""

    name: str = Field(
        alias="name",
        description="Name of the Service Offer. In case of an app-provision, name of service-manager will be picked. If absent, name of app will be picked.",
    )

    resourceUri: str = Field(alias="resourceUri", description="Resource URI")

    slug: str = Field(
        alias="slug",
        description="Short identifier for a service offer. In case of an app-provision, slug will be picked from service-manager. If absent, slug will be picked from application.",
    )

    staticLaunchUrl: str = Field(alias="staticLaunchUrl", description="Relative URLs to launch")

    workspaceOpModes: list[Any] = Field(
        alias="workspaceOpModes", description="Types of Workspace Operational Modes for Tenant Workspaces"
    )

    workspaceTypes: list[Any] = Field(alias="workspaceTypes", description="Workspace Types supported")

    categories: list[Any] = Field(alias="categories", description="Types of categories")

    id: str = Field(alias="id", description="Identifier of service offer")


class Service_offer_management_ServiceOfferReadWithMedia(BaseModel):
    """Service_offer_management_ServiceOfferReadWithMedia model"""

    termsOfServiceUrl: str = Field(alias="termsOfServiceUrl", description="An HTTPS URL to the terms of service.")

    capabilities: list[Any] = Field(
        alias="capabilities", description="A list of key features or functionalities provided by the service offer."
    )

    featuresSupported: list[Any] = Field(
        alias="featuresSupported",
        description="The features supported by this service offer, such as deep linking or RBAC.",
    )

    createdAt: str = Field(alias="createdAt", description="Date and time at which the service offer was created.")

    id: str = Field(alias="id", description="The unique identifier for the service offer.")

    contactSalesUrl: str = Field(alias="contactSalesUrl", description="The HTTPS URL for contacting the sales team.")

    testDriveUrl: str = Field(alias="testDriveUrl", description="An HTTPS URL to test drive.")

    workspaceTypes: str = Field(alias="workspaceTypes", description="workspaceTypes field")

    staticLaunchUrl: str = Field(
        alias="staticLaunchUrl", description="The relative URL used to launch the service offer."
    )

    slug: str = Field(alias="slug", description="A short identifier for the service offer.")

    preProvisionMessage: str = Field(
        alias="preProvisionMessage",
        description="A message displayed to users before provisioning the service offer, such as warnings or important information.",
    )

    documentationUrl: str = Field(alias="documentationUrl", description="An HTTPS URL to the documentation.")

    categories: list[Any] = Field(alias="categories", description="The categories to which the service offer belongs.")

    brokerUri: str = Field(
        alias="brokerUri",
        description="HPE Internal. Applies only to internal service offers. It is the relative path starting with API group (the API group is sufficient). The base URI is the API gateway for the HPE GreenLake cloud cluster. This is the application API endpoint exposed by application to be called from HPE GreenLake cloud.",
    )

    logo: str = Field(alias="logo", description="S3/minio URL")

    resourceUri: str = Field(alias="resourceUri", description="The URI reference to this resource.")

    updatedAt: Optional[str] = Field(
        default=None, alias="updatedAt", description="Date and time at which the service offer was last updated."
    )

    languagesSupported: list[Any] = Field(
        alias="languagesSupported", description="The ISO codes for languages supported by this service offer."
    )

    isDefault: Optional[str] = Field(
        default=None,
        alias="isDefault",
        description="Indicates whether this service offer is the default for its service manager.",
    )

    videos: list[Any] = Field(alias="videos", description="S3/minio URLs for the videos")

    overview: str = Field(alias="overview", description="A brief overview of the service offer.")

    serviceOfferType: str = Field(alias="serviceOfferType", description="serviceOfferType field")

    shortDescription: str = Field(
        alias="shortDescription", description="A short description or tagline for the service offer."
    )

    serviceManager: dict[str, Any] = Field(alias="serviceManager", description="serviceManager field")

    name: str = Field(alias="name", description="The name of the service offer.")

    evalUrl: str = Field(
        alias="evalUrl", description="The URL to sign up for a time-limited evaluation or trial of the service offer."
    )

    generation: Optional[str] = Field(
        default=None, alias="generation", description="A monotonically increasing update counter."
    )

    status: str = Field(alias="status", description="status field")

    screenshots: list[Any] = Field(alias="screenshots", description="S3/minio URLs for the screenshots")


class Service_offer_management_ServiceManagerProvisionPartialInfo(BaseModel):
    """Service manager provision abraged information. Typically used when only fully provisioned entries are needed."""

    serviceManagerInstanceId: str = Field(
        alias="serviceManagerInstanceId", description="serviceManagerInstanceId field"
    )

    updatedAt: Optional[str] = Field(
        default=None, alias="updatedAt", description="Date and time at which the service offer was updated."
    )

    createdAt: Optional[str] = Field(
        default=None, alias="createdAt", description="Date and time at which the service offer was created or upgraded."
    )

    createdBy: Optional[str] = Field(default=None, alias="createdBy", description="createdBy field")

    generation: int = Field(alias="generation", description="Monotonically increasing update counter.")

    id: str = Field(alias="id", description="id field")

    region: str = Field(alias="region", description="region field")

    resourceUri: str = Field(alias="resourceUri", description="URI to the service manager provision resource")


class Service_offer_management_ServiceOfferType(BaseModel):
    """The type of service offer."""


class Service_Manager_Management_InternalError(BaseModel):
    """Service_Manager_Management_InternalError model"""

    debugId: str = Field(alias="debugId", description="A unique identifier for the instance of this error.")

    errorCode: str = Field(
        alias="errorCode", description="A unique machine-friendly, but human-readable identifier for the error."
    )

    httpStatusCode: int = Field(alias="httpStatusCode", description="The HTTP equivalent status code.")

    message: str = Field(alias="message", description="A user-friendly error message.")


class Service_offer_management_DetailedServiceManagerResourceLink(BaseModel):
    """Service_offer_management_DetailedServiceManagerResourceLink model"""

    resourceUri: Optional[str] = Field(default=None, alias="resourceUri", description="Resource URI")

    serviceOfferId: Optional[str] = Field(default=None, alias="serviceOfferId", description="Service offer ID")

    id: Optional[str] = Field(default=None, alias="id", description="Service Manager ID")

    name: Optional[str] = Field(
        default=None,
        alias="name",
        description="service-offer belonging to the same application that has isDefault true",
    )


class Service_offer_management_RegionWithDetailedProvisions(BaseModel):
    """Service_offer_management_RegionWithDetailedProvisions model"""

    id: str = Field(alias="id", description="Region with Detailed Provisions identifier")

    provisions: list[Any] = Field(alias="provisions", description="provisions field")

    type: str = Field(alias="type", description="Resource Type")


class Service_offer_management_ConflictError(BaseModel):
    """Service_offer_management_ConflictError model"""

    message: str = Field(alias="message", description="A user-friendly error message.")

    debugId: str = Field(alias="debugId", description="A unique identifier for the instance of this error.")

    errorCode: str = Field(alias="errorCode", description="A unique machine-friendly identifier for the error.")

    errorDetails: Optional[list[Any]] = Field(
        default=None, alias="errorDetails", description="Additional detailed information about the error"
    )

    httpStatusCode: int = Field(alias="httpStatusCode", description="The HTTP equivalent status code")


class Service_offer_management_InternalError(BaseModel):
    """Service_offer_management_InternalError model"""

    debugId: str = Field(alias="debugId", description="A unique identifier for the instance of this error.")

    errorCode: str = Field(alias="errorCode", description="A unique machine-friendly identifier for the error.")

    errorDetails: list[Any] = Field(alias="errorDetails", description="Additional detailed information about the error")

    httpStatusCode: int = Field(alias="httpStatusCode", description="The HTTP equivalent status code")

    message: str = Field(alias="message", description="A user-friendly error message.")


class Service_offer_management_NotFoundError(BaseModel):
    """Service_offer_management_NotFoundError model"""

    debugId: str = Field(alias="debugId", description="A unique identifier for the instance of this error.")

    errorCode: str = Field(alias="errorCode", description="A unique machine-friendly identifier for the error.")

    errorDetails: Optional[list[Any]] = Field(
        default=None, alias="errorDetails", description="Additional detailed information about the error"
    )

    httpStatusCode: int = Field(alias="httpStatusCode", description="The HTTP equivalent status code")

    message: str = Field(alias="message", description="A user-friendly error message.")


class Service_offer_management_RegionWithLocations(BaseModel):
    """Service_offer_management_RegionWithLocations model"""

    id: Optional[str] = Field(
        default=None,
        alias="id",
        description="The code name for a geographical region supported by the HPE GreenLake cloud.",
    )

    name: Optional[str] = Field(
        default=None, alias="name", description="The human-readable name for the geographical region."
    )

    type: Optional[str] = Field(default=None, alias="type", description="The resource type identifier for the region.")

    locations: Optional[list[Any]] = Field(
        default=None,
        alias="locations",
        description="A list of physical locations within the region where the application instance is available.",
    )


class Service_offer_management_RecentServicesV2(BaseModel):
    """Service_offer_management_RecentServicesV2 model"""

    count: int = Field(alias="count", description="Count Per Page")

    items: list[Any] = Field(alias="items", description="Service offer with provisions and last accessed timestamp")

    next: str = Field(alias="next", description="next field")

    total: int = Field(alias="total", description="Total Count")


class Service_Manager_Management_NotFoundError(BaseModel):
    """Service_Manager_Management_NotFoundError model"""

    httpStatusCode: int = Field(alias="httpStatusCode", description="The HTTP equivalent status code.")

    message: str = Field(alias="message", description="A user-friendly error message.")

    debugId: str = Field(alias="debugId", description="A unique identifier for the instance of this error.")

    errorCode: str = Field(
        alias="errorCode", description="A unique machine-friendly, but human-readable identifier for the error."
    )


class Service_offer_management_ProvisionStatus(BaseModel):
    """The current provisioning status of the service, such as provisioned or failed."""


class Service_offer_management_UnauthorizedError(BaseModel):
    """Service_offer_management_UnauthorizedError model"""

    httpStatusCode: int = Field(alias="httpStatusCode", description="The HTTP equivalent status code")

    message: str = Field(alias="message", description="A user-friendly error message.")

    debugId: str = Field(alias="debugId", description="A unique identifier for the instance of this error.")

    errorCode: str = Field(alias="errorCode", description="A unique machine-friendly identifier for the error.")

    errorDetails: Optional[list[Any]] = Field(
        default=None, alias="errorDetails", description="Additional detailed information about the error"
    )
