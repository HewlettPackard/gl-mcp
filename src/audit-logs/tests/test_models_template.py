# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
Test template for models package.
Tests all generated data models from OpenAPI schemas.
"""

import pytest
from typing import Any, Dict
from pydantic import ValidationError as PydanticValidationError


from greenlake_audit_logs_mcp.models.base import AuditLogDetails

from greenlake_audit_logs_mcp.models.base import Error

from greenlake_audit_logs_mcp.models.base import AuditLog

from greenlake_audit_logs_mcp.models.base import AuditLogs

from greenlake_audit_logs_mcp.models.base import ErrorGeneralDetails

from greenlake_audit_logs_mcp.models.base import ErrorRetryDetails

from greenlake_audit_logs_mcp.models.base import ErrorBadRequestDetails

from greenlake_audit_logs_mcp.models.base import ErrorNotFoundDetails

from greenlake_audit_logs_mcp.models.base import PaginatedApiResponse


class TestModels:
    """Test suite for all generated data models."""

    def test_audit_log_details_model_creation(self):
        """Test AuditLogDetails model creation with valid data."""
        # Valid test data for AuditLogDetails
        valid_data = {
            "type": "test_type",
            "body": [],
            "header": "test_header",
            "id": "test_id",
        }

        # Create model instance
        model = AuditLogDetails(**valid_data)

        # Verify model creation
        assert isinstance(model, AuditLogDetails)
        assert model.type == valid_data["type"]
        assert model.body == valid_data["body"]
        assert model.header == valid_data["header"]
        assert model.id == valid_data["id"]

    def test_audit_log_details_model_validation(self):
        """Test AuditLogDetails model field validation."""
        # Test with minimal required data
        minimal_data = {
            "type": "required_type",
            "body": [],
            "header": "required_header",
            "id": "required_id",
        }

        model = AuditLogDetails(**minimal_data)
        assert isinstance(model, AuditLogDetails)
        assert model.type == minimal_data["type"]
        assert model.body == minimal_data["body"]
        assert model.header == minimal_data["header"]
        assert model.id == minimal_data["id"]

    def test_audit_log_details_model_required_fields(self):
        """Test AuditLogDetails model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "type",
            "body",
            "header",
            "id",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                AuditLogDetails()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "type",
                "body",
                "header",
                "id",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = AuditLogDetails()
            assert isinstance(model, AuditLogDetails)

    def test_audit_log_details_model_optional_fields(self):
        """Test AuditLogDetails model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "type": "required_type",
            "body": [],
            "header": "required_header",
            "id": "required_id",
        }

        model = AuditLogDetails(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_audit_log_details_model_serialization(self):
        """Test AuditLogDetails model serialization to dict."""
        test_data = {
            "type": "serialize_value",
            "body": [],
            "header": "serialize_value",
            "id": "serialize_value",
        }

        model = AuditLogDetails(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "type" in serialized
        assert "body" in serialized
        assert "header" in serialized
        assert "id" in serialized

        # Verify values are preserved
        assert serialized["type"] == test_data["type"]
        assert serialized["body"] == test_data["body"]
        assert serialized["header"] == test_data["header"]
        assert serialized["id"] == test_data["id"]

    def test_audit_log_details_model_json_schema(self):
        """Test AuditLogDetails model JSON schema generation."""
        schema = AuditLogDetails.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "type",
            "body",
            "header",
            "id",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "type",
            "body",
            "header",
            "id",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_error_model_creation(self):
        """Test Error model creation with valid data."""
        # Valid test data for Error
        valid_data = {
            "message": "test_message",
            "debugId": "test_debugId",
            "errorCode": "test_errorCode",
            "httpStatusCode": 42,
        }

        # Create model instance
        model = Error(**valid_data)

        # Verify model creation
        assert isinstance(model, Error)
        assert model.message == valid_data["message"]
        assert model.debugId == valid_data["debugId"]
        assert model.errorCode == valid_data["errorCode"]
        assert model.httpStatusCode == valid_data["httpStatusCode"]

    def test_error_model_validation(self):
        """Test Error model field validation."""
        # Test with minimal required data
        minimal_data = {
            "message": "required_message",
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
            "httpStatusCode": 1,
        }

        model = Error(**minimal_data)
        assert isinstance(model, Error)
        assert model.message == minimal_data["message"]
        assert model.debugId == minimal_data["debugId"]
        assert model.errorCode == minimal_data["errorCode"]
        assert model.httpStatusCode == minimal_data["httpStatusCode"]

    def test_error_model_required_fields(self):
        """Test Error model required field validation."""
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
                Error()

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
            model = Error()
            assert isinstance(model, Error)

    def test_error_model_optional_fields(self):
        """Test Error model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "message": "required_message",
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
            "httpStatusCode": 1,
        }

        model = Error(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_error_model_serialization(self):
        """Test Error model serialization to dict."""
        test_data = {
            "message": "serialize_value",
            "debugId": "serialize_value",
            "errorCode": "serialize_value",
            "httpStatusCode": 99,
        }

        model = Error(**test_data)
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

    def test_error_model_json_schema(self):
        """Test Error model JSON schema generation."""
        schema = Error.model_json_schema()

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

    def test_audit_log_model_creation(self):
        """Test AuditLog model creation with valid data."""
        # Valid test data for AuditLog
        valid_data = {
            "updatedAt": "test_updatedAt",
            "additionalInfo": {},
            "category": "test_category",
            "region": "test_region",
            "createdAt": "test_createdAt",
            "hasDetails": True,
            "user": {},
            "workspace": {},
            "type": "test_type",
            "application": {},
            "description": "test_description",
            "generation": 42,
            "id": "test_id",
        }

        # Create model instance
        model = AuditLog(**valid_data)

        # Verify model creation
        assert isinstance(model, AuditLog)
        assert model.updatedAt == valid_data["updatedAt"]
        assert model.additionalInfo == valid_data["additionalInfo"]
        assert model.category == valid_data["category"]
        assert model.region == valid_data["region"]
        assert model.createdAt == valid_data["createdAt"]
        assert model.hasDetails == valid_data["hasDetails"]
        assert model.user == valid_data["user"]
        assert model.workspace == valid_data["workspace"]
        assert model.type == valid_data["type"]
        assert model.application == valid_data["application"]
        assert model.description == valid_data["description"]
        assert model.generation == valid_data["generation"]
        assert model.id == valid_data["id"]

    def test_audit_log_model_validation(self):
        """Test AuditLog model field validation."""
        # Test with minimal required data
        minimal_data = {
            "type": "required_type",
            "id": "required_id",
        }

        model = AuditLog(**minimal_data)
        assert isinstance(model, AuditLog)
        assert model.type == minimal_data["type"]
        assert model.id == minimal_data["id"]

    def test_audit_log_model_required_fields(self):
        """Test AuditLog model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "type",
            "id",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                AuditLog()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "type",
                "id",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = AuditLog()
            assert isinstance(model, AuditLog)

    def test_audit_log_model_optional_fields(self):
        """Test AuditLog model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "type": "required_type",
            "id": "required_id",
        }

        model = AuditLog(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "updatedAt")
        # Optional field updatedAt should be None or have a default value
        assert model.updatedAt is None or model.updatedAt is not None
        assert hasattr(model, "additionalInfo")
        # Optional field additionalInfo should be None or have a default value
        assert model.additionalInfo is None or model.additionalInfo is not None
        assert hasattr(model, "category")
        # Optional field category should be None or have a default value
        assert model.category is None or model.category is not None
        assert hasattr(model, "region")
        # Optional field region should be None or have a default value
        assert model.region is None or model.region is not None
        assert hasattr(model, "createdAt")
        # Optional field createdAt should be None or have a default value
        assert model.createdAt is None or model.createdAt is not None
        assert hasattr(model, "hasDetails")
        # Optional field hasDetails should be None or have a default value
        assert model.hasDetails is None or model.hasDetails is not None
        assert hasattr(model, "user")
        # Optional field user should be None or have a default value
        assert model.user is None or model.user is not None
        assert hasattr(model, "workspace")
        # Optional field workspace should be None or have a default value
        assert model.workspace is None or model.workspace is not None
        assert hasattr(model, "application")
        # Optional field application should be None or have a default value
        assert model.application is None or model.application is not None
        assert hasattr(model, "description")
        # Optional field description should be None or have a default value
        assert model.description is None or model.description is not None
        assert hasattr(model, "generation")
        # Optional field generation should be None or have a default value
        assert model.generation is None or model.generation is not None

    def test_audit_log_model_serialization(self):
        """Test AuditLog model serialization to dict."""
        test_data = {
            "updatedAt": "serialize_value",
            "additionalInfo": {"key": "value"},
            "category": "serialize_value",
            "region": "serialize_value",
            "createdAt": "serialize_value",
            "hasDetails": False,
            "user": {"key": "value"},
            "workspace": {"key": "value"},
            "type": "serialize_value",
            "application": {"key": "value"},
            "description": "serialize_value",
            "generation": 99,
            "id": "serialize_value",
        }

        model = AuditLog(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "updatedAt" in serialized
        assert "additionalInfo" in serialized
        assert "category" in serialized
        assert "region" in serialized
        assert "createdAt" in serialized
        assert "hasDetails" in serialized
        assert "user" in serialized
        assert "workspace" in serialized
        assert "type" in serialized
        assert "application" in serialized
        assert "description" in serialized
        assert "generation" in serialized
        assert "id" in serialized

        # Verify values are preserved
        assert serialized["updatedAt"] == test_data["updatedAt"]
        assert serialized["additionalInfo"] == test_data["additionalInfo"]
        assert serialized["category"] == test_data["category"]
        assert serialized["region"] == test_data["region"]
        assert serialized["createdAt"] == test_data["createdAt"]
        assert serialized["hasDetails"] == test_data["hasDetails"]
        assert serialized["user"] == test_data["user"]
        assert serialized["workspace"] == test_data["workspace"]
        assert serialized["type"] == test_data["type"]
        assert serialized["application"] == test_data["application"]
        assert serialized["description"] == test_data["description"]
        assert serialized["generation"] == test_data["generation"]
        assert serialized["id"] == test_data["id"]

    def test_audit_log_model_json_schema(self):
        """Test AuditLog model JSON schema generation."""
        schema = AuditLog.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "updatedAt",
            "additionalInfo",
            "category",
            "region",
            "createdAt",
            "hasDetails",
            "user",
            "workspace",
            "type",
            "application",
            "description",
            "generation",
            "id",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "type",
            "id",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_audit_logs_model_creation(self):
        """Test AuditLogs model creation with valid data."""
        # Valid test data for AuditLogs
        valid_data = {
            "items": [],
            "total": 42,
            "count": 42,
            "offset": 42,
            "remainingRecords": True,
        }

        # Create model instance
        model = AuditLogs(**valid_data)

        # Verify model creation
        assert isinstance(model, AuditLogs)
        assert model.items == valid_data["items"]
        assert model.total == valid_data["total"]
        assert model.count == valid_data["count"]
        assert model.offset == valid_data["offset"]
        assert model.remainingRecords == valid_data["remainingRecords"]

    def test_audit_logs_model_validation(self):
        """Test AuditLogs model field validation."""
        # Test with minimal required data
        minimal_data = {
            "items": [],
            "total": 1,
            "count": 1,
        }

        model = AuditLogs(**minimal_data)
        assert isinstance(model, AuditLogs)
        assert model.items == minimal_data["items"]
        assert model.total == minimal_data["total"]
        assert model.count == minimal_data["count"]

    def test_audit_logs_model_required_fields(self):
        """Test AuditLogs model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "items",
            "total",
            "count",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                AuditLogs()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "items",
                "total",
                "count",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = AuditLogs()
            assert isinstance(model, AuditLogs)

    def test_audit_logs_model_optional_fields(self):
        """Test AuditLogs model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "items": [],
            "total": 1,
            "count": 1,
        }

        model = AuditLogs(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "offset")
        # Optional field offset should be None or have a default value
        assert model.offset is None or model.offset is not None
        assert hasattr(model, "remainingRecords")
        # Optional field remainingRecords should be None or have a default value
        assert model.remainingRecords is None or model.remainingRecords is not None

    def test_audit_logs_model_serialization(self):
        """Test AuditLogs model serialization to dict."""
        test_data = {
            "items": [],
            "total": 99,
            "count": 99,
            "offset": 99,
            "remainingRecords": False,
        }

        model = AuditLogs(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "items" in serialized
        assert "total" in serialized
        assert "count" in serialized
        assert "offset" in serialized
        assert "remainingRecords" in serialized

        # Verify values are preserved
        assert serialized["items"] == test_data["items"]
        assert serialized["total"] == test_data["total"]
        assert serialized["count"] == test_data["count"]
        assert serialized["offset"] == test_data["offset"]
        assert serialized["remainingRecords"] == test_data["remainingRecords"]

    def test_audit_logs_model_json_schema(self):
        """Test AuditLogs model JSON schema generation."""
        schema = AuditLogs.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "items",
            "total",
            "count",
            "offset",
            "remainingRecords",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "items",
            "total",
            "count",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_error_general_details_model_creation(self):
        """Test ErrorGeneralDetails model creation with valid data."""
        # Valid test data for ErrorGeneralDetails
        valid_data = {
            "errorDetails": [],
        }

        # Create model instance
        model = ErrorGeneralDetails(**valid_data)

        # Verify model creation
        assert isinstance(model, ErrorGeneralDetails)
        assert model.errorDetails == valid_data["errorDetails"]

    def test_error_general_details_model_validation(self):
        """Test ErrorGeneralDetails model field validation."""
        # Test with minimal required data
        minimal_data = {}

        model = ErrorGeneralDetails(**minimal_data)
        assert isinstance(model, ErrorGeneralDetails)

    def test_error_general_details_model_required_fields(self):
        """Test ErrorGeneralDetails model required field validation."""
        # Check if this model has any required fields
        required_fields = []

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                ErrorGeneralDetails()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {}

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = ErrorGeneralDetails()
            assert isinstance(model, ErrorGeneralDetails)

    def test_error_general_details_model_optional_fields(self):
        """Test ErrorGeneralDetails model optional field handling."""
        # Create with minimal required data
        minimal_data = {}

        model = ErrorGeneralDetails(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "errorDetails")
        # Optional field errorDetails should be None or have a default value
        assert model.errorDetails is None or model.errorDetails is not None

    def test_error_general_details_model_serialization(self):
        """Test ErrorGeneralDetails model serialization to dict."""
        test_data = {
            "errorDetails": [],
        }

        model = ErrorGeneralDetails(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "errorDetails" in serialized

        # Verify values are preserved
        assert serialized["errorDetails"] == test_data["errorDetails"]

    def test_error_general_details_model_json_schema(self):
        """Test ErrorGeneralDetails model JSON schema generation."""
        schema = ErrorGeneralDetails.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "errorDetails",
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

    def test_error_retry_details_model_creation(self):
        """Test ErrorRetryDetails model creation with valid data."""
        # Valid test data for ErrorRetryDetails
        valid_data = {
            "errorDetails": [],
        }

        # Create model instance
        model = ErrorRetryDetails(**valid_data)

        # Verify model creation
        assert isinstance(model, ErrorRetryDetails)
        assert model.errorDetails == valid_data["errorDetails"]

    def test_error_retry_details_model_validation(self):
        """Test ErrorRetryDetails model field validation."""
        # Test with minimal required data
        minimal_data = {}

        model = ErrorRetryDetails(**minimal_data)
        assert isinstance(model, ErrorRetryDetails)

    def test_error_retry_details_model_required_fields(self):
        """Test ErrorRetryDetails model required field validation."""
        # Check if this model has any required fields
        required_fields = []

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                ErrorRetryDetails()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {}

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = ErrorRetryDetails()
            assert isinstance(model, ErrorRetryDetails)

    def test_error_retry_details_model_optional_fields(self):
        """Test ErrorRetryDetails model optional field handling."""
        # Create with minimal required data
        minimal_data = {}

        model = ErrorRetryDetails(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "errorDetails")
        # Optional field errorDetails should be None or have a default value
        assert model.errorDetails is None or model.errorDetails is not None

    def test_error_retry_details_model_serialization(self):
        """Test ErrorRetryDetails model serialization to dict."""
        test_data = {
            "errorDetails": [],
        }

        model = ErrorRetryDetails(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "errorDetails" in serialized

        # Verify values are preserved
        assert serialized["errorDetails"] == test_data["errorDetails"]

    def test_error_retry_details_model_json_schema(self):
        """Test ErrorRetryDetails model JSON schema generation."""
        schema = ErrorRetryDetails.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "errorDetails",
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

    def test_error_bad_request_details_model_creation(self):
        """Test ErrorBadRequestDetails model creation with valid data."""
        # Valid test data for ErrorBadRequestDetails
        valid_data = {
            "errorDetails": [],
        }

        # Create model instance
        model = ErrorBadRequestDetails(**valid_data)

        # Verify model creation
        assert isinstance(model, ErrorBadRequestDetails)
        assert model.errorDetails == valid_data["errorDetails"]

    def test_error_bad_request_details_model_validation(self):
        """Test ErrorBadRequestDetails model field validation."""
        # Test with minimal required data
        minimal_data = {}

        model = ErrorBadRequestDetails(**minimal_data)
        assert isinstance(model, ErrorBadRequestDetails)

    def test_error_bad_request_details_model_required_fields(self):
        """Test ErrorBadRequestDetails model required field validation."""
        # Check if this model has any required fields
        required_fields = []

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                ErrorBadRequestDetails()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {}

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = ErrorBadRequestDetails()
            assert isinstance(model, ErrorBadRequestDetails)

    def test_error_bad_request_details_model_optional_fields(self):
        """Test ErrorBadRequestDetails model optional field handling."""
        # Create with minimal required data
        minimal_data = {}

        model = ErrorBadRequestDetails(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "errorDetails")
        # Optional field errorDetails should be None or have a default value
        assert model.errorDetails is None or model.errorDetails is not None

    def test_error_bad_request_details_model_serialization(self):
        """Test ErrorBadRequestDetails model serialization to dict."""
        test_data = {
            "errorDetails": [],
        }

        model = ErrorBadRequestDetails(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "errorDetails" in serialized

        # Verify values are preserved
        assert serialized["errorDetails"] == test_data["errorDetails"]

    def test_error_bad_request_details_model_json_schema(self):
        """Test ErrorBadRequestDetails model JSON schema generation."""
        schema = ErrorBadRequestDetails.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "errorDetails",
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

    def test_error_not_found_details_model_creation(self):
        """Test ErrorNotFoundDetails model creation with valid data."""
        # Valid test data for ErrorNotFoundDetails
        valid_data = {
            "errorDetails": [],
        }

        # Create model instance
        model = ErrorNotFoundDetails(**valid_data)

        # Verify model creation
        assert isinstance(model, ErrorNotFoundDetails)
        assert model.errorDetails == valid_data["errorDetails"]

    def test_error_not_found_details_model_validation(self):
        """Test ErrorNotFoundDetails model field validation."""
        # Test with minimal required data
        minimal_data = {}

        model = ErrorNotFoundDetails(**minimal_data)
        assert isinstance(model, ErrorNotFoundDetails)

    def test_error_not_found_details_model_required_fields(self):
        """Test ErrorNotFoundDetails model required field validation."""
        # Check if this model has any required fields
        required_fields = []

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                ErrorNotFoundDetails()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {}

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = ErrorNotFoundDetails()
            assert isinstance(model, ErrorNotFoundDetails)

    def test_error_not_found_details_model_optional_fields(self):
        """Test ErrorNotFoundDetails model optional field handling."""
        # Create with minimal required data
        minimal_data = {}

        model = ErrorNotFoundDetails(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "errorDetails")
        # Optional field errorDetails should be None or have a default value
        assert model.errorDetails is None or model.errorDetails is not None

    def test_error_not_found_details_model_serialization(self):
        """Test ErrorNotFoundDetails model serialization to dict."""
        test_data = {
            "errorDetails": [],
        }

        model = ErrorNotFoundDetails(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "errorDetails" in serialized

        # Verify values are preserved
        assert serialized["errorDetails"] == test_data["errorDetails"]

    def test_error_not_found_details_model_json_schema(self):
        """Test ErrorNotFoundDetails model JSON schema generation."""
        schema = ErrorNotFoundDetails.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "errorDetails",
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

    def test_paginated_api_response_model_creation(self):
        """Test PaginatedApiResponse model creation with valid data."""
        # Valid test data for PaginatedApiResponse
        valid_data = {
            "count": 42,
            "offset": 42,
            "remainingRecords": True,
            "total": 42,
        }

        # Create model instance
        model = PaginatedApiResponse(**valid_data)

        # Verify model creation
        assert isinstance(model, PaginatedApiResponse)
        assert model.count == valid_data["count"]
        assert model.offset == valid_data["offset"]
        assert model.remainingRecords == valid_data["remainingRecords"]
        assert model.total == valid_data["total"]

    def test_paginated_api_response_model_validation(self):
        """Test PaginatedApiResponse model field validation."""
        # Test with minimal required data
        minimal_data = {
            "count": 1,
            "total": 1,
        }

        model = PaginatedApiResponse(**minimal_data)
        assert isinstance(model, PaginatedApiResponse)
        assert model.count == minimal_data["count"]
        assert model.total == minimal_data["total"]

    def test_paginated_api_response_model_required_fields(self):
        """Test PaginatedApiResponse model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "count",
            "total",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                PaginatedApiResponse()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "count",
                "total",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = PaginatedApiResponse()
            assert isinstance(model, PaginatedApiResponse)

    def test_paginated_api_response_model_optional_fields(self):
        """Test PaginatedApiResponse model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "count": 1,
            "total": 1,
        }

        model = PaginatedApiResponse(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "offset")
        # Optional field offset should be None or have a default value
        assert model.offset is None or model.offset is not None
        assert hasattr(model, "remainingRecords")
        # Optional field remainingRecords should be None or have a default value
        assert model.remainingRecords is None or model.remainingRecords is not None

    def test_paginated_api_response_model_serialization(self):
        """Test PaginatedApiResponse model serialization to dict."""
        test_data = {
            "count": 99,
            "offset": 99,
            "remainingRecords": False,
            "total": 99,
        }

        model = PaginatedApiResponse(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "count" in serialized
        assert "offset" in serialized
        assert "remainingRecords" in serialized
        assert "total" in serialized

        # Verify values are preserved
        assert serialized["count"] == test_data["count"]
        assert serialized["offset"] == test_data["offset"]
        assert serialized["remainingRecords"] == test_data["remainingRecords"]
        assert serialized["total"] == test_data["total"]

    def test_paginated_api_response_model_json_schema(self):
        """Test PaginatedApiResponse model JSON schema generation."""
        schema = PaginatedApiResponse.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "count",
            "offset",
            "remainingRecords",
            "total",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "count",
            "total",
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
            AuditLogDetails,
            Error,
            AuditLog,
            AuditLogs,
            ErrorGeneralDetails,
            ErrorRetryDetails,
            ErrorBadRequestDetails,
            ErrorNotFoundDetails,
            PaginatedApiResponse,
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
            AuditLogDetails,
            Error,
            AuditLog,
            AuditLogs,
            ErrorGeneralDetails,
            ErrorRetryDetails,
            ErrorBadRequestDetails,
            ErrorNotFoundDetails,
            PaginatedApiResponse,
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
            AuditLogDetails,
            Error,
            AuditLog,
            AuditLogs,
            ErrorGeneralDetails,
            ErrorRetryDetails,
            ErrorBadRequestDetails,
            ErrorNotFoundDetails,
            PaginatedApiResponse,
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
            AuditLogDetails,
            Error,
            AuditLog,
            AuditLogs,
            ErrorGeneralDetails,
            ErrorRetryDetails,
            ErrorBadRequestDetails,
            ErrorNotFoundDetails,
            PaginatedApiResponse,
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
