# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""Unit tests for generated Pydantic models."""

from __future__ import annotations

from typing import Any

import pytest
from pydantic import ValidationError as PydanticValidationError

from greenlake_service_catalog_mcp.models import (
    BaseModel,
    Service_Manager_Management_PreConditionFailedError,
    Service_Manager_Management_MSPConversionStatus,
    Service_offer_management_Region,
    Service_offer_management_ServiceManagerResourceLink,
    Service_Manager_Management_BaseError,
    Service_offer_management_BadRequestError,
    Service_offer_management_NotFoundError,
    Service_offer_management_ServiceManagerProvisionPartialInfo,
    Service_offer_management_OperationalMode,
    Service_offer_management_ForbiddenError,
    Service_offer_management_ProvisionStatus,
    Service_offer_management_ServiceOfferStatus,
    Service_offer_management_RecentServices,
    Service_provision_management_MspConversionStatus,
    Service_offer_management_RecentService,
    Service_offer_management_ServiceManagerProvision,
    Service_offer_management_ConflictError,
    Service_Manager_Management_ServiceManagerProvisionCreateResponse,
    Service_Manager_Management_NotFoundError,
    Service_Manager_Management_ValidationError,
    Service_Manager_Management_ServiceManagerRead,
    Service_offer_management_ServiceOfferPartialDetails,
    Service_Manager_Management_Error,
    Service_provision_management_ServiceProvision,
    Service_offer_management_ServiceOfferResourceLink,
    Service_offer_management_RecentServiceV2,
    Service_offer_management_RegionalProvision,
    Service_offer_management_DetailedServiceManagerResourceLink,
    Service_offer_management_WorkspaceTransferStatus,
    Service_offer_management_TooManyRequestsError,
    Service_offer_management_DetailedServiceOffer,
    Service_offer_management_CategoryWithServiceOffers,
    Service_provision_management_ServiceProvisionList,
    Service_offer_management_ServiceOfferMediaVideoDetails,
    Service_offer_management_SupportedFeature,
    Service_provision_management_ConflictError,
    Service_provision_management_NotFoundError,
    Service_offer_management_ServiceOfferList,
    Service_Manager_Management_ServiceManagersPerRegion,
    Service_offer_management_ServiceOfferMediaImageDetails,
    Service_offer_management_RegionWithDetailedProvisions,
    Service_Manager_Management_ServiceManagerReadList,
    Service_offer_management_FeaturedServiceOffers,
    Service_provision_management_PreConditionFailedError,
    Service_offer_management_DetailedProvision,
    Service_offer_management_ServiceOfferWithAvailableRegions,
    Service_offer_management_ValidationError,
    Service_provision_management_ServiceProvisionCreateBase,
    Service_offer_management_ServiceOfferCatalog,
    Service_provision_management_ForbiddenError,
    Service_offer_management_ServiceOfferRegionsList,
    Service_offer_management_ServiceProvisionPartialInfo,
    Service_provision_management_WorkspaceResourceLink,
    Service_provision_management_ServiceManagerProvisionResourceLink,
    Service_Manager_Management_ProvisionStatus,
    Service_offer_management_InternalError,
    Service_provision_management_InternalError,
    Service_Manager_Management_BadRequestError,
    Service_offer_management_ServiceOfferReadWithMedia,
    Service_provision_management_BaseError,
    Service_Manager_Management_ServiceManagerProvisionRead,
    Service_offer_management_Category,
    Service_provision_management_ValidationError,
    Service_Manager_Management_UnauthorizedError,
    Service_provision_management_Error,
    Service_offer_management_ServiceProvision,
    Service_provision_management_AccountType,
    Service_offer_management_PreConditionFailedError,
    Service_Manager_Management_InternalError,
    Service_Manager_Management_ForbiddenError,
    Service_offer_management_RegionWithLocations,
    Service_offer_management_UnauthorizedError,
    Service_provision_management_BadRequestError,
    Service_offer_management_ServiceManagerProvisionResourceLink,
    Service_offer_management_MSPConversionStatus,
    Service_Manager_Management_ServiceManagerProvisionReadList,
    Service_offer_management_WorkspaceResourceLink,
    Service_offer_management_ServiceOfferRead,
    Service_offer_management_WorkspaceOpMode,
    Service_provision_management_WorkspaceTransferStatus,
    Service_offer_management_ServiceOfferType,
    Service_Manager_Management_ServiceManagersForARegion,
    Service_offer_management_MyServices,
    Service_provision_management_ServiceManagerResourceLink,
    Service_provision_management_OperationalMode,
    Service_provision_management_UnauthorizedError,
    Service_Manager_Management_ConflictError,
    Service_provision_management_ProvisionStatus,
    Service_offer_management_RecentServicesV2,
    Service_offer_management_ServiceOfferRegionRead,
    Service_offer_management_CategoryWithFeaturedServiceOffers,
    Service_provision_management_ServiceOfferResourceLink,
    Service_Manager_Management_ServiceManagerResourceLink,
    Service_offer_management_WorkspaceTypes,
    Service_offer_management_ServiceOfferPartialInfo,
    Service_Manager_Management_ServiceManagerProvisionCreateBase,
)

MODEL_TEST_MATRIX = [
    {
        "model": Service_Manager_Management_PreConditionFailedError,
        "name": "Service_Manager_Management_PreConditionFailedError",
        "fields": [
            {
                "name": "message",
                "sanitized": "message",
                "type": r"string",
                "required": True,
            },
            {
                "name": "debugId",
                "sanitized": "debugId",
                "type": r"string",
                "required": True,
            },
            {
                "name": "errorCode",
                "sanitized": "errorCode",
                "type": r"string",
                "required": True,
            },
            {
                "name": "httpStatusCode",
                "sanitized": "httpStatusCode",
                "type": r"integer",
                "required": True,
            },
        ],
    },
    {
        "model": Service_Manager_Management_MSPConversionStatus,
        "name": "Service_Manager_Management_MSPConversionStatus",
        "fields": [],
    },
    {
        "model": Service_offer_management_Region,
        "name": "Service_offer_management_Region",
        "fields": [
            {
                "name": "name",
                "sanitized": "name",
                "type": r"string",
                "required": False,
            },
            {
                "name": "type",
                "sanitized": "type",
                "type": r"string",
                "required": False,
            },
            {
                "name": "id",
                "sanitized": "id",
                "type": r"string",
                "required": False,
            },
        ],
    },
    {
        "model": Service_offer_management_ServiceManagerResourceLink,
        "name": "Service_offer_management_ServiceManagerResourceLink",
        "fields": [
            {
                "name": "id",
                "sanitized": "id",
                "type": r"string",
                "required": False,
            },
            {
                "name": "resourceUri",
                "sanitized": "resourceUri",
                "type": r"string",
                "required": False,
            },
        ],
    },
    {
        "model": Service_Manager_Management_BaseError,
        "name": "Service_Manager_Management_BaseError",
        "fields": [
            {
                "name": "debugId",
                "sanitized": "debugId",
                "type": r"string",
                "required": True,
            },
            {
                "name": "errorCode",
                "sanitized": "errorCode",
                "type": r"string",
                "required": True,
            },
            {
                "name": "httpStatusCode",
                "sanitized": "httpStatusCode",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "message",
                "sanitized": "message",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": Service_offer_management_BadRequestError,
        "name": "Service_offer_management_BadRequestError",
        "fields": [
            {
                "name": "errorCode",
                "sanitized": "errorCode",
                "type": r"string",
                "required": True,
            },
            {
                "name": "errorDetails",
                "sanitized": "errorDetails",
                "type": r"array",
                "required": True,
            },
            {
                "name": "httpStatusCode",
                "sanitized": "httpStatusCode",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "message",
                "sanitized": "message",
                "type": r"string",
                "required": True,
            },
            {
                "name": "debugId",
                "sanitized": "debugId",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": Service_offer_management_NotFoundError,
        "name": "Service_offer_management_NotFoundError",
        "fields": [
            {
                "name": "errorDetails",
                "sanitized": "errorDetails",
                "type": r"array",
                "required": False,
            },
            {
                "name": "httpStatusCode",
                "sanitized": "httpStatusCode",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "message",
                "sanitized": "message",
                "type": r"string",
                "required": True,
            },
            {
                "name": "debugId",
                "sanitized": "debugId",
                "type": r"string",
                "required": True,
            },
            {
                "name": "errorCode",
                "sanitized": "errorCode",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": Service_offer_management_ServiceManagerProvisionPartialInfo,
        "name": "Service_offer_management_ServiceManagerProvisionPartialInfo",
        "fields": [
            {
                "name": "region",
                "sanitized": "region",
                "type": r"string",
                "required": True,
            },
            {
                "name": "resourceUri",
                "sanitized": "resourceUri",
                "type": r"string",
                "required": True,
            },
            {
                "name": "serviceManagerInstanceId",
                "sanitized": "serviceManagerInstanceId",
                "type": r"string",
                "required": True,
            },
            {
                "name": "updatedAt",
                "sanitized": "updatedAt",
                "type": r"string",
                "required": False,
            },
            {
                "name": "createdAt",
                "sanitized": "createdAt",
                "type": r"string",
                "required": False,
            },
            {
                "name": "createdBy",
                "sanitized": "createdBy",
                "type": r"string",
                "required": False,
            },
            {
                "name": "generation",
                "sanitized": "generation",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "id",
                "sanitized": "id",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": Service_offer_management_OperationalMode,
        "name": "Service_offer_management_OperationalMode",
        "fields": [],
    },
    {
        "model": Service_offer_management_ForbiddenError,
        "name": "Service_offer_management_ForbiddenError",
        "fields": [
            {
                "name": "httpStatusCode",
                "sanitized": "httpStatusCode",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "message",
                "sanitized": "message",
                "type": r"string",
                "required": True,
            },
            {
                "name": "debugId",
                "sanitized": "debugId",
                "type": r"string",
                "required": True,
            },
            {
                "name": "errorCode",
                "sanitized": "errorCode",
                "type": r"string",
                "required": True,
            },
            {
                "name": "errorDetails",
                "sanitized": "errorDetails",
                "type": r"array",
                "required": False,
            },
        ],
    },
    {
        "model": Service_offer_management_ProvisionStatus,
        "name": "Service_offer_management_ProvisionStatus",
        "fields": [],
    },
    {
        "model": Service_offer_management_ServiceOfferStatus,
        "name": "Service_offer_management_ServiceOfferStatus",
        "fields": [],
    },
    {
        "model": Service_offer_management_RecentServices,
        "name": "Service_offer_management_RecentServices",
        "fields": [
            {
                "name": "total",
                "sanitized": "total",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "count",
                "sanitized": "count",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "items",
                "sanitized": "items",
                "type": r"array",
                "required": True,
            },
            {
                "name": "next",
                "sanitized": "next",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": Service_provision_management_MspConversionStatus,
        "name": "Service_provision_management_MspConversionStatus",
        "fields": [],
    },
    {
        "model": Service_offer_management_RecentService,
        "name": "Service_offer_management_RecentService",
        "fields": [
            {
                "name": "type",
                "sanitized": "type",
                "type": r"string",
                "required": True,
            },
            {
                "name": "id",
                "sanitized": "id",
                "type": r"string",
                "required": True,
            },
            {
                "name": "lastAccessedTime",
                "sanitized": "lastAccessedTime",
                "type": r"string",
                "required": False,
            },
            {
                "name": "regionalProvisions",
                "sanitized": "regionalProvisions",
                "type": r"array",
                "required": False,
            },
            {
                "name": "serviceOffer",
                "sanitized": "serviceOffer",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": Service_offer_management_ServiceManagerProvision,
        "name": "Service_offer_management_ServiceManagerProvision",
        "fields": [
            {
                "name": "reason",
                "sanitized": "reason",
                "type": r"string",
                "required": True,
            },
            {
                "name": "serviceManager",
                "sanitized": "serviceManager",
                "type": r"object",
                "required": True,
            },
            {
                "name": "provisionStatus",
                "sanitized": "provisionStatus",
                "type": r"string",
                "required": True,
            },
            {
                "name": "createdAt",
                "sanitized": "createdAt",
                "type": r"string",
                "required": True,
            },
            {
                "name": "workspaceTransferStatus",
                "sanitized": "workspaceTransferStatus",
                "type": r"string",
                "required": False,
            },
            {
                "name": "id",
                "sanitized": "id",
                "type": r"string",
                "required": True,
            },
            {
                "name": "region",
                "sanitized": "region",
                "type": r"string",
                "required": True,
            },
            {
                "name": "updatedAt",
                "sanitized": "updatedAt",
                "type": r"string",
                "required": True,
            },
            {
                "name": "generation",
                "sanitized": "generation",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "resourceUri",
                "sanitized": "resourceUri",
                "type": r"string",
                "required": True,
            },
            {
                "name": "serviceManagerInstanceId",
                "sanitized": "serviceManagerInstanceId",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": Service_offer_management_ConflictError,
        "name": "Service_offer_management_ConflictError",
        "fields": [
            {
                "name": "debugId",
                "sanitized": "debugId",
                "type": r"string",
                "required": True,
            },
            {
                "name": "errorCode",
                "sanitized": "errorCode",
                "type": r"string",
                "required": True,
            },
            {
                "name": "errorDetails",
                "sanitized": "errorDetails",
                "type": r"array",
                "required": False,
            },
            {
                "name": "httpStatusCode",
                "sanitized": "httpStatusCode",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "message",
                "sanitized": "message",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": Service_Manager_Management_ServiceManagerProvisionCreateResponse,
        "name": "Service_Manager_Management_ServiceManagerProvisionCreateResponse",
        "fields": [
            {
                "name": "createdBy",
                "sanitized": "createdBy",
                "type": r"string",
                "required": True,
            },
            {
                "name": "generation",
                "sanitized": "generation",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "id",
                "sanitized": "id",
                "type": r"string",
                "required": True,
            },
            {
                "name": "region",
                "sanitized": "region",
                "type": r"string",
                "required": True,
            },
            {
                "name": "resourceUri",
                "sanitized": "resourceUri",
                "type": r"string",
                "required": True,
            },
            {
                "name": "serviceManager",
                "sanitized": "serviceManager",
                "type": r"object",
                "required": True,
            },
            {
                "name": "type",
                "sanitized": "type",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": Service_Manager_Management_NotFoundError,
        "name": "Service_Manager_Management_NotFoundError",
        "fields": [
            {
                "name": "httpStatusCode",
                "sanitized": "httpStatusCode",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "message",
                "sanitized": "message",
                "type": r"string",
                "required": True,
            },
            {
                "name": "debugId",
                "sanitized": "debugId",
                "type": r"string",
                "required": True,
            },
            {
                "name": "errorCode",
                "sanitized": "errorCode",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": Service_Manager_Management_ValidationError,
        "name": "Service_Manager_Management_ValidationError",
        "fields": [
            {
                "name": "debugId",
                "sanitized": "debugId",
                "type": r"string",
                "required": True,
            },
            {
                "name": "errorCode",
                "sanitized": "errorCode",
                "type": r"string",
                "required": True,
            },
            {
                "name": "httpStatusCode",
                "sanitized": "httpStatusCode",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "message",
                "sanitized": "message",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": Service_Manager_Management_ServiceManagerRead,
        "name": "Service_Manager_Management_ServiceManagerRead",
        "fields": [
            {
                "name": "updatedAt",
                "sanitized": "updatedAt",
                "type": r"string",
                "required": True,
            },
            {
                "name": "generation",
                "sanitized": "generation",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "createdAt",
                "sanitized": "createdAt",
                "type": r"string",
                "required": True,
            },
            {
                "name": "name",
                "sanitized": "name",
                "type": r"string",
                "required": True,
            },
            {
                "name": "standaloneSupported",
                "sanitized": "standaloneSupported",
                "type": r"boolean",
                "required": True,
            },
            {
                "name": "id",
                "sanitized": "id",
                "type": r"string",
                "required": True,
            },
            {
                "name": "tenantOnlySupported",
                "sanitized": "tenantOnlySupported",
                "type": r"boolean",
                "required": True,
            },
            {
                "name": "honorUnprovisionResponse",
                "sanitized": "honorUnprovisionResponse",
                "type": r"boolean",
                "required": True,
            },
            {
                "name": "mspSupported",
                "sanitized": "mspSupported",
                "type": r"boolean",
                "required": True,
            },
            {
                "name": "mspOnlySupported",
                "sanitized": "mspOnlySupported",
                "type": r"boolean",
                "required": False,
            },
            {
                "name": "type",
                "sanitized": "type",
                "type": r"string",
                "required": True,
            },
            {
                "name": "resourceUri",
                "sanitized": "resourceUri",
                "type": r"string",
                "required": True,
            },
            {
                "name": "workspaceTransferSupported",
                "sanitized": "workspaceTransferSupported",
                "type": r"boolean",
                "required": False,
            },
            {
                "name": "workspaceOpModesSupported",
                "sanitized": "workspaceOpModesSupported",
                "type": r"string",
                "required": False,
            },
            {
                "name": "description",
                "sanitized": "description",
                "type": r"string",
                "required": False,
            },
        ],
    },
    {
        "model": Service_offer_management_ServiceOfferPartialDetails,
        "name": "Service_offer_management_ServiceOfferPartialDetails",
        "fields": [
            {
                "name": "workspaceOpModes",
                "sanitized": "workspaceOpModes",
                "type": r"array",
                "required": True,
            },
            {
                "name": "workspaceTypes",
                "sanitized": "workspaceTypes",
                "type": r"array",
                "required": True,
            },
            {
                "name": "categories",
                "sanitized": "categories",
                "type": r"array",
                "required": True,
            },
            {
                "name": "id",
                "sanitized": "id",
                "type": r"string",
                "required": True,
            },
            {
                "name": "name",
                "sanitized": "name",
                "type": r"string",
                "required": True,
            },
            {
                "name": "resourceUri",
                "sanitized": "resourceUri",
                "type": r"string",
                "required": True,
            },
            {
                "name": "slug",
                "sanitized": "slug",
                "type": r"string",
                "required": True,
            },
            {
                "name": "staticLaunchUrl",
                "sanitized": "staticLaunchUrl",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": Service_Manager_Management_Error,
        "name": "Service_Manager_Management_Error",
        "fields": [
            {
                "name": "httpStatusCode",
                "sanitized": "httpStatusCode",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "message",
                "sanitized": "message",
                "type": r"string",
                "required": True,
            },
            {
                "name": "debugId",
                "sanitized": "debugId",
                "type": r"string",
                "required": True,
            },
            {
                "name": "errorCode",
                "sanitized": "errorCode",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": Service_provision_management_ServiceProvision,
        "name": "Service_provision_management_ServiceProvision",
        "fields": [
            {
                "name": "updatedAt",
                "sanitized": "updatedAt",
                "type": r"string",
                "required": True,
            },
            {
                "name": "serviceManagerInstanceId",
                "sanitized": "serviceManagerInstanceId",
                "type": r"string",
                "required": False,
            },
            {
                "name": "createdAt",
                "sanitized": "createdAt",
                "type": r"string",
                "required": True,
            },
            {
                "name": "createdBy",
                "sanitized": "createdBy",
                "type": r"string",
                "required": False,
            },
            {
                "name": "serviceOffer",
                "sanitized": "serviceOffer",
                "type": r"object",
                "required": True,
            },
            {
                "name": "generation",
                "sanitized": "generation",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "serviceManager",
                "sanitized": "serviceManager",
                "type": r"object",
                "required": False,
            },
            {
                "name": "retryCount",
                "sanitized": "retryCount",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "serviceManagerProvision",
                "sanitized": "serviceManagerProvision",
                "type": r"object",
                "required": False,
            },
            {
                "name": "id",
                "sanitized": "id",
                "type": r"string",
                "required": True,
            },
            {
                "name": "workspace",
                "sanitized": "workspace",
                "type": r"object",
                "required": True,
            },
            {
                "name": "type",
                "sanitized": "type",
                "type": r"string",
                "required": True,
            },
            {
                "name": "reason",
                "sanitized": "reason",
                "type": r"string",
                "required": False,
            },
            {
                "name": "provisionStatus",
                "sanitized": "provisionStatus",
                "type": r"string",
                "required": False,
            },
            {
                "name": "region",
                "sanitized": "region",
                "type": r"string",
                "required": True,
            },
            {
                "name": "resourceUri",
                "sanitized": "resourceUri",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": Service_offer_management_ServiceOfferResourceLink,
        "name": "Service_offer_management_ServiceOfferResourceLink",
        "fields": [
            {
                "name": "id",
                "sanitized": "id",
                "type": r"string",
                "required": False,
            },
            {
                "name": "resourceUri",
                "sanitized": "resourceUri",
                "type": r"string",
                "required": False,
            },
        ],
    },
    {
        "model": Service_offer_management_RecentServiceV2,
        "name": "Service_offer_management_RecentServiceV2",
        "fields": [
            {
                "name": "type",
                "sanitized": "type",
                "type": r"string",
                "required": True,
            },
            {
                "name": "id",
                "sanitized": "id",
                "type": r"string",
                "required": True,
            },
            {
                "name": "lastAccessedTime",
                "sanitized": "lastAccessedTime",
                "type": r"string",
                "required": True,
            },
            {
                "name": "region",
                "sanitized": "region",
                "type": r"string",
                "required": True,
            },
            {
                "name": "serviceManagerProvision",
                "sanitized": "serviceManagerProvision",
                "type": r"string",
                "required": False,
            },
            {
                "name": "serviceOffer",
                "sanitized": "serviceOffer",
                "type": r"string",
                "required": True,
            },
            {
                "name": "serviceProvision",
                "sanitized": "serviceProvision",
                "type": r"string",
                "required": False,
            },
        ],
    },
    {
        "model": Service_offer_management_RegionalProvision,
        "name": "Service_offer_management_RegionalProvision",
        "fields": [
            {
                "name": "id",
                "sanitized": "id",
                "type": r"string",
                "required": False,
            },
            {
                "name": "serviceManagerProvision",
                "sanitized": "serviceManagerProvision",
                "type": r"string",
                "required": False,
            },
            {
                "name": "serviceProvision",
                "sanitized": "serviceProvision",
                "type": r"string",
                "required": False,
            },
            {
                "name": "type",
                "sanitized": "type",
                "type": r"string",
                "required": False,
            },
        ],
    },
    {
        "model": Service_offer_management_DetailedServiceManagerResourceLink,
        "name": "Service_offer_management_DetailedServiceManagerResourceLink",
        "fields": [
            {
                "name": "id",
                "sanitized": "id",
                "type": r"string",
                "required": False,
            },
            {
                "name": "name",
                "sanitized": "name",
                "type": r"string",
                "required": False,
            },
            {
                "name": "resourceUri",
                "sanitized": "resourceUri",
                "type": r"string",
                "required": False,
            },
            {
                "name": "serviceOfferId",
                "sanitized": "serviceOfferId",
                "type": r"string",
                "required": False,
            },
        ],
    },
    {
        "model": Service_offer_management_WorkspaceTransferStatus,
        "name": "Service_offer_management_WorkspaceTransferStatus",
        "fields": [],
    },
    {
        "model": Service_offer_management_TooManyRequestsError,
        "name": "Service_offer_management_TooManyRequestsError",
        "fields": [
            {
                "name": "errorDetails",
                "sanitized": "errorDetails",
                "type": r"array",
                "required": False,
            },
            {
                "name": "httpStatusCode",
                "sanitized": "httpStatusCode",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "message",
                "sanitized": "message",
                "type": r"string",
                "required": True,
            },
            {
                "name": "debugId",
                "sanitized": "debugId",
                "type": r"string",
                "required": True,
            },
            {
                "name": "errorCode",
                "sanitized": "errorCode",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": Service_offer_management_DetailedServiceOffer,
        "name": "Service_offer_management_DetailedServiceOffer",
        "fields": [
            {
                "name": "id",
                "sanitized": "id",
                "type": r"string",
                "required": True,
            },
            {
                "name": "orgSingletonServiceProvisions",
                "sanitized": "orgSingletonServiceProvisions",
                "type": r"array",
                "required": True,
            },
            {
                "name": "provisions",
                "sanitized": "provisions",
                "type": r"array",
                "required": True,
            },
            {
                "name": "serviceManager",
                "sanitized": "serviceManager",
                "type": r"object",
                "required": False,
            },
            {
                "name": "serviceOffer",
                "sanitized": "serviceOffer",
                "type": r"string",
                "required": False,
            },
            {
                "name": "type",
                "sanitized": "type",
                "type": r"string",
                "required": True,
            },
            {
                "name": "availableRegions",
                "sanitized": "availableRegions",
                "type": r"array",
                "required": True,
            },
        ],
    },
    {
        "model": Service_offer_management_CategoryWithServiceOffers,
        "name": "Service_offer_management_CategoryWithServiceOffers",
        "fields": [
            {
                "name": "type",
                "sanitized": "type",
                "type": r"string",
                "required": True,
            },
            {
                "name": "id",
                "sanitized": "id",
                "type": r"string",
                "required": True,
            },
            {
                "name": "servicesWithRegions",
                "sanitized": "servicesWithRegions",
                "type": r"array",
                "required": True,
            },
        ],
    },
    {
        "model": Service_provision_management_ServiceProvisionList,
        "name": "Service_provision_management_ServiceProvisionList",
        "fields": [
            {
                "name": "count",
                "sanitized": "count",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "items",
                "sanitized": "items",
                "type": r"array",
                "required": True,
            },
            {
                "name": "next",
                "sanitized": "next",
                "type": r"string",
                "required": True,
            },
            {
                "name": "total",
                "sanitized": "total",
                "type": r"integer",
                "required": True,
            },
        ],
    },
    {
        "model": Service_offer_management_ServiceOfferMediaVideoDetails,
        "name": "Service_offer_management_ServiceOfferMediaVideoDetails",
        "fields": [
            {
                "name": "video",
                "sanitized": "video",
                "type": r"string",
                "required": True,
            },
            {
                "name": "description",
                "sanitized": "description",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": Service_offer_management_SupportedFeature,
        "name": "Service_offer_management_SupportedFeature",
        "fields": [],
    },
    {
        "model": Service_provision_management_ConflictError,
        "name": "Service_provision_management_ConflictError",
        "fields": [
            {
                "name": "debugId",
                "sanitized": "debugId",
                "type": r"string",
                "required": True,
            },
            {
                "name": "errorCode",
                "sanitized": "errorCode",
                "type": r"string",
                "required": True,
            },
            {
                "name": "httpStatusCode",
                "sanitized": "httpStatusCode",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "message",
                "sanitized": "message",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": Service_provision_management_NotFoundError,
        "name": "Service_provision_management_NotFoundError",
        "fields": [
            {
                "name": "debugId",
                "sanitized": "debugId",
                "type": r"string",
                "required": True,
            },
            {
                "name": "errorCode",
                "sanitized": "errorCode",
                "type": r"string",
                "required": True,
            },
            {
                "name": "httpStatusCode",
                "sanitized": "httpStatusCode",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "message",
                "sanitized": "message",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": Service_offer_management_ServiceOfferList,
        "name": "Service_offer_management_ServiceOfferList",
        "fields": [
            {
                "name": "count",
                "sanitized": "count",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "items",
                "sanitized": "items",
                "type": r"array",
                "required": True,
            },
            {
                "name": "next",
                "sanitized": "next",
                "type": r"string",
                "required": True,
            },
            {
                "name": "total",
                "sanitized": "total",
                "type": r"integer",
                "required": True,
            },
        ],
    },
    {
        "model": Service_Manager_Management_ServiceManagersPerRegion,
        "name": "Service_Manager_Management_ServiceManagersPerRegion",
        "fields": [
            {
                "name": "count",
                "sanitized": "count",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "items",
                "sanitized": "items",
                "type": r"array",
                "required": True,
            },
            {
                "name": "offset",
                "sanitized": "offset",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "total",
                "sanitized": "total",
                "type": r"integer",
                "required": False,
            },
        ],
    },
    {
        "model": Service_offer_management_ServiceOfferMediaImageDetails,
        "name": "Service_offer_management_ServiceOfferMediaImageDetails",
        "fields": [
            {
                "name": "image",
                "sanitized": "image",
                "type": r"string",
                "required": True,
            },
            {
                "name": "description",
                "sanitized": "description",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": Service_offer_management_RegionWithDetailedProvisions,
        "name": "Service_offer_management_RegionWithDetailedProvisions",
        "fields": [
            {
                "name": "id",
                "sanitized": "id",
                "type": r"string",
                "required": True,
            },
            {
                "name": "provisions",
                "sanitized": "provisions",
                "type": r"array",
                "required": True,
            },
            {
                "name": "type",
                "sanitized": "type",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": Service_Manager_Management_ServiceManagerReadList,
        "name": "Service_Manager_Management_ServiceManagerReadList",
        "fields": [
            {
                "name": "offset",
                "sanitized": "offset",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "total",
                "sanitized": "total",
                "type": r"integer",
                "required": False,
            },
            {
                "name": "count",
                "sanitized": "count",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "items",
                "sanitized": "items",
                "type": r"array",
                "required": True,
            },
        ],
    },
    {
        "model": Service_offer_management_FeaturedServiceOffers,
        "name": "Service_offer_management_FeaturedServiceOffers",
        "fields": [
            {
                "name": "items",
                "sanitized": "items",
                "type": r"array",
                "required": True,
            },
            {
                "name": "next",
                "sanitized": "next",
                "type": r"string",
                "required": True,
            },
            {
                "name": "total",
                "sanitized": "total",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "count",
                "sanitized": "count",
                "type": r"integer",
                "required": True,
            },
        ],
    },
    {
        "model": Service_provision_management_PreConditionFailedError,
        "name": "Service_provision_management_PreConditionFailedError",
        "fields": [
            {
                "name": "debugId",
                "sanitized": "debugId",
                "type": r"string",
                "required": True,
            },
            {
                "name": "errorCode",
                "sanitized": "errorCode",
                "type": r"string",
                "required": True,
            },
            {
                "name": "httpStatusCode",
                "sanitized": "httpStatusCode",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "message",
                "sanitized": "message",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": Service_offer_management_DetailedProvision,
        "name": "Service_offer_management_DetailedProvision",
        "fields": [
            {
                "name": "serviceManagerProvision",
                "sanitized": "serviceManagerProvision",
                "type": r"string",
                "required": False,
            },
            {
                "name": "serviceOffer",
                "sanitized": "serviceOffer",
                "type": r"string",
                "required": False,
            },
            {
                "name": "serviceProvision",
                "sanitized": "serviceProvision",
                "type": r"string",
                "required": False,
            },
        ],
    },
    {
        "model": Service_offer_management_ServiceOfferWithAvailableRegions,
        "name": "Service_offer_management_ServiceOfferWithAvailableRegions",
        "fields": [
            {
                "name": "availableRegions",
                "sanitized": "availableRegions",
                "type": r"array",
                "required": True,
            },
            {
                "name": "id",
                "sanitized": "id",
                "type": r"string",
                "required": False,
            },
            {
                "name": "serviceOffer",
                "sanitized": "serviceOffer",
                "type": r"object",
                "required": True,
            },
            {
                "name": "type",
                "sanitized": "type",
                "type": r"string",
                "required": False,
            },
        ],
    },
    {
        "model": Service_offer_management_ValidationError,
        "name": "Service_offer_management_ValidationError",
        "fields": [
            {
                "name": "httpStatusCode",
                "sanitized": "httpStatusCode",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "message",
                "sanitized": "message",
                "type": r"string",
                "required": True,
            },
            {
                "name": "debugId",
                "sanitized": "debugId",
                "type": r"string",
                "required": True,
            },
            {
                "name": "errorCode",
                "sanitized": "errorCode",
                "type": r"string",
                "required": True,
            },
            {
                "name": "errorDetails",
                "sanitized": "errorDetails",
                "type": r"array",
                "required": False,
            },
        ],
    },
    {
        "model": Service_provision_management_ServiceProvisionCreateBase,
        "name": "Service_provision_management_ServiceProvisionCreateBase",
        "fields": [
            {
                "name": "serviceOfferId",
                "sanitized": "serviceOfferId",
                "type": r"string",
                "required": True,
            },
            {
                "name": "region",
                "sanitized": "region",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": Service_offer_management_ServiceOfferCatalog,
        "name": "Service_offer_management_ServiceOfferCatalog",
        "fields": [
            {
                "name": "count",
                "sanitized": "count",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "items",
                "sanitized": "items",
                "type": r"array",
                "required": True,
            },
            {
                "name": "next",
                "sanitized": "next",
                "type": r"string",
                "required": True,
            },
            {
                "name": "total",
                "sanitized": "total",
                "type": r"integer",
                "required": True,
            },
        ],
    },
    {
        "model": Service_provision_management_ForbiddenError,
        "name": "Service_provision_management_ForbiddenError",
        "fields": [
            {
                "name": "errorCode",
                "sanitized": "errorCode",
                "type": r"string",
                "required": True,
            },
            {
                "name": "httpStatusCode",
                "sanitized": "httpStatusCode",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "message",
                "sanitized": "message",
                "type": r"string",
                "required": True,
            },
            {
                "name": "debugId",
                "sanitized": "debugId",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": Service_offer_management_ServiceOfferRegionsList,
        "name": "Service_offer_management_ServiceOfferRegionsList",
        "fields": [
            {
                "name": "next",
                "sanitized": "next",
                "type": r"string",
                "required": True,
            },
            {
                "name": "total",
                "sanitized": "total",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "count",
                "sanitized": "count",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "items",
                "sanitized": "items",
                "type": r"array",
                "required": True,
            },
        ],
    },
    {
        "model": Service_offer_management_ServiceProvisionPartialInfo,
        "name": "Service_offer_management_ServiceProvisionPartialInfo",
        "fields": [
            {
                "name": "id",
                "sanitized": "id",
                "type": r"string",
                "required": True,
            },
            {
                "name": "region",
                "sanitized": "region",
                "type": r"string",
                "required": True,
            },
            {
                "name": "resourceUri",
                "sanitized": "resourceUri",
                "type": r"string",
                "required": True,
            },
            {
                "name": "serviceManagerInstanceId",
                "sanitized": "serviceManagerInstanceId",
                "type": r"string",
                "required": True,
            },
            {
                "name": "updatedAt",
                "sanitized": "updatedAt",
                "type": r"string",
                "required": False,
            },
            {
                "name": "createdAt",
                "sanitized": "createdAt",
                "type": r"string",
                "required": False,
            },
            {
                "name": "createdBy",
                "sanitized": "createdBy",
                "type": r"string",
                "required": False,
            },
            {
                "name": "generation",
                "sanitized": "generation",
                "type": r"integer",
                "required": True,
            },
        ],
    },
    {
        "model": Service_provision_management_WorkspaceResourceLink,
        "name": "Service_provision_management_WorkspaceResourceLink",
        "fields": [
            {
                "name": "workspaceTransferStatus",
                "sanitized": "workspaceTransferStatus",
                "type": r"string",
                "required": False,
            },
            {
                "name": "id",
                "sanitized": "id",
                "type": r"string",
                "required": False,
            },
            {
                "name": "mspId",
                "sanitized": "mspId",
                "type": r"string",
                "required": False,
            },
            {
                "name": "name",
                "sanitized": "name",
                "type": r"string",
                "required": False,
            },
            {
                "name": "organizationId",
                "sanitized": "organizationId",
                "type": r"string",
                "required": False,
            },
            {
                "name": "resourceUri",
                "sanitized": "resourceUri",
                "type": r"string",
                "required": False,
            },
        ],
    },
    {
        "model": Service_provision_management_ServiceManagerProvisionResourceLink,
        "name": "Service_provision_management_ServiceManagerProvisionResourceLink",
        "fields": [
            {
                "name": "accountType",
                "sanitized": "accountType",
                "type": r"string",
                "required": False,
            },
            {
                "name": "id",
                "sanitized": "id",
                "type": r"string",
                "required": False,
            },
            {
                "name": "mspConversionStatus",
                "sanitized": "mspConversionStatus",
                "type": r"string",
                "required": False,
            },
            {
                "name": "operationalMode",
                "sanitized": "operationalMode",
                "type": r"string",
                "required": False,
            },
            {
                "name": "provisionStatus",
                "sanitized": "provisionStatus",
                "type": r"string",
                "required": False,
            },
            {
                "name": "reason",
                "sanitized": "reason",
                "type": r"string",
                "required": False,
            },
            {
                "name": "resourceUri",
                "sanitized": "resourceUri",
                "type": r"string",
                "required": False,
            },
        ],
    },
    {
        "model": Service_Manager_Management_ProvisionStatus,
        "name": "Service_Manager_Management_ProvisionStatus",
        "fields": [],
    },
    {
        "model": Service_offer_management_InternalError,
        "name": "Service_offer_management_InternalError",
        "fields": [
            {
                "name": "debugId",
                "sanitized": "debugId",
                "type": r"string",
                "required": True,
            },
            {
                "name": "errorCode",
                "sanitized": "errorCode",
                "type": r"string",
                "required": True,
            },
            {
                "name": "errorDetails",
                "sanitized": "errorDetails",
                "type": r"array",
                "required": True,
            },
            {
                "name": "httpStatusCode",
                "sanitized": "httpStatusCode",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "message",
                "sanitized": "message",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": Service_provision_management_InternalError,
        "name": "Service_provision_management_InternalError",
        "fields": [
            {
                "name": "debugId",
                "sanitized": "debugId",
                "type": r"string",
                "required": True,
            },
            {
                "name": "errorCode",
                "sanitized": "errorCode",
                "type": r"string",
                "required": True,
            },
            {
                "name": "errorDetails",
                "sanitized": "errorDetails",
                "type": r"array",
                "required": False,
            },
            {
                "name": "httpStatusCode",
                "sanitized": "httpStatusCode",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "message",
                "sanitized": "message",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": Service_Manager_Management_BadRequestError,
        "name": "Service_Manager_Management_BadRequestError",
        "fields": [
            {
                "name": "httpStatusCode",
                "sanitized": "httpStatusCode",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "message",
                "sanitized": "message",
                "type": r"string",
                "required": True,
            },
            {
                "name": "debugId",
                "sanitized": "debugId",
                "type": r"string",
                "required": True,
            },
            {
                "name": "errorCode",
                "sanitized": "errorCode",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": Service_offer_management_ServiceOfferReadWithMedia,
        "name": "Service_offer_management_ServiceOfferReadWithMedia",
        "fields": [
            {
                "name": "id",
                "sanitized": "id",
                "type": r"string",
                "required": True,
            },
            {
                "name": "capabilities",
                "sanitized": "capabilities",
                "type": r"array",
                "required": True,
            },
            {
                "name": "termsOfServiceUrl",
                "sanitized": "termsOfServiceUrl",
                "type": r"string",
                "required": True,
            },
            {
                "name": "createdAt",
                "sanitized": "createdAt",
                "type": r"string",
                "required": True,
            },
            {
                "name": "preProvisionMessage",
                "sanitized": "preProvisionMessage",
                "type": r"string",
                "required": True,
            },
            {
                "name": "languagesSupported",
                "sanitized": "languagesSupported",
                "type": r"array",
                "required": True,
            },
            {
                "name": "documentationUrl",
                "sanitized": "documentationUrl",
                "type": r"string",
                "required": True,
            },
            {
                "name": "resourceUri",
                "sanitized": "resourceUri",
                "type": r"string",
                "required": True,
            },
            {
                "name": "screenshots",
                "sanitized": "screenshots",
                "type": r"array",
                "required": True,
            },
            {
                "name": "videos",
                "sanitized": "videos",
                "type": r"array",
                "required": True,
            },
            {
                "name": "serviceManager",
                "sanitized": "serviceManager",
                "type": r"object",
                "required": True,
            },
            {
                "name": "brokerUri",
                "sanitized": "brokerUri",
                "type": r"string",
                "required": True,
            },
            {
                "name": "featuresSupported",
                "sanitized": "featuresSupported",
                "type": r"array",
                "required": True,
            },
            {
                "name": "staticLaunchUrl",
                "sanitized": "staticLaunchUrl",
                "type": r"string",
                "required": True,
            },
            {
                "name": "testDriveUrl",
                "sanitized": "testDriveUrl",
                "type": r"string",
                "required": True,
            },
            {
                "name": "evalUrl",
                "sanitized": "evalUrl",
                "type": r"string",
                "required": True,
            },
            {
                "name": "workspaceTypes",
                "sanitized": "workspaceTypes",
                "type": r"string",
                "required": True,
            },
            {
                "name": "updatedAt",
                "sanitized": "updatedAt",
                "type": r"string",
                "required": False,
            },
            {
                "name": "name",
                "sanitized": "name",
                "type": r"string",
                "required": True,
            },
            {
                "name": "overview",
                "sanitized": "overview",
                "type": r"string",
                "required": True,
            },
            {
                "name": "status",
                "sanitized": "status",
                "type": r"string",
                "required": True,
            },
            {
                "name": "logo",
                "sanitized": "logo",
                "type": r"string",
                "required": True,
            },
            {
                "name": "generation",
                "sanitized": "generation",
                "type": r"string",
                "required": False,
            },
            {
                "name": "shortDescription",
                "sanitized": "shortDescription",
                "type": r"string",
                "required": True,
            },
            {
                "name": "serviceOfferType",
                "sanitized": "serviceOfferType",
                "type": r"string",
                "required": True,
            },
            {
                "name": "slug",
                "sanitized": "slug",
                "type": r"string",
                "required": True,
            },
            {
                "name": "categories",
                "sanitized": "categories",
                "type": r"array",
                "required": True,
            },
            {
                "name": "contactSalesUrl",
                "sanitized": "contactSalesUrl",
                "type": r"string",
                "required": True,
            },
            {
                "name": "isDefault",
                "sanitized": "isDefault",
                "type": r"string",
                "required": False,
            },
        ],
    },
    {
        "model": Service_provision_management_BaseError,
        "name": "Service_provision_management_BaseError",
        "fields": [
            {
                "name": "errorCode",
                "sanitized": "errorCode",
                "type": r"string",
                "required": True,
            },
            {
                "name": "httpStatusCode",
                "sanitized": "httpStatusCode",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "message",
                "sanitized": "message",
                "type": r"string",
                "required": True,
            },
            {
                "name": "debugId",
                "sanitized": "debugId",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": Service_Manager_Management_ServiceManagerProvisionRead,
        "name": "Service_Manager_Management_ServiceManagerProvisionRead",
        "fields": [
            {
                "name": "serviceManager",
                "sanitized": "serviceManager",
                "type": r"object",
                "required": True,
            },
            {
                "name": "id",
                "sanitized": "id",
                "type": r"string",
                "required": True,
            },
            {
                "name": "updatedAt",
                "sanitized": "updatedAt",
                "type": r"string",
                "required": True,
            },
            {
                "name": "createdBy",
                "sanitized": "createdBy",
                "type": r"string",
                "required": True,
            },
            {
                "name": "resourceUri",
                "sanitized": "resourceUri",
                "type": r"string",
                "required": True,
            },
            {
                "name": "type",
                "sanitized": "type",
                "type": r"string",
                "required": True,
            },
            {
                "name": "createdAt",
                "sanitized": "createdAt",
                "type": r"string",
                "required": True,
            },
            {
                "name": "region",
                "sanitized": "region",
                "type": r"string",
                "required": True,
            },
            {
                "name": "generation",
                "sanitized": "generation",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "provisionStatus",
                "sanitized": "provisionStatus",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": Service_offer_management_Category,
        "name": "Service_offer_management_Category",
        "fields": [],
    },
    {
        "model": Service_provision_management_ValidationError,
        "name": "Service_provision_management_ValidationError",
        "fields": [
            {
                "name": "errorCode",
                "sanitized": "errorCode",
                "type": r"string",
                "required": True,
            },
            {
                "name": "httpStatusCode",
                "sanitized": "httpStatusCode",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "message",
                "sanitized": "message",
                "type": r"string",
                "required": True,
            },
            {
                "name": "debugId",
                "sanitized": "debugId",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": Service_Manager_Management_UnauthorizedError,
        "name": "Service_Manager_Management_UnauthorizedError",
        "fields": [
            {
                "name": "debugId",
                "sanitized": "debugId",
                "type": r"string",
                "required": True,
            },
            {
                "name": "errorCode",
                "sanitized": "errorCode",
                "type": r"string",
                "required": True,
            },
            {
                "name": "httpStatusCode",
                "sanitized": "httpStatusCode",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "message",
                "sanitized": "message",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": Service_provision_management_Error,
        "name": "Service_provision_management_Error",
        "fields": [
            {
                "name": "debugId",
                "sanitized": "debugId",
                "type": r"string",
                "required": True,
            },
            {
                "name": "errorCode",
                "sanitized": "errorCode",
                "type": r"string",
                "required": True,
            },
            {
                "name": "httpStatusCode",
                "sanitized": "httpStatusCode",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "message",
                "sanitized": "message",
                "type": r"string",
                "required": True,
            },
            {
                "name": "errorDetails",
                "sanitized": "errorDetails",
                "type": r"array",
                "required": False,
            },
        ],
    },
    {
        "model": Service_offer_management_ServiceProvision,
        "name": "Service_offer_management_ServiceProvision",
        "fields": [
            {
                "name": "provisionStatus",
                "sanitized": "provisionStatus",
                "type": r"string",
                "required": False,
            },
            {
                "name": "reason",
                "sanitized": "reason",
                "type": r"string",
                "required": False,
            },
            {
                "name": "serviceManagerInstanceId",
                "sanitized": "serviceManagerInstanceId",
                "type": r"string",
                "required": False,
            },
            {
                "name": "createdBy",
                "sanitized": "createdBy",
                "type": r"string",
                "required": False,
            },
            {
                "name": "resourceUri",
                "sanitized": "resourceUri",
                "type": r"string",
                "required": True,
            },
            {
                "name": "serviceManager",
                "sanitized": "serviceManager",
                "type": r"object",
                "required": False,
            },
            {
                "name": "serviceManagerProvision",
                "sanitized": "serviceManagerProvision",
                "type": r"object",
                "required": False,
            },
            {
                "name": "workspace",
                "sanitized": "workspace",
                "type": r"object",
                "required": True,
            },
            {
                "name": "updatedAt",
                "sanitized": "updatedAt",
                "type": r"string",
                "required": False,
            },
            {
                "name": "createdAt",
                "sanitized": "createdAt",
                "type": r"string",
                "required": False,
            },
            {
                "name": "region",
                "sanitized": "region",
                "type": r"string",
                "required": True,
            },
            {
                "name": "generation",
                "sanitized": "generation",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "id",
                "sanitized": "id",
                "type": r"string",
                "required": True,
            },
            {
                "name": "serviceOffer",
                "sanitized": "serviceOffer",
                "type": r"object",
                "required": True,
            },
        ],
    },
    {
        "model": Service_provision_management_AccountType,
        "name": "Service_provision_management_AccountType",
        "fields": [],
    },
    {
        "model": Service_offer_management_PreConditionFailedError,
        "name": "Service_offer_management_PreConditionFailedError",
        "fields": [
            {
                "name": "errorDetails",
                "sanitized": "errorDetails",
                "type": r"array",
                "required": True,
            },
            {
                "name": "httpStatusCode",
                "sanitized": "httpStatusCode",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "message",
                "sanitized": "message",
                "type": r"string",
                "required": True,
            },
            {
                "name": "debugId",
                "sanitized": "debugId",
                "type": r"string",
                "required": True,
            },
            {
                "name": "errorCode",
                "sanitized": "errorCode",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": Service_Manager_Management_InternalError,
        "name": "Service_Manager_Management_InternalError",
        "fields": [
            {
                "name": "debugId",
                "sanitized": "debugId",
                "type": r"string",
                "required": True,
            },
            {
                "name": "errorCode",
                "sanitized": "errorCode",
                "type": r"string",
                "required": True,
            },
            {
                "name": "httpStatusCode",
                "sanitized": "httpStatusCode",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "message",
                "sanitized": "message",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": Service_Manager_Management_ForbiddenError,
        "name": "Service_Manager_Management_ForbiddenError",
        "fields": [
            {
                "name": "debugId",
                "sanitized": "debugId",
                "type": r"string",
                "required": True,
            },
            {
                "name": "errorCode",
                "sanitized": "errorCode",
                "type": r"string",
                "required": True,
            },
            {
                "name": "httpStatusCode",
                "sanitized": "httpStatusCode",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "message",
                "sanitized": "message",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": Service_offer_management_RegionWithLocations,
        "name": "Service_offer_management_RegionWithLocations",
        "fields": [
            {
                "name": "type",
                "sanitized": "type",
                "type": r"string",
                "required": False,
            },
            {
                "name": "id",
                "sanitized": "id",
                "type": r"string",
                "required": False,
            },
            {
                "name": "name",
                "sanitized": "name",
                "type": r"string",
                "required": False,
            },
            {
                "name": "locations",
                "sanitized": "locations",
                "type": r"array",
                "required": False,
            },
        ],
    },
    {
        "model": Service_offer_management_UnauthorizedError,
        "name": "Service_offer_management_UnauthorizedError",
        "fields": [
            {
                "name": "debugId",
                "sanitized": "debugId",
                "type": r"string",
                "required": True,
            },
            {
                "name": "errorCode",
                "sanitized": "errorCode",
                "type": r"string",
                "required": True,
            },
            {
                "name": "errorDetails",
                "sanitized": "errorDetails",
                "type": r"array",
                "required": False,
            },
            {
                "name": "httpStatusCode",
                "sanitized": "httpStatusCode",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "message",
                "sanitized": "message",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": Service_provision_management_BadRequestError,
        "name": "Service_provision_management_BadRequestError",
        "fields": [
            {
                "name": "message",
                "sanitized": "message",
                "type": r"string",
                "required": True,
            },
            {
                "name": "debugId",
                "sanitized": "debugId",
                "type": r"string",
                "required": True,
            },
            {
                "name": "errorCode",
                "sanitized": "errorCode",
                "type": r"string",
                "required": True,
            },
            {
                "name": "errorDetails",
                "sanitized": "errorDetails",
                "type": r"array",
                "required": True,
            },
            {
                "name": "httpStatusCode",
                "sanitized": "httpStatusCode",
                "type": r"integer",
                "required": True,
            },
        ],
    },
    {
        "model": Service_offer_management_ServiceManagerProvisionResourceLink,
        "name": "Service_offer_management_ServiceManagerProvisionResourceLink",
        "fields": [
            {
                "name": "id",
                "sanitized": "id",
                "type": r"string",
                "required": False,
            },
            {
                "name": "resourceUri",
                "sanitized": "resourceUri",
                "type": r"string",
                "required": False,
            },
        ],
    },
    {
        "model": Service_offer_management_MSPConversionStatus,
        "name": "Service_offer_management_MSPConversionStatus",
        "fields": [],
    },
    {
        "model": Service_Manager_Management_ServiceManagerProvisionReadList,
        "name": "Service_Manager_Management_ServiceManagerProvisionReadList",
        "fields": [
            {
                "name": "offset",
                "sanitized": "offset",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "total",
                "sanitized": "total",
                "type": r"integer",
                "required": False,
            },
            {
                "name": "count",
                "sanitized": "count",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "items",
                "sanitized": "items",
                "type": r"array",
                "required": True,
            },
        ],
    },
    {
        "model": Service_offer_management_WorkspaceResourceLink,
        "name": "Service_offer_management_WorkspaceResourceLink",
        "fields": [
            {
                "name": "organizationId",
                "sanitized": "organizationId",
                "type": r"string",
                "required": False,
            },
            {
                "name": "resourceUri",
                "sanitized": "resourceUri",
                "type": r"string",
                "required": False,
            },
            {
                "name": "workspaceTransferStatus",
                "sanitized": "workspaceTransferStatus",
                "type": r"string",
                "required": False,
            },
            {
                "name": "id",
                "sanitized": "id",
                "type": r"string",
                "required": False,
            },
            {
                "name": "name",
                "sanitized": "name",
                "type": r"string",
                "required": False,
            },
        ],
    },
    {
        "model": Service_offer_management_ServiceOfferRead,
        "name": "Service_offer_management_ServiceOfferRead",
        "fields": [
            {
                "name": "termsOfServiceUrl",
                "sanitized": "termsOfServiceUrl",
                "type": r"string",
                "required": True,
            },
            {
                "name": "shortDescription",
                "sanitized": "shortDescription",
                "type": r"string",
                "required": True,
            },
            {
                "name": "capabilities",
                "sanitized": "capabilities",
                "type": r"array",
                "required": True,
            },
            {
                "name": "overview",
                "sanitized": "overview",
                "type": r"string",
                "required": True,
            },
            {
                "name": "resourceUri",
                "sanitized": "resourceUri",
                "type": r"string",
                "required": True,
            },
            {
                "name": "categories",
                "sanitized": "categories",
                "type": r"array",
                "required": True,
            },
            {
                "name": "documentationUrl",
                "sanitized": "documentationUrl",
                "type": r"string",
                "required": True,
            },
            {
                "name": "status",
                "sanitized": "status",
                "type": r"string",
                "required": True,
            },
            {
                "name": "preProvisionMessage",
                "sanitized": "preProvisionMessage",
                "type": r"string",
                "required": True,
            },
            {
                "name": "testDriveUrl",
                "sanitized": "testDriveUrl",
                "type": r"string",
                "required": True,
            },
            {
                "name": "generation",
                "sanitized": "generation",
                "type": r"string",
                "required": False,
            },
            {
                "name": "id",
                "sanitized": "id",
                "type": r"string",
                "required": True,
            },
            {
                "name": "contactSalesUrl",
                "sanitized": "contactSalesUrl",
                "type": r"string",
                "required": True,
            },
            {
                "name": "isDefault",
                "sanitized": "isDefault",
                "type": r"string",
                "required": False,
            },
            {
                "name": "name",
                "sanitized": "name",
                "type": r"string",
                "required": True,
            },
            {
                "name": "createdAt",
                "sanitized": "createdAt",
                "type": r"string",
                "required": True,
            },
            {
                "name": "serviceManager",
                "sanitized": "serviceManager",
                "type": r"object",
                "required": True,
            },
            {
                "name": "serviceOfferType",
                "sanitized": "serviceOfferType",
                "type": r"string",
                "required": True,
            },
            {
                "name": "evalUrl",
                "sanitized": "evalUrl",
                "type": r"string",
                "required": True,
            },
            {
                "name": "brokerUri",
                "sanitized": "brokerUri",
                "type": r"string",
                "required": True,
            },
            {
                "name": "staticLaunchUrl",
                "sanitized": "staticLaunchUrl",
                "type": r"string",
                "required": True,
            },
            {
                "name": "languagesSupported",
                "sanitized": "languagesSupported",
                "type": r"array",
                "required": True,
            },
            {
                "name": "slug",
                "sanitized": "slug",
                "type": r"string",
                "required": True,
            },
            {
                "name": "featuresSupported",
                "sanitized": "featuresSupported",
                "type": r"array",
                "required": True,
            },
            {
                "name": "updatedAt",
                "sanitized": "updatedAt",
                "type": r"string",
                "required": False,
            },
        ],
    },
    {
        "model": Service_offer_management_WorkspaceOpMode,
        "name": "Service_offer_management_WorkspaceOpMode",
        "fields": [],
    },
    {
        "model": Service_provision_management_WorkspaceTransferStatus,
        "name": "Service_provision_management_WorkspaceTransferStatus",
        "fields": [],
    },
    {
        "model": Service_offer_management_ServiceOfferType,
        "name": "Service_offer_management_ServiceOfferType",
        "fields": [],
    },
    {
        "model": Service_Manager_Management_ServiceManagersForARegion,
        "name": "Service_Manager_Management_ServiceManagersForARegion",
        "fields": [
            {
                "name": "generation",
                "sanitized": "generation",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "id",
                "sanitized": "id",
                "type": r"string",
                "required": True,
            },
            {
                "name": "regionName",
                "sanitized": "regionName",
                "type": r"string",
                "required": True,
            },
            {
                "name": "serviceManagers",
                "sanitized": "serviceManagers",
                "type": r"array",
                "required": True,
            },
            {
                "name": "type",
                "sanitized": "type",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": Service_offer_management_MyServices,
        "name": "Service_offer_management_MyServices",
        "fields": [
            {
                "name": "next",
                "sanitized": "next",
                "type": r"string",
                "required": True,
            },
            {
                "name": "total",
                "sanitized": "total",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "count",
                "sanitized": "count",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "items",
                "sanitized": "items",
                "type": r"array",
                "required": True,
            },
        ],
    },
    {
        "model": Service_provision_management_ServiceManagerResourceLink,
        "name": "Service_provision_management_ServiceManagerResourceLink",
        "fields": [
            {
                "name": "resourceUri",
                "sanitized": "resourceUri",
                "type": r"string",
                "required": False,
            },
            {
                "name": "id",
                "sanitized": "id",
                "type": r"string",
                "required": False,
            },
        ],
    },
    {
        "model": Service_provision_management_OperationalMode,
        "name": "Service_provision_management_OperationalMode",
        "fields": [],
    },
    {
        "model": Service_provision_management_UnauthorizedError,
        "name": "Service_provision_management_UnauthorizedError",
        "fields": [
            {
                "name": "httpStatusCode",
                "sanitized": "httpStatusCode",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "message",
                "sanitized": "message",
                "type": r"string",
                "required": True,
            },
            {
                "name": "debugId",
                "sanitized": "debugId",
                "type": r"string",
                "required": True,
            },
            {
                "name": "errorCode",
                "sanitized": "errorCode",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": Service_Manager_Management_ConflictError,
        "name": "Service_Manager_Management_ConflictError",
        "fields": [
            {
                "name": "errorCode",
                "sanitized": "errorCode",
                "type": r"string",
                "required": True,
            },
            {
                "name": "httpStatusCode",
                "sanitized": "httpStatusCode",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "message",
                "sanitized": "message",
                "type": r"string",
                "required": True,
            },
            {
                "name": "debugId",
                "sanitized": "debugId",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": Service_provision_management_ProvisionStatus,
        "name": "Service_provision_management_ProvisionStatus",
        "fields": [],
    },
    {
        "model": Service_offer_management_RecentServicesV2,
        "name": "Service_offer_management_RecentServicesV2",
        "fields": [
            {
                "name": "next",
                "sanitized": "next",
                "type": r"string",
                "required": True,
            },
            {
                "name": "total",
                "sanitized": "total",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "count",
                "sanitized": "count",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "items",
                "sanitized": "items",
                "type": r"array",
                "required": True,
            },
        ],
    },
    {
        "model": Service_offer_management_ServiceOfferRegionRead,
        "name": "Service_offer_management_ServiceOfferRegionRead",
        "fields": [
            {
                "name": "status",
                "sanitized": "status",
                "type": r"string",
                "required": True,
            },
            {
                "name": "type",
                "sanitized": "type",
                "type": r"string",
                "required": True,
            },
            {
                "name": "updatedAt",
                "sanitized": "updatedAt",
                "type": r"string",
                "required": True,
            },
            {
                "name": "generation",
                "sanitized": "generation",
                "type": r"integer",
                "required": True,
            },
            {
                "name": "resourceUri",
                "sanitized": "resourceUri",
                "type": r"string",
                "required": False,
            },
            {
                "name": "region",
                "sanitized": "region",
                "type": r"string",
                "required": True,
            },
            {
                "name": "serviceOffer",
                "sanitized": "serviceOffer",
                "type": r"object",
                "required": False,
            },
            {
                "name": "createdAt",
                "sanitized": "createdAt",
                "type": r"string",
                "required": True,
            },
            {
                "name": "id",
                "sanitized": "id",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": Service_offer_management_CategoryWithFeaturedServiceOffers,
        "name": "Service_offer_management_CategoryWithFeaturedServiceOffers",
        "fields": [
            {
                "name": "id",
                "sanitized": "id",
                "type": r"string",
                "required": True,
            },
            {
                "name": "servicesWithRegions",
                "sanitized": "servicesWithRegions",
                "type": r"array",
                "required": False,
            },
            {
                "name": "type",
                "sanitized": "type",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": Service_provision_management_ServiceOfferResourceLink,
        "name": "Service_provision_management_ServiceOfferResourceLink",
        "fields": [
            {
                "name": "id",
                "sanitized": "id",
                "type": r"string",
                "required": False,
            },
            {
                "name": "name",
                "sanitized": "name",
                "type": r"string",
                "required": False,
            },
            {
                "name": "resourceUri",
                "sanitized": "resourceUri",
                "type": r"string",
                "required": False,
            },
        ],
    },
    {
        "model": Service_Manager_Management_ServiceManagerResourceLink,
        "name": "Service_Manager_Management_ServiceManagerResourceLink",
        "fields": [
            {
                "name": "id",
                "sanitized": "id",
                "type": r"string",
                "required": False,
            },
            {
                "name": "resourceUri",
                "sanitized": "resourceUri",
                "type": r"string",
                "required": False,
            },
        ],
    },
    {
        "model": Service_offer_management_WorkspaceTypes,
        "name": "Service_offer_management_WorkspaceTypes",
        "fields": [],
    },
    {
        "model": Service_offer_management_ServiceOfferPartialInfo,
        "name": "Service_offer_management_ServiceOfferPartialInfo",
        "fields": [
            {
                "name": "staticLaunchUrl",
                "sanitized": "staticLaunchUrl",
                "type": r"string",
                "required": True,
            },
            {
                "name": "categories",
                "sanitized": "categories",
                "type": r"array",
                "required": True,
            },
            {
                "name": "id",
                "sanitized": "id",
                "type": r"string",
                "required": True,
            },
            {
                "name": "name",
                "sanitized": "name",
                "type": r"string",
                "required": True,
            },
            {
                "name": "resourceUri",
                "sanitized": "resourceUri",
                "type": r"string",
                "required": True,
            },
            {
                "name": "serviceManager",
                "sanitized": "serviceManager",
                "type": r"object",
                "required": False,
            },
            {
                "name": "slug",
                "sanitized": "slug",
                "type": r"string",
                "required": True,
            },
        ],
    },
    {
        "model": Service_Manager_Management_ServiceManagerProvisionCreateBase,
        "name": "Service_Manager_Management_ServiceManagerProvisionCreateBase",
        "fields": [
            {
                "name": "region",
                "sanitized": "region",
                "type": r"string",
                "required": True,
            },
            {
                "name": "serviceManagerId",
                "sanitized": "serviceManagerId",
                "type": r"string",
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
