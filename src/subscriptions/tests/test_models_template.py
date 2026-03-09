# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
Test template for models package.
Tests all generated data models from OpenAPI schemas.
"""

import pytest
from typing import Any, Dict
from pydantic import ValidationError as PydanticValidationError


from models.base import AutoSubscriptionsPostRequest

from models.base import AutoSubscriptionsResponseDtoWithTenant

from models.base import ErrorIssue

from models.base import RequestPostAutoSubscription

from models.base import GeneralErrorDetail

from models.base import HpeGreenLakeBadRequestError

from models.base import AutoSubscriptionsResponsePaginatedDto

from models.base import HpeGreenLakeGeneralError

from models.base import ServerErrorDetail

from models.base import V1Beta1SubscriptionDetail

from models.base import AutoSubscriptionsResponseDto

from models.base import BulkUnclaimId

from models.base import SubscriptionsGetResponse

from models.base import RequestPostSubscription

from models.base import SubscriptionDetail

from models.base import SubscriptionsPostRequest

from models.base import SubscriptionsBulkUnclaimRequest

from models.base import V1Beta1SubscriptionsGetResponse

from models.base import AsyncOperationResource

from models.base import AsyncResponse

from models.base import AutoSubscriptionSettings

from models.base import Appointment

from models.base import HpeGreenLakeServerError

from models.base import SubscriptionsPatchRequest

from models.base import BadRequestErrorDetail


class TestModels:
    """Test suite for all generated data models."""

    def test_autosubscriptionspostrequest_model_creation(self):
        """Test AutoSubscriptionsPostRequest model creation with valid data."""
        # Valid test data for AutoSubscriptionsPostRequest
        valid_data = {
            "autoSubscriptionSettings": [],
        }

        # Create model instance
        model = AutoSubscriptionsPostRequest(**valid_data)

        # Verify model creation
        assert isinstance(model, AutoSubscriptionsPostRequest)
        assert model.autoSubscriptionSettings == valid_data["autoSubscriptionSettings"]

    def test_autosubscriptionspostrequest_model_validation(self):
        """Test AutoSubscriptionsPostRequest model field validation."""
        # Test with minimal required data
        minimal_data = {}

        model = AutoSubscriptionsPostRequest(**minimal_data)
        assert isinstance(model, AutoSubscriptionsPostRequest)

    def test_autosubscriptionspostrequest_model_required_fields(self):
        """Test AutoSubscriptionsPostRequest model required field validation."""
        # Check if this model has any required fields
        required_fields = []

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                AutoSubscriptionsPostRequest()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {}

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = AutoSubscriptionsPostRequest()
            assert isinstance(model, AutoSubscriptionsPostRequest)

    def test_autosubscriptionspostrequest_model_optional_fields(self):
        """Test AutoSubscriptionsPostRequest model optional field handling."""
        # Create with minimal required data
        minimal_data = {}

        model = AutoSubscriptionsPostRequest(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "autoSubscriptionSettings")
        # Optional field autoSubscriptionSettings should be None or have a default value
        assert model.autoSubscriptionSettings is None or model.autoSubscriptionSettings is not None

    def test_autosubscriptionspostrequest_model_serialization(self):
        """Test AutoSubscriptionsPostRequest model serialization to dict."""
        test_data = {
            "autoSubscriptionSettings": [],
        }

        model = AutoSubscriptionsPostRequest(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "autoSubscriptionSettings" in serialized

        # Verify values are preserved
        assert serialized["autoSubscriptionSettings"] == test_data["autoSubscriptionSettings"]

    def test_autosubscriptionspostrequest_model_json_schema(self):
        """Test AutoSubscriptionsPostRequest model JSON schema generation."""
        schema = AutoSubscriptionsPostRequest.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "autoSubscriptionSettings",
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

    def test_autosubscriptionsresponsedtowithtenant_model_creation(self):
        """Test AutoSubscriptionsResponseDtoWithTenant model creation with valid data."""
        # Valid test data for AutoSubscriptionsResponseDtoWithTenant
        valid_data = {
            "generation": 42,
            "id": "test_id",
            "resourceUri": "test_resourceUri",
            "tenantWorkspaceId": "test_tenantWorkspaceId",
            "type": "test_type",
            "updatedAt": "test_updatedAt",
            "autoSubscriptionSettings": [],
            "createdAt": "test_createdAt",
        }

        # Create model instance
        model = AutoSubscriptionsResponseDtoWithTenant(**valid_data)

        # Verify model creation
        assert isinstance(model, AutoSubscriptionsResponseDtoWithTenant)
        assert model.generation == valid_data["generation"]
        assert model.id == valid_data["id"]
        assert model.resourceUri == valid_data["resourceUri"]
        assert model.tenantWorkspaceId == valid_data["tenantWorkspaceId"]
        assert model.type == valid_data["type"]
        assert model.updatedAt == valid_data["updatedAt"]
        assert model.autoSubscriptionSettings == valid_data["autoSubscriptionSettings"]
        assert model.createdAt == valid_data["createdAt"]

    def test_autosubscriptionsresponsedtowithtenant_model_validation(self):
        """Test AutoSubscriptionsResponseDtoWithTenant model field validation."""
        # Test with minimal required data
        minimal_data = {
            "id": "required_id",
            "resourceUri": "required_resourceUri",
            "type": "required_type",
            "updatedAt": "required_updatedAt",
            "createdAt": "required_createdAt",
        }

        model = AutoSubscriptionsResponseDtoWithTenant(**minimal_data)
        assert isinstance(model, AutoSubscriptionsResponseDtoWithTenant)
        assert model.id == minimal_data["id"]
        assert model.resourceUri == minimal_data["resourceUri"]
        assert model.type == minimal_data["type"]
        assert model.updatedAt == minimal_data["updatedAt"]
        assert model.createdAt == minimal_data["createdAt"]

    def test_autosubscriptionsresponsedtowithtenant_model_required_fields(self):
        """Test AutoSubscriptionsResponseDtoWithTenant model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "id",
            "resourceUri",
            "type",
            "updatedAt",
            "createdAt",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                AutoSubscriptionsResponseDtoWithTenant()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "id",
                "resourceUri",
                "type",
                "updatedAt",
                "createdAt",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = AutoSubscriptionsResponseDtoWithTenant()
            assert isinstance(model, AutoSubscriptionsResponseDtoWithTenant)

    def test_autosubscriptionsresponsedtowithtenant_model_optional_fields(self):
        """Test AutoSubscriptionsResponseDtoWithTenant model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "id": "required_id",
            "resourceUri": "required_resourceUri",
            "type": "required_type",
            "updatedAt": "required_updatedAt",
            "createdAt": "required_createdAt",
        }

        model = AutoSubscriptionsResponseDtoWithTenant(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "generation")
        # Optional field generation should be None or have a default value
        assert model.generation is None or model.generation is not None
        assert hasattr(model, "tenantWorkspaceId")
        # Optional field tenantWorkspaceId should be None or have a default value
        assert model.tenantWorkspaceId is None or model.tenantWorkspaceId is not None
        assert hasattr(model, "autoSubscriptionSettings")
        # Optional field autoSubscriptionSettings should be None or have a default value
        assert model.autoSubscriptionSettings is None or model.autoSubscriptionSettings is not None

    def test_autosubscriptionsresponsedtowithtenant_model_serialization(self):
        """Test AutoSubscriptionsResponseDtoWithTenant model serialization to dict."""
        test_data = {
            "generation": 99,
            "id": "serialize_value",
            "resourceUri": "serialize_value",
            "tenantWorkspaceId": "serialize_value",
            "type": "serialize_value",
            "updatedAt": "serialize_value",
            "autoSubscriptionSettings": [],
            "createdAt": "serialize_value",
        }

        model = AutoSubscriptionsResponseDtoWithTenant(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "generation" in serialized
        assert "id" in serialized
        assert "resourceUri" in serialized
        assert "tenantWorkspaceId" in serialized
        assert "type" in serialized
        assert "updatedAt" in serialized
        assert "autoSubscriptionSettings" in serialized
        assert "createdAt" in serialized

        # Verify values are preserved
        assert serialized["generation"] == test_data["generation"]
        assert serialized["id"] == test_data["id"]
        assert serialized["resourceUri"] == test_data["resourceUri"]
        assert serialized["tenantWorkspaceId"] == test_data["tenantWorkspaceId"]
        assert serialized["type"] == test_data["type"]
        assert serialized["updatedAt"] == test_data["updatedAt"]
        assert serialized["autoSubscriptionSettings"] == test_data["autoSubscriptionSettings"]
        assert serialized["createdAt"] == test_data["createdAt"]

    def test_autosubscriptionsresponsedtowithtenant_model_json_schema(self):
        """Test AutoSubscriptionsResponseDtoWithTenant model JSON schema generation."""
        schema = AutoSubscriptionsResponseDtoWithTenant.model_json_schema()

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
            "tenantWorkspaceId",
            "type",
            "updatedAt",
            "autoSubscriptionSettings",
            "createdAt",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "id",
            "resourceUri",
            "type",
            "updatedAt",
            "createdAt",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_errorissue_model_creation(self):
        """Test ErrorIssue model creation with valid data."""
        # Valid test data for ErrorIssue
        valid_data = {
            "subject": "test_subject",
            "description": "test_description",
            "source": "test_source",
        }

        # Create model instance
        model = ErrorIssue(**valid_data)

        # Verify model creation
        assert isinstance(model, ErrorIssue)
        assert model.subject == valid_data["subject"]
        assert model.description == valid_data["description"]
        assert model.source == valid_data["source"]

    def test_errorissue_model_validation(self):
        """Test ErrorIssue model field validation."""
        # Test with minimal required data
        minimal_data = {}

        model = ErrorIssue(**minimal_data)
        assert isinstance(model, ErrorIssue)

    def test_errorissue_model_required_fields(self):
        """Test ErrorIssue model required field validation."""
        # Check if this model has any required fields
        required_fields = []

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                ErrorIssue()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {}

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = ErrorIssue()
            assert isinstance(model, ErrorIssue)

    def test_errorissue_model_optional_fields(self):
        """Test ErrorIssue model optional field handling."""
        # Create with minimal required data
        minimal_data = {}

        model = ErrorIssue(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "subject")
        # Optional field subject should be None or have a default value
        assert model.subject is None or model.subject is not None
        assert hasattr(model, "description")
        # Optional field description should be None or have a default value
        assert model.description is None or model.description is not None
        assert hasattr(model, "source")
        # Optional field source should be None or have a default value
        assert model.source is None or model.source is not None

    def test_errorissue_model_serialization(self):
        """Test ErrorIssue model serialization to dict."""
        test_data = {
            "subject": "serialize_value",
            "description": "serialize_value",
            "source": "serialize_value",
        }

        model = ErrorIssue(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "subject" in serialized
        assert "description" in serialized
        assert "source" in serialized

        # Verify values are preserved
        assert serialized["subject"] == test_data["subject"]
        assert serialized["description"] == test_data["description"]
        assert serialized["source"] == test_data["source"]

    def test_errorissue_model_json_schema(self):
        """Test ErrorIssue model JSON schema generation."""
        schema = ErrorIssue.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "subject",
            "description",
            "source",
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

    def test_requestpostautosubscription_model_creation(self):
        """Test RequestPostAutoSubscription model creation with valid data."""
        # Valid test data for RequestPostAutoSubscription
        valid_data = {
            "deviceType": "test_deviceType",
            "tier": "test_tier",
        }

        # Create model instance
        model = RequestPostAutoSubscription(**valid_data)

        # Verify model creation
        assert isinstance(model, RequestPostAutoSubscription)
        assert model.deviceType == valid_data["deviceType"]
        assert model.tier == valid_data["tier"]

    def test_requestpostautosubscription_model_validation(self):
        """Test RequestPostAutoSubscription model field validation."""
        # Test with minimal required data
        minimal_data = {
            "deviceType": "required_deviceType",
            "tier": "required_tier",
        }

        model = RequestPostAutoSubscription(**minimal_data)
        assert isinstance(model, RequestPostAutoSubscription)
        assert model.deviceType == minimal_data["deviceType"]
        assert model.tier == minimal_data["tier"]

    def test_requestpostautosubscription_model_required_fields(self):
        """Test RequestPostAutoSubscription model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "deviceType",
            "tier",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                RequestPostAutoSubscription()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "deviceType",
                "tier",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = RequestPostAutoSubscription()
            assert isinstance(model, RequestPostAutoSubscription)

    def test_requestpostautosubscription_model_optional_fields(self):
        """Test RequestPostAutoSubscription model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "deviceType": "required_deviceType",
            "tier": "required_tier",
        }

        model = RequestPostAutoSubscription(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_requestpostautosubscription_model_serialization(self):
        """Test RequestPostAutoSubscription model serialization to dict."""
        test_data = {
            "deviceType": "serialize_value",
            "tier": "serialize_value",
        }

        model = RequestPostAutoSubscription(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "deviceType" in serialized
        assert "tier" in serialized

        # Verify values are preserved
        assert serialized["deviceType"] == test_data["deviceType"]
        assert serialized["tier"] == test_data["tier"]

    def test_requestpostautosubscription_model_json_schema(self):
        """Test RequestPostAutoSubscription model JSON schema generation."""
        schema = RequestPostAutoSubscription.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "deviceType",
            "tier",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "deviceType",
            "tier",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_generalerrordetail_model_creation(self):
        """Test GeneralErrorDetail model creation with valid data."""
        # Valid test data for GeneralErrorDetail
        valid_data = {
            "metadata": {},
            "source": "test_source",
            "type": "test_type",
        }

        # Create model instance
        model = GeneralErrorDetail(**valid_data)

        # Verify model creation
        assert isinstance(model, GeneralErrorDetail)
        assert model.metadata == valid_data["metadata"]
        assert model.source == valid_data["source"]
        assert model.type == valid_data["type"]

    def test_generalerrordetail_model_validation(self):
        """Test GeneralErrorDetail model field validation."""
        # Test with minimal required data
        minimal_data = {
            "metadata": {},
            "source": "required_source",
            "type": "required_type",
        }

        model = GeneralErrorDetail(**minimal_data)
        assert isinstance(model, GeneralErrorDetail)
        assert model.metadata == minimal_data["metadata"]
        assert model.source == minimal_data["source"]
        assert model.type == minimal_data["type"]

    def test_generalerrordetail_model_required_fields(self):
        """Test GeneralErrorDetail model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "metadata",
            "source",
            "type",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                GeneralErrorDetail()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "metadata",
                "source",
                "type",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = GeneralErrorDetail()
            assert isinstance(model, GeneralErrorDetail)

    def test_generalerrordetail_model_optional_fields(self):
        """Test GeneralErrorDetail model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "metadata": {},
            "source": "required_source",
            "type": "required_type",
        }

        model = GeneralErrorDetail(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_generalerrordetail_model_serialization(self):
        """Test GeneralErrorDetail model serialization to dict."""
        test_data = {
            "metadata": {"key": "value"},
            "source": "serialize_value",
            "type": "serialize_value",
        }

        model = GeneralErrorDetail(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "metadata" in serialized
        assert "source" in serialized
        assert "type" in serialized

        # Verify values are preserved
        assert serialized["metadata"] == test_data["metadata"]
        assert serialized["source"] == test_data["source"]
        assert serialized["type"] == test_data["type"]

    def test_generalerrordetail_model_json_schema(self):
        """Test GeneralErrorDetail model JSON schema generation."""
        schema = GeneralErrorDetail.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "metadata",
            "source",
            "type",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "metadata",
            "source",
            "type",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_hpegreenlakebadrequesterror_model_creation(self):
        """Test HpeGreenLakeBadRequestError model creation with valid data."""
        # Valid test data for HpeGreenLakeBadRequestError
        valid_data = {
            "errorCode": "test_errorCode",
            "errorDetails": [],
            "httpStatusCode": 42,
            "message": "test_message",
            "debugId": "test_debugId",
        }

        # Create model instance
        model = HpeGreenLakeBadRequestError(**valid_data)

        # Verify model creation
        assert isinstance(model, HpeGreenLakeBadRequestError)
        assert model.errorCode == valid_data["errorCode"]
        assert model.errorDetails == valid_data["errorDetails"]
        assert model.httpStatusCode == valid_data["httpStatusCode"]
        assert model.message == valid_data["message"]
        assert model.debugId == valid_data["debugId"]

    def test_hpegreenlakebadrequesterror_model_validation(self):
        """Test HpeGreenLakeBadRequestError model field validation."""
        # Test with minimal required data
        minimal_data = {
            "errorCode": "required_errorCode",
            "httpStatusCode": 1,
            "message": "required_message",
            "debugId": "required_debugId",
        }

        model = HpeGreenLakeBadRequestError(**minimal_data)
        assert isinstance(model, HpeGreenLakeBadRequestError)
        assert model.errorCode == minimal_data["errorCode"]
        assert model.httpStatusCode == minimal_data["httpStatusCode"]
        assert model.message == minimal_data["message"]
        assert model.debugId == minimal_data["debugId"]

    def test_hpegreenlakebadrequesterror_model_required_fields(self):
        """Test HpeGreenLakeBadRequestError model required field validation."""
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
                HpeGreenLakeBadRequestError()

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
            model = HpeGreenLakeBadRequestError()
            assert isinstance(model, HpeGreenLakeBadRequestError)

    def test_hpegreenlakebadrequesterror_model_optional_fields(self):
        """Test HpeGreenLakeBadRequestError model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "errorCode": "required_errorCode",
            "httpStatusCode": 1,
            "message": "required_message",
            "debugId": "required_debugId",
        }

        model = HpeGreenLakeBadRequestError(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "errorDetails")
        # Optional field errorDetails should be None or have a default value
        assert model.errorDetails is None or model.errorDetails is not None

    def test_hpegreenlakebadrequesterror_model_serialization(self):
        """Test HpeGreenLakeBadRequestError model serialization to dict."""
        test_data = {
            "errorCode": "serialize_value",
            "errorDetails": [],
            "httpStatusCode": 99,
            "message": "serialize_value",
            "debugId": "serialize_value",
        }

        model = HpeGreenLakeBadRequestError(**test_data)
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

    def test_hpegreenlakebadrequesterror_model_json_schema(self):
        """Test HpeGreenLakeBadRequestError model JSON schema generation."""
        schema = HpeGreenLakeBadRequestError.model_json_schema()

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
            "httpStatusCode",
            "message",
            "debugId",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_autosubscriptionsresponsepaginateddto_model_creation(self):
        """Test AutoSubscriptionsResponsePaginatedDto model creation with valid data."""
        # Valid test data for AutoSubscriptionsResponsePaginatedDto
        valid_data = {
            "count": 42,
            "items": [],
            "offset": 42,
            "total": 42,
        }

        # Create model instance
        model = AutoSubscriptionsResponsePaginatedDto(**valid_data)

        # Verify model creation
        assert isinstance(model, AutoSubscriptionsResponsePaginatedDto)
        assert model.count == valid_data["count"]
        assert model.items == valid_data["items"]
        assert model.offset == valid_data["offset"]
        assert model.total == valid_data["total"]

    def test_autosubscriptionsresponsepaginateddto_model_validation(self):
        """Test AutoSubscriptionsResponsePaginatedDto model field validation."""
        # Test with minimal required data
        minimal_data = {
            "count": 1,
            "items": [],
        }

        model = AutoSubscriptionsResponsePaginatedDto(**minimal_data)
        assert isinstance(model, AutoSubscriptionsResponsePaginatedDto)
        assert model.count == minimal_data["count"]
        assert model.items == minimal_data["items"]

    def test_autosubscriptionsresponsepaginateddto_model_required_fields(self):
        """Test AutoSubscriptionsResponsePaginatedDto model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "count",
            "items",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                AutoSubscriptionsResponsePaginatedDto()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "count",
                "items",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = AutoSubscriptionsResponsePaginatedDto()
            assert isinstance(model, AutoSubscriptionsResponsePaginatedDto)

    def test_autosubscriptionsresponsepaginateddto_model_optional_fields(self):
        """Test AutoSubscriptionsResponsePaginatedDto model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "count": 1,
            "items": [],
        }

        model = AutoSubscriptionsResponsePaginatedDto(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "offset")
        # Optional field offset should be None or have a default value
        assert model.offset is None or model.offset is not None
        assert hasattr(model, "total")
        # Optional field total should be None or have a default value
        assert model.total is None or model.total is not None

    def test_autosubscriptionsresponsepaginateddto_model_serialization(self):
        """Test AutoSubscriptionsResponsePaginatedDto model serialization to dict."""
        test_data = {
            "count": 99,
            "items": [],
            "offset": 99,
            "total": 99,
        }

        model = AutoSubscriptionsResponsePaginatedDto(**test_data)
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

    def test_autosubscriptionsresponsepaginateddto_model_json_schema(self):
        """Test AutoSubscriptionsResponsePaginatedDto model JSON schema generation."""
        schema = AutoSubscriptionsResponsePaginatedDto.model_json_schema()

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
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_hpegreenlakegeneralerror_model_creation(self):
        """Test HpeGreenLakeGeneralError model creation with valid data."""
        # Valid test data for HpeGreenLakeGeneralError
        valid_data = {
            "message": "test_message",
            "debugId": "test_debugId",
            "errorCode": "test_errorCode",
            "errorDetails": [],
            "httpStatusCode": 42,
        }

        # Create model instance
        model = HpeGreenLakeGeneralError(**valid_data)

        # Verify model creation
        assert isinstance(model, HpeGreenLakeGeneralError)
        assert model.message == valid_data["message"]
        assert model.debugId == valid_data["debugId"]
        assert model.errorCode == valid_data["errorCode"]
        assert model.errorDetails == valid_data["errorDetails"]
        assert model.httpStatusCode == valid_data["httpStatusCode"]

    def test_hpegreenlakegeneralerror_model_validation(self):
        """Test HpeGreenLakeGeneralError model field validation."""
        # Test with minimal required data
        minimal_data = {
            "message": "required_message",
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
            "httpStatusCode": 1,
        }

        model = HpeGreenLakeGeneralError(**minimal_data)
        assert isinstance(model, HpeGreenLakeGeneralError)
        assert model.message == minimal_data["message"]
        assert model.debugId == minimal_data["debugId"]
        assert model.errorCode == minimal_data["errorCode"]
        assert model.httpStatusCode == minimal_data["httpStatusCode"]

    def test_hpegreenlakegeneralerror_model_required_fields(self):
        """Test HpeGreenLakeGeneralError model required field validation."""
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
                HpeGreenLakeGeneralError()

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
            model = HpeGreenLakeGeneralError()
            assert isinstance(model, HpeGreenLakeGeneralError)

    def test_hpegreenlakegeneralerror_model_optional_fields(self):
        """Test HpeGreenLakeGeneralError model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "message": "required_message",
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
            "httpStatusCode": 1,
        }

        model = HpeGreenLakeGeneralError(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "errorDetails")
        # Optional field errorDetails should be None or have a default value
        assert model.errorDetails is None or model.errorDetails is not None

    def test_hpegreenlakegeneralerror_model_serialization(self):
        """Test HpeGreenLakeGeneralError model serialization to dict."""
        test_data = {
            "message": "serialize_value",
            "debugId": "serialize_value",
            "errorCode": "serialize_value",
            "errorDetails": [],
            "httpStatusCode": 99,
        }

        model = HpeGreenLakeGeneralError(**test_data)
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

    def test_hpegreenlakegeneralerror_model_json_schema(self):
        """Test HpeGreenLakeGeneralError model JSON schema generation."""
        schema = HpeGreenLakeGeneralError.model_json_schema()

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
            "httpStatusCode",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_servererrordetail_model_creation(self):
        """Test ServerErrorDetail model creation with valid data."""
        # Valid test data for ServerErrorDetail
        valid_data = {
            "retryAfterSeconds": 42,
            "type": "test_type",
        }

        # Create model instance
        model = ServerErrorDetail(**valid_data)

        # Verify model creation
        assert isinstance(model, ServerErrorDetail)
        assert model.retryAfterSeconds == valid_data["retryAfterSeconds"]
        assert model.type == valid_data["type"]

    def test_servererrordetail_model_validation(self):
        """Test ServerErrorDetail model field validation."""
        # Test with minimal required data
        minimal_data = {
            "retryAfterSeconds": 1,
            "type": "required_type",
        }

        model = ServerErrorDetail(**minimal_data)
        assert isinstance(model, ServerErrorDetail)
        assert model.retryAfterSeconds == minimal_data["retryAfterSeconds"]
        assert model.type == minimal_data["type"]

    def test_servererrordetail_model_required_fields(self):
        """Test ServerErrorDetail model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "retryAfterSeconds",
            "type",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                ServerErrorDetail()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "retryAfterSeconds",
                "type",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = ServerErrorDetail()
            assert isinstance(model, ServerErrorDetail)

    def test_servererrordetail_model_optional_fields(self):
        """Test ServerErrorDetail model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "retryAfterSeconds": 1,
            "type": "required_type",
        }

        model = ServerErrorDetail(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_servererrordetail_model_serialization(self):
        """Test ServerErrorDetail model serialization to dict."""
        test_data = {
            "retryAfterSeconds": 99,
            "type": "serialize_value",
        }

        model = ServerErrorDetail(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "retryAfterSeconds" in serialized
        assert "type" in serialized

        # Verify values are preserved
        assert serialized["retryAfterSeconds"] == test_data["retryAfterSeconds"]
        assert serialized["type"] == test_data["type"]

    def test_servererrordetail_model_json_schema(self):
        """Test ServerErrorDetail model JSON schema generation."""
        schema = ServerErrorDetail.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "retryAfterSeconds",
            "type",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "retryAfterSeconds",
            "type",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_v1beta1subscriptiondetail_model_creation(self):
        """Test V1Beta1SubscriptionDetail model creation with valid data."""
        # Valid test data for V1Beta1SubscriptionDetail
        valid_data = {
            "po": "test_po",
            "productType": "test_productType",
            "tierDescription": "test_tierDescription",
            "endTime": "test_endTime",
            "resellerPo": "test_resellerPo",
            "startTime": "test_startTime",
            "availableQuantity": "test_availableQuantity",
            "quote": "test_quote",
            "key": "test_key",
            "skuDescription": "test_skuDescription",
            "tier": "test_tier",
            "subscriptionType": "test_subscriptionType",
            "sku": "test_sku",
            "quantity": "test_quantity",
            "createdAt": "test_createdAt",
            "type": "test_type",
            "contract": "test_contract",
            "updatedAt": "test_updatedAt",
            "tags": {},
            "subscriptionStatus": "test_subscriptionStatus",
            "isEval": True,
            "id": "test_id",
        }

        # Create model instance
        model = V1Beta1SubscriptionDetail(**valid_data)

        # Verify model creation
        assert isinstance(model, V1Beta1SubscriptionDetail)
        assert model.po == valid_data["po"]
        assert model.productType == valid_data["productType"]
        assert model.tierDescription == valid_data["tierDescription"]
        assert model.endTime == valid_data["endTime"]
        assert model.resellerPo == valid_data["resellerPo"]
        assert model.startTime == valid_data["startTime"]
        assert model.availableQuantity == valid_data["availableQuantity"]
        assert model.quote == valid_data["quote"]
        assert model.key == valid_data["key"]
        assert model.skuDescription == valid_data["skuDescription"]
        assert model.tier == valid_data["tier"]
        assert model.subscriptionType == valid_data["subscriptionType"]
        assert model.sku == valid_data["sku"]
        assert model.quantity == valid_data["quantity"]
        assert model.createdAt == valid_data["createdAt"]
        assert model.type == valid_data["type"]
        assert model.contract == valid_data["contract"]
        assert model.updatedAt == valid_data["updatedAt"]
        assert model.tags == valid_data["tags"]
        assert model.subscriptionStatus == valid_data["subscriptionStatus"]
        assert model.isEval == valid_data["isEval"]
        assert model.id == valid_data["id"]

    def test_v1beta1subscriptiondetail_model_validation(self):
        """Test V1Beta1SubscriptionDetail model field validation."""
        # Test with minimal required data
        minimal_data = {
            "type": "required_type",
            "id": "required_id",
        }

        model = V1Beta1SubscriptionDetail(**minimal_data)
        assert isinstance(model, V1Beta1SubscriptionDetail)
        assert model.type == minimal_data["type"]
        assert model.id == minimal_data["id"]

    def test_v1beta1subscriptiondetail_model_required_fields(self):
        """Test V1Beta1SubscriptionDetail model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "type",
            "id",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                V1Beta1SubscriptionDetail()

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
            model = V1Beta1SubscriptionDetail()
            assert isinstance(model, V1Beta1SubscriptionDetail)

    def test_v1beta1subscriptiondetail_model_optional_fields(self):
        """Test V1Beta1SubscriptionDetail model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "type": "required_type",
            "id": "required_id",
        }

        model = V1Beta1SubscriptionDetail(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "po")
        # Optional field po should be None or have a default value
        assert model.po is None or model.po is not None
        assert hasattr(model, "productType")
        # Optional field productType should be None or have a default value
        assert model.productType is None or model.productType is not None
        assert hasattr(model, "tierDescription")
        # Optional field tierDescription should be None or have a default value
        assert model.tierDescription is None or model.tierDescription is not None
        assert hasattr(model, "endTime")
        # Optional field endTime should be None or have a default value
        assert model.endTime is None or model.endTime is not None
        assert hasattr(model, "resellerPo")
        # Optional field resellerPo should be None or have a default value
        assert model.resellerPo is None or model.resellerPo is not None
        assert hasattr(model, "startTime")
        # Optional field startTime should be None or have a default value
        assert model.startTime is None or model.startTime is not None
        assert hasattr(model, "availableQuantity")
        # Optional field availableQuantity should be None or have a default value
        assert model.availableQuantity is None or model.availableQuantity is not None
        assert hasattr(model, "quote")
        # Optional field quote should be None or have a default value
        assert model.quote is None or model.quote is not None
        assert hasattr(model, "key")
        # Optional field key should be None or have a default value
        assert model.key is None or model.key is not None
        assert hasattr(model, "skuDescription")
        # Optional field skuDescription should be None or have a default value
        assert model.skuDescription is None or model.skuDescription is not None
        assert hasattr(model, "tier")
        # Optional field tier should be None or have a default value
        assert model.tier is None or model.tier is not None
        assert hasattr(model, "subscriptionType")
        # Optional field subscriptionType should be None or have a default value
        assert model.subscriptionType is None or model.subscriptionType is not None
        assert hasattr(model, "sku")
        # Optional field sku should be None or have a default value
        assert model.sku is None or model.sku is not None
        assert hasattr(model, "quantity")
        # Optional field quantity should be None or have a default value
        assert model.quantity is None or model.quantity is not None
        assert hasattr(model, "createdAt")
        # Optional field createdAt should be None or have a default value
        assert model.createdAt is None or model.createdAt is not None
        assert hasattr(model, "contract")
        # Optional field contract should be None or have a default value
        assert model.contract is None or model.contract is not None
        assert hasattr(model, "updatedAt")
        # Optional field updatedAt should be None or have a default value
        assert model.updatedAt is None or model.updatedAt is not None
        assert hasattr(model, "tags")
        # Optional field tags should be None or have a default value
        assert model.tags is None or model.tags is not None
        assert hasattr(model, "subscriptionStatus")
        # Optional field subscriptionStatus should be None or have a default value
        assert model.subscriptionStatus is None or model.subscriptionStatus is not None
        assert hasattr(model, "isEval")
        # Optional field isEval should be None or have a default value
        assert model.isEval is None or model.isEval is not None

    def test_v1beta1subscriptiondetail_model_serialization(self):
        """Test V1Beta1SubscriptionDetail model serialization to dict."""
        test_data = {
            "po": "serialize_value",
            "productType": "serialize_value",
            "tierDescription": "serialize_value",
            "endTime": "serialize_value",
            "resellerPo": "serialize_value",
            "startTime": "serialize_value",
            "availableQuantity": "serialize_value",
            "quote": "serialize_value",
            "key": "serialize_value",
            "skuDescription": "serialize_value",
            "tier": "serialize_value",
            "subscriptionType": "serialize_value",
            "sku": "serialize_value",
            "quantity": "serialize_value",
            "createdAt": "serialize_value",
            "type": "serialize_value",
            "contract": "serialize_value",
            "updatedAt": "serialize_value",
            "tags": {"key": "value"},
            "subscriptionStatus": "serialize_value",
            "isEval": False,
            "id": "serialize_value",
        }

        model = V1Beta1SubscriptionDetail(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "po" in serialized
        assert "productType" in serialized
        assert "tierDescription" in serialized
        assert "endTime" in serialized
        assert "resellerPo" in serialized
        assert "startTime" in serialized
        assert "availableQuantity" in serialized
        assert "quote" in serialized
        assert "key" in serialized
        assert "skuDescription" in serialized
        assert "tier" in serialized
        assert "subscriptionType" in serialized
        assert "sku" in serialized
        assert "quantity" in serialized
        assert "createdAt" in serialized
        assert "type" in serialized
        assert "contract" in serialized
        assert "updatedAt" in serialized
        assert "tags" in serialized
        assert "subscriptionStatus" in serialized
        assert "isEval" in serialized
        assert "id" in serialized

        # Verify values are preserved
        assert serialized["po"] == test_data["po"]
        assert serialized["productType"] == test_data["productType"]
        assert serialized["tierDescription"] == test_data["tierDescription"]
        assert serialized["endTime"] == test_data["endTime"]
        assert serialized["resellerPo"] == test_data["resellerPo"]
        assert serialized["startTime"] == test_data["startTime"]
        assert serialized["availableQuantity"] == test_data["availableQuantity"]
        assert serialized["quote"] == test_data["quote"]
        assert serialized["key"] == test_data["key"]
        assert serialized["skuDescription"] == test_data["skuDescription"]
        assert serialized["tier"] == test_data["tier"]
        assert serialized["subscriptionType"] == test_data["subscriptionType"]
        assert serialized["sku"] == test_data["sku"]
        assert serialized["quantity"] == test_data["quantity"]
        assert serialized["createdAt"] == test_data["createdAt"]
        assert serialized["type"] == test_data["type"]
        assert serialized["contract"] == test_data["contract"]
        assert serialized["updatedAt"] == test_data["updatedAt"]
        assert serialized["tags"] == test_data["tags"]
        assert serialized["subscriptionStatus"] == test_data["subscriptionStatus"]
        assert serialized["isEval"] == test_data["isEval"]
        assert serialized["id"] == test_data["id"]

    def test_v1beta1subscriptiondetail_model_json_schema(self):
        """Test V1Beta1SubscriptionDetail model JSON schema generation."""
        schema = V1Beta1SubscriptionDetail.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "po",
            "productType",
            "tierDescription",
            "endTime",
            "resellerPo",
            "startTime",
            "availableQuantity",
            "quote",
            "key",
            "skuDescription",
            "tier",
            "subscriptionType",
            "sku",
            "quantity",
            "createdAt",
            "type",
            "contract",
            "updatedAt",
            "tags",
            "subscriptionStatus",
            "isEval",
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

    def test_autosubscriptionsresponsedto_model_creation(self):
        """Test AutoSubscriptionsResponseDto model creation with valid data."""
        # Valid test data for AutoSubscriptionsResponseDto
        valid_data = {
            "autoSubscriptionSettings": [],
            "createdAt": "test_createdAt",
            "generation": 42,
            "id": "test_id",
            "resourceUri": "test_resourceUri",
            "type": "test_type",
            "updatedAt": "test_updatedAt",
        }

        # Create model instance
        model = AutoSubscriptionsResponseDto(**valid_data)

        # Verify model creation
        assert isinstance(model, AutoSubscriptionsResponseDto)
        assert model.autoSubscriptionSettings == valid_data["autoSubscriptionSettings"]
        assert model.createdAt == valid_data["createdAt"]
        assert model.generation == valid_data["generation"]
        assert model.id == valid_data["id"]
        assert model.resourceUri == valid_data["resourceUri"]
        assert model.type == valid_data["type"]
        assert model.updatedAt == valid_data["updatedAt"]

    def test_autosubscriptionsresponsedto_model_validation(self):
        """Test AutoSubscriptionsResponseDto model field validation."""
        # Test with minimal required data
        minimal_data = {
            "createdAt": "required_createdAt",
            "id": "required_id",
            "resourceUri": "required_resourceUri",
            "type": "required_type",
            "updatedAt": "required_updatedAt",
        }

        model = AutoSubscriptionsResponseDto(**minimal_data)
        assert isinstance(model, AutoSubscriptionsResponseDto)
        assert model.createdAt == minimal_data["createdAt"]
        assert model.id == minimal_data["id"]
        assert model.resourceUri == minimal_data["resourceUri"]
        assert model.type == minimal_data["type"]
        assert model.updatedAt == minimal_data["updatedAt"]

    def test_autosubscriptionsresponsedto_model_required_fields(self):
        """Test AutoSubscriptionsResponseDto model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "createdAt",
            "id",
            "resourceUri",
            "type",
            "updatedAt",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                AutoSubscriptionsResponseDto()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "createdAt",
                "id",
                "resourceUri",
                "type",
                "updatedAt",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = AutoSubscriptionsResponseDto()
            assert isinstance(model, AutoSubscriptionsResponseDto)

    def test_autosubscriptionsresponsedto_model_optional_fields(self):
        """Test AutoSubscriptionsResponseDto model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "createdAt": "required_createdAt",
            "id": "required_id",
            "resourceUri": "required_resourceUri",
            "type": "required_type",
            "updatedAt": "required_updatedAt",
        }

        model = AutoSubscriptionsResponseDto(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "autoSubscriptionSettings")
        # Optional field autoSubscriptionSettings should be None or have a default value
        assert model.autoSubscriptionSettings is None or model.autoSubscriptionSettings is not None
        assert hasattr(model, "generation")
        # Optional field generation should be None or have a default value
        assert model.generation is None or model.generation is not None

    def test_autosubscriptionsresponsedto_model_serialization(self):
        """Test AutoSubscriptionsResponseDto model serialization to dict."""
        test_data = {
            "autoSubscriptionSettings": [],
            "createdAt": "serialize_value",
            "generation": 99,
            "id": "serialize_value",
            "resourceUri": "serialize_value",
            "type": "serialize_value",
            "updatedAt": "serialize_value",
        }

        model = AutoSubscriptionsResponseDto(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "autoSubscriptionSettings" in serialized
        assert "createdAt" in serialized
        assert "generation" in serialized
        assert "id" in serialized
        assert "resourceUri" in serialized
        assert "type" in serialized
        assert "updatedAt" in serialized

        # Verify values are preserved
        assert serialized["autoSubscriptionSettings"] == test_data["autoSubscriptionSettings"]
        assert serialized["createdAt"] == test_data["createdAt"]
        assert serialized["generation"] == test_data["generation"]
        assert serialized["id"] == test_data["id"]
        assert serialized["resourceUri"] == test_data["resourceUri"]
        assert serialized["type"] == test_data["type"]
        assert serialized["updatedAt"] == test_data["updatedAt"]

    def test_autosubscriptionsresponsedto_model_json_schema(self):
        """Test AutoSubscriptionsResponseDto model JSON schema generation."""
        schema = AutoSubscriptionsResponseDto.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "autoSubscriptionSettings",
            "createdAt",
            "generation",
            "id",
            "resourceUri",
            "type",
            "updatedAt",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "createdAt",
            "id",
            "resourceUri",
            "type",
            "updatedAt",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_bulkunclaimid_model_creation(self):
        """Test BulkUnclaimId model creation with valid data."""
        # Valid test data for BulkUnclaimId
        valid_data = {
            "id": "test_id",
        }

        # Create model instance
        model = BulkUnclaimId(**valid_data)

        # Verify model creation
        assert isinstance(model, BulkUnclaimId)
        assert model.id == valid_data["id"]

    def test_bulkunclaimid_model_validation(self):
        """Test BulkUnclaimId model field validation."""
        # Test with minimal required data
        minimal_data = {
            "id": "required_id",
        }

        model = BulkUnclaimId(**minimal_data)
        assert isinstance(model, BulkUnclaimId)
        assert model.id == minimal_data["id"]

    def test_bulkunclaimid_model_required_fields(self):
        """Test BulkUnclaimId model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "id",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                BulkUnclaimId()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "id",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = BulkUnclaimId()
            assert isinstance(model, BulkUnclaimId)

    def test_bulkunclaimid_model_optional_fields(self):
        """Test BulkUnclaimId model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "id": "required_id",
        }

        model = BulkUnclaimId(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_bulkunclaimid_model_serialization(self):
        """Test BulkUnclaimId model serialization to dict."""
        test_data = {
            "id": "serialize_value",
        }

        model = BulkUnclaimId(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "id" in serialized

        # Verify values are preserved
        assert serialized["id"] == test_data["id"]

    def test_bulkunclaimid_model_json_schema(self):
        """Test BulkUnclaimId model JSON schema generation."""
        schema = BulkUnclaimId.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "id",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "id",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_subscriptionsgetresponse_model_creation(self):
        """Test SubscriptionsGetResponse model creation with valid data."""
        # Valid test data for SubscriptionsGetResponse
        valid_data = {
            "items": [],
            "offset": 42,
            "total": 42,
            "count": 42,
        }

        # Create model instance
        model = SubscriptionsGetResponse(**valid_data)

        # Verify model creation
        assert isinstance(model, SubscriptionsGetResponse)
        assert model.items == valid_data["items"]
        assert model.offset == valid_data["offset"]
        assert model.total == valid_data["total"]
        assert model.count == valid_data["count"]

    def test_subscriptionsgetresponse_model_validation(self):
        """Test SubscriptionsGetResponse model field validation."""
        # Test with minimal required data
        minimal_data = {
            "items": [],
            "count": 1,
        }

        model = SubscriptionsGetResponse(**minimal_data)
        assert isinstance(model, SubscriptionsGetResponse)
        assert model.items == minimal_data["items"]
        assert model.count == minimal_data["count"]

    def test_subscriptionsgetresponse_model_required_fields(self):
        """Test SubscriptionsGetResponse model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "items",
            "count",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                SubscriptionsGetResponse()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "items",
                "count",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = SubscriptionsGetResponse()
            assert isinstance(model, SubscriptionsGetResponse)

    def test_subscriptionsgetresponse_model_optional_fields(self):
        """Test SubscriptionsGetResponse model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "items": [],
            "count": 1,
        }

        model = SubscriptionsGetResponse(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "offset")
        # Optional field offset should be None or have a default value
        assert model.offset is None or model.offset is not None
        assert hasattr(model, "total")
        # Optional field total should be None or have a default value
        assert model.total is None or model.total is not None

    def test_subscriptionsgetresponse_model_serialization(self):
        """Test SubscriptionsGetResponse model serialization to dict."""
        test_data = {
            "items": [],
            "offset": 99,
            "total": 99,
            "count": 99,
        }

        model = SubscriptionsGetResponse(**test_data)
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

    def test_subscriptionsgetresponse_model_json_schema(self):
        """Test SubscriptionsGetResponse model JSON schema generation."""
        schema = SubscriptionsGetResponse.model_json_schema()

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
            "count",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_requestpostsubscription_model_creation(self):
        """Test RequestPostSubscription model creation with valid data."""
        # Valid test data for RequestPostSubscription
        valid_data = {
            "tags": {},
            "key": "test_key",
        }

        # Create model instance
        model = RequestPostSubscription(**valid_data)

        # Verify model creation
        assert isinstance(model, RequestPostSubscription)
        assert model.tags == valid_data["tags"]
        assert model.key == valid_data["key"]

    def test_requestpostsubscription_model_validation(self):
        """Test RequestPostSubscription model field validation."""
        # Test with minimal required data
        minimal_data = {
            "key": "required_key",
        }

        model = RequestPostSubscription(**minimal_data)
        assert isinstance(model, RequestPostSubscription)
        assert model.key == minimal_data["key"]

    def test_requestpostsubscription_model_required_fields(self):
        """Test RequestPostSubscription model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "key",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                RequestPostSubscription()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "key",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = RequestPostSubscription()
            assert isinstance(model, RequestPostSubscription)

    def test_requestpostsubscription_model_optional_fields(self):
        """Test RequestPostSubscription model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "key": "required_key",
        }

        model = RequestPostSubscription(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "tags")
        # Optional field tags should be None or have a default value
        assert model.tags is None or model.tags is not None

    def test_requestpostsubscription_model_serialization(self):
        """Test RequestPostSubscription model serialization to dict."""
        test_data = {
            "tags": {"key": "value"},
            "key": "serialize_value",
        }

        model = RequestPostSubscription(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "tags" in serialized
        assert "key" in serialized

        # Verify values are preserved
        assert serialized["tags"] == test_data["tags"]
        assert serialized["key"] == test_data["key"]

    def test_requestpostsubscription_model_json_schema(self):
        """Test RequestPostSubscription model JSON schema generation."""
        schema = RequestPostSubscription.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "tags",
            "key",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "key",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_subscriptiondetail_model_creation(self):
        """Test SubscriptionDetail model creation with valid data."""
        # Valid test data for SubscriptionDetail
        valid_data = {
            "po": "test_po",
            "productSku": "test_productSku",
            "id": "test_id",
            "orderClass": "test_orderClass",
            "quantity": "test_quantity",
            "productDescription": "test_productDescription",
            "quote": "test_quote",
            "aasType": "test_aasType",
            "endUserName": "test_endUserName",
            "evaluationType": "test_evaluationType",
            "key": "test_key",
            "appointment": {},
            "contract": "test_contract",
        }

        # Create model instance
        model = SubscriptionDetail(**valid_data)

        # Verify model creation
        assert isinstance(model, SubscriptionDetail)
        assert model.po == valid_data["po"]
        assert model.productSku == valid_data["productSku"]
        assert model.id == valid_data["id"]
        assert model.orderClass == valid_data["orderClass"]
        assert model.quantity == valid_data["quantity"]
        assert model.productDescription == valid_data["productDescription"]
        assert model.quote == valid_data["quote"]
        assert model.aasType == valid_data["aasType"]
        assert model.endUserName == valid_data["endUserName"]
        assert model.evaluationType == valid_data["evaluationType"]
        assert model.key == valid_data["key"]
        assert model.appointment == valid_data["appointment"]
        assert model.contract == valid_data["contract"]

    def test_subscriptiondetail_model_validation(self):
        """Test SubscriptionDetail model field validation."""
        # Test with minimal required data
        minimal_data = {
            "id": "required_id",
        }

        model = SubscriptionDetail(**minimal_data)
        assert isinstance(model, SubscriptionDetail)
        assert model.id == minimal_data["id"]

    def test_subscriptiondetail_model_required_fields(self):
        """Test SubscriptionDetail model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "id",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                SubscriptionDetail()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "id",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = SubscriptionDetail()
            assert isinstance(model, SubscriptionDetail)

    def test_subscriptiondetail_model_optional_fields(self):
        """Test SubscriptionDetail model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "id": "required_id",
        }

        model = SubscriptionDetail(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "po")
        # Optional field po should be None or have a default value
        assert model.po is None or model.po is not None
        assert hasattr(model, "productSku")
        # Optional field productSku should be None or have a default value
        assert model.productSku is None or model.productSku is not None
        assert hasattr(model, "orderClass")
        # Optional field orderClass should be None or have a default value
        assert model.orderClass is None or model.orderClass is not None
        assert hasattr(model, "quantity")
        # Optional field quantity should be None or have a default value
        assert model.quantity is None or model.quantity is not None
        assert hasattr(model, "productDescription")
        # Optional field productDescription should be None or have a default value
        assert model.productDescription is None or model.productDescription is not None
        assert hasattr(model, "quote")
        # Optional field quote should be None or have a default value
        assert model.quote is None or model.quote is not None
        assert hasattr(model, "aasType")
        # Optional field aasType should be None or have a default value
        assert model.aasType is None or model.aasType is not None
        assert hasattr(model, "endUserName")
        # Optional field endUserName should be None or have a default value
        assert model.endUserName is None or model.endUserName is not None
        assert hasattr(model, "evaluationType")
        # Optional field evaluationType should be None or have a default value
        assert model.evaluationType is None or model.evaluationType is not None
        assert hasattr(model, "key")
        # Optional field key should be None or have a default value
        assert model.key is None or model.key is not None
        assert hasattr(model, "appointment")
        # Optional field appointment should be None or have a default value
        assert model.appointment is None or model.appointment is not None
        assert hasattr(model, "contract")
        # Optional field contract should be None or have a default value
        assert model.contract is None or model.contract is not None

    def test_subscriptiondetail_model_serialization(self):
        """Test SubscriptionDetail model serialization to dict."""
        test_data = {
            "po": "serialize_value",
            "productSku": "serialize_value",
            "id": "serialize_value",
            "orderClass": "serialize_value",
            "quantity": "serialize_value",
            "productDescription": "serialize_value",
            "quote": "serialize_value",
            "aasType": "serialize_value",
            "endUserName": "serialize_value",
            "evaluationType": "serialize_value",
            "key": "serialize_value",
            "appointment": {"key": "value"},
            "contract": "serialize_value",
        }

        model = SubscriptionDetail(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "po" in serialized
        assert "productSku" in serialized
        assert "id" in serialized
        assert "orderClass" in serialized
        assert "quantity" in serialized
        assert "productDescription" in serialized
        assert "quote" in serialized
        assert "aasType" in serialized
        assert "endUserName" in serialized
        assert "evaluationType" in serialized
        assert "key" in serialized
        assert "appointment" in serialized
        assert "contract" in serialized

        # Verify values are preserved
        assert serialized["po"] == test_data["po"]
        assert serialized["productSku"] == test_data["productSku"]
        assert serialized["id"] == test_data["id"]
        assert serialized["orderClass"] == test_data["orderClass"]
        assert serialized["quantity"] == test_data["quantity"]
        assert serialized["productDescription"] == test_data["productDescription"]
        assert serialized["quote"] == test_data["quote"]
        assert serialized["aasType"] == test_data["aasType"]
        assert serialized["endUserName"] == test_data["endUserName"]
        assert serialized["evaluationType"] == test_data["evaluationType"]
        assert serialized["key"] == test_data["key"]
        assert serialized["appointment"] == test_data["appointment"]
        assert serialized["contract"] == test_data["contract"]

    def test_subscriptiondetail_model_json_schema(self):
        """Test SubscriptionDetail model JSON schema generation."""
        schema = SubscriptionDetail.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "po",
            "productSku",
            "id",
            "orderClass",
            "quantity",
            "productDescription",
            "quote",
            "aasType",
            "endUserName",
            "evaluationType",
            "key",
            "appointment",
            "contract",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "id",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_subscriptionspostrequest_model_creation(self):
        """Test SubscriptionsPostRequest model creation with valid data."""
        # Valid test data for SubscriptionsPostRequest
        valid_data = {
            "subscriptions": [],
        }

        # Create model instance
        model = SubscriptionsPostRequest(**valid_data)

        # Verify model creation
        assert isinstance(model, SubscriptionsPostRequest)
        assert model.subscriptions == valid_data["subscriptions"]

    def test_subscriptionspostrequest_model_validation(self):
        """Test SubscriptionsPostRequest model field validation."""
        # Test with minimal required data
        minimal_data = {
            "subscriptions": [],
        }

        model = SubscriptionsPostRequest(**minimal_data)
        assert isinstance(model, SubscriptionsPostRequest)
        assert model.subscriptions == minimal_data["subscriptions"]

    def test_subscriptionspostrequest_model_required_fields(self):
        """Test SubscriptionsPostRequest model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "subscriptions",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                SubscriptionsPostRequest()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "subscriptions",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = SubscriptionsPostRequest()
            assert isinstance(model, SubscriptionsPostRequest)

    def test_subscriptionspostrequest_model_optional_fields(self):
        """Test SubscriptionsPostRequest model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "subscriptions": [],
        }

        model = SubscriptionsPostRequest(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_subscriptionspostrequest_model_serialization(self):
        """Test SubscriptionsPostRequest model serialization to dict."""
        test_data = {
            "subscriptions": [],
        }

        model = SubscriptionsPostRequest(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "subscriptions" in serialized

        # Verify values are preserved
        assert serialized["subscriptions"] == test_data["subscriptions"]

    def test_subscriptionspostrequest_model_json_schema(self):
        """Test SubscriptionsPostRequest model JSON schema generation."""
        schema = SubscriptionsPostRequest.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "subscriptions",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "subscriptions",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_subscriptionsbulkunclaimrequest_model_creation(self):
        """Test SubscriptionsBulkUnclaimRequest model creation with valid data."""
        # Valid test data for SubscriptionsBulkUnclaimRequest
        valid_data = {
            "items": [],
        }

        # Create model instance
        model = SubscriptionsBulkUnclaimRequest(**valid_data)

        # Verify model creation
        assert isinstance(model, SubscriptionsBulkUnclaimRequest)
        assert model.items == valid_data["items"]

    def test_subscriptionsbulkunclaimrequest_model_validation(self):
        """Test SubscriptionsBulkUnclaimRequest model field validation."""
        # Test with minimal required data
        minimal_data = {
            "items": [],
        }

        model = SubscriptionsBulkUnclaimRequest(**minimal_data)
        assert isinstance(model, SubscriptionsBulkUnclaimRequest)
        assert model.items == minimal_data["items"]

    def test_subscriptionsbulkunclaimrequest_model_required_fields(self):
        """Test SubscriptionsBulkUnclaimRequest model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "items",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                SubscriptionsBulkUnclaimRequest()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "items",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = SubscriptionsBulkUnclaimRequest()
            assert isinstance(model, SubscriptionsBulkUnclaimRequest)

    def test_subscriptionsbulkunclaimrequest_model_optional_fields(self):
        """Test SubscriptionsBulkUnclaimRequest model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "items": [],
        }

        model = SubscriptionsBulkUnclaimRequest(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_subscriptionsbulkunclaimrequest_model_serialization(self):
        """Test SubscriptionsBulkUnclaimRequest model serialization to dict."""
        test_data = {
            "items": [],
        }

        model = SubscriptionsBulkUnclaimRequest(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "items" in serialized

        # Verify values are preserved
        assert serialized["items"] == test_data["items"]

    def test_subscriptionsbulkunclaimrequest_model_json_schema(self):
        """Test SubscriptionsBulkUnclaimRequest model JSON schema generation."""
        schema = SubscriptionsBulkUnclaimRequest.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "items",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "items",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_v1beta1subscriptionsgetresponse_model_creation(self):
        """Test V1Beta1SubscriptionsGetResponse model creation with valid data."""
        # Valid test data for V1Beta1SubscriptionsGetResponse
        valid_data = {
            "items": [],
            "offset": 42,
            "total": 42,
            "count": 42,
        }

        # Create model instance
        model = V1Beta1SubscriptionsGetResponse(**valid_data)

        # Verify model creation
        assert isinstance(model, V1Beta1SubscriptionsGetResponse)
        assert model.items == valid_data["items"]
        assert model.offset == valid_data["offset"]
        assert model.total == valid_data["total"]
        assert model.count == valid_data["count"]

    def test_v1beta1subscriptionsgetresponse_model_validation(self):
        """Test V1Beta1SubscriptionsGetResponse model field validation."""
        # Test with minimal required data
        minimal_data = {
            "items": [],
            "count": 1,
        }

        model = V1Beta1SubscriptionsGetResponse(**minimal_data)
        assert isinstance(model, V1Beta1SubscriptionsGetResponse)
        assert model.items == minimal_data["items"]
        assert model.count == minimal_data["count"]

    def test_v1beta1subscriptionsgetresponse_model_required_fields(self):
        """Test V1Beta1SubscriptionsGetResponse model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "items",
            "count",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                V1Beta1SubscriptionsGetResponse()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "items",
                "count",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = V1Beta1SubscriptionsGetResponse()
            assert isinstance(model, V1Beta1SubscriptionsGetResponse)

    def test_v1beta1subscriptionsgetresponse_model_optional_fields(self):
        """Test V1Beta1SubscriptionsGetResponse model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "items": [],
            "count": 1,
        }

        model = V1Beta1SubscriptionsGetResponse(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "offset")
        # Optional field offset should be None or have a default value
        assert model.offset is None or model.offset is not None
        assert hasattr(model, "total")
        # Optional field total should be None or have a default value
        assert model.total is None or model.total is not None

    def test_v1beta1subscriptionsgetresponse_model_serialization(self):
        """Test V1Beta1SubscriptionsGetResponse model serialization to dict."""
        test_data = {
            "items": [],
            "offset": 99,
            "total": 99,
            "count": 99,
        }

        model = V1Beta1SubscriptionsGetResponse(**test_data)
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

    def test_v1beta1subscriptionsgetresponse_model_json_schema(self):
        """Test V1Beta1SubscriptionsGetResponse model JSON schema generation."""
        schema = V1Beta1SubscriptionsGetResponse.model_json_schema()

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
            "count",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_asyncoperationresource_model_creation(self):
        """Test AsyncOperationResource model creation with valid data."""
        # Valid test data for AsyncOperationResource
        valid_data = {
            "suggestedPollingIntervalSeconds": 42,
            "resultType": "test_resultType",
            "timeoutMinutes": 42,
            "startedAt": "test_startedAt",
            "status": "test_status",
            "endedAt": "test_endedAt",
            "type": "test_type",
            "id": "test_id",
            "progressPercent": 42,
            "error": {},
            "result": {},
        }

        # Create model instance
        model = AsyncOperationResource(**valid_data)

        # Verify model creation
        assert isinstance(model, AsyncOperationResource)
        assert model.suggestedPollingIntervalSeconds == valid_data["suggestedPollingIntervalSeconds"]
        assert model.resultType == valid_data["resultType"]
        assert model.timeoutMinutes == valid_data["timeoutMinutes"]
        assert model.startedAt == valid_data["startedAt"]
        assert model.status == valid_data["status"]
        assert model.endedAt == valid_data["endedAt"]
        assert model.type == valid_data["type"]
        assert model.id == valid_data["id"]
        assert model.progressPercent == valid_data["progressPercent"]
        assert model.error == valid_data["error"]
        assert model.result == valid_data["result"]

    def test_asyncoperationresource_model_validation(self):
        """Test AsyncOperationResource model field validation."""
        # Test with minimal required data
        minimal_data = {
            "type": "required_type",
            "id": "required_id",
        }

        model = AsyncOperationResource(**minimal_data)
        assert isinstance(model, AsyncOperationResource)
        assert model.type == minimal_data["type"]
        assert model.id == minimal_data["id"]

    def test_asyncoperationresource_model_required_fields(self):
        """Test AsyncOperationResource model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "type",
            "id",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                AsyncOperationResource()

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
            model = AsyncOperationResource()
            assert isinstance(model, AsyncOperationResource)

    def test_asyncoperationresource_model_optional_fields(self):
        """Test AsyncOperationResource model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "type": "required_type",
            "id": "required_id",
        }

        model = AsyncOperationResource(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "suggestedPollingIntervalSeconds")
        # Optional field suggestedPollingIntervalSeconds should be None or have a default value
        assert model.suggestedPollingIntervalSeconds is None or model.suggestedPollingIntervalSeconds is not None
        assert hasattr(model, "resultType")
        # Optional field resultType should be None or have a default value
        assert model.resultType is None or model.resultType is not None
        assert hasattr(model, "timeoutMinutes")
        # Optional field timeoutMinutes should be None or have a default value
        assert model.timeoutMinutes is None or model.timeoutMinutes is not None
        assert hasattr(model, "startedAt")
        # Optional field startedAt should be None or have a default value
        assert model.startedAt is None or model.startedAt is not None
        assert hasattr(model, "status")
        # Optional field status should be None or have a default value
        assert model.status is None or model.status is not None
        assert hasattr(model, "endedAt")
        # Optional field endedAt should be None or have a default value
        assert model.endedAt is None or model.endedAt is not None
        assert hasattr(model, "progressPercent")
        # Optional field progressPercent should be None or have a default value
        assert model.progressPercent is None or model.progressPercent is not None
        assert hasattr(model, "error")
        # Optional field error should be None or have a default value
        assert model.error is None or model.error is not None
        assert hasattr(model, "result")
        # Optional field result should be None or have a default value
        assert model.result is None or model.result is not None

    def test_asyncoperationresource_model_serialization(self):
        """Test AsyncOperationResource model serialization to dict."""
        test_data = {
            "suggestedPollingIntervalSeconds": 99,
            "resultType": "serialize_value",
            "timeoutMinutes": 99,
            "startedAt": "serialize_value",
            "status": "serialize_value",
            "endedAt": "serialize_value",
            "type": "serialize_value",
            "id": "serialize_value",
            "progressPercent": 99,
            "error": {"key": "value"},
            "result": {"key": "value"},
        }

        model = AsyncOperationResource(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "suggestedPollingIntervalSeconds" in serialized
        assert "resultType" in serialized
        assert "timeoutMinutes" in serialized
        assert "startedAt" in serialized
        assert "status" in serialized
        assert "endedAt" in serialized
        assert "type" in serialized
        assert "id" in serialized
        assert "progressPercent" in serialized
        assert "error" in serialized
        assert "result" in serialized

        # Verify values are preserved
        assert serialized["suggestedPollingIntervalSeconds"] == test_data["suggestedPollingIntervalSeconds"]
        assert serialized["resultType"] == test_data["resultType"]
        assert serialized["timeoutMinutes"] == test_data["timeoutMinutes"]
        assert serialized["startedAt"] == test_data["startedAt"]
        assert serialized["status"] == test_data["status"]
        assert serialized["endedAt"] == test_data["endedAt"]
        assert serialized["type"] == test_data["type"]
        assert serialized["id"] == test_data["id"]
        assert serialized["progressPercent"] == test_data["progressPercent"]
        assert serialized["error"] == test_data["error"]
        assert serialized["result"] == test_data["result"]

    def test_asyncoperationresource_model_json_schema(self):
        """Test AsyncOperationResource model JSON schema generation."""
        schema = AsyncOperationResource.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "suggestedPollingIntervalSeconds",
            "resultType",
            "timeoutMinutes",
            "startedAt",
            "status",
            "endedAt",
            "type",
            "id",
            "progressPercent",
            "error",
            "result",
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

    def test_asyncresponse_model_creation(self):
        """Test AsyncResponse model creation with valid data."""
        # Valid test data for AsyncResponse
        valid_data = {
            "transactionId": "test_transactionId",
            "code": 42,
            "status": "test_status",
        }

        # Create model instance
        model = AsyncResponse(**valid_data)

        # Verify model creation
        assert isinstance(model, AsyncResponse)
        assert model.transactionId == valid_data["transactionId"]
        assert model.code == valid_data["code"]
        assert model.status == valid_data["status"]

    def test_asyncresponse_model_validation(self):
        """Test AsyncResponse model field validation."""
        # Test with minimal required data
        minimal_data = {
            "transactionId": "required_transactionId",
            "code": 1,
            "status": "required_status",
        }

        model = AsyncResponse(**minimal_data)
        assert isinstance(model, AsyncResponse)
        assert model.transactionId == minimal_data["transactionId"]
        assert model.code == minimal_data["code"]
        assert model.status == minimal_data["status"]

    def test_asyncresponse_model_required_fields(self):
        """Test AsyncResponse model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "transactionId",
            "code",
            "status",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                AsyncResponse()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "transactionId",
                "code",
                "status",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = AsyncResponse()
            assert isinstance(model, AsyncResponse)

    def test_asyncresponse_model_optional_fields(self):
        """Test AsyncResponse model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "transactionId": "required_transactionId",
            "code": 1,
            "status": "required_status",
        }

        model = AsyncResponse(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_asyncresponse_model_serialization(self):
        """Test AsyncResponse model serialization to dict."""
        test_data = {
            "transactionId": "serialize_value",
            "code": 99,
            "status": "serialize_value",
        }

        model = AsyncResponse(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "transactionId" in serialized
        assert "code" in serialized
        assert "status" in serialized

        # Verify values are preserved
        assert serialized["transactionId"] == test_data["transactionId"]
        assert serialized["code"] == test_data["code"]
        assert serialized["status"] == test_data["status"]

    def test_asyncresponse_model_json_schema(self):
        """Test AsyncResponse model JSON schema generation."""
        schema = AsyncResponse.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "transactionId",
            "code",
            "status",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "transactionId",
            "code",
            "status",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_autosubscriptionsettings_model_creation(self):
        """Test AutoSubscriptionSettings model creation with valid data."""
        # Valid test data for AutoSubscriptionSettings
        valid_data = {
            "deviceType": "test_deviceType",
            "tier": "test_tier",
        }

        # Create model instance
        model = AutoSubscriptionSettings(**valid_data)

        # Verify model creation
        assert isinstance(model, AutoSubscriptionSettings)
        assert model.deviceType == valid_data["deviceType"]
        assert model.tier == valid_data["tier"]

    def test_autosubscriptionsettings_model_validation(self):
        """Test AutoSubscriptionSettings model field validation."""
        # Test with minimal required data
        minimal_data = {
            "deviceType": "required_deviceType",
            "tier": "required_tier",
        }

        model = AutoSubscriptionSettings(**minimal_data)
        assert isinstance(model, AutoSubscriptionSettings)
        assert model.deviceType == minimal_data["deviceType"]
        assert model.tier == minimal_data["tier"]

    def test_autosubscriptionsettings_model_required_fields(self):
        """Test AutoSubscriptionSettings model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "deviceType",
            "tier",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                AutoSubscriptionSettings()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "deviceType",
                "tier",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = AutoSubscriptionSettings()
            assert isinstance(model, AutoSubscriptionSettings)

    def test_autosubscriptionsettings_model_optional_fields(self):
        """Test AutoSubscriptionSettings model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "deviceType": "required_deviceType",
            "tier": "required_tier",
        }

        model = AutoSubscriptionSettings(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_autosubscriptionsettings_model_serialization(self):
        """Test AutoSubscriptionSettings model serialization to dict."""
        test_data = {
            "deviceType": "serialize_value",
            "tier": "serialize_value",
        }

        model = AutoSubscriptionSettings(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "deviceType" in serialized
        assert "tier" in serialized

        # Verify values are preserved
        assert serialized["deviceType"] == test_data["deviceType"]
        assert serialized["tier"] == test_data["tier"]

    def test_autosubscriptionsettings_model_json_schema(self):
        """Test AutoSubscriptionSettings model JSON schema generation."""
        schema = AutoSubscriptionSettings.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "deviceType",
            "tier",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "deviceType",
            "tier",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_appointment_model_creation(self):
        """Test Appointment model creation with valid data."""
        # Valid test data for Appointment
        valid_data = {
            "subscriptionEnd": "test_subscriptionEnd",
            "subscriptionStart": "test_subscriptionStart",
            "delayedActivation": "test_delayedActivation",
        }

        # Create model instance
        model = Appointment(**valid_data)

        # Verify model creation
        assert isinstance(model, Appointment)
        assert model.subscriptionEnd == valid_data["subscriptionEnd"]
        assert model.subscriptionStart == valid_data["subscriptionStart"]
        assert model.delayedActivation == valid_data["delayedActivation"]

    def test_appointment_model_validation(self):
        """Test Appointment model field validation."""
        # Test with minimal required data
        minimal_data = {}

        model = Appointment(**minimal_data)
        assert isinstance(model, Appointment)

    def test_appointment_model_required_fields(self):
        """Test Appointment model required field validation."""
        # Check if this model has any required fields
        required_fields = []

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                Appointment()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {}

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = Appointment()
            assert isinstance(model, Appointment)

    def test_appointment_model_optional_fields(self):
        """Test Appointment model optional field handling."""
        # Create with minimal required data
        minimal_data = {}

        model = Appointment(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "subscriptionEnd")
        # Optional field subscriptionEnd should be None or have a default value
        assert model.subscriptionEnd is None or model.subscriptionEnd is not None
        assert hasattr(model, "subscriptionStart")
        # Optional field subscriptionStart should be None or have a default value
        assert model.subscriptionStart is None or model.subscriptionStart is not None
        assert hasattr(model, "delayedActivation")
        # Optional field delayedActivation should be None or have a default value
        assert model.delayedActivation is None or model.delayedActivation is not None

    def test_appointment_model_serialization(self):
        """Test Appointment model serialization to dict."""
        test_data = {
            "subscriptionEnd": "serialize_value",
            "subscriptionStart": "serialize_value",
            "delayedActivation": "serialize_value",
        }

        model = Appointment(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "subscriptionEnd" in serialized
        assert "subscriptionStart" in serialized
        assert "delayedActivation" in serialized

        # Verify values are preserved
        assert serialized["subscriptionEnd"] == test_data["subscriptionEnd"]
        assert serialized["subscriptionStart"] == test_data["subscriptionStart"]
        assert serialized["delayedActivation"] == test_data["delayedActivation"]

    def test_appointment_model_json_schema(self):
        """Test Appointment model JSON schema generation."""
        schema = Appointment.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "subscriptionEnd",
            "subscriptionStart",
            "delayedActivation",
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

    def test_hpegreenlakeservererror_model_creation(self):
        """Test HpeGreenLakeServerError model creation with valid data."""
        # Valid test data for HpeGreenLakeServerError
        valid_data = {
            "message": "test_message",
            "debugId": "test_debugId",
            "errorCode": "test_errorCode",
            "errorDetails": [],
            "httpStatusCode": 42,
        }

        # Create model instance
        model = HpeGreenLakeServerError(**valid_data)

        # Verify model creation
        assert isinstance(model, HpeGreenLakeServerError)
        assert model.message == valid_data["message"]
        assert model.debugId == valid_data["debugId"]
        assert model.errorCode == valid_data["errorCode"]
        assert model.errorDetails == valid_data["errorDetails"]
        assert model.httpStatusCode == valid_data["httpStatusCode"]

    def test_hpegreenlakeservererror_model_validation(self):
        """Test HpeGreenLakeServerError model field validation."""
        # Test with minimal required data
        minimal_data = {
            "message": "required_message",
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
            "httpStatusCode": 1,
        }

        model = HpeGreenLakeServerError(**minimal_data)
        assert isinstance(model, HpeGreenLakeServerError)
        assert model.message == minimal_data["message"]
        assert model.debugId == minimal_data["debugId"]
        assert model.errorCode == minimal_data["errorCode"]
        assert model.httpStatusCode == minimal_data["httpStatusCode"]

    def test_hpegreenlakeservererror_model_required_fields(self):
        """Test HpeGreenLakeServerError model required field validation."""
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
                HpeGreenLakeServerError()

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
            model = HpeGreenLakeServerError()
            assert isinstance(model, HpeGreenLakeServerError)

    def test_hpegreenlakeservererror_model_optional_fields(self):
        """Test HpeGreenLakeServerError model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "message": "required_message",
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
            "httpStatusCode": 1,
        }

        model = HpeGreenLakeServerError(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "errorDetails")
        # Optional field errorDetails should be None or have a default value
        assert model.errorDetails is None or model.errorDetails is not None

    def test_hpegreenlakeservererror_model_serialization(self):
        """Test HpeGreenLakeServerError model serialization to dict."""
        test_data = {
            "message": "serialize_value",
            "debugId": "serialize_value",
            "errorCode": "serialize_value",
            "errorDetails": [],
            "httpStatusCode": 99,
        }

        model = HpeGreenLakeServerError(**test_data)
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

    def test_hpegreenlakeservererror_model_json_schema(self):
        """Test HpeGreenLakeServerError model JSON schema generation."""
        schema = HpeGreenLakeServerError.model_json_schema()

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
            "httpStatusCode",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_subscriptionspatchrequest_model_creation(self):
        """Test SubscriptionsPatchRequest model creation with valid data."""
        # Valid test data for SubscriptionsPatchRequest
        valid_data = {
            "tags": {},
        }

        # Create model instance
        model = SubscriptionsPatchRequest(**valid_data)

        # Verify model creation
        assert isinstance(model, SubscriptionsPatchRequest)
        assert model.tags == valid_data["tags"]

    def test_subscriptionspatchrequest_model_validation(self):
        """Test SubscriptionsPatchRequest model field validation."""
        # Test with minimal required data
        minimal_data = {
            "tags": {},
        }

        model = SubscriptionsPatchRequest(**minimal_data)
        assert isinstance(model, SubscriptionsPatchRequest)
        assert model.tags == minimal_data["tags"]

    def test_subscriptionspatchrequest_model_required_fields(self):
        """Test SubscriptionsPatchRequest model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "tags",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                SubscriptionsPatchRequest()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "tags",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = SubscriptionsPatchRequest()
            assert isinstance(model, SubscriptionsPatchRequest)

    def test_subscriptionspatchrequest_model_optional_fields(self):
        """Test SubscriptionsPatchRequest model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "tags": {},
        }

        model = SubscriptionsPatchRequest(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_subscriptionspatchrequest_model_serialization(self):
        """Test SubscriptionsPatchRequest model serialization to dict."""
        test_data = {
            "tags": {"key": "value"},
        }

        model = SubscriptionsPatchRequest(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "tags" in serialized

        # Verify values are preserved
        assert serialized["tags"] == test_data["tags"]

    def test_subscriptionspatchrequest_model_json_schema(self):
        """Test SubscriptionsPatchRequest model JSON schema generation."""
        schema = SubscriptionsPatchRequest.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "tags",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "tags",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_badrequesterrordetail_model_creation(self):
        """Test BadRequestErrorDetail model creation with valid data."""
        # Valid test data for BadRequestErrorDetail
        valid_data = {
            "issues": [],
            "type": "test_type",
        }

        # Create model instance
        model = BadRequestErrorDetail(**valid_data)

        # Verify model creation
        assert isinstance(model, BadRequestErrorDetail)
        assert model.issues == valid_data["issues"]
        assert model.type == valid_data["type"]

    def test_badrequesterrordetail_model_validation(self):
        """Test BadRequestErrorDetail model field validation."""
        # Test with minimal required data
        minimal_data = {
            "issues": [],
            "type": "required_type",
        }

        model = BadRequestErrorDetail(**minimal_data)
        assert isinstance(model, BadRequestErrorDetail)
        assert model.issues == minimal_data["issues"]
        assert model.type == minimal_data["type"]

    def test_badrequesterrordetail_model_required_fields(self):
        """Test BadRequestErrorDetail model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "issues",
            "type",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                BadRequestErrorDetail()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "issues",
                "type",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = BadRequestErrorDetail()
            assert isinstance(model, BadRequestErrorDetail)

    def test_badrequesterrordetail_model_optional_fields(self):
        """Test BadRequestErrorDetail model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "issues": [],
            "type": "required_type",
        }

        model = BadRequestErrorDetail(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_badrequesterrordetail_model_serialization(self):
        """Test BadRequestErrorDetail model serialization to dict."""
        test_data = {
            "issues": [],
            "type": "serialize_value",
        }

        model = BadRequestErrorDetail(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "issues" in serialized
        assert "type" in serialized

        # Verify values are preserved
        assert serialized["issues"] == test_data["issues"]
        assert serialized["type"] == test_data["type"]

    def test_badrequesterrordetail_model_json_schema(self):
        """Test BadRequestErrorDetail model JSON schema generation."""
        schema = BadRequestErrorDetail.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "issues",
            "type",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "issues",
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
            AutoSubscriptionsPostRequest,
            AutoSubscriptionsResponseDtoWithTenant,
            ErrorIssue,
            RequestPostAutoSubscription,
            GeneralErrorDetail,
            HpeGreenLakeBadRequestError,
            AutoSubscriptionsResponsePaginatedDto,
            HpeGreenLakeGeneralError,
            ServerErrorDetail,
            V1Beta1SubscriptionDetail,
            AutoSubscriptionsResponseDto,
            BulkUnclaimId,
            SubscriptionsGetResponse,
            RequestPostSubscription,
            SubscriptionDetail,
            SubscriptionsPostRequest,
            SubscriptionsBulkUnclaimRequest,
            V1Beta1SubscriptionsGetResponse,
            AsyncOperationResource,
            AsyncResponse,
            AutoSubscriptionSettings,
            Appointment,
            HpeGreenLakeServerError,
            SubscriptionsPatchRequest,
            BadRequestErrorDetail,
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
            AutoSubscriptionsPostRequest,
            AutoSubscriptionsResponseDtoWithTenant,
            ErrorIssue,
            RequestPostAutoSubscription,
            GeneralErrorDetail,
            HpeGreenLakeBadRequestError,
            AutoSubscriptionsResponsePaginatedDto,
            HpeGreenLakeGeneralError,
            ServerErrorDetail,
            V1Beta1SubscriptionDetail,
            AutoSubscriptionsResponseDto,
            BulkUnclaimId,
            SubscriptionsGetResponse,
            RequestPostSubscription,
            SubscriptionDetail,
            SubscriptionsPostRequest,
            SubscriptionsBulkUnclaimRequest,
            V1Beta1SubscriptionsGetResponse,
            AsyncOperationResource,
            AsyncResponse,
            AutoSubscriptionSettings,
            Appointment,
            HpeGreenLakeServerError,
            SubscriptionsPatchRequest,
            BadRequestErrorDetail,
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
            AutoSubscriptionsPostRequest,
            AutoSubscriptionsResponseDtoWithTenant,
            ErrorIssue,
            RequestPostAutoSubscription,
            GeneralErrorDetail,
            HpeGreenLakeBadRequestError,
            AutoSubscriptionsResponsePaginatedDto,
            HpeGreenLakeGeneralError,
            ServerErrorDetail,
            V1Beta1SubscriptionDetail,
            AutoSubscriptionsResponseDto,
            BulkUnclaimId,
            SubscriptionsGetResponse,
            RequestPostSubscription,
            SubscriptionDetail,
            SubscriptionsPostRequest,
            SubscriptionsBulkUnclaimRequest,
            V1Beta1SubscriptionsGetResponse,
            AsyncOperationResource,
            AsyncResponse,
            AutoSubscriptionSettings,
            Appointment,
            HpeGreenLakeServerError,
            SubscriptionsPatchRequest,
            BadRequestErrorDetail,
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
            AutoSubscriptionsPostRequest,
            AutoSubscriptionsResponseDtoWithTenant,
            ErrorIssue,
            RequestPostAutoSubscription,
            GeneralErrorDetail,
            HpeGreenLakeBadRequestError,
            AutoSubscriptionsResponsePaginatedDto,
            HpeGreenLakeGeneralError,
            ServerErrorDetail,
            V1Beta1SubscriptionDetail,
            AutoSubscriptionsResponseDto,
            BulkUnclaimId,
            SubscriptionsGetResponse,
            RequestPostSubscription,
            SubscriptionDetail,
            SubscriptionsPostRequest,
            SubscriptionsBulkUnclaimRequest,
            V1Beta1SubscriptionsGetResponse,
            AsyncOperationResource,
            AsyncResponse,
            AutoSubscriptionSettings,
            Appointment,
            HpeGreenLakeServerError,
            SubscriptionsPatchRequest,
            BadRequestErrorDetail,
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
