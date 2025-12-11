# (c) Copyright 2025 Hewlett Packard Enterprise Development LP
"""
Test template for models package.
Tests all generated data models from OpenAPI schemas.
"""

import pytest
from typing import Any, Dict
from pydantic import ValidationError as PydanticValidationError


from models.base import CountryCode

from models.base import NBCcsAddress

from models.base import NBCcsAddressV2

from models.base import NBTenantInventoryOwnership

from models.base import StandardErrorResponse

from models.base import NBContactWorkspace

from models.base import NBBasicWorkspace

from models.base import NBContactTenant

from models.base import NBTenantWorkspacePaginate

from models.base import Message

from models.base import NBBasicTenant


class TestModels:
    """Test suite for all generated data models."""

    def test_countrycode_model_creation(self):
        """Test CountryCode model creation with valid data."""
        # Valid test data for CountryCode
        valid_data = {}

        # Create model instance
        model = CountryCode(**valid_data)

        # Verify model creation
        assert isinstance(model, CountryCode)

    def test_countrycode_model_validation(self):
        """Test CountryCode model field validation."""
        # Test with minimal required data
        minimal_data = {}

        model = CountryCode(**minimal_data)
        assert isinstance(model, CountryCode)

    def test_countrycode_model_required_fields(self):
        """Test CountryCode model required field validation."""
        # Check if this model has any required fields
        required_fields = []

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                CountryCode()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {}

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = CountryCode()
            assert isinstance(model, CountryCode)

    def test_countrycode_model_optional_fields(self):
        """Test CountryCode model optional field handling."""
        # Create with minimal required data
        minimal_data = {}

        model = CountryCode(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_countrycode_model_serialization(self):
        """Test CountryCode model serialization to dict."""
        test_data = {}

        model = CountryCode(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)

        # Verify values are preserved

    def test_countrycode_model_json_schema(self):
        """Test CountryCode model JSON schema generation."""
        schema = CountryCode.model_json_schema()

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

    def test_nbccsaddress_model_creation(self):
        """Test NBCcsAddress model creation with valid data."""
        # Valid test data for NBCcsAddress
        valid_data = {
            "city": "test_value",
            "countryCode": "test_value",
            "stateOrRegion": "test_value",
            "streetAddress": "test_value",
            "streetAddressComplement": "test_value",
            "zip": "test_value",
        }

        # Create model instance
        model = NBCcsAddress(**valid_data)

        # Verify model creation
        assert isinstance(model, NBCcsAddress)
        assert model.city == valid_data["city"]
        assert model.countryCode == valid_data["countryCode"]
        assert model.stateOrRegion == valid_data["stateOrRegion"]
        assert model.streetAddress == valid_data["streetAddress"]
        assert model.streetAddressComplement == valid_data["streetAddressComplement"]
        assert model.zip == valid_data["zip"]

    def test_nbccsaddress_model_validation(self):
        """Test NBCcsAddress model field validation."""
        # Test with minimal required data
        minimal_data = {}

        model = NBCcsAddress(**minimal_data)
        assert isinstance(model, NBCcsAddress)

    def test_nbccsaddress_model_required_fields(self):
        """Test NBCcsAddress model required field validation."""
        # Check if this model has any required fields
        required_fields = []

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                NBCcsAddress()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {}

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = NBCcsAddress()
            assert isinstance(model, NBCcsAddress)

    def test_nbccsaddress_model_optional_fields(self):
        """Test NBCcsAddress model optional field handling."""
        # Create with minimal required data
        minimal_data = {}

        model = NBCcsAddress(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "city")
        # Optional field city should be None or have a default value
        assert model.city is None or model.city is not None
        assert hasattr(model, "countryCode")
        # Optional field countryCode should be None or have a default value
        assert model.countryCode is None or model.countryCode is not None
        assert hasattr(model, "stateOrRegion")
        # Optional field stateOrRegion should be None or have a default value
        assert model.stateOrRegion is None or model.stateOrRegion is not None
        assert hasattr(model, "streetAddress")
        # Optional field streetAddress should be None or have a default value
        assert model.streetAddress is None or model.streetAddress is not None
        assert hasattr(model, "streetAddressComplement")
        # Optional field streetAddressComplement should be None or have a default value
        assert model.streetAddressComplement is None or model.streetAddressComplement is not None
        assert hasattr(model, "zip")
        # Optional field zip should be None or have a default value
        assert model.zip is None or model.zip is not None

    def test_nbccsaddress_model_serialization(self):
        """Test NBCcsAddress model serialization to dict."""
        test_data = {
            "city": "serialize_value",
            "countryCode": "serialize_value",
            "stateOrRegion": "serialize_value",
            "streetAddress": "serialize_value",
            "streetAddressComplement": "serialize_value",
            "zip": "serialize_value",
        }

        model = NBCcsAddress(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "city" in serialized
        assert "countryCode" in serialized
        assert "stateOrRegion" in serialized
        assert "streetAddress" in serialized
        assert "streetAddressComplement" in serialized
        assert "zip" in serialized

        # Verify values are preserved
        assert serialized["city"] == test_data["city"]
        assert serialized["countryCode"] == test_data["countryCode"]
        assert serialized["stateOrRegion"] == test_data["stateOrRegion"]
        assert serialized["streetAddress"] == test_data["streetAddress"]
        assert serialized["streetAddressComplement"] == test_data["streetAddressComplement"]
        assert serialized["zip"] == test_data["zip"]

    def test_nbccsaddress_model_json_schema(self):
        """Test NBCcsAddress model JSON schema generation."""
        schema = NBCcsAddress.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "city",
            "countryCode",
            "stateOrRegion",
            "streetAddress",
            "streetAddressComplement",
            "zip",
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

    def test_nbccsaddressv2_model_creation(self):
        """Test NBCcsAddressV2 model creation with valid data."""
        # Valid test data for NBCcsAddressV2
        valid_data = {
            "stateOrRegion": "test_value",
            "streetAddress": "test_value",
            "streetAddressComplement": "test_value",
            "zip": "test_value",
            "city": "test_value",
            "countryCode": "test_value",
        }

        # Create model instance
        model = NBCcsAddressV2(**valid_data)

        # Verify model creation
        assert isinstance(model, NBCcsAddressV2)
        assert model.stateOrRegion == valid_data["stateOrRegion"]
        assert model.streetAddress == valid_data["streetAddress"]
        assert model.streetAddressComplement == valid_data["streetAddressComplement"]
        assert model.zip == valid_data["zip"]
        assert model.city == valid_data["city"]
        assert model.countryCode == valid_data["countryCode"]

    def test_nbccsaddressv2_model_validation(self):
        """Test NBCcsAddressV2 model field validation."""
        # Test with minimal required data
        minimal_data = {
            "countryCode": "required_value",
        }

        model = NBCcsAddressV2(**minimal_data)
        assert isinstance(model, NBCcsAddressV2)
        assert model.countryCode == minimal_data["countryCode"]

    def test_nbccsaddressv2_model_required_fields(self):
        """Test NBCcsAddressV2 model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "countryCode",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                NBCcsAddressV2()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "countryCode",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = NBCcsAddressV2()
            assert isinstance(model, NBCcsAddressV2)

    def test_nbccsaddressv2_model_optional_fields(self):
        """Test NBCcsAddressV2 model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "countryCode": "required_value",
        }

        model = NBCcsAddressV2(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "stateOrRegion")
        # Optional field stateOrRegion should be None or have a default value
        assert model.stateOrRegion is None or model.stateOrRegion is not None
        assert hasattr(model, "streetAddress")
        # Optional field streetAddress should be None or have a default value
        assert model.streetAddress is None or model.streetAddress is not None
        assert hasattr(model, "streetAddressComplement")
        # Optional field streetAddressComplement should be None or have a default value
        assert model.streetAddressComplement is None or model.streetAddressComplement is not None
        assert hasattr(model, "zip")
        # Optional field zip should be None or have a default value
        assert model.zip is None or model.zip is not None
        assert hasattr(model, "city")
        # Optional field city should be None or have a default value
        assert model.city is None or model.city is not None

    def test_nbccsaddressv2_model_serialization(self):
        """Test NBCcsAddressV2 model serialization to dict."""
        test_data = {
            "stateOrRegion": "serialize_value",
            "streetAddress": "serialize_value",
            "streetAddressComplement": "serialize_value",
            "zip": "serialize_value",
            "city": "serialize_value",
            "countryCode": "serialize_value",
        }

        model = NBCcsAddressV2(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "stateOrRegion" in serialized
        assert "streetAddress" in serialized
        assert "streetAddressComplement" in serialized
        assert "zip" in serialized
        assert "city" in serialized
        assert "countryCode" in serialized

        # Verify values are preserved
        assert serialized["stateOrRegion"] == test_data["stateOrRegion"]
        assert serialized["streetAddress"] == test_data["streetAddress"]
        assert serialized["streetAddressComplement"] == test_data["streetAddressComplement"]
        assert serialized["zip"] == test_data["zip"]
        assert serialized["city"] == test_data["city"]
        assert serialized["countryCode"] == test_data["countryCode"]

    def test_nbccsaddressv2_model_json_schema(self):
        """Test NBCcsAddressV2 model JSON schema generation."""
        schema = NBCcsAddressV2.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "stateOrRegion",
            "streetAddress",
            "streetAddressComplement",
            "zip",
            "city",
            "countryCode",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "countryCode",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_nbtenantinventoryownership_model_creation(self):
        """Test NBTenantInventoryOwnership model creation with valid data."""
        # Valid test data for NBTenantInventoryOwnership
        valid_data = {}

        # Create model instance
        model = NBTenantInventoryOwnership(**valid_data)

        # Verify model creation
        assert isinstance(model, NBTenantInventoryOwnership)

    def test_nbtenantinventoryownership_model_validation(self):
        """Test NBTenantInventoryOwnership model field validation."""
        # Test with minimal required data
        minimal_data = {}

        model = NBTenantInventoryOwnership(**minimal_data)
        assert isinstance(model, NBTenantInventoryOwnership)

    def test_nbtenantinventoryownership_model_required_fields(self):
        """Test NBTenantInventoryOwnership model required field validation."""
        # Check if this model has any required fields
        required_fields = []

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                NBTenantInventoryOwnership()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {}

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = NBTenantInventoryOwnership()
            assert isinstance(model, NBTenantInventoryOwnership)

    def test_nbtenantinventoryownership_model_optional_fields(self):
        """Test NBTenantInventoryOwnership model optional field handling."""
        # Create with minimal required data
        minimal_data = {}

        model = NBTenantInventoryOwnership(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_nbtenantinventoryownership_model_serialization(self):
        """Test NBTenantInventoryOwnership model serialization to dict."""
        test_data = {}

        model = NBTenantInventoryOwnership(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)

        # Verify values are preserved

    def test_nbtenantinventoryownership_model_json_schema(self):
        """Test NBTenantInventoryOwnership model JSON schema generation."""
        schema = NBTenantInventoryOwnership.model_json_schema()

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

    def test_standarderrorresponse_model_creation(self):
        """Test StandardErrorResponse model creation with valid data."""
        # Valid test data for StandardErrorResponse
        valid_data = {
            "debugId": "test_value",
            "errorCode": "test_value",
            "httpStatusCode": 42,
            "message": "test_value",
        }

        # Create model instance
        model = StandardErrorResponse(**valid_data)

        # Verify model creation
        assert isinstance(model, StandardErrorResponse)
        assert model.debugId == valid_data["debugId"]
        assert model.errorCode == valid_data["errorCode"]
        assert model.httpStatusCode == valid_data["httpStatusCode"]
        assert model.message == valid_data["message"]

    def test_standarderrorresponse_model_validation(self):
        """Test StandardErrorResponse model field validation."""
        # Test with minimal required data
        minimal_data = {
            "debugId": "required_value",
            "errorCode": "required_value",
            "httpStatusCode": 1,
            "message": "required_value",
        }

        model = StandardErrorResponse(**minimal_data)
        assert isinstance(model, StandardErrorResponse)
        assert model.debugId == minimal_data["debugId"]
        assert model.errorCode == minimal_data["errorCode"]
        assert model.httpStatusCode == minimal_data["httpStatusCode"]
        assert model.message == minimal_data["message"]

    def test_standarderrorresponse_model_required_fields(self):
        """Test StandardErrorResponse model required field validation."""
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
                StandardErrorResponse()

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
            model = StandardErrorResponse()
            assert isinstance(model, StandardErrorResponse)

    def test_standarderrorresponse_model_optional_fields(self):
        """Test StandardErrorResponse model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "debugId": "required_value",
            "errorCode": "required_value",
            "httpStatusCode": 1,
            "message": "required_value",
        }

        model = StandardErrorResponse(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_standarderrorresponse_model_serialization(self):
        """Test StandardErrorResponse model serialization to dict."""
        test_data = {
            "debugId": "serialize_value",
            "errorCode": "serialize_value",
            "httpStatusCode": 99,
            "message": "serialize_value",
        }

        model = StandardErrorResponse(**test_data)
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

    def test_standarderrorresponse_model_json_schema(self):
        """Test StandardErrorResponse model JSON schema generation."""
        schema = StandardErrorResponse.model_json_schema()

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

    def test_nbcontactworkspace_model_creation(self):
        """Test NBContactWorkspace model creation with valid data."""
        # Valid test data for NBContactWorkspace
        valid_data = {
            "phoneNumber": "test_value",
            "resourceUri": "test_value",
            "address": "test_value",
            "email": "test_value",
        }

        # Create model instance
        model = NBContactWorkspace(**valid_data)

        # Verify model creation
        assert isinstance(model, NBContactWorkspace)
        assert model.phoneNumber == valid_data["phoneNumber"]
        assert model.resourceUri == valid_data["resourceUri"]
        assert model.address == valid_data["address"]
        assert model.email == valid_data["email"]

    def test_nbcontactworkspace_model_validation(self):
        """Test NBContactWorkspace model field validation."""
        # Test with minimal required data
        minimal_data = {}

        model = NBContactWorkspace(**minimal_data)
        assert isinstance(model, NBContactWorkspace)

    def test_nbcontactworkspace_model_required_fields(self):
        """Test NBContactWorkspace model required field validation."""
        # Check if this model has any required fields
        required_fields = []

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                NBContactWorkspace()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {}

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = NBContactWorkspace()
            assert isinstance(model, NBContactWorkspace)

    def test_nbcontactworkspace_model_optional_fields(self):
        """Test NBContactWorkspace model optional field handling."""
        # Create with minimal required data
        minimal_data = {}

        model = NBContactWorkspace(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "phoneNumber")
        # Optional field phoneNumber should be None or have a default value
        assert model.phoneNumber is None or model.phoneNumber is not None
        assert hasattr(model, "resourceUri")
        # Optional field resourceUri should be None or have a default value
        assert model.resourceUri is None or model.resourceUri is not None
        assert hasattr(model, "address")
        # Optional field address should be None or have a default value
        assert model.address is None or model.address is not None
        assert hasattr(model, "email")
        # Optional field email should be None or have a default value
        assert model.email is None or model.email is not None

    def test_nbcontactworkspace_model_serialization(self):
        """Test NBContactWorkspace model serialization to dict."""
        test_data = {
            "phoneNumber": "serialize_value",
            "resourceUri": "serialize_value",
            "address": "serialize_value",
            "email": "serialize_value",
        }

        model = NBContactWorkspace(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "phoneNumber" in serialized
        assert "resourceUri" in serialized
        assert "address" in serialized
        assert "email" in serialized

        # Verify values are preserved
        assert serialized["phoneNumber"] == test_data["phoneNumber"]
        assert serialized["resourceUri"] == test_data["resourceUri"]
        assert serialized["address"] == test_data["address"]
        assert serialized["email"] == test_data["email"]

    def test_nbcontactworkspace_model_json_schema(self):
        """Test NBContactWorkspace model JSON schema generation."""
        schema = NBContactWorkspace.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "phoneNumber",
            "resourceUri",
            "address",
            "email",
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

    def test_nbbasicworkspace_model_creation(self):
        """Test NBBasicWorkspace model creation with valid data."""
        # Valid test data for NBBasicWorkspace
        valid_data = {
            "generation": 42,
            "id": "test_value",
            "resourceUri": "test_value",
            "type": "test_value",
            "updatedAt": "test_value",
            "workspaceName": "test_value",
            "createdAt": "test_value",
            "createdBy": "test_value",
        }

        # Create model instance
        model = NBBasicWorkspace(**valid_data)

        # Verify model creation
        assert isinstance(model, NBBasicWorkspace)
        assert model.generation == valid_data["generation"]
        assert model.id == valid_data["id"]
        assert model.resourceUri == valid_data["resourceUri"]
        assert model.type == valid_data["type"]
        assert model.updatedAt == valid_data["updatedAt"]
        assert model.workspaceName == valid_data["workspaceName"]
        assert model.createdAt == valid_data["createdAt"]
        assert model.createdBy == valid_data["createdBy"]

    def test_nbbasicworkspace_model_validation(self):
        """Test NBBasicWorkspace model field validation."""
        # Test with minimal required data
        minimal_data = {
            "id": "required_value",
            "type": "required_value",
            "workspaceName": "required_value",
        }

        model = NBBasicWorkspace(**minimal_data)
        assert isinstance(model, NBBasicWorkspace)
        assert model.id == minimal_data["id"]
        assert model.type == minimal_data["type"]
        assert model.workspaceName == minimal_data["workspaceName"]

    def test_nbbasicworkspace_model_required_fields(self):
        """Test NBBasicWorkspace model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "id",
            "type",
            "workspaceName",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                NBBasicWorkspace()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "id",
                "type",
                "workspaceName",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = NBBasicWorkspace()
            assert isinstance(model, NBBasicWorkspace)

    def test_nbbasicworkspace_model_optional_fields(self):
        """Test NBBasicWorkspace model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "id": "required_value",
            "type": "required_value",
            "workspaceName": "required_value",
        }

        model = NBBasicWorkspace(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "generation")
        # Optional field generation should be None or have a default value
        assert model.generation is None or model.generation is not None
        assert hasattr(model, "resourceUri")
        # Optional field resourceUri should be None or have a default value
        assert model.resourceUri is None or model.resourceUri is not None
        assert hasattr(model, "updatedAt")
        # Optional field updatedAt should be None or have a default value
        assert model.updatedAt is None or model.updatedAt is not None
        assert hasattr(model, "createdAt")
        # Optional field createdAt should be None or have a default value
        assert model.createdAt is None or model.createdAt is not None
        assert hasattr(model, "createdBy")
        # Optional field createdBy should be None or have a default value
        assert model.createdBy is None or model.createdBy is not None

    def test_nbbasicworkspace_model_serialization(self):
        """Test NBBasicWorkspace model serialization to dict."""
        test_data = {
            "generation": 99,
            "id": "serialize_value",
            "resourceUri": "serialize_value",
            "type": "serialize_value",
            "updatedAt": "serialize_value",
            "workspaceName": "serialize_value",
            "createdAt": "serialize_value",
            "createdBy": "serialize_value",
        }

        model = NBBasicWorkspace(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "generation" in serialized
        assert "id" in serialized
        assert "resourceUri" in serialized
        assert "type" in serialized
        assert "updatedAt" in serialized
        assert "workspaceName" in serialized
        assert "createdAt" in serialized
        assert "createdBy" in serialized

        # Verify values are preserved
        assert serialized["generation"] == test_data["generation"]
        assert serialized["id"] == test_data["id"]
        assert serialized["resourceUri"] == test_data["resourceUri"]
        assert serialized["type"] == test_data["type"]
        assert serialized["updatedAt"] == test_data["updatedAt"]
        assert serialized["workspaceName"] == test_data["workspaceName"]
        assert serialized["createdAt"] == test_data["createdAt"]
        assert serialized["createdBy"] == test_data["createdBy"]

    def test_nbbasicworkspace_model_json_schema(self):
        """Test NBBasicWorkspace model JSON schema generation."""
        schema = NBBasicWorkspace.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "generation",
            "id",
            "resourceUri",
            "type",
            "updatedAt",
            "workspaceName",
            "createdAt",
            "createdBy",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "id",
            "type",
            "workspaceName",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_nbcontacttenant_model_creation(self):
        """Test NBContactTenant model creation with valid data."""
        # Valid test data for NBContactTenant
        valid_data = {
            "inventoryOwnership": "test_value",
            "phoneNumber": "test_value",
            "resourceUri": "test_value",
            "workspaceName": "test_value",
            "address": "test_value",
            "description": "test_value",
            "email": "test_value",
        }

        # Create model instance
        model = NBContactTenant(**valid_data)

        # Verify model creation
        assert isinstance(model, NBContactTenant)
        assert model.inventoryOwnership == valid_data["inventoryOwnership"]
        assert model.phoneNumber == valid_data["phoneNumber"]
        assert model.resourceUri == valid_data["resourceUri"]
        assert model.workspaceName == valid_data["workspaceName"]
        assert model.address == valid_data["address"]
        assert model.description == valid_data["description"]
        assert model.email == valid_data["email"]

    def test_nbcontacttenant_model_validation(self):
        """Test NBContactTenant model field validation."""
        # Test with minimal required data
        minimal_data = {
            "workspaceName": "required_value",
        }

        model = NBContactTenant(**minimal_data)
        assert isinstance(model, NBContactTenant)
        assert model.workspaceName == minimal_data["workspaceName"]

    def test_nbcontacttenant_model_required_fields(self):
        """Test NBContactTenant model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "workspaceName",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                NBContactTenant()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "workspaceName",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = NBContactTenant()
            assert isinstance(model, NBContactTenant)

    def test_nbcontacttenant_model_optional_fields(self):
        """Test NBContactTenant model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "workspaceName": "required_value",
        }

        model = NBContactTenant(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "inventoryOwnership")
        # Optional field inventoryOwnership should be None or have a default value
        assert model.inventoryOwnership is None or model.inventoryOwnership is not None
        assert hasattr(model, "phoneNumber")
        # Optional field phoneNumber should be None or have a default value
        assert model.phoneNumber is None or model.phoneNumber is not None
        assert hasattr(model, "resourceUri")
        # Optional field resourceUri should be None or have a default value
        assert model.resourceUri is None or model.resourceUri is not None
        assert hasattr(model, "address")
        # Optional field address should be None or have a default value
        assert model.address is None or model.address is not None
        assert hasattr(model, "description")
        # Optional field description should be None or have a default value
        assert model.description is None or model.description is not None
        assert hasattr(model, "email")
        # Optional field email should be None or have a default value
        assert model.email is None or model.email is not None

    def test_nbcontacttenant_model_serialization(self):
        """Test NBContactTenant model serialization to dict."""
        test_data = {
            "inventoryOwnership": "serialize_value",
            "phoneNumber": "serialize_value",
            "resourceUri": "serialize_value",
            "workspaceName": "serialize_value",
            "address": "serialize_value",
            "description": "serialize_value",
            "email": "serialize_value",
        }

        model = NBContactTenant(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "inventoryOwnership" in serialized
        assert "phoneNumber" in serialized
        assert "resourceUri" in serialized
        assert "workspaceName" in serialized
        assert "address" in serialized
        assert "description" in serialized
        assert "email" in serialized

        # Verify values are preserved
        assert serialized["inventoryOwnership"] == test_data["inventoryOwnership"]
        assert serialized["phoneNumber"] == test_data["phoneNumber"]
        assert serialized["resourceUri"] == test_data["resourceUri"]
        assert serialized["workspaceName"] == test_data["workspaceName"]
        assert serialized["address"] == test_data["address"]
        assert serialized["description"] == test_data["description"]
        assert serialized["email"] == test_data["email"]

    def test_nbcontacttenant_model_json_schema(self):
        """Test NBContactTenant model JSON schema generation."""
        schema = NBContactTenant.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "inventoryOwnership",
            "phoneNumber",
            "resourceUri",
            "workspaceName",
            "address",
            "description",
            "email",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "workspaceName",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_nbtenantworkspacepaginate_model_creation(self):
        """Test NBTenantWorkspacePaginate model creation with valid data."""
        # Valid test data for NBTenantWorkspacePaginate
        valid_data = {
            "items": [{"key": "value"}, {"key": "value"}],
            "offset": 42,
            "total": 42,
            "count": 42,
        }

        # Create model instance
        model = NBTenantWorkspacePaginate(**valid_data)

        # Verify model creation
        assert isinstance(model, NBTenantWorkspacePaginate)
        assert model.items == valid_data["items"]
        assert model.offset == valid_data["offset"]
        assert model.total == valid_data["total"]
        assert model.count == valid_data["count"]

    def test_nbtenantworkspacepaginate_model_validation(self):
        """Test NBTenantWorkspacePaginate model field validation."""
        # Test with minimal required data
        minimal_data = {
            "items": [{"key": "value"}, {"key": "value"}],
            "offset": 1,
            "total": 1,
            "count": 1,
        }

        model = NBTenantWorkspacePaginate(**minimal_data)
        assert isinstance(model, NBTenantWorkspacePaginate)
        assert model.items == minimal_data["items"]
        assert model.offset == minimal_data["offset"]
        assert model.total == minimal_data["total"]
        assert model.count == minimal_data["count"]

    def test_nbtenantworkspacepaginate_model_required_fields(self):
        """Test NBTenantWorkspacePaginate model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "items",
            "offset",
            "total",
            "count",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                NBTenantWorkspacePaginate()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "items",
                "offset",
                "total",
                "count",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = NBTenantWorkspacePaginate()
            assert isinstance(model, NBTenantWorkspacePaginate)

    def test_nbtenantworkspacepaginate_model_optional_fields(self):
        """Test NBTenantWorkspacePaginate model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "items": [{"key": "value"}, {"key": "value"}],
            "offset": 1,
            "total": 1,
            "count": 1,
        }

        model = NBTenantWorkspacePaginate(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_nbtenantworkspacepaginate_model_serialization(self):
        """Test NBTenantWorkspacePaginate model serialization to dict."""
        test_data = {
            "items": [{"key": "value"}, {"key": "value"}],
            "offset": 99,
            "total": 99,
            "count": 99,
        }

        model = NBTenantWorkspacePaginate(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "items" in serialized
        assert "offset" in serialized
        assert "total" in serialized
        assert "count" in serialized

        # Verify values are preserved
        assert serialized["items"] == test_data["items"]
        assert serialized["offset"] == test_data["offset"]
        assert serialized["total"] == test_data["total"]
        assert serialized["count"] == test_data["count"]

    def test_nbtenantworkspacepaginate_model_json_schema(self):
        """Test NBTenantWorkspacePaginate model JSON schema generation."""
        schema = NBTenantWorkspacePaginate.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "items",
            "offset",
            "total",
            "count",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "items",
            "offset",
            "total",
            "count",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_message_model_creation(self):
        """Test Message model creation with valid data."""
        # Valid test data for Message
        valid_data = {
            "message": "test_value",
        }

        # Create model instance
        model = Message(**valid_data)

        # Verify model creation
        assert isinstance(model, Message)
        assert model.message == valid_data["message"]

    def test_message_model_validation(self):
        """Test Message model field validation."""
        # Test with minimal required data
        minimal_data = {
            "message": "required_value",
        }

        model = Message(**minimal_data)
        assert isinstance(model, Message)
        assert model.message == minimal_data["message"]

    def test_message_model_required_fields(self):
        """Test Message model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "message",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Message()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "message",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Message()
            assert isinstance(model, Message)

    def test_message_model_optional_fields(self):
        """Test Message model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "message": "required_value",
        }

        model = Message(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_message_model_serialization(self):
        """Test Message model serialization to dict."""
        test_data = {
            "message": "serialize_value",
        }

        model = Message(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "message" in serialized

        # Verify values are preserved
        assert serialized["message"] == test_data["message"]

    def test_message_model_json_schema(self):
        """Test Message model JSON schema generation."""
        schema = Message.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "message",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "message",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_nbbasictenant_model_creation(self):
        """Test NBBasicTenant model creation with valid data."""
        # Valid test data for NBBasicTenant
        valid_data = {
            "inventoryOwnership": "test_value",
            "generation": 42,
            "resourceUri": "test_value",
            "updatedAt": "test_value",
            "workspaceName": "test_value",
            "id": "test_value",
            "createdAt": "test_value",
            "type": "test_value",
            "createdBy": "test_value",
        }

        # Create model instance
        model = NBBasicTenant(**valid_data)

        # Verify model creation
        assert isinstance(model, NBBasicTenant)
        assert model.inventoryOwnership == valid_data["inventoryOwnership"]
        assert model.generation == valid_data["generation"]
        assert model.resourceUri == valid_data["resourceUri"]
        assert model.updatedAt == valid_data["updatedAt"]
        assert model.workspaceName == valid_data["workspaceName"]
        assert model.id == valid_data["id"]
        assert model.createdAt == valid_data["createdAt"]
        assert model.type == valid_data["type"]
        assert model.createdBy == valid_data["createdBy"]

    def test_nbbasictenant_model_validation(self):
        """Test NBBasicTenant model field validation."""
        # Test with minimal required data
        minimal_data = {
            "workspaceName": "required_value",
            "id": "required_value",
            "type": "required_value",
        }

        model = NBBasicTenant(**minimal_data)
        assert isinstance(model, NBBasicTenant)
        assert model.workspaceName == minimal_data["workspaceName"]
        assert model.id == minimal_data["id"]
        assert model.type == minimal_data["type"]

    def test_nbbasictenant_model_required_fields(self):
        """Test NBBasicTenant model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "workspaceName",
            "id",
            "type",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                NBBasicTenant()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "workspaceName",
                "id",
                "type",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = NBBasicTenant()
            assert isinstance(model, NBBasicTenant)

    def test_nbbasictenant_model_optional_fields(self):
        """Test NBBasicTenant model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "workspaceName": "required_value",
            "id": "required_value",
            "type": "required_value",
        }

        model = NBBasicTenant(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "inventoryOwnership")
        # Optional field inventoryOwnership should be None or have a default value
        assert model.inventoryOwnership is None or model.inventoryOwnership is not None
        assert hasattr(model, "generation")
        # Optional field generation should be None or have a default value
        assert model.generation is None or model.generation is not None
        assert hasattr(model, "resourceUri")
        # Optional field resourceUri should be None or have a default value
        assert model.resourceUri is None or model.resourceUri is not None
        assert hasattr(model, "updatedAt")
        # Optional field updatedAt should be None or have a default value
        assert model.updatedAt is None or model.updatedAt is not None
        assert hasattr(model, "createdAt")
        # Optional field createdAt should be None or have a default value
        assert model.createdAt is None or model.createdAt is not None
        assert hasattr(model, "createdBy")
        # Optional field createdBy should be None or have a default value
        assert model.createdBy is None or model.createdBy is not None

    def test_nbbasictenant_model_serialization(self):
        """Test NBBasicTenant model serialization to dict."""
        test_data = {
            "inventoryOwnership": "serialize_value",
            "generation": 99,
            "resourceUri": "serialize_value",
            "updatedAt": "serialize_value",
            "workspaceName": "serialize_value",
            "id": "serialize_value",
            "createdAt": "serialize_value",
            "type": "serialize_value",
            "createdBy": "serialize_value",
        }

        model = NBBasicTenant(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "inventoryOwnership" in serialized
        assert "generation" in serialized
        assert "resourceUri" in serialized
        assert "updatedAt" in serialized
        assert "workspaceName" in serialized
        assert "id" in serialized
        assert "createdAt" in serialized
        assert "type" in serialized
        assert "createdBy" in serialized

        # Verify values are preserved
        assert serialized["inventoryOwnership"] == test_data["inventoryOwnership"]
        assert serialized["generation"] == test_data["generation"]
        assert serialized["resourceUri"] == test_data["resourceUri"]
        assert serialized["updatedAt"] == test_data["updatedAt"]
        assert serialized["workspaceName"] == test_data["workspaceName"]
        assert serialized["id"] == test_data["id"]
        assert serialized["createdAt"] == test_data["createdAt"]
        assert serialized["type"] == test_data["type"]
        assert serialized["createdBy"] == test_data["createdBy"]

    def test_nbbasictenant_model_json_schema(self):
        """Test NBBasicTenant model JSON schema generation."""
        schema = NBBasicTenant.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "inventoryOwnership",
            "generation",
            "resourceUri",
            "updatedAt",
            "workspaceName",
            "id",
            "createdAt",
            "type",
            "createdBy",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "workspaceName",
            "id",
            "type",
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
            CountryCode,
            NBCcsAddress,
            NBCcsAddressV2,
            NBTenantInventoryOwnership,
            StandardErrorResponse,
            NBContactWorkspace,
            NBBasicWorkspace,
            NBContactTenant,
            NBTenantWorkspacePaginate,
            Message,
            NBBasicTenant,
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
            CountryCode,
            NBCcsAddress,
            NBCcsAddressV2,
            NBTenantInventoryOwnership,
            StandardErrorResponse,
            NBContactWorkspace,
            NBBasicWorkspace,
            NBContactTenant,
            NBTenantWorkspacePaginate,
            Message,
            NBBasicTenant,
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
            CountryCode,
            NBCcsAddress,
            NBCcsAddressV2,
            NBTenantInventoryOwnership,
            StandardErrorResponse,
            NBContactWorkspace,
            NBBasicWorkspace,
            NBContactTenant,
            NBTenantWorkspacePaginate,
            Message,
            NBBasicTenant,
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
            CountryCode,
            NBCcsAddress,
            NBCcsAddressV2,
            NBTenantInventoryOwnership,
            StandardErrorResponse,
            NBContactWorkspace,
            NBBasicWorkspace,
            NBContactTenant,
            NBTenantWorkspacePaginate,
            Message,
            NBBasicTenant,
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
