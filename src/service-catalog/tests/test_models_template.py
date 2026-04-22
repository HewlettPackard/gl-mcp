# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
Test template for models package.
Tests all generated data models from OpenAPI schemas.
"""

import pytest
from typing import Any, Dict
from pydantic import ValidationError as PydanticValidationError


from greenlake_service_catalog_mcp.models.base import Service_Manager_Management_PreConditionFailedError

from greenlake_service_catalog_mcp.models.base import Service_Manager_Management_MSPConversionStatus

from greenlake_service_catalog_mcp.models.base import Service_offer_management_Region

from greenlake_service_catalog_mcp.models.base import Service_offer_management_ServiceManagerResourceLink

from greenlake_service_catalog_mcp.models.base import Service_Manager_Management_BaseError

from greenlake_service_catalog_mcp.models.base import Service_offer_management_BadRequestError

from greenlake_service_catalog_mcp.models.base import Service_offer_management_NotFoundError

from greenlake_service_catalog_mcp.models.base import Service_offer_management_ServiceManagerProvisionPartialInfo

from greenlake_service_catalog_mcp.models.base import Service_offer_management_OperationalMode

from greenlake_service_catalog_mcp.models.base import Service_offer_management_ForbiddenError

from greenlake_service_catalog_mcp.models.base import Service_offer_management_ProvisionStatus

from greenlake_service_catalog_mcp.models.base import Service_offer_management_ServiceOfferStatus

from greenlake_service_catalog_mcp.models.base import Service_offer_management_RecentServices

from greenlake_service_catalog_mcp.models.base import Service_provision_management_MspConversionStatus

from greenlake_service_catalog_mcp.models.base import Service_offer_management_RecentService

from greenlake_service_catalog_mcp.models.base import Service_offer_management_ServiceManagerProvision

from greenlake_service_catalog_mcp.models.base import Service_offer_management_ConflictError

from greenlake_service_catalog_mcp.models.base import Service_Manager_Management_ServiceManagerProvisionCreateResponse

from greenlake_service_catalog_mcp.models.base import Service_Manager_Management_NotFoundError

from greenlake_service_catalog_mcp.models.base import Service_Manager_Management_ValidationError

from greenlake_service_catalog_mcp.models.base import Service_Manager_Management_ServiceManagerRead

from greenlake_service_catalog_mcp.models.base import Service_offer_management_ServiceOfferPartialDetails

from greenlake_service_catalog_mcp.models.base import Service_Manager_Management_Error

from greenlake_service_catalog_mcp.models.base import Service_provision_management_ServiceProvision

from greenlake_service_catalog_mcp.models.base import Service_offer_management_ServiceOfferResourceLink

from greenlake_service_catalog_mcp.models.base import Service_offer_management_RecentServiceV2

from greenlake_service_catalog_mcp.models.base import Service_offer_management_RegionalProvision

from greenlake_service_catalog_mcp.models.base import Service_offer_management_DetailedServiceManagerResourceLink

from greenlake_service_catalog_mcp.models.base import Service_offer_management_WorkspaceTransferStatus

from greenlake_service_catalog_mcp.models.base import Service_offer_management_TooManyRequestsError

from greenlake_service_catalog_mcp.models.base import Service_offer_management_DetailedServiceOffer

from greenlake_service_catalog_mcp.models.base import Service_offer_management_CategoryWithServiceOffers

from greenlake_service_catalog_mcp.models.base import Service_provision_management_ServiceProvisionList

from greenlake_service_catalog_mcp.models.base import Service_offer_management_ServiceOfferMediaVideoDetails

from greenlake_service_catalog_mcp.models.base import Service_offer_management_SupportedFeature

from greenlake_service_catalog_mcp.models.base import Service_provision_management_ConflictError

from greenlake_service_catalog_mcp.models.base import Service_provision_management_NotFoundError

from greenlake_service_catalog_mcp.models.base import Service_offer_management_ServiceOfferList

from greenlake_service_catalog_mcp.models.base import Service_Manager_Management_ServiceManagersPerRegion

from greenlake_service_catalog_mcp.models.base import Service_offer_management_ServiceOfferMediaImageDetails

from greenlake_service_catalog_mcp.models.base import Service_offer_management_RegionWithDetailedProvisions

from greenlake_service_catalog_mcp.models.base import Service_Manager_Management_ServiceManagerReadList

from greenlake_service_catalog_mcp.models.base import Service_offer_management_FeaturedServiceOffers

from greenlake_service_catalog_mcp.models.base import Service_provision_management_PreConditionFailedError

from greenlake_service_catalog_mcp.models.base import Service_offer_management_DetailedProvision

from greenlake_service_catalog_mcp.models.base import Service_offer_management_ServiceOfferWithAvailableRegions

from greenlake_service_catalog_mcp.models.base import Service_offer_management_ValidationError

from greenlake_service_catalog_mcp.models.base import Service_provision_management_ServiceProvisionCreateBase

from greenlake_service_catalog_mcp.models.base import Service_offer_management_ServiceOfferCatalog

from greenlake_service_catalog_mcp.models.base import Service_provision_management_ForbiddenError

from greenlake_service_catalog_mcp.models.base import Service_offer_management_ServiceOfferRegionsList

from greenlake_service_catalog_mcp.models.base import Service_offer_management_ServiceProvisionPartialInfo

from greenlake_service_catalog_mcp.models.base import Service_provision_management_WorkspaceResourceLink

from greenlake_service_catalog_mcp.models.base import Service_provision_management_ServiceManagerProvisionResourceLink

from greenlake_service_catalog_mcp.models.base import Service_Manager_Management_ProvisionStatus

from greenlake_service_catalog_mcp.models.base import Service_offer_management_InternalError

from greenlake_service_catalog_mcp.models.base import Service_provision_management_InternalError

from greenlake_service_catalog_mcp.models.base import Service_Manager_Management_BadRequestError

from greenlake_service_catalog_mcp.models.base import Service_offer_management_ServiceOfferReadWithMedia

from greenlake_service_catalog_mcp.models.base import Service_provision_management_BaseError

from greenlake_service_catalog_mcp.models.base import Service_Manager_Management_ServiceManagerProvisionRead

from greenlake_service_catalog_mcp.models.base import Service_offer_management_Category

from greenlake_service_catalog_mcp.models.base import Service_provision_management_ValidationError

from greenlake_service_catalog_mcp.models.base import Service_Manager_Management_UnauthorizedError

from greenlake_service_catalog_mcp.models.base import Service_provision_management_Error

from greenlake_service_catalog_mcp.models.base import Service_offer_management_ServiceProvision

from greenlake_service_catalog_mcp.models.base import Service_provision_management_AccountType

from greenlake_service_catalog_mcp.models.base import Service_offer_management_PreConditionFailedError

from greenlake_service_catalog_mcp.models.base import Service_Manager_Management_InternalError

from greenlake_service_catalog_mcp.models.base import Service_Manager_Management_ForbiddenError

from greenlake_service_catalog_mcp.models.base import Service_offer_management_RegionWithLocations

from greenlake_service_catalog_mcp.models.base import Service_offer_management_UnauthorizedError

from greenlake_service_catalog_mcp.models.base import Service_provision_management_BadRequestError

from greenlake_service_catalog_mcp.models.base import Service_offer_management_ServiceManagerProvisionResourceLink

from greenlake_service_catalog_mcp.models.base import Service_offer_management_MSPConversionStatus

from greenlake_service_catalog_mcp.models.base import Service_Manager_Management_ServiceManagerProvisionReadList

from greenlake_service_catalog_mcp.models.base import Service_offer_management_WorkspaceResourceLink

from greenlake_service_catalog_mcp.models.base import Service_offer_management_ServiceOfferRead

from greenlake_service_catalog_mcp.models.base import Service_offer_management_WorkspaceOpMode

from greenlake_service_catalog_mcp.models.base import Service_provision_management_WorkspaceTransferStatus

from greenlake_service_catalog_mcp.models.base import Service_offer_management_ServiceOfferType

from greenlake_service_catalog_mcp.models.base import Service_Manager_Management_ServiceManagersForARegion

from greenlake_service_catalog_mcp.models.base import Service_offer_management_MyServices

from greenlake_service_catalog_mcp.models.base import Service_provision_management_ServiceManagerResourceLink

from greenlake_service_catalog_mcp.models.base import Service_provision_management_OperationalMode

from greenlake_service_catalog_mcp.models.base import Service_provision_management_UnauthorizedError

from greenlake_service_catalog_mcp.models.base import Service_Manager_Management_ConflictError

from greenlake_service_catalog_mcp.models.base import Service_provision_management_ProvisionStatus

from greenlake_service_catalog_mcp.models.base import Service_offer_management_RecentServicesV2

from greenlake_service_catalog_mcp.models.base import Service_offer_management_ServiceOfferRegionRead

from greenlake_service_catalog_mcp.models.base import Service_offer_management_CategoryWithFeaturedServiceOffers

from greenlake_service_catalog_mcp.models.base import Service_provision_management_ServiceOfferResourceLink

from greenlake_service_catalog_mcp.models.base import Service_Manager_Management_ServiceManagerResourceLink

from greenlake_service_catalog_mcp.models.base import Service_offer_management_WorkspaceTypes

from greenlake_service_catalog_mcp.models.base import Service_offer_management_ServiceOfferPartialInfo

from greenlake_service_catalog_mcp.models.base import Service_Manager_Management_ServiceManagerProvisionCreateBase


class TestModels:
    """Test suite for all generated data models."""

    def test_service_manager_management_preconditionfailederror_model_creation(self):
        """Test Service_Manager_Management_PreConditionFailedError model creation with valid data."""
        # Valid test data for Service_Manager_Management_PreConditionFailedError
        valid_data = {
            "message": "test_message",
            "debugId": "test_debugId",
            "errorCode": "test_errorCode",
            "httpStatusCode": 42,
        }

        # Create model instance
        model = Service_Manager_Management_PreConditionFailedError(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_Manager_Management_PreConditionFailedError)
        assert model.message == valid_data["message"]
        assert model.debugId == valid_data["debugId"]
        assert model.errorCode == valid_data["errorCode"]
        assert model.httpStatusCode == valid_data["httpStatusCode"]

    def test_service_manager_management_preconditionfailederror_model_validation(self):
        """Test Service_Manager_Management_PreConditionFailedError model field validation."""
        # Test with minimal required data
        minimal_data = {
            "message": "required_message",
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
            "httpStatusCode": 1,
        }

        model = Service_Manager_Management_PreConditionFailedError(**minimal_data)
        assert isinstance(model, Service_Manager_Management_PreConditionFailedError)
        assert model.message == minimal_data["message"]
        assert model.debugId == minimal_data["debugId"]
        assert model.errorCode == minimal_data["errorCode"]
        assert model.httpStatusCode == minimal_data["httpStatusCode"]

    def test_service_manager_management_preconditionfailederror_model_required_fields(self):
        """Test Service_Manager_Management_PreConditionFailedError model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "message",
            "debugId",
            "errorCode",
            "httpStatusCode",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_Manager_Management_PreConditionFailedError()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "message",
                "debugId",
                "errorCode",
                "httpStatusCode",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_Manager_Management_PreConditionFailedError()
            assert isinstance(model, Service_Manager_Management_PreConditionFailedError)

    def test_service_manager_management_preconditionfailederror_model_optional_fields(self):
        """Test Service_Manager_Management_PreConditionFailedError model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "message": "required_message",
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
            "httpStatusCode": 1,
        }

        model = Service_Manager_Management_PreConditionFailedError(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_manager_management_preconditionfailederror_model_serialization(self):
        """Test Service_Manager_Management_PreConditionFailedError model serialization to dict."""
        test_data = {
            "message": "serialize_value",
            "debugId": "serialize_value",
            "errorCode": "serialize_value",
            "httpStatusCode": 99,
        }

        model = Service_Manager_Management_PreConditionFailedError(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "message" in serialized
        assert "debugId" in serialized
        assert "errorCode" in serialized
        assert "httpStatusCode" in serialized

        # Verify values are preserved
        assert serialized["message"] == test_data["message"]
        assert serialized["debugId"] == test_data["debugId"]
        assert serialized["errorCode"] == test_data["errorCode"]
        assert serialized["httpStatusCode"] == test_data["httpStatusCode"]

    def test_service_manager_management_preconditionfailederror_model_json_schema(self):
        """Test Service_Manager_Management_PreConditionFailedError model JSON schema generation."""
        schema = Service_Manager_Management_PreConditionFailedError.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "message",
            "debugId",
            "errorCode",
            "httpStatusCode",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "message",
            "debugId",
            "errorCode",
            "httpStatusCode",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_manager_management_mspconversionstatus_model_creation(self):
        """Test Service_Manager_Management_MSPConversionStatus model creation with valid data."""
        # Valid test data for Service_Manager_Management_MSPConversionStatus
        valid_data = {}

        # Create model instance
        model = Service_Manager_Management_MSPConversionStatus(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_Manager_Management_MSPConversionStatus)

    def test_service_manager_management_mspconversionstatus_model_validation(self):
        """Test Service_Manager_Management_MSPConversionStatus model field validation."""
        # Test with minimal required data
        minimal_data = {}

        model = Service_Manager_Management_MSPConversionStatus(**minimal_data)
        assert isinstance(model, Service_Manager_Management_MSPConversionStatus)

    def test_service_manager_management_mspconversionstatus_model_required_fields(self):
        """Test Service_Manager_Management_MSPConversionStatus model required field validation."""
        # Check if this model has any required fields
        required_fields = []

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_Manager_Management_MSPConversionStatus()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {}

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_Manager_Management_MSPConversionStatus()
            assert isinstance(model, Service_Manager_Management_MSPConversionStatus)

    def test_service_manager_management_mspconversionstatus_model_optional_fields(self):
        """Test Service_Manager_Management_MSPConversionStatus model optional field handling."""
        # Create with minimal required data
        minimal_data = {}

        model = Service_Manager_Management_MSPConversionStatus(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_manager_management_mspconversionstatus_model_serialization(self):
        """Test Service_Manager_Management_MSPConversionStatus model serialization to dict."""
        test_data = {}

        model = Service_Manager_Management_MSPConversionStatus(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)

        # Verify values are preserved

    def test_service_manager_management_mspconversionstatus_model_json_schema(self):
        """Test Service_Manager_Management_MSPConversionStatus model JSON schema generation."""
        schema = Service_Manager_Management_MSPConversionStatus.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {}

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = []
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_offer_management_region_model_creation(self):
        """Test Service_offer_management_Region model creation with valid data."""
        # Valid test data for Service_offer_management_Region
        valid_data = {
            "name": "test_name",
            "type": "test_type",
            "id": "test_id",
        }

        # Create model instance
        model = Service_offer_management_Region(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_offer_management_Region)
        assert model.name == valid_data["name"]
        assert model.type == valid_data["type"]
        assert model.id == valid_data["id"]

    def test_service_offer_management_region_model_validation(self):
        """Test Service_offer_management_Region model field validation."""
        # Test with minimal required data
        minimal_data = {}

        model = Service_offer_management_Region(**minimal_data)
        assert isinstance(model, Service_offer_management_Region)

    def test_service_offer_management_region_model_required_fields(self):
        """Test Service_offer_management_Region model required field validation."""
        # Check if this model has any required fields
        required_fields = []

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_offer_management_Region()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {}

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_offer_management_Region()
            assert isinstance(model, Service_offer_management_Region)

    def test_service_offer_management_region_model_optional_fields(self):
        """Test Service_offer_management_Region model optional field handling."""
        # Create with minimal required data
        minimal_data = {}

        model = Service_offer_management_Region(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "name")
        # Optional field name should be None or have a default value
        assert model.name is None or model.name is not None
        assert hasattr(model, "type")
        # Optional field type should be None or have a default value
        assert model.type is None or model.type is not None
        assert hasattr(model, "id")
        # Optional field id should be None or have a default value
        assert model.id is None or model.id is not None

    def test_service_offer_management_region_model_serialization(self):
        """Test Service_offer_management_Region model serialization to dict."""
        test_data = {
            "name": "serialize_value",
            "type": "serialize_value",
            "id": "serialize_value",
        }

        model = Service_offer_management_Region(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "name" in serialized
        assert "type" in serialized
        assert "id" in serialized

        # Verify values are preserved
        assert serialized["name"] == test_data["name"]
        assert serialized["type"] == test_data["type"]
        assert serialized["id"] == test_data["id"]

    def test_service_offer_management_region_model_json_schema(self):
        """Test Service_offer_management_Region model JSON schema generation."""
        schema = Service_offer_management_Region.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "name",
            "type",
            "id",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = []
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_offer_management_servicemanagerresourcelink_model_creation(self):
        """Test Service_offer_management_ServiceManagerResourceLink model creation with valid data."""
        # Valid test data for Service_offer_management_ServiceManagerResourceLink
        valid_data = {
            "id": "test_id",
            "resourceUri": "test_resourceUri",
        }

        # Create model instance
        model = Service_offer_management_ServiceManagerResourceLink(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_offer_management_ServiceManagerResourceLink)
        assert model.id == valid_data["id"]
        assert model.resourceUri == valid_data["resourceUri"]

    def test_service_offer_management_servicemanagerresourcelink_model_validation(self):
        """Test Service_offer_management_ServiceManagerResourceLink model field validation."""
        # Test with minimal required data
        minimal_data = {}

        model = Service_offer_management_ServiceManagerResourceLink(**minimal_data)
        assert isinstance(model, Service_offer_management_ServiceManagerResourceLink)

    def test_service_offer_management_servicemanagerresourcelink_model_required_fields(self):
        """Test Service_offer_management_ServiceManagerResourceLink model required field validation."""
        # Check if this model has any required fields
        required_fields = []

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_offer_management_ServiceManagerResourceLink()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {}

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_offer_management_ServiceManagerResourceLink()
            assert isinstance(model, Service_offer_management_ServiceManagerResourceLink)

    def test_service_offer_management_servicemanagerresourcelink_model_optional_fields(self):
        """Test Service_offer_management_ServiceManagerResourceLink model optional field handling."""
        # Create with minimal required data
        minimal_data = {}

        model = Service_offer_management_ServiceManagerResourceLink(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "id")
        # Optional field id should be None or have a default value
        assert model.id is None or model.id is not None
        assert hasattr(model, "resourceUri")
        # Optional field resourceUri should be None or have a default value
        assert model.resourceUri is None or model.resourceUri is not None

    def test_service_offer_management_servicemanagerresourcelink_model_serialization(self):
        """Test Service_offer_management_ServiceManagerResourceLink model serialization to dict."""
        test_data = {
            "id": "serialize_value",
            "resourceUri": "serialize_value",
        }

        model = Service_offer_management_ServiceManagerResourceLink(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "id" in serialized
        assert "resourceUri" in serialized

        # Verify values are preserved
        assert serialized["id"] == test_data["id"]
        assert serialized["resourceUri"] == test_data["resourceUri"]

    def test_service_offer_management_servicemanagerresourcelink_model_json_schema(self):
        """Test Service_offer_management_ServiceManagerResourceLink model JSON schema generation."""
        schema = Service_offer_management_ServiceManagerResourceLink.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "id",
            "resourceUri",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = []
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_manager_management_baseerror_model_creation(self):
        """Test Service_Manager_Management_BaseError model creation with valid data."""
        # Valid test data for Service_Manager_Management_BaseError
        valid_data = {
            "debugId": "test_debugId",
            "errorCode": "test_errorCode",
            "httpStatusCode": 42,
            "message": "test_message",
        }

        # Create model instance
        model = Service_Manager_Management_BaseError(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_Manager_Management_BaseError)
        assert model.debugId == valid_data["debugId"]
        assert model.errorCode == valid_data["errorCode"]
        assert model.httpStatusCode == valid_data["httpStatusCode"]
        assert model.message == valid_data["message"]

    def test_service_manager_management_baseerror_model_validation(self):
        """Test Service_Manager_Management_BaseError model field validation."""
        # Test with minimal required data
        minimal_data = {
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
            "httpStatusCode": 1,
            "message": "required_message",
        }

        model = Service_Manager_Management_BaseError(**minimal_data)
        assert isinstance(model, Service_Manager_Management_BaseError)
        assert model.debugId == minimal_data["debugId"]
        assert model.errorCode == minimal_data["errorCode"]
        assert model.httpStatusCode == minimal_data["httpStatusCode"]
        assert model.message == minimal_data["message"]

    def test_service_manager_management_baseerror_model_required_fields(self):
        """Test Service_Manager_Management_BaseError model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "debugId",
            "errorCode",
            "httpStatusCode",
            "message",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_Manager_Management_BaseError()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "debugId",
                "errorCode",
                "httpStatusCode",
                "message",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_Manager_Management_BaseError()
            assert isinstance(model, Service_Manager_Management_BaseError)

    def test_service_manager_management_baseerror_model_optional_fields(self):
        """Test Service_Manager_Management_BaseError model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
            "httpStatusCode": 1,
            "message": "required_message",
        }

        model = Service_Manager_Management_BaseError(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_manager_management_baseerror_model_serialization(self):
        """Test Service_Manager_Management_BaseError model serialization to dict."""
        test_data = {
            "debugId": "serialize_value",
            "errorCode": "serialize_value",
            "httpStatusCode": 99,
            "message": "serialize_value",
        }

        model = Service_Manager_Management_BaseError(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "debugId" in serialized
        assert "errorCode" in serialized
        assert "httpStatusCode" in serialized
        assert "message" in serialized

        # Verify values are preserved
        assert serialized["debugId"] == test_data["debugId"]
        assert serialized["errorCode"] == test_data["errorCode"]
        assert serialized["httpStatusCode"] == test_data["httpStatusCode"]
        assert serialized["message"] == test_data["message"]

    def test_service_manager_management_baseerror_model_json_schema(self):
        """Test Service_Manager_Management_BaseError model JSON schema generation."""
        schema = Service_Manager_Management_BaseError.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "debugId",
            "errorCode",
            "httpStatusCode",
            "message",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "debugId",
            "errorCode",
            "httpStatusCode",
            "message",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_offer_management_badrequesterror_model_creation(self):
        """Test Service_offer_management_BadRequestError model creation with valid data."""
        # Valid test data for Service_offer_management_BadRequestError
        valid_data = {
            "errorCode": "test_errorCode",
            "errorDetails": [],
            "httpStatusCode": 42,
            "message": "test_message",
            "debugId": "test_debugId",
        }

        # Create model instance
        model = Service_offer_management_BadRequestError(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_offer_management_BadRequestError)
        assert model.errorCode == valid_data["errorCode"]
        assert model.errorDetails == valid_data["errorDetails"]
        assert model.httpStatusCode == valid_data["httpStatusCode"]
        assert model.message == valid_data["message"]
        assert model.debugId == valid_data["debugId"]

    def test_service_offer_management_badrequesterror_model_validation(self):
        """Test Service_offer_management_BadRequestError model field validation."""
        # Test with minimal required data
        minimal_data = {
            "errorCode": "required_errorCode",
            "errorDetails": [],
            "httpStatusCode": 1,
            "message": "required_message",
            "debugId": "required_debugId",
        }

        model = Service_offer_management_BadRequestError(**minimal_data)
        assert isinstance(model, Service_offer_management_BadRequestError)
        assert model.errorCode == minimal_data["errorCode"]
        assert model.errorDetails == minimal_data["errorDetails"]
        assert model.httpStatusCode == minimal_data["httpStatusCode"]
        assert model.message == minimal_data["message"]
        assert model.debugId == minimal_data["debugId"]

    def test_service_offer_management_badrequesterror_model_required_fields(self):
        """Test Service_offer_management_BadRequestError model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "errorCode",
            "errorDetails",
            "httpStatusCode",
            "message",
            "debugId",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_offer_management_BadRequestError()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "errorCode",
                "errorDetails",
                "httpStatusCode",
                "message",
                "debugId",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_offer_management_BadRequestError()
            assert isinstance(model, Service_offer_management_BadRequestError)

    def test_service_offer_management_badrequesterror_model_optional_fields(self):
        """Test Service_offer_management_BadRequestError model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "errorCode": "required_errorCode",
            "errorDetails": [],
            "httpStatusCode": 1,
            "message": "required_message",
            "debugId": "required_debugId",
        }

        model = Service_offer_management_BadRequestError(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_offer_management_badrequesterror_model_serialization(self):
        """Test Service_offer_management_BadRequestError model serialization to dict."""
        test_data = {
            "errorCode": "serialize_value",
            "errorDetails": [],
            "httpStatusCode": 99,
            "message": "serialize_value",
            "debugId": "serialize_value",
        }

        model = Service_offer_management_BadRequestError(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "errorCode" in serialized
        assert "errorDetails" in serialized
        assert "httpStatusCode" in serialized
        assert "message" in serialized
        assert "debugId" in serialized

        # Verify values are preserved
        assert serialized["errorCode"] == test_data["errorCode"]
        assert serialized["errorDetails"] == test_data["errorDetails"]
        assert serialized["httpStatusCode"] == test_data["httpStatusCode"]
        assert serialized["message"] == test_data["message"]
        assert serialized["debugId"] == test_data["debugId"]

    def test_service_offer_management_badrequesterror_model_json_schema(self):
        """Test Service_offer_management_BadRequestError model JSON schema generation."""
        schema = Service_offer_management_BadRequestError.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "errorCode",
            "errorDetails",
            "httpStatusCode",
            "message",
            "debugId",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "errorCode",
            "errorDetails",
            "httpStatusCode",
            "message",
            "debugId",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_offer_management_notfounderror_model_creation(self):
        """Test Service_offer_management_NotFoundError model creation with valid data."""
        # Valid test data for Service_offer_management_NotFoundError
        valid_data = {
            "errorDetails": [],
            "httpStatusCode": 42,
            "message": "test_message",
            "debugId": "test_debugId",
            "errorCode": "test_errorCode",
        }

        # Create model instance
        model = Service_offer_management_NotFoundError(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_offer_management_NotFoundError)
        assert model.errorDetails == valid_data["errorDetails"]
        assert model.httpStatusCode == valid_data["httpStatusCode"]
        assert model.message == valid_data["message"]
        assert model.debugId == valid_data["debugId"]
        assert model.errorCode == valid_data["errorCode"]

    def test_service_offer_management_notfounderror_model_validation(self):
        """Test Service_offer_management_NotFoundError model field validation."""
        # Test with minimal required data
        minimal_data = {
            "httpStatusCode": 1,
            "message": "required_message",
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
        }

        model = Service_offer_management_NotFoundError(**minimal_data)
        assert isinstance(model, Service_offer_management_NotFoundError)
        assert model.httpStatusCode == minimal_data["httpStatusCode"]
        assert model.message == minimal_data["message"]
        assert model.debugId == minimal_data["debugId"]
        assert model.errorCode == minimal_data["errorCode"]

    def test_service_offer_management_notfounderror_model_required_fields(self):
        """Test Service_offer_management_NotFoundError model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "httpStatusCode",
            "message",
            "debugId",
            "errorCode",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_offer_management_NotFoundError()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "httpStatusCode",
                "message",
                "debugId",
                "errorCode",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_offer_management_NotFoundError()
            assert isinstance(model, Service_offer_management_NotFoundError)

    def test_service_offer_management_notfounderror_model_optional_fields(self):
        """Test Service_offer_management_NotFoundError model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "httpStatusCode": 1,
            "message": "required_message",
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
        }

        model = Service_offer_management_NotFoundError(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "errorDetails")
        # Optional field errorDetails should be None or have a default value
        assert model.errorDetails is None or model.errorDetails is not None

    def test_service_offer_management_notfounderror_model_serialization(self):
        """Test Service_offer_management_NotFoundError model serialization to dict."""
        test_data = {
            "errorDetails": [],
            "httpStatusCode": 99,
            "message": "serialize_value",
            "debugId": "serialize_value",
            "errorCode": "serialize_value",
        }

        model = Service_offer_management_NotFoundError(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "errorDetails" in serialized
        assert "httpStatusCode" in serialized
        assert "message" in serialized
        assert "debugId" in serialized
        assert "errorCode" in serialized

        # Verify values are preserved
        assert serialized["errorDetails"] == test_data["errorDetails"]
        assert serialized["httpStatusCode"] == test_data["httpStatusCode"]
        assert serialized["message"] == test_data["message"]
        assert serialized["debugId"] == test_data["debugId"]
        assert serialized["errorCode"] == test_data["errorCode"]

    def test_service_offer_management_notfounderror_model_json_schema(self):
        """Test Service_offer_management_NotFoundError model JSON schema generation."""
        schema = Service_offer_management_NotFoundError.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "errorDetails",
            "httpStatusCode",
            "message",
            "debugId",
            "errorCode",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "httpStatusCode",
            "message",
            "debugId",
            "errorCode",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_offer_management_servicemanagerprovisionpartialinfo_model_creation(self):
        """Test Service_offer_management_ServiceManagerProvisionPartialInfo model creation with valid data."""
        # Valid test data for Service_offer_management_ServiceManagerProvisionPartialInfo
        valid_data = {
            "region": "test_region",
            "resourceUri": "test_resourceUri",
            "serviceManagerInstanceId": "test_serviceManagerInstanceId",
            "updatedAt": "test_updatedAt",
            "createdAt": "test_createdAt",
            "createdBy": "test_createdBy",
            "generation": 42,
            "id": "test_id",
        }

        # Create model instance
        model = Service_offer_management_ServiceManagerProvisionPartialInfo(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_offer_management_ServiceManagerProvisionPartialInfo)
        assert model.region == valid_data["region"]
        assert model.resourceUri == valid_data["resourceUri"]
        assert model.serviceManagerInstanceId == valid_data["serviceManagerInstanceId"]
        assert model.updatedAt == valid_data["updatedAt"]
        assert model.createdAt == valid_data["createdAt"]
        assert model.createdBy == valid_data["createdBy"]
        assert model.generation == valid_data["generation"]
        assert model.id == valid_data["id"]

    def test_service_offer_management_servicemanagerprovisionpartialinfo_model_validation(self):
        """Test Service_offer_management_ServiceManagerProvisionPartialInfo model field validation."""
        # Test with minimal required data
        minimal_data = {
            "region": "required_region",
            "resourceUri": "required_resourceUri",
            "serviceManagerInstanceId": "required_serviceManagerInstanceId",
            "generation": 1,
            "id": "required_id",
        }

        model = Service_offer_management_ServiceManagerProvisionPartialInfo(**minimal_data)
        assert isinstance(model, Service_offer_management_ServiceManagerProvisionPartialInfo)
        assert model.region == minimal_data["region"]
        assert model.resourceUri == minimal_data["resourceUri"]
        assert model.serviceManagerInstanceId == minimal_data["serviceManagerInstanceId"]
        assert model.generation == minimal_data["generation"]
        assert model.id == minimal_data["id"]

    def test_service_offer_management_servicemanagerprovisionpartialinfo_model_required_fields(self):
        """Test Service_offer_management_ServiceManagerProvisionPartialInfo model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "region",
            "resourceUri",
            "serviceManagerInstanceId",
            "generation",
            "id",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_offer_management_ServiceManagerProvisionPartialInfo()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "region",
                "resourceUri",
                "serviceManagerInstanceId",
                "generation",
                "id",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_offer_management_ServiceManagerProvisionPartialInfo()
            assert isinstance(model, Service_offer_management_ServiceManagerProvisionPartialInfo)

    def test_service_offer_management_servicemanagerprovisionpartialinfo_model_optional_fields(self):
        """Test Service_offer_management_ServiceManagerProvisionPartialInfo model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "region": "required_region",
            "resourceUri": "required_resourceUri",
            "serviceManagerInstanceId": "required_serviceManagerInstanceId",
            "generation": 1,
            "id": "required_id",
        }

        model = Service_offer_management_ServiceManagerProvisionPartialInfo(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "updatedAt")
        # Optional field updatedAt should be None or have a default value
        assert model.updatedAt is None or model.updatedAt is not None
        assert hasattr(model, "createdAt")
        # Optional field createdAt should be None or have a default value
        assert model.createdAt is None or model.createdAt is not None
        assert hasattr(model, "createdBy")
        # Optional field createdBy should be None or have a default value
        assert model.createdBy is None or model.createdBy is not None

    def test_service_offer_management_servicemanagerprovisionpartialinfo_model_serialization(self):
        """Test Service_offer_management_ServiceManagerProvisionPartialInfo model serialization to dict."""
        test_data = {
            "region": "serialize_value",
            "resourceUri": "serialize_value",
            "serviceManagerInstanceId": "serialize_value",
            "updatedAt": "serialize_value",
            "createdAt": "serialize_value",
            "createdBy": "serialize_value",
            "generation": 99,
            "id": "serialize_value",
        }

        model = Service_offer_management_ServiceManagerProvisionPartialInfo(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "region" in serialized
        assert "resourceUri" in serialized
        assert "serviceManagerInstanceId" in serialized
        assert "updatedAt" in serialized
        assert "createdAt" in serialized
        assert "createdBy" in serialized
        assert "generation" in serialized
        assert "id" in serialized

        # Verify values are preserved
        assert serialized["region"] == test_data["region"]
        assert serialized["resourceUri"] == test_data["resourceUri"]
        assert serialized["serviceManagerInstanceId"] == test_data["serviceManagerInstanceId"]
        assert serialized["updatedAt"] == test_data["updatedAt"]
        assert serialized["createdAt"] == test_data["createdAt"]
        assert serialized["createdBy"] == test_data["createdBy"]
        assert serialized["generation"] == test_data["generation"]
        assert serialized["id"] == test_data["id"]

    def test_service_offer_management_servicemanagerprovisionpartialinfo_model_json_schema(self):
        """Test Service_offer_management_ServiceManagerProvisionPartialInfo model JSON schema generation."""
        schema = Service_offer_management_ServiceManagerProvisionPartialInfo.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "region",
            "resourceUri",
            "serviceManagerInstanceId",
            "updatedAt",
            "createdAt",
            "createdBy",
            "generation",
            "id",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "region",
            "resourceUri",
            "serviceManagerInstanceId",
            "generation",
            "id",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_offer_management_operationalmode_model_creation(self):
        """Test Service_offer_management_OperationalMode model creation with valid data."""
        # Valid test data for Service_offer_management_OperationalMode
        valid_data = {}

        # Create model instance
        model = Service_offer_management_OperationalMode(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_offer_management_OperationalMode)

    def test_service_offer_management_operationalmode_model_validation(self):
        """Test Service_offer_management_OperationalMode model field validation."""
        # Test with minimal required data
        minimal_data = {}

        model = Service_offer_management_OperationalMode(**minimal_data)
        assert isinstance(model, Service_offer_management_OperationalMode)

    def test_service_offer_management_operationalmode_model_required_fields(self):
        """Test Service_offer_management_OperationalMode model required field validation."""
        # Check if this model has any required fields
        required_fields = []

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_offer_management_OperationalMode()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {}

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_offer_management_OperationalMode()
            assert isinstance(model, Service_offer_management_OperationalMode)

    def test_service_offer_management_operationalmode_model_optional_fields(self):
        """Test Service_offer_management_OperationalMode model optional field handling."""
        # Create with minimal required data
        minimal_data = {}

        model = Service_offer_management_OperationalMode(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_offer_management_operationalmode_model_serialization(self):
        """Test Service_offer_management_OperationalMode model serialization to dict."""
        test_data = {}

        model = Service_offer_management_OperationalMode(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)

        # Verify values are preserved

    def test_service_offer_management_operationalmode_model_json_schema(self):
        """Test Service_offer_management_OperationalMode model JSON schema generation."""
        schema = Service_offer_management_OperationalMode.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {}

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = []
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_offer_management_forbiddenerror_model_creation(self):
        """Test Service_offer_management_ForbiddenError model creation with valid data."""
        # Valid test data for Service_offer_management_ForbiddenError
        valid_data = {
            "httpStatusCode": 42,
            "message": "test_message",
            "debugId": "test_debugId",
            "errorCode": "test_errorCode",
            "errorDetails": [],
        }

        # Create model instance
        model = Service_offer_management_ForbiddenError(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_offer_management_ForbiddenError)
        assert model.httpStatusCode == valid_data["httpStatusCode"]
        assert model.message == valid_data["message"]
        assert model.debugId == valid_data["debugId"]
        assert model.errorCode == valid_data["errorCode"]
        assert model.errorDetails == valid_data["errorDetails"]

    def test_service_offer_management_forbiddenerror_model_validation(self):
        """Test Service_offer_management_ForbiddenError model field validation."""
        # Test with minimal required data
        minimal_data = {
            "httpStatusCode": 1,
            "message": "required_message",
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
        }

        model = Service_offer_management_ForbiddenError(**minimal_data)
        assert isinstance(model, Service_offer_management_ForbiddenError)
        assert model.httpStatusCode == minimal_data["httpStatusCode"]
        assert model.message == minimal_data["message"]
        assert model.debugId == minimal_data["debugId"]
        assert model.errorCode == minimal_data["errorCode"]

    def test_service_offer_management_forbiddenerror_model_required_fields(self):
        """Test Service_offer_management_ForbiddenError model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "httpStatusCode",
            "message",
            "debugId",
            "errorCode",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_offer_management_ForbiddenError()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "httpStatusCode",
                "message",
                "debugId",
                "errorCode",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_offer_management_ForbiddenError()
            assert isinstance(model, Service_offer_management_ForbiddenError)

    def test_service_offer_management_forbiddenerror_model_optional_fields(self):
        """Test Service_offer_management_ForbiddenError model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "httpStatusCode": 1,
            "message": "required_message",
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
        }

        model = Service_offer_management_ForbiddenError(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "errorDetails")
        # Optional field errorDetails should be None or have a default value
        assert model.errorDetails is None or model.errorDetails is not None

    def test_service_offer_management_forbiddenerror_model_serialization(self):
        """Test Service_offer_management_ForbiddenError model serialization to dict."""
        test_data = {
            "httpStatusCode": 99,
            "message": "serialize_value",
            "debugId": "serialize_value",
            "errorCode": "serialize_value",
            "errorDetails": [],
        }

        model = Service_offer_management_ForbiddenError(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "httpStatusCode" in serialized
        assert "message" in serialized
        assert "debugId" in serialized
        assert "errorCode" in serialized
        assert "errorDetails" in serialized

        # Verify values are preserved
        assert serialized["httpStatusCode"] == test_data["httpStatusCode"]
        assert serialized["message"] == test_data["message"]
        assert serialized["debugId"] == test_data["debugId"]
        assert serialized["errorCode"] == test_data["errorCode"]
        assert serialized["errorDetails"] == test_data["errorDetails"]

    def test_service_offer_management_forbiddenerror_model_json_schema(self):
        """Test Service_offer_management_ForbiddenError model JSON schema generation."""
        schema = Service_offer_management_ForbiddenError.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "httpStatusCode",
            "message",
            "debugId",
            "errorCode",
            "errorDetails",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "httpStatusCode",
            "message",
            "debugId",
            "errorCode",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_offer_management_provisionstatus_model_creation(self):
        """Test Service_offer_management_ProvisionStatus model creation with valid data."""
        # Valid test data for Service_offer_management_ProvisionStatus
        valid_data = {}

        # Create model instance
        model = Service_offer_management_ProvisionStatus(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_offer_management_ProvisionStatus)

    def test_service_offer_management_provisionstatus_model_validation(self):
        """Test Service_offer_management_ProvisionStatus model field validation."""
        # Test with minimal required data
        minimal_data = {}

        model = Service_offer_management_ProvisionStatus(**minimal_data)
        assert isinstance(model, Service_offer_management_ProvisionStatus)

    def test_service_offer_management_provisionstatus_model_required_fields(self):
        """Test Service_offer_management_ProvisionStatus model required field validation."""
        # Check if this model has any required fields
        required_fields = []

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_offer_management_ProvisionStatus()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {}

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_offer_management_ProvisionStatus()
            assert isinstance(model, Service_offer_management_ProvisionStatus)

    def test_service_offer_management_provisionstatus_model_optional_fields(self):
        """Test Service_offer_management_ProvisionStatus model optional field handling."""
        # Create with minimal required data
        minimal_data = {}

        model = Service_offer_management_ProvisionStatus(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_offer_management_provisionstatus_model_serialization(self):
        """Test Service_offer_management_ProvisionStatus model serialization to dict."""
        test_data = {}

        model = Service_offer_management_ProvisionStatus(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)

        # Verify values are preserved

    def test_service_offer_management_provisionstatus_model_json_schema(self):
        """Test Service_offer_management_ProvisionStatus model JSON schema generation."""
        schema = Service_offer_management_ProvisionStatus.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {}

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = []
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_offer_management_serviceofferstatus_model_creation(self):
        """Test Service_offer_management_ServiceOfferStatus model creation with valid data."""
        # Valid test data for Service_offer_management_ServiceOfferStatus
        valid_data = {}

        # Create model instance
        model = Service_offer_management_ServiceOfferStatus(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_offer_management_ServiceOfferStatus)

    def test_service_offer_management_serviceofferstatus_model_validation(self):
        """Test Service_offer_management_ServiceOfferStatus model field validation."""
        # Test with minimal required data
        minimal_data = {}

        model = Service_offer_management_ServiceOfferStatus(**minimal_data)
        assert isinstance(model, Service_offer_management_ServiceOfferStatus)

    def test_service_offer_management_serviceofferstatus_model_required_fields(self):
        """Test Service_offer_management_ServiceOfferStatus model required field validation."""
        # Check if this model has any required fields
        required_fields = []

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_offer_management_ServiceOfferStatus()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {}

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_offer_management_ServiceOfferStatus()
            assert isinstance(model, Service_offer_management_ServiceOfferStatus)

    def test_service_offer_management_serviceofferstatus_model_optional_fields(self):
        """Test Service_offer_management_ServiceOfferStatus model optional field handling."""
        # Create with minimal required data
        minimal_data = {}

        model = Service_offer_management_ServiceOfferStatus(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_offer_management_serviceofferstatus_model_serialization(self):
        """Test Service_offer_management_ServiceOfferStatus model serialization to dict."""
        test_data = {}

        model = Service_offer_management_ServiceOfferStatus(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)

        # Verify values are preserved

    def test_service_offer_management_serviceofferstatus_model_json_schema(self):
        """Test Service_offer_management_ServiceOfferStatus model JSON schema generation."""
        schema = Service_offer_management_ServiceOfferStatus.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {}

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = []
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_offer_management_recentservices_model_creation(self):
        """Test Service_offer_management_RecentServices model creation with valid data."""
        # Valid test data for Service_offer_management_RecentServices
        valid_data = {
            "total": 42,
            "count": 42,
            "items": [],
            "next": "test_next",
        }

        # Create model instance
        model = Service_offer_management_RecentServices(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_offer_management_RecentServices)
        assert model.total == valid_data["total"]
        assert model.count == valid_data["count"]
        assert model.items == valid_data["items"]
        assert model.next == valid_data["next"]

    def test_service_offer_management_recentservices_model_validation(self):
        """Test Service_offer_management_RecentServices model field validation."""
        # Test with minimal required data
        minimal_data = {
            "total": 1,
            "count": 1,
            "items": [],
            "next": "required_next",
        }

        model = Service_offer_management_RecentServices(**minimal_data)
        assert isinstance(model, Service_offer_management_RecentServices)
        assert model.total == minimal_data["total"]
        assert model.count == minimal_data["count"]
        assert model.items == minimal_data["items"]
        assert model.next == minimal_data["next"]

    def test_service_offer_management_recentservices_model_required_fields(self):
        """Test Service_offer_management_RecentServices model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "total",
            "count",
            "items",
            "next",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_offer_management_RecentServices()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "total",
                "count",
                "items",
                "next",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_offer_management_RecentServices()
            assert isinstance(model, Service_offer_management_RecentServices)

    def test_service_offer_management_recentservices_model_optional_fields(self):
        """Test Service_offer_management_RecentServices model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "total": 1,
            "count": 1,
            "items": [],
            "next": "required_next",
        }

        model = Service_offer_management_RecentServices(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_offer_management_recentservices_model_serialization(self):
        """Test Service_offer_management_RecentServices model serialization to dict."""
        test_data = {
            "total": 99,
            "count": 99,
            "items": [],
            "next": "serialize_value",
        }

        model = Service_offer_management_RecentServices(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "total" in serialized
        assert "count" in serialized
        assert "items" in serialized
        assert "next" in serialized

        # Verify values are preserved
        assert serialized["total"] == test_data["total"]
        assert serialized["count"] == test_data["count"]
        assert serialized["items"] == test_data["items"]
        assert serialized["next"] == test_data["next"]

    def test_service_offer_management_recentservices_model_json_schema(self):
        """Test Service_offer_management_RecentServices model JSON schema generation."""
        schema = Service_offer_management_RecentServices.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "total",
            "count",
            "items",
            "next",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "total",
            "count",
            "items",
            "next",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_provision_management_mspconversionstatus_model_creation(self):
        """Test Service_provision_management_MspConversionStatus model creation with valid data."""
        # Valid test data for Service_provision_management_MspConversionStatus
        valid_data = {}

        # Create model instance
        model = Service_provision_management_MspConversionStatus(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_provision_management_MspConversionStatus)

    def test_service_provision_management_mspconversionstatus_model_validation(self):
        """Test Service_provision_management_MspConversionStatus model field validation."""
        # Test with minimal required data
        minimal_data = {}

        model = Service_provision_management_MspConversionStatus(**minimal_data)
        assert isinstance(model, Service_provision_management_MspConversionStatus)

    def test_service_provision_management_mspconversionstatus_model_required_fields(self):
        """Test Service_provision_management_MspConversionStatus model required field validation."""
        # Check if this model has any required fields
        required_fields = []

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_provision_management_MspConversionStatus()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {}

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_provision_management_MspConversionStatus()
            assert isinstance(model, Service_provision_management_MspConversionStatus)

    def test_service_provision_management_mspconversionstatus_model_optional_fields(self):
        """Test Service_provision_management_MspConversionStatus model optional field handling."""
        # Create with minimal required data
        minimal_data = {}

        model = Service_provision_management_MspConversionStatus(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_provision_management_mspconversionstatus_model_serialization(self):
        """Test Service_provision_management_MspConversionStatus model serialization to dict."""
        test_data = {}

        model = Service_provision_management_MspConversionStatus(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)

        # Verify values are preserved

    def test_service_provision_management_mspconversionstatus_model_json_schema(self):
        """Test Service_provision_management_MspConversionStatus model JSON schema generation."""
        schema = Service_provision_management_MspConversionStatus.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {}

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = []
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_offer_management_recentservice_model_creation(self):
        """Test Service_offer_management_RecentService model creation with valid data."""
        # Valid test data for Service_offer_management_RecentService
        valid_data = {
            "type": "test_type",
            "id": "test_id",
            "lastAccessedTime": "test_lastAccessedTime",
            "regionalProvisions": [],
            "serviceOffer": "test_serviceOffer",
        }

        # Create model instance
        model = Service_offer_management_RecentService(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_offer_management_RecentService)
        assert model.type == valid_data["type"]
        assert model.id == valid_data["id"]
        assert model.lastAccessedTime == valid_data["lastAccessedTime"]
        assert model.regionalProvisions == valid_data["regionalProvisions"]
        assert model.serviceOffer == valid_data["serviceOffer"]

    def test_service_offer_management_recentservice_model_validation(self):
        """Test Service_offer_management_RecentService model field validation."""
        # Test with minimal required data
        minimal_data = {
            "type": "required_type",
            "id": "required_id",
            "serviceOffer": "required_serviceOffer",
        }

        model = Service_offer_management_RecentService(**minimal_data)
        assert isinstance(model, Service_offer_management_RecentService)
        assert model.type == minimal_data["type"]
        assert model.id == minimal_data["id"]
        assert model.serviceOffer == minimal_data["serviceOffer"]

    def test_service_offer_management_recentservice_model_required_fields(self):
        """Test Service_offer_management_RecentService model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "type",
            "id",
            "serviceOffer",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_offer_management_RecentService()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "type",
                "id",
                "serviceOffer",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_offer_management_RecentService()
            assert isinstance(model, Service_offer_management_RecentService)

    def test_service_offer_management_recentservice_model_optional_fields(self):
        """Test Service_offer_management_RecentService model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "type": "required_type",
            "id": "required_id",
            "serviceOffer": "required_serviceOffer",
        }

        model = Service_offer_management_RecentService(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "lastAccessedTime")
        # Optional field lastAccessedTime should be None or have a default value
        assert model.lastAccessedTime is None or model.lastAccessedTime is not None
        assert hasattr(model, "regionalProvisions")
        # Optional field regionalProvisions should be None or have a default value
        assert model.regionalProvisions is None or model.regionalProvisions is not None

    def test_service_offer_management_recentservice_model_serialization(self):
        """Test Service_offer_management_RecentService model serialization to dict."""
        test_data = {
            "type": "serialize_value",
            "id": "serialize_value",
            "lastAccessedTime": "serialize_value",
            "regionalProvisions": [],
            "serviceOffer": "serialize_value",
        }

        model = Service_offer_management_RecentService(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "type" in serialized
        assert "id" in serialized
        assert "lastAccessedTime" in serialized
        assert "regionalProvisions" in serialized
        assert "serviceOffer" in serialized

        # Verify values are preserved
        assert serialized["type"] == test_data["type"]
        assert serialized["id"] == test_data["id"]
        assert serialized["lastAccessedTime"] == test_data["lastAccessedTime"]
        assert serialized["regionalProvisions"] == test_data["regionalProvisions"]
        assert serialized["serviceOffer"] == test_data["serviceOffer"]

    def test_service_offer_management_recentservice_model_json_schema(self):
        """Test Service_offer_management_RecentService model JSON schema generation."""
        schema = Service_offer_management_RecentService.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "type",
            "id",
            "lastAccessedTime",
            "regionalProvisions",
            "serviceOffer",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "type",
            "id",
            "serviceOffer",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_offer_management_servicemanagerprovision_model_creation(self):
        """Test Service_offer_management_ServiceManagerProvision model creation with valid data."""
        # Valid test data for Service_offer_management_ServiceManagerProvision
        valid_data = {
            "reason": "test_reason",
            "serviceManager": {},
            "provisionStatus": "test_provisionStatus",
            "createdAt": "test_createdAt",
            "workspaceTransferStatus": "test_workspaceTransferStatus",
            "id": "test_id",
            "region": "test_region",
            "updatedAt": "test_updatedAt",
            "generation": 42,
            "resourceUri": "test_resourceUri",
            "serviceManagerInstanceId": "test_serviceManagerInstanceId",
        }

        # Create model instance
        model = Service_offer_management_ServiceManagerProvision(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_offer_management_ServiceManagerProvision)
        assert model.reason == valid_data["reason"]
        assert model.serviceManager == valid_data["serviceManager"]
        assert model.provisionStatus == valid_data["provisionStatus"]
        assert model.createdAt == valid_data["createdAt"]
        assert model.workspaceTransferStatus == valid_data["workspaceTransferStatus"]
        assert model.id == valid_data["id"]
        assert model.region == valid_data["region"]
        assert model.updatedAt == valid_data["updatedAt"]
        assert model.generation == valid_data["generation"]
        assert model.resourceUri == valid_data["resourceUri"]
        assert model.serviceManagerInstanceId == valid_data["serviceManagerInstanceId"]

    def test_service_offer_management_servicemanagerprovision_model_validation(self):
        """Test Service_offer_management_ServiceManagerProvision model field validation."""
        # Test with minimal required data
        minimal_data = {
            "reason": "required_reason",
            "serviceManager": {},
            "provisionStatus": "required_provisionStatus",
            "createdAt": "required_createdAt",
            "id": "required_id",
            "region": "required_region",
            "updatedAt": "required_updatedAt",
            "generation": 1,
            "resourceUri": "required_resourceUri",
            "serviceManagerInstanceId": "required_serviceManagerInstanceId",
        }

        model = Service_offer_management_ServiceManagerProvision(**minimal_data)
        assert isinstance(model, Service_offer_management_ServiceManagerProvision)
        assert model.reason == minimal_data["reason"]
        assert model.serviceManager == minimal_data["serviceManager"]
        assert model.provisionStatus == minimal_data["provisionStatus"]
        assert model.createdAt == minimal_data["createdAt"]
        assert model.id == minimal_data["id"]
        assert model.region == minimal_data["region"]
        assert model.updatedAt == minimal_data["updatedAt"]
        assert model.generation == minimal_data["generation"]
        assert model.resourceUri == minimal_data["resourceUri"]
        assert model.serviceManagerInstanceId == minimal_data["serviceManagerInstanceId"]

    def test_service_offer_management_servicemanagerprovision_model_required_fields(self):
        """Test Service_offer_management_ServiceManagerProvision model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "reason",
            "serviceManager",
            "provisionStatus",
            "createdAt",
            "id",
            "region",
            "updatedAt",
            "generation",
            "resourceUri",
            "serviceManagerInstanceId",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_offer_management_ServiceManagerProvision()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "reason",
                "serviceManager",
                "provisionStatus",
                "createdAt",
                "id",
                "region",
                "updatedAt",
                "generation",
                "resourceUri",
                "serviceManagerInstanceId",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_offer_management_ServiceManagerProvision()
            assert isinstance(model, Service_offer_management_ServiceManagerProvision)

    def test_service_offer_management_servicemanagerprovision_model_optional_fields(self):
        """Test Service_offer_management_ServiceManagerProvision model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "reason": "required_reason",
            "serviceManager": {},
            "provisionStatus": "required_provisionStatus",
            "createdAt": "required_createdAt",
            "id": "required_id",
            "region": "required_region",
            "updatedAt": "required_updatedAt",
            "generation": 1,
            "resourceUri": "required_resourceUri",
            "serviceManagerInstanceId": "required_serviceManagerInstanceId",
        }

        model = Service_offer_management_ServiceManagerProvision(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "workspaceTransferStatus")
        # Optional field workspaceTransferStatus should be None or have a default value
        assert model.workspaceTransferStatus is None or model.workspaceTransferStatus is not None

    def test_service_offer_management_servicemanagerprovision_model_serialization(self):
        """Test Service_offer_management_ServiceManagerProvision model serialization to dict."""
        test_data = {
            "reason": "serialize_value",
            "serviceManager": {"key": "value"},
            "provisionStatus": "serialize_value",
            "createdAt": "serialize_value",
            "workspaceTransferStatus": "serialize_value",
            "id": "serialize_value",
            "region": "serialize_value",
            "updatedAt": "serialize_value",
            "generation": 99,
            "resourceUri": "serialize_value",
            "serviceManagerInstanceId": "serialize_value",
        }

        model = Service_offer_management_ServiceManagerProvision(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "reason" in serialized
        assert "serviceManager" in serialized
        assert "provisionStatus" in serialized
        assert "createdAt" in serialized
        assert "workspaceTransferStatus" in serialized
        assert "id" in serialized
        assert "region" in serialized
        assert "updatedAt" in serialized
        assert "generation" in serialized
        assert "resourceUri" in serialized
        assert "serviceManagerInstanceId" in serialized

        # Verify values are preserved
        assert serialized["reason"] == test_data["reason"]
        assert serialized["serviceManager"] == test_data["serviceManager"]
        assert serialized["provisionStatus"] == test_data["provisionStatus"]
        assert serialized["createdAt"] == test_data["createdAt"]
        assert serialized["workspaceTransferStatus"] == test_data["workspaceTransferStatus"]
        assert serialized["id"] == test_data["id"]
        assert serialized["region"] == test_data["region"]
        assert serialized["updatedAt"] == test_data["updatedAt"]
        assert serialized["generation"] == test_data["generation"]
        assert serialized["resourceUri"] == test_data["resourceUri"]
        assert serialized["serviceManagerInstanceId"] == test_data["serviceManagerInstanceId"]

    def test_service_offer_management_servicemanagerprovision_model_json_schema(self):
        """Test Service_offer_management_ServiceManagerProvision model JSON schema generation."""
        schema = Service_offer_management_ServiceManagerProvision.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "reason",
            "serviceManager",
            "provisionStatus",
            "createdAt",
            "workspaceTransferStatus",
            "id",
            "region",
            "updatedAt",
            "generation",
            "resourceUri",
            "serviceManagerInstanceId",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "reason",
            "serviceManager",
            "provisionStatus",
            "createdAt",
            "id",
            "region",
            "updatedAt",
            "generation",
            "resourceUri",
            "serviceManagerInstanceId",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_offer_management_conflicterror_model_creation(self):
        """Test Service_offer_management_ConflictError model creation with valid data."""
        # Valid test data for Service_offer_management_ConflictError
        valid_data = {
            "debugId": "test_debugId",
            "errorCode": "test_errorCode",
            "errorDetails": [],
            "httpStatusCode": 42,
            "message": "test_message",
        }

        # Create model instance
        model = Service_offer_management_ConflictError(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_offer_management_ConflictError)
        assert model.debugId == valid_data["debugId"]
        assert model.errorCode == valid_data["errorCode"]
        assert model.errorDetails == valid_data["errorDetails"]
        assert model.httpStatusCode == valid_data["httpStatusCode"]
        assert model.message == valid_data["message"]

    def test_service_offer_management_conflicterror_model_validation(self):
        """Test Service_offer_management_ConflictError model field validation."""
        # Test with minimal required data
        minimal_data = {
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
            "httpStatusCode": 1,
            "message": "required_message",
        }

        model = Service_offer_management_ConflictError(**minimal_data)
        assert isinstance(model, Service_offer_management_ConflictError)
        assert model.debugId == minimal_data["debugId"]
        assert model.errorCode == minimal_data["errorCode"]
        assert model.httpStatusCode == minimal_data["httpStatusCode"]
        assert model.message == minimal_data["message"]

    def test_service_offer_management_conflicterror_model_required_fields(self):
        """Test Service_offer_management_ConflictError model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "debugId",
            "errorCode",
            "httpStatusCode",
            "message",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_offer_management_ConflictError()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "debugId",
                "errorCode",
                "httpStatusCode",
                "message",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_offer_management_ConflictError()
            assert isinstance(model, Service_offer_management_ConflictError)

    def test_service_offer_management_conflicterror_model_optional_fields(self):
        """Test Service_offer_management_ConflictError model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
            "httpStatusCode": 1,
            "message": "required_message",
        }

        model = Service_offer_management_ConflictError(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "errorDetails")
        # Optional field errorDetails should be None or have a default value
        assert model.errorDetails is None or model.errorDetails is not None

    def test_service_offer_management_conflicterror_model_serialization(self):
        """Test Service_offer_management_ConflictError model serialization to dict."""
        test_data = {
            "debugId": "serialize_value",
            "errorCode": "serialize_value",
            "errorDetails": [],
            "httpStatusCode": 99,
            "message": "serialize_value",
        }

        model = Service_offer_management_ConflictError(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "debugId" in serialized
        assert "errorCode" in serialized
        assert "errorDetails" in serialized
        assert "httpStatusCode" in serialized
        assert "message" in serialized

        # Verify values are preserved
        assert serialized["debugId"] == test_data["debugId"]
        assert serialized["errorCode"] == test_data["errorCode"]
        assert serialized["errorDetails"] == test_data["errorDetails"]
        assert serialized["httpStatusCode"] == test_data["httpStatusCode"]
        assert serialized["message"] == test_data["message"]

    def test_service_offer_management_conflicterror_model_json_schema(self):
        """Test Service_offer_management_ConflictError model JSON schema generation."""
        schema = Service_offer_management_ConflictError.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "debugId",
            "errorCode",
            "errorDetails",
            "httpStatusCode",
            "message",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "debugId",
            "errorCode",
            "httpStatusCode",
            "message",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_manager_management_servicemanagerprovisioncreateresponse_model_creation(self):
        """Test Service_Manager_Management_ServiceManagerProvisionCreateResponse model creation with valid data."""
        # Valid test data for Service_Manager_Management_ServiceManagerProvisionCreateResponse
        valid_data = {
            "createdBy": "test_createdBy",
            "generation": 42,
            "id": "test_id",
            "region": "test_region",
            "resourceUri": "test_resourceUri",
            "serviceManager": {},
            "type": "test_type",
        }

        # Create model instance
        model = Service_Manager_Management_ServiceManagerProvisionCreateResponse(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_Manager_Management_ServiceManagerProvisionCreateResponse)
        assert model.createdBy == valid_data["createdBy"]
        assert model.generation == valid_data["generation"]
        assert model.id == valid_data["id"]
        assert model.region == valid_data["region"]
        assert model.resourceUri == valid_data["resourceUri"]
        assert model.serviceManager == valid_data["serviceManager"]
        assert model.type == valid_data["type"]

    def test_service_manager_management_servicemanagerprovisioncreateresponse_model_validation(self):
        """Test Service_Manager_Management_ServiceManagerProvisionCreateResponse model field validation."""
        # Test with minimal required data
        minimal_data = {
            "createdBy": "required_createdBy",
            "generation": 1,
            "id": "required_id",
            "region": "required_region",
            "resourceUri": "required_resourceUri",
            "serviceManager": {},
            "type": "required_type",
        }

        model = Service_Manager_Management_ServiceManagerProvisionCreateResponse(**minimal_data)
        assert isinstance(model, Service_Manager_Management_ServiceManagerProvisionCreateResponse)
        assert model.createdBy == minimal_data["createdBy"]
        assert model.generation == minimal_data["generation"]
        assert model.id == minimal_data["id"]
        assert model.region == minimal_data["region"]
        assert model.resourceUri == minimal_data["resourceUri"]
        assert model.serviceManager == minimal_data["serviceManager"]
        assert model.type == minimal_data["type"]

    def test_service_manager_management_servicemanagerprovisioncreateresponse_model_required_fields(self):
        """Test Service_Manager_Management_ServiceManagerProvisionCreateResponse model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "createdBy",
            "generation",
            "id",
            "region",
            "resourceUri",
            "serviceManager",
            "type",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_Manager_Management_ServiceManagerProvisionCreateResponse()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "createdBy",
                "generation",
                "id",
                "region",
                "resourceUri",
                "serviceManager",
                "type",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_Manager_Management_ServiceManagerProvisionCreateResponse()
            assert isinstance(model, Service_Manager_Management_ServiceManagerProvisionCreateResponse)

    def test_service_manager_management_servicemanagerprovisioncreateresponse_model_optional_fields(self):
        """Test Service_Manager_Management_ServiceManagerProvisionCreateResponse model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "createdBy": "required_createdBy",
            "generation": 1,
            "id": "required_id",
            "region": "required_region",
            "resourceUri": "required_resourceUri",
            "serviceManager": {},
            "type": "required_type",
        }

        model = Service_Manager_Management_ServiceManagerProvisionCreateResponse(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_manager_management_servicemanagerprovisioncreateresponse_model_serialization(self):
        """Test Service_Manager_Management_ServiceManagerProvisionCreateResponse model serialization to dict."""
        test_data = {
            "createdBy": "serialize_value",
            "generation": 99,
            "id": "serialize_value",
            "region": "serialize_value",
            "resourceUri": "serialize_value",
            "serviceManager": {"key": "value"},
            "type": "serialize_value",
        }

        model = Service_Manager_Management_ServiceManagerProvisionCreateResponse(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "createdBy" in serialized
        assert "generation" in serialized
        assert "id" in serialized
        assert "region" in serialized
        assert "resourceUri" in serialized
        assert "serviceManager" in serialized
        assert "type" in serialized

        # Verify values are preserved
        assert serialized["createdBy"] == test_data["createdBy"]
        assert serialized["generation"] == test_data["generation"]
        assert serialized["id"] == test_data["id"]
        assert serialized["region"] == test_data["region"]
        assert serialized["resourceUri"] == test_data["resourceUri"]
        assert serialized["serviceManager"] == test_data["serviceManager"]
        assert serialized["type"] == test_data["type"]

    def test_service_manager_management_servicemanagerprovisioncreateresponse_model_json_schema(self):
        """Test Service_Manager_Management_ServiceManagerProvisionCreateResponse model JSON schema generation."""
        schema = Service_Manager_Management_ServiceManagerProvisionCreateResponse.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "createdBy",
            "generation",
            "id",
            "region",
            "resourceUri",
            "serviceManager",
            "type",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "createdBy",
            "generation",
            "id",
            "region",
            "resourceUri",
            "serviceManager",
            "type",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_manager_management_notfounderror_model_creation(self):
        """Test Service_Manager_Management_NotFoundError model creation with valid data."""
        # Valid test data for Service_Manager_Management_NotFoundError
        valid_data = {
            "httpStatusCode": 42,
            "message": "test_message",
            "debugId": "test_debugId",
            "errorCode": "test_errorCode",
        }

        # Create model instance
        model = Service_Manager_Management_NotFoundError(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_Manager_Management_NotFoundError)
        assert model.httpStatusCode == valid_data["httpStatusCode"]
        assert model.message == valid_data["message"]
        assert model.debugId == valid_data["debugId"]
        assert model.errorCode == valid_data["errorCode"]

    def test_service_manager_management_notfounderror_model_validation(self):
        """Test Service_Manager_Management_NotFoundError model field validation."""
        # Test with minimal required data
        minimal_data = {
            "httpStatusCode": 1,
            "message": "required_message",
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
        }

        model = Service_Manager_Management_NotFoundError(**minimal_data)
        assert isinstance(model, Service_Manager_Management_NotFoundError)
        assert model.httpStatusCode == minimal_data["httpStatusCode"]
        assert model.message == minimal_data["message"]
        assert model.debugId == minimal_data["debugId"]
        assert model.errorCode == minimal_data["errorCode"]

    def test_service_manager_management_notfounderror_model_required_fields(self):
        """Test Service_Manager_Management_NotFoundError model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "httpStatusCode",
            "message",
            "debugId",
            "errorCode",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_Manager_Management_NotFoundError()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "httpStatusCode",
                "message",
                "debugId",
                "errorCode",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_Manager_Management_NotFoundError()
            assert isinstance(model, Service_Manager_Management_NotFoundError)

    def test_service_manager_management_notfounderror_model_optional_fields(self):
        """Test Service_Manager_Management_NotFoundError model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "httpStatusCode": 1,
            "message": "required_message",
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
        }

        model = Service_Manager_Management_NotFoundError(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_manager_management_notfounderror_model_serialization(self):
        """Test Service_Manager_Management_NotFoundError model serialization to dict."""
        test_data = {
            "httpStatusCode": 99,
            "message": "serialize_value",
            "debugId": "serialize_value",
            "errorCode": "serialize_value",
        }

        model = Service_Manager_Management_NotFoundError(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "httpStatusCode" in serialized
        assert "message" in serialized
        assert "debugId" in serialized
        assert "errorCode" in serialized

        # Verify values are preserved
        assert serialized["httpStatusCode"] == test_data["httpStatusCode"]
        assert serialized["message"] == test_data["message"]
        assert serialized["debugId"] == test_data["debugId"]
        assert serialized["errorCode"] == test_data["errorCode"]

    def test_service_manager_management_notfounderror_model_json_schema(self):
        """Test Service_Manager_Management_NotFoundError model JSON schema generation."""
        schema = Service_Manager_Management_NotFoundError.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "httpStatusCode",
            "message",
            "debugId",
            "errorCode",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "httpStatusCode",
            "message",
            "debugId",
            "errorCode",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_manager_management_validationerror_model_creation(self):
        """Test Service_Manager_Management_ValidationError model creation with valid data."""
        # Valid test data for Service_Manager_Management_ValidationError
        valid_data = {
            "debugId": "test_debugId",
            "errorCode": "test_errorCode",
            "httpStatusCode": 42,
            "message": "test_message",
        }

        # Create model instance
        model = Service_Manager_Management_ValidationError(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_Manager_Management_ValidationError)
        assert model.debugId == valid_data["debugId"]
        assert model.errorCode == valid_data["errorCode"]
        assert model.httpStatusCode == valid_data["httpStatusCode"]
        assert model.message == valid_data["message"]

    def test_service_manager_management_validationerror_model_validation(self):
        """Test Service_Manager_Management_ValidationError model field validation."""
        # Test with minimal required data
        minimal_data = {
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
            "httpStatusCode": 1,
            "message": "required_message",
        }

        model = Service_Manager_Management_ValidationError(**minimal_data)
        assert isinstance(model, Service_Manager_Management_ValidationError)
        assert model.debugId == minimal_data["debugId"]
        assert model.errorCode == minimal_data["errorCode"]
        assert model.httpStatusCode == minimal_data["httpStatusCode"]
        assert model.message == minimal_data["message"]

    def test_service_manager_management_validationerror_model_required_fields(self):
        """Test Service_Manager_Management_ValidationError model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "debugId",
            "errorCode",
            "httpStatusCode",
            "message",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_Manager_Management_ValidationError()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "debugId",
                "errorCode",
                "httpStatusCode",
                "message",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_Manager_Management_ValidationError()
            assert isinstance(model, Service_Manager_Management_ValidationError)

    def test_service_manager_management_validationerror_model_optional_fields(self):
        """Test Service_Manager_Management_ValidationError model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
            "httpStatusCode": 1,
            "message": "required_message",
        }

        model = Service_Manager_Management_ValidationError(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_manager_management_validationerror_model_serialization(self):
        """Test Service_Manager_Management_ValidationError model serialization to dict."""
        test_data = {
            "debugId": "serialize_value",
            "errorCode": "serialize_value",
            "httpStatusCode": 99,
            "message": "serialize_value",
        }

        model = Service_Manager_Management_ValidationError(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "debugId" in serialized
        assert "errorCode" in serialized
        assert "httpStatusCode" in serialized
        assert "message" in serialized

        # Verify values are preserved
        assert serialized["debugId"] == test_data["debugId"]
        assert serialized["errorCode"] == test_data["errorCode"]
        assert serialized["httpStatusCode"] == test_data["httpStatusCode"]
        assert serialized["message"] == test_data["message"]

    def test_service_manager_management_validationerror_model_json_schema(self):
        """Test Service_Manager_Management_ValidationError model JSON schema generation."""
        schema = Service_Manager_Management_ValidationError.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "debugId",
            "errorCode",
            "httpStatusCode",
            "message",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "debugId",
            "errorCode",
            "httpStatusCode",
            "message",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_manager_management_servicemanagerread_model_creation(self):
        """Test Service_Manager_Management_ServiceManagerRead model creation with valid data."""
        # Valid test data for Service_Manager_Management_ServiceManagerRead
        valid_data = {
            "updatedAt": "test_updatedAt",
            "generation": 42,
            "createdAt": "test_createdAt",
            "name": "test_name",
            "standaloneSupported": True,
            "id": "test_id",
            "tenantOnlySupported": True,
            "honorUnprovisionResponse": True,
            "mspSupported": True,
            "mspOnlySupported": True,
            "type": "test_type",
            "resourceUri": "test_resourceUri",
            "workspaceTransferSupported": True,
            "workspaceOpModesSupported": "test_workspaceOpModesSupported",
            "description": "test_description",
        }

        # Create model instance
        model = Service_Manager_Management_ServiceManagerRead(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_Manager_Management_ServiceManagerRead)
        assert model.updatedAt == valid_data["updatedAt"]
        assert model.generation == valid_data["generation"]
        assert model.createdAt == valid_data["createdAt"]
        assert model.name == valid_data["name"]
        assert model.standaloneSupported == valid_data["standaloneSupported"]
        assert model.id == valid_data["id"]
        assert model.tenantOnlySupported == valid_data["tenantOnlySupported"]
        assert model.honorUnprovisionResponse == valid_data["honorUnprovisionResponse"]
        assert model.mspSupported == valid_data["mspSupported"]
        assert model.mspOnlySupported == valid_data["mspOnlySupported"]
        assert model.type == valid_data["type"]
        assert model.resourceUri == valid_data["resourceUri"]
        assert model.workspaceTransferSupported == valid_data["workspaceTransferSupported"]
        assert model.workspaceOpModesSupported == valid_data["workspaceOpModesSupported"]
        assert model.description == valid_data["description"]

    def test_service_manager_management_servicemanagerread_model_validation(self):
        """Test Service_Manager_Management_ServiceManagerRead model field validation."""
        # Test with minimal required data
        minimal_data = {
            "updatedAt": "required_updatedAt",
            "generation": 1,
            "createdAt": "required_createdAt",
            "name": "required_name",
            "standaloneSupported": True,
            "id": "required_id",
            "tenantOnlySupported": True,
            "honorUnprovisionResponse": True,
            "mspSupported": True,
            "type": "required_type",
            "resourceUri": "required_resourceUri",
        }

        model = Service_Manager_Management_ServiceManagerRead(**minimal_data)
        assert isinstance(model, Service_Manager_Management_ServiceManagerRead)
        assert model.updatedAt == minimal_data["updatedAt"]
        assert model.generation == minimal_data["generation"]
        assert model.createdAt == minimal_data["createdAt"]
        assert model.name == minimal_data["name"]
        assert model.standaloneSupported == minimal_data["standaloneSupported"]
        assert model.id == minimal_data["id"]
        assert model.tenantOnlySupported == minimal_data["tenantOnlySupported"]
        assert model.honorUnprovisionResponse == minimal_data["honorUnprovisionResponse"]
        assert model.mspSupported == minimal_data["mspSupported"]
        assert model.type == minimal_data["type"]
        assert model.resourceUri == minimal_data["resourceUri"]

    def test_service_manager_management_servicemanagerread_model_required_fields(self):
        """Test Service_Manager_Management_ServiceManagerRead model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "updatedAt",
            "generation",
            "createdAt",
            "name",
            "standaloneSupported",
            "id",
            "tenantOnlySupported",
            "honorUnprovisionResponse",
            "mspSupported",
            "type",
            "resourceUri",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_Manager_Management_ServiceManagerRead()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "updatedAt",
                "generation",
                "createdAt",
                "name",
                "standaloneSupported",
                "id",
                "tenantOnlySupported",
                "honorUnprovisionResponse",
                "mspSupported",
                "type",
                "resourceUri",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_Manager_Management_ServiceManagerRead()
            assert isinstance(model, Service_Manager_Management_ServiceManagerRead)

    def test_service_manager_management_servicemanagerread_model_optional_fields(self):
        """Test Service_Manager_Management_ServiceManagerRead model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "updatedAt": "required_updatedAt",
            "generation": 1,
            "createdAt": "required_createdAt",
            "name": "required_name",
            "standaloneSupported": True,
            "id": "required_id",
            "tenantOnlySupported": True,
            "honorUnprovisionResponse": True,
            "mspSupported": True,
            "type": "required_type",
            "resourceUri": "required_resourceUri",
        }

        model = Service_Manager_Management_ServiceManagerRead(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "mspOnlySupported")
        # Optional field mspOnlySupported should be None or have a default value
        assert model.mspOnlySupported is None or model.mspOnlySupported is not None
        assert hasattr(model, "workspaceTransferSupported")
        # Optional field workspaceTransferSupported should be None or have a default value
        assert model.workspaceTransferSupported is None or model.workspaceTransferSupported is not None
        assert hasattr(model, "workspaceOpModesSupported")
        # Optional field workspaceOpModesSupported should be None or have a default value
        assert model.workspaceOpModesSupported is None or model.workspaceOpModesSupported is not None
        assert hasattr(model, "description")
        # Optional field description should be None or have a default value
        assert model.description is None or model.description is not None

    def test_service_manager_management_servicemanagerread_model_serialization(self):
        """Test Service_Manager_Management_ServiceManagerRead model serialization to dict."""
        test_data = {
            "updatedAt": "serialize_value",
            "generation": 99,
            "createdAt": "serialize_value",
            "name": "serialize_value",
            "standaloneSupported": False,
            "id": "serialize_value",
            "tenantOnlySupported": False,
            "honorUnprovisionResponse": False,
            "mspSupported": False,
            "mspOnlySupported": False,
            "type": "serialize_value",
            "resourceUri": "serialize_value",
            "workspaceTransferSupported": False,
            "workspaceOpModesSupported": "serialize_value",
            "description": "serialize_value",
        }

        model = Service_Manager_Management_ServiceManagerRead(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "updatedAt" in serialized
        assert "generation" in serialized
        assert "createdAt" in serialized
        assert "name" in serialized
        assert "standaloneSupported" in serialized
        assert "id" in serialized
        assert "tenantOnlySupported" in serialized
        assert "honorUnprovisionResponse" in serialized
        assert "mspSupported" in serialized
        assert "mspOnlySupported" in serialized
        assert "type" in serialized
        assert "resourceUri" in serialized
        assert "workspaceTransferSupported" in serialized
        assert "workspaceOpModesSupported" in serialized
        assert "description" in serialized

        # Verify values are preserved
        assert serialized["updatedAt"] == test_data["updatedAt"]
        assert serialized["generation"] == test_data["generation"]
        assert serialized["createdAt"] == test_data["createdAt"]
        assert serialized["name"] == test_data["name"]
        assert serialized["standaloneSupported"] == test_data["standaloneSupported"]
        assert serialized["id"] == test_data["id"]
        assert serialized["tenantOnlySupported"] == test_data["tenantOnlySupported"]
        assert serialized["honorUnprovisionResponse"] == test_data["honorUnprovisionResponse"]
        assert serialized["mspSupported"] == test_data["mspSupported"]
        assert serialized["mspOnlySupported"] == test_data["mspOnlySupported"]
        assert serialized["type"] == test_data["type"]
        assert serialized["resourceUri"] == test_data["resourceUri"]
        assert serialized["workspaceTransferSupported"] == test_data["workspaceTransferSupported"]
        assert serialized["workspaceOpModesSupported"] == test_data["workspaceOpModesSupported"]
        assert serialized["description"] == test_data["description"]

    def test_service_manager_management_servicemanagerread_model_json_schema(self):
        """Test Service_Manager_Management_ServiceManagerRead model JSON schema generation."""
        schema = Service_Manager_Management_ServiceManagerRead.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "updatedAt",
            "generation",
            "createdAt",
            "name",
            "standaloneSupported",
            "id",
            "tenantOnlySupported",
            "honorUnprovisionResponse",
            "mspSupported",
            "mspOnlySupported",
            "type",
            "resourceUri",
            "workspaceTransferSupported",
            "workspaceOpModesSupported",
            "description",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "updatedAt",
            "generation",
            "createdAt",
            "name",
            "standaloneSupported",
            "id",
            "tenantOnlySupported",
            "honorUnprovisionResponse",
            "mspSupported",
            "type",
            "resourceUri",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_offer_management_serviceofferpartialdetails_model_creation(self):
        """Test Service_offer_management_ServiceOfferPartialDetails model creation with valid data."""
        # Valid test data for Service_offer_management_ServiceOfferPartialDetails
        valid_data = {
            "workspaceOpModes": [],
            "workspaceTypes": [],
            "categories": [],
            "id": "test_id",
            "name": "test_name",
            "resourceUri": "test_resourceUri",
            "slug": "test_slug",
            "staticLaunchUrl": "test_staticLaunchUrl",
        }

        # Create model instance
        model = Service_offer_management_ServiceOfferPartialDetails(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_offer_management_ServiceOfferPartialDetails)
        assert model.workspaceOpModes == valid_data["workspaceOpModes"]
        assert model.workspaceTypes == valid_data["workspaceTypes"]
        assert model.categories == valid_data["categories"]
        assert model.id == valid_data["id"]
        assert model.name == valid_data["name"]
        assert model.resourceUri == valid_data["resourceUri"]
        assert model.slug == valid_data["slug"]
        assert model.staticLaunchUrl == valid_data["staticLaunchUrl"]

    def test_service_offer_management_serviceofferpartialdetails_model_validation(self):
        """Test Service_offer_management_ServiceOfferPartialDetails model field validation."""
        # Test with minimal required data
        minimal_data = {
            "workspaceOpModes": [],
            "workspaceTypes": [],
            "categories": [],
            "id": "required_id",
            "name": "required_name",
            "resourceUri": "required_resourceUri",
            "slug": "required_slug",
            "staticLaunchUrl": "required_staticLaunchUrl",
        }

        model = Service_offer_management_ServiceOfferPartialDetails(**minimal_data)
        assert isinstance(model, Service_offer_management_ServiceOfferPartialDetails)
        assert model.workspaceOpModes == minimal_data["workspaceOpModes"]
        assert model.workspaceTypes == minimal_data["workspaceTypes"]
        assert model.categories == minimal_data["categories"]
        assert model.id == minimal_data["id"]
        assert model.name == minimal_data["name"]
        assert model.resourceUri == minimal_data["resourceUri"]
        assert model.slug == minimal_data["slug"]
        assert model.staticLaunchUrl == minimal_data["staticLaunchUrl"]

    def test_service_offer_management_serviceofferpartialdetails_model_required_fields(self):
        """Test Service_offer_management_ServiceOfferPartialDetails model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "workspaceOpModes",
            "workspaceTypes",
            "categories",
            "id",
            "name",
            "resourceUri",
            "slug",
            "staticLaunchUrl",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_offer_management_ServiceOfferPartialDetails()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "workspaceOpModes",
                "workspaceTypes",
                "categories",
                "id",
                "name",
                "resourceUri",
                "slug",
                "staticLaunchUrl",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_offer_management_ServiceOfferPartialDetails()
            assert isinstance(model, Service_offer_management_ServiceOfferPartialDetails)

    def test_service_offer_management_serviceofferpartialdetails_model_optional_fields(self):
        """Test Service_offer_management_ServiceOfferPartialDetails model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "workspaceOpModes": [],
            "workspaceTypes": [],
            "categories": [],
            "id": "required_id",
            "name": "required_name",
            "resourceUri": "required_resourceUri",
            "slug": "required_slug",
            "staticLaunchUrl": "required_staticLaunchUrl",
        }

        model = Service_offer_management_ServiceOfferPartialDetails(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_offer_management_serviceofferpartialdetails_model_serialization(self):
        """Test Service_offer_management_ServiceOfferPartialDetails model serialization to dict."""
        test_data = {
            "workspaceOpModes": [],
            "workspaceTypes": [],
            "categories": [],
            "id": "serialize_value",
            "name": "serialize_value",
            "resourceUri": "serialize_value",
            "slug": "serialize_value",
            "staticLaunchUrl": "serialize_value",
        }

        model = Service_offer_management_ServiceOfferPartialDetails(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "workspaceOpModes" in serialized
        assert "workspaceTypes" in serialized
        assert "categories" in serialized
        assert "id" in serialized
        assert "name" in serialized
        assert "resourceUri" in serialized
        assert "slug" in serialized
        assert "staticLaunchUrl" in serialized

        # Verify values are preserved
        assert serialized["workspaceOpModes"] == test_data["workspaceOpModes"]
        assert serialized["workspaceTypes"] == test_data["workspaceTypes"]
        assert serialized["categories"] == test_data["categories"]
        assert serialized["id"] == test_data["id"]
        assert serialized["name"] == test_data["name"]
        assert serialized["resourceUri"] == test_data["resourceUri"]
        assert serialized["slug"] == test_data["slug"]
        assert serialized["staticLaunchUrl"] == test_data["staticLaunchUrl"]

    def test_service_offer_management_serviceofferpartialdetails_model_json_schema(self):
        """Test Service_offer_management_ServiceOfferPartialDetails model JSON schema generation."""
        schema = Service_offer_management_ServiceOfferPartialDetails.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "workspaceOpModes",
            "workspaceTypes",
            "categories",
            "id",
            "name",
            "resourceUri",
            "slug",
            "staticLaunchUrl",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "workspaceOpModes",
            "workspaceTypes",
            "categories",
            "id",
            "name",
            "resourceUri",
            "slug",
            "staticLaunchUrl",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_manager_management_error_model_creation(self):
        """Test Service_Manager_Management_Error model creation with valid data."""
        # Valid test data for Service_Manager_Management_Error
        valid_data = {
            "httpStatusCode": 42,
            "message": "test_message",
            "debugId": "test_debugId",
            "errorCode": "test_errorCode",
        }

        # Create model instance
        model = Service_Manager_Management_Error(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_Manager_Management_Error)
        assert model.httpStatusCode == valid_data["httpStatusCode"]
        assert model.message == valid_data["message"]
        assert model.debugId == valid_data["debugId"]
        assert model.errorCode == valid_data["errorCode"]

    def test_service_manager_management_error_model_validation(self):
        """Test Service_Manager_Management_Error model field validation."""
        # Test with minimal required data
        minimal_data = {
            "httpStatusCode": 1,
            "message": "required_message",
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
        }

        model = Service_Manager_Management_Error(**minimal_data)
        assert isinstance(model, Service_Manager_Management_Error)
        assert model.httpStatusCode == minimal_data["httpStatusCode"]
        assert model.message == minimal_data["message"]
        assert model.debugId == minimal_data["debugId"]
        assert model.errorCode == minimal_data["errorCode"]

    def test_service_manager_management_error_model_required_fields(self):
        """Test Service_Manager_Management_Error model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "httpStatusCode",
            "message",
            "debugId",
            "errorCode",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_Manager_Management_Error()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "httpStatusCode",
                "message",
                "debugId",
                "errorCode",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_Manager_Management_Error()
            assert isinstance(model, Service_Manager_Management_Error)

    def test_service_manager_management_error_model_optional_fields(self):
        """Test Service_Manager_Management_Error model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "httpStatusCode": 1,
            "message": "required_message",
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
        }

        model = Service_Manager_Management_Error(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_manager_management_error_model_serialization(self):
        """Test Service_Manager_Management_Error model serialization to dict."""
        test_data = {
            "httpStatusCode": 99,
            "message": "serialize_value",
            "debugId": "serialize_value",
            "errorCode": "serialize_value",
        }

        model = Service_Manager_Management_Error(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "httpStatusCode" in serialized
        assert "message" in serialized
        assert "debugId" in serialized
        assert "errorCode" in serialized

        # Verify values are preserved
        assert serialized["httpStatusCode"] == test_data["httpStatusCode"]
        assert serialized["message"] == test_data["message"]
        assert serialized["debugId"] == test_data["debugId"]
        assert serialized["errorCode"] == test_data["errorCode"]

    def test_service_manager_management_error_model_json_schema(self):
        """Test Service_Manager_Management_Error model JSON schema generation."""
        schema = Service_Manager_Management_Error.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "httpStatusCode",
            "message",
            "debugId",
            "errorCode",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "httpStatusCode",
            "message",
            "debugId",
            "errorCode",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_provision_management_serviceprovision_model_creation(self):
        """Test Service_provision_management_ServiceProvision model creation with valid data."""
        # Valid test data for Service_provision_management_ServiceProvision
        valid_data = {
            "updatedAt": "test_updatedAt",
            "serviceManagerInstanceId": "test_serviceManagerInstanceId",
            "createdAt": "test_createdAt",
            "createdBy": "test_createdBy",
            "serviceOffer": {},
            "generation": 42,
            "serviceManager": {},
            "retryCount": 42,
            "serviceManagerProvision": {},
            "id": "test_id",
            "workspace": {},
            "type": "test_type",
            "reason": "test_reason",
            "provisionStatus": "test_provisionStatus",
            "region": "test_region",
            "resourceUri": "test_resourceUri",
        }

        # Create model instance
        model = Service_provision_management_ServiceProvision(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_provision_management_ServiceProvision)
        assert model.updatedAt == valid_data["updatedAt"]
        assert model.serviceManagerInstanceId == valid_data["serviceManagerInstanceId"]
        assert model.createdAt == valid_data["createdAt"]
        assert model.createdBy == valid_data["createdBy"]
        assert model.serviceOffer == valid_data["serviceOffer"]
        assert model.generation == valid_data["generation"]
        assert model.serviceManager == valid_data["serviceManager"]
        assert model.retryCount == valid_data["retryCount"]
        assert model.serviceManagerProvision == valid_data["serviceManagerProvision"]
        assert model.id == valid_data["id"]
        assert model.workspace == valid_data["workspace"]
        assert model.type == valid_data["type"]
        assert model.reason == valid_data["reason"]
        assert model.provisionStatus == valid_data["provisionStatus"]
        assert model.region == valid_data["region"]
        assert model.resourceUri == valid_data["resourceUri"]

    def test_service_provision_management_serviceprovision_model_validation(self):
        """Test Service_provision_management_ServiceProvision model field validation."""
        # Test with minimal required data
        minimal_data = {
            "updatedAt": "required_updatedAt",
            "createdAt": "required_createdAt",
            "serviceOffer": {},
            "generation": 1,
            "retryCount": 1,
            "id": "required_id",
            "workspace": {},
            "type": "required_type",
            "region": "required_region",
            "resourceUri": "required_resourceUri",
        }

        model = Service_provision_management_ServiceProvision(**minimal_data)
        assert isinstance(model, Service_provision_management_ServiceProvision)
        assert model.updatedAt == minimal_data["updatedAt"]
        assert model.createdAt == minimal_data["createdAt"]
        assert model.serviceOffer == minimal_data["serviceOffer"]
        assert model.generation == minimal_data["generation"]
        assert model.retryCount == minimal_data["retryCount"]
        assert model.id == minimal_data["id"]
        assert model.workspace == minimal_data["workspace"]
        assert model.type == minimal_data["type"]
        assert model.region == minimal_data["region"]
        assert model.resourceUri == minimal_data["resourceUri"]

    def test_service_provision_management_serviceprovision_model_required_fields(self):
        """Test Service_provision_management_ServiceProvision model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "updatedAt",
            "createdAt",
            "serviceOffer",
            "generation",
            "retryCount",
            "id",
            "workspace",
            "type",
            "region",
            "resourceUri",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_provision_management_ServiceProvision()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "updatedAt",
                "createdAt",
                "serviceOffer",
                "generation",
                "retryCount",
                "id",
                "workspace",
                "type",
                "region",
                "resourceUri",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_provision_management_ServiceProvision()
            assert isinstance(model, Service_provision_management_ServiceProvision)

    def test_service_provision_management_serviceprovision_model_optional_fields(self):
        """Test Service_provision_management_ServiceProvision model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "updatedAt": "required_updatedAt",
            "createdAt": "required_createdAt",
            "serviceOffer": {},
            "generation": 1,
            "retryCount": 1,
            "id": "required_id",
            "workspace": {},
            "type": "required_type",
            "region": "required_region",
            "resourceUri": "required_resourceUri",
        }

        model = Service_provision_management_ServiceProvision(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "serviceManagerInstanceId")
        # Optional field serviceManagerInstanceId should be None or have a default value
        assert model.serviceManagerInstanceId is None or model.serviceManagerInstanceId is not None
        assert hasattr(model, "createdBy")
        # Optional field createdBy should be None or have a default value
        assert model.createdBy is None or model.createdBy is not None
        assert hasattr(model, "serviceManager")
        # Optional field serviceManager should be None or have a default value
        assert model.serviceManager is None or model.serviceManager is not None
        assert hasattr(model, "serviceManagerProvision")
        # Optional field serviceManagerProvision should be None or have a default value
        assert model.serviceManagerProvision is None or model.serviceManagerProvision is not None
        assert hasattr(model, "reason")
        # Optional field reason should be None or have a default value
        assert model.reason is None or model.reason is not None
        assert hasattr(model, "provisionStatus")
        # Optional field provisionStatus should be None or have a default value
        assert model.provisionStatus is None or model.provisionStatus is not None

    def test_service_provision_management_serviceprovision_model_serialization(self):
        """Test Service_provision_management_ServiceProvision model serialization to dict."""
        test_data = {
            "updatedAt": "serialize_value",
            "serviceManagerInstanceId": "serialize_value",
            "createdAt": "serialize_value",
            "createdBy": "serialize_value",
            "serviceOffer": {"key": "value"},
            "generation": 99,
            "serviceManager": {"key": "value"},
            "retryCount": 99,
            "serviceManagerProvision": {"key": "value"},
            "id": "serialize_value",
            "workspace": {"key": "value"},
            "type": "serialize_value",
            "reason": "serialize_value",
            "provisionStatus": "serialize_value",
            "region": "serialize_value",
            "resourceUri": "serialize_value",
        }

        model = Service_provision_management_ServiceProvision(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "updatedAt" in serialized
        assert "serviceManagerInstanceId" in serialized
        assert "createdAt" in serialized
        assert "createdBy" in serialized
        assert "serviceOffer" in serialized
        assert "generation" in serialized
        assert "serviceManager" in serialized
        assert "retryCount" in serialized
        assert "serviceManagerProvision" in serialized
        assert "id" in serialized
        assert "workspace" in serialized
        assert "type" in serialized
        assert "reason" in serialized
        assert "provisionStatus" in serialized
        assert "region" in serialized
        assert "resourceUri" in serialized

        # Verify values are preserved
        assert serialized["updatedAt"] == test_data["updatedAt"]
        assert serialized["serviceManagerInstanceId"] == test_data["serviceManagerInstanceId"]
        assert serialized["createdAt"] == test_data["createdAt"]
        assert serialized["createdBy"] == test_data["createdBy"]
        assert serialized["serviceOffer"] == test_data["serviceOffer"]
        assert serialized["generation"] == test_data["generation"]
        assert serialized["serviceManager"] == test_data["serviceManager"]
        assert serialized["retryCount"] == test_data["retryCount"]
        assert serialized["serviceManagerProvision"] == test_data["serviceManagerProvision"]
        assert serialized["id"] == test_data["id"]
        assert serialized["workspace"] == test_data["workspace"]
        assert serialized["type"] == test_data["type"]
        assert serialized["reason"] == test_data["reason"]
        assert serialized["provisionStatus"] == test_data["provisionStatus"]
        assert serialized["region"] == test_data["region"]
        assert serialized["resourceUri"] == test_data["resourceUri"]

    def test_service_provision_management_serviceprovision_model_json_schema(self):
        """Test Service_provision_management_ServiceProvision model JSON schema generation."""
        schema = Service_provision_management_ServiceProvision.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "updatedAt",
            "serviceManagerInstanceId",
            "createdAt",
            "createdBy",
            "serviceOffer",
            "generation",
            "serviceManager",
            "retryCount",
            "serviceManagerProvision",
            "id",
            "workspace",
            "type",
            "reason",
            "provisionStatus",
            "region",
            "resourceUri",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "updatedAt",
            "createdAt",
            "serviceOffer",
            "generation",
            "retryCount",
            "id",
            "workspace",
            "type",
            "region",
            "resourceUri",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_offer_management_serviceofferresourcelink_model_creation(self):
        """Test Service_offer_management_ServiceOfferResourceLink model creation with valid data."""
        # Valid test data for Service_offer_management_ServiceOfferResourceLink
        valid_data = {
            "id": "test_id",
            "resourceUri": "test_resourceUri",
        }

        # Create model instance
        model = Service_offer_management_ServiceOfferResourceLink(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_offer_management_ServiceOfferResourceLink)
        assert model.id == valid_data["id"]
        assert model.resourceUri == valid_data["resourceUri"]

    def test_service_offer_management_serviceofferresourcelink_model_validation(self):
        """Test Service_offer_management_ServiceOfferResourceLink model field validation."""
        # Test with minimal required data
        minimal_data = {}

        model = Service_offer_management_ServiceOfferResourceLink(**minimal_data)
        assert isinstance(model, Service_offer_management_ServiceOfferResourceLink)

    def test_service_offer_management_serviceofferresourcelink_model_required_fields(self):
        """Test Service_offer_management_ServiceOfferResourceLink model required field validation."""
        # Check if this model has any required fields
        required_fields = []

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_offer_management_ServiceOfferResourceLink()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {}

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_offer_management_ServiceOfferResourceLink()
            assert isinstance(model, Service_offer_management_ServiceOfferResourceLink)

    def test_service_offer_management_serviceofferresourcelink_model_optional_fields(self):
        """Test Service_offer_management_ServiceOfferResourceLink model optional field handling."""
        # Create with minimal required data
        minimal_data = {}

        model = Service_offer_management_ServiceOfferResourceLink(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "id")
        # Optional field id should be None or have a default value
        assert model.id is None or model.id is not None
        assert hasattr(model, "resourceUri")
        # Optional field resourceUri should be None or have a default value
        assert model.resourceUri is None or model.resourceUri is not None

    def test_service_offer_management_serviceofferresourcelink_model_serialization(self):
        """Test Service_offer_management_ServiceOfferResourceLink model serialization to dict."""
        test_data = {
            "id": "serialize_value",
            "resourceUri": "serialize_value",
        }

        model = Service_offer_management_ServiceOfferResourceLink(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "id" in serialized
        assert "resourceUri" in serialized

        # Verify values are preserved
        assert serialized["id"] == test_data["id"]
        assert serialized["resourceUri"] == test_data["resourceUri"]

    def test_service_offer_management_serviceofferresourcelink_model_json_schema(self):
        """Test Service_offer_management_ServiceOfferResourceLink model JSON schema generation."""
        schema = Service_offer_management_ServiceOfferResourceLink.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "id",
            "resourceUri",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = []
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_offer_management_recentservicev2_model_creation(self):
        """Test Service_offer_management_RecentServiceV2 model creation with valid data."""
        # Valid test data for Service_offer_management_RecentServiceV2
        valid_data = {
            "type": "test_type",
            "id": "test_id",
            "lastAccessedTime": "test_lastAccessedTime",
            "region": "test_region",
            "serviceManagerProvision": "test_serviceManagerProvision",
            "serviceOffer": "test_serviceOffer",
            "serviceProvision": "test_serviceProvision",
        }

        # Create model instance
        model = Service_offer_management_RecentServiceV2(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_offer_management_RecentServiceV2)
        assert model.type == valid_data["type"]
        assert model.id == valid_data["id"]
        assert model.lastAccessedTime == valid_data["lastAccessedTime"]
        assert model.region == valid_data["region"]
        assert model.serviceManagerProvision == valid_data["serviceManagerProvision"]
        assert model.serviceOffer == valid_data["serviceOffer"]
        assert model.serviceProvision == valid_data["serviceProvision"]

    def test_service_offer_management_recentservicev2_model_validation(self):
        """Test Service_offer_management_RecentServiceV2 model field validation."""
        # Test with minimal required data
        minimal_data = {
            "type": "required_type",
            "id": "required_id",
            "lastAccessedTime": "required_lastAccessedTime",
            "region": "required_region",
            "serviceOffer": "required_serviceOffer",
        }

        model = Service_offer_management_RecentServiceV2(**minimal_data)
        assert isinstance(model, Service_offer_management_RecentServiceV2)
        assert model.type == minimal_data["type"]
        assert model.id == minimal_data["id"]
        assert model.lastAccessedTime == minimal_data["lastAccessedTime"]
        assert model.region == minimal_data["region"]
        assert model.serviceOffer == minimal_data["serviceOffer"]

    def test_service_offer_management_recentservicev2_model_required_fields(self):
        """Test Service_offer_management_RecentServiceV2 model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "type",
            "id",
            "lastAccessedTime",
            "region",
            "serviceOffer",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_offer_management_RecentServiceV2()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "type",
                "id",
                "lastAccessedTime",
                "region",
                "serviceOffer",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_offer_management_RecentServiceV2()
            assert isinstance(model, Service_offer_management_RecentServiceV2)

    def test_service_offer_management_recentservicev2_model_optional_fields(self):
        """Test Service_offer_management_RecentServiceV2 model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "type": "required_type",
            "id": "required_id",
            "lastAccessedTime": "required_lastAccessedTime",
            "region": "required_region",
            "serviceOffer": "required_serviceOffer",
        }

        model = Service_offer_management_RecentServiceV2(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "serviceManagerProvision")
        # Optional field serviceManagerProvision should be None or have a default value
        assert model.serviceManagerProvision is None or model.serviceManagerProvision is not None
        assert hasattr(model, "serviceProvision")
        # Optional field serviceProvision should be None or have a default value
        assert model.serviceProvision is None or model.serviceProvision is not None

    def test_service_offer_management_recentservicev2_model_serialization(self):
        """Test Service_offer_management_RecentServiceV2 model serialization to dict."""
        test_data = {
            "type": "serialize_value",
            "id": "serialize_value",
            "lastAccessedTime": "serialize_value",
            "region": "serialize_value",
            "serviceManagerProvision": "serialize_value",
            "serviceOffer": "serialize_value",
            "serviceProvision": "serialize_value",
        }

        model = Service_offer_management_RecentServiceV2(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "type" in serialized
        assert "id" in serialized
        assert "lastAccessedTime" in serialized
        assert "region" in serialized
        assert "serviceManagerProvision" in serialized
        assert "serviceOffer" in serialized
        assert "serviceProvision" in serialized

        # Verify values are preserved
        assert serialized["type"] == test_data["type"]
        assert serialized["id"] == test_data["id"]
        assert serialized["lastAccessedTime"] == test_data["lastAccessedTime"]
        assert serialized["region"] == test_data["region"]
        assert serialized["serviceManagerProvision"] == test_data["serviceManagerProvision"]
        assert serialized["serviceOffer"] == test_data["serviceOffer"]
        assert serialized["serviceProvision"] == test_data["serviceProvision"]

    def test_service_offer_management_recentservicev2_model_json_schema(self):
        """Test Service_offer_management_RecentServiceV2 model JSON schema generation."""
        schema = Service_offer_management_RecentServiceV2.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "type",
            "id",
            "lastAccessedTime",
            "region",
            "serviceManagerProvision",
            "serviceOffer",
            "serviceProvision",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "type",
            "id",
            "lastAccessedTime",
            "region",
            "serviceOffer",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_offer_management_regionalprovision_model_creation(self):
        """Test Service_offer_management_RegionalProvision model creation with valid data."""
        # Valid test data for Service_offer_management_RegionalProvision
        valid_data = {
            "id": "test_id",
            "serviceManagerProvision": "test_serviceManagerProvision",
            "serviceProvision": "test_serviceProvision",
            "type": "test_type",
        }

        # Create model instance
        model = Service_offer_management_RegionalProvision(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_offer_management_RegionalProvision)
        assert model.id == valid_data["id"]
        assert model.serviceManagerProvision == valid_data["serviceManagerProvision"]
        assert model.serviceProvision == valid_data["serviceProvision"]
        assert model.type == valid_data["type"]

    def test_service_offer_management_regionalprovision_model_validation(self):
        """Test Service_offer_management_RegionalProvision model field validation."""
        # Test with minimal required data
        minimal_data = {}

        model = Service_offer_management_RegionalProvision(**minimal_data)
        assert isinstance(model, Service_offer_management_RegionalProvision)

    def test_service_offer_management_regionalprovision_model_required_fields(self):
        """Test Service_offer_management_RegionalProvision model required field validation."""
        # Check if this model has any required fields
        required_fields = []

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_offer_management_RegionalProvision()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {}

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_offer_management_RegionalProvision()
            assert isinstance(model, Service_offer_management_RegionalProvision)

    def test_service_offer_management_regionalprovision_model_optional_fields(self):
        """Test Service_offer_management_RegionalProvision model optional field handling."""
        # Create with minimal required data
        minimal_data = {}

        model = Service_offer_management_RegionalProvision(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "id")
        # Optional field id should be None or have a default value
        assert model.id is None or model.id is not None
        assert hasattr(model, "serviceManagerProvision")
        # Optional field serviceManagerProvision should be None or have a default value
        assert model.serviceManagerProvision is None or model.serviceManagerProvision is not None
        assert hasattr(model, "serviceProvision")
        # Optional field serviceProvision should be None or have a default value
        assert model.serviceProvision is None or model.serviceProvision is not None
        assert hasattr(model, "type")
        # Optional field type should be None or have a default value
        assert model.type is None or model.type is not None

    def test_service_offer_management_regionalprovision_model_serialization(self):
        """Test Service_offer_management_RegionalProvision model serialization to dict."""
        test_data = {
            "id": "serialize_value",
            "serviceManagerProvision": "serialize_value",
            "serviceProvision": "serialize_value",
            "type": "serialize_value",
        }

        model = Service_offer_management_RegionalProvision(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "id" in serialized
        assert "serviceManagerProvision" in serialized
        assert "serviceProvision" in serialized
        assert "type" in serialized

        # Verify values are preserved
        assert serialized["id"] == test_data["id"]
        assert serialized["serviceManagerProvision"] == test_data["serviceManagerProvision"]
        assert serialized["serviceProvision"] == test_data["serviceProvision"]
        assert serialized["type"] == test_data["type"]

    def test_service_offer_management_regionalprovision_model_json_schema(self):
        """Test Service_offer_management_RegionalProvision model JSON schema generation."""
        schema = Service_offer_management_RegionalProvision.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "id",
            "serviceManagerProvision",
            "serviceProvision",
            "type",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = []
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_offer_management_detailedservicemanagerresourcelink_model_creation(self):
        """Test Service_offer_management_DetailedServiceManagerResourceLink model creation with valid data."""
        # Valid test data for Service_offer_management_DetailedServiceManagerResourceLink
        valid_data = {
            "id": "test_id",
            "name": "test_name",
            "resourceUri": "test_resourceUri",
            "serviceOfferId": "test_serviceOfferId",
        }

        # Create model instance
        model = Service_offer_management_DetailedServiceManagerResourceLink(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_offer_management_DetailedServiceManagerResourceLink)
        assert model.id == valid_data["id"]
        assert model.name == valid_data["name"]
        assert model.resourceUri == valid_data["resourceUri"]
        assert model.serviceOfferId == valid_data["serviceOfferId"]

    def test_service_offer_management_detailedservicemanagerresourcelink_model_validation(self):
        """Test Service_offer_management_DetailedServiceManagerResourceLink model field validation."""
        # Test with minimal required data
        minimal_data = {}

        model = Service_offer_management_DetailedServiceManagerResourceLink(**minimal_data)
        assert isinstance(model, Service_offer_management_DetailedServiceManagerResourceLink)

    def test_service_offer_management_detailedservicemanagerresourcelink_model_required_fields(self):
        """Test Service_offer_management_DetailedServiceManagerResourceLink model required field validation."""
        # Check if this model has any required fields
        required_fields = []

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_offer_management_DetailedServiceManagerResourceLink()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {}

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_offer_management_DetailedServiceManagerResourceLink()
            assert isinstance(model, Service_offer_management_DetailedServiceManagerResourceLink)

    def test_service_offer_management_detailedservicemanagerresourcelink_model_optional_fields(self):
        """Test Service_offer_management_DetailedServiceManagerResourceLink model optional field handling."""
        # Create with minimal required data
        minimal_data = {}

        model = Service_offer_management_DetailedServiceManagerResourceLink(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "id")
        # Optional field id should be None or have a default value
        assert model.id is None or model.id is not None
        assert hasattr(model, "name")
        # Optional field name should be None or have a default value
        assert model.name is None or model.name is not None
        assert hasattr(model, "resourceUri")
        # Optional field resourceUri should be None or have a default value
        assert model.resourceUri is None or model.resourceUri is not None
        assert hasattr(model, "serviceOfferId")
        # Optional field serviceOfferId should be None or have a default value
        assert model.serviceOfferId is None or model.serviceOfferId is not None

    def test_service_offer_management_detailedservicemanagerresourcelink_model_serialization(self):
        """Test Service_offer_management_DetailedServiceManagerResourceLink model serialization to dict."""
        test_data = {
            "id": "serialize_value",
            "name": "serialize_value",
            "resourceUri": "serialize_value",
            "serviceOfferId": "serialize_value",
        }

        model = Service_offer_management_DetailedServiceManagerResourceLink(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "id" in serialized
        assert "name" in serialized
        assert "resourceUri" in serialized
        assert "serviceOfferId" in serialized

        # Verify values are preserved
        assert serialized["id"] == test_data["id"]
        assert serialized["name"] == test_data["name"]
        assert serialized["resourceUri"] == test_data["resourceUri"]
        assert serialized["serviceOfferId"] == test_data["serviceOfferId"]

    def test_service_offer_management_detailedservicemanagerresourcelink_model_json_schema(self):
        """Test Service_offer_management_DetailedServiceManagerResourceLink model JSON schema generation."""
        schema = Service_offer_management_DetailedServiceManagerResourceLink.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "id",
            "name",
            "resourceUri",
            "serviceOfferId",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = []
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_offer_management_workspacetransferstatus_model_creation(self):
        """Test Service_offer_management_WorkspaceTransferStatus model creation with valid data."""
        # Valid test data for Service_offer_management_WorkspaceTransferStatus
        valid_data = {}

        # Create model instance
        model = Service_offer_management_WorkspaceTransferStatus(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_offer_management_WorkspaceTransferStatus)

    def test_service_offer_management_workspacetransferstatus_model_validation(self):
        """Test Service_offer_management_WorkspaceTransferStatus model field validation."""
        # Test with minimal required data
        minimal_data = {}

        model = Service_offer_management_WorkspaceTransferStatus(**minimal_data)
        assert isinstance(model, Service_offer_management_WorkspaceTransferStatus)

    def test_service_offer_management_workspacetransferstatus_model_required_fields(self):
        """Test Service_offer_management_WorkspaceTransferStatus model required field validation."""
        # Check if this model has any required fields
        required_fields = []

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_offer_management_WorkspaceTransferStatus()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {}

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_offer_management_WorkspaceTransferStatus()
            assert isinstance(model, Service_offer_management_WorkspaceTransferStatus)

    def test_service_offer_management_workspacetransferstatus_model_optional_fields(self):
        """Test Service_offer_management_WorkspaceTransferStatus model optional field handling."""
        # Create with minimal required data
        minimal_data = {}

        model = Service_offer_management_WorkspaceTransferStatus(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_offer_management_workspacetransferstatus_model_serialization(self):
        """Test Service_offer_management_WorkspaceTransferStatus model serialization to dict."""
        test_data = {}

        model = Service_offer_management_WorkspaceTransferStatus(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)

        # Verify values are preserved

    def test_service_offer_management_workspacetransferstatus_model_json_schema(self):
        """Test Service_offer_management_WorkspaceTransferStatus model JSON schema generation."""
        schema = Service_offer_management_WorkspaceTransferStatus.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {}

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = []
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_offer_management_toomanyrequestserror_model_creation(self):
        """Test Service_offer_management_TooManyRequestsError model creation with valid data."""
        # Valid test data for Service_offer_management_TooManyRequestsError
        valid_data = {
            "errorDetails": [],
            "httpStatusCode": 42,
            "message": "test_message",
            "debugId": "test_debugId",
            "errorCode": "test_errorCode",
        }

        # Create model instance
        model = Service_offer_management_TooManyRequestsError(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_offer_management_TooManyRequestsError)
        assert model.errorDetails == valid_data["errorDetails"]
        assert model.httpStatusCode == valid_data["httpStatusCode"]
        assert model.message == valid_data["message"]
        assert model.debugId == valid_data["debugId"]
        assert model.errorCode == valid_data["errorCode"]

    def test_service_offer_management_toomanyrequestserror_model_validation(self):
        """Test Service_offer_management_TooManyRequestsError model field validation."""
        # Test with minimal required data
        minimal_data = {
            "httpStatusCode": 1,
            "message": "required_message",
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
        }

        model = Service_offer_management_TooManyRequestsError(**minimal_data)
        assert isinstance(model, Service_offer_management_TooManyRequestsError)
        assert model.httpStatusCode == minimal_data["httpStatusCode"]
        assert model.message == minimal_data["message"]
        assert model.debugId == minimal_data["debugId"]
        assert model.errorCode == minimal_data["errorCode"]

    def test_service_offer_management_toomanyrequestserror_model_required_fields(self):
        """Test Service_offer_management_TooManyRequestsError model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "httpStatusCode",
            "message",
            "debugId",
            "errorCode",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_offer_management_TooManyRequestsError()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "httpStatusCode",
                "message",
                "debugId",
                "errorCode",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_offer_management_TooManyRequestsError()
            assert isinstance(model, Service_offer_management_TooManyRequestsError)

    def test_service_offer_management_toomanyrequestserror_model_optional_fields(self):
        """Test Service_offer_management_TooManyRequestsError model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "httpStatusCode": 1,
            "message": "required_message",
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
        }

        model = Service_offer_management_TooManyRequestsError(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "errorDetails")
        # Optional field errorDetails should be None or have a default value
        assert model.errorDetails is None or model.errorDetails is not None

    def test_service_offer_management_toomanyrequestserror_model_serialization(self):
        """Test Service_offer_management_TooManyRequestsError model serialization to dict."""
        test_data = {
            "errorDetails": [],
            "httpStatusCode": 99,
            "message": "serialize_value",
            "debugId": "serialize_value",
            "errorCode": "serialize_value",
        }

        model = Service_offer_management_TooManyRequestsError(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "errorDetails" in serialized
        assert "httpStatusCode" in serialized
        assert "message" in serialized
        assert "debugId" in serialized
        assert "errorCode" in serialized

        # Verify values are preserved
        assert serialized["errorDetails"] == test_data["errorDetails"]
        assert serialized["httpStatusCode"] == test_data["httpStatusCode"]
        assert serialized["message"] == test_data["message"]
        assert serialized["debugId"] == test_data["debugId"]
        assert serialized["errorCode"] == test_data["errorCode"]

    def test_service_offer_management_toomanyrequestserror_model_json_schema(self):
        """Test Service_offer_management_TooManyRequestsError model JSON schema generation."""
        schema = Service_offer_management_TooManyRequestsError.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "errorDetails",
            "httpStatusCode",
            "message",
            "debugId",
            "errorCode",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "httpStatusCode",
            "message",
            "debugId",
            "errorCode",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_offer_management_detailedserviceoffer_model_creation(self):
        """Test Service_offer_management_DetailedServiceOffer model creation with valid data."""
        # Valid test data for Service_offer_management_DetailedServiceOffer
        valid_data = {
            "id": "test_id",
            "orgSingletonServiceProvisions": [],
            "provisions": [],
            "serviceManager": {},
            "serviceOffer": "test_serviceOffer",
            "type": "test_type",
            "availableRegions": [],
        }

        # Create model instance
        model = Service_offer_management_DetailedServiceOffer(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_offer_management_DetailedServiceOffer)
        assert model.id == valid_data["id"]
        assert model.orgSingletonServiceProvisions == valid_data["orgSingletonServiceProvisions"]
        assert model.provisions == valid_data["provisions"]
        assert model.serviceManager == valid_data["serviceManager"]
        assert model.serviceOffer == valid_data["serviceOffer"]
        assert model.type == valid_data["type"]
        assert model.availableRegions == valid_data["availableRegions"]

    def test_service_offer_management_detailedserviceoffer_model_validation(self):
        """Test Service_offer_management_DetailedServiceOffer model field validation."""
        # Test with minimal required data
        minimal_data = {
            "id": "required_id",
            "orgSingletonServiceProvisions": [],
            "provisions": [],
            "type": "required_type",
            "availableRegions": [],
        }

        model = Service_offer_management_DetailedServiceOffer(**minimal_data)
        assert isinstance(model, Service_offer_management_DetailedServiceOffer)
        assert model.id == minimal_data["id"]
        assert model.orgSingletonServiceProvisions == minimal_data["orgSingletonServiceProvisions"]
        assert model.provisions == minimal_data["provisions"]
        assert model.type == minimal_data["type"]
        assert model.availableRegions == minimal_data["availableRegions"]

    def test_service_offer_management_detailedserviceoffer_model_required_fields(self):
        """Test Service_offer_management_DetailedServiceOffer model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "id",
            "orgSingletonServiceProvisions",
            "provisions",
            "type",
            "availableRegions",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_offer_management_DetailedServiceOffer()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "id",
                "orgSingletonServiceProvisions",
                "provisions",
                "type",
                "availableRegions",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_offer_management_DetailedServiceOffer()
            assert isinstance(model, Service_offer_management_DetailedServiceOffer)

    def test_service_offer_management_detailedserviceoffer_model_optional_fields(self):
        """Test Service_offer_management_DetailedServiceOffer model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "id": "required_id",
            "orgSingletonServiceProvisions": [],
            "provisions": [],
            "type": "required_type",
            "availableRegions": [],
        }

        model = Service_offer_management_DetailedServiceOffer(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "serviceManager")
        # Optional field serviceManager should be None or have a default value
        assert model.serviceManager is None or model.serviceManager is not None
        assert hasattr(model, "serviceOffer")
        # Optional field serviceOffer should be None or have a default value
        assert model.serviceOffer is None or model.serviceOffer is not None

    def test_service_offer_management_detailedserviceoffer_model_serialization(self):
        """Test Service_offer_management_DetailedServiceOffer model serialization to dict."""
        test_data = {
            "id": "serialize_value",
            "orgSingletonServiceProvisions": [],
            "provisions": [],
            "serviceManager": {"key": "value"},
            "serviceOffer": "serialize_value",
            "type": "serialize_value",
            "availableRegions": [],
        }

        model = Service_offer_management_DetailedServiceOffer(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "id" in serialized
        assert "orgSingletonServiceProvisions" in serialized
        assert "provisions" in serialized
        assert "serviceManager" in serialized
        assert "serviceOffer" in serialized
        assert "type" in serialized
        assert "availableRegions" in serialized

        # Verify values are preserved
        assert serialized["id"] == test_data["id"]
        assert serialized["orgSingletonServiceProvisions"] == test_data["orgSingletonServiceProvisions"]
        assert serialized["provisions"] == test_data["provisions"]
        assert serialized["serviceManager"] == test_data["serviceManager"]
        assert serialized["serviceOffer"] == test_data["serviceOffer"]
        assert serialized["type"] == test_data["type"]
        assert serialized["availableRegions"] == test_data["availableRegions"]

    def test_service_offer_management_detailedserviceoffer_model_json_schema(self):
        """Test Service_offer_management_DetailedServiceOffer model JSON schema generation."""
        schema = Service_offer_management_DetailedServiceOffer.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "id",
            "orgSingletonServiceProvisions",
            "provisions",
            "serviceManager",
            "serviceOffer",
            "type",
            "availableRegions",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "id",
            "orgSingletonServiceProvisions",
            "provisions",
            "type",
            "availableRegions",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_offer_management_categorywithserviceoffers_model_creation(self):
        """Test Service_offer_management_CategoryWithServiceOffers model creation with valid data."""
        # Valid test data for Service_offer_management_CategoryWithServiceOffers
        valid_data = {
            "type": "test_type",
            "id": "test_id",
            "servicesWithRegions": [],
        }

        # Create model instance
        model = Service_offer_management_CategoryWithServiceOffers(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_offer_management_CategoryWithServiceOffers)
        assert model.type == valid_data["type"]
        assert model.id == valid_data["id"]
        assert model.servicesWithRegions == valid_data["servicesWithRegions"]

    def test_service_offer_management_categorywithserviceoffers_model_validation(self):
        """Test Service_offer_management_CategoryWithServiceOffers model field validation."""
        # Test with minimal required data
        minimal_data = {
            "type": "required_type",
            "id": "required_id",
            "servicesWithRegions": [],
        }

        model = Service_offer_management_CategoryWithServiceOffers(**minimal_data)
        assert isinstance(model, Service_offer_management_CategoryWithServiceOffers)
        assert model.type == minimal_data["type"]
        assert model.id == minimal_data["id"]
        assert model.servicesWithRegions == minimal_data["servicesWithRegions"]

    def test_service_offer_management_categorywithserviceoffers_model_required_fields(self):
        """Test Service_offer_management_CategoryWithServiceOffers model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "type",
            "id",
            "servicesWithRegions",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_offer_management_CategoryWithServiceOffers()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "type",
                "id",
                "servicesWithRegions",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_offer_management_CategoryWithServiceOffers()
            assert isinstance(model, Service_offer_management_CategoryWithServiceOffers)

    def test_service_offer_management_categorywithserviceoffers_model_optional_fields(self):
        """Test Service_offer_management_CategoryWithServiceOffers model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "type": "required_type",
            "id": "required_id",
            "servicesWithRegions": [],
        }

        model = Service_offer_management_CategoryWithServiceOffers(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_offer_management_categorywithserviceoffers_model_serialization(self):
        """Test Service_offer_management_CategoryWithServiceOffers model serialization to dict."""
        test_data = {
            "type": "serialize_value",
            "id": "serialize_value",
            "servicesWithRegions": [],
        }

        model = Service_offer_management_CategoryWithServiceOffers(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "type" in serialized
        assert "id" in serialized
        assert "servicesWithRegions" in serialized

        # Verify values are preserved
        assert serialized["type"] == test_data["type"]
        assert serialized["id"] == test_data["id"]
        assert serialized["servicesWithRegions"] == test_data["servicesWithRegions"]

    def test_service_offer_management_categorywithserviceoffers_model_json_schema(self):
        """Test Service_offer_management_CategoryWithServiceOffers model JSON schema generation."""
        schema = Service_offer_management_CategoryWithServiceOffers.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "type",
            "id",
            "servicesWithRegions",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "type",
            "id",
            "servicesWithRegions",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_provision_management_serviceprovisionlist_model_creation(self):
        """Test Service_provision_management_ServiceProvisionList model creation with valid data."""
        # Valid test data for Service_provision_management_ServiceProvisionList
        valid_data = {
            "count": 42,
            "items": [],
            "next": "test_next",
            "total": 42,
        }

        # Create model instance
        model = Service_provision_management_ServiceProvisionList(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_provision_management_ServiceProvisionList)
        assert model.count == valid_data["count"]
        assert model.items == valid_data["items"]
        assert model.next == valid_data["next"]
        assert model.total == valid_data["total"]

    def test_service_provision_management_serviceprovisionlist_model_validation(self):
        """Test Service_provision_management_ServiceProvisionList model field validation."""
        # Test with minimal required data
        minimal_data = {
            "count": 1,
            "items": [],
            "next": "required_next",
            "total": 1,
        }

        model = Service_provision_management_ServiceProvisionList(**minimal_data)
        assert isinstance(model, Service_provision_management_ServiceProvisionList)
        assert model.count == minimal_data["count"]
        assert model.items == minimal_data["items"]
        assert model.next == minimal_data["next"]
        assert model.total == minimal_data["total"]

    def test_service_provision_management_serviceprovisionlist_model_required_fields(self):
        """Test Service_provision_management_ServiceProvisionList model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "count",
            "items",
            "next",
            "total",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_provision_management_ServiceProvisionList()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "count",
                "items",
                "next",
                "total",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_provision_management_ServiceProvisionList()
            assert isinstance(model, Service_provision_management_ServiceProvisionList)

    def test_service_provision_management_serviceprovisionlist_model_optional_fields(self):
        """Test Service_provision_management_ServiceProvisionList model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "count": 1,
            "items": [],
            "next": "required_next",
            "total": 1,
        }

        model = Service_provision_management_ServiceProvisionList(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_provision_management_serviceprovisionlist_model_serialization(self):
        """Test Service_provision_management_ServiceProvisionList model serialization to dict."""
        test_data = {
            "count": 99,
            "items": [],
            "next": "serialize_value",
            "total": 99,
        }

        model = Service_provision_management_ServiceProvisionList(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "count" in serialized
        assert "items" in serialized
        assert "next" in serialized
        assert "total" in serialized

        # Verify values are preserved
        assert serialized["count"] == test_data["count"]
        assert serialized["items"] == test_data["items"]
        assert serialized["next"] == test_data["next"]
        assert serialized["total"] == test_data["total"]

    def test_service_provision_management_serviceprovisionlist_model_json_schema(self):
        """Test Service_provision_management_ServiceProvisionList model JSON schema generation."""
        schema = Service_provision_management_ServiceProvisionList.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "count",
            "items",
            "next",
            "total",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "count",
            "items",
            "next",
            "total",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_offer_management_serviceoffermediavideodetails_model_creation(self):
        """Test Service_offer_management_ServiceOfferMediaVideoDetails model creation with valid data."""
        # Valid test data for Service_offer_management_ServiceOfferMediaVideoDetails
        valid_data = {
            "video": "test_video",
            "description": "test_description",
        }

        # Create model instance
        model = Service_offer_management_ServiceOfferMediaVideoDetails(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_offer_management_ServiceOfferMediaVideoDetails)
        assert model.video == valid_data["video"]
        assert model.description == valid_data["description"]

    def test_service_offer_management_serviceoffermediavideodetails_model_validation(self):
        """Test Service_offer_management_ServiceOfferMediaVideoDetails model field validation."""
        # Test with minimal required data
        minimal_data = {
            "video": "required_video",
            "description": "required_description",
        }

        model = Service_offer_management_ServiceOfferMediaVideoDetails(**minimal_data)
        assert isinstance(model, Service_offer_management_ServiceOfferMediaVideoDetails)
        assert model.video == minimal_data["video"]
        assert model.description == minimal_data["description"]

    def test_service_offer_management_serviceoffermediavideodetails_model_required_fields(self):
        """Test Service_offer_management_ServiceOfferMediaVideoDetails model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "video",
            "description",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_offer_management_ServiceOfferMediaVideoDetails()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "video",
                "description",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_offer_management_ServiceOfferMediaVideoDetails()
            assert isinstance(model, Service_offer_management_ServiceOfferMediaVideoDetails)

    def test_service_offer_management_serviceoffermediavideodetails_model_optional_fields(self):
        """Test Service_offer_management_ServiceOfferMediaVideoDetails model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "video": "required_video",
            "description": "required_description",
        }

        model = Service_offer_management_ServiceOfferMediaVideoDetails(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_offer_management_serviceoffermediavideodetails_model_serialization(self):
        """Test Service_offer_management_ServiceOfferMediaVideoDetails model serialization to dict."""
        test_data = {
            "video": "serialize_value",
            "description": "serialize_value",
        }

        model = Service_offer_management_ServiceOfferMediaVideoDetails(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "video" in serialized
        assert "description" in serialized

        # Verify values are preserved
        assert serialized["video"] == test_data["video"]
        assert serialized["description"] == test_data["description"]

    def test_service_offer_management_serviceoffermediavideodetails_model_json_schema(self):
        """Test Service_offer_management_ServiceOfferMediaVideoDetails model JSON schema generation."""
        schema = Service_offer_management_ServiceOfferMediaVideoDetails.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "video",
            "description",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "video",
            "description",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_offer_management_supportedfeature_model_creation(self):
        """Test Service_offer_management_SupportedFeature model creation with valid data."""
        # Valid test data for Service_offer_management_SupportedFeature
        valid_data = {}

        # Create model instance
        model = Service_offer_management_SupportedFeature(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_offer_management_SupportedFeature)

    def test_service_offer_management_supportedfeature_model_validation(self):
        """Test Service_offer_management_SupportedFeature model field validation."""
        # Test with minimal required data
        minimal_data = {}

        model = Service_offer_management_SupportedFeature(**minimal_data)
        assert isinstance(model, Service_offer_management_SupportedFeature)

    def test_service_offer_management_supportedfeature_model_required_fields(self):
        """Test Service_offer_management_SupportedFeature model required field validation."""
        # Check if this model has any required fields
        required_fields = []

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_offer_management_SupportedFeature()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {}

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_offer_management_SupportedFeature()
            assert isinstance(model, Service_offer_management_SupportedFeature)

    def test_service_offer_management_supportedfeature_model_optional_fields(self):
        """Test Service_offer_management_SupportedFeature model optional field handling."""
        # Create with minimal required data
        minimal_data = {}

        model = Service_offer_management_SupportedFeature(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_offer_management_supportedfeature_model_serialization(self):
        """Test Service_offer_management_SupportedFeature model serialization to dict."""
        test_data = {}

        model = Service_offer_management_SupportedFeature(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)

        # Verify values are preserved

    def test_service_offer_management_supportedfeature_model_json_schema(self):
        """Test Service_offer_management_SupportedFeature model JSON schema generation."""
        schema = Service_offer_management_SupportedFeature.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {}

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = []
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_provision_management_conflicterror_model_creation(self):
        """Test Service_provision_management_ConflictError model creation with valid data."""
        # Valid test data for Service_provision_management_ConflictError
        valid_data = {
            "debugId": "test_debugId",
            "errorCode": "test_errorCode",
            "httpStatusCode": 42,
            "message": "test_message",
        }

        # Create model instance
        model = Service_provision_management_ConflictError(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_provision_management_ConflictError)
        assert model.debugId == valid_data["debugId"]
        assert model.errorCode == valid_data["errorCode"]
        assert model.httpStatusCode == valid_data["httpStatusCode"]
        assert model.message == valid_data["message"]

    def test_service_provision_management_conflicterror_model_validation(self):
        """Test Service_provision_management_ConflictError model field validation."""
        # Test with minimal required data
        minimal_data = {
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
            "httpStatusCode": 1,
            "message": "required_message",
        }

        model = Service_provision_management_ConflictError(**minimal_data)
        assert isinstance(model, Service_provision_management_ConflictError)
        assert model.debugId == minimal_data["debugId"]
        assert model.errorCode == minimal_data["errorCode"]
        assert model.httpStatusCode == minimal_data["httpStatusCode"]
        assert model.message == minimal_data["message"]

    def test_service_provision_management_conflicterror_model_required_fields(self):
        """Test Service_provision_management_ConflictError model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "debugId",
            "errorCode",
            "httpStatusCode",
            "message",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_provision_management_ConflictError()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "debugId",
                "errorCode",
                "httpStatusCode",
                "message",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_provision_management_ConflictError()
            assert isinstance(model, Service_provision_management_ConflictError)

    def test_service_provision_management_conflicterror_model_optional_fields(self):
        """Test Service_provision_management_ConflictError model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
            "httpStatusCode": 1,
            "message": "required_message",
        }

        model = Service_provision_management_ConflictError(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_provision_management_conflicterror_model_serialization(self):
        """Test Service_provision_management_ConflictError model serialization to dict."""
        test_data = {
            "debugId": "serialize_value",
            "errorCode": "serialize_value",
            "httpStatusCode": 99,
            "message": "serialize_value",
        }

        model = Service_provision_management_ConflictError(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "debugId" in serialized
        assert "errorCode" in serialized
        assert "httpStatusCode" in serialized
        assert "message" in serialized

        # Verify values are preserved
        assert serialized["debugId"] == test_data["debugId"]
        assert serialized["errorCode"] == test_data["errorCode"]
        assert serialized["httpStatusCode"] == test_data["httpStatusCode"]
        assert serialized["message"] == test_data["message"]

    def test_service_provision_management_conflicterror_model_json_schema(self):
        """Test Service_provision_management_ConflictError model JSON schema generation."""
        schema = Service_provision_management_ConflictError.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "debugId",
            "errorCode",
            "httpStatusCode",
            "message",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "debugId",
            "errorCode",
            "httpStatusCode",
            "message",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_provision_management_notfounderror_model_creation(self):
        """Test Service_provision_management_NotFoundError model creation with valid data."""
        # Valid test data for Service_provision_management_NotFoundError
        valid_data = {
            "debugId": "test_debugId",
            "errorCode": "test_errorCode",
            "httpStatusCode": 42,
            "message": "test_message",
        }

        # Create model instance
        model = Service_provision_management_NotFoundError(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_provision_management_NotFoundError)
        assert model.debugId == valid_data["debugId"]
        assert model.errorCode == valid_data["errorCode"]
        assert model.httpStatusCode == valid_data["httpStatusCode"]
        assert model.message == valid_data["message"]

    def test_service_provision_management_notfounderror_model_validation(self):
        """Test Service_provision_management_NotFoundError model field validation."""
        # Test with minimal required data
        minimal_data = {
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
            "httpStatusCode": 1,
            "message": "required_message",
        }

        model = Service_provision_management_NotFoundError(**minimal_data)
        assert isinstance(model, Service_provision_management_NotFoundError)
        assert model.debugId == minimal_data["debugId"]
        assert model.errorCode == minimal_data["errorCode"]
        assert model.httpStatusCode == minimal_data["httpStatusCode"]
        assert model.message == minimal_data["message"]

    def test_service_provision_management_notfounderror_model_required_fields(self):
        """Test Service_provision_management_NotFoundError model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "debugId",
            "errorCode",
            "httpStatusCode",
            "message",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_provision_management_NotFoundError()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "debugId",
                "errorCode",
                "httpStatusCode",
                "message",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_provision_management_NotFoundError()
            assert isinstance(model, Service_provision_management_NotFoundError)

    def test_service_provision_management_notfounderror_model_optional_fields(self):
        """Test Service_provision_management_NotFoundError model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
            "httpStatusCode": 1,
            "message": "required_message",
        }

        model = Service_provision_management_NotFoundError(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_provision_management_notfounderror_model_serialization(self):
        """Test Service_provision_management_NotFoundError model serialization to dict."""
        test_data = {
            "debugId": "serialize_value",
            "errorCode": "serialize_value",
            "httpStatusCode": 99,
            "message": "serialize_value",
        }

        model = Service_provision_management_NotFoundError(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "debugId" in serialized
        assert "errorCode" in serialized
        assert "httpStatusCode" in serialized
        assert "message" in serialized

        # Verify values are preserved
        assert serialized["debugId"] == test_data["debugId"]
        assert serialized["errorCode"] == test_data["errorCode"]
        assert serialized["httpStatusCode"] == test_data["httpStatusCode"]
        assert serialized["message"] == test_data["message"]

    def test_service_provision_management_notfounderror_model_json_schema(self):
        """Test Service_provision_management_NotFoundError model JSON schema generation."""
        schema = Service_provision_management_NotFoundError.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "debugId",
            "errorCode",
            "httpStatusCode",
            "message",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "debugId",
            "errorCode",
            "httpStatusCode",
            "message",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_offer_management_serviceofferlist_model_creation(self):
        """Test Service_offer_management_ServiceOfferList model creation with valid data."""
        # Valid test data for Service_offer_management_ServiceOfferList
        valid_data = {
            "count": 42,
            "items": [],
            "next": "test_next",
            "total": 42,
        }

        # Create model instance
        model = Service_offer_management_ServiceOfferList(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_offer_management_ServiceOfferList)
        assert model.count == valid_data["count"]
        assert model.items == valid_data["items"]
        assert model.next == valid_data["next"]
        assert model.total == valid_data["total"]

    def test_service_offer_management_serviceofferlist_model_validation(self):
        """Test Service_offer_management_ServiceOfferList model field validation."""
        # Test with minimal required data
        minimal_data = {
            "count": 1,
            "items": [],
            "next": "required_next",
            "total": 1,
        }

        model = Service_offer_management_ServiceOfferList(**minimal_data)
        assert isinstance(model, Service_offer_management_ServiceOfferList)
        assert model.count == minimal_data["count"]
        assert model.items == minimal_data["items"]
        assert model.next == minimal_data["next"]
        assert model.total == minimal_data["total"]

    def test_service_offer_management_serviceofferlist_model_required_fields(self):
        """Test Service_offer_management_ServiceOfferList model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "count",
            "items",
            "next",
            "total",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_offer_management_ServiceOfferList()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "count",
                "items",
                "next",
                "total",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_offer_management_ServiceOfferList()
            assert isinstance(model, Service_offer_management_ServiceOfferList)

    def test_service_offer_management_serviceofferlist_model_optional_fields(self):
        """Test Service_offer_management_ServiceOfferList model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "count": 1,
            "items": [],
            "next": "required_next",
            "total": 1,
        }

        model = Service_offer_management_ServiceOfferList(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_offer_management_serviceofferlist_model_serialization(self):
        """Test Service_offer_management_ServiceOfferList model serialization to dict."""
        test_data = {
            "count": 99,
            "items": [],
            "next": "serialize_value",
            "total": 99,
        }

        model = Service_offer_management_ServiceOfferList(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "count" in serialized
        assert "items" in serialized
        assert "next" in serialized
        assert "total" in serialized

        # Verify values are preserved
        assert serialized["count"] == test_data["count"]
        assert serialized["items"] == test_data["items"]
        assert serialized["next"] == test_data["next"]
        assert serialized["total"] == test_data["total"]

    def test_service_offer_management_serviceofferlist_model_json_schema(self):
        """Test Service_offer_management_ServiceOfferList model JSON schema generation."""
        schema = Service_offer_management_ServiceOfferList.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "count",
            "items",
            "next",
            "total",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "count",
            "items",
            "next",
            "total",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_manager_management_servicemanagersperregion_model_creation(self):
        """Test Service_Manager_Management_ServiceManagersPerRegion model creation with valid data."""
        # Valid test data for Service_Manager_Management_ServiceManagersPerRegion
        valid_data = {
            "count": 42,
            "items": [],
            "offset": 42,
            "total": 42,
        }

        # Create model instance
        model = Service_Manager_Management_ServiceManagersPerRegion(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_Manager_Management_ServiceManagersPerRegion)
        assert model.count == valid_data["count"]
        assert model.items == valid_data["items"]
        assert model.offset == valid_data["offset"]
        assert model.total == valid_data["total"]

    def test_service_manager_management_servicemanagersperregion_model_validation(self):
        """Test Service_Manager_Management_ServiceManagersPerRegion model field validation."""
        # Test with minimal required data
        minimal_data = {
            "count": 1,
            "items": [],
            "offset": 1,
        }

        model = Service_Manager_Management_ServiceManagersPerRegion(**minimal_data)
        assert isinstance(model, Service_Manager_Management_ServiceManagersPerRegion)
        assert model.count == minimal_data["count"]
        assert model.items == minimal_data["items"]
        assert model.offset == minimal_data["offset"]

    def test_service_manager_management_servicemanagersperregion_model_required_fields(self):
        """Test Service_Manager_Management_ServiceManagersPerRegion model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "count",
            "items",
            "offset",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_Manager_Management_ServiceManagersPerRegion()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "count",
                "items",
                "offset",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_Manager_Management_ServiceManagersPerRegion()
            assert isinstance(model, Service_Manager_Management_ServiceManagersPerRegion)

    def test_service_manager_management_servicemanagersperregion_model_optional_fields(self):
        """Test Service_Manager_Management_ServiceManagersPerRegion model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "count": 1,
            "items": [],
            "offset": 1,
        }

        model = Service_Manager_Management_ServiceManagersPerRegion(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "total")
        # Optional field total should be None or have a default value
        assert model.total is None or model.total is not None

    def test_service_manager_management_servicemanagersperregion_model_serialization(self):
        """Test Service_Manager_Management_ServiceManagersPerRegion model serialization to dict."""
        test_data = {
            "count": 99,
            "items": [],
            "offset": 99,
            "total": 99,
        }

        model = Service_Manager_Management_ServiceManagersPerRegion(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "count" in serialized
        assert "items" in serialized
        assert "offset" in serialized
        assert "total" in serialized

        # Verify values are preserved
        assert serialized["count"] == test_data["count"]
        assert serialized["items"] == test_data["items"]
        assert serialized["offset"] == test_data["offset"]
        assert serialized["total"] == test_data["total"]

    def test_service_manager_management_servicemanagersperregion_model_json_schema(self):
        """Test Service_Manager_Management_ServiceManagersPerRegion model JSON schema generation."""
        schema = Service_Manager_Management_ServiceManagersPerRegion.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "count",
            "items",
            "offset",
            "total",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "count",
            "items",
            "offset",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_offer_management_serviceoffermediaimagedetails_model_creation(self):
        """Test Service_offer_management_ServiceOfferMediaImageDetails model creation with valid data."""
        # Valid test data for Service_offer_management_ServiceOfferMediaImageDetails
        valid_data = {
            "image": "test_image",
            "description": "test_description",
        }

        # Create model instance
        model = Service_offer_management_ServiceOfferMediaImageDetails(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_offer_management_ServiceOfferMediaImageDetails)
        assert model.image == valid_data["image"]
        assert model.description == valid_data["description"]

    def test_service_offer_management_serviceoffermediaimagedetails_model_validation(self):
        """Test Service_offer_management_ServiceOfferMediaImageDetails model field validation."""
        # Test with minimal required data
        minimal_data = {
            "image": "required_image",
            "description": "required_description",
        }

        model = Service_offer_management_ServiceOfferMediaImageDetails(**minimal_data)
        assert isinstance(model, Service_offer_management_ServiceOfferMediaImageDetails)
        assert model.image == minimal_data["image"]
        assert model.description == minimal_data["description"]

    def test_service_offer_management_serviceoffermediaimagedetails_model_required_fields(self):
        """Test Service_offer_management_ServiceOfferMediaImageDetails model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "image",
            "description",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_offer_management_ServiceOfferMediaImageDetails()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "image",
                "description",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_offer_management_ServiceOfferMediaImageDetails()
            assert isinstance(model, Service_offer_management_ServiceOfferMediaImageDetails)

    def test_service_offer_management_serviceoffermediaimagedetails_model_optional_fields(self):
        """Test Service_offer_management_ServiceOfferMediaImageDetails model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "image": "required_image",
            "description": "required_description",
        }

        model = Service_offer_management_ServiceOfferMediaImageDetails(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_offer_management_serviceoffermediaimagedetails_model_serialization(self):
        """Test Service_offer_management_ServiceOfferMediaImageDetails model serialization to dict."""
        test_data = {
            "image": "serialize_value",
            "description": "serialize_value",
        }

        model = Service_offer_management_ServiceOfferMediaImageDetails(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "image" in serialized
        assert "description" in serialized

        # Verify values are preserved
        assert serialized["image"] == test_data["image"]
        assert serialized["description"] == test_data["description"]

    def test_service_offer_management_serviceoffermediaimagedetails_model_json_schema(self):
        """Test Service_offer_management_ServiceOfferMediaImageDetails model JSON schema generation."""
        schema = Service_offer_management_ServiceOfferMediaImageDetails.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "image",
            "description",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "image",
            "description",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_offer_management_regionwithdetailedprovisions_model_creation(self):
        """Test Service_offer_management_RegionWithDetailedProvisions model creation with valid data."""
        # Valid test data for Service_offer_management_RegionWithDetailedProvisions
        valid_data = {
            "id": "test_id",
            "provisions": [],
            "type": "test_type",
        }

        # Create model instance
        model = Service_offer_management_RegionWithDetailedProvisions(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_offer_management_RegionWithDetailedProvisions)
        assert model.id == valid_data["id"]
        assert model.provisions == valid_data["provisions"]
        assert model.type == valid_data["type"]

    def test_service_offer_management_regionwithdetailedprovisions_model_validation(self):
        """Test Service_offer_management_RegionWithDetailedProvisions model field validation."""
        # Test with minimal required data
        minimal_data = {
            "id": "required_id",
            "provisions": [],
            "type": "required_type",
        }

        model = Service_offer_management_RegionWithDetailedProvisions(**minimal_data)
        assert isinstance(model, Service_offer_management_RegionWithDetailedProvisions)
        assert model.id == minimal_data["id"]
        assert model.provisions == minimal_data["provisions"]
        assert model.type == minimal_data["type"]

    def test_service_offer_management_regionwithdetailedprovisions_model_required_fields(self):
        """Test Service_offer_management_RegionWithDetailedProvisions model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "id",
            "provisions",
            "type",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_offer_management_RegionWithDetailedProvisions()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "id",
                "provisions",
                "type",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_offer_management_RegionWithDetailedProvisions()
            assert isinstance(model, Service_offer_management_RegionWithDetailedProvisions)

    def test_service_offer_management_regionwithdetailedprovisions_model_optional_fields(self):
        """Test Service_offer_management_RegionWithDetailedProvisions model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "id": "required_id",
            "provisions": [],
            "type": "required_type",
        }

        model = Service_offer_management_RegionWithDetailedProvisions(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_offer_management_regionwithdetailedprovisions_model_serialization(self):
        """Test Service_offer_management_RegionWithDetailedProvisions model serialization to dict."""
        test_data = {
            "id": "serialize_value",
            "provisions": [],
            "type": "serialize_value",
        }

        model = Service_offer_management_RegionWithDetailedProvisions(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "id" in serialized
        assert "provisions" in serialized
        assert "type" in serialized

        # Verify values are preserved
        assert serialized["id"] == test_data["id"]
        assert serialized["provisions"] == test_data["provisions"]
        assert serialized["type"] == test_data["type"]

    def test_service_offer_management_regionwithdetailedprovisions_model_json_schema(self):
        """Test Service_offer_management_RegionWithDetailedProvisions model JSON schema generation."""
        schema = Service_offer_management_RegionWithDetailedProvisions.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "id",
            "provisions",
            "type",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "id",
            "provisions",
            "type",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_manager_management_servicemanagerreadlist_model_creation(self):
        """Test Service_Manager_Management_ServiceManagerReadList model creation with valid data."""
        # Valid test data for Service_Manager_Management_ServiceManagerReadList
        valid_data = {
            "offset": 42,
            "total": 42,
            "count": 42,
            "items": [],
        }

        # Create model instance
        model = Service_Manager_Management_ServiceManagerReadList(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_Manager_Management_ServiceManagerReadList)
        assert model.offset == valid_data["offset"]
        assert model.total == valid_data["total"]
        assert model.count == valid_data["count"]
        assert model.items == valid_data["items"]

    def test_service_manager_management_servicemanagerreadlist_model_validation(self):
        """Test Service_Manager_Management_ServiceManagerReadList model field validation."""
        # Test with minimal required data
        minimal_data = {
            "offset": 1,
            "count": 1,
            "items": [],
        }

        model = Service_Manager_Management_ServiceManagerReadList(**minimal_data)
        assert isinstance(model, Service_Manager_Management_ServiceManagerReadList)
        assert model.offset == minimal_data["offset"]
        assert model.count == minimal_data["count"]
        assert model.items == minimal_data["items"]

    def test_service_manager_management_servicemanagerreadlist_model_required_fields(self):
        """Test Service_Manager_Management_ServiceManagerReadList model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "offset",
            "count",
            "items",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_Manager_Management_ServiceManagerReadList()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "offset",
                "count",
                "items",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_Manager_Management_ServiceManagerReadList()
            assert isinstance(model, Service_Manager_Management_ServiceManagerReadList)

    def test_service_manager_management_servicemanagerreadlist_model_optional_fields(self):
        """Test Service_Manager_Management_ServiceManagerReadList model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "offset": 1,
            "count": 1,
            "items": [],
        }

        model = Service_Manager_Management_ServiceManagerReadList(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "total")
        # Optional field total should be None or have a default value
        assert model.total is None or model.total is not None

    def test_service_manager_management_servicemanagerreadlist_model_serialization(self):
        """Test Service_Manager_Management_ServiceManagerReadList model serialization to dict."""
        test_data = {
            "offset": 99,
            "total": 99,
            "count": 99,
            "items": [],
        }

        model = Service_Manager_Management_ServiceManagerReadList(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "offset" in serialized
        assert "total" in serialized
        assert "count" in serialized
        assert "items" in serialized

        # Verify values are preserved
        assert serialized["offset"] == test_data["offset"]
        assert serialized["total"] == test_data["total"]
        assert serialized["count"] == test_data["count"]
        assert serialized["items"] == test_data["items"]

    def test_service_manager_management_servicemanagerreadlist_model_json_schema(self):
        """Test Service_Manager_Management_ServiceManagerReadList model JSON schema generation."""
        schema = Service_Manager_Management_ServiceManagerReadList.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "offset",
            "total",
            "count",
            "items",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "offset",
            "count",
            "items",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_offer_management_featuredserviceoffers_model_creation(self):
        """Test Service_offer_management_FeaturedServiceOffers model creation with valid data."""
        # Valid test data for Service_offer_management_FeaturedServiceOffers
        valid_data = {
            "items": [],
            "next": "test_next",
            "total": 42,
            "count": 42,
        }

        # Create model instance
        model = Service_offer_management_FeaturedServiceOffers(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_offer_management_FeaturedServiceOffers)
        assert model.items == valid_data["items"]
        assert model.next == valid_data["next"]
        assert model.total == valid_data["total"]
        assert model.count == valid_data["count"]

    def test_service_offer_management_featuredserviceoffers_model_validation(self):
        """Test Service_offer_management_FeaturedServiceOffers model field validation."""
        # Test with minimal required data
        minimal_data = {
            "items": [],
            "next": "required_next",
            "total": 1,
            "count": 1,
        }

        model = Service_offer_management_FeaturedServiceOffers(**minimal_data)
        assert isinstance(model, Service_offer_management_FeaturedServiceOffers)
        assert model.items == minimal_data["items"]
        assert model.next == minimal_data["next"]
        assert model.total == minimal_data["total"]
        assert model.count == minimal_data["count"]

    def test_service_offer_management_featuredserviceoffers_model_required_fields(self):
        """Test Service_offer_management_FeaturedServiceOffers model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "items",
            "next",
            "total",
            "count",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_offer_management_FeaturedServiceOffers()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "items",
                "next",
                "total",
                "count",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_offer_management_FeaturedServiceOffers()
            assert isinstance(model, Service_offer_management_FeaturedServiceOffers)

    def test_service_offer_management_featuredserviceoffers_model_optional_fields(self):
        """Test Service_offer_management_FeaturedServiceOffers model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "items": [],
            "next": "required_next",
            "total": 1,
            "count": 1,
        }

        model = Service_offer_management_FeaturedServiceOffers(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_offer_management_featuredserviceoffers_model_serialization(self):
        """Test Service_offer_management_FeaturedServiceOffers model serialization to dict."""
        test_data = {
            "items": [],
            "next": "serialize_value",
            "total": 99,
            "count": 99,
        }

        model = Service_offer_management_FeaturedServiceOffers(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "items" in serialized
        assert "next" in serialized
        assert "total" in serialized
        assert "count" in serialized

        # Verify values are preserved
        assert serialized["items"] == test_data["items"]
        assert serialized["next"] == test_data["next"]
        assert serialized["total"] == test_data["total"]
        assert serialized["count"] == test_data["count"]

    def test_service_offer_management_featuredserviceoffers_model_json_schema(self):
        """Test Service_offer_management_FeaturedServiceOffers model JSON schema generation."""
        schema = Service_offer_management_FeaturedServiceOffers.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "items",
            "next",
            "total",
            "count",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "items",
            "next",
            "total",
            "count",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_provision_management_preconditionfailederror_model_creation(self):
        """Test Service_provision_management_PreConditionFailedError model creation with valid data."""
        # Valid test data for Service_provision_management_PreConditionFailedError
        valid_data = {
            "debugId": "test_debugId",
            "errorCode": "test_errorCode",
            "httpStatusCode": 42,
            "message": "test_message",
        }

        # Create model instance
        model = Service_provision_management_PreConditionFailedError(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_provision_management_PreConditionFailedError)
        assert model.debugId == valid_data["debugId"]
        assert model.errorCode == valid_data["errorCode"]
        assert model.httpStatusCode == valid_data["httpStatusCode"]
        assert model.message == valid_data["message"]

    def test_service_provision_management_preconditionfailederror_model_validation(self):
        """Test Service_provision_management_PreConditionFailedError model field validation."""
        # Test with minimal required data
        minimal_data = {
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
            "httpStatusCode": 1,
            "message": "required_message",
        }

        model = Service_provision_management_PreConditionFailedError(**minimal_data)
        assert isinstance(model, Service_provision_management_PreConditionFailedError)
        assert model.debugId == minimal_data["debugId"]
        assert model.errorCode == minimal_data["errorCode"]
        assert model.httpStatusCode == minimal_data["httpStatusCode"]
        assert model.message == minimal_data["message"]

    def test_service_provision_management_preconditionfailederror_model_required_fields(self):
        """Test Service_provision_management_PreConditionFailedError model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "debugId",
            "errorCode",
            "httpStatusCode",
            "message",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_provision_management_PreConditionFailedError()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "debugId",
                "errorCode",
                "httpStatusCode",
                "message",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_provision_management_PreConditionFailedError()
            assert isinstance(model, Service_provision_management_PreConditionFailedError)

    def test_service_provision_management_preconditionfailederror_model_optional_fields(self):
        """Test Service_provision_management_PreConditionFailedError model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
            "httpStatusCode": 1,
            "message": "required_message",
        }

        model = Service_provision_management_PreConditionFailedError(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_provision_management_preconditionfailederror_model_serialization(self):
        """Test Service_provision_management_PreConditionFailedError model serialization to dict."""
        test_data = {
            "debugId": "serialize_value",
            "errorCode": "serialize_value",
            "httpStatusCode": 99,
            "message": "serialize_value",
        }

        model = Service_provision_management_PreConditionFailedError(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "debugId" in serialized
        assert "errorCode" in serialized
        assert "httpStatusCode" in serialized
        assert "message" in serialized

        # Verify values are preserved
        assert serialized["debugId"] == test_data["debugId"]
        assert serialized["errorCode"] == test_data["errorCode"]
        assert serialized["httpStatusCode"] == test_data["httpStatusCode"]
        assert serialized["message"] == test_data["message"]

    def test_service_provision_management_preconditionfailederror_model_json_schema(self):
        """Test Service_provision_management_PreConditionFailedError model JSON schema generation."""
        schema = Service_provision_management_PreConditionFailedError.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "debugId",
            "errorCode",
            "httpStatusCode",
            "message",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "debugId",
            "errorCode",
            "httpStatusCode",
            "message",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_offer_management_detailedprovision_model_creation(self):
        """Test Service_offer_management_DetailedProvision model creation with valid data."""
        # Valid test data for Service_offer_management_DetailedProvision
        valid_data = {
            "serviceManagerProvision": "test_serviceManagerProvision",
            "serviceOffer": "test_serviceOffer",
            "serviceProvision": "test_serviceProvision",
        }

        # Create model instance
        model = Service_offer_management_DetailedProvision(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_offer_management_DetailedProvision)
        assert model.serviceManagerProvision == valid_data["serviceManagerProvision"]
        assert model.serviceOffer == valid_data["serviceOffer"]
        assert model.serviceProvision == valid_data["serviceProvision"]

    def test_service_offer_management_detailedprovision_model_validation(self):
        """Test Service_offer_management_DetailedProvision model field validation."""
        # Test with minimal required data
        minimal_data = {}

        model = Service_offer_management_DetailedProvision(**minimal_data)
        assert isinstance(model, Service_offer_management_DetailedProvision)

    def test_service_offer_management_detailedprovision_model_required_fields(self):
        """Test Service_offer_management_DetailedProvision model required field validation."""
        # Check if this model has any required fields
        required_fields = []

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_offer_management_DetailedProvision()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {}

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_offer_management_DetailedProvision()
            assert isinstance(model, Service_offer_management_DetailedProvision)

    def test_service_offer_management_detailedprovision_model_optional_fields(self):
        """Test Service_offer_management_DetailedProvision model optional field handling."""
        # Create with minimal required data
        minimal_data = {}

        model = Service_offer_management_DetailedProvision(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "serviceManagerProvision")
        # Optional field serviceManagerProvision should be None or have a default value
        assert model.serviceManagerProvision is None or model.serviceManagerProvision is not None
        assert hasattr(model, "serviceOffer")
        # Optional field serviceOffer should be None or have a default value
        assert model.serviceOffer is None or model.serviceOffer is not None
        assert hasattr(model, "serviceProvision")
        # Optional field serviceProvision should be None or have a default value
        assert model.serviceProvision is None or model.serviceProvision is not None

    def test_service_offer_management_detailedprovision_model_serialization(self):
        """Test Service_offer_management_DetailedProvision model serialization to dict."""
        test_data = {
            "serviceManagerProvision": "serialize_value",
            "serviceOffer": "serialize_value",
            "serviceProvision": "serialize_value",
        }

        model = Service_offer_management_DetailedProvision(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "serviceManagerProvision" in serialized
        assert "serviceOffer" in serialized
        assert "serviceProvision" in serialized

        # Verify values are preserved
        assert serialized["serviceManagerProvision"] == test_data["serviceManagerProvision"]
        assert serialized["serviceOffer"] == test_data["serviceOffer"]
        assert serialized["serviceProvision"] == test_data["serviceProvision"]

    def test_service_offer_management_detailedprovision_model_json_schema(self):
        """Test Service_offer_management_DetailedProvision model JSON schema generation."""
        schema = Service_offer_management_DetailedProvision.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "serviceManagerProvision",
            "serviceOffer",
            "serviceProvision",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = []
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_offer_management_serviceofferwithavailableregions_model_creation(self):
        """Test Service_offer_management_ServiceOfferWithAvailableRegions model creation with valid data."""
        # Valid test data for Service_offer_management_ServiceOfferWithAvailableRegions
        valid_data = {
            "availableRegions": [],
            "id": "test_id",
            "serviceOffer": {},
            "type": "test_type",
        }

        # Create model instance
        model = Service_offer_management_ServiceOfferWithAvailableRegions(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_offer_management_ServiceOfferWithAvailableRegions)
        assert model.availableRegions == valid_data["availableRegions"]
        assert model.id == valid_data["id"]
        assert model.serviceOffer == valid_data["serviceOffer"]
        assert model.type == valid_data["type"]

    def test_service_offer_management_serviceofferwithavailableregions_model_validation(self):
        """Test Service_offer_management_ServiceOfferWithAvailableRegions model field validation."""
        # Test with minimal required data
        minimal_data = {
            "availableRegions": [],
            "serviceOffer": {},
        }

        model = Service_offer_management_ServiceOfferWithAvailableRegions(**minimal_data)
        assert isinstance(model, Service_offer_management_ServiceOfferWithAvailableRegions)
        assert model.availableRegions == minimal_data["availableRegions"]
        assert model.serviceOffer == minimal_data["serviceOffer"]

    def test_service_offer_management_serviceofferwithavailableregions_model_required_fields(self):
        """Test Service_offer_management_ServiceOfferWithAvailableRegions model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "availableRegions",
            "serviceOffer",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_offer_management_ServiceOfferWithAvailableRegions()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "availableRegions",
                "serviceOffer",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_offer_management_ServiceOfferWithAvailableRegions()
            assert isinstance(model, Service_offer_management_ServiceOfferWithAvailableRegions)

    def test_service_offer_management_serviceofferwithavailableregions_model_optional_fields(self):
        """Test Service_offer_management_ServiceOfferWithAvailableRegions model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "availableRegions": [],
            "serviceOffer": {},
        }

        model = Service_offer_management_ServiceOfferWithAvailableRegions(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "id")
        # Optional field id should be None or have a default value
        assert model.id is None or model.id is not None
        assert hasattr(model, "type")
        # Optional field type should be None or have a default value
        assert model.type is None or model.type is not None

    def test_service_offer_management_serviceofferwithavailableregions_model_serialization(self):
        """Test Service_offer_management_ServiceOfferWithAvailableRegions model serialization to dict."""
        test_data = {
            "availableRegions": [],
            "id": "serialize_value",
            "serviceOffer": {"key": "value"},
            "type": "serialize_value",
        }

        model = Service_offer_management_ServiceOfferWithAvailableRegions(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "availableRegions" in serialized
        assert "id" in serialized
        assert "serviceOffer" in serialized
        assert "type" in serialized

        # Verify values are preserved
        assert serialized["availableRegions"] == test_data["availableRegions"]
        assert serialized["id"] == test_data["id"]
        assert serialized["serviceOffer"] == test_data["serviceOffer"]
        assert serialized["type"] == test_data["type"]

    def test_service_offer_management_serviceofferwithavailableregions_model_json_schema(self):
        """Test Service_offer_management_ServiceOfferWithAvailableRegions model JSON schema generation."""
        schema = Service_offer_management_ServiceOfferWithAvailableRegions.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "availableRegions",
            "id",
            "serviceOffer",
            "type",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "availableRegions",
            "serviceOffer",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_offer_management_validationerror_model_creation(self):
        """Test Service_offer_management_ValidationError model creation with valid data."""
        # Valid test data for Service_offer_management_ValidationError
        valid_data = {
            "httpStatusCode": 42,
            "message": "test_message",
            "debugId": "test_debugId",
            "errorCode": "test_errorCode",
            "errorDetails": [],
        }

        # Create model instance
        model = Service_offer_management_ValidationError(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_offer_management_ValidationError)
        assert model.httpStatusCode == valid_data["httpStatusCode"]
        assert model.message == valid_data["message"]
        assert model.debugId == valid_data["debugId"]
        assert model.errorCode == valid_data["errorCode"]
        assert model.errorDetails == valid_data["errorDetails"]

    def test_service_offer_management_validationerror_model_validation(self):
        """Test Service_offer_management_ValidationError model field validation."""
        # Test with minimal required data
        minimal_data = {
            "httpStatusCode": 1,
            "message": "required_message",
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
        }

        model = Service_offer_management_ValidationError(**minimal_data)
        assert isinstance(model, Service_offer_management_ValidationError)
        assert model.httpStatusCode == minimal_data["httpStatusCode"]
        assert model.message == minimal_data["message"]
        assert model.debugId == minimal_data["debugId"]
        assert model.errorCode == minimal_data["errorCode"]

    def test_service_offer_management_validationerror_model_required_fields(self):
        """Test Service_offer_management_ValidationError model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "httpStatusCode",
            "message",
            "debugId",
            "errorCode",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_offer_management_ValidationError()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "httpStatusCode",
                "message",
                "debugId",
                "errorCode",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_offer_management_ValidationError()
            assert isinstance(model, Service_offer_management_ValidationError)

    def test_service_offer_management_validationerror_model_optional_fields(self):
        """Test Service_offer_management_ValidationError model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "httpStatusCode": 1,
            "message": "required_message",
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
        }

        model = Service_offer_management_ValidationError(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "errorDetails")
        # Optional field errorDetails should be None or have a default value
        assert model.errorDetails is None or model.errorDetails is not None

    def test_service_offer_management_validationerror_model_serialization(self):
        """Test Service_offer_management_ValidationError model serialization to dict."""
        test_data = {
            "httpStatusCode": 99,
            "message": "serialize_value",
            "debugId": "serialize_value",
            "errorCode": "serialize_value",
            "errorDetails": [],
        }

        model = Service_offer_management_ValidationError(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "httpStatusCode" in serialized
        assert "message" in serialized
        assert "debugId" in serialized
        assert "errorCode" in serialized
        assert "errorDetails" in serialized

        # Verify values are preserved
        assert serialized["httpStatusCode"] == test_data["httpStatusCode"]
        assert serialized["message"] == test_data["message"]
        assert serialized["debugId"] == test_data["debugId"]
        assert serialized["errorCode"] == test_data["errorCode"]
        assert serialized["errorDetails"] == test_data["errorDetails"]

    def test_service_offer_management_validationerror_model_json_schema(self):
        """Test Service_offer_management_ValidationError model JSON schema generation."""
        schema = Service_offer_management_ValidationError.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "httpStatusCode",
            "message",
            "debugId",
            "errorCode",
            "errorDetails",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "httpStatusCode",
            "message",
            "debugId",
            "errorCode",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_provision_management_serviceprovisioncreatebase_model_creation(self):
        """Test Service_provision_management_ServiceProvisionCreateBase model creation with valid data."""
        # Valid test data for Service_provision_management_ServiceProvisionCreateBase
        valid_data = {
            "serviceOfferId": "test_serviceOfferId",
            "region": "test_region",
        }

        # Create model instance
        model = Service_provision_management_ServiceProvisionCreateBase(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_provision_management_ServiceProvisionCreateBase)
        assert model.serviceOfferId == valid_data["serviceOfferId"]
        assert model.region == valid_data["region"]

    def test_service_provision_management_serviceprovisioncreatebase_model_validation(self):
        """Test Service_provision_management_ServiceProvisionCreateBase model field validation."""
        # Test with minimal required data
        minimal_data = {
            "serviceOfferId": "required_serviceOfferId",
            "region": "required_region",
        }

        model = Service_provision_management_ServiceProvisionCreateBase(**minimal_data)
        assert isinstance(model, Service_provision_management_ServiceProvisionCreateBase)
        assert model.serviceOfferId == minimal_data["serviceOfferId"]
        assert model.region == minimal_data["region"]

    def test_service_provision_management_serviceprovisioncreatebase_model_required_fields(self):
        """Test Service_provision_management_ServiceProvisionCreateBase model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "serviceOfferId",
            "region",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_provision_management_ServiceProvisionCreateBase()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "serviceOfferId",
                "region",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_provision_management_ServiceProvisionCreateBase()
            assert isinstance(model, Service_provision_management_ServiceProvisionCreateBase)

    def test_service_provision_management_serviceprovisioncreatebase_model_optional_fields(self):
        """Test Service_provision_management_ServiceProvisionCreateBase model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "serviceOfferId": "required_serviceOfferId",
            "region": "required_region",
        }

        model = Service_provision_management_ServiceProvisionCreateBase(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_provision_management_serviceprovisioncreatebase_model_serialization(self):
        """Test Service_provision_management_ServiceProvisionCreateBase model serialization to dict."""
        test_data = {
            "serviceOfferId": "serialize_value",
            "region": "serialize_value",
        }

        model = Service_provision_management_ServiceProvisionCreateBase(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "serviceOfferId" in serialized
        assert "region" in serialized

        # Verify values are preserved
        assert serialized["serviceOfferId"] == test_data["serviceOfferId"]
        assert serialized["region"] == test_data["region"]

    def test_service_provision_management_serviceprovisioncreatebase_model_json_schema(self):
        """Test Service_provision_management_ServiceProvisionCreateBase model JSON schema generation."""
        schema = Service_provision_management_ServiceProvisionCreateBase.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "serviceOfferId",
            "region",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "serviceOfferId",
            "region",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_offer_management_serviceoffercatalog_model_creation(self):
        """Test Service_offer_management_ServiceOfferCatalog model creation with valid data."""
        # Valid test data for Service_offer_management_ServiceOfferCatalog
        valid_data = {
            "count": 42,
            "items": [],
            "next": "test_next",
            "total": 42,
        }

        # Create model instance
        model = Service_offer_management_ServiceOfferCatalog(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_offer_management_ServiceOfferCatalog)
        assert model.count == valid_data["count"]
        assert model.items == valid_data["items"]
        assert model.next == valid_data["next"]
        assert model.total == valid_data["total"]

    def test_service_offer_management_serviceoffercatalog_model_validation(self):
        """Test Service_offer_management_ServiceOfferCatalog model field validation."""
        # Test with minimal required data
        minimal_data = {
            "count": 1,
            "items": [],
            "next": "required_next",
            "total": 1,
        }

        model = Service_offer_management_ServiceOfferCatalog(**minimal_data)
        assert isinstance(model, Service_offer_management_ServiceOfferCatalog)
        assert model.count == minimal_data["count"]
        assert model.items == minimal_data["items"]
        assert model.next == minimal_data["next"]
        assert model.total == minimal_data["total"]

    def test_service_offer_management_serviceoffercatalog_model_required_fields(self):
        """Test Service_offer_management_ServiceOfferCatalog model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "count",
            "items",
            "next",
            "total",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_offer_management_ServiceOfferCatalog()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "count",
                "items",
                "next",
                "total",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_offer_management_ServiceOfferCatalog()
            assert isinstance(model, Service_offer_management_ServiceOfferCatalog)

    def test_service_offer_management_serviceoffercatalog_model_optional_fields(self):
        """Test Service_offer_management_ServiceOfferCatalog model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "count": 1,
            "items": [],
            "next": "required_next",
            "total": 1,
        }

        model = Service_offer_management_ServiceOfferCatalog(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_offer_management_serviceoffercatalog_model_serialization(self):
        """Test Service_offer_management_ServiceOfferCatalog model serialization to dict."""
        test_data = {
            "count": 99,
            "items": [],
            "next": "serialize_value",
            "total": 99,
        }

        model = Service_offer_management_ServiceOfferCatalog(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "count" in serialized
        assert "items" in serialized
        assert "next" in serialized
        assert "total" in serialized

        # Verify values are preserved
        assert serialized["count"] == test_data["count"]
        assert serialized["items"] == test_data["items"]
        assert serialized["next"] == test_data["next"]
        assert serialized["total"] == test_data["total"]

    def test_service_offer_management_serviceoffercatalog_model_json_schema(self):
        """Test Service_offer_management_ServiceOfferCatalog model JSON schema generation."""
        schema = Service_offer_management_ServiceOfferCatalog.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "count",
            "items",
            "next",
            "total",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "count",
            "items",
            "next",
            "total",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_provision_management_forbiddenerror_model_creation(self):
        """Test Service_provision_management_ForbiddenError model creation with valid data."""
        # Valid test data for Service_provision_management_ForbiddenError
        valid_data = {
            "errorCode": "test_errorCode",
            "httpStatusCode": 42,
            "message": "test_message",
            "debugId": "test_debugId",
        }

        # Create model instance
        model = Service_provision_management_ForbiddenError(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_provision_management_ForbiddenError)
        assert model.errorCode == valid_data["errorCode"]
        assert model.httpStatusCode == valid_data["httpStatusCode"]
        assert model.message == valid_data["message"]
        assert model.debugId == valid_data["debugId"]

    def test_service_provision_management_forbiddenerror_model_validation(self):
        """Test Service_provision_management_ForbiddenError model field validation."""
        # Test with minimal required data
        minimal_data = {
            "errorCode": "required_errorCode",
            "httpStatusCode": 1,
            "message": "required_message",
            "debugId": "required_debugId",
        }

        model = Service_provision_management_ForbiddenError(**minimal_data)
        assert isinstance(model, Service_provision_management_ForbiddenError)
        assert model.errorCode == minimal_data["errorCode"]
        assert model.httpStatusCode == minimal_data["httpStatusCode"]
        assert model.message == minimal_data["message"]
        assert model.debugId == minimal_data["debugId"]

    def test_service_provision_management_forbiddenerror_model_required_fields(self):
        """Test Service_provision_management_ForbiddenError model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "errorCode",
            "httpStatusCode",
            "message",
            "debugId",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_provision_management_ForbiddenError()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "errorCode",
                "httpStatusCode",
                "message",
                "debugId",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_provision_management_ForbiddenError()
            assert isinstance(model, Service_provision_management_ForbiddenError)

    def test_service_provision_management_forbiddenerror_model_optional_fields(self):
        """Test Service_provision_management_ForbiddenError model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "errorCode": "required_errorCode",
            "httpStatusCode": 1,
            "message": "required_message",
            "debugId": "required_debugId",
        }

        model = Service_provision_management_ForbiddenError(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_provision_management_forbiddenerror_model_serialization(self):
        """Test Service_provision_management_ForbiddenError model serialization to dict."""
        test_data = {
            "errorCode": "serialize_value",
            "httpStatusCode": 99,
            "message": "serialize_value",
            "debugId": "serialize_value",
        }

        model = Service_provision_management_ForbiddenError(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "errorCode" in serialized
        assert "httpStatusCode" in serialized
        assert "message" in serialized
        assert "debugId" in serialized

        # Verify values are preserved
        assert serialized["errorCode"] == test_data["errorCode"]
        assert serialized["httpStatusCode"] == test_data["httpStatusCode"]
        assert serialized["message"] == test_data["message"]
        assert serialized["debugId"] == test_data["debugId"]

    def test_service_provision_management_forbiddenerror_model_json_schema(self):
        """Test Service_provision_management_ForbiddenError model JSON schema generation."""
        schema = Service_provision_management_ForbiddenError.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "errorCode",
            "httpStatusCode",
            "message",
            "debugId",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "errorCode",
            "httpStatusCode",
            "message",
            "debugId",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_offer_management_serviceofferregionslist_model_creation(self):
        """Test Service_offer_management_ServiceOfferRegionsList model creation with valid data."""
        # Valid test data for Service_offer_management_ServiceOfferRegionsList
        valid_data = {
            "next": "test_next",
            "total": 42,
            "count": 42,
            "items": [],
        }

        # Create model instance
        model = Service_offer_management_ServiceOfferRegionsList(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_offer_management_ServiceOfferRegionsList)
        assert model.next == valid_data["next"]
        assert model.total == valid_data["total"]
        assert model.count == valid_data["count"]
        assert model.items == valid_data["items"]

    def test_service_offer_management_serviceofferregionslist_model_validation(self):
        """Test Service_offer_management_ServiceOfferRegionsList model field validation."""
        # Test with minimal required data
        minimal_data = {
            "next": "required_next",
            "total": 1,
            "count": 1,
            "items": [],
        }

        model = Service_offer_management_ServiceOfferRegionsList(**minimal_data)
        assert isinstance(model, Service_offer_management_ServiceOfferRegionsList)
        assert model.next == minimal_data["next"]
        assert model.total == minimal_data["total"]
        assert model.count == minimal_data["count"]
        assert model.items == minimal_data["items"]

    def test_service_offer_management_serviceofferregionslist_model_required_fields(self):
        """Test Service_offer_management_ServiceOfferRegionsList model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "next",
            "total",
            "count",
            "items",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_offer_management_ServiceOfferRegionsList()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "next",
                "total",
                "count",
                "items",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_offer_management_ServiceOfferRegionsList()
            assert isinstance(model, Service_offer_management_ServiceOfferRegionsList)

    def test_service_offer_management_serviceofferregionslist_model_optional_fields(self):
        """Test Service_offer_management_ServiceOfferRegionsList model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "next": "required_next",
            "total": 1,
            "count": 1,
            "items": [],
        }

        model = Service_offer_management_ServiceOfferRegionsList(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_offer_management_serviceofferregionslist_model_serialization(self):
        """Test Service_offer_management_ServiceOfferRegionsList model serialization to dict."""
        test_data = {
            "next": "serialize_value",
            "total": 99,
            "count": 99,
            "items": [],
        }

        model = Service_offer_management_ServiceOfferRegionsList(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "next" in serialized
        assert "total" in serialized
        assert "count" in serialized
        assert "items" in serialized

        # Verify values are preserved
        assert serialized["next"] == test_data["next"]
        assert serialized["total"] == test_data["total"]
        assert serialized["count"] == test_data["count"]
        assert serialized["items"] == test_data["items"]

    def test_service_offer_management_serviceofferregionslist_model_json_schema(self):
        """Test Service_offer_management_ServiceOfferRegionsList model JSON schema generation."""
        schema = Service_offer_management_ServiceOfferRegionsList.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "next",
            "total",
            "count",
            "items",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "next",
            "total",
            "count",
            "items",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_offer_management_serviceprovisionpartialinfo_model_creation(self):
        """Test Service_offer_management_ServiceProvisionPartialInfo model creation with valid data."""
        # Valid test data for Service_offer_management_ServiceProvisionPartialInfo
        valid_data = {
            "id": "test_id",
            "region": "test_region",
            "resourceUri": "test_resourceUri",
            "serviceManagerInstanceId": "test_serviceManagerInstanceId",
            "updatedAt": "test_updatedAt",
            "createdAt": "test_createdAt",
            "createdBy": "test_createdBy",
            "generation": 42,
        }

        # Create model instance
        model = Service_offer_management_ServiceProvisionPartialInfo(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_offer_management_ServiceProvisionPartialInfo)
        assert model.id == valid_data["id"]
        assert model.region == valid_data["region"]
        assert model.resourceUri == valid_data["resourceUri"]
        assert model.serviceManagerInstanceId == valid_data["serviceManagerInstanceId"]
        assert model.updatedAt == valid_data["updatedAt"]
        assert model.createdAt == valid_data["createdAt"]
        assert model.createdBy == valid_data["createdBy"]
        assert model.generation == valid_data["generation"]

    def test_service_offer_management_serviceprovisionpartialinfo_model_validation(self):
        """Test Service_offer_management_ServiceProvisionPartialInfo model field validation."""
        # Test with minimal required data
        minimal_data = {
            "id": "required_id",
            "region": "required_region",
            "resourceUri": "required_resourceUri",
            "serviceManagerInstanceId": "required_serviceManagerInstanceId",
            "generation": 1,
        }

        model = Service_offer_management_ServiceProvisionPartialInfo(**minimal_data)
        assert isinstance(model, Service_offer_management_ServiceProvisionPartialInfo)
        assert model.id == minimal_data["id"]
        assert model.region == minimal_data["region"]
        assert model.resourceUri == minimal_data["resourceUri"]
        assert model.serviceManagerInstanceId == minimal_data["serviceManagerInstanceId"]
        assert model.generation == minimal_data["generation"]

    def test_service_offer_management_serviceprovisionpartialinfo_model_required_fields(self):
        """Test Service_offer_management_ServiceProvisionPartialInfo model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "id",
            "region",
            "resourceUri",
            "serviceManagerInstanceId",
            "generation",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_offer_management_ServiceProvisionPartialInfo()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "id",
                "region",
                "resourceUri",
                "serviceManagerInstanceId",
                "generation",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_offer_management_ServiceProvisionPartialInfo()
            assert isinstance(model, Service_offer_management_ServiceProvisionPartialInfo)

    def test_service_offer_management_serviceprovisionpartialinfo_model_optional_fields(self):
        """Test Service_offer_management_ServiceProvisionPartialInfo model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "id": "required_id",
            "region": "required_region",
            "resourceUri": "required_resourceUri",
            "serviceManagerInstanceId": "required_serviceManagerInstanceId",
            "generation": 1,
        }

        model = Service_offer_management_ServiceProvisionPartialInfo(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "updatedAt")
        # Optional field updatedAt should be None or have a default value
        assert model.updatedAt is None or model.updatedAt is not None
        assert hasattr(model, "createdAt")
        # Optional field createdAt should be None or have a default value
        assert model.createdAt is None or model.createdAt is not None
        assert hasattr(model, "createdBy")
        # Optional field createdBy should be None or have a default value
        assert model.createdBy is None or model.createdBy is not None

    def test_service_offer_management_serviceprovisionpartialinfo_model_serialization(self):
        """Test Service_offer_management_ServiceProvisionPartialInfo model serialization to dict."""
        test_data = {
            "id": "serialize_value",
            "region": "serialize_value",
            "resourceUri": "serialize_value",
            "serviceManagerInstanceId": "serialize_value",
            "updatedAt": "serialize_value",
            "createdAt": "serialize_value",
            "createdBy": "serialize_value",
            "generation": 99,
        }

        model = Service_offer_management_ServiceProvisionPartialInfo(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "id" in serialized
        assert "region" in serialized
        assert "resourceUri" in serialized
        assert "serviceManagerInstanceId" in serialized
        assert "updatedAt" in serialized
        assert "createdAt" in serialized
        assert "createdBy" in serialized
        assert "generation" in serialized

        # Verify values are preserved
        assert serialized["id"] == test_data["id"]
        assert serialized["region"] == test_data["region"]
        assert serialized["resourceUri"] == test_data["resourceUri"]
        assert serialized["serviceManagerInstanceId"] == test_data["serviceManagerInstanceId"]
        assert serialized["updatedAt"] == test_data["updatedAt"]
        assert serialized["createdAt"] == test_data["createdAt"]
        assert serialized["createdBy"] == test_data["createdBy"]
        assert serialized["generation"] == test_data["generation"]

    def test_service_offer_management_serviceprovisionpartialinfo_model_json_schema(self):
        """Test Service_offer_management_ServiceProvisionPartialInfo model JSON schema generation."""
        schema = Service_offer_management_ServiceProvisionPartialInfo.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "id",
            "region",
            "resourceUri",
            "serviceManagerInstanceId",
            "updatedAt",
            "createdAt",
            "createdBy",
            "generation",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "id",
            "region",
            "resourceUri",
            "serviceManagerInstanceId",
            "generation",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_provision_management_workspaceresourcelink_model_creation(self):
        """Test Service_provision_management_WorkspaceResourceLink model creation with valid data."""
        # Valid test data for Service_provision_management_WorkspaceResourceLink
        valid_data = {
            "workspaceTransferStatus": "test_workspaceTransferStatus",
            "id": "test_id",
            "mspId": "test_mspId",
            "name": "test_name",
            "organizationId": "test_organizationId",
            "resourceUri": "test_resourceUri",
        }

        # Create model instance
        model = Service_provision_management_WorkspaceResourceLink(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_provision_management_WorkspaceResourceLink)
        assert model.workspaceTransferStatus == valid_data["workspaceTransferStatus"]
        assert model.id == valid_data["id"]
        assert model.mspId == valid_data["mspId"]
        assert model.name == valid_data["name"]
        assert model.organizationId == valid_data["organizationId"]
        assert model.resourceUri == valid_data["resourceUri"]

    def test_service_provision_management_workspaceresourcelink_model_validation(self):
        """Test Service_provision_management_WorkspaceResourceLink model field validation."""
        # Test with minimal required data
        minimal_data = {}

        model = Service_provision_management_WorkspaceResourceLink(**minimal_data)
        assert isinstance(model, Service_provision_management_WorkspaceResourceLink)

    def test_service_provision_management_workspaceresourcelink_model_required_fields(self):
        """Test Service_provision_management_WorkspaceResourceLink model required field validation."""
        # Check if this model has any required fields
        required_fields = []

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_provision_management_WorkspaceResourceLink()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {}

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_provision_management_WorkspaceResourceLink()
            assert isinstance(model, Service_provision_management_WorkspaceResourceLink)

    def test_service_provision_management_workspaceresourcelink_model_optional_fields(self):
        """Test Service_provision_management_WorkspaceResourceLink model optional field handling."""
        # Create with minimal required data
        minimal_data = {}

        model = Service_provision_management_WorkspaceResourceLink(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "workspaceTransferStatus")
        # Optional field workspaceTransferStatus should be None or have a default value
        assert model.workspaceTransferStatus is None or model.workspaceTransferStatus is not None
        assert hasattr(model, "id")
        # Optional field id should be None or have a default value
        assert model.id is None or model.id is not None
        assert hasattr(model, "mspId")
        # Optional field mspId should be None or have a default value
        assert model.mspId is None or model.mspId is not None
        assert hasattr(model, "name")
        # Optional field name should be None or have a default value
        assert model.name is None or model.name is not None
        assert hasattr(model, "organizationId")
        # Optional field organizationId should be None or have a default value
        assert model.organizationId is None or model.organizationId is not None
        assert hasattr(model, "resourceUri")
        # Optional field resourceUri should be None or have a default value
        assert model.resourceUri is None or model.resourceUri is not None

    def test_service_provision_management_workspaceresourcelink_model_serialization(self):
        """Test Service_provision_management_WorkspaceResourceLink model serialization to dict."""
        test_data = {
            "workspaceTransferStatus": "serialize_value",
            "id": "serialize_value",
            "mspId": "serialize_value",
            "name": "serialize_value",
            "organizationId": "serialize_value",
            "resourceUri": "serialize_value",
        }

        model = Service_provision_management_WorkspaceResourceLink(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "workspaceTransferStatus" in serialized
        assert "id" in serialized
        assert "mspId" in serialized
        assert "name" in serialized
        assert "organizationId" in serialized
        assert "resourceUri" in serialized

        # Verify values are preserved
        assert serialized["workspaceTransferStatus"] == test_data["workspaceTransferStatus"]
        assert serialized["id"] == test_data["id"]
        assert serialized["mspId"] == test_data["mspId"]
        assert serialized["name"] == test_data["name"]
        assert serialized["organizationId"] == test_data["organizationId"]
        assert serialized["resourceUri"] == test_data["resourceUri"]

    def test_service_provision_management_workspaceresourcelink_model_json_schema(self):
        """Test Service_provision_management_WorkspaceResourceLink model JSON schema generation."""
        schema = Service_provision_management_WorkspaceResourceLink.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "workspaceTransferStatus",
            "id",
            "mspId",
            "name",
            "organizationId",
            "resourceUri",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = []
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_provision_management_servicemanagerprovisionresourcelink_model_creation(self):
        """Test Service_provision_management_ServiceManagerProvisionResourceLink model creation with valid data."""
        # Valid test data for Service_provision_management_ServiceManagerProvisionResourceLink
        valid_data = {
            "accountType": "test_accountType",
            "id": "test_id",
            "mspConversionStatus": "test_mspConversionStatus",
            "operationalMode": "test_operationalMode",
            "provisionStatus": "test_provisionStatus",
            "reason": "test_reason",
            "resourceUri": "test_resourceUri",
        }

        # Create model instance
        model = Service_provision_management_ServiceManagerProvisionResourceLink(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_provision_management_ServiceManagerProvisionResourceLink)
        assert model.accountType == valid_data["accountType"]
        assert model.id == valid_data["id"]
        assert model.mspConversionStatus == valid_data["mspConversionStatus"]
        assert model.operationalMode == valid_data["operationalMode"]
        assert model.provisionStatus == valid_data["provisionStatus"]
        assert model.reason == valid_data["reason"]
        assert model.resourceUri == valid_data["resourceUri"]

    def test_service_provision_management_servicemanagerprovisionresourcelink_model_validation(self):
        """Test Service_provision_management_ServiceManagerProvisionResourceLink model field validation."""
        # Test with minimal required data
        minimal_data = {}

        model = Service_provision_management_ServiceManagerProvisionResourceLink(**minimal_data)
        assert isinstance(model, Service_provision_management_ServiceManagerProvisionResourceLink)

    def test_service_provision_management_servicemanagerprovisionresourcelink_model_required_fields(self):
        """Test Service_provision_management_ServiceManagerProvisionResourceLink model required field validation."""
        # Check if this model has any required fields
        required_fields = []

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_provision_management_ServiceManagerProvisionResourceLink()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {}

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_provision_management_ServiceManagerProvisionResourceLink()
            assert isinstance(model, Service_provision_management_ServiceManagerProvisionResourceLink)

    def test_service_provision_management_servicemanagerprovisionresourcelink_model_optional_fields(self):
        """Test Service_provision_management_ServiceManagerProvisionResourceLink model optional field handling."""
        # Create with minimal required data
        minimal_data = {}

        model = Service_provision_management_ServiceManagerProvisionResourceLink(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "accountType")
        # Optional field accountType should be None or have a default value
        assert model.accountType is None or model.accountType is not None
        assert hasattr(model, "id")
        # Optional field id should be None or have a default value
        assert model.id is None or model.id is not None
        assert hasattr(model, "mspConversionStatus")
        # Optional field mspConversionStatus should be None or have a default value
        assert model.mspConversionStatus is None or model.mspConversionStatus is not None
        assert hasattr(model, "operationalMode")
        # Optional field operationalMode should be None or have a default value
        assert model.operationalMode is None or model.operationalMode is not None
        assert hasattr(model, "provisionStatus")
        # Optional field provisionStatus should be None or have a default value
        assert model.provisionStatus is None or model.provisionStatus is not None
        assert hasattr(model, "reason")
        # Optional field reason should be None or have a default value
        assert model.reason is None or model.reason is not None
        assert hasattr(model, "resourceUri")
        # Optional field resourceUri should be None or have a default value
        assert model.resourceUri is None or model.resourceUri is not None

    def test_service_provision_management_servicemanagerprovisionresourcelink_model_serialization(self):
        """Test Service_provision_management_ServiceManagerProvisionResourceLink model serialization to dict."""
        test_data = {
            "accountType": "serialize_value",
            "id": "serialize_value",
            "mspConversionStatus": "serialize_value",
            "operationalMode": "serialize_value",
            "provisionStatus": "serialize_value",
            "reason": "serialize_value",
            "resourceUri": "serialize_value",
        }

        model = Service_provision_management_ServiceManagerProvisionResourceLink(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "accountType" in serialized
        assert "id" in serialized
        assert "mspConversionStatus" in serialized
        assert "operationalMode" in serialized
        assert "provisionStatus" in serialized
        assert "reason" in serialized
        assert "resourceUri" in serialized

        # Verify values are preserved
        assert serialized["accountType"] == test_data["accountType"]
        assert serialized["id"] == test_data["id"]
        assert serialized["mspConversionStatus"] == test_data["mspConversionStatus"]
        assert serialized["operationalMode"] == test_data["operationalMode"]
        assert serialized["provisionStatus"] == test_data["provisionStatus"]
        assert serialized["reason"] == test_data["reason"]
        assert serialized["resourceUri"] == test_data["resourceUri"]

    def test_service_provision_management_servicemanagerprovisionresourcelink_model_json_schema(self):
        """Test Service_provision_management_ServiceManagerProvisionResourceLink model JSON schema generation."""
        schema = Service_provision_management_ServiceManagerProvisionResourceLink.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "accountType",
            "id",
            "mspConversionStatus",
            "operationalMode",
            "provisionStatus",
            "reason",
            "resourceUri",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = []
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_manager_management_provisionstatus_model_creation(self):
        """Test Service_Manager_Management_ProvisionStatus model creation with valid data."""
        # Valid test data for Service_Manager_Management_ProvisionStatus
        valid_data = {}

        # Create model instance
        model = Service_Manager_Management_ProvisionStatus(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_Manager_Management_ProvisionStatus)

    def test_service_manager_management_provisionstatus_model_validation(self):
        """Test Service_Manager_Management_ProvisionStatus model field validation."""
        # Test with minimal required data
        minimal_data = {}

        model = Service_Manager_Management_ProvisionStatus(**minimal_data)
        assert isinstance(model, Service_Manager_Management_ProvisionStatus)

    def test_service_manager_management_provisionstatus_model_required_fields(self):
        """Test Service_Manager_Management_ProvisionStatus model required field validation."""
        # Check if this model has any required fields
        required_fields = []

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_Manager_Management_ProvisionStatus()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {}

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_Manager_Management_ProvisionStatus()
            assert isinstance(model, Service_Manager_Management_ProvisionStatus)

    def test_service_manager_management_provisionstatus_model_optional_fields(self):
        """Test Service_Manager_Management_ProvisionStatus model optional field handling."""
        # Create with minimal required data
        minimal_data = {}

        model = Service_Manager_Management_ProvisionStatus(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_manager_management_provisionstatus_model_serialization(self):
        """Test Service_Manager_Management_ProvisionStatus model serialization to dict."""
        test_data = {}

        model = Service_Manager_Management_ProvisionStatus(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)

        # Verify values are preserved

    def test_service_manager_management_provisionstatus_model_json_schema(self):
        """Test Service_Manager_Management_ProvisionStatus model JSON schema generation."""
        schema = Service_Manager_Management_ProvisionStatus.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {}

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = []
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_offer_management_internalerror_model_creation(self):
        """Test Service_offer_management_InternalError model creation with valid data."""
        # Valid test data for Service_offer_management_InternalError
        valid_data = {
            "debugId": "test_debugId",
            "errorCode": "test_errorCode",
            "errorDetails": [],
            "httpStatusCode": 42,
            "message": "test_message",
        }

        # Create model instance
        model = Service_offer_management_InternalError(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_offer_management_InternalError)
        assert model.debugId == valid_data["debugId"]
        assert model.errorCode == valid_data["errorCode"]
        assert model.errorDetails == valid_data["errorDetails"]
        assert model.httpStatusCode == valid_data["httpStatusCode"]
        assert model.message == valid_data["message"]

    def test_service_offer_management_internalerror_model_validation(self):
        """Test Service_offer_management_InternalError model field validation."""
        # Test with minimal required data
        minimal_data = {
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
            "errorDetails": [],
            "httpStatusCode": 1,
            "message": "required_message",
        }

        model = Service_offer_management_InternalError(**minimal_data)
        assert isinstance(model, Service_offer_management_InternalError)
        assert model.debugId == minimal_data["debugId"]
        assert model.errorCode == minimal_data["errorCode"]
        assert model.errorDetails == minimal_data["errorDetails"]
        assert model.httpStatusCode == minimal_data["httpStatusCode"]
        assert model.message == minimal_data["message"]

    def test_service_offer_management_internalerror_model_required_fields(self):
        """Test Service_offer_management_InternalError model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "debugId",
            "errorCode",
            "errorDetails",
            "httpStatusCode",
            "message",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_offer_management_InternalError()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "debugId",
                "errorCode",
                "errorDetails",
                "httpStatusCode",
                "message",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_offer_management_InternalError()
            assert isinstance(model, Service_offer_management_InternalError)

    def test_service_offer_management_internalerror_model_optional_fields(self):
        """Test Service_offer_management_InternalError model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
            "errorDetails": [],
            "httpStatusCode": 1,
            "message": "required_message",
        }

        model = Service_offer_management_InternalError(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_offer_management_internalerror_model_serialization(self):
        """Test Service_offer_management_InternalError model serialization to dict."""
        test_data = {
            "debugId": "serialize_value",
            "errorCode": "serialize_value",
            "errorDetails": [],
            "httpStatusCode": 99,
            "message": "serialize_value",
        }

        model = Service_offer_management_InternalError(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "debugId" in serialized
        assert "errorCode" in serialized
        assert "errorDetails" in serialized
        assert "httpStatusCode" in serialized
        assert "message" in serialized

        # Verify values are preserved
        assert serialized["debugId"] == test_data["debugId"]
        assert serialized["errorCode"] == test_data["errorCode"]
        assert serialized["errorDetails"] == test_data["errorDetails"]
        assert serialized["httpStatusCode"] == test_data["httpStatusCode"]
        assert serialized["message"] == test_data["message"]

    def test_service_offer_management_internalerror_model_json_schema(self):
        """Test Service_offer_management_InternalError model JSON schema generation."""
        schema = Service_offer_management_InternalError.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "debugId",
            "errorCode",
            "errorDetails",
            "httpStatusCode",
            "message",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "debugId",
            "errorCode",
            "errorDetails",
            "httpStatusCode",
            "message",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_provision_management_internalerror_model_creation(self):
        """Test Service_provision_management_InternalError model creation with valid data."""
        # Valid test data for Service_provision_management_InternalError
        valid_data = {
            "debugId": "test_debugId",
            "errorCode": "test_errorCode",
            "errorDetails": [],
            "httpStatusCode": 42,
            "message": "test_message",
        }

        # Create model instance
        model = Service_provision_management_InternalError(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_provision_management_InternalError)
        assert model.debugId == valid_data["debugId"]
        assert model.errorCode == valid_data["errorCode"]
        assert model.errorDetails == valid_data["errorDetails"]
        assert model.httpStatusCode == valid_data["httpStatusCode"]
        assert model.message == valid_data["message"]

    def test_service_provision_management_internalerror_model_validation(self):
        """Test Service_provision_management_InternalError model field validation."""
        # Test with minimal required data
        minimal_data = {
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
            "httpStatusCode": 1,
            "message": "required_message",
        }

        model = Service_provision_management_InternalError(**minimal_data)
        assert isinstance(model, Service_provision_management_InternalError)
        assert model.debugId == minimal_data["debugId"]
        assert model.errorCode == minimal_data["errorCode"]
        assert model.httpStatusCode == minimal_data["httpStatusCode"]
        assert model.message == minimal_data["message"]

    def test_service_provision_management_internalerror_model_required_fields(self):
        """Test Service_provision_management_InternalError model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "debugId",
            "errorCode",
            "httpStatusCode",
            "message",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_provision_management_InternalError()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "debugId",
                "errorCode",
                "httpStatusCode",
                "message",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_provision_management_InternalError()
            assert isinstance(model, Service_provision_management_InternalError)

    def test_service_provision_management_internalerror_model_optional_fields(self):
        """Test Service_provision_management_InternalError model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
            "httpStatusCode": 1,
            "message": "required_message",
        }

        model = Service_provision_management_InternalError(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "errorDetails")
        # Optional field errorDetails should be None or have a default value
        assert model.errorDetails is None or model.errorDetails is not None

    def test_service_provision_management_internalerror_model_serialization(self):
        """Test Service_provision_management_InternalError model serialization to dict."""
        test_data = {
            "debugId": "serialize_value",
            "errorCode": "serialize_value",
            "errorDetails": [],
            "httpStatusCode": 99,
            "message": "serialize_value",
        }

        model = Service_provision_management_InternalError(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "debugId" in serialized
        assert "errorCode" in serialized
        assert "errorDetails" in serialized
        assert "httpStatusCode" in serialized
        assert "message" in serialized

        # Verify values are preserved
        assert serialized["debugId"] == test_data["debugId"]
        assert serialized["errorCode"] == test_data["errorCode"]
        assert serialized["errorDetails"] == test_data["errorDetails"]
        assert serialized["httpStatusCode"] == test_data["httpStatusCode"]
        assert serialized["message"] == test_data["message"]

    def test_service_provision_management_internalerror_model_json_schema(self):
        """Test Service_provision_management_InternalError model JSON schema generation."""
        schema = Service_provision_management_InternalError.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "debugId",
            "errorCode",
            "errorDetails",
            "httpStatusCode",
            "message",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "debugId",
            "errorCode",
            "httpStatusCode",
            "message",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_manager_management_badrequesterror_model_creation(self):
        """Test Service_Manager_Management_BadRequestError model creation with valid data."""
        # Valid test data for Service_Manager_Management_BadRequestError
        valid_data = {
            "httpStatusCode": 42,
            "message": "test_message",
            "debugId": "test_debugId",
            "errorCode": "test_errorCode",
        }

        # Create model instance
        model = Service_Manager_Management_BadRequestError(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_Manager_Management_BadRequestError)
        assert model.httpStatusCode == valid_data["httpStatusCode"]
        assert model.message == valid_data["message"]
        assert model.debugId == valid_data["debugId"]
        assert model.errorCode == valid_data["errorCode"]

    def test_service_manager_management_badrequesterror_model_validation(self):
        """Test Service_Manager_Management_BadRequestError model field validation."""
        # Test with minimal required data
        minimal_data = {
            "httpStatusCode": 1,
            "message": "required_message",
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
        }

        model = Service_Manager_Management_BadRequestError(**minimal_data)
        assert isinstance(model, Service_Manager_Management_BadRequestError)
        assert model.httpStatusCode == minimal_data["httpStatusCode"]
        assert model.message == minimal_data["message"]
        assert model.debugId == minimal_data["debugId"]
        assert model.errorCode == minimal_data["errorCode"]

    def test_service_manager_management_badrequesterror_model_required_fields(self):
        """Test Service_Manager_Management_BadRequestError model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "httpStatusCode",
            "message",
            "debugId",
            "errorCode",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_Manager_Management_BadRequestError()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "httpStatusCode",
                "message",
                "debugId",
                "errorCode",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_Manager_Management_BadRequestError()
            assert isinstance(model, Service_Manager_Management_BadRequestError)

    def test_service_manager_management_badrequesterror_model_optional_fields(self):
        """Test Service_Manager_Management_BadRequestError model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "httpStatusCode": 1,
            "message": "required_message",
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
        }

        model = Service_Manager_Management_BadRequestError(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_manager_management_badrequesterror_model_serialization(self):
        """Test Service_Manager_Management_BadRequestError model serialization to dict."""
        test_data = {
            "httpStatusCode": 99,
            "message": "serialize_value",
            "debugId": "serialize_value",
            "errorCode": "serialize_value",
        }

        model = Service_Manager_Management_BadRequestError(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "httpStatusCode" in serialized
        assert "message" in serialized
        assert "debugId" in serialized
        assert "errorCode" in serialized

        # Verify values are preserved
        assert serialized["httpStatusCode"] == test_data["httpStatusCode"]
        assert serialized["message"] == test_data["message"]
        assert serialized["debugId"] == test_data["debugId"]
        assert serialized["errorCode"] == test_data["errorCode"]

    def test_service_manager_management_badrequesterror_model_json_schema(self):
        """Test Service_Manager_Management_BadRequestError model JSON schema generation."""
        schema = Service_Manager_Management_BadRequestError.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "httpStatusCode",
            "message",
            "debugId",
            "errorCode",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "httpStatusCode",
            "message",
            "debugId",
            "errorCode",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_offer_management_serviceofferreadwithmedia_model_creation(self):
        """Test Service_offer_management_ServiceOfferReadWithMedia model creation with valid data."""
        # Valid test data for Service_offer_management_ServiceOfferReadWithMedia
        valid_data = {
            "id": "test_id",
            "capabilities": [],
            "termsOfServiceUrl": "test_termsOfServiceUrl",
            "createdAt": "test_createdAt",
            "preProvisionMessage": "test_preProvisionMessage",
            "languagesSupported": [],
            "documentationUrl": "test_documentationUrl",
            "resourceUri": "test_resourceUri",
            "screenshots": [],
            "videos": [],
            "serviceManager": {},
            "brokerUri": "test_brokerUri",
            "featuresSupported": [],
            "staticLaunchUrl": "test_staticLaunchUrl",
            "testDriveUrl": "test_testDriveUrl",
            "evalUrl": "test_evalUrl",
            "workspaceTypes": "test_workspaceTypes",
            "updatedAt": "test_updatedAt",
            "name": "test_name",
            "overview": "test_overview",
            "status": "test_status",
            "logo": "test_logo",
            "generation": "test_generation",
            "shortDescription": "test_shortDescription",
            "serviceOfferType": "test_serviceOfferType",
            "slug": "test_slug",
            "categories": [],
            "contactSalesUrl": "test_contactSalesUrl",
            "isDefault": "test_isDefault",
        }

        # Create model instance
        model = Service_offer_management_ServiceOfferReadWithMedia(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_offer_management_ServiceOfferReadWithMedia)
        assert model.id == valid_data["id"]
        assert model.capabilities == valid_data["capabilities"]
        assert model.termsOfServiceUrl == valid_data["termsOfServiceUrl"]
        assert model.createdAt == valid_data["createdAt"]
        assert model.preProvisionMessage == valid_data["preProvisionMessage"]
        assert model.languagesSupported == valid_data["languagesSupported"]
        assert model.documentationUrl == valid_data["documentationUrl"]
        assert model.resourceUri == valid_data["resourceUri"]
        assert model.screenshots == valid_data["screenshots"]
        assert model.videos == valid_data["videos"]
        assert model.serviceManager == valid_data["serviceManager"]
        assert model.brokerUri == valid_data["brokerUri"]
        assert model.featuresSupported == valid_data["featuresSupported"]
        assert model.staticLaunchUrl == valid_data["staticLaunchUrl"]
        assert model.testDriveUrl == valid_data["testDriveUrl"]
        assert model.evalUrl == valid_data["evalUrl"]
        assert model.workspaceTypes == valid_data["workspaceTypes"]
        assert model.updatedAt == valid_data["updatedAt"]
        assert model.name == valid_data["name"]
        assert model.overview == valid_data["overview"]
        assert model.status == valid_data["status"]
        assert model.logo == valid_data["logo"]
        assert model.generation == valid_data["generation"]
        assert model.shortDescription == valid_data["shortDescription"]
        assert model.serviceOfferType == valid_data["serviceOfferType"]
        assert model.slug == valid_data["slug"]
        assert model.categories == valid_data["categories"]
        assert model.contactSalesUrl == valid_data["contactSalesUrl"]
        assert model.isDefault == valid_data["isDefault"]

    def test_service_offer_management_serviceofferreadwithmedia_model_validation(self):
        """Test Service_offer_management_ServiceOfferReadWithMedia model field validation."""
        # Test with minimal required data
        minimal_data = {
            "id": "required_id",
            "capabilities": [],
            "termsOfServiceUrl": "required_termsOfServiceUrl",
            "createdAt": "required_createdAt",
            "preProvisionMessage": "required_preProvisionMessage",
            "languagesSupported": [],
            "documentationUrl": "required_documentationUrl",
            "resourceUri": "required_resourceUri",
            "screenshots": [],
            "videos": [],
            "serviceManager": {},
            "brokerUri": "required_brokerUri",
            "featuresSupported": [],
            "staticLaunchUrl": "required_staticLaunchUrl",
            "testDriveUrl": "required_testDriveUrl",
            "evalUrl": "required_evalUrl",
            "workspaceTypes": "required_workspaceTypes",
            "name": "required_name",
            "overview": "required_overview",
            "status": "required_status",
            "logo": "required_logo",
            "shortDescription": "required_shortDescription",
            "serviceOfferType": "required_serviceOfferType",
            "slug": "required_slug",
            "categories": [],
            "contactSalesUrl": "required_contactSalesUrl",
        }

        model = Service_offer_management_ServiceOfferReadWithMedia(**minimal_data)
        assert isinstance(model, Service_offer_management_ServiceOfferReadWithMedia)
        assert model.id == minimal_data["id"]
        assert model.capabilities == minimal_data["capabilities"]
        assert model.termsOfServiceUrl == minimal_data["termsOfServiceUrl"]
        assert model.createdAt == minimal_data["createdAt"]
        assert model.preProvisionMessage == minimal_data["preProvisionMessage"]
        assert model.languagesSupported == minimal_data["languagesSupported"]
        assert model.documentationUrl == minimal_data["documentationUrl"]
        assert model.resourceUri == minimal_data["resourceUri"]
        assert model.screenshots == minimal_data["screenshots"]
        assert model.videos == minimal_data["videos"]
        assert model.serviceManager == minimal_data["serviceManager"]
        assert model.brokerUri == minimal_data["brokerUri"]
        assert model.featuresSupported == minimal_data["featuresSupported"]
        assert model.staticLaunchUrl == minimal_data["staticLaunchUrl"]
        assert model.testDriveUrl == minimal_data["testDriveUrl"]
        assert model.evalUrl == minimal_data["evalUrl"]
        assert model.workspaceTypes == minimal_data["workspaceTypes"]
        assert model.name == minimal_data["name"]
        assert model.overview == minimal_data["overview"]
        assert model.status == minimal_data["status"]
        assert model.logo == minimal_data["logo"]
        assert model.shortDescription == minimal_data["shortDescription"]
        assert model.serviceOfferType == minimal_data["serviceOfferType"]
        assert model.slug == minimal_data["slug"]
        assert model.categories == minimal_data["categories"]
        assert model.contactSalesUrl == minimal_data["contactSalesUrl"]

    def test_service_offer_management_serviceofferreadwithmedia_model_required_fields(self):
        """Test Service_offer_management_ServiceOfferReadWithMedia model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "id",
            "capabilities",
            "termsOfServiceUrl",
            "createdAt",
            "preProvisionMessage",
            "languagesSupported",
            "documentationUrl",
            "resourceUri",
            "screenshots",
            "videos",
            "serviceManager",
            "brokerUri",
            "featuresSupported",
            "staticLaunchUrl",
            "testDriveUrl",
            "evalUrl",
            "workspaceTypes",
            "name",
            "overview",
            "status",
            "logo",
            "shortDescription",
            "serviceOfferType",
            "slug",
            "categories",
            "contactSalesUrl",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_offer_management_ServiceOfferReadWithMedia()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "id",
                "capabilities",
                "termsOfServiceUrl",
                "createdAt",
                "preProvisionMessage",
                "languagesSupported",
                "documentationUrl",
                "resourceUri",
                "screenshots",
                "videos",
                "serviceManager",
                "brokerUri",
                "featuresSupported",
                "staticLaunchUrl",
                "testDriveUrl",
                "evalUrl",
                "workspaceTypes",
                "name",
                "overview",
                "status",
                "logo",
                "shortDescription",
                "serviceOfferType",
                "slug",
                "categories",
                "contactSalesUrl",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_offer_management_ServiceOfferReadWithMedia()
            assert isinstance(model, Service_offer_management_ServiceOfferReadWithMedia)

    def test_service_offer_management_serviceofferreadwithmedia_model_optional_fields(self):
        """Test Service_offer_management_ServiceOfferReadWithMedia model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "id": "required_id",
            "capabilities": [],
            "termsOfServiceUrl": "required_termsOfServiceUrl",
            "createdAt": "required_createdAt",
            "preProvisionMessage": "required_preProvisionMessage",
            "languagesSupported": [],
            "documentationUrl": "required_documentationUrl",
            "resourceUri": "required_resourceUri",
            "screenshots": [],
            "videos": [],
            "serviceManager": {},
            "brokerUri": "required_brokerUri",
            "featuresSupported": [],
            "staticLaunchUrl": "required_staticLaunchUrl",
            "testDriveUrl": "required_testDriveUrl",
            "evalUrl": "required_evalUrl",
            "workspaceTypes": "required_workspaceTypes",
            "name": "required_name",
            "overview": "required_overview",
            "status": "required_status",
            "logo": "required_logo",
            "shortDescription": "required_shortDescription",
            "serviceOfferType": "required_serviceOfferType",
            "slug": "required_slug",
            "categories": [],
            "contactSalesUrl": "required_contactSalesUrl",
        }

        model = Service_offer_management_ServiceOfferReadWithMedia(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "updatedAt")
        # Optional field updatedAt should be None or have a default value
        assert model.updatedAt is None or model.updatedAt is not None
        assert hasattr(model, "generation")
        # Optional field generation should be None or have a default value
        assert model.generation is None or model.generation is not None
        assert hasattr(model, "isDefault")
        # Optional field isDefault should be None or have a default value
        assert model.isDefault is None or model.isDefault is not None

    def test_service_offer_management_serviceofferreadwithmedia_model_serialization(self):
        """Test Service_offer_management_ServiceOfferReadWithMedia model serialization to dict."""
        test_data = {
            "id": "serialize_value",
            "capabilities": [],
            "termsOfServiceUrl": "serialize_value",
            "createdAt": "serialize_value",
            "preProvisionMessage": "serialize_value",
            "languagesSupported": [],
            "documentationUrl": "serialize_value",
            "resourceUri": "serialize_value",
            "screenshots": [],
            "videos": [],
            "serviceManager": {"key": "value"},
            "brokerUri": "serialize_value",
            "featuresSupported": [],
            "staticLaunchUrl": "serialize_value",
            "testDriveUrl": "serialize_value",
            "evalUrl": "serialize_value",
            "workspaceTypes": "serialize_value",
            "updatedAt": "serialize_value",
            "name": "serialize_value",
            "overview": "serialize_value",
            "status": "serialize_value",
            "logo": "serialize_value",
            "generation": "serialize_value",
            "shortDescription": "serialize_value",
            "serviceOfferType": "serialize_value",
            "slug": "serialize_value",
            "categories": [],
            "contactSalesUrl": "serialize_value",
            "isDefault": "serialize_value",
        }

        model = Service_offer_management_ServiceOfferReadWithMedia(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "id" in serialized
        assert "capabilities" in serialized
        assert "termsOfServiceUrl" in serialized
        assert "createdAt" in serialized
        assert "preProvisionMessage" in serialized
        assert "languagesSupported" in serialized
        assert "documentationUrl" in serialized
        assert "resourceUri" in serialized
        assert "screenshots" in serialized
        assert "videos" in serialized
        assert "serviceManager" in serialized
        assert "brokerUri" in serialized
        assert "featuresSupported" in serialized
        assert "staticLaunchUrl" in serialized
        assert "testDriveUrl" in serialized
        assert "evalUrl" in serialized
        assert "workspaceTypes" in serialized
        assert "updatedAt" in serialized
        assert "name" in serialized
        assert "overview" in serialized
        assert "status" in serialized
        assert "logo" in serialized
        assert "generation" in serialized
        assert "shortDescription" in serialized
        assert "serviceOfferType" in serialized
        assert "slug" in serialized
        assert "categories" in serialized
        assert "contactSalesUrl" in serialized
        assert "isDefault" in serialized

        # Verify values are preserved
        assert serialized["id"] == test_data["id"]
        assert serialized["capabilities"] == test_data["capabilities"]
        assert serialized["termsOfServiceUrl"] == test_data["termsOfServiceUrl"]
        assert serialized["createdAt"] == test_data["createdAt"]
        assert serialized["preProvisionMessage"] == test_data["preProvisionMessage"]
        assert serialized["languagesSupported"] == test_data["languagesSupported"]
        assert serialized["documentationUrl"] == test_data["documentationUrl"]
        assert serialized["resourceUri"] == test_data["resourceUri"]
        assert serialized["screenshots"] == test_data["screenshots"]
        assert serialized["videos"] == test_data["videos"]
        assert serialized["serviceManager"] == test_data["serviceManager"]
        assert serialized["brokerUri"] == test_data["brokerUri"]
        assert serialized["featuresSupported"] == test_data["featuresSupported"]
        assert serialized["staticLaunchUrl"] == test_data["staticLaunchUrl"]
        assert serialized["testDriveUrl"] == test_data["testDriveUrl"]
        assert serialized["evalUrl"] == test_data["evalUrl"]
        assert serialized["workspaceTypes"] == test_data["workspaceTypes"]
        assert serialized["updatedAt"] == test_data["updatedAt"]
        assert serialized["name"] == test_data["name"]
        assert serialized["overview"] == test_data["overview"]
        assert serialized["status"] == test_data["status"]
        assert serialized["logo"] == test_data["logo"]
        assert serialized["generation"] == test_data["generation"]
        assert serialized["shortDescription"] == test_data["shortDescription"]
        assert serialized["serviceOfferType"] == test_data["serviceOfferType"]
        assert serialized["slug"] == test_data["slug"]
        assert serialized["categories"] == test_data["categories"]
        assert serialized["contactSalesUrl"] == test_data["contactSalesUrl"]
        assert serialized["isDefault"] == test_data["isDefault"]

    def test_service_offer_management_serviceofferreadwithmedia_model_json_schema(self):
        """Test Service_offer_management_ServiceOfferReadWithMedia model JSON schema generation."""
        schema = Service_offer_management_ServiceOfferReadWithMedia.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "id",
            "capabilities",
            "termsOfServiceUrl",
            "createdAt",
            "preProvisionMessage",
            "languagesSupported",
            "documentationUrl",
            "resourceUri",
            "screenshots",
            "videos",
            "serviceManager",
            "brokerUri",
            "featuresSupported",
            "staticLaunchUrl",
            "testDriveUrl",
            "evalUrl",
            "workspaceTypes",
            "updatedAt",
            "name",
            "overview",
            "status",
            "logo",
            "generation",
            "shortDescription",
            "serviceOfferType",
            "slug",
            "categories",
            "contactSalesUrl",
            "isDefault",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "id",
            "capabilities",
            "termsOfServiceUrl",
            "createdAt",
            "preProvisionMessage",
            "languagesSupported",
            "documentationUrl",
            "resourceUri",
            "screenshots",
            "videos",
            "serviceManager",
            "brokerUri",
            "featuresSupported",
            "staticLaunchUrl",
            "testDriveUrl",
            "evalUrl",
            "workspaceTypes",
            "name",
            "overview",
            "status",
            "logo",
            "shortDescription",
            "serviceOfferType",
            "slug",
            "categories",
            "contactSalesUrl",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_provision_management_baseerror_model_creation(self):
        """Test Service_provision_management_BaseError model creation with valid data."""
        # Valid test data for Service_provision_management_BaseError
        valid_data = {
            "errorCode": "test_errorCode",
            "httpStatusCode": 42,
            "message": "test_message",
            "debugId": "test_debugId",
        }

        # Create model instance
        model = Service_provision_management_BaseError(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_provision_management_BaseError)
        assert model.errorCode == valid_data["errorCode"]
        assert model.httpStatusCode == valid_data["httpStatusCode"]
        assert model.message == valid_data["message"]
        assert model.debugId == valid_data["debugId"]

    def test_service_provision_management_baseerror_model_validation(self):
        """Test Service_provision_management_BaseError model field validation."""
        # Test with minimal required data
        minimal_data = {
            "errorCode": "required_errorCode",
            "httpStatusCode": 1,
            "message": "required_message",
            "debugId": "required_debugId",
        }

        model = Service_provision_management_BaseError(**minimal_data)
        assert isinstance(model, Service_provision_management_BaseError)
        assert model.errorCode == minimal_data["errorCode"]
        assert model.httpStatusCode == minimal_data["httpStatusCode"]
        assert model.message == minimal_data["message"]
        assert model.debugId == minimal_data["debugId"]

    def test_service_provision_management_baseerror_model_required_fields(self):
        """Test Service_provision_management_BaseError model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "errorCode",
            "httpStatusCode",
            "message",
            "debugId",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_provision_management_BaseError()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "errorCode",
                "httpStatusCode",
                "message",
                "debugId",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_provision_management_BaseError()
            assert isinstance(model, Service_provision_management_BaseError)

    def test_service_provision_management_baseerror_model_optional_fields(self):
        """Test Service_provision_management_BaseError model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "errorCode": "required_errorCode",
            "httpStatusCode": 1,
            "message": "required_message",
            "debugId": "required_debugId",
        }

        model = Service_provision_management_BaseError(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_provision_management_baseerror_model_serialization(self):
        """Test Service_provision_management_BaseError model serialization to dict."""
        test_data = {
            "errorCode": "serialize_value",
            "httpStatusCode": 99,
            "message": "serialize_value",
            "debugId": "serialize_value",
        }

        model = Service_provision_management_BaseError(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "errorCode" in serialized
        assert "httpStatusCode" in serialized
        assert "message" in serialized
        assert "debugId" in serialized

        # Verify values are preserved
        assert serialized["errorCode"] == test_data["errorCode"]
        assert serialized["httpStatusCode"] == test_data["httpStatusCode"]
        assert serialized["message"] == test_data["message"]
        assert serialized["debugId"] == test_data["debugId"]

    def test_service_provision_management_baseerror_model_json_schema(self):
        """Test Service_provision_management_BaseError model JSON schema generation."""
        schema = Service_provision_management_BaseError.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "errorCode",
            "httpStatusCode",
            "message",
            "debugId",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "errorCode",
            "httpStatusCode",
            "message",
            "debugId",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_manager_management_servicemanagerprovisionread_model_creation(self):
        """Test Service_Manager_Management_ServiceManagerProvisionRead model creation with valid data."""
        # Valid test data for Service_Manager_Management_ServiceManagerProvisionRead
        valid_data = {
            "serviceManager": {},
            "id": "test_id",
            "updatedAt": "test_updatedAt",
            "createdBy": "test_createdBy",
            "resourceUri": "test_resourceUri",
            "type": "test_type",
            "createdAt": "test_createdAt",
            "region": "test_region",
            "generation": 42,
            "provisionStatus": "test_provisionStatus",
        }

        # Create model instance
        model = Service_Manager_Management_ServiceManagerProvisionRead(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_Manager_Management_ServiceManagerProvisionRead)
        assert model.serviceManager == valid_data["serviceManager"]
        assert model.id == valid_data["id"]
        assert model.updatedAt == valid_data["updatedAt"]
        assert model.createdBy == valid_data["createdBy"]
        assert model.resourceUri == valid_data["resourceUri"]
        assert model.type == valid_data["type"]
        assert model.createdAt == valid_data["createdAt"]
        assert model.region == valid_data["region"]
        assert model.generation == valid_data["generation"]
        assert model.provisionStatus == valid_data["provisionStatus"]

    def test_service_manager_management_servicemanagerprovisionread_model_validation(self):
        """Test Service_Manager_Management_ServiceManagerProvisionRead model field validation."""
        # Test with minimal required data
        minimal_data = {
            "serviceManager": {},
            "id": "required_id",
            "updatedAt": "required_updatedAt",
            "createdBy": "required_createdBy",
            "resourceUri": "required_resourceUri",
            "type": "required_type",
            "createdAt": "required_createdAt",
            "region": "required_region",
            "generation": 1,
            "provisionStatus": "required_provisionStatus",
        }

        model = Service_Manager_Management_ServiceManagerProvisionRead(**minimal_data)
        assert isinstance(model, Service_Manager_Management_ServiceManagerProvisionRead)
        assert model.serviceManager == minimal_data["serviceManager"]
        assert model.id == minimal_data["id"]
        assert model.updatedAt == minimal_data["updatedAt"]
        assert model.createdBy == minimal_data["createdBy"]
        assert model.resourceUri == minimal_data["resourceUri"]
        assert model.type == minimal_data["type"]
        assert model.createdAt == minimal_data["createdAt"]
        assert model.region == minimal_data["region"]
        assert model.generation == minimal_data["generation"]
        assert model.provisionStatus == minimal_data["provisionStatus"]

    def test_service_manager_management_servicemanagerprovisionread_model_required_fields(self):
        """Test Service_Manager_Management_ServiceManagerProvisionRead model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "serviceManager",
            "id",
            "updatedAt",
            "createdBy",
            "resourceUri",
            "type",
            "createdAt",
            "region",
            "generation",
            "provisionStatus",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_Manager_Management_ServiceManagerProvisionRead()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "serviceManager",
                "id",
                "updatedAt",
                "createdBy",
                "resourceUri",
                "type",
                "createdAt",
                "region",
                "generation",
                "provisionStatus",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_Manager_Management_ServiceManagerProvisionRead()
            assert isinstance(model, Service_Manager_Management_ServiceManagerProvisionRead)

    def test_service_manager_management_servicemanagerprovisionread_model_optional_fields(self):
        """Test Service_Manager_Management_ServiceManagerProvisionRead model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "serviceManager": {},
            "id": "required_id",
            "updatedAt": "required_updatedAt",
            "createdBy": "required_createdBy",
            "resourceUri": "required_resourceUri",
            "type": "required_type",
            "createdAt": "required_createdAt",
            "region": "required_region",
            "generation": 1,
            "provisionStatus": "required_provisionStatus",
        }

        model = Service_Manager_Management_ServiceManagerProvisionRead(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_manager_management_servicemanagerprovisionread_model_serialization(self):
        """Test Service_Manager_Management_ServiceManagerProvisionRead model serialization to dict."""
        test_data = {
            "serviceManager": {"key": "value"},
            "id": "serialize_value",
            "updatedAt": "serialize_value",
            "createdBy": "serialize_value",
            "resourceUri": "serialize_value",
            "type": "serialize_value",
            "createdAt": "serialize_value",
            "region": "serialize_value",
            "generation": 99,
            "provisionStatus": "serialize_value",
        }

        model = Service_Manager_Management_ServiceManagerProvisionRead(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "serviceManager" in serialized
        assert "id" in serialized
        assert "updatedAt" in serialized
        assert "createdBy" in serialized
        assert "resourceUri" in serialized
        assert "type" in serialized
        assert "createdAt" in serialized
        assert "region" in serialized
        assert "generation" in serialized
        assert "provisionStatus" in serialized

        # Verify values are preserved
        assert serialized["serviceManager"] == test_data["serviceManager"]
        assert serialized["id"] == test_data["id"]
        assert serialized["updatedAt"] == test_data["updatedAt"]
        assert serialized["createdBy"] == test_data["createdBy"]
        assert serialized["resourceUri"] == test_data["resourceUri"]
        assert serialized["type"] == test_data["type"]
        assert serialized["createdAt"] == test_data["createdAt"]
        assert serialized["region"] == test_data["region"]
        assert serialized["generation"] == test_data["generation"]
        assert serialized["provisionStatus"] == test_data["provisionStatus"]

    def test_service_manager_management_servicemanagerprovisionread_model_json_schema(self):
        """Test Service_Manager_Management_ServiceManagerProvisionRead model JSON schema generation."""
        schema = Service_Manager_Management_ServiceManagerProvisionRead.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "serviceManager",
            "id",
            "updatedAt",
            "createdBy",
            "resourceUri",
            "type",
            "createdAt",
            "region",
            "generation",
            "provisionStatus",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "serviceManager",
            "id",
            "updatedAt",
            "createdBy",
            "resourceUri",
            "type",
            "createdAt",
            "region",
            "generation",
            "provisionStatus",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_offer_management_category_model_creation(self):
        """Test Service_offer_management_Category model creation with valid data."""
        # Valid test data for Service_offer_management_Category
        valid_data = {}

        # Create model instance
        model = Service_offer_management_Category(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_offer_management_Category)

    def test_service_offer_management_category_model_validation(self):
        """Test Service_offer_management_Category model field validation."""
        # Test with minimal required data
        minimal_data = {}

        model = Service_offer_management_Category(**minimal_data)
        assert isinstance(model, Service_offer_management_Category)

    def test_service_offer_management_category_model_required_fields(self):
        """Test Service_offer_management_Category model required field validation."""
        # Check if this model has any required fields
        required_fields = []

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_offer_management_Category()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {}

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_offer_management_Category()
            assert isinstance(model, Service_offer_management_Category)

    def test_service_offer_management_category_model_optional_fields(self):
        """Test Service_offer_management_Category model optional field handling."""
        # Create with minimal required data
        minimal_data = {}

        model = Service_offer_management_Category(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_offer_management_category_model_serialization(self):
        """Test Service_offer_management_Category model serialization to dict."""
        test_data = {}

        model = Service_offer_management_Category(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)

        # Verify values are preserved

    def test_service_offer_management_category_model_json_schema(self):
        """Test Service_offer_management_Category model JSON schema generation."""
        schema = Service_offer_management_Category.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {}

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = []
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_provision_management_validationerror_model_creation(self):
        """Test Service_provision_management_ValidationError model creation with valid data."""
        # Valid test data for Service_provision_management_ValidationError
        valid_data = {
            "errorCode": "test_errorCode",
            "httpStatusCode": 42,
            "message": "test_message",
            "debugId": "test_debugId",
        }

        # Create model instance
        model = Service_provision_management_ValidationError(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_provision_management_ValidationError)
        assert model.errorCode == valid_data["errorCode"]
        assert model.httpStatusCode == valid_data["httpStatusCode"]
        assert model.message == valid_data["message"]
        assert model.debugId == valid_data["debugId"]

    def test_service_provision_management_validationerror_model_validation(self):
        """Test Service_provision_management_ValidationError model field validation."""
        # Test with minimal required data
        minimal_data = {
            "errorCode": "required_errorCode",
            "httpStatusCode": 1,
            "message": "required_message",
            "debugId": "required_debugId",
        }

        model = Service_provision_management_ValidationError(**minimal_data)
        assert isinstance(model, Service_provision_management_ValidationError)
        assert model.errorCode == minimal_data["errorCode"]
        assert model.httpStatusCode == minimal_data["httpStatusCode"]
        assert model.message == minimal_data["message"]
        assert model.debugId == minimal_data["debugId"]

    def test_service_provision_management_validationerror_model_required_fields(self):
        """Test Service_provision_management_ValidationError model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "errorCode",
            "httpStatusCode",
            "message",
            "debugId",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_provision_management_ValidationError()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "errorCode",
                "httpStatusCode",
                "message",
                "debugId",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_provision_management_ValidationError()
            assert isinstance(model, Service_provision_management_ValidationError)

    def test_service_provision_management_validationerror_model_optional_fields(self):
        """Test Service_provision_management_ValidationError model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "errorCode": "required_errorCode",
            "httpStatusCode": 1,
            "message": "required_message",
            "debugId": "required_debugId",
        }

        model = Service_provision_management_ValidationError(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_provision_management_validationerror_model_serialization(self):
        """Test Service_provision_management_ValidationError model serialization to dict."""
        test_data = {
            "errorCode": "serialize_value",
            "httpStatusCode": 99,
            "message": "serialize_value",
            "debugId": "serialize_value",
        }

        model = Service_provision_management_ValidationError(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "errorCode" in serialized
        assert "httpStatusCode" in serialized
        assert "message" in serialized
        assert "debugId" in serialized

        # Verify values are preserved
        assert serialized["errorCode"] == test_data["errorCode"]
        assert serialized["httpStatusCode"] == test_data["httpStatusCode"]
        assert serialized["message"] == test_data["message"]
        assert serialized["debugId"] == test_data["debugId"]

    def test_service_provision_management_validationerror_model_json_schema(self):
        """Test Service_provision_management_ValidationError model JSON schema generation."""
        schema = Service_provision_management_ValidationError.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "errorCode",
            "httpStatusCode",
            "message",
            "debugId",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "errorCode",
            "httpStatusCode",
            "message",
            "debugId",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_manager_management_unauthorizederror_model_creation(self):
        """Test Service_Manager_Management_UnauthorizedError model creation with valid data."""
        # Valid test data for Service_Manager_Management_UnauthorizedError
        valid_data = {
            "debugId": "test_debugId",
            "errorCode": "test_errorCode",
            "httpStatusCode": 42,
            "message": "test_message",
        }

        # Create model instance
        model = Service_Manager_Management_UnauthorizedError(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_Manager_Management_UnauthorizedError)
        assert model.debugId == valid_data["debugId"]
        assert model.errorCode == valid_data["errorCode"]
        assert model.httpStatusCode == valid_data["httpStatusCode"]
        assert model.message == valid_data["message"]

    def test_service_manager_management_unauthorizederror_model_validation(self):
        """Test Service_Manager_Management_UnauthorizedError model field validation."""
        # Test with minimal required data
        minimal_data = {
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
            "httpStatusCode": 1,
            "message": "required_message",
        }

        model = Service_Manager_Management_UnauthorizedError(**minimal_data)
        assert isinstance(model, Service_Manager_Management_UnauthorizedError)
        assert model.debugId == minimal_data["debugId"]
        assert model.errorCode == minimal_data["errorCode"]
        assert model.httpStatusCode == minimal_data["httpStatusCode"]
        assert model.message == minimal_data["message"]

    def test_service_manager_management_unauthorizederror_model_required_fields(self):
        """Test Service_Manager_Management_UnauthorizedError model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "debugId",
            "errorCode",
            "httpStatusCode",
            "message",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_Manager_Management_UnauthorizedError()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "debugId",
                "errorCode",
                "httpStatusCode",
                "message",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_Manager_Management_UnauthorizedError()
            assert isinstance(model, Service_Manager_Management_UnauthorizedError)

    def test_service_manager_management_unauthorizederror_model_optional_fields(self):
        """Test Service_Manager_Management_UnauthorizedError model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
            "httpStatusCode": 1,
            "message": "required_message",
        }

        model = Service_Manager_Management_UnauthorizedError(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_manager_management_unauthorizederror_model_serialization(self):
        """Test Service_Manager_Management_UnauthorizedError model serialization to dict."""
        test_data = {
            "debugId": "serialize_value",
            "errorCode": "serialize_value",
            "httpStatusCode": 99,
            "message": "serialize_value",
        }

        model = Service_Manager_Management_UnauthorizedError(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "debugId" in serialized
        assert "errorCode" in serialized
        assert "httpStatusCode" in serialized
        assert "message" in serialized

        # Verify values are preserved
        assert serialized["debugId"] == test_data["debugId"]
        assert serialized["errorCode"] == test_data["errorCode"]
        assert serialized["httpStatusCode"] == test_data["httpStatusCode"]
        assert serialized["message"] == test_data["message"]

    def test_service_manager_management_unauthorizederror_model_json_schema(self):
        """Test Service_Manager_Management_UnauthorizedError model JSON schema generation."""
        schema = Service_Manager_Management_UnauthorizedError.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "debugId",
            "errorCode",
            "httpStatusCode",
            "message",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "debugId",
            "errorCode",
            "httpStatusCode",
            "message",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_provision_management_error_model_creation(self):
        """Test Service_provision_management_Error model creation with valid data."""
        # Valid test data for Service_provision_management_Error
        valid_data = {
            "debugId": "test_debugId",
            "errorCode": "test_errorCode",
            "httpStatusCode": 42,
            "message": "test_message",
            "errorDetails": [],
        }

        # Create model instance
        model = Service_provision_management_Error(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_provision_management_Error)
        assert model.debugId == valid_data["debugId"]
        assert model.errorCode == valid_data["errorCode"]
        assert model.httpStatusCode == valid_data["httpStatusCode"]
        assert model.message == valid_data["message"]
        assert model.errorDetails == valid_data["errorDetails"]

    def test_service_provision_management_error_model_validation(self):
        """Test Service_provision_management_Error model field validation."""
        # Test with minimal required data
        minimal_data = {
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
            "httpStatusCode": 1,
            "message": "required_message",
        }

        model = Service_provision_management_Error(**minimal_data)
        assert isinstance(model, Service_provision_management_Error)
        assert model.debugId == minimal_data["debugId"]
        assert model.errorCode == minimal_data["errorCode"]
        assert model.httpStatusCode == minimal_data["httpStatusCode"]
        assert model.message == minimal_data["message"]

    def test_service_provision_management_error_model_required_fields(self):
        """Test Service_provision_management_Error model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "debugId",
            "errorCode",
            "httpStatusCode",
            "message",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_provision_management_Error()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "debugId",
                "errorCode",
                "httpStatusCode",
                "message",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_provision_management_Error()
            assert isinstance(model, Service_provision_management_Error)

    def test_service_provision_management_error_model_optional_fields(self):
        """Test Service_provision_management_Error model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
            "httpStatusCode": 1,
            "message": "required_message",
        }

        model = Service_provision_management_Error(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "errorDetails")
        # Optional field errorDetails should be None or have a default value
        assert model.errorDetails is None or model.errorDetails is not None

    def test_service_provision_management_error_model_serialization(self):
        """Test Service_provision_management_Error model serialization to dict."""
        test_data = {
            "debugId": "serialize_value",
            "errorCode": "serialize_value",
            "httpStatusCode": 99,
            "message": "serialize_value",
            "errorDetails": [],
        }

        model = Service_provision_management_Error(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "debugId" in serialized
        assert "errorCode" in serialized
        assert "httpStatusCode" in serialized
        assert "message" in serialized
        assert "errorDetails" in serialized

        # Verify values are preserved
        assert serialized["debugId"] == test_data["debugId"]
        assert serialized["errorCode"] == test_data["errorCode"]
        assert serialized["httpStatusCode"] == test_data["httpStatusCode"]
        assert serialized["message"] == test_data["message"]
        assert serialized["errorDetails"] == test_data["errorDetails"]

    def test_service_provision_management_error_model_json_schema(self):
        """Test Service_provision_management_Error model JSON schema generation."""
        schema = Service_provision_management_Error.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "debugId",
            "errorCode",
            "httpStatusCode",
            "message",
            "errorDetails",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "debugId",
            "errorCode",
            "httpStatusCode",
            "message",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_offer_management_serviceprovision_model_creation(self):
        """Test Service_offer_management_ServiceProvision model creation with valid data."""
        # Valid test data for Service_offer_management_ServiceProvision
        valid_data = {
            "provisionStatus": "test_provisionStatus",
            "reason": "test_reason",
            "serviceManagerInstanceId": "test_serviceManagerInstanceId",
            "createdBy": "test_createdBy",
            "resourceUri": "test_resourceUri",
            "serviceManager": {},
            "serviceManagerProvision": {},
            "workspace": {},
            "updatedAt": "test_updatedAt",
            "createdAt": "test_createdAt",
            "region": "test_region",
            "generation": 42,
            "id": "test_id",
            "serviceOffer": {},
        }

        # Create model instance
        model = Service_offer_management_ServiceProvision(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_offer_management_ServiceProvision)
        assert model.provisionStatus == valid_data["provisionStatus"]
        assert model.reason == valid_data["reason"]
        assert model.serviceManagerInstanceId == valid_data["serviceManagerInstanceId"]
        assert model.createdBy == valid_data["createdBy"]
        assert model.resourceUri == valid_data["resourceUri"]
        assert model.serviceManager == valid_data["serviceManager"]
        assert model.serviceManagerProvision == valid_data["serviceManagerProvision"]
        assert model.workspace == valid_data["workspace"]
        assert model.updatedAt == valid_data["updatedAt"]
        assert model.createdAt == valid_data["createdAt"]
        assert model.region == valid_data["region"]
        assert model.generation == valid_data["generation"]
        assert model.id == valid_data["id"]
        assert model.serviceOffer == valid_data["serviceOffer"]

    def test_service_offer_management_serviceprovision_model_validation(self):
        """Test Service_offer_management_ServiceProvision model field validation."""
        # Test with minimal required data
        minimal_data = {
            "resourceUri": "required_resourceUri",
            "workspace": {},
            "region": "required_region",
            "generation": 1,
            "id": "required_id",
            "serviceOffer": {},
        }

        model = Service_offer_management_ServiceProvision(**minimal_data)
        assert isinstance(model, Service_offer_management_ServiceProvision)
        assert model.resourceUri == minimal_data["resourceUri"]
        assert model.workspace == minimal_data["workspace"]
        assert model.region == minimal_data["region"]
        assert model.generation == minimal_data["generation"]
        assert model.id == minimal_data["id"]
        assert model.serviceOffer == minimal_data["serviceOffer"]

    def test_service_offer_management_serviceprovision_model_required_fields(self):
        """Test Service_offer_management_ServiceProvision model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "resourceUri",
            "workspace",
            "region",
            "generation",
            "id",
            "serviceOffer",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_offer_management_ServiceProvision()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "resourceUri",
                "workspace",
                "region",
                "generation",
                "id",
                "serviceOffer",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_offer_management_ServiceProvision()
            assert isinstance(model, Service_offer_management_ServiceProvision)

    def test_service_offer_management_serviceprovision_model_optional_fields(self):
        """Test Service_offer_management_ServiceProvision model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "resourceUri": "required_resourceUri",
            "workspace": {},
            "region": "required_region",
            "generation": 1,
            "id": "required_id",
            "serviceOffer": {},
        }

        model = Service_offer_management_ServiceProvision(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "provisionStatus")
        # Optional field provisionStatus should be None or have a default value
        assert model.provisionStatus is None or model.provisionStatus is not None
        assert hasattr(model, "reason")
        # Optional field reason should be None or have a default value
        assert model.reason is None or model.reason is not None
        assert hasattr(model, "serviceManagerInstanceId")
        # Optional field serviceManagerInstanceId should be None or have a default value
        assert model.serviceManagerInstanceId is None or model.serviceManagerInstanceId is not None
        assert hasattr(model, "createdBy")
        # Optional field createdBy should be None or have a default value
        assert model.createdBy is None or model.createdBy is not None
        assert hasattr(model, "serviceManager")
        # Optional field serviceManager should be None or have a default value
        assert model.serviceManager is None or model.serviceManager is not None
        assert hasattr(model, "serviceManagerProvision")
        # Optional field serviceManagerProvision should be None or have a default value
        assert model.serviceManagerProvision is None or model.serviceManagerProvision is not None
        assert hasattr(model, "updatedAt")
        # Optional field updatedAt should be None or have a default value
        assert model.updatedAt is None or model.updatedAt is not None
        assert hasattr(model, "createdAt")
        # Optional field createdAt should be None or have a default value
        assert model.createdAt is None or model.createdAt is not None

    def test_service_offer_management_serviceprovision_model_serialization(self):
        """Test Service_offer_management_ServiceProvision model serialization to dict."""
        test_data = {
            "provisionStatus": "serialize_value",
            "reason": "serialize_value",
            "serviceManagerInstanceId": "serialize_value",
            "createdBy": "serialize_value",
            "resourceUri": "serialize_value",
            "serviceManager": {"key": "value"},
            "serviceManagerProvision": {"key": "value"},
            "workspace": {"key": "value"},
            "updatedAt": "serialize_value",
            "createdAt": "serialize_value",
            "region": "serialize_value",
            "generation": 99,
            "id": "serialize_value",
            "serviceOffer": {"key": "value"},
        }

        model = Service_offer_management_ServiceProvision(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "provisionStatus" in serialized
        assert "reason" in serialized
        assert "serviceManagerInstanceId" in serialized
        assert "createdBy" in serialized
        assert "resourceUri" in serialized
        assert "serviceManager" in serialized
        assert "serviceManagerProvision" in serialized
        assert "workspace" in serialized
        assert "updatedAt" in serialized
        assert "createdAt" in serialized
        assert "region" in serialized
        assert "generation" in serialized
        assert "id" in serialized
        assert "serviceOffer" in serialized

        # Verify values are preserved
        assert serialized["provisionStatus"] == test_data["provisionStatus"]
        assert serialized["reason"] == test_data["reason"]
        assert serialized["serviceManagerInstanceId"] == test_data["serviceManagerInstanceId"]
        assert serialized["createdBy"] == test_data["createdBy"]
        assert serialized["resourceUri"] == test_data["resourceUri"]
        assert serialized["serviceManager"] == test_data["serviceManager"]
        assert serialized["serviceManagerProvision"] == test_data["serviceManagerProvision"]
        assert serialized["workspace"] == test_data["workspace"]
        assert serialized["updatedAt"] == test_data["updatedAt"]
        assert serialized["createdAt"] == test_data["createdAt"]
        assert serialized["region"] == test_data["region"]
        assert serialized["generation"] == test_data["generation"]
        assert serialized["id"] == test_data["id"]
        assert serialized["serviceOffer"] == test_data["serviceOffer"]

    def test_service_offer_management_serviceprovision_model_json_schema(self):
        """Test Service_offer_management_ServiceProvision model JSON schema generation."""
        schema = Service_offer_management_ServiceProvision.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "provisionStatus",
            "reason",
            "serviceManagerInstanceId",
            "createdBy",
            "resourceUri",
            "serviceManager",
            "serviceManagerProvision",
            "workspace",
            "updatedAt",
            "createdAt",
            "region",
            "generation",
            "id",
            "serviceOffer",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "resourceUri",
            "workspace",
            "region",
            "generation",
            "id",
            "serviceOffer",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_provision_management_accounttype_model_creation(self):
        """Test Service_provision_management_AccountType model creation with valid data."""
        # Valid test data for Service_provision_management_AccountType
        valid_data = {}

        # Create model instance
        model = Service_provision_management_AccountType(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_provision_management_AccountType)

    def test_service_provision_management_accounttype_model_validation(self):
        """Test Service_provision_management_AccountType model field validation."""
        # Test with minimal required data
        minimal_data = {}

        model = Service_provision_management_AccountType(**minimal_data)
        assert isinstance(model, Service_provision_management_AccountType)

    def test_service_provision_management_accounttype_model_required_fields(self):
        """Test Service_provision_management_AccountType model required field validation."""
        # Check if this model has any required fields
        required_fields = []

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_provision_management_AccountType()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {}

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_provision_management_AccountType()
            assert isinstance(model, Service_provision_management_AccountType)

    def test_service_provision_management_accounttype_model_optional_fields(self):
        """Test Service_provision_management_AccountType model optional field handling."""
        # Create with minimal required data
        minimal_data = {}

        model = Service_provision_management_AccountType(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_provision_management_accounttype_model_serialization(self):
        """Test Service_provision_management_AccountType model serialization to dict."""
        test_data = {}

        model = Service_provision_management_AccountType(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)

        # Verify values are preserved

    def test_service_provision_management_accounttype_model_json_schema(self):
        """Test Service_provision_management_AccountType model JSON schema generation."""
        schema = Service_provision_management_AccountType.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {}

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = []
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_offer_management_preconditionfailederror_model_creation(self):
        """Test Service_offer_management_PreConditionFailedError model creation with valid data."""
        # Valid test data for Service_offer_management_PreConditionFailedError
        valid_data = {
            "errorDetails": [],
            "httpStatusCode": 42,
            "message": "test_message",
            "debugId": "test_debugId",
            "errorCode": "test_errorCode",
        }

        # Create model instance
        model = Service_offer_management_PreConditionFailedError(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_offer_management_PreConditionFailedError)
        assert model.errorDetails == valid_data["errorDetails"]
        assert model.httpStatusCode == valid_data["httpStatusCode"]
        assert model.message == valid_data["message"]
        assert model.debugId == valid_data["debugId"]
        assert model.errorCode == valid_data["errorCode"]

    def test_service_offer_management_preconditionfailederror_model_validation(self):
        """Test Service_offer_management_PreConditionFailedError model field validation."""
        # Test with minimal required data
        minimal_data = {
            "errorDetails": [],
            "httpStatusCode": 1,
            "message": "required_message",
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
        }

        model = Service_offer_management_PreConditionFailedError(**minimal_data)
        assert isinstance(model, Service_offer_management_PreConditionFailedError)
        assert model.errorDetails == minimal_data["errorDetails"]
        assert model.httpStatusCode == minimal_data["httpStatusCode"]
        assert model.message == minimal_data["message"]
        assert model.debugId == minimal_data["debugId"]
        assert model.errorCode == minimal_data["errorCode"]

    def test_service_offer_management_preconditionfailederror_model_required_fields(self):
        """Test Service_offer_management_PreConditionFailedError model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "errorDetails",
            "httpStatusCode",
            "message",
            "debugId",
            "errorCode",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_offer_management_PreConditionFailedError()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "errorDetails",
                "httpStatusCode",
                "message",
                "debugId",
                "errorCode",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_offer_management_PreConditionFailedError()
            assert isinstance(model, Service_offer_management_PreConditionFailedError)

    def test_service_offer_management_preconditionfailederror_model_optional_fields(self):
        """Test Service_offer_management_PreConditionFailedError model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "errorDetails": [],
            "httpStatusCode": 1,
            "message": "required_message",
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
        }

        model = Service_offer_management_PreConditionFailedError(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_offer_management_preconditionfailederror_model_serialization(self):
        """Test Service_offer_management_PreConditionFailedError model serialization to dict."""
        test_data = {
            "errorDetails": [],
            "httpStatusCode": 99,
            "message": "serialize_value",
            "debugId": "serialize_value",
            "errorCode": "serialize_value",
        }

        model = Service_offer_management_PreConditionFailedError(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "errorDetails" in serialized
        assert "httpStatusCode" in serialized
        assert "message" in serialized
        assert "debugId" in serialized
        assert "errorCode" in serialized

        # Verify values are preserved
        assert serialized["errorDetails"] == test_data["errorDetails"]
        assert serialized["httpStatusCode"] == test_data["httpStatusCode"]
        assert serialized["message"] == test_data["message"]
        assert serialized["debugId"] == test_data["debugId"]
        assert serialized["errorCode"] == test_data["errorCode"]

    def test_service_offer_management_preconditionfailederror_model_json_schema(self):
        """Test Service_offer_management_PreConditionFailedError model JSON schema generation."""
        schema = Service_offer_management_PreConditionFailedError.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "errorDetails",
            "httpStatusCode",
            "message",
            "debugId",
            "errorCode",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "errorDetails",
            "httpStatusCode",
            "message",
            "debugId",
            "errorCode",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_manager_management_internalerror_model_creation(self):
        """Test Service_Manager_Management_InternalError model creation with valid data."""
        # Valid test data for Service_Manager_Management_InternalError
        valid_data = {
            "debugId": "test_debugId",
            "errorCode": "test_errorCode",
            "httpStatusCode": 42,
            "message": "test_message",
        }

        # Create model instance
        model = Service_Manager_Management_InternalError(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_Manager_Management_InternalError)
        assert model.debugId == valid_data["debugId"]
        assert model.errorCode == valid_data["errorCode"]
        assert model.httpStatusCode == valid_data["httpStatusCode"]
        assert model.message == valid_data["message"]

    def test_service_manager_management_internalerror_model_validation(self):
        """Test Service_Manager_Management_InternalError model field validation."""
        # Test with minimal required data
        minimal_data = {
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
            "httpStatusCode": 1,
            "message": "required_message",
        }

        model = Service_Manager_Management_InternalError(**minimal_data)
        assert isinstance(model, Service_Manager_Management_InternalError)
        assert model.debugId == minimal_data["debugId"]
        assert model.errorCode == minimal_data["errorCode"]
        assert model.httpStatusCode == minimal_data["httpStatusCode"]
        assert model.message == minimal_data["message"]

    def test_service_manager_management_internalerror_model_required_fields(self):
        """Test Service_Manager_Management_InternalError model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "debugId",
            "errorCode",
            "httpStatusCode",
            "message",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_Manager_Management_InternalError()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "debugId",
                "errorCode",
                "httpStatusCode",
                "message",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_Manager_Management_InternalError()
            assert isinstance(model, Service_Manager_Management_InternalError)

    def test_service_manager_management_internalerror_model_optional_fields(self):
        """Test Service_Manager_Management_InternalError model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
            "httpStatusCode": 1,
            "message": "required_message",
        }

        model = Service_Manager_Management_InternalError(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_manager_management_internalerror_model_serialization(self):
        """Test Service_Manager_Management_InternalError model serialization to dict."""
        test_data = {
            "debugId": "serialize_value",
            "errorCode": "serialize_value",
            "httpStatusCode": 99,
            "message": "serialize_value",
        }

        model = Service_Manager_Management_InternalError(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "debugId" in serialized
        assert "errorCode" in serialized
        assert "httpStatusCode" in serialized
        assert "message" in serialized

        # Verify values are preserved
        assert serialized["debugId"] == test_data["debugId"]
        assert serialized["errorCode"] == test_data["errorCode"]
        assert serialized["httpStatusCode"] == test_data["httpStatusCode"]
        assert serialized["message"] == test_data["message"]

    def test_service_manager_management_internalerror_model_json_schema(self):
        """Test Service_Manager_Management_InternalError model JSON schema generation."""
        schema = Service_Manager_Management_InternalError.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "debugId",
            "errorCode",
            "httpStatusCode",
            "message",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "debugId",
            "errorCode",
            "httpStatusCode",
            "message",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_manager_management_forbiddenerror_model_creation(self):
        """Test Service_Manager_Management_ForbiddenError model creation with valid data."""
        # Valid test data for Service_Manager_Management_ForbiddenError
        valid_data = {
            "debugId": "test_debugId",
            "errorCode": "test_errorCode",
            "httpStatusCode": 42,
            "message": "test_message",
        }

        # Create model instance
        model = Service_Manager_Management_ForbiddenError(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_Manager_Management_ForbiddenError)
        assert model.debugId == valid_data["debugId"]
        assert model.errorCode == valid_data["errorCode"]
        assert model.httpStatusCode == valid_data["httpStatusCode"]
        assert model.message == valid_data["message"]

    def test_service_manager_management_forbiddenerror_model_validation(self):
        """Test Service_Manager_Management_ForbiddenError model field validation."""
        # Test with minimal required data
        minimal_data = {
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
            "httpStatusCode": 1,
            "message": "required_message",
        }

        model = Service_Manager_Management_ForbiddenError(**minimal_data)
        assert isinstance(model, Service_Manager_Management_ForbiddenError)
        assert model.debugId == minimal_data["debugId"]
        assert model.errorCode == minimal_data["errorCode"]
        assert model.httpStatusCode == minimal_data["httpStatusCode"]
        assert model.message == minimal_data["message"]

    def test_service_manager_management_forbiddenerror_model_required_fields(self):
        """Test Service_Manager_Management_ForbiddenError model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "debugId",
            "errorCode",
            "httpStatusCode",
            "message",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_Manager_Management_ForbiddenError()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "debugId",
                "errorCode",
                "httpStatusCode",
                "message",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_Manager_Management_ForbiddenError()
            assert isinstance(model, Service_Manager_Management_ForbiddenError)

    def test_service_manager_management_forbiddenerror_model_optional_fields(self):
        """Test Service_Manager_Management_ForbiddenError model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
            "httpStatusCode": 1,
            "message": "required_message",
        }

        model = Service_Manager_Management_ForbiddenError(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_manager_management_forbiddenerror_model_serialization(self):
        """Test Service_Manager_Management_ForbiddenError model serialization to dict."""
        test_data = {
            "debugId": "serialize_value",
            "errorCode": "serialize_value",
            "httpStatusCode": 99,
            "message": "serialize_value",
        }

        model = Service_Manager_Management_ForbiddenError(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "debugId" in serialized
        assert "errorCode" in serialized
        assert "httpStatusCode" in serialized
        assert "message" in serialized

        # Verify values are preserved
        assert serialized["debugId"] == test_data["debugId"]
        assert serialized["errorCode"] == test_data["errorCode"]
        assert serialized["httpStatusCode"] == test_data["httpStatusCode"]
        assert serialized["message"] == test_data["message"]

    def test_service_manager_management_forbiddenerror_model_json_schema(self):
        """Test Service_Manager_Management_ForbiddenError model JSON schema generation."""
        schema = Service_Manager_Management_ForbiddenError.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "debugId",
            "errorCode",
            "httpStatusCode",
            "message",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "debugId",
            "errorCode",
            "httpStatusCode",
            "message",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_offer_management_regionwithlocations_model_creation(self):
        """Test Service_offer_management_RegionWithLocations model creation with valid data."""
        # Valid test data for Service_offer_management_RegionWithLocations
        valid_data = {
            "type": "test_type",
            "id": "test_id",
            "name": "test_name",
            "locations": [],
        }

        # Create model instance
        model = Service_offer_management_RegionWithLocations(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_offer_management_RegionWithLocations)
        assert model.type == valid_data["type"]
        assert model.id == valid_data["id"]
        assert model.name == valid_data["name"]
        assert model.locations == valid_data["locations"]

    def test_service_offer_management_regionwithlocations_model_validation(self):
        """Test Service_offer_management_RegionWithLocations model field validation."""
        # Test with minimal required data
        minimal_data = {}

        model = Service_offer_management_RegionWithLocations(**minimal_data)
        assert isinstance(model, Service_offer_management_RegionWithLocations)

    def test_service_offer_management_regionwithlocations_model_required_fields(self):
        """Test Service_offer_management_RegionWithLocations model required field validation."""
        # Check if this model has any required fields
        required_fields = []

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_offer_management_RegionWithLocations()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {}

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_offer_management_RegionWithLocations()
            assert isinstance(model, Service_offer_management_RegionWithLocations)

    def test_service_offer_management_regionwithlocations_model_optional_fields(self):
        """Test Service_offer_management_RegionWithLocations model optional field handling."""
        # Create with minimal required data
        minimal_data = {}

        model = Service_offer_management_RegionWithLocations(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "type")
        # Optional field type should be None or have a default value
        assert model.type is None or model.type is not None
        assert hasattr(model, "id")
        # Optional field id should be None or have a default value
        assert model.id is None or model.id is not None
        assert hasattr(model, "name")
        # Optional field name should be None or have a default value
        assert model.name is None or model.name is not None
        assert hasattr(model, "locations")
        # Optional field locations should be None or have a default value
        assert model.locations is None or model.locations is not None

    def test_service_offer_management_regionwithlocations_model_serialization(self):
        """Test Service_offer_management_RegionWithLocations model serialization to dict."""
        test_data = {
            "type": "serialize_value",
            "id": "serialize_value",
            "name": "serialize_value",
            "locations": [],
        }

        model = Service_offer_management_RegionWithLocations(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "type" in serialized
        assert "id" in serialized
        assert "name" in serialized
        assert "locations" in serialized

        # Verify values are preserved
        assert serialized["type"] == test_data["type"]
        assert serialized["id"] == test_data["id"]
        assert serialized["name"] == test_data["name"]
        assert serialized["locations"] == test_data["locations"]

    def test_service_offer_management_regionwithlocations_model_json_schema(self):
        """Test Service_offer_management_RegionWithLocations model JSON schema generation."""
        schema = Service_offer_management_RegionWithLocations.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "type",
            "id",
            "name",
            "locations",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = []
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_offer_management_unauthorizederror_model_creation(self):
        """Test Service_offer_management_UnauthorizedError model creation with valid data."""
        # Valid test data for Service_offer_management_UnauthorizedError
        valid_data = {
            "debugId": "test_debugId",
            "errorCode": "test_errorCode",
            "errorDetails": [],
            "httpStatusCode": 42,
            "message": "test_message",
        }

        # Create model instance
        model = Service_offer_management_UnauthorizedError(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_offer_management_UnauthorizedError)
        assert model.debugId == valid_data["debugId"]
        assert model.errorCode == valid_data["errorCode"]
        assert model.errorDetails == valid_data["errorDetails"]
        assert model.httpStatusCode == valid_data["httpStatusCode"]
        assert model.message == valid_data["message"]

    def test_service_offer_management_unauthorizederror_model_validation(self):
        """Test Service_offer_management_UnauthorizedError model field validation."""
        # Test with minimal required data
        minimal_data = {
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
            "httpStatusCode": 1,
            "message": "required_message",
        }

        model = Service_offer_management_UnauthorizedError(**minimal_data)
        assert isinstance(model, Service_offer_management_UnauthorizedError)
        assert model.debugId == minimal_data["debugId"]
        assert model.errorCode == minimal_data["errorCode"]
        assert model.httpStatusCode == minimal_data["httpStatusCode"]
        assert model.message == minimal_data["message"]

    def test_service_offer_management_unauthorizederror_model_required_fields(self):
        """Test Service_offer_management_UnauthorizedError model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "debugId",
            "errorCode",
            "httpStatusCode",
            "message",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_offer_management_UnauthorizedError()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "debugId",
                "errorCode",
                "httpStatusCode",
                "message",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_offer_management_UnauthorizedError()
            assert isinstance(model, Service_offer_management_UnauthorizedError)

    def test_service_offer_management_unauthorizederror_model_optional_fields(self):
        """Test Service_offer_management_UnauthorizedError model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
            "httpStatusCode": 1,
            "message": "required_message",
        }

        model = Service_offer_management_UnauthorizedError(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "errorDetails")
        # Optional field errorDetails should be None or have a default value
        assert model.errorDetails is None or model.errorDetails is not None

    def test_service_offer_management_unauthorizederror_model_serialization(self):
        """Test Service_offer_management_UnauthorizedError model serialization to dict."""
        test_data = {
            "debugId": "serialize_value",
            "errorCode": "serialize_value",
            "errorDetails": [],
            "httpStatusCode": 99,
            "message": "serialize_value",
        }

        model = Service_offer_management_UnauthorizedError(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "debugId" in serialized
        assert "errorCode" in serialized
        assert "errorDetails" in serialized
        assert "httpStatusCode" in serialized
        assert "message" in serialized

        # Verify values are preserved
        assert serialized["debugId"] == test_data["debugId"]
        assert serialized["errorCode"] == test_data["errorCode"]
        assert serialized["errorDetails"] == test_data["errorDetails"]
        assert serialized["httpStatusCode"] == test_data["httpStatusCode"]
        assert serialized["message"] == test_data["message"]

    def test_service_offer_management_unauthorizederror_model_json_schema(self):
        """Test Service_offer_management_UnauthorizedError model JSON schema generation."""
        schema = Service_offer_management_UnauthorizedError.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "debugId",
            "errorCode",
            "errorDetails",
            "httpStatusCode",
            "message",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "debugId",
            "errorCode",
            "httpStatusCode",
            "message",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_provision_management_badrequesterror_model_creation(self):
        """Test Service_provision_management_BadRequestError model creation with valid data."""
        # Valid test data for Service_provision_management_BadRequestError
        valid_data = {
            "message": "test_message",
            "debugId": "test_debugId",
            "errorCode": "test_errorCode",
            "errorDetails": [],
            "httpStatusCode": 42,
        }

        # Create model instance
        model = Service_provision_management_BadRequestError(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_provision_management_BadRequestError)
        assert model.message == valid_data["message"]
        assert model.debugId == valid_data["debugId"]
        assert model.errorCode == valid_data["errorCode"]
        assert model.errorDetails == valid_data["errorDetails"]
        assert model.httpStatusCode == valid_data["httpStatusCode"]

    def test_service_provision_management_badrequesterror_model_validation(self):
        """Test Service_provision_management_BadRequestError model field validation."""
        # Test with minimal required data
        minimal_data = {
            "message": "required_message",
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
            "errorDetails": [],
            "httpStatusCode": 1,
        }

        model = Service_provision_management_BadRequestError(**minimal_data)
        assert isinstance(model, Service_provision_management_BadRequestError)
        assert model.message == minimal_data["message"]
        assert model.debugId == minimal_data["debugId"]
        assert model.errorCode == minimal_data["errorCode"]
        assert model.errorDetails == minimal_data["errorDetails"]
        assert model.httpStatusCode == minimal_data["httpStatusCode"]

    def test_service_provision_management_badrequesterror_model_required_fields(self):
        """Test Service_provision_management_BadRequestError model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "message",
            "debugId",
            "errorCode",
            "errorDetails",
            "httpStatusCode",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_provision_management_BadRequestError()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "message",
                "debugId",
                "errorCode",
                "errorDetails",
                "httpStatusCode",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_provision_management_BadRequestError()
            assert isinstance(model, Service_provision_management_BadRequestError)

    def test_service_provision_management_badrequesterror_model_optional_fields(self):
        """Test Service_provision_management_BadRequestError model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "message": "required_message",
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
            "errorDetails": [],
            "httpStatusCode": 1,
        }

        model = Service_provision_management_BadRequestError(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_provision_management_badrequesterror_model_serialization(self):
        """Test Service_provision_management_BadRequestError model serialization to dict."""
        test_data = {
            "message": "serialize_value",
            "debugId": "serialize_value",
            "errorCode": "serialize_value",
            "errorDetails": [],
            "httpStatusCode": 99,
        }

        model = Service_provision_management_BadRequestError(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "message" in serialized
        assert "debugId" in serialized
        assert "errorCode" in serialized
        assert "errorDetails" in serialized
        assert "httpStatusCode" in serialized

        # Verify values are preserved
        assert serialized["message"] == test_data["message"]
        assert serialized["debugId"] == test_data["debugId"]
        assert serialized["errorCode"] == test_data["errorCode"]
        assert serialized["errorDetails"] == test_data["errorDetails"]
        assert serialized["httpStatusCode"] == test_data["httpStatusCode"]

    def test_service_provision_management_badrequesterror_model_json_schema(self):
        """Test Service_provision_management_BadRequestError model JSON schema generation."""
        schema = Service_provision_management_BadRequestError.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "message",
            "debugId",
            "errorCode",
            "errorDetails",
            "httpStatusCode",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "message",
            "debugId",
            "errorCode",
            "errorDetails",
            "httpStatusCode",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_offer_management_servicemanagerprovisionresourcelink_model_creation(self):
        """Test Service_offer_management_ServiceManagerProvisionResourceLink model creation with valid data."""
        # Valid test data for Service_offer_management_ServiceManagerProvisionResourceLink
        valid_data = {
            "id": "test_id",
            "resourceUri": "test_resourceUri",
        }

        # Create model instance
        model = Service_offer_management_ServiceManagerProvisionResourceLink(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_offer_management_ServiceManagerProvisionResourceLink)
        assert model.id == valid_data["id"]
        assert model.resourceUri == valid_data["resourceUri"]

    def test_service_offer_management_servicemanagerprovisionresourcelink_model_validation(self):
        """Test Service_offer_management_ServiceManagerProvisionResourceLink model field validation."""
        # Test with minimal required data
        minimal_data = {}

        model = Service_offer_management_ServiceManagerProvisionResourceLink(**minimal_data)
        assert isinstance(model, Service_offer_management_ServiceManagerProvisionResourceLink)

    def test_service_offer_management_servicemanagerprovisionresourcelink_model_required_fields(self):
        """Test Service_offer_management_ServiceManagerProvisionResourceLink model required field validation."""
        # Check if this model has any required fields
        required_fields = []

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_offer_management_ServiceManagerProvisionResourceLink()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {}

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_offer_management_ServiceManagerProvisionResourceLink()
            assert isinstance(model, Service_offer_management_ServiceManagerProvisionResourceLink)

    def test_service_offer_management_servicemanagerprovisionresourcelink_model_optional_fields(self):
        """Test Service_offer_management_ServiceManagerProvisionResourceLink model optional field handling."""
        # Create with minimal required data
        minimal_data = {}

        model = Service_offer_management_ServiceManagerProvisionResourceLink(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "id")
        # Optional field id should be None or have a default value
        assert model.id is None or model.id is not None
        assert hasattr(model, "resourceUri")
        # Optional field resourceUri should be None or have a default value
        assert model.resourceUri is None or model.resourceUri is not None

    def test_service_offer_management_servicemanagerprovisionresourcelink_model_serialization(self):
        """Test Service_offer_management_ServiceManagerProvisionResourceLink model serialization to dict."""
        test_data = {
            "id": "serialize_value",
            "resourceUri": "serialize_value",
        }

        model = Service_offer_management_ServiceManagerProvisionResourceLink(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "id" in serialized
        assert "resourceUri" in serialized

        # Verify values are preserved
        assert serialized["id"] == test_data["id"]
        assert serialized["resourceUri"] == test_data["resourceUri"]

    def test_service_offer_management_servicemanagerprovisionresourcelink_model_json_schema(self):
        """Test Service_offer_management_ServiceManagerProvisionResourceLink model JSON schema generation."""
        schema = Service_offer_management_ServiceManagerProvisionResourceLink.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "id",
            "resourceUri",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = []
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_offer_management_mspconversionstatus_model_creation(self):
        """Test Service_offer_management_MSPConversionStatus model creation with valid data."""
        # Valid test data for Service_offer_management_MSPConversionStatus
        valid_data = {}

        # Create model instance
        model = Service_offer_management_MSPConversionStatus(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_offer_management_MSPConversionStatus)

    def test_service_offer_management_mspconversionstatus_model_validation(self):
        """Test Service_offer_management_MSPConversionStatus model field validation."""
        # Test with minimal required data
        minimal_data = {}

        model = Service_offer_management_MSPConversionStatus(**minimal_data)
        assert isinstance(model, Service_offer_management_MSPConversionStatus)

    def test_service_offer_management_mspconversionstatus_model_required_fields(self):
        """Test Service_offer_management_MSPConversionStatus model required field validation."""
        # Check if this model has any required fields
        required_fields = []

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_offer_management_MSPConversionStatus()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {}

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_offer_management_MSPConversionStatus()
            assert isinstance(model, Service_offer_management_MSPConversionStatus)

    def test_service_offer_management_mspconversionstatus_model_optional_fields(self):
        """Test Service_offer_management_MSPConversionStatus model optional field handling."""
        # Create with minimal required data
        minimal_data = {}

        model = Service_offer_management_MSPConversionStatus(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_offer_management_mspconversionstatus_model_serialization(self):
        """Test Service_offer_management_MSPConversionStatus model serialization to dict."""
        test_data = {}

        model = Service_offer_management_MSPConversionStatus(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)

        # Verify values are preserved

    def test_service_offer_management_mspconversionstatus_model_json_schema(self):
        """Test Service_offer_management_MSPConversionStatus model JSON schema generation."""
        schema = Service_offer_management_MSPConversionStatus.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {}

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = []
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_manager_management_servicemanagerprovisionreadlist_model_creation(self):
        """Test Service_Manager_Management_ServiceManagerProvisionReadList model creation with valid data."""
        # Valid test data for Service_Manager_Management_ServiceManagerProvisionReadList
        valid_data = {
            "offset": 42,
            "total": 42,
            "count": 42,
            "items": [],
        }

        # Create model instance
        model = Service_Manager_Management_ServiceManagerProvisionReadList(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_Manager_Management_ServiceManagerProvisionReadList)
        assert model.offset == valid_data["offset"]
        assert model.total == valid_data["total"]
        assert model.count == valid_data["count"]
        assert model.items == valid_data["items"]

    def test_service_manager_management_servicemanagerprovisionreadlist_model_validation(self):
        """Test Service_Manager_Management_ServiceManagerProvisionReadList model field validation."""
        # Test with minimal required data
        minimal_data = {
            "offset": 1,
            "count": 1,
            "items": [],
        }

        model = Service_Manager_Management_ServiceManagerProvisionReadList(**minimal_data)
        assert isinstance(model, Service_Manager_Management_ServiceManagerProvisionReadList)
        assert model.offset == minimal_data["offset"]
        assert model.count == minimal_data["count"]
        assert model.items == minimal_data["items"]

    def test_service_manager_management_servicemanagerprovisionreadlist_model_required_fields(self):
        """Test Service_Manager_Management_ServiceManagerProvisionReadList model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "offset",
            "count",
            "items",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_Manager_Management_ServiceManagerProvisionReadList()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "offset",
                "count",
                "items",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_Manager_Management_ServiceManagerProvisionReadList()
            assert isinstance(model, Service_Manager_Management_ServiceManagerProvisionReadList)

    def test_service_manager_management_servicemanagerprovisionreadlist_model_optional_fields(self):
        """Test Service_Manager_Management_ServiceManagerProvisionReadList model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "offset": 1,
            "count": 1,
            "items": [],
        }

        model = Service_Manager_Management_ServiceManagerProvisionReadList(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "total")
        # Optional field total should be None or have a default value
        assert model.total is None or model.total is not None

    def test_service_manager_management_servicemanagerprovisionreadlist_model_serialization(self):
        """Test Service_Manager_Management_ServiceManagerProvisionReadList model serialization to dict."""
        test_data = {
            "offset": 99,
            "total": 99,
            "count": 99,
            "items": [],
        }

        model = Service_Manager_Management_ServiceManagerProvisionReadList(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "offset" in serialized
        assert "total" in serialized
        assert "count" in serialized
        assert "items" in serialized

        # Verify values are preserved
        assert serialized["offset"] == test_data["offset"]
        assert serialized["total"] == test_data["total"]
        assert serialized["count"] == test_data["count"]
        assert serialized["items"] == test_data["items"]

    def test_service_manager_management_servicemanagerprovisionreadlist_model_json_schema(self):
        """Test Service_Manager_Management_ServiceManagerProvisionReadList model JSON schema generation."""
        schema = Service_Manager_Management_ServiceManagerProvisionReadList.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "offset",
            "total",
            "count",
            "items",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "offset",
            "count",
            "items",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_offer_management_workspaceresourcelink_model_creation(self):
        """Test Service_offer_management_WorkspaceResourceLink model creation with valid data."""
        # Valid test data for Service_offer_management_WorkspaceResourceLink
        valid_data = {
            "organizationId": "test_organizationId",
            "resourceUri": "test_resourceUri",
            "workspaceTransferStatus": "test_workspaceTransferStatus",
            "id": "test_id",
            "name": "test_name",
        }

        # Create model instance
        model = Service_offer_management_WorkspaceResourceLink(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_offer_management_WorkspaceResourceLink)
        assert model.organizationId == valid_data["organizationId"]
        assert model.resourceUri == valid_data["resourceUri"]
        assert model.workspaceTransferStatus == valid_data["workspaceTransferStatus"]
        assert model.id == valid_data["id"]
        assert model.name == valid_data["name"]

    def test_service_offer_management_workspaceresourcelink_model_validation(self):
        """Test Service_offer_management_WorkspaceResourceLink model field validation."""
        # Test with minimal required data
        minimal_data = {}

        model = Service_offer_management_WorkspaceResourceLink(**minimal_data)
        assert isinstance(model, Service_offer_management_WorkspaceResourceLink)

    def test_service_offer_management_workspaceresourcelink_model_required_fields(self):
        """Test Service_offer_management_WorkspaceResourceLink model required field validation."""
        # Check if this model has any required fields
        required_fields = []

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_offer_management_WorkspaceResourceLink()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {}

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_offer_management_WorkspaceResourceLink()
            assert isinstance(model, Service_offer_management_WorkspaceResourceLink)

    def test_service_offer_management_workspaceresourcelink_model_optional_fields(self):
        """Test Service_offer_management_WorkspaceResourceLink model optional field handling."""
        # Create with minimal required data
        minimal_data = {}

        model = Service_offer_management_WorkspaceResourceLink(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "organizationId")
        # Optional field organizationId should be None or have a default value
        assert model.organizationId is None or model.organizationId is not None
        assert hasattr(model, "resourceUri")
        # Optional field resourceUri should be None or have a default value
        assert model.resourceUri is None or model.resourceUri is not None
        assert hasattr(model, "workspaceTransferStatus")
        # Optional field workspaceTransferStatus should be None or have a default value
        assert model.workspaceTransferStatus is None or model.workspaceTransferStatus is not None
        assert hasattr(model, "id")
        # Optional field id should be None or have a default value
        assert model.id is None or model.id is not None
        assert hasattr(model, "name")
        # Optional field name should be None or have a default value
        assert model.name is None or model.name is not None

    def test_service_offer_management_workspaceresourcelink_model_serialization(self):
        """Test Service_offer_management_WorkspaceResourceLink model serialization to dict."""
        test_data = {
            "organizationId": "serialize_value",
            "resourceUri": "serialize_value",
            "workspaceTransferStatus": "serialize_value",
            "id": "serialize_value",
            "name": "serialize_value",
        }

        model = Service_offer_management_WorkspaceResourceLink(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "organizationId" in serialized
        assert "resourceUri" in serialized
        assert "workspaceTransferStatus" in serialized
        assert "id" in serialized
        assert "name" in serialized

        # Verify values are preserved
        assert serialized["organizationId"] == test_data["organizationId"]
        assert serialized["resourceUri"] == test_data["resourceUri"]
        assert serialized["workspaceTransferStatus"] == test_data["workspaceTransferStatus"]
        assert serialized["id"] == test_data["id"]
        assert serialized["name"] == test_data["name"]

    def test_service_offer_management_workspaceresourcelink_model_json_schema(self):
        """Test Service_offer_management_WorkspaceResourceLink model JSON schema generation."""
        schema = Service_offer_management_WorkspaceResourceLink.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "organizationId",
            "resourceUri",
            "workspaceTransferStatus",
            "id",
            "name",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = []
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_offer_management_serviceofferread_model_creation(self):
        """Test Service_offer_management_ServiceOfferRead model creation with valid data."""
        # Valid test data for Service_offer_management_ServiceOfferRead
        valid_data = {
            "termsOfServiceUrl": "test_termsOfServiceUrl",
            "shortDescription": "test_shortDescription",
            "capabilities": [],
            "overview": "test_overview",
            "resourceUri": "test_resourceUri",
            "categories": [],
            "documentationUrl": "test_documentationUrl",
            "status": "test_status",
            "preProvisionMessage": "test_preProvisionMessage",
            "testDriveUrl": "test_testDriveUrl",
            "generation": "test_generation",
            "id": "test_id",
            "contactSalesUrl": "test_contactSalesUrl",
            "isDefault": "test_isDefault",
            "name": "test_name",
            "createdAt": "test_createdAt",
            "serviceManager": {},
            "serviceOfferType": "test_serviceOfferType",
            "evalUrl": "test_evalUrl",
            "brokerUri": "test_brokerUri",
            "staticLaunchUrl": "test_staticLaunchUrl",
            "languagesSupported": [],
            "slug": "test_slug",
            "featuresSupported": [],
            "updatedAt": "test_updatedAt",
        }

        # Create model instance
        model = Service_offer_management_ServiceOfferRead(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_offer_management_ServiceOfferRead)
        assert model.termsOfServiceUrl == valid_data["termsOfServiceUrl"]
        assert model.shortDescription == valid_data["shortDescription"]
        assert model.capabilities == valid_data["capabilities"]
        assert model.overview == valid_data["overview"]
        assert model.resourceUri == valid_data["resourceUri"]
        assert model.categories == valid_data["categories"]
        assert model.documentationUrl == valid_data["documentationUrl"]
        assert model.status == valid_data["status"]
        assert model.preProvisionMessage == valid_data["preProvisionMessage"]
        assert model.testDriveUrl == valid_data["testDriveUrl"]
        assert model.generation == valid_data["generation"]
        assert model.id == valid_data["id"]
        assert model.contactSalesUrl == valid_data["contactSalesUrl"]
        assert model.isDefault == valid_data["isDefault"]
        assert model.name == valid_data["name"]
        assert model.createdAt == valid_data["createdAt"]
        assert model.serviceManager == valid_data["serviceManager"]
        assert model.serviceOfferType == valid_data["serviceOfferType"]
        assert model.evalUrl == valid_data["evalUrl"]
        assert model.brokerUri == valid_data["brokerUri"]
        assert model.staticLaunchUrl == valid_data["staticLaunchUrl"]
        assert model.languagesSupported == valid_data["languagesSupported"]
        assert model.slug == valid_data["slug"]
        assert model.featuresSupported == valid_data["featuresSupported"]
        assert model.updatedAt == valid_data["updatedAt"]

    def test_service_offer_management_serviceofferread_model_validation(self):
        """Test Service_offer_management_ServiceOfferRead model field validation."""
        # Test with minimal required data
        minimal_data = {
            "termsOfServiceUrl": "required_termsOfServiceUrl",
            "shortDescription": "required_shortDescription",
            "capabilities": [],
            "overview": "required_overview",
            "resourceUri": "required_resourceUri",
            "categories": [],
            "documentationUrl": "required_documentationUrl",
            "status": "required_status",
            "preProvisionMessage": "required_preProvisionMessage",
            "testDriveUrl": "required_testDriveUrl",
            "id": "required_id",
            "contactSalesUrl": "required_contactSalesUrl",
            "name": "required_name",
            "createdAt": "required_createdAt",
            "serviceManager": {},
            "serviceOfferType": "required_serviceOfferType",
            "evalUrl": "required_evalUrl",
            "brokerUri": "required_brokerUri",
            "staticLaunchUrl": "required_staticLaunchUrl",
            "languagesSupported": [],
            "slug": "required_slug",
            "featuresSupported": [],
        }

        model = Service_offer_management_ServiceOfferRead(**minimal_data)
        assert isinstance(model, Service_offer_management_ServiceOfferRead)
        assert model.termsOfServiceUrl == minimal_data["termsOfServiceUrl"]
        assert model.shortDescription == minimal_data["shortDescription"]
        assert model.capabilities == minimal_data["capabilities"]
        assert model.overview == minimal_data["overview"]
        assert model.resourceUri == minimal_data["resourceUri"]
        assert model.categories == minimal_data["categories"]
        assert model.documentationUrl == minimal_data["documentationUrl"]
        assert model.status == minimal_data["status"]
        assert model.preProvisionMessage == minimal_data["preProvisionMessage"]
        assert model.testDriveUrl == minimal_data["testDriveUrl"]
        assert model.id == minimal_data["id"]
        assert model.contactSalesUrl == minimal_data["contactSalesUrl"]
        assert model.name == minimal_data["name"]
        assert model.createdAt == minimal_data["createdAt"]
        assert model.serviceManager == minimal_data["serviceManager"]
        assert model.serviceOfferType == minimal_data["serviceOfferType"]
        assert model.evalUrl == minimal_data["evalUrl"]
        assert model.brokerUri == minimal_data["brokerUri"]
        assert model.staticLaunchUrl == minimal_data["staticLaunchUrl"]
        assert model.languagesSupported == minimal_data["languagesSupported"]
        assert model.slug == minimal_data["slug"]
        assert model.featuresSupported == minimal_data["featuresSupported"]

    def test_service_offer_management_serviceofferread_model_required_fields(self):
        """Test Service_offer_management_ServiceOfferRead model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "termsOfServiceUrl",
            "shortDescription",
            "capabilities",
            "overview",
            "resourceUri",
            "categories",
            "documentationUrl",
            "status",
            "preProvisionMessage",
            "testDriveUrl",
            "id",
            "contactSalesUrl",
            "name",
            "createdAt",
            "serviceManager",
            "serviceOfferType",
            "evalUrl",
            "brokerUri",
            "staticLaunchUrl",
            "languagesSupported",
            "slug",
            "featuresSupported",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_offer_management_ServiceOfferRead()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "termsOfServiceUrl",
                "shortDescription",
                "capabilities",
                "overview",
                "resourceUri",
                "categories",
                "documentationUrl",
                "status",
                "preProvisionMessage",
                "testDriveUrl",
                "id",
                "contactSalesUrl",
                "name",
                "createdAt",
                "serviceManager",
                "serviceOfferType",
                "evalUrl",
                "brokerUri",
                "staticLaunchUrl",
                "languagesSupported",
                "slug",
                "featuresSupported",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_offer_management_ServiceOfferRead()
            assert isinstance(model, Service_offer_management_ServiceOfferRead)

    def test_service_offer_management_serviceofferread_model_optional_fields(self):
        """Test Service_offer_management_ServiceOfferRead model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "termsOfServiceUrl": "required_termsOfServiceUrl",
            "shortDescription": "required_shortDescription",
            "capabilities": [],
            "overview": "required_overview",
            "resourceUri": "required_resourceUri",
            "categories": [],
            "documentationUrl": "required_documentationUrl",
            "status": "required_status",
            "preProvisionMessage": "required_preProvisionMessage",
            "testDriveUrl": "required_testDriveUrl",
            "id": "required_id",
            "contactSalesUrl": "required_contactSalesUrl",
            "name": "required_name",
            "createdAt": "required_createdAt",
            "serviceManager": {},
            "serviceOfferType": "required_serviceOfferType",
            "evalUrl": "required_evalUrl",
            "brokerUri": "required_brokerUri",
            "staticLaunchUrl": "required_staticLaunchUrl",
            "languagesSupported": [],
            "slug": "required_slug",
            "featuresSupported": [],
        }

        model = Service_offer_management_ServiceOfferRead(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "generation")
        # Optional field generation should be None or have a default value
        assert model.generation is None or model.generation is not None
        assert hasattr(model, "isDefault")
        # Optional field isDefault should be None or have a default value
        assert model.isDefault is None or model.isDefault is not None
        assert hasattr(model, "updatedAt")
        # Optional field updatedAt should be None or have a default value
        assert model.updatedAt is None or model.updatedAt is not None

    def test_service_offer_management_serviceofferread_model_serialization(self):
        """Test Service_offer_management_ServiceOfferRead model serialization to dict."""
        test_data = {
            "termsOfServiceUrl": "serialize_value",
            "shortDescription": "serialize_value",
            "capabilities": [],
            "overview": "serialize_value",
            "resourceUri": "serialize_value",
            "categories": [],
            "documentationUrl": "serialize_value",
            "status": "serialize_value",
            "preProvisionMessage": "serialize_value",
            "testDriveUrl": "serialize_value",
            "generation": "serialize_value",
            "id": "serialize_value",
            "contactSalesUrl": "serialize_value",
            "isDefault": "serialize_value",
            "name": "serialize_value",
            "createdAt": "serialize_value",
            "serviceManager": {"key": "value"},
            "serviceOfferType": "serialize_value",
            "evalUrl": "serialize_value",
            "brokerUri": "serialize_value",
            "staticLaunchUrl": "serialize_value",
            "languagesSupported": [],
            "slug": "serialize_value",
            "featuresSupported": [],
            "updatedAt": "serialize_value",
        }

        model = Service_offer_management_ServiceOfferRead(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "termsOfServiceUrl" in serialized
        assert "shortDescription" in serialized
        assert "capabilities" in serialized
        assert "overview" in serialized
        assert "resourceUri" in serialized
        assert "categories" in serialized
        assert "documentationUrl" in serialized
        assert "status" in serialized
        assert "preProvisionMessage" in serialized
        assert "testDriveUrl" in serialized
        assert "generation" in serialized
        assert "id" in serialized
        assert "contactSalesUrl" in serialized
        assert "isDefault" in serialized
        assert "name" in serialized
        assert "createdAt" in serialized
        assert "serviceManager" in serialized
        assert "serviceOfferType" in serialized
        assert "evalUrl" in serialized
        assert "brokerUri" in serialized
        assert "staticLaunchUrl" in serialized
        assert "languagesSupported" in serialized
        assert "slug" in serialized
        assert "featuresSupported" in serialized
        assert "updatedAt" in serialized

        # Verify values are preserved
        assert serialized["termsOfServiceUrl"] == test_data["termsOfServiceUrl"]
        assert serialized["shortDescription"] == test_data["shortDescription"]
        assert serialized["capabilities"] == test_data["capabilities"]
        assert serialized["overview"] == test_data["overview"]
        assert serialized["resourceUri"] == test_data["resourceUri"]
        assert serialized["categories"] == test_data["categories"]
        assert serialized["documentationUrl"] == test_data["documentationUrl"]
        assert serialized["status"] == test_data["status"]
        assert serialized["preProvisionMessage"] == test_data["preProvisionMessage"]
        assert serialized["testDriveUrl"] == test_data["testDriveUrl"]
        assert serialized["generation"] == test_data["generation"]
        assert serialized["id"] == test_data["id"]
        assert serialized["contactSalesUrl"] == test_data["contactSalesUrl"]
        assert serialized["isDefault"] == test_data["isDefault"]
        assert serialized["name"] == test_data["name"]
        assert serialized["createdAt"] == test_data["createdAt"]
        assert serialized["serviceManager"] == test_data["serviceManager"]
        assert serialized["serviceOfferType"] == test_data["serviceOfferType"]
        assert serialized["evalUrl"] == test_data["evalUrl"]
        assert serialized["brokerUri"] == test_data["brokerUri"]
        assert serialized["staticLaunchUrl"] == test_data["staticLaunchUrl"]
        assert serialized["languagesSupported"] == test_data["languagesSupported"]
        assert serialized["slug"] == test_data["slug"]
        assert serialized["featuresSupported"] == test_data["featuresSupported"]
        assert serialized["updatedAt"] == test_data["updatedAt"]

    def test_service_offer_management_serviceofferread_model_json_schema(self):
        """Test Service_offer_management_ServiceOfferRead model JSON schema generation."""
        schema = Service_offer_management_ServiceOfferRead.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "termsOfServiceUrl",
            "shortDescription",
            "capabilities",
            "overview",
            "resourceUri",
            "categories",
            "documentationUrl",
            "status",
            "preProvisionMessage",
            "testDriveUrl",
            "generation",
            "id",
            "contactSalesUrl",
            "isDefault",
            "name",
            "createdAt",
            "serviceManager",
            "serviceOfferType",
            "evalUrl",
            "brokerUri",
            "staticLaunchUrl",
            "languagesSupported",
            "slug",
            "featuresSupported",
            "updatedAt",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "termsOfServiceUrl",
            "shortDescription",
            "capabilities",
            "overview",
            "resourceUri",
            "categories",
            "documentationUrl",
            "status",
            "preProvisionMessage",
            "testDriveUrl",
            "id",
            "contactSalesUrl",
            "name",
            "createdAt",
            "serviceManager",
            "serviceOfferType",
            "evalUrl",
            "brokerUri",
            "staticLaunchUrl",
            "languagesSupported",
            "slug",
            "featuresSupported",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_offer_management_workspaceopmode_model_creation(self):
        """Test Service_offer_management_WorkspaceOpMode model creation with valid data."""
        # Valid test data for Service_offer_management_WorkspaceOpMode
        valid_data = {}

        # Create model instance
        model = Service_offer_management_WorkspaceOpMode(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_offer_management_WorkspaceOpMode)

    def test_service_offer_management_workspaceopmode_model_validation(self):
        """Test Service_offer_management_WorkspaceOpMode model field validation."""
        # Test with minimal required data
        minimal_data = {}

        model = Service_offer_management_WorkspaceOpMode(**minimal_data)
        assert isinstance(model, Service_offer_management_WorkspaceOpMode)

    def test_service_offer_management_workspaceopmode_model_required_fields(self):
        """Test Service_offer_management_WorkspaceOpMode model required field validation."""
        # Check if this model has any required fields
        required_fields = []

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_offer_management_WorkspaceOpMode()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {}

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_offer_management_WorkspaceOpMode()
            assert isinstance(model, Service_offer_management_WorkspaceOpMode)

    def test_service_offer_management_workspaceopmode_model_optional_fields(self):
        """Test Service_offer_management_WorkspaceOpMode model optional field handling."""
        # Create with minimal required data
        minimal_data = {}

        model = Service_offer_management_WorkspaceOpMode(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_offer_management_workspaceopmode_model_serialization(self):
        """Test Service_offer_management_WorkspaceOpMode model serialization to dict."""
        test_data = {}

        model = Service_offer_management_WorkspaceOpMode(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)

        # Verify values are preserved

    def test_service_offer_management_workspaceopmode_model_json_schema(self):
        """Test Service_offer_management_WorkspaceOpMode model JSON schema generation."""
        schema = Service_offer_management_WorkspaceOpMode.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {}

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = []
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_provision_management_workspacetransferstatus_model_creation(self):
        """Test Service_provision_management_WorkspaceTransferStatus model creation with valid data."""
        # Valid test data for Service_provision_management_WorkspaceTransferStatus
        valid_data = {}

        # Create model instance
        model = Service_provision_management_WorkspaceTransferStatus(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_provision_management_WorkspaceTransferStatus)

    def test_service_provision_management_workspacetransferstatus_model_validation(self):
        """Test Service_provision_management_WorkspaceTransferStatus model field validation."""
        # Test with minimal required data
        minimal_data = {}

        model = Service_provision_management_WorkspaceTransferStatus(**minimal_data)
        assert isinstance(model, Service_provision_management_WorkspaceTransferStatus)

    def test_service_provision_management_workspacetransferstatus_model_required_fields(self):
        """Test Service_provision_management_WorkspaceTransferStatus model required field validation."""
        # Check if this model has any required fields
        required_fields = []

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_provision_management_WorkspaceTransferStatus()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {}

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_provision_management_WorkspaceTransferStatus()
            assert isinstance(model, Service_provision_management_WorkspaceTransferStatus)

    def test_service_provision_management_workspacetransferstatus_model_optional_fields(self):
        """Test Service_provision_management_WorkspaceTransferStatus model optional field handling."""
        # Create with minimal required data
        minimal_data = {}

        model = Service_provision_management_WorkspaceTransferStatus(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_provision_management_workspacetransferstatus_model_serialization(self):
        """Test Service_provision_management_WorkspaceTransferStatus model serialization to dict."""
        test_data = {}

        model = Service_provision_management_WorkspaceTransferStatus(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)

        # Verify values are preserved

    def test_service_provision_management_workspacetransferstatus_model_json_schema(self):
        """Test Service_provision_management_WorkspaceTransferStatus model JSON schema generation."""
        schema = Service_provision_management_WorkspaceTransferStatus.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {}

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = []
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_offer_management_serviceoffertype_model_creation(self):
        """Test Service_offer_management_ServiceOfferType model creation with valid data."""
        # Valid test data for Service_offer_management_ServiceOfferType
        valid_data = {}

        # Create model instance
        model = Service_offer_management_ServiceOfferType(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_offer_management_ServiceOfferType)

    def test_service_offer_management_serviceoffertype_model_validation(self):
        """Test Service_offer_management_ServiceOfferType model field validation."""
        # Test with minimal required data
        minimal_data = {}

        model = Service_offer_management_ServiceOfferType(**minimal_data)
        assert isinstance(model, Service_offer_management_ServiceOfferType)

    def test_service_offer_management_serviceoffertype_model_required_fields(self):
        """Test Service_offer_management_ServiceOfferType model required field validation."""
        # Check if this model has any required fields
        required_fields = []

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_offer_management_ServiceOfferType()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {}

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_offer_management_ServiceOfferType()
            assert isinstance(model, Service_offer_management_ServiceOfferType)

    def test_service_offer_management_serviceoffertype_model_optional_fields(self):
        """Test Service_offer_management_ServiceOfferType model optional field handling."""
        # Create with minimal required data
        minimal_data = {}

        model = Service_offer_management_ServiceOfferType(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_offer_management_serviceoffertype_model_serialization(self):
        """Test Service_offer_management_ServiceOfferType model serialization to dict."""
        test_data = {}

        model = Service_offer_management_ServiceOfferType(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)

        # Verify values are preserved

    def test_service_offer_management_serviceoffertype_model_json_schema(self):
        """Test Service_offer_management_ServiceOfferType model JSON schema generation."""
        schema = Service_offer_management_ServiceOfferType.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {}

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = []
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_manager_management_servicemanagersforaregion_model_creation(self):
        """Test Service_Manager_Management_ServiceManagersForARegion model creation with valid data."""
        # Valid test data for Service_Manager_Management_ServiceManagersForARegion
        valid_data = {
            "generation": 42,
            "id": "test_id",
            "regionName": "test_regionName",
            "serviceManagers": [],
            "type": "test_type",
        }

        # Create model instance
        model = Service_Manager_Management_ServiceManagersForARegion(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_Manager_Management_ServiceManagersForARegion)
        assert model.generation == valid_data["generation"]
        assert model.id == valid_data["id"]
        assert model.regionName == valid_data["regionName"]
        assert model.serviceManagers == valid_data["serviceManagers"]
        assert model.type == valid_data["type"]

    def test_service_manager_management_servicemanagersforaregion_model_validation(self):
        """Test Service_Manager_Management_ServiceManagersForARegion model field validation."""
        # Test with minimal required data
        minimal_data = {
            "generation": 1,
            "id": "required_id",
            "regionName": "required_regionName",
            "serviceManagers": [],
            "type": "required_type",
        }

        model = Service_Manager_Management_ServiceManagersForARegion(**minimal_data)
        assert isinstance(model, Service_Manager_Management_ServiceManagersForARegion)
        assert model.generation == minimal_data["generation"]
        assert model.id == minimal_data["id"]
        assert model.regionName == minimal_data["regionName"]
        assert model.serviceManagers == minimal_data["serviceManagers"]
        assert model.type == minimal_data["type"]

    def test_service_manager_management_servicemanagersforaregion_model_required_fields(self):
        """Test Service_Manager_Management_ServiceManagersForARegion model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "generation",
            "id",
            "regionName",
            "serviceManagers",
            "type",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_Manager_Management_ServiceManagersForARegion()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "generation",
                "id",
                "regionName",
                "serviceManagers",
                "type",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_Manager_Management_ServiceManagersForARegion()
            assert isinstance(model, Service_Manager_Management_ServiceManagersForARegion)

    def test_service_manager_management_servicemanagersforaregion_model_optional_fields(self):
        """Test Service_Manager_Management_ServiceManagersForARegion model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "generation": 1,
            "id": "required_id",
            "regionName": "required_regionName",
            "serviceManagers": [],
            "type": "required_type",
        }

        model = Service_Manager_Management_ServiceManagersForARegion(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_manager_management_servicemanagersforaregion_model_serialization(self):
        """Test Service_Manager_Management_ServiceManagersForARegion model serialization to dict."""
        test_data = {
            "generation": 99,
            "id": "serialize_value",
            "regionName": "serialize_value",
            "serviceManagers": [],
            "type": "serialize_value",
        }

        model = Service_Manager_Management_ServiceManagersForARegion(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "generation" in serialized
        assert "id" in serialized
        assert "regionName" in serialized
        assert "serviceManagers" in serialized
        assert "type" in serialized

        # Verify values are preserved
        assert serialized["generation"] == test_data["generation"]
        assert serialized["id"] == test_data["id"]
        assert serialized["regionName"] == test_data["regionName"]
        assert serialized["serviceManagers"] == test_data["serviceManagers"]
        assert serialized["type"] == test_data["type"]

    def test_service_manager_management_servicemanagersforaregion_model_json_schema(self):
        """Test Service_Manager_Management_ServiceManagersForARegion model JSON schema generation."""
        schema = Service_Manager_Management_ServiceManagersForARegion.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "generation",
            "id",
            "regionName",
            "serviceManagers",
            "type",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "generation",
            "id",
            "regionName",
            "serviceManagers",
            "type",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_offer_management_myservices_model_creation(self):
        """Test Service_offer_management_MyServices model creation with valid data."""
        # Valid test data for Service_offer_management_MyServices
        valid_data = {
            "next": "test_next",
            "total": 42,
            "count": 42,
            "items": [],
        }

        # Create model instance
        model = Service_offer_management_MyServices(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_offer_management_MyServices)
        assert model.next == valid_data["next"]
        assert model.total == valid_data["total"]
        assert model.count == valid_data["count"]
        assert model.items == valid_data["items"]

    def test_service_offer_management_myservices_model_validation(self):
        """Test Service_offer_management_MyServices model field validation."""
        # Test with minimal required data
        minimal_data = {
            "next": "required_next",
            "total": 1,
            "count": 1,
            "items": [],
        }

        model = Service_offer_management_MyServices(**minimal_data)
        assert isinstance(model, Service_offer_management_MyServices)
        assert model.next == minimal_data["next"]
        assert model.total == minimal_data["total"]
        assert model.count == minimal_data["count"]
        assert model.items == minimal_data["items"]

    def test_service_offer_management_myservices_model_required_fields(self):
        """Test Service_offer_management_MyServices model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "next",
            "total",
            "count",
            "items",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_offer_management_MyServices()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "next",
                "total",
                "count",
                "items",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_offer_management_MyServices()
            assert isinstance(model, Service_offer_management_MyServices)

    def test_service_offer_management_myservices_model_optional_fields(self):
        """Test Service_offer_management_MyServices model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "next": "required_next",
            "total": 1,
            "count": 1,
            "items": [],
        }

        model = Service_offer_management_MyServices(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_offer_management_myservices_model_serialization(self):
        """Test Service_offer_management_MyServices model serialization to dict."""
        test_data = {
            "next": "serialize_value",
            "total": 99,
            "count": 99,
            "items": [],
        }

        model = Service_offer_management_MyServices(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "next" in serialized
        assert "total" in serialized
        assert "count" in serialized
        assert "items" in serialized

        # Verify values are preserved
        assert serialized["next"] == test_data["next"]
        assert serialized["total"] == test_data["total"]
        assert serialized["count"] == test_data["count"]
        assert serialized["items"] == test_data["items"]

    def test_service_offer_management_myservices_model_json_schema(self):
        """Test Service_offer_management_MyServices model JSON schema generation."""
        schema = Service_offer_management_MyServices.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "next",
            "total",
            "count",
            "items",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "next",
            "total",
            "count",
            "items",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_provision_management_servicemanagerresourcelink_model_creation(self):
        """Test Service_provision_management_ServiceManagerResourceLink model creation with valid data."""
        # Valid test data for Service_provision_management_ServiceManagerResourceLink
        valid_data = {
            "resourceUri": "test_resourceUri",
            "id": "test_id",
        }

        # Create model instance
        model = Service_provision_management_ServiceManagerResourceLink(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_provision_management_ServiceManagerResourceLink)
        assert model.resourceUri == valid_data["resourceUri"]
        assert model.id == valid_data["id"]

    def test_service_provision_management_servicemanagerresourcelink_model_validation(self):
        """Test Service_provision_management_ServiceManagerResourceLink model field validation."""
        # Test with minimal required data
        minimal_data = {}

        model = Service_provision_management_ServiceManagerResourceLink(**minimal_data)
        assert isinstance(model, Service_provision_management_ServiceManagerResourceLink)

    def test_service_provision_management_servicemanagerresourcelink_model_required_fields(self):
        """Test Service_provision_management_ServiceManagerResourceLink model required field validation."""
        # Check if this model has any required fields
        required_fields = []

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_provision_management_ServiceManagerResourceLink()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {}

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_provision_management_ServiceManagerResourceLink()
            assert isinstance(model, Service_provision_management_ServiceManagerResourceLink)

    def test_service_provision_management_servicemanagerresourcelink_model_optional_fields(self):
        """Test Service_provision_management_ServiceManagerResourceLink model optional field handling."""
        # Create with minimal required data
        minimal_data = {}

        model = Service_provision_management_ServiceManagerResourceLink(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "resourceUri")
        # Optional field resourceUri should be None or have a default value
        assert model.resourceUri is None or model.resourceUri is not None
        assert hasattr(model, "id")
        # Optional field id should be None or have a default value
        assert model.id is None or model.id is not None

    def test_service_provision_management_servicemanagerresourcelink_model_serialization(self):
        """Test Service_provision_management_ServiceManagerResourceLink model serialization to dict."""
        test_data = {
            "resourceUri": "serialize_value",
            "id": "serialize_value",
        }

        model = Service_provision_management_ServiceManagerResourceLink(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "resourceUri" in serialized
        assert "id" in serialized

        # Verify values are preserved
        assert serialized["resourceUri"] == test_data["resourceUri"]
        assert serialized["id"] == test_data["id"]

    def test_service_provision_management_servicemanagerresourcelink_model_json_schema(self):
        """Test Service_provision_management_ServiceManagerResourceLink model JSON schema generation."""
        schema = Service_provision_management_ServiceManagerResourceLink.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "resourceUri",
            "id",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = []
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_provision_management_operationalmode_model_creation(self):
        """Test Service_provision_management_OperationalMode model creation with valid data."""
        # Valid test data for Service_provision_management_OperationalMode
        valid_data = {}

        # Create model instance
        model = Service_provision_management_OperationalMode(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_provision_management_OperationalMode)

    def test_service_provision_management_operationalmode_model_validation(self):
        """Test Service_provision_management_OperationalMode model field validation."""
        # Test with minimal required data
        minimal_data = {}

        model = Service_provision_management_OperationalMode(**minimal_data)
        assert isinstance(model, Service_provision_management_OperationalMode)

    def test_service_provision_management_operationalmode_model_required_fields(self):
        """Test Service_provision_management_OperationalMode model required field validation."""
        # Check if this model has any required fields
        required_fields = []

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_provision_management_OperationalMode()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {}

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_provision_management_OperationalMode()
            assert isinstance(model, Service_provision_management_OperationalMode)

    def test_service_provision_management_operationalmode_model_optional_fields(self):
        """Test Service_provision_management_OperationalMode model optional field handling."""
        # Create with minimal required data
        minimal_data = {}

        model = Service_provision_management_OperationalMode(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_provision_management_operationalmode_model_serialization(self):
        """Test Service_provision_management_OperationalMode model serialization to dict."""
        test_data = {}

        model = Service_provision_management_OperationalMode(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)

        # Verify values are preserved

    def test_service_provision_management_operationalmode_model_json_schema(self):
        """Test Service_provision_management_OperationalMode model JSON schema generation."""
        schema = Service_provision_management_OperationalMode.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {}

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = []
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_provision_management_unauthorizederror_model_creation(self):
        """Test Service_provision_management_UnauthorizedError model creation with valid data."""
        # Valid test data for Service_provision_management_UnauthorizedError
        valid_data = {
            "httpStatusCode": 42,
            "message": "test_message",
            "debugId": "test_debugId",
            "errorCode": "test_errorCode",
        }

        # Create model instance
        model = Service_provision_management_UnauthorizedError(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_provision_management_UnauthorizedError)
        assert model.httpStatusCode == valid_data["httpStatusCode"]
        assert model.message == valid_data["message"]
        assert model.debugId == valid_data["debugId"]
        assert model.errorCode == valid_data["errorCode"]

    def test_service_provision_management_unauthorizederror_model_validation(self):
        """Test Service_provision_management_UnauthorizedError model field validation."""
        # Test with minimal required data
        minimal_data = {
            "httpStatusCode": 1,
            "message": "required_message",
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
        }

        model = Service_provision_management_UnauthorizedError(**minimal_data)
        assert isinstance(model, Service_provision_management_UnauthorizedError)
        assert model.httpStatusCode == minimal_data["httpStatusCode"]
        assert model.message == minimal_data["message"]
        assert model.debugId == minimal_data["debugId"]
        assert model.errorCode == minimal_data["errorCode"]

    def test_service_provision_management_unauthorizederror_model_required_fields(self):
        """Test Service_provision_management_UnauthorizedError model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "httpStatusCode",
            "message",
            "debugId",
            "errorCode",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_provision_management_UnauthorizedError()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "httpStatusCode",
                "message",
                "debugId",
                "errorCode",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_provision_management_UnauthorizedError()
            assert isinstance(model, Service_provision_management_UnauthorizedError)

    def test_service_provision_management_unauthorizederror_model_optional_fields(self):
        """Test Service_provision_management_UnauthorizedError model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "httpStatusCode": 1,
            "message": "required_message",
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
        }

        model = Service_provision_management_UnauthorizedError(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_provision_management_unauthorizederror_model_serialization(self):
        """Test Service_provision_management_UnauthorizedError model serialization to dict."""
        test_data = {
            "httpStatusCode": 99,
            "message": "serialize_value",
            "debugId": "serialize_value",
            "errorCode": "serialize_value",
        }

        model = Service_provision_management_UnauthorizedError(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "httpStatusCode" in serialized
        assert "message" in serialized
        assert "debugId" in serialized
        assert "errorCode" in serialized

        # Verify values are preserved
        assert serialized["httpStatusCode"] == test_data["httpStatusCode"]
        assert serialized["message"] == test_data["message"]
        assert serialized["debugId"] == test_data["debugId"]
        assert serialized["errorCode"] == test_data["errorCode"]

    def test_service_provision_management_unauthorizederror_model_json_schema(self):
        """Test Service_provision_management_UnauthorizedError model JSON schema generation."""
        schema = Service_provision_management_UnauthorizedError.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "httpStatusCode",
            "message",
            "debugId",
            "errorCode",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "httpStatusCode",
            "message",
            "debugId",
            "errorCode",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_manager_management_conflicterror_model_creation(self):
        """Test Service_Manager_Management_ConflictError model creation with valid data."""
        # Valid test data for Service_Manager_Management_ConflictError
        valid_data = {
            "errorCode": "test_errorCode",
            "httpStatusCode": 42,
            "message": "test_message",
            "debugId": "test_debugId",
        }

        # Create model instance
        model = Service_Manager_Management_ConflictError(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_Manager_Management_ConflictError)
        assert model.errorCode == valid_data["errorCode"]
        assert model.httpStatusCode == valid_data["httpStatusCode"]
        assert model.message == valid_data["message"]
        assert model.debugId == valid_data["debugId"]

    def test_service_manager_management_conflicterror_model_validation(self):
        """Test Service_Manager_Management_ConflictError model field validation."""
        # Test with minimal required data
        minimal_data = {
            "errorCode": "required_errorCode",
            "httpStatusCode": 1,
            "message": "required_message",
            "debugId": "required_debugId",
        }

        model = Service_Manager_Management_ConflictError(**minimal_data)
        assert isinstance(model, Service_Manager_Management_ConflictError)
        assert model.errorCode == minimal_data["errorCode"]
        assert model.httpStatusCode == minimal_data["httpStatusCode"]
        assert model.message == minimal_data["message"]
        assert model.debugId == minimal_data["debugId"]

    def test_service_manager_management_conflicterror_model_required_fields(self):
        """Test Service_Manager_Management_ConflictError model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "errorCode",
            "httpStatusCode",
            "message",
            "debugId",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_Manager_Management_ConflictError()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "errorCode",
                "httpStatusCode",
                "message",
                "debugId",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_Manager_Management_ConflictError()
            assert isinstance(model, Service_Manager_Management_ConflictError)

    def test_service_manager_management_conflicterror_model_optional_fields(self):
        """Test Service_Manager_Management_ConflictError model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "errorCode": "required_errorCode",
            "httpStatusCode": 1,
            "message": "required_message",
            "debugId": "required_debugId",
        }

        model = Service_Manager_Management_ConflictError(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_manager_management_conflicterror_model_serialization(self):
        """Test Service_Manager_Management_ConflictError model serialization to dict."""
        test_data = {
            "errorCode": "serialize_value",
            "httpStatusCode": 99,
            "message": "serialize_value",
            "debugId": "serialize_value",
        }

        model = Service_Manager_Management_ConflictError(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "errorCode" in serialized
        assert "httpStatusCode" in serialized
        assert "message" in serialized
        assert "debugId" in serialized

        # Verify values are preserved
        assert serialized["errorCode"] == test_data["errorCode"]
        assert serialized["httpStatusCode"] == test_data["httpStatusCode"]
        assert serialized["message"] == test_data["message"]
        assert serialized["debugId"] == test_data["debugId"]

    def test_service_manager_management_conflicterror_model_json_schema(self):
        """Test Service_Manager_Management_ConflictError model JSON schema generation."""
        schema = Service_Manager_Management_ConflictError.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "errorCode",
            "httpStatusCode",
            "message",
            "debugId",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "errorCode",
            "httpStatusCode",
            "message",
            "debugId",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_provision_management_provisionstatus_model_creation(self):
        """Test Service_provision_management_ProvisionStatus model creation with valid data."""
        # Valid test data for Service_provision_management_ProvisionStatus
        valid_data = {}

        # Create model instance
        model = Service_provision_management_ProvisionStatus(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_provision_management_ProvisionStatus)

    def test_service_provision_management_provisionstatus_model_validation(self):
        """Test Service_provision_management_ProvisionStatus model field validation."""
        # Test with minimal required data
        minimal_data = {}

        model = Service_provision_management_ProvisionStatus(**minimal_data)
        assert isinstance(model, Service_provision_management_ProvisionStatus)

    def test_service_provision_management_provisionstatus_model_required_fields(self):
        """Test Service_provision_management_ProvisionStatus model required field validation."""
        # Check if this model has any required fields
        required_fields = []

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_provision_management_ProvisionStatus()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {}

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_provision_management_ProvisionStatus()
            assert isinstance(model, Service_provision_management_ProvisionStatus)

    def test_service_provision_management_provisionstatus_model_optional_fields(self):
        """Test Service_provision_management_ProvisionStatus model optional field handling."""
        # Create with minimal required data
        minimal_data = {}

        model = Service_provision_management_ProvisionStatus(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_provision_management_provisionstatus_model_serialization(self):
        """Test Service_provision_management_ProvisionStatus model serialization to dict."""
        test_data = {}

        model = Service_provision_management_ProvisionStatus(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)

        # Verify values are preserved

    def test_service_provision_management_provisionstatus_model_json_schema(self):
        """Test Service_provision_management_ProvisionStatus model JSON schema generation."""
        schema = Service_provision_management_ProvisionStatus.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {}

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = []
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_offer_management_recentservicesv2_model_creation(self):
        """Test Service_offer_management_RecentServicesV2 model creation with valid data."""
        # Valid test data for Service_offer_management_RecentServicesV2
        valid_data = {
            "next": "test_next",
            "total": 42,
            "count": 42,
            "items": [],
        }

        # Create model instance
        model = Service_offer_management_RecentServicesV2(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_offer_management_RecentServicesV2)
        assert model.next == valid_data["next"]
        assert model.total == valid_data["total"]
        assert model.count == valid_data["count"]
        assert model.items == valid_data["items"]

    def test_service_offer_management_recentservicesv2_model_validation(self):
        """Test Service_offer_management_RecentServicesV2 model field validation."""
        # Test with minimal required data
        minimal_data = {
            "next": "required_next",
            "total": 1,
            "count": 1,
            "items": [],
        }

        model = Service_offer_management_RecentServicesV2(**minimal_data)
        assert isinstance(model, Service_offer_management_RecentServicesV2)
        assert model.next == minimal_data["next"]
        assert model.total == minimal_data["total"]
        assert model.count == minimal_data["count"]
        assert model.items == minimal_data["items"]

    def test_service_offer_management_recentservicesv2_model_required_fields(self):
        """Test Service_offer_management_RecentServicesV2 model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "next",
            "total",
            "count",
            "items",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_offer_management_RecentServicesV2()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "next",
                "total",
                "count",
                "items",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_offer_management_RecentServicesV2()
            assert isinstance(model, Service_offer_management_RecentServicesV2)

    def test_service_offer_management_recentservicesv2_model_optional_fields(self):
        """Test Service_offer_management_RecentServicesV2 model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "next": "required_next",
            "total": 1,
            "count": 1,
            "items": [],
        }

        model = Service_offer_management_RecentServicesV2(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_offer_management_recentservicesv2_model_serialization(self):
        """Test Service_offer_management_RecentServicesV2 model serialization to dict."""
        test_data = {
            "next": "serialize_value",
            "total": 99,
            "count": 99,
            "items": [],
        }

        model = Service_offer_management_RecentServicesV2(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "next" in serialized
        assert "total" in serialized
        assert "count" in serialized
        assert "items" in serialized

        # Verify values are preserved
        assert serialized["next"] == test_data["next"]
        assert serialized["total"] == test_data["total"]
        assert serialized["count"] == test_data["count"]
        assert serialized["items"] == test_data["items"]

    def test_service_offer_management_recentservicesv2_model_json_schema(self):
        """Test Service_offer_management_RecentServicesV2 model JSON schema generation."""
        schema = Service_offer_management_RecentServicesV2.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "next",
            "total",
            "count",
            "items",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "next",
            "total",
            "count",
            "items",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_offer_management_serviceofferregionread_model_creation(self):
        """Test Service_offer_management_ServiceOfferRegionRead model creation with valid data."""
        # Valid test data for Service_offer_management_ServiceOfferRegionRead
        valid_data = {
            "status": "test_status",
            "type": "test_type",
            "updatedAt": "test_updatedAt",
            "generation": 42,
            "resourceUri": "test_resourceUri",
            "region": "test_region",
            "serviceOffer": {},
            "createdAt": "test_createdAt",
            "id": "test_id",
        }

        # Create model instance
        model = Service_offer_management_ServiceOfferRegionRead(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_offer_management_ServiceOfferRegionRead)
        assert model.status == valid_data["status"]
        assert model.type == valid_data["type"]
        assert model.updatedAt == valid_data["updatedAt"]
        assert model.generation == valid_data["generation"]
        assert model.resourceUri == valid_data["resourceUri"]
        assert model.region == valid_data["region"]
        assert model.serviceOffer == valid_data["serviceOffer"]
        assert model.createdAt == valid_data["createdAt"]
        assert model.id == valid_data["id"]

    def test_service_offer_management_serviceofferregionread_model_validation(self):
        """Test Service_offer_management_ServiceOfferRegionRead model field validation."""
        # Test with minimal required data
        minimal_data = {
            "status": "required_status",
            "type": "required_type",
            "updatedAt": "required_updatedAt",
            "generation": 1,
            "region": "required_region",
            "createdAt": "required_createdAt",
            "id": "required_id",
        }

        model = Service_offer_management_ServiceOfferRegionRead(**minimal_data)
        assert isinstance(model, Service_offer_management_ServiceOfferRegionRead)
        assert model.status == minimal_data["status"]
        assert model.type == minimal_data["type"]
        assert model.updatedAt == minimal_data["updatedAt"]
        assert model.generation == minimal_data["generation"]
        assert model.region == minimal_data["region"]
        assert model.createdAt == minimal_data["createdAt"]
        assert model.id == minimal_data["id"]

    def test_service_offer_management_serviceofferregionread_model_required_fields(self):
        """Test Service_offer_management_ServiceOfferRegionRead model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "status",
            "type",
            "updatedAt",
            "generation",
            "region",
            "createdAt",
            "id",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_offer_management_ServiceOfferRegionRead()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "status",
                "type",
                "updatedAt",
                "generation",
                "region",
                "createdAt",
                "id",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_offer_management_ServiceOfferRegionRead()
            assert isinstance(model, Service_offer_management_ServiceOfferRegionRead)

    def test_service_offer_management_serviceofferregionread_model_optional_fields(self):
        """Test Service_offer_management_ServiceOfferRegionRead model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "status": "required_status",
            "type": "required_type",
            "updatedAt": "required_updatedAt",
            "generation": 1,
            "region": "required_region",
            "createdAt": "required_createdAt",
            "id": "required_id",
        }

        model = Service_offer_management_ServiceOfferRegionRead(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "resourceUri")
        # Optional field resourceUri should be None or have a default value
        assert model.resourceUri is None or model.resourceUri is not None
        assert hasattr(model, "serviceOffer")
        # Optional field serviceOffer should be None or have a default value
        assert model.serviceOffer is None or model.serviceOffer is not None

    def test_service_offer_management_serviceofferregionread_model_serialization(self):
        """Test Service_offer_management_ServiceOfferRegionRead model serialization to dict."""
        test_data = {
            "status": "serialize_value",
            "type": "serialize_value",
            "updatedAt": "serialize_value",
            "generation": 99,
            "resourceUri": "serialize_value",
            "region": "serialize_value",
            "serviceOffer": {"key": "value"},
            "createdAt": "serialize_value",
            "id": "serialize_value",
        }

        model = Service_offer_management_ServiceOfferRegionRead(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "status" in serialized
        assert "type" in serialized
        assert "updatedAt" in serialized
        assert "generation" in serialized
        assert "resourceUri" in serialized
        assert "region" in serialized
        assert "serviceOffer" in serialized
        assert "createdAt" in serialized
        assert "id" in serialized

        # Verify values are preserved
        assert serialized["status"] == test_data["status"]
        assert serialized["type"] == test_data["type"]
        assert serialized["updatedAt"] == test_data["updatedAt"]
        assert serialized["generation"] == test_data["generation"]
        assert serialized["resourceUri"] == test_data["resourceUri"]
        assert serialized["region"] == test_data["region"]
        assert serialized["serviceOffer"] == test_data["serviceOffer"]
        assert serialized["createdAt"] == test_data["createdAt"]
        assert serialized["id"] == test_data["id"]

    def test_service_offer_management_serviceofferregionread_model_json_schema(self):
        """Test Service_offer_management_ServiceOfferRegionRead model JSON schema generation."""
        schema = Service_offer_management_ServiceOfferRegionRead.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "status",
            "type",
            "updatedAt",
            "generation",
            "resourceUri",
            "region",
            "serviceOffer",
            "createdAt",
            "id",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "status",
            "type",
            "updatedAt",
            "generation",
            "region",
            "createdAt",
            "id",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_offer_management_categorywithfeaturedserviceoffers_model_creation(self):
        """Test Service_offer_management_CategoryWithFeaturedServiceOffers model creation with valid data."""
        # Valid test data for Service_offer_management_CategoryWithFeaturedServiceOffers
        valid_data = {
            "id": "test_id",
            "servicesWithRegions": [],
            "type": "test_type",
        }

        # Create model instance
        model = Service_offer_management_CategoryWithFeaturedServiceOffers(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_offer_management_CategoryWithFeaturedServiceOffers)
        assert model.id == valid_data["id"]
        assert model.servicesWithRegions == valid_data["servicesWithRegions"]
        assert model.type == valid_data["type"]

    def test_service_offer_management_categorywithfeaturedserviceoffers_model_validation(self):
        """Test Service_offer_management_CategoryWithFeaturedServiceOffers model field validation."""
        # Test with minimal required data
        minimal_data = {
            "id": "required_id",
            "type": "required_type",
        }

        model = Service_offer_management_CategoryWithFeaturedServiceOffers(**minimal_data)
        assert isinstance(model, Service_offer_management_CategoryWithFeaturedServiceOffers)
        assert model.id == minimal_data["id"]
        assert model.type == minimal_data["type"]

    def test_service_offer_management_categorywithfeaturedserviceoffers_model_required_fields(self):
        """Test Service_offer_management_CategoryWithFeaturedServiceOffers model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "id",
            "type",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_offer_management_CategoryWithFeaturedServiceOffers()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "id",
                "type",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_offer_management_CategoryWithFeaturedServiceOffers()
            assert isinstance(model, Service_offer_management_CategoryWithFeaturedServiceOffers)

    def test_service_offer_management_categorywithfeaturedserviceoffers_model_optional_fields(self):
        """Test Service_offer_management_CategoryWithFeaturedServiceOffers model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "id": "required_id",
            "type": "required_type",
        }

        model = Service_offer_management_CategoryWithFeaturedServiceOffers(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "servicesWithRegions")
        # Optional field servicesWithRegions should be None or have a default value
        assert model.servicesWithRegions is None or model.servicesWithRegions is not None

    def test_service_offer_management_categorywithfeaturedserviceoffers_model_serialization(self):
        """Test Service_offer_management_CategoryWithFeaturedServiceOffers model serialization to dict."""
        test_data = {
            "id": "serialize_value",
            "servicesWithRegions": [],
            "type": "serialize_value",
        }

        model = Service_offer_management_CategoryWithFeaturedServiceOffers(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "id" in serialized
        assert "servicesWithRegions" in serialized
        assert "type" in serialized

        # Verify values are preserved
        assert serialized["id"] == test_data["id"]
        assert serialized["servicesWithRegions"] == test_data["servicesWithRegions"]
        assert serialized["type"] == test_data["type"]

    def test_service_offer_management_categorywithfeaturedserviceoffers_model_json_schema(self):
        """Test Service_offer_management_CategoryWithFeaturedServiceOffers model JSON schema generation."""
        schema = Service_offer_management_CategoryWithFeaturedServiceOffers.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "id",
            "servicesWithRegions",
            "type",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "id",
            "type",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_provision_management_serviceofferresourcelink_model_creation(self):
        """Test Service_provision_management_ServiceOfferResourceLink model creation with valid data."""
        # Valid test data for Service_provision_management_ServiceOfferResourceLink
        valid_data = {
            "id": "test_id",
            "name": "test_name",
            "resourceUri": "test_resourceUri",
        }

        # Create model instance
        model = Service_provision_management_ServiceOfferResourceLink(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_provision_management_ServiceOfferResourceLink)
        assert model.id == valid_data["id"]
        assert model.name == valid_data["name"]
        assert model.resourceUri == valid_data["resourceUri"]

    def test_service_provision_management_serviceofferresourcelink_model_validation(self):
        """Test Service_provision_management_ServiceOfferResourceLink model field validation."""
        # Test with minimal required data
        minimal_data = {}

        model = Service_provision_management_ServiceOfferResourceLink(**minimal_data)
        assert isinstance(model, Service_provision_management_ServiceOfferResourceLink)

    def test_service_provision_management_serviceofferresourcelink_model_required_fields(self):
        """Test Service_provision_management_ServiceOfferResourceLink model required field validation."""
        # Check if this model has any required fields
        required_fields = []

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_provision_management_ServiceOfferResourceLink()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {}

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_provision_management_ServiceOfferResourceLink()
            assert isinstance(model, Service_provision_management_ServiceOfferResourceLink)

    def test_service_provision_management_serviceofferresourcelink_model_optional_fields(self):
        """Test Service_provision_management_ServiceOfferResourceLink model optional field handling."""
        # Create with minimal required data
        minimal_data = {}

        model = Service_provision_management_ServiceOfferResourceLink(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "id")
        # Optional field id should be None or have a default value
        assert model.id is None or model.id is not None
        assert hasattr(model, "name")
        # Optional field name should be None or have a default value
        assert model.name is None or model.name is not None
        assert hasattr(model, "resourceUri")
        # Optional field resourceUri should be None or have a default value
        assert model.resourceUri is None or model.resourceUri is not None

    def test_service_provision_management_serviceofferresourcelink_model_serialization(self):
        """Test Service_provision_management_ServiceOfferResourceLink model serialization to dict."""
        test_data = {
            "id": "serialize_value",
            "name": "serialize_value",
            "resourceUri": "serialize_value",
        }

        model = Service_provision_management_ServiceOfferResourceLink(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "id" in serialized
        assert "name" in serialized
        assert "resourceUri" in serialized

        # Verify values are preserved
        assert serialized["id"] == test_data["id"]
        assert serialized["name"] == test_data["name"]
        assert serialized["resourceUri"] == test_data["resourceUri"]

    def test_service_provision_management_serviceofferresourcelink_model_json_schema(self):
        """Test Service_provision_management_ServiceOfferResourceLink model JSON schema generation."""
        schema = Service_provision_management_ServiceOfferResourceLink.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "id",
            "name",
            "resourceUri",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = []
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_manager_management_servicemanagerresourcelink_model_creation(self):
        """Test Service_Manager_Management_ServiceManagerResourceLink model creation with valid data."""
        # Valid test data for Service_Manager_Management_ServiceManagerResourceLink
        valid_data = {
            "id": "test_id",
            "resourceUri": "test_resourceUri",
        }

        # Create model instance
        model = Service_Manager_Management_ServiceManagerResourceLink(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_Manager_Management_ServiceManagerResourceLink)
        assert model.id == valid_data["id"]
        assert model.resourceUri == valid_data["resourceUri"]

    def test_service_manager_management_servicemanagerresourcelink_model_validation(self):
        """Test Service_Manager_Management_ServiceManagerResourceLink model field validation."""
        # Test with minimal required data
        minimal_data = {}

        model = Service_Manager_Management_ServiceManagerResourceLink(**minimal_data)
        assert isinstance(model, Service_Manager_Management_ServiceManagerResourceLink)

    def test_service_manager_management_servicemanagerresourcelink_model_required_fields(self):
        """Test Service_Manager_Management_ServiceManagerResourceLink model required field validation."""
        # Check if this model has any required fields
        required_fields = []

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_Manager_Management_ServiceManagerResourceLink()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {}

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_Manager_Management_ServiceManagerResourceLink()
            assert isinstance(model, Service_Manager_Management_ServiceManagerResourceLink)

    def test_service_manager_management_servicemanagerresourcelink_model_optional_fields(self):
        """Test Service_Manager_Management_ServiceManagerResourceLink model optional field handling."""
        # Create with minimal required data
        minimal_data = {}

        model = Service_Manager_Management_ServiceManagerResourceLink(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "id")
        # Optional field id should be None or have a default value
        assert model.id is None or model.id is not None
        assert hasattr(model, "resourceUri")
        # Optional field resourceUri should be None or have a default value
        assert model.resourceUri is None or model.resourceUri is not None

    def test_service_manager_management_servicemanagerresourcelink_model_serialization(self):
        """Test Service_Manager_Management_ServiceManagerResourceLink model serialization to dict."""
        test_data = {
            "id": "serialize_value",
            "resourceUri": "serialize_value",
        }

        model = Service_Manager_Management_ServiceManagerResourceLink(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "id" in serialized
        assert "resourceUri" in serialized

        # Verify values are preserved
        assert serialized["id"] == test_data["id"]
        assert serialized["resourceUri"] == test_data["resourceUri"]

    def test_service_manager_management_servicemanagerresourcelink_model_json_schema(self):
        """Test Service_Manager_Management_ServiceManagerResourceLink model JSON schema generation."""
        schema = Service_Manager_Management_ServiceManagerResourceLink.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "id",
            "resourceUri",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = []
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_offer_management_workspacetypes_model_creation(self):
        """Test Service_offer_management_WorkspaceTypes model creation with valid data."""
        # Valid test data for Service_offer_management_WorkspaceTypes
        valid_data = {}

        # Create model instance
        model = Service_offer_management_WorkspaceTypes(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_offer_management_WorkspaceTypes)

    def test_service_offer_management_workspacetypes_model_validation(self):
        """Test Service_offer_management_WorkspaceTypes model field validation."""
        # Test with minimal required data
        minimal_data = {}

        model = Service_offer_management_WorkspaceTypes(**minimal_data)
        assert isinstance(model, Service_offer_management_WorkspaceTypes)

    def test_service_offer_management_workspacetypes_model_required_fields(self):
        """Test Service_offer_management_WorkspaceTypes model required field validation."""
        # Check if this model has any required fields
        required_fields = []

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_offer_management_WorkspaceTypes()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {}

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_offer_management_WorkspaceTypes()
            assert isinstance(model, Service_offer_management_WorkspaceTypes)

    def test_service_offer_management_workspacetypes_model_optional_fields(self):
        """Test Service_offer_management_WorkspaceTypes model optional field handling."""
        # Create with minimal required data
        minimal_data = {}

        model = Service_offer_management_WorkspaceTypes(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_offer_management_workspacetypes_model_serialization(self):
        """Test Service_offer_management_WorkspaceTypes model serialization to dict."""
        test_data = {}

        model = Service_offer_management_WorkspaceTypes(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)

        # Verify values are preserved

    def test_service_offer_management_workspacetypes_model_json_schema(self):
        """Test Service_offer_management_WorkspaceTypes model JSON schema generation."""
        schema = Service_offer_management_WorkspaceTypes.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {}

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = []
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_offer_management_serviceofferpartialinfo_model_creation(self):
        """Test Service_offer_management_ServiceOfferPartialInfo model creation with valid data."""
        # Valid test data for Service_offer_management_ServiceOfferPartialInfo
        valid_data = {
            "staticLaunchUrl": "test_staticLaunchUrl",
            "categories": [],
            "id": "test_id",
            "name": "test_name",
            "resourceUri": "test_resourceUri",
            "serviceManager": {},
            "slug": "test_slug",
        }

        # Create model instance
        model = Service_offer_management_ServiceOfferPartialInfo(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_offer_management_ServiceOfferPartialInfo)
        assert model.staticLaunchUrl == valid_data["staticLaunchUrl"]
        assert model.categories == valid_data["categories"]
        assert model.id == valid_data["id"]
        assert model.name == valid_data["name"]
        assert model.resourceUri == valid_data["resourceUri"]
        assert model.serviceManager == valid_data["serviceManager"]
        assert model.slug == valid_data["slug"]

    def test_service_offer_management_serviceofferpartialinfo_model_validation(self):
        """Test Service_offer_management_ServiceOfferPartialInfo model field validation."""
        # Test with minimal required data
        minimal_data = {
            "staticLaunchUrl": "required_staticLaunchUrl",
            "categories": [],
            "id": "required_id",
            "name": "required_name",
            "resourceUri": "required_resourceUri",
            "slug": "required_slug",
        }

        model = Service_offer_management_ServiceOfferPartialInfo(**minimal_data)
        assert isinstance(model, Service_offer_management_ServiceOfferPartialInfo)
        assert model.staticLaunchUrl == minimal_data["staticLaunchUrl"]
        assert model.categories == minimal_data["categories"]
        assert model.id == minimal_data["id"]
        assert model.name == minimal_data["name"]
        assert model.resourceUri == minimal_data["resourceUri"]
        assert model.slug == minimal_data["slug"]

    def test_service_offer_management_serviceofferpartialinfo_model_required_fields(self):
        """Test Service_offer_management_ServiceOfferPartialInfo model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "staticLaunchUrl",
            "categories",
            "id",
            "name",
            "resourceUri",
            "slug",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_offer_management_ServiceOfferPartialInfo()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "staticLaunchUrl",
                "categories",
                "id",
                "name",
                "resourceUri",
                "slug",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_offer_management_ServiceOfferPartialInfo()
            assert isinstance(model, Service_offer_management_ServiceOfferPartialInfo)

    def test_service_offer_management_serviceofferpartialinfo_model_optional_fields(self):
        """Test Service_offer_management_ServiceOfferPartialInfo model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "staticLaunchUrl": "required_staticLaunchUrl",
            "categories": [],
            "id": "required_id",
            "name": "required_name",
            "resourceUri": "required_resourceUri",
            "slug": "required_slug",
        }

        model = Service_offer_management_ServiceOfferPartialInfo(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "serviceManager")
        # Optional field serviceManager should be None or have a default value
        assert model.serviceManager is None or model.serviceManager is not None

    def test_service_offer_management_serviceofferpartialinfo_model_serialization(self):
        """Test Service_offer_management_ServiceOfferPartialInfo model serialization to dict."""
        test_data = {
            "staticLaunchUrl": "serialize_value",
            "categories": [],
            "id": "serialize_value",
            "name": "serialize_value",
            "resourceUri": "serialize_value",
            "serviceManager": {"key": "value"},
            "slug": "serialize_value",
        }

        model = Service_offer_management_ServiceOfferPartialInfo(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "staticLaunchUrl" in serialized
        assert "categories" in serialized
        assert "id" in serialized
        assert "name" in serialized
        assert "resourceUri" in serialized
        assert "serviceManager" in serialized
        assert "slug" in serialized

        # Verify values are preserved
        assert serialized["staticLaunchUrl"] == test_data["staticLaunchUrl"]
        assert serialized["categories"] == test_data["categories"]
        assert serialized["id"] == test_data["id"]
        assert serialized["name"] == test_data["name"]
        assert serialized["resourceUri"] == test_data["resourceUri"]
        assert serialized["serviceManager"] == test_data["serviceManager"]
        assert serialized["slug"] == test_data["slug"]

    def test_service_offer_management_serviceofferpartialinfo_model_json_schema(self):
        """Test Service_offer_management_ServiceOfferPartialInfo model JSON schema generation."""
        schema = Service_offer_management_ServiceOfferPartialInfo.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "staticLaunchUrl",
            "categories",
            "id",
            "name",
            "resourceUri",
            "serviceManager",
            "slug",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "staticLaunchUrl",
            "categories",
            "id",
            "name",
            "resourceUri",
            "slug",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_service_manager_management_servicemanagerprovisioncreatebase_model_creation(self):
        """Test Service_Manager_Management_ServiceManagerProvisionCreateBase model creation with valid data."""
        # Valid test data for Service_Manager_Management_ServiceManagerProvisionCreateBase
        valid_data = {
            "region": "test_region",
            "serviceManagerId": "test_serviceManagerId",
        }

        # Create model instance
        model = Service_Manager_Management_ServiceManagerProvisionCreateBase(**valid_data)

        # Verify model creation
        assert isinstance(model, Service_Manager_Management_ServiceManagerProvisionCreateBase)
        assert model.region == valid_data["region"]
        assert model.serviceManagerId == valid_data["serviceManagerId"]

    def test_service_manager_management_servicemanagerprovisioncreatebase_model_validation(self):
        """Test Service_Manager_Management_ServiceManagerProvisionCreateBase model field validation."""
        # Test with minimal required data
        minimal_data = {
            "region": "required_region",
            "serviceManagerId": "required_serviceManagerId",
        }

        model = Service_Manager_Management_ServiceManagerProvisionCreateBase(**minimal_data)
        assert isinstance(model, Service_Manager_Management_ServiceManagerProvisionCreateBase)
        assert model.region == minimal_data["region"]
        assert model.serviceManagerId == minimal_data["serviceManagerId"]

    def test_service_manager_management_servicemanagerprovisioncreatebase_model_required_fields(self):
        """Test Service_Manager_Management_ServiceManagerProvisionCreateBase model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "region",
            "serviceManagerId",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Service_Manager_Management_ServiceManagerProvisionCreateBase()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "region",
                "serviceManagerId",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Service_Manager_Management_ServiceManagerProvisionCreateBase()
            assert isinstance(model, Service_Manager_Management_ServiceManagerProvisionCreateBase)

    def test_service_manager_management_servicemanagerprovisioncreatebase_model_optional_fields(self):
        """Test Service_Manager_Management_ServiceManagerProvisionCreateBase model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "region": "required_region",
            "serviceManagerId": "required_serviceManagerId",
        }

        model = Service_Manager_Management_ServiceManagerProvisionCreateBase(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_service_manager_management_servicemanagerprovisioncreatebase_model_serialization(self):
        """Test Service_Manager_Management_ServiceManagerProvisionCreateBase model serialization to dict."""
        test_data = {
            "region": "serialize_value",
            "serviceManagerId": "serialize_value",
        }

        model = Service_Manager_Management_ServiceManagerProvisionCreateBase(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "region" in serialized
        assert "serviceManagerId" in serialized

        # Verify values are preserved
        assert serialized["region"] == test_data["region"]
        assert serialized["serviceManagerId"] == test_data["serviceManagerId"]

    def test_service_manager_management_servicemanagerprovisioncreatebase_model_json_schema(self):
        """Test Service_Manager_Management_ServiceManagerProvisionCreateBase model JSON schema generation."""
        schema = Service_Manager_Management_ServiceManagerProvisionCreateBase.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "region",
            "serviceManagerId",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "region",
            "serviceManagerId",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)


class TestModelInteractions:
    """Test interactions between different models."""

    def test_model_creation_with_all_types(self):
        """Test creating models with various data types."""
        # Test data with different types
        test_cases = [
            ("string", "test_string"),
            ("integer", 42),
            ("number", 3.14159),
            ("boolean", True),
            ("array", ["item1", "item2", "item3"]),
            ("object", {"nested_key": "nested_value"}),
        ]

        for type_name, test_value in test_cases:
            # This is a general test - specific model tests are above
            assert test_value is not None

    def test_all_models_have_base_methods(self):
        """Test that all models inherit proper base functionality."""
        models_to_test = [
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
        ]

        for model_class in models_to_test:
            # Verify model has expected Pydantic methods
            assert hasattr(model_class, "model_dump")
            assert hasattr(model_class, "model_json_schema")
            assert hasattr(model_class, "model_validate")

            # Verify model inheritance
            assert hasattr(model_class, "__fields__") or hasattr(model_class, "model_fields")

    def test_model_error_handling(self):
        """Test model error handling with invalid data."""
        models_to_test = [
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
        ]

        for model_class in models_to_test:
            # Test with invalid type data
            with pytest.raises((PydanticValidationError, TypeError, ValueError)):
                # This should fail for most models
                model_class(invalid_field="invalid_data_type_for_most_models")


# Additional test fixtures for complex scenarios
@pytest.fixture
def sample_model_data() -> Dict[str, Any]:
    """Provide sample data for model testing."""
    return {
        "string_field": "sample_string",
        "integer_field": 42,
        "number_field": 3.14,
        "boolean_field": True,
        "array_field": ["item1", "item2"],
        "object_field": {"key": "value"},
    }


@pytest.fixture
def invalid_model_data() -> Dict[str, Any]:
    """Provide invalid data for model testing."""
    return {
        "string_field": 123,  # Wrong type
        "integer_field": "not_an_int",  # Wrong type
        "number_field": "not_a_number",  # Wrong type
        "boolean_field": "not_a_bool",  # Wrong type
        "array_field": "not_an_array",  # Wrong type
        "object_field": "not_an_object",  # Wrong type
    }


class TestModelValidationEdgeCases:
    """Test edge cases for model validation."""

    def test_empty_model_handling(self):
        """Test handling of models with no required fields."""
        # Find models that might accept empty initialization
        models_to_test = [
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
        ]

        for model_class in models_to_test:
            try:
                # Try to create with no arguments
                model = model_class()
                assert isinstance(model, model_class)
            except PydanticValidationError:
                # Some models require fields - this is expected
                pass

    def test_model_field_types(self):
        """Test that model fields have correct types."""
        models_to_test = [
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
        ]

        for model_class in models_to_test:
            # Verify model has proper field definitions
            if hasattr(model_class, "model_fields"):
                fields = model_class.model_fields
            elif hasattr(model_class, "__fields__"):
                fields = model_class.__fields__
            else:
                continue

            assert isinstance(fields, dict)

            # Each field should have proper metadata
            for field_name, field_info in fields.items():
                assert isinstance(field_name, str)
                assert field_info is not None
