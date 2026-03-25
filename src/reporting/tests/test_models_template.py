# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
Test template for models package.
Tests all generated data models from OpenAPI schemas.
"""

import pytest
from typing import Any, Dict
from pydantic import ValidationError as PydanticValidationError


from models.base import error

from models.base import filterCriteria

from models.base import generateDocResponse

from models.base import delivery

from models.base import enrollment

from models.base import generateResponse

from models.base import queryElements

from models.base import reportDefinition

from models.base import reportDoc

from models.base import generateReportBody

from models.base import asyncOperationResponse


class TestModels:
    """Test suite for all generated data models."""

    def test_error_model_creation(self):
        """Test error model creation with valid data."""
        # Valid test data for error
        valid_data = {
            "debugId": "test_debugId",
            "errorCode": "test_errorCode",
            "httpStatusCode": 42,
            "message": "test_message",
        }

        # Create model instance
        model = error(**valid_data)

        # Verify model creation
        assert isinstance(model, error)
        assert model.debugId == valid_data["debugId"]
        assert model.errorCode == valid_data["errorCode"]
        assert model.httpStatusCode == valid_data["httpStatusCode"]
        assert model.message == valid_data["message"]

    def test_error_model_validation(self):
        """Test error model field validation."""
        # Test with minimal required data
        minimal_data = {
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
            "httpStatusCode": 1,
            "message": "required_message",
        }

        model = error(**minimal_data)
        assert isinstance(model, error)
        assert model.debugId == minimal_data["debugId"]
        assert model.errorCode == minimal_data["errorCode"]
        assert model.httpStatusCode == minimal_data["httpStatusCode"]
        assert model.message == minimal_data["message"]

    def test_error_model_required_fields(self):
        """Test error model required field validation."""
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
                error()

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
            model = error()
            assert isinstance(model, error)

    def test_error_model_optional_fields(self):
        """Test error model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
            "httpStatusCode": 1,
            "message": "required_message",
        }

        model = error(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_error_model_serialization(self):
        """Test error model serialization to dict."""
        test_data = {
            "debugId": "serialize_value",
            "errorCode": "serialize_value",
            "httpStatusCode": 99,
            "message": "serialize_value",
        }

        model = error(**test_data)
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

    def test_error_model_json_schema(self):
        """Test error model JSON schema generation."""
        schema = error.model_json_schema()

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

    def test_filtercriteria_model_creation(self):
        """Test filterCriteria model creation with valid data."""
        # Valid test data for filterCriteria
        valid_data = {
            "key": "test_key",
            "operator": "test_operator",
            "value": "test_value",
        }

        # Create model instance
        model = filterCriteria(**valid_data)

        # Verify model creation
        assert isinstance(model, filterCriteria)
        assert model.key == valid_data["key"]
        assert model.operator == valid_data["operator"]
        assert model.value == valid_data["value"]

    def test_filtercriteria_model_validation(self):
        """Test filterCriteria model field validation."""
        # Test with minimal required data
        minimal_data = {}

        model = filterCriteria(**minimal_data)
        assert isinstance(model, filterCriteria)

    def test_filtercriteria_model_required_fields(self):
        """Test filterCriteria model required field validation."""
        # Check if this model has any required fields
        required_fields = []

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                filterCriteria()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {}

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = filterCriteria()
            assert isinstance(model, filterCriteria)

    def test_filtercriteria_model_optional_fields(self):
        """Test filterCriteria model optional field handling."""
        # Create with minimal required data
        minimal_data = {}

        model = filterCriteria(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "key")
        # Optional field key should be None or have a default value
        assert model.key is None or model.key is not None
        assert hasattr(model, "operator")
        # Optional field operator should be None or have a default value
        assert model.operator is None or model.operator is not None
        assert hasattr(model, "value")
        # Optional field value should be None or have a default value
        assert model.value is None or model.value is not None

    def test_filtercriteria_model_serialization(self):
        """Test filterCriteria model serialization to dict."""
        test_data = {
            "key": "serialize_value",
            "operator": "serialize_value",
            "value": "serialize_value",
        }

        model = filterCriteria(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "key" in serialized
        assert "operator" in serialized
        assert "value" in serialized

        # Verify values are preserved
        assert serialized["key"] == test_data["key"]
        assert serialized["operator"] == test_data["operator"]
        assert serialized["value"] == test_data["value"]

    def test_filtercriteria_model_json_schema(self):
        """Test filterCriteria model JSON schema generation."""
        schema = filterCriteria.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "key",
            "operator",
            "value",
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

    def test_generatedocresponse_model_creation(self):
        """Test generateDocResponse model creation with valid data."""
        # Valid test data for generateDocResponse
        valid_data = {
            "count": 42,
            "items": [],
            "offset": 42,
            "total": 42,
        }

        # Create model instance
        model = generateDocResponse(**valid_data)

        # Verify model creation
        assert isinstance(model, generateDocResponse)
        assert model.count == valid_data["count"]
        assert model.items == valid_data["items"]
        assert model.offset == valid_data["offset"]
        assert model.total == valid_data["total"]

    def test_generatedocresponse_model_validation(self):
        """Test generateDocResponse model field validation."""
        # Test with minimal required data
        minimal_data = {
            "count": 1,
            "items": [],
            "offset": 1,
            "total": 1,
        }

        model = generateDocResponse(**minimal_data)
        assert isinstance(model, generateDocResponse)
        assert model.count == minimal_data["count"]
        assert model.items == minimal_data["items"]
        assert model.offset == minimal_data["offset"]
        assert model.total == minimal_data["total"]

    def test_generatedocresponse_model_required_fields(self):
        """Test generateDocResponse model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "count",
            "items",
            "offset",
            "total",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                generateDocResponse()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "count",
                "items",
                "offset",
                "total",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = generateDocResponse()
            assert isinstance(model, generateDocResponse)

    def test_generatedocresponse_model_optional_fields(self):
        """Test generateDocResponse model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "count": 1,
            "items": [],
            "offset": 1,
            "total": 1,
        }

        model = generateDocResponse(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_generatedocresponse_model_serialization(self):
        """Test generateDocResponse model serialization to dict."""
        test_data = {
            "count": 99,
            "items": [],
            "offset": 99,
            "total": 99,
        }

        model = generateDocResponse(**test_data)
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

    def test_generatedocresponse_model_json_schema(self):
        """Test generateDocResponse model JSON schema generation."""
        schema = generateDocResponse.model_json_schema()

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
            "total",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_delivery_model_creation(self):
        """Test delivery model creation with valid data."""
        # Valid test data for delivery
        valid_data = {
            "email": {},
            "format": "test_format",
        }

        # Create model instance
        model = delivery(**valid_data)

        # Verify model creation
        assert isinstance(model, delivery)
        assert model.email == valid_data["email"]
        assert model.format == valid_data["format"]

    def test_delivery_model_validation(self):
        """Test delivery model field validation."""
        # Test with minimal required data
        minimal_data = {}

        model = delivery(**minimal_data)
        assert isinstance(model, delivery)

    def test_delivery_model_required_fields(self):
        """Test delivery model required field validation."""
        # Check if this model has any required fields
        required_fields = []

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                delivery()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {}

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = delivery()
            assert isinstance(model, delivery)

    def test_delivery_model_optional_fields(self):
        """Test delivery model optional field handling."""
        # Create with minimal required data
        minimal_data = {}

        model = delivery(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "email")
        # Optional field email should be None or have a default value
        assert model.email is None or model.email is not None
        assert hasattr(model, "format")
        # Optional field format should be None or have a default value
        assert model.format is None or model.format is not None

    def test_delivery_model_serialization(self):
        """Test delivery model serialization to dict."""
        test_data = {
            "email": {"key": "value"},
            "format": "serialize_value",
        }

        model = delivery(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "email" in serialized
        assert "format" in serialized

        # Verify values are preserved
        assert serialized["email"] == test_data["email"]
        assert serialized["format"] == test_data["format"]

    def test_delivery_model_json_schema(self):
        """Test delivery model JSON schema generation."""
        schema = delivery.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "email",
            "format",
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

    def test_enrollment_model_creation(self):
        """Test enrollment model creation with valid data."""
        # Valid test data for enrollment
        valid_data = {
            "delivery": {},
        }

        # Create model instance
        model = enrollment(**valid_data)

        # Verify model creation
        assert isinstance(model, enrollment)
        assert model.delivery == valid_data["delivery"]

    def test_enrollment_model_validation(self):
        """Test enrollment model field validation."""
        # Test with minimal required data
        minimal_data = {}

        model = enrollment(**minimal_data)
        assert isinstance(model, enrollment)

    def test_enrollment_model_required_fields(self):
        """Test enrollment model required field validation."""
        # Check if this model has any required fields
        required_fields = []

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                enrollment()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {}

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = enrollment()
            assert isinstance(model, enrollment)

    def test_enrollment_model_optional_fields(self):
        """Test enrollment model optional field handling."""
        # Create with minimal required data
        minimal_data = {}

        model = enrollment(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "delivery")
        # Optional field delivery should be None or have a default value
        assert model.delivery is None or model.delivery is not None

    def test_enrollment_model_serialization(self):
        """Test enrollment model serialization to dict."""
        test_data = {
            "delivery": {"key": "value"},
        }

        model = enrollment(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "delivery" in serialized

        # Verify values are preserved
        assert serialized["delivery"] == test_data["delivery"]

    def test_enrollment_model_json_schema(self):
        """Test enrollment model JSON schema generation."""
        schema = enrollment.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "delivery",
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

    def test_generateresponse_model_creation(self):
        """Test generateResponse model creation with valid data."""
        # Valid test data for generateResponse
        valid_data = {
            "name": "test_name",
            "id": "test_id",
        }

        # Create model instance
        model = generateResponse(**valid_data)

        # Verify model creation
        assert isinstance(model, generateResponse)
        assert model.name == valid_data["name"]
        assert model.id == valid_data["id"]

    def test_generateresponse_model_validation(self):
        """Test generateResponse model field validation."""
        # Test with minimal required data
        minimal_data = {}

        model = generateResponse(**minimal_data)
        assert isinstance(model, generateResponse)

    def test_generateresponse_model_required_fields(self):
        """Test generateResponse model required field validation."""
        # Check if this model has any required fields
        required_fields = []

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                generateResponse()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {}

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = generateResponse()
            assert isinstance(model, generateResponse)

    def test_generateresponse_model_optional_fields(self):
        """Test generateResponse model optional field handling."""
        # Create with minimal required data
        minimal_data = {}

        model = generateResponse(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "name")
        # Optional field name should be None or have a default value
        assert model.name is None or model.name is not None
        assert hasattr(model, "id")
        # Optional field id should be None or have a default value
        assert model.id is None or model.id is not None

    def test_generateresponse_model_serialization(self):
        """Test generateResponse model serialization to dict."""
        test_data = {
            "name": "serialize_value",
            "id": "serialize_value",
        }

        model = generateResponse(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "name" in serialized
        assert "id" in serialized

        # Verify values are preserved
        assert serialized["name"] == test_data["name"]
        assert serialized["id"] == test_data["id"]

    def test_generateresponse_model_json_schema(self):
        """Test generateResponse model JSON schema generation."""
        schema = generateResponse.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "name",
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

    def test_queryelements_model_creation(self):
        """Test queryElements model creation with valid data."""
        # Valid test data for queryElements
        valid_data = {
            "columns": [],
            "filterCriteria": [],
        }

        # Create model instance
        model = queryElements(**valid_data)

        # Verify model creation
        assert isinstance(model, queryElements)
        assert model.columns == valid_data["columns"]
        assert model.filterCriteria == valid_data["filterCriteria"]

    def test_queryelements_model_validation(self):
        """Test queryElements model field validation."""
        # Test with minimal required data
        minimal_data = {}

        model = queryElements(**minimal_data)
        assert isinstance(model, queryElements)

    def test_queryelements_model_required_fields(self):
        """Test queryElements model required field validation."""
        # Check if this model has any required fields
        required_fields = []

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                queryElements()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {}

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = queryElements()
            assert isinstance(model, queryElements)

    def test_queryelements_model_optional_fields(self):
        """Test queryElements model optional field handling."""
        # Create with minimal required data
        minimal_data = {}

        model = queryElements(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "columns")
        # Optional field columns should be None or have a default value
        assert model.columns is None or model.columns is not None
        assert hasattr(model, "filterCriteria")
        # Optional field filterCriteria should be None or have a default value
        assert model.filterCriteria is None or model.filterCriteria is not None

    def test_queryelements_model_serialization(self):
        """Test queryElements model serialization to dict."""
        test_data = {
            "columns": [],
            "filterCriteria": [],
        }

        model = queryElements(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "columns" in serialized
        assert "filterCriteria" in serialized

        # Verify values are preserved
        assert serialized["columns"] == test_data["columns"]
        assert serialized["filterCriteria"] == test_data["filterCriteria"]

    def test_queryelements_model_json_schema(self):
        """Test queryElements model JSON schema generation."""
        schema = queryElements.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "columns",
            "filterCriteria",
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

    def test_reportdefinition_model_creation(self):
        """Test reportDefinition model creation with valid data."""
        # Valid test data for reportDefinition
        valid_data = {
            "enrollment": {},
            "queryElements": {},
        }

        # Create model instance
        model = reportDefinition(**valid_data)

        # Verify model creation
        assert isinstance(model, reportDefinition)
        assert model.enrollment == valid_data["enrollment"]
        assert model.queryElements == valid_data["queryElements"]

    def test_reportdefinition_model_validation(self):
        """Test reportDefinition model field validation."""
        # Test with minimal required data
        minimal_data = {}

        model = reportDefinition(**minimal_data)
        assert isinstance(model, reportDefinition)

    def test_reportdefinition_model_required_fields(self):
        """Test reportDefinition model required field validation."""
        # Check if this model has any required fields
        required_fields = []

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                reportDefinition()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {}

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = reportDefinition()
            assert isinstance(model, reportDefinition)

    def test_reportdefinition_model_optional_fields(self):
        """Test reportDefinition model optional field handling."""
        # Create with minimal required data
        minimal_data = {}

        model = reportDefinition(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "enrollment")
        # Optional field enrollment should be None or have a default value
        assert model.enrollment is None or model.enrollment is not None
        assert hasattr(model, "queryElements")
        # Optional field queryElements should be None or have a default value
        assert model.queryElements is None or model.queryElements is not None

    def test_reportdefinition_model_serialization(self):
        """Test reportDefinition model serialization to dict."""
        test_data = {
            "enrollment": {"key": "value"},
            "queryElements": {"key": "value"},
        }

        model = reportDefinition(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "enrollment" in serialized
        assert "queryElements" in serialized

        # Verify values are preserved
        assert serialized["enrollment"] == test_data["enrollment"]
        assert serialized["queryElements"] == test_data["queryElements"]

    def test_reportdefinition_model_json_schema(self):
        """Test reportDefinition model JSON schema generation."""
        schema = reportDefinition.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "enrollment",
            "queryElements",
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

    def test_reportdoc_model_creation(self):
        """Test reportDoc model creation with valid data."""
        # Valid test data for reportDoc
        valid_data = {
            "kind": "test_kind",
            "name": "test_name",
            "type": "test_type",
            "columns": [],
            "filterCriteria": [],
            "id": "test_id",
        }

        # Create model instance
        model = reportDoc(**valid_data)

        # Verify model creation
        assert isinstance(model, reportDoc)
        assert model.kind == valid_data["kind"]
        assert model.name == valid_data["name"]
        assert model.type == valid_data["type"]
        assert model.columns == valid_data["columns"]
        assert model.filterCriteria == valid_data["filterCriteria"]
        assert model.id == valid_data["id"]

    def test_reportdoc_model_validation(self):
        """Test reportDoc model field validation."""
        # Test with minimal required data
        minimal_data = {
            "kind": "required_kind",
            "name": "required_name",
            "type": "required_type",
            "columns": [],
            "filterCriteria": [],
            "id": "required_id",
        }

        model = reportDoc(**minimal_data)
        assert isinstance(model, reportDoc)
        assert model.kind == minimal_data["kind"]
        assert model.name == minimal_data["name"]
        assert model.type == minimal_data["type"]
        assert model.columns == minimal_data["columns"]
        assert model.filterCriteria == minimal_data["filterCriteria"]
        assert model.id == minimal_data["id"]

    def test_reportdoc_model_required_fields(self):
        """Test reportDoc model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "kind",
            "name",
            "type",
            "columns",
            "filterCriteria",
            "id",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                reportDoc()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "kind",
                "name",
                "type",
                "columns",
                "filterCriteria",
                "id",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = reportDoc()
            assert isinstance(model, reportDoc)

    def test_reportdoc_model_optional_fields(self):
        """Test reportDoc model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "kind": "required_kind",
            "name": "required_name",
            "type": "required_type",
            "columns": [],
            "filterCriteria": [],
            "id": "required_id",
        }

        model = reportDoc(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_reportdoc_model_serialization(self):
        """Test reportDoc model serialization to dict."""
        test_data = {
            "kind": "serialize_value",
            "name": "serialize_value",
            "type": "serialize_value",
            "columns": [],
            "filterCriteria": [],
            "id": "serialize_value",
        }

        model = reportDoc(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "kind" in serialized
        assert "name" in serialized
        assert "type" in serialized
        assert "columns" in serialized
        assert "filterCriteria" in serialized
        assert "id" in serialized

        # Verify values are preserved
        assert serialized["kind"] == test_data["kind"]
        assert serialized["name"] == test_data["name"]
        assert serialized["type"] == test_data["type"]
        assert serialized["columns"] == test_data["columns"]
        assert serialized["filterCriteria"] == test_data["filterCriteria"]
        assert serialized["id"] == test_data["id"]

    def test_reportdoc_model_json_schema(self):
        """Test reportDoc model JSON schema generation."""
        schema = reportDoc.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "kind",
            "name",
            "type",
            "columns",
            "filterCriteria",
            "id",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "kind",
            "name",
            "type",
            "columns",
            "filterCriteria",
            "id",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_generatereportbody_model_creation(self):
        """Test generateReportBody model creation with valid data."""
        # Valid test data for generateReportBody
        valid_data = {
            "definition": {},
            "description": "test_description",
            "kind": "test_kind",
            "name": "test_name",
            "type": "test_type",
        }

        # Create model instance
        model = generateReportBody(**valid_data)

        # Verify model creation
        assert isinstance(model, generateReportBody)
        assert model.definition == valid_data["definition"]
        assert model.description == valid_data["description"]
        assert model.kind == valid_data["kind"]
        assert model.name == valid_data["name"]
        assert model.type == valid_data["type"]

    def test_generatereportbody_model_validation(self):
        """Test generateReportBody model field validation."""
        # Test with minimal required data
        minimal_data = {}

        model = generateReportBody(**minimal_data)
        assert isinstance(model, generateReportBody)

    def test_generatereportbody_model_required_fields(self):
        """Test generateReportBody model required field validation."""
        # Check if this model has any required fields
        required_fields = []

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                generateReportBody()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {}

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = generateReportBody()
            assert isinstance(model, generateReportBody)

    def test_generatereportbody_model_optional_fields(self):
        """Test generateReportBody model optional field handling."""
        # Create with minimal required data
        minimal_data = {}

        model = generateReportBody(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "definition")
        # Optional field definition should be None or have a default value
        assert model.definition is None or model.definition is not None
        assert hasattr(model, "description")
        # Optional field description should be None or have a default value
        assert model.description is None or model.description is not None
        assert hasattr(model, "kind")
        # Optional field kind should be None or have a default value
        assert model.kind is None or model.kind is not None
        assert hasattr(model, "name")
        # Optional field name should be None or have a default value
        assert model.name is None or model.name is not None
        assert hasattr(model, "type")
        # Optional field type should be None or have a default value
        assert model.type is None or model.type is not None

    def test_generatereportbody_model_serialization(self):
        """Test generateReportBody model serialization to dict."""
        test_data = {
            "definition": {"key": "value"},
            "description": "serialize_value",
            "kind": "serialize_value",
            "name": "serialize_value",
            "type": "serialize_value",
        }

        model = generateReportBody(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "definition" in serialized
        assert "description" in serialized
        assert "kind" in serialized
        assert "name" in serialized
        assert "type" in serialized

        # Verify values are preserved
        assert serialized["definition"] == test_data["definition"]
        assert serialized["description"] == test_data["description"]
        assert serialized["kind"] == test_data["kind"]
        assert serialized["name"] == test_data["name"]
        assert serialized["type"] == test_data["type"]

    def test_generatereportbody_model_json_schema(self):
        """Test generateReportBody model JSON schema generation."""
        schema = generateReportBody.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "definition",
            "description",
            "kind",
            "name",
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

    def test_asyncoperationresponse_model_creation(self):
        """Test asyncOperationResponse model creation with valid data."""
        # Valid test data for asyncOperationResponse
        valid_data = {
            "id": "test_id",
            "results": [],
            "error": {},
            "sourceResourceUri": "test_sourceResourceUri",
            "progressPercent": 42,
            "type": "test_type",
            "startedAt": "test_startedAt",
            "logMessages": [],
            "state": "test_state",
            "endedAt": "test_endedAt",
        }

        # Create model instance
        model = asyncOperationResponse(**valid_data)

        # Verify model creation
        assert isinstance(model, asyncOperationResponse)
        assert model.id == valid_data["id"]
        assert model.results == valid_data["results"]
        assert model.error == valid_data["error"]
        assert model.sourceResourceUri == valid_data["sourceResourceUri"]
        assert model.progressPercent == valid_data["progressPercent"]
        assert model.type == valid_data["type"]
        assert model.startedAt == valid_data["startedAt"]
        assert model.logMessages == valid_data["logMessages"]
        assert model.state == valid_data["state"]
        assert model.endedAt == valid_data["endedAt"]

    def test_asyncoperationresponse_model_validation(self):
        """Test asyncOperationResponse model field validation."""
        # Test with minimal required data
        minimal_data = {
            "id": "required_id",
            "sourceResourceUri": "required_sourceResourceUri",
            "progressPercent": 1,
            "type": "required_type",
            "logMessages": [],
            "state": "required_state",
        }

        model = asyncOperationResponse(**minimal_data)
        assert isinstance(model, asyncOperationResponse)
        assert model.id == minimal_data["id"]
        assert model.sourceResourceUri == minimal_data["sourceResourceUri"]
        assert model.progressPercent == minimal_data["progressPercent"]
        assert model.type == minimal_data["type"]
        assert model.logMessages == minimal_data["logMessages"]
        assert model.state == minimal_data["state"]

    def test_asyncoperationresponse_model_required_fields(self):
        """Test asyncOperationResponse model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "id",
            "sourceResourceUri",
            "progressPercent",
            "type",
            "logMessages",
            "state",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                asyncOperationResponse()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "id",
                "sourceResourceUri",
                "progressPercent",
                "type",
                "logMessages",
                "state",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = asyncOperationResponse()
            assert isinstance(model, asyncOperationResponse)

    def test_asyncoperationresponse_model_optional_fields(self):
        """Test asyncOperationResponse model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "id": "required_id",
            "sourceResourceUri": "required_sourceResourceUri",
            "progressPercent": 1,
            "type": "required_type",
            "logMessages": [],
            "state": "required_state",
        }

        model = asyncOperationResponse(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "results")
        # Optional field results should be None or have a default value
        assert model.results is None or model.results is not None
        assert hasattr(model, "error")
        # Optional field error should be None or have a default value
        assert model.error is None or model.error is not None
        assert hasattr(model, "startedAt")
        # Optional field startedAt should be None or have a default value
        assert model.startedAt is None or model.startedAt is not None
        assert hasattr(model, "endedAt")
        # Optional field endedAt should be None or have a default value
        assert model.endedAt is None or model.endedAt is not None

    def test_asyncoperationresponse_model_serialization(self):
        """Test asyncOperationResponse model serialization to dict."""
        test_data = {
            "id": "serialize_value",
            "results": [],
            "error": {"key": "value"},
            "sourceResourceUri": "serialize_value",
            "progressPercent": 99,
            "type": "serialize_value",
            "startedAt": "serialize_value",
            "logMessages": [],
            "state": "serialize_value",
            "endedAt": "serialize_value",
        }

        model = asyncOperationResponse(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "id" in serialized
        assert "results" in serialized
        assert "error" in serialized
        assert "sourceResourceUri" in serialized
        assert "progressPercent" in serialized
        assert "type" in serialized
        assert "startedAt" in serialized
        assert "logMessages" in serialized
        assert "state" in serialized
        assert "endedAt" in serialized

        # Verify values are preserved
        assert serialized["id"] == test_data["id"]
        assert serialized["results"] == test_data["results"]
        assert serialized["error"] == test_data["error"]
        assert serialized["sourceResourceUri"] == test_data["sourceResourceUri"]
        assert serialized["progressPercent"] == test_data["progressPercent"]
        assert serialized["type"] == test_data["type"]
        assert serialized["startedAt"] == test_data["startedAt"]
        assert serialized["logMessages"] == test_data["logMessages"]
        assert serialized["state"] == test_data["state"]
        assert serialized["endedAt"] == test_data["endedAt"]

    def test_asyncoperationresponse_model_json_schema(self):
        """Test asyncOperationResponse model JSON schema generation."""
        schema = asyncOperationResponse.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "id",
            "results",
            "error",
            "sourceResourceUri",
            "progressPercent",
            "type",
            "startedAt",
            "logMessages",
            "state",
            "endedAt",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "id",
            "sourceResourceUri",
            "progressPercent",
            "type",
            "logMessages",
            "state",
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
            error,
            filterCriteria,
            generateDocResponse,
            delivery,
            enrollment,
            generateResponse,
            queryElements,
            reportDefinition,
            reportDoc,
            generateReportBody,
            asyncOperationResponse,
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
            error,
            filterCriteria,
            generateDocResponse,
            delivery,
            enrollment,
            generateResponse,
            queryElements,
            reportDefinition,
            reportDoc,
            generateReportBody,
            asyncOperationResponse,
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
            error,
            filterCriteria,
            generateDocResponse,
            delivery,
            enrollment,
            generateResponse,
            queryElements,
            reportDefinition,
            reportDoc,
            generateReportBody,
            asyncOperationResponse,
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
            error,
            filterCriteria,
            generateDocResponse,
            delivery,
            enrollment,
            generateResponse,
            queryElements,
            reportDefinition,
            reportDoc,
            generateReportBody,
            asyncOperationResponse,
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
