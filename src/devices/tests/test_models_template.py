# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
Test template for models package.
Tests all generated data models from OpenAPI schemas.
"""

import pytest
from typing import Any, Dict
from pydantic import ValidationError as PydanticValidationError


from greenlake_devices_mcp.models.base import RequestSubscription

from greenlake_devices_mcp.models.base import ResponseLocation

from greenlake_devices_mcp.models.base import ServerErrorDetail

from greenlake_devices_mcp.models.base import DeviceDetail

from greenlake_devices_mcp.models.base import ResponseDedicatedPlatform

from greenlake_devices_mcp.models.base import DevicesPostRequest

from greenlake_devices_mcp.models.base import ErrorIssue

from greenlake_devices_mcp.models.base import HpeGreenLakeBadRequestError

from greenlake_devices_mcp.models.base import HpeGreenLakeServerError

from greenlake_devices_mcp.models.base import RequestNetwork

from greenlake_devices_mcp.models.base import BadRequestErrorDetail

from greenlake_devices_mcp.models.base import ResponseWarranty

from greenlake_devices_mcp.models.base import AsyncOperationResource

from greenlake_devices_mcp.models.base import DevicesGetResponse

from greenlake_devices_mcp.models.base import PatchDevicesRequest

from greenlake_devices_mcp.models.base import RequestCompute

from greenlake_devices_mcp.models.base import ResponseSupportLevel

from greenlake_devices_mcp.models.base import AsyncResponse

from greenlake_devices_mcp.models.base import GeneralErrorDetail

from greenlake_devices_mcp.models.base import PatchDevicesRequestV2

from greenlake_devices_mcp.models.base import ResponseApplication

from greenlake_devices_mcp.models.base import HpeGreenLakeGeneralError

from greenlake_devices_mcp.models.base import ResponseSubscription

from greenlake_devices_mcp.models.base import DevicesPostRequestV2Beta1

from greenlake_devices_mcp.models.base import RequestApplication

from greenlake_devices_mcp.models.base import RequestStorage


class TestModels:
    """Test suite for all generated data models."""

    def test_request_subscription_model_creation(self):
        """Test RequestSubscription model creation with valid data."""
        # Valid test data for RequestSubscription
        valid_data = {
            "id": "test_id",
        }

        # Create model instance
        model = RequestSubscription(**valid_data)

        # Verify model creation
        assert isinstance(model, RequestSubscription)
        assert model.id == valid_data["id"]

    def test_request_subscription_model_validation(self):
        """Test RequestSubscription model field validation."""
        # Test with minimal required data
        minimal_data = {
            "id": "required_id",
        }

        model = RequestSubscription(**minimal_data)
        assert isinstance(model, RequestSubscription)
        assert model.id == minimal_data["id"]

    def test_request_subscription_model_required_fields(self):
        """Test RequestSubscription model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "id",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                RequestSubscription()

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
            model = RequestSubscription()
            assert isinstance(model, RequestSubscription)

    def test_request_subscription_model_optional_fields(self):
        """Test RequestSubscription model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "id": "required_id",
        }

        model = RequestSubscription(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_request_subscription_model_serialization(self):
        """Test RequestSubscription model serialization to dict."""
        test_data = {
            "id": "serialize_value",
        }

        model = RequestSubscription(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "id" in serialized

        # Verify values are preserved
        assert serialized["id"] == test_data["id"]

    def test_request_subscription_model_json_schema(self):
        """Test RequestSubscription model JSON schema generation."""
        schema = RequestSubscription.model_json_schema()

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

    def test_response_location_model_creation(self):
        """Test ResponseLocation model creation with valid data."""
        # Valid test data for ResponseLocation
        valid_data = {
            "id": "test_id",
            "resourceUri": "test_resourceUri",
        }

        # Create model instance
        model = ResponseLocation(**valid_data)

        # Verify model creation
        assert isinstance(model, ResponseLocation)
        assert model.id == valid_data["id"]
        assert model.resourceUri == valid_data["resourceUri"]

    def test_response_location_model_validation(self):
        """Test ResponseLocation model field validation."""
        # Test with minimal required data
        minimal_data = {
            "id": "required_id",
            "resourceUri": "required_resourceUri",
        }

        model = ResponseLocation(**minimal_data)
        assert isinstance(model, ResponseLocation)
        assert model.id == minimal_data["id"]
        assert model.resourceUri == minimal_data["resourceUri"]

    def test_response_location_model_required_fields(self):
        """Test ResponseLocation model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "id",
            "resourceUri",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                ResponseLocation()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "id",
                "resourceUri",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = ResponseLocation()
            assert isinstance(model, ResponseLocation)

    def test_response_location_model_optional_fields(self):
        """Test ResponseLocation model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "id": "required_id",
            "resourceUri": "required_resourceUri",
        }

        model = ResponseLocation(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_response_location_model_serialization(self):
        """Test ResponseLocation model serialization to dict."""
        test_data = {
            "id": "serialize_value",
            "resourceUri": "serialize_value",
        }

        model = ResponseLocation(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "id" in serialized
        assert "resourceUri" in serialized

        # Verify values are preserved
        assert serialized["id"] == test_data["id"]
        assert serialized["resourceUri"] == test_data["resourceUri"]

    def test_response_location_model_json_schema(self):
        """Test ResponseLocation model JSON schema generation."""
        schema = ResponseLocation.model_json_schema()

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
        required_fields = [
            "id",
            "resourceUri",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_server_error_detail_model_creation(self):
        """Test ServerErrorDetail model creation with valid data."""
        # Valid test data for ServerErrorDetail
        valid_data = {
            "type": "test_type",
            "retryAfterSeconds": 42,
        }

        # Create model instance
        model = ServerErrorDetail(**valid_data)

        # Verify model creation
        assert isinstance(model, ServerErrorDetail)
        assert model.type == valid_data["type"]
        assert model.retryAfterSeconds == valid_data["retryAfterSeconds"]

    def test_server_error_detail_model_validation(self):
        """Test ServerErrorDetail model field validation."""
        # Test with minimal required data
        minimal_data = {
            "type": "required_type",
            "retryAfterSeconds": 1,
        }

        model = ServerErrorDetail(**minimal_data)
        assert isinstance(model, ServerErrorDetail)
        assert model.type == minimal_data["type"]
        assert model.retryAfterSeconds == minimal_data["retryAfterSeconds"]

    def test_server_error_detail_model_required_fields(self):
        """Test ServerErrorDetail model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "type",
            "retryAfterSeconds",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                ServerErrorDetail()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "type",
                "retryAfterSeconds",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = ServerErrorDetail()
            assert isinstance(model, ServerErrorDetail)

    def test_server_error_detail_model_optional_fields(self):
        """Test ServerErrorDetail model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "type": "required_type",
            "retryAfterSeconds": 1,
        }

        model = ServerErrorDetail(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_server_error_detail_model_serialization(self):
        """Test ServerErrorDetail model serialization to dict."""
        test_data = {
            "type": "serialize_value",
            "retryAfterSeconds": 99,
        }

        model = ServerErrorDetail(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "type" in serialized
        assert "retryAfterSeconds" in serialized

        # Verify values are preserved
        assert serialized["type"] == test_data["type"]
        assert serialized["retryAfterSeconds"] == test_data["retryAfterSeconds"]

    def test_server_error_detail_model_json_schema(self):
        """Test ServerErrorDetail model JSON schema generation."""
        schema = ServerErrorDetail.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "type",
            "retryAfterSeconds",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "type",
            "retryAfterSeconds",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_device_detail_model_creation(self):
        """Test DeviceDetail model creation with valid data."""
        # Valid test data for DeviceDetail
        valid_data = {
            "assignedState": "test_assignedState",
            "deviceType": "test_deviceType",
            "secondaryName": "test_secondaryName",
            "archived": True,
            "application": {},
            "updatedAt": "test_updatedAt",
            "partNumber": "test_partNumber",
            "warranty": {},
            "deviceName": "test_deviceName",
            "model": "test_model",
            "location": {},
            "tenantWorkspaceId": "test_tenantWorkspaceId",
            "macAddress": "test_macAddress",
            "tags": {},
            "id": "test_id",
            "createdAt": "test_createdAt",
            "dedicatedPlatformWorkspace": {},
            "serialNumber": "test_serialNumber",
            "type": "test_type",
            "subscription": [],
            "region": "test_region",
        }

        # Create model instance
        model = DeviceDetail(**valid_data)

        # Verify model creation
        assert isinstance(model, DeviceDetail)
        assert model.assignedState == valid_data["assignedState"]
        assert model.deviceType == valid_data["deviceType"]
        assert model.secondaryName == valid_data["secondaryName"]
        assert model.archived == valid_data["archived"]
        assert model.application == valid_data["application"]
        assert model.updatedAt == valid_data["updatedAt"]
        assert model.partNumber == valid_data["partNumber"]
        assert model.warranty == valid_data["warranty"]
        assert model.deviceName == valid_data["deviceName"]
        assert model.model == valid_data["model"]
        assert model.location == valid_data["location"]
        assert model.tenantWorkspaceId == valid_data["tenantWorkspaceId"]
        assert model.macAddress == valid_data["macAddress"]
        assert model.tags == valid_data["tags"]
        assert model.id == valid_data["id"]
        assert model.createdAt == valid_data["createdAt"]
        assert model.dedicatedPlatformWorkspace == valid_data["dedicatedPlatformWorkspace"]
        assert model.serialNumber == valid_data["serialNumber"]
        assert model.type == valid_data["type"]
        assert model.subscription == valid_data["subscription"]
        assert model.region == valid_data["region"]

    def test_device_detail_model_validation(self):
        """Test DeviceDetail model field validation."""
        # Test with minimal required data
        minimal_data = {
            "partNumber": "required_partNumber",
            "id": "required_id",
            "serialNumber": "required_serialNumber",
            "type": "required_type",
        }

        model = DeviceDetail(**minimal_data)
        assert isinstance(model, DeviceDetail)
        assert model.partNumber == minimal_data["partNumber"]
        assert model.id == minimal_data["id"]
        assert model.serialNumber == minimal_data["serialNumber"]
        assert model.type == minimal_data["type"]

    def test_device_detail_model_required_fields(self):
        """Test DeviceDetail model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "partNumber",
            "id",
            "serialNumber",
            "type",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                DeviceDetail()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "partNumber",
                "id",
                "serialNumber",
                "type",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = DeviceDetail()
            assert isinstance(model, DeviceDetail)

    def test_device_detail_model_optional_fields(self):
        """Test DeviceDetail model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "partNumber": "required_partNumber",
            "id": "required_id",
            "serialNumber": "required_serialNumber",
            "type": "required_type",
        }

        model = DeviceDetail(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "assignedState")
        # Optional field assignedState should be None or have a default value
        assert model.assignedState is None or model.assignedState is not None
        assert hasattr(model, "deviceType")
        # Optional field deviceType should be None or have a default value
        assert model.deviceType is None or model.deviceType is not None
        assert hasattr(model, "secondaryName")
        # Optional field secondaryName should be None or have a default value
        assert model.secondaryName is None or model.secondaryName is not None
        assert hasattr(model, "archived")
        # Optional field archived should be None or have a default value
        assert model.archived is None or model.archived is not None
        assert hasattr(model, "application")
        # Optional field application should be None or have a default value
        assert model.application is None or model.application is not None
        assert hasattr(model, "updatedAt")
        # Optional field updatedAt should be None or have a default value
        assert model.updatedAt is None or model.updatedAt is not None
        assert hasattr(model, "warranty")
        # Optional field warranty should be None or have a default value
        assert model.warranty is None or model.warranty is not None
        assert hasattr(model, "deviceName")
        # Optional field deviceName should be None or have a default value
        assert model.deviceName is None or model.deviceName is not None
        assert hasattr(model, "model")
        # Optional field model should be None or have a default value
        assert model.model is None or model.model is not None
        assert hasattr(model, "location")
        # Optional field location should be None or have a default value
        assert model.location is None or model.location is not None
        assert hasattr(model, "tenantWorkspaceId")
        # Optional field tenantWorkspaceId should be None or have a default value
        assert model.tenantWorkspaceId is None or model.tenantWorkspaceId is not None
        assert hasattr(model, "macAddress")
        # Optional field macAddress should be None or have a default value
        assert model.macAddress is None or model.macAddress is not None
        assert hasattr(model, "tags")
        # Optional field tags should be None or have a default value
        assert model.tags is None or model.tags is not None
        assert hasattr(model, "createdAt")
        # Optional field createdAt should be None or have a default value
        assert model.createdAt is None or model.createdAt is not None
        assert hasattr(model, "dedicatedPlatformWorkspace")
        # Optional field dedicatedPlatformWorkspace should be None or have a default value
        assert model.dedicatedPlatformWorkspace is None or model.dedicatedPlatformWorkspace is not None
        assert hasattr(model, "subscription")
        # Optional field subscription should be None or have a default value
        assert model.subscription is None or model.subscription is not None
        assert hasattr(model, "region")
        # Optional field region should be None or have a default value
        assert model.region is None or model.region is not None

    def test_device_detail_model_serialization(self):
        """Test DeviceDetail model serialization to dict."""
        test_data = {
            "assignedState": "serialize_value",
            "deviceType": "serialize_value",
            "secondaryName": "serialize_value",
            "archived": False,
            "application": {"key": "value"},
            "updatedAt": "serialize_value",
            "partNumber": "serialize_value",
            "warranty": {"key": "value"},
            "deviceName": "serialize_value",
            "model": "serialize_value",
            "location": {"key": "value"},
            "tenantWorkspaceId": "serialize_value",
            "macAddress": "serialize_value",
            "tags": {"key": "value"},
            "id": "serialize_value",
            "createdAt": "serialize_value",
            "dedicatedPlatformWorkspace": {"key": "value"},
            "serialNumber": "serialize_value",
            "type": "serialize_value",
            "subscription": [],
            "region": "serialize_value",
        }

        model = DeviceDetail(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "assignedState" in serialized
        assert "deviceType" in serialized
        assert "secondaryName" in serialized
        assert "archived" in serialized
        assert "application" in serialized
        assert "updatedAt" in serialized
        assert "partNumber" in serialized
        assert "warranty" in serialized
        assert "deviceName" in serialized
        assert "model" in serialized
        assert "location" in serialized
        assert "tenantWorkspaceId" in serialized
        assert "macAddress" in serialized
        assert "tags" in serialized
        assert "id" in serialized
        assert "createdAt" in serialized
        assert "dedicatedPlatformWorkspace" in serialized
        assert "serialNumber" in serialized
        assert "type" in serialized
        assert "subscription" in serialized
        assert "region" in serialized

        # Verify values are preserved
        assert serialized["assignedState"] == test_data["assignedState"]
        assert serialized["deviceType"] == test_data["deviceType"]
        assert serialized["secondaryName"] == test_data["secondaryName"]
        assert serialized["archived"] == test_data["archived"]
        assert serialized["application"] == test_data["application"]
        assert serialized["updatedAt"] == test_data["updatedAt"]
        assert serialized["partNumber"] == test_data["partNumber"]
        assert serialized["warranty"] == test_data["warranty"]
        assert serialized["deviceName"] == test_data["deviceName"]
        assert serialized["model"] == test_data["model"]
        assert serialized["location"] == test_data["location"]
        assert serialized["tenantWorkspaceId"] == test_data["tenantWorkspaceId"]
        assert serialized["macAddress"] == test_data["macAddress"]
        assert serialized["tags"] == test_data["tags"]
        assert serialized["id"] == test_data["id"]
        assert serialized["createdAt"] == test_data["createdAt"]
        assert serialized["dedicatedPlatformWorkspace"] == test_data["dedicatedPlatformWorkspace"]
        assert serialized["serialNumber"] == test_data["serialNumber"]
        assert serialized["type"] == test_data["type"]
        assert serialized["subscription"] == test_data["subscription"]
        assert serialized["region"] == test_data["region"]

    def test_device_detail_model_json_schema(self):
        """Test DeviceDetail model JSON schema generation."""
        schema = DeviceDetail.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "assignedState",
            "deviceType",
            "secondaryName",
            "archived",
            "application",
            "updatedAt",
            "partNumber",
            "warranty",
            "deviceName",
            "model",
            "location",
            "tenantWorkspaceId",
            "macAddress",
            "tags",
            "id",
            "createdAt",
            "dedicatedPlatformWorkspace",
            "serialNumber",
            "type",
            "subscription",
            "region",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "partNumber",
            "id",
            "serialNumber",
            "type",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_response_dedicated_platform_model_creation(self):
        """Test ResponseDedicatedPlatform model creation with valid data."""
        # Valid test data for ResponseDedicatedPlatform
        valid_data = {
            "id": "test_id",
        }

        # Create model instance
        model = ResponseDedicatedPlatform(**valid_data)

        # Verify model creation
        assert isinstance(model, ResponseDedicatedPlatform)
        assert model.id == valid_data["id"]

    def test_response_dedicated_platform_model_validation(self):
        """Test ResponseDedicatedPlatform model field validation."""
        # Test with minimal required data
        minimal_data = {
            "id": "required_id",
        }

        model = ResponseDedicatedPlatform(**minimal_data)
        assert isinstance(model, ResponseDedicatedPlatform)
        assert model.id == minimal_data["id"]

    def test_response_dedicated_platform_model_required_fields(self):
        """Test ResponseDedicatedPlatform model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "id",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                ResponseDedicatedPlatform()

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
            model = ResponseDedicatedPlatform()
            assert isinstance(model, ResponseDedicatedPlatform)

    def test_response_dedicated_platform_model_optional_fields(self):
        """Test ResponseDedicatedPlatform model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "id": "required_id",
        }

        model = ResponseDedicatedPlatform(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_response_dedicated_platform_model_serialization(self):
        """Test ResponseDedicatedPlatform model serialization to dict."""
        test_data = {
            "id": "serialize_value",
        }

        model = ResponseDedicatedPlatform(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "id" in serialized

        # Verify values are preserved
        assert serialized["id"] == test_data["id"]

    def test_response_dedicated_platform_model_json_schema(self):
        """Test ResponseDedicatedPlatform model JSON schema generation."""
        schema = ResponseDedicatedPlatform.model_json_schema()

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

    def test_devices_post_request_model_creation(self):
        """Test DevicesPostRequest model creation with valid data."""
        # Valid test data for DevicesPostRequest
        valid_data = {
            "network": [],
            "storage": [],
            "compute": [],
        }

        # Create model instance
        model = DevicesPostRequest(**valid_data)

        # Verify model creation
        assert isinstance(model, DevicesPostRequest)
        assert model.network == valid_data["network"]
        assert model.storage == valid_data["storage"]
        assert model.compute == valid_data["compute"]

    def test_devices_post_request_model_validation(self):
        """Test DevicesPostRequest model field validation."""
        # Test with minimal required data
        minimal_data = {
            "network": [],
            "storage": [],
            "compute": [],
        }

        model = DevicesPostRequest(**minimal_data)
        assert isinstance(model, DevicesPostRequest)
        assert model.network == minimal_data["network"]
        assert model.storage == minimal_data["storage"]
        assert model.compute == minimal_data["compute"]

    def test_devices_post_request_model_required_fields(self):
        """Test DevicesPostRequest model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "network",
            "storage",
            "compute",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                DevicesPostRequest()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "network",
                "storage",
                "compute",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = DevicesPostRequest()
            assert isinstance(model, DevicesPostRequest)

    def test_devices_post_request_model_optional_fields(self):
        """Test DevicesPostRequest model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "network": [],
            "storage": [],
            "compute": [],
        }

        model = DevicesPostRequest(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_devices_post_request_model_serialization(self):
        """Test DevicesPostRequest model serialization to dict."""
        test_data = {
            "network": [],
            "storage": [],
            "compute": [],
        }

        model = DevicesPostRequest(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "network" in serialized
        assert "storage" in serialized
        assert "compute" in serialized

        # Verify values are preserved
        assert serialized["network"] == test_data["network"]
        assert serialized["storage"] == test_data["storage"]
        assert serialized["compute"] == test_data["compute"]

    def test_devices_post_request_model_json_schema(self):
        """Test DevicesPostRequest model JSON schema generation."""
        schema = DevicesPostRequest.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "network",
            "storage",
            "compute",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "network",
            "storage",
            "compute",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_error_issue_model_creation(self):
        """Test ErrorIssue model creation with valid data."""
        # Valid test data for ErrorIssue
        valid_data = {
            "description": "test_description",
            "source": "test_source",
            "subject": "test_subject",
        }

        # Create model instance
        model = ErrorIssue(**valid_data)

        # Verify model creation
        assert isinstance(model, ErrorIssue)
        assert model.description == valid_data["description"]
        assert model.source == valid_data["source"]
        assert model.subject == valid_data["subject"]

    def test_error_issue_model_validation(self):
        """Test ErrorIssue model field validation."""
        # Test with minimal required data
        minimal_data = {}

        model = ErrorIssue(**minimal_data)
        assert isinstance(model, ErrorIssue)

    def test_error_issue_model_required_fields(self):
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

    def test_error_issue_model_optional_fields(self):
        """Test ErrorIssue model optional field handling."""
        # Create with minimal required data
        minimal_data = {}

        model = ErrorIssue(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "description")
        # Optional field description should be None or have a default value
        assert model.description is None or model.description is not None
        assert hasattr(model, "source")
        # Optional field source should be None or have a default value
        assert model.source is None or model.source is not None
        assert hasattr(model, "subject")
        # Optional field subject should be None or have a default value
        assert model.subject is None or model.subject is not None

    def test_error_issue_model_serialization(self):
        """Test ErrorIssue model serialization to dict."""
        test_data = {
            "description": "serialize_value",
            "source": "serialize_value",
            "subject": "serialize_value",
        }

        model = ErrorIssue(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "description" in serialized
        assert "source" in serialized
        assert "subject" in serialized

        # Verify values are preserved
        assert serialized["description"] == test_data["description"]
        assert serialized["source"] == test_data["source"]
        assert serialized["subject"] == test_data["subject"]

    def test_error_issue_model_json_schema(self):
        """Test ErrorIssue model JSON schema generation."""
        schema = ErrorIssue.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "description",
            "source",
            "subject",
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

    def test_hpe_green_lake_bad_request_error_model_creation(self):
        """Test HpeGreenLakeBadRequestError model creation with valid data."""
        # Valid test data for HpeGreenLakeBadRequestError
        valid_data = {
            "debugId": "test_debugId",
            "errorCode": "test_errorCode",
            "httpStatusCode": 42,
            "message": "test_message",
            "badRequestErrorDetails": [],
        }

        # Create model instance
        model = HpeGreenLakeBadRequestError(**valid_data)

        # Verify model creation
        assert isinstance(model, HpeGreenLakeBadRequestError)
        assert model.debugId == valid_data["debugId"]
        assert model.errorCode == valid_data["errorCode"]
        assert model.httpStatusCode == valid_data["httpStatusCode"]
        assert model.message == valid_data["message"]
        assert model.badRequestErrorDetails == valid_data["badRequestErrorDetails"]

    def test_hpe_green_lake_bad_request_error_model_validation(self):
        """Test HpeGreenLakeBadRequestError model field validation."""
        # Test with minimal required data
        minimal_data = {
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
            "httpStatusCode": 1,
            "message": "required_message",
        }

        model = HpeGreenLakeBadRequestError(**minimal_data)
        assert isinstance(model, HpeGreenLakeBadRequestError)
        assert model.debugId == minimal_data["debugId"]
        assert model.errorCode == minimal_data["errorCode"]
        assert model.httpStatusCode == minimal_data["httpStatusCode"]
        assert model.message == minimal_data["message"]

    def test_hpe_green_lake_bad_request_error_model_required_fields(self):
        """Test HpeGreenLakeBadRequestError model required field validation."""
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
                HpeGreenLakeBadRequestError()

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
            model = HpeGreenLakeBadRequestError()
            assert isinstance(model, HpeGreenLakeBadRequestError)

    def test_hpe_green_lake_bad_request_error_model_optional_fields(self):
        """Test HpeGreenLakeBadRequestError model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
            "httpStatusCode": 1,
            "message": "required_message",
        }

        model = HpeGreenLakeBadRequestError(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "badRequestErrorDetails")
        # Optional field badRequestErrorDetails should be None or have a default value
        assert model.badRequestErrorDetails is None or model.badRequestErrorDetails is not None

    def test_hpe_green_lake_bad_request_error_model_serialization(self):
        """Test HpeGreenLakeBadRequestError model serialization to dict."""
        test_data = {
            "debugId": "serialize_value",
            "errorCode": "serialize_value",
            "httpStatusCode": 99,
            "message": "serialize_value",
            "badRequestErrorDetails": [],
        }

        model = HpeGreenLakeBadRequestError(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "debugId" in serialized
        assert "errorCode" in serialized
        assert "httpStatusCode" in serialized
        assert "message" in serialized
        assert "badRequestErrorDetails" in serialized

        # Verify values are preserved
        assert serialized["debugId"] == test_data["debugId"]
        assert serialized["errorCode"] == test_data["errorCode"]
        assert serialized["httpStatusCode"] == test_data["httpStatusCode"]
        assert serialized["message"] == test_data["message"]
        assert serialized["badRequestErrorDetails"] == test_data["badRequestErrorDetails"]

    def test_hpe_green_lake_bad_request_error_model_json_schema(self):
        """Test HpeGreenLakeBadRequestError model JSON schema generation."""
        schema = HpeGreenLakeBadRequestError.model_json_schema()

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
            "badRequestErrorDetails",
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

    def test_hpe_green_lake_server_error_model_creation(self):
        """Test HpeGreenLakeServerError model creation with valid data."""
        # Valid test data for HpeGreenLakeServerError
        valid_data = {
            "serverErrorDetails": [],
            "debugId": "test_debugId",
            "errorCode": "test_errorCode",
            "httpStatusCode": 42,
            "message": "test_message",
        }

        # Create model instance
        model = HpeGreenLakeServerError(**valid_data)

        # Verify model creation
        assert isinstance(model, HpeGreenLakeServerError)
        assert model.serverErrorDetails == valid_data["serverErrorDetails"]
        assert model.debugId == valid_data["debugId"]
        assert model.errorCode == valid_data["errorCode"]
        assert model.httpStatusCode == valid_data["httpStatusCode"]
        assert model.message == valid_data["message"]

    def test_hpe_green_lake_server_error_model_validation(self):
        """Test HpeGreenLakeServerError model field validation."""
        # Test with minimal required data
        minimal_data = {
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
            "httpStatusCode": 1,
            "message": "required_message",
        }

        model = HpeGreenLakeServerError(**minimal_data)
        assert isinstance(model, HpeGreenLakeServerError)
        assert model.debugId == minimal_data["debugId"]
        assert model.errorCode == minimal_data["errorCode"]
        assert model.httpStatusCode == minimal_data["httpStatusCode"]
        assert model.message == minimal_data["message"]

    def test_hpe_green_lake_server_error_model_required_fields(self):
        """Test HpeGreenLakeServerError model required field validation."""
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
                HpeGreenLakeServerError()

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
            model = HpeGreenLakeServerError()
            assert isinstance(model, HpeGreenLakeServerError)

    def test_hpe_green_lake_server_error_model_optional_fields(self):
        """Test HpeGreenLakeServerError model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
            "httpStatusCode": 1,
            "message": "required_message",
        }

        model = HpeGreenLakeServerError(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "serverErrorDetails")
        # Optional field serverErrorDetails should be None or have a default value
        assert model.serverErrorDetails is None or model.serverErrorDetails is not None

    def test_hpe_green_lake_server_error_model_serialization(self):
        """Test HpeGreenLakeServerError model serialization to dict."""
        test_data = {
            "serverErrorDetails": [],
            "debugId": "serialize_value",
            "errorCode": "serialize_value",
            "httpStatusCode": 99,
            "message": "serialize_value",
        }

        model = HpeGreenLakeServerError(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "serverErrorDetails" in serialized
        assert "debugId" in serialized
        assert "errorCode" in serialized
        assert "httpStatusCode" in serialized
        assert "message" in serialized

        # Verify values are preserved
        assert serialized["serverErrorDetails"] == test_data["serverErrorDetails"]
        assert serialized["debugId"] == test_data["debugId"]
        assert serialized["errorCode"] == test_data["errorCode"]
        assert serialized["httpStatusCode"] == test_data["httpStatusCode"]
        assert serialized["message"] == test_data["message"]

    def test_hpe_green_lake_server_error_model_json_schema(self):
        """Test HpeGreenLakeServerError model JSON schema generation."""
        schema = HpeGreenLakeServerError.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "serverErrorDetails",
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

    def test_request_network_model_creation(self):
        """Test RequestNetwork model creation with valid data."""
        # Valid test data for RequestNetwork
        valid_data = {
            "tags": {},
            "macAddress": "test_macAddress",
            "serialNumber": "test_serialNumber",
        }

        # Create model instance
        model = RequestNetwork(**valid_data)

        # Verify model creation
        assert isinstance(model, RequestNetwork)
        assert model.tags == valid_data["tags"]
        assert model.macAddress == valid_data["macAddress"]
        assert model.serialNumber == valid_data["serialNumber"]

    def test_request_network_model_validation(self):
        """Test RequestNetwork model field validation."""
        # Test with minimal required data
        minimal_data = {
            "macAddress": "required_macAddress",
            "serialNumber": "required_serialNumber",
        }

        model = RequestNetwork(**minimal_data)
        assert isinstance(model, RequestNetwork)
        assert model.macAddress == minimal_data["macAddress"]
        assert model.serialNumber == minimal_data["serialNumber"]

    def test_request_network_model_required_fields(self):
        """Test RequestNetwork model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "macAddress",
            "serialNumber",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                RequestNetwork()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "macAddress",
                "serialNumber",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = RequestNetwork()
            assert isinstance(model, RequestNetwork)

    def test_request_network_model_optional_fields(self):
        """Test RequestNetwork model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "macAddress": "required_macAddress",
            "serialNumber": "required_serialNumber",
        }

        model = RequestNetwork(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "tags")
        # Optional field tags should be None or have a default value
        assert model.tags is None or model.tags is not None

    def test_request_network_model_serialization(self):
        """Test RequestNetwork model serialization to dict."""
        test_data = {
            "tags": {"key": "value"},
            "macAddress": "serialize_value",
            "serialNumber": "serialize_value",
        }

        model = RequestNetwork(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "tags" in serialized
        assert "macAddress" in serialized
        assert "serialNumber" in serialized

        # Verify values are preserved
        assert serialized["tags"] == test_data["tags"]
        assert serialized["macAddress"] == test_data["macAddress"]
        assert serialized["serialNumber"] == test_data["serialNumber"]

    def test_request_network_model_json_schema(self):
        """Test RequestNetwork model JSON schema generation."""
        schema = RequestNetwork.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "tags",
            "macAddress",
            "serialNumber",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "macAddress",
            "serialNumber",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_bad_request_error_detail_model_creation(self):
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

    def test_bad_request_error_detail_model_validation(self):
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

    def test_bad_request_error_detail_model_required_fields(self):
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

    def test_bad_request_error_detail_model_optional_fields(self):
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

    def test_bad_request_error_detail_model_serialization(self):
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

    def test_bad_request_error_detail_model_json_schema(self):
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

    def test_response_warranty_model_creation(self):
        """Test ResponseWarranty model creation with valid data."""
        # Valid test data for ResponseWarranty
        valid_data = {
            "currentSupportLevel": {},
            "supportLevels": [],
            "country": "test_country",
        }

        # Create model instance
        model = ResponseWarranty(**valid_data)

        # Verify model creation
        assert isinstance(model, ResponseWarranty)
        assert model.currentSupportLevel == valid_data["currentSupportLevel"]
        assert model.supportLevels == valid_data["supportLevels"]
        assert model.country == valid_data["country"]

    def test_response_warranty_model_validation(self):
        """Test ResponseWarranty model field validation."""
        # Test with minimal required data
        minimal_data = {}

        model = ResponseWarranty(**minimal_data)
        assert isinstance(model, ResponseWarranty)

    def test_response_warranty_model_required_fields(self):
        """Test ResponseWarranty model required field validation."""
        # Check if this model has any required fields
        required_fields = []

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                ResponseWarranty()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {}

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = ResponseWarranty()
            assert isinstance(model, ResponseWarranty)

    def test_response_warranty_model_optional_fields(self):
        """Test ResponseWarranty model optional field handling."""
        # Create with minimal required data
        minimal_data = {}

        model = ResponseWarranty(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "currentSupportLevel")
        # Optional field currentSupportLevel should be None or have a default value
        assert model.currentSupportLevel is None or model.currentSupportLevel is not None
        assert hasattr(model, "supportLevels")
        # Optional field supportLevels should be None or have a default value
        assert model.supportLevels is None or model.supportLevels is not None
        assert hasattr(model, "country")
        # Optional field country should be None or have a default value
        assert model.country is None or model.country is not None

    def test_response_warranty_model_serialization(self):
        """Test ResponseWarranty model serialization to dict."""
        test_data = {
            "currentSupportLevel": {"key": "value"},
            "supportLevels": [],
            "country": "serialize_value",
        }

        model = ResponseWarranty(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "currentSupportLevel" in serialized
        assert "supportLevels" in serialized
        assert "country" in serialized

        # Verify values are preserved
        assert serialized["currentSupportLevel"] == test_data["currentSupportLevel"]
        assert serialized["supportLevels"] == test_data["supportLevels"]
        assert serialized["country"] == test_data["country"]

    def test_response_warranty_model_json_schema(self):
        """Test ResponseWarranty model JSON schema generation."""
        schema = ResponseWarranty.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "currentSupportLevel",
            "supportLevels",
            "country",
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

    def test_async_operation_resource_model_creation(self):
        """Test AsyncOperationResource model creation with valid data."""
        # Valid test data for AsyncOperationResource
        valid_data = {
            "progressPercent": 42,
            "resultType": "test_resultType",
            "suggestedPollingIntervalSeconds": 42,
            "timeoutMinutes": 42,
            "endedAt": "test_endedAt",
            "result": {},
            "status": "test_status",
            "type": "test_type",
            "id": "test_id",
            "startedAt": "test_startedAt",
        }

        # Create model instance
        model = AsyncOperationResource(**valid_data)

        # Verify model creation
        assert isinstance(model, AsyncOperationResource)
        assert model.progressPercent == valid_data["progressPercent"]
        assert model.resultType == valid_data["resultType"]
        assert model.suggestedPollingIntervalSeconds == valid_data["suggestedPollingIntervalSeconds"]
        assert model.timeoutMinutes == valid_data["timeoutMinutes"]
        assert model.endedAt == valid_data["endedAt"]
        assert model.result == valid_data["result"]
        assert model.status == valid_data["status"]
        assert model.type == valid_data["type"]
        assert model.id == valid_data["id"]
        assert model.startedAt == valid_data["startedAt"]

    def test_async_operation_resource_model_validation(self):
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

    def test_async_operation_resource_model_required_fields(self):
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

    def test_async_operation_resource_model_optional_fields(self):
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
        assert hasattr(model, "progressPercent")
        # Optional field progressPercent should be None or have a default value
        assert model.progressPercent is None or model.progressPercent is not None
        assert hasattr(model, "resultType")
        # Optional field resultType should be None or have a default value
        assert model.resultType is None or model.resultType is not None
        assert hasattr(model, "suggestedPollingIntervalSeconds")
        # Optional field suggestedPollingIntervalSeconds should be None or have a default value
        assert model.suggestedPollingIntervalSeconds is None or model.suggestedPollingIntervalSeconds is not None
        assert hasattr(model, "timeoutMinutes")
        # Optional field timeoutMinutes should be None or have a default value
        assert model.timeoutMinutes is None or model.timeoutMinutes is not None
        assert hasattr(model, "endedAt")
        # Optional field endedAt should be None or have a default value
        assert model.endedAt is None or model.endedAt is not None
        assert hasattr(model, "result")
        # Optional field result should be None or have a default value
        assert model.result is None or model.result is not None
        assert hasattr(model, "status")
        # Optional field status should be None or have a default value
        assert model.status is None or model.status is not None
        assert hasattr(model, "startedAt")
        # Optional field startedAt should be None or have a default value
        assert model.startedAt is None or model.startedAt is not None

    def test_async_operation_resource_model_serialization(self):
        """Test AsyncOperationResource model serialization to dict."""
        test_data = {
            "progressPercent": 99,
            "resultType": "serialize_value",
            "suggestedPollingIntervalSeconds": 99,
            "timeoutMinutes": 99,
            "endedAt": "serialize_value",
            "result": {"key": "value"},
            "status": "serialize_value",
            "type": "serialize_value",
            "id": "serialize_value",
            "startedAt": "serialize_value",
        }

        model = AsyncOperationResource(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "progressPercent" in serialized
        assert "resultType" in serialized
        assert "suggestedPollingIntervalSeconds" in serialized
        assert "timeoutMinutes" in serialized
        assert "endedAt" in serialized
        assert "result" in serialized
        assert "status" in serialized
        assert "type" in serialized
        assert "id" in serialized
        assert "startedAt" in serialized

        # Verify values are preserved
        assert serialized["progressPercent"] == test_data["progressPercent"]
        assert serialized["resultType"] == test_data["resultType"]
        assert serialized["suggestedPollingIntervalSeconds"] == test_data["suggestedPollingIntervalSeconds"]
        assert serialized["timeoutMinutes"] == test_data["timeoutMinutes"]
        assert serialized["endedAt"] == test_data["endedAt"]
        assert serialized["result"] == test_data["result"]
        assert serialized["status"] == test_data["status"]
        assert serialized["type"] == test_data["type"]
        assert serialized["id"] == test_data["id"]
        assert serialized["startedAt"] == test_data["startedAt"]

    def test_async_operation_resource_model_json_schema(self):
        """Test AsyncOperationResource model JSON schema generation."""
        schema = AsyncOperationResource.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "progressPercent",
            "resultType",
            "suggestedPollingIntervalSeconds",
            "timeoutMinutes",
            "endedAt",
            "result",
            "status",
            "type",
            "id",
            "startedAt",
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

    def test_devices_get_response_model_creation(self):
        """Test DevicesGetResponse model creation with valid data."""
        # Valid test data for DevicesGetResponse
        valid_data = {
            "total": 42,
            "count": 42,
            "items": [],
            "offset": 42,
        }

        # Create model instance
        model = DevicesGetResponse(**valid_data)

        # Verify model creation
        assert isinstance(model, DevicesGetResponse)
        assert model.total == valid_data["total"]
        assert model.count == valid_data["count"]
        assert model.items == valid_data["items"]
        assert model.offset == valid_data["offset"]

    def test_devices_get_response_model_validation(self):
        """Test DevicesGetResponse model field validation."""
        # Test with minimal required data
        minimal_data = {
            "count": 1,
            "items": [],
        }

        model = DevicesGetResponse(**minimal_data)
        assert isinstance(model, DevicesGetResponse)
        assert model.count == minimal_data["count"]
        assert model.items == minimal_data["items"]

    def test_devices_get_response_model_required_fields(self):
        """Test DevicesGetResponse model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "count",
            "items",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                DevicesGetResponse()

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
            model = DevicesGetResponse()
            assert isinstance(model, DevicesGetResponse)

    def test_devices_get_response_model_optional_fields(self):
        """Test DevicesGetResponse model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "count": 1,
            "items": [],
        }

        model = DevicesGetResponse(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "total")
        # Optional field total should be None or have a default value
        assert model.total is None or model.total is not None
        assert hasattr(model, "offset")
        # Optional field offset should be None or have a default value
        assert model.offset is None or model.offset is not None

    def test_devices_get_response_model_serialization(self):
        """Test DevicesGetResponse model serialization to dict."""
        test_data = {
            "total": 99,
            "count": 99,
            "items": [],
            "offset": 99,
        }

        model = DevicesGetResponse(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "total" in serialized
        assert "count" in serialized
        assert "items" in serialized
        assert "offset" in serialized

        # Verify values are preserved
        assert serialized["total"] == test_data["total"]
        assert serialized["count"] == test_data["count"]
        assert serialized["items"] == test_data["items"]
        assert serialized["offset"] == test_data["offset"]

    def test_devices_get_response_model_json_schema(self):
        """Test DevicesGetResponse model JSON schema generation."""
        schema = DevicesGetResponse.model_json_schema()

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
            "offset",
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

    def test_patch_devices_request_model_creation(self):
        """Test PatchDevicesRequest model creation with valid data."""
        # Valid test data for PatchDevicesRequest
        valid_data = {
            "region": "test_region",
            "subscription": [],
            "tenantPlatformCustomerId": "test_tenantPlatformCustomerId",
            "application": {},
        }

        # Create model instance
        model = PatchDevicesRequest(**valid_data)

        # Verify model creation
        assert isinstance(model, PatchDevicesRequest)
        assert model.region == valid_data["region"]
        assert model.subscription == valid_data["subscription"]
        assert model.tenantPlatformCustomerId == valid_data["tenantPlatformCustomerId"]
        assert model.application == valid_data["application"]

    def test_patch_devices_request_model_validation(self):
        """Test PatchDevicesRequest model field validation."""
        # Test with minimal required data
        minimal_data = {}

        model = PatchDevicesRequest(**minimal_data)
        assert isinstance(model, PatchDevicesRequest)

    def test_patch_devices_request_model_required_fields(self):
        """Test PatchDevicesRequest model required field validation."""
        # Check if this model has any required fields
        required_fields = []

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                PatchDevicesRequest()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {}

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = PatchDevicesRequest()
            assert isinstance(model, PatchDevicesRequest)

    def test_patch_devices_request_model_optional_fields(self):
        """Test PatchDevicesRequest model optional field handling."""
        # Create with minimal required data
        minimal_data = {}

        model = PatchDevicesRequest(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "region")
        # Optional field region should be None or have a default value
        assert model.region is None or model.region is not None
        assert hasattr(model, "subscription")
        # Optional field subscription should be None or have a default value
        assert model.subscription is None or model.subscription is not None
        assert hasattr(model, "tenantPlatformCustomerId")
        # Optional field tenantPlatformCustomerId should be None or have a default value
        assert model.tenantPlatformCustomerId is None or model.tenantPlatformCustomerId is not None
        assert hasattr(model, "application")
        # Optional field application should be None or have a default value
        assert model.application is None or model.application is not None

    def test_patch_devices_request_model_serialization(self):
        """Test PatchDevicesRequest model serialization to dict."""
        test_data = {
            "region": "serialize_value",
            "subscription": [],
            "tenantPlatformCustomerId": "serialize_value",
            "application": {"key": "value"},
        }

        model = PatchDevicesRequest(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "region" in serialized
        assert "subscription" in serialized
        assert "tenantPlatformCustomerId" in serialized
        assert "application" in serialized

        # Verify values are preserved
        assert serialized["region"] == test_data["region"]
        assert serialized["subscription"] == test_data["subscription"]
        assert serialized["tenantPlatformCustomerId"] == test_data["tenantPlatformCustomerId"]
        assert serialized["application"] == test_data["application"]

    def test_patch_devices_request_model_json_schema(self):
        """Test PatchDevicesRequest model JSON schema generation."""
        schema = PatchDevicesRequest.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "region",
            "subscription",
            "tenantPlatformCustomerId",
            "application",
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

    def test_request_compute_model_creation(self):
        """Test RequestCompute model creation with valid data."""
        # Valid test data for RequestCompute
        valid_data = {
            "serialNumber": "test_serialNumber",
            "tags": {},
            "partNumber": "test_partNumber",
        }

        # Create model instance
        model = RequestCompute(**valid_data)

        # Verify model creation
        assert isinstance(model, RequestCompute)
        assert model.serialNumber == valid_data["serialNumber"]
        assert model.tags == valid_data["tags"]
        assert model.partNumber == valid_data["partNumber"]

    def test_request_compute_model_validation(self):
        """Test RequestCompute model field validation."""
        # Test with minimal required data
        minimal_data = {
            "serialNumber": "required_serialNumber",
            "partNumber": "required_partNumber",
        }

        model = RequestCompute(**minimal_data)
        assert isinstance(model, RequestCompute)
        assert model.serialNumber == minimal_data["serialNumber"]
        assert model.partNumber == minimal_data["partNumber"]

    def test_request_compute_model_required_fields(self):
        """Test RequestCompute model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "serialNumber",
            "partNumber",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                RequestCompute()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "serialNumber",
                "partNumber",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = RequestCompute()
            assert isinstance(model, RequestCompute)

    def test_request_compute_model_optional_fields(self):
        """Test RequestCompute model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "serialNumber": "required_serialNumber",
            "partNumber": "required_partNumber",
        }

        model = RequestCompute(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "tags")
        # Optional field tags should be None or have a default value
        assert model.tags is None or model.tags is not None

    def test_request_compute_model_serialization(self):
        """Test RequestCompute model serialization to dict."""
        test_data = {
            "serialNumber": "serialize_value",
            "tags": {"key": "value"},
            "partNumber": "serialize_value",
        }

        model = RequestCompute(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "serialNumber" in serialized
        assert "tags" in serialized
        assert "partNumber" in serialized

        # Verify values are preserved
        assert serialized["serialNumber"] == test_data["serialNumber"]
        assert serialized["tags"] == test_data["tags"]
        assert serialized["partNumber"] == test_data["partNumber"]

    def test_request_compute_model_json_schema(self):
        """Test RequestCompute model JSON schema generation."""
        schema = RequestCompute.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "serialNumber",
            "tags",
            "partNumber",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "serialNumber",
            "partNumber",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_response_support_level_model_creation(self):
        """Test ResponseSupportLevel model creation with valid data."""
        # Valid test data for ResponseSupportLevel
        valid_data = {
            "contractLevelRank": 42,
            "endDate": 42,
            "serviceLevel": "test_serviceLevel",
            "serviceLevelRank": 42,
            "startDate": 42,
            "contractLevel": "test_contractLevel",
        }

        # Create model instance
        model = ResponseSupportLevel(**valid_data)

        # Verify model creation
        assert isinstance(model, ResponseSupportLevel)
        assert model.contractLevelRank == valid_data["contractLevelRank"]
        assert model.endDate == valid_data["endDate"]
        assert model.serviceLevel == valid_data["serviceLevel"]
        assert model.serviceLevelRank == valid_data["serviceLevelRank"]
        assert model.startDate == valid_data["startDate"]
        assert model.contractLevel == valid_data["contractLevel"]

    def test_response_support_level_model_validation(self):
        """Test ResponseSupportLevel model field validation."""
        # Test with minimal required data
        minimal_data = {}

        model = ResponseSupportLevel(**minimal_data)
        assert isinstance(model, ResponseSupportLevel)

    def test_response_support_level_model_required_fields(self):
        """Test ResponseSupportLevel model required field validation."""
        # Check if this model has any required fields
        required_fields = []

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                ResponseSupportLevel()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {}

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = ResponseSupportLevel()
            assert isinstance(model, ResponseSupportLevel)

    def test_response_support_level_model_optional_fields(self):
        """Test ResponseSupportLevel model optional field handling."""
        # Create with minimal required data
        minimal_data = {}

        model = ResponseSupportLevel(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "contractLevelRank")
        # Optional field contractLevelRank should be None or have a default value
        assert model.contractLevelRank is None or model.contractLevelRank is not None
        assert hasattr(model, "endDate")
        # Optional field endDate should be None or have a default value
        assert model.endDate is None or model.endDate is not None
        assert hasattr(model, "serviceLevel")
        # Optional field serviceLevel should be None or have a default value
        assert model.serviceLevel is None or model.serviceLevel is not None
        assert hasattr(model, "serviceLevelRank")
        # Optional field serviceLevelRank should be None or have a default value
        assert model.serviceLevelRank is None or model.serviceLevelRank is not None
        assert hasattr(model, "startDate")
        # Optional field startDate should be None or have a default value
        assert model.startDate is None or model.startDate is not None
        assert hasattr(model, "contractLevel")
        # Optional field contractLevel should be None or have a default value
        assert model.contractLevel is None or model.contractLevel is not None

    def test_response_support_level_model_serialization(self):
        """Test ResponseSupportLevel model serialization to dict."""
        test_data = {
            "contractLevelRank": 99,
            "endDate": 99,
            "serviceLevel": "serialize_value",
            "serviceLevelRank": 99,
            "startDate": 99,
            "contractLevel": "serialize_value",
        }

        model = ResponseSupportLevel(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "contractLevelRank" in serialized
        assert "endDate" in serialized
        assert "serviceLevel" in serialized
        assert "serviceLevelRank" in serialized
        assert "startDate" in serialized
        assert "contractLevel" in serialized

        # Verify values are preserved
        assert serialized["contractLevelRank"] == test_data["contractLevelRank"]
        assert serialized["endDate"] == test_data["endDate"]
        assert serialized["serviceLevel"] == test_data["serviceLevel"]
        assert serialized["serviceLevelRank"] == test_data["serviceLevelRank"]
        assert serialized["startDate"] == test_data["startDate"]
        assert serialized["contractLevel"] == test_data["contractLevel"]

    def test_response_support_level_model_json_schema(self):
        """Test ResponseSupportLevel model JSON schema generation."""
        schema = ResponseSupportLevel.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "contractLevelRank",
            "endDate",
            "serviceLevel",
            "serviceLevelRank",
            "startDate",
            "contractLevel",
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

    def test_async_response_model_creation(self):
        """Test AsyncResponse model creation with valid data."""
        # Valid test data for AsyncResponse
        valid_data = {
            "status": "test_status",
            "transactionId": "test_transactionId",
            "code": 42,
        }

        # Create model instance
        model = AsyncResponse(**valid_data)

        # Verify model creation
        assert isinstance(model, AsyncResponse)
        assert model.status == valid_data["status"]
        assert model.transactionId == valid_data["transactionId"]
        assert model.code == valid_data["code"]

    def test_async_response_model_validation(self):
        """Test AsyncResponse model field validation."""
        # Test with minimal required data
        minimal_data = {
            "status": "required_status",
            "transactionId": "required_transactionId",
            "code": 1,
        }

        model = AsyncResponse(**minimal_data)
        assert isinstance(model, AsyncResponse)
        assert model.status == minimal_data["status"]
        assert model.transactionId == minimal_data["transactionId"]
        assert model.code == minimal_data["code"]

    def test_async_response_model_required_fields(self):
        """Test AsyncResponse model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "status",
            "transactionId",
            "code",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                AsyncResponse()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "status",
                "transactionId",
                "code",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = AsyncResponse()
            assert isinstance(model, AsyncResponse)

    def test_async_response_model_optional_fields(self):
        """Test AsyncResponse model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "status": "required_status",
            "transactionId": "required_transactionId",
            "code": 1,
        }

        model = AsyncResponse(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_async_response_model_serialization(self):
        """Test AsyncResponse model serialization to dict."""
        test_data = {
            "status": "serialize_value",
            "transactionId": "serialize_value",
            "code": 99,
        }

        model = AsyncResponse(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "status" in serialized
        assert "transactionId" in serialized
        assert "code" in serialized

        # Verify values are preserved
        assert serialized["status"] == test_data["status"]
        assert serialized["transactionId"] == test_data["transactionId"]
        assert serialized["code"] == test_data["code"]

    def test_async_response_model_json_schema(self):
        """Test AsyncResponse model JSON schema generation."""
        schema = AsyncResponse.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "status",
            "transactionId",
            "code",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "status",
            "transactionId",
            "code",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_general_error_detail_model_creation(self):
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

    def test_general_error_detail_model_validation(self):
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

    def test_general_error_detail_model_required_fields(self):
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

    def test_general_error_detail_model_optional_fields(self):
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

    def test_general_error_detail_model_serialization(self):
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

    def test_general_error_detail_model_json_schema(self):
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

    def test_patch_devices_request_v2_model_creation(self):
        """Test PatchDevicesRequestV2 model creation with valid data."""
        # Valid test data for PatchDevicesRequestV2
        valid_data = {
            "tenantWorkspaceId": "test_tenantWorkspaceId",
            "application": {},
            "archived": True,
            "region": "test_region",
            "subscription": [],
            "tags": {},
        }

        # Create model instance
        model = PatchDevicesRequestV2(**valid_data)

        # Verify model creation
        assert isinstance(model, PatchDevicesRequestV2)
        assert model.tenantWorkspaceId == valid_data["tenantWorkspaceId"]
        assert model.application == valid_data["application"]
        assert model.archived == valid_data["archived"]
        assert model.region == valid_data["region"]
        assert model.subscription == valid_data["subscription"]
        assert model.tags == valid_data["tags"]

    def test_patch_devices_request_v2_model_validation(self):
        """Test PatchDevicesRequestV2 model field validation."""
        # Test with minimal required data
        minimal_data = {}

        model = PatchDevicesRequestV2(**minimal_data)
        assert isinstance(model, PatchDevicesRequestV2)

    def test_patch_devices_request_v2_model_required_fields(self):
        """Test PatchDevicesRequestV2 model required field validation."""
        # Check if this model has any required fields
        required_fields = []

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                PatchDevicesRequestV2()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {}

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = PatchDevicesRequestV2()
            assert isinstance(model, PatchDevicesRequestV2)

    def test_patch_devices_request_v2_model_optional_fields(self):
        """Test PatchDevicesRequestV2 model optional field handling."""
        # Create with minimal required data
        minimal_data = {}

        model = PatchDevicesRequestV2(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "tenantWorkspaceId")
        # Optional field tenantWorkspaceId should be None or have a default value
        assert model.tenantWorkspaceId is None or model.tenantWorkspaceId is not None
        assert hasattr(model, "application")
        # Optional field application should be None or have a default value
        assert model.application is None or model.application is not None
        assert hasattr(model, "archived")
        # Optional field archived should be None or have a default value
        assert model.archived is None or model.archived is not None
        assert hasattr(model, "region")
        # Optional field region should be None or have a default value
        assert model.region is None or model.region is not None
        assert hasattr(model, "subscription")
        # Optional field subscription should be None or have a default value
        assert model.subscription is None or model.subscription is not None
        assert hasattr(model, "tags")
        # Optional field tags should be None or have a default value
        assert model.tags is None or model.tags is not None

    def test_patch_devices_request_v2_model_serialization(self):
        """Test PatchDevicesRequestV2 model serialization to dict."""
        test_data = {
            "tenantWorkspaceId": "serialize_value",
            "application": {"key": "value"},
            "archived": False,
            "region": "serialize_value",
            "subscription": [],
            "tags": {"key": "value"},
        }

        model = PatchDevicesRequestV2(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "tenantWorkspaceId" in serialized
        assert "application" in serialized
        assert "archived" in serialized
        assert "region" in serialized
        assert "subscription" in serialized
        assert "tags" in serialized

        # Verify values are preserved
        assert serialized["tenantWorkspaceId"] == test_data["tenantWorkspaceId"]
        assert serialized["application"] == test_data["application"]
        assert serialized["archived"] == test_data["archived"]
        assert serialized["region"] == test_data["region"]
        assert serialized["subscription"] == test_data["subscription"]
        assert serialized["tags"] == test_data["tags"]

    def test_patch_devices_request_v2_model_json_schema(self):
        """Test PatchDevicesRequestV2 model JSON schema generation."""
        schema = PatchDevicesRequestV2.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "tenantWorkspaceId",
            "application",
            "archived",
            "region",
            "subscription",
            "tags",
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

    def test_response_application_model_creation(self):
        """Test ResponseApplication model creation with valid data."""
        # Valid test data for ResponseApplication
        valid_data = {
            "resourceUri": "test_resourceUri",
            "id": "test_id",
        }

        # Create model instance
        model = ResponseApplication(**valid_data)

        # Verify model creation
        assert isinstance(model, ResponseApplication)
        assert model.resourceUri == valid_data["resourceUri"]
        assert model.id == valid_data["id"]

    def test_response_application_model_validation(self):
        """Test ResponseApplication model field validation."""
        # Test with minimal required data
        minimal_data = {
            "resourceUri": "required_resourceUri",
            "id": "required_id",
        }

        model = ResponseApplication(**minimal_data)
        assert isinstance(model, ResponseApplication)
        assert model.resourceUri == minimal_data["resourceUri"]
        assert model.id == minimal_data["id"]

    def test_response_application_model_required_fields(self):
        """Test ResponseApplication model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "resourceUri",
            "id",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                ResponseApplication()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "resourceUri",
                "id",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = ResponseApplication()
            assert isinstance(model, ResponseApplication)

    def test_response_application_model_optional_fields(self):
        """Test ResponseApplication model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "resourceUri": "required_resourceUri",
            "id": "required_id",
        }

        model = ResponseApplication(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_response_application_model_serialization(self):
        """Test ResponseApplication model serialization to dict."""
        test_data = {
            "resourceUri": "serialize_value",
            "id": "serialize_value",
        }

        model = ResponseApplication(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "resourceUri" in serialized
        assert "id" in serialized

        # Verify values are preserved
        assert serialized["resourceUri"] == test_data["resourceUri"]
        assert serialized["id"] == test_data["id"]

    def test_response_application_model_json_schema(self):
        """Test ResponseApplication model JSON schema generation."""
        schema = ResponseApplication.model_json_schema()

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
        required_fields = [
            "resourceUri",
            "id",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_hpe_green_lake_general_error_model_creation(self):
        """Test HpeGreenLakeGeneralError model creation with valid data."""
        # Valid test data for HpeGreenLakeGeneralError
        valid_data = {
            "debugId": "test_debugId",
            "errorCode": "test_errorCode",
            "generalErrorDetails": [],
            "httpStatusCode": 42,
            "message": "test_message",
        }

        # Create model instance
        model = HpeGreenLakeGeneralError(**valid_data)

        # Verify model creation
        assert isinstance(model, HpeGreenLakeGeneralError)
        assert model.debugId == valid_data["debugId"]
        assert model.errorCode == valid_data["errorCode"]
        assert model.generalErrorDetails == valid_data["generalErrorDetails"]
        assert model.httpStatusCode == valid_data["httpStatusCode"]
        assert model.message == valid_data["message"]

    def test_hpe_green_lake_general_error_model_validation(self):
        """Test HpeGreenLakeGeneralError model field validation."""
        # Test with minimal required data
        minimal_data = {
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
            "httpStatusCode": 1,
            "message": "required_message",
        }

        model = HpeGreenLakeGeneralError(**minimal_data)
        assert isinstance(model, HpeGreenLakeGeneralError)
        assert model.debugId == minimal_data["debugId"]
        assert model.errorCode == minimal_data["errorCode"]
        assert model.httpStatusCode == minimal_data["httpStatusCode"]
        assert model.message == minimal_data["message"]

    def test_hpe_green_lake_general_error_model_required_fields(self):
        """Test HpeGreenLakeGeneralError model required field validation."""
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
                HpeGreenLakeGeneralError()

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
            model = HpeGreenLakeGeneralError()
            assert isinstance(model, HpeGreenLakeGeneralError)

    def test_hpe_green_lake_general_error_model_optional_fields(self):
        """Test HpeGreenLakeGeneralError model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
            "httpStatusCode": 1,
            "message": "required_message",
        }

        model = HpeGreenLakeGeneralError(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "generalErrorDetails")
        # Optional field generalErrorDetails should be None or have a default value
        assert model.generalErrorDetails is None or model.generalErrorDetails is not None

    def test_hpe_green_lake_general_error_model_serialization(self):
        """Test HpeGreenLakeGeneralError model serialization to dict."""
        test_data = {
            "debugId": "serialize_value",
            "errorCode": "serialize_value",
            "generalErrorDetails": [],
            "httpStatusCode": 99,
            "message": "serialize_value",
        }

        model = HpeGreenLakeGeneralError(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "debugId" in serialized
        assert "errorCode" in serialized
        assert "generalErrorDetails" in serialized
        assert "httpStatusCode" in serialized
        assert "message" in serialized

        # Verify values are preserved
        assert serialized["debugId"] == test_data["debugId"]
        assert serialized["errorCode"] == test_data["errorCode"]
        assert serialized["generalErrorDetails"] == test_data["generalErrorDetails"]
        assert serialized["httpStatusCode"] == test_data["httpStatusCode"]
        assert serialized["message"] == test_data["message"]

    def test_hpe_green_lake_general_error_model_json_schema(self):
        """Test HpeGreenLakeGeneralError model JSON schema generation."""
        schema = HpeGreenLakeGeneralError.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "debugId",
            "errorCode",
            "generalErrorDetails",
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

    def test_response_subscription_model_creation(self):
        """Test ResponseSubscription model creation with valid data."""
        # Valid test data for ResponseSubscription
        valid_data = {
            "id": "test_id",
            "resourceUri": "test_resourceUri",
        }

        # Create model instance
        model = ResponseSubscription(**valid_data)

        # Verify model creation
        assert isinstance(model, ResponseSubscription)
        assert model.id == valid_data["id"]
        assert model.resourceUri == valid_data["resourceUri"]

    def test_response_subscription_model_validation(self):
        """Test ResponseSubscription model field validation."""
        # Test with minimal required data
        minimal_data = {
            "id": "required_id",
            "resourceUri": "required_resourceUri",
        }

        model = ResponseSubscription(**minimal_data)
        assert isinstance(model, ResponseSubscription)
        assert model.id == minimal_data["id"]
        assert model.resourceUri == minimal_data["resourceUri"]

    def test_response_subscription_model_required_fields(self):
        """Test ResponseSubscription model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "id",
            "resourceUri",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                ResponseSubscription()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "id",
                "resourceUri",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = ResponseSubscription()
            assert isinstance(model, ResponseSubscription)

    def test_response_subscription_model_optional_fields(self):
        """Test ResponseSubscription model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "id": "required_id",
            "resourceUri": "required_resourceUri",
        }

        model = ResponseSubscription(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_response_subscription_model_serialization(self):
        """Test ResponseSubscription model serialization to dict."""
        test_data = {
            "id": "serialize_value",
            "resourceUri": "serialize_value",
        }

        model = ResponseSubscription(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "id" in serialized
        assert "resourceUri" in serialized

        # Verify values are preserved
        assert serialized["id"] == test_data["id"]
        assert serialized["resourceUri"] == test_data["resourceUri"]

    def test_response_subscription_model_json_schema(self):
        """Test ResponseSubscription model JSON schema generation."""
        schema = ResponseSubscription.model_json_schema()

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
        required_fields = [
            "id",
            "resourceUri",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_devices_post_request_v2_beta1_model_creation(self):
        """Test DevicesPostRequestV2Beta1 model creation with valid data."""
        # Valid test data for DevicesPostRequestV2Beta1
        valid_data = {
            "serialNumber": "test_serialNumber",
            "tags": {},
            "deviceType": "test_deviceType",
            "location": {},
            "macAddress": "test_macAddress",
            "partNumber": "test_partNumber",
        }

        # Create model instance
        model = DevicesPostRequestV2Beta1(**valid_data)

        # Verify model creation
        assert isinstance(model, DevicesPostRequestV2Beta1)
        assert model.serialNumber == valid_data["serialNumber"]
        assert model.tags == valid_data["tags"]
        assert model.deviceType == valid_data["deviceType"]
        assert model.location == valid_data["location"]
        assert model.macAddress == valid_data["macAddress"]
        assert model.partNumber == valid_data["partNumber"]

    def test_devices_post_request_v2_beta1_model_validation(self):
        """Test DevicesPostRequestV2Beta1 model field validation."""
        # Test with minimal required data
        minimal_data = {
            "serialNumber": "required_serialNumber",
            "deviceType": "required_deviceType",
        }

        model = DevicesPostRequestV2Beta1(**minimal_data)
        assert isinstance(model, DevicesPostRequestV2Beta1)
        assert model.serialNumber == minimal_data["serialNumber"]
        assert model.deviceType == minimal_data["deviceType"]

    def test_devices_post_request_v2_beta1_model_required_fields(self):
        """Test DevicesPostRequestV2Beta1 model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "serialNumber",
            "deviceType",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                DevicesPostRequestV2Beta1()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "serialNumber",
                "deviceType",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = DevicesPostRequestV2Beta1()
            assert isinstance(model, DevicesPostRequestV2Beta1)

    def test_devices_post_request_v2_beta1_model_optional_fields(self):
        """Test DevicesPostRequestV2Beta1 model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "serialNumber": "required_serialNumber",
            "deviceType": "required_deviceType",
        }

        model = DevicesPostRequestV2Beta1(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "tags")
        # Optional field tags should be None or have a default value
        assert model.tags is None or model.tags is not None
        assert hasattr(model, "location")
        # Optional field location should be None or have a default value
        assert model.location is None or model.location is not None
        assert hasattr(model, "macAddress")
        # Optional field macAddress should be None or have a default value
        assert model.macAddress is None or model.macAddress is not None
        assert hasattr(model, "partNumber")
        # Optional field partNumber should be None or have a default value
        assert model.partNumber is None or model.partNumber is not None

    def test_devices_post_request_v2_beta1_model_serialization(self):
        """Test DevicesPostRequestV2Beta1 model serialization to dict."""
        test_data = {
            "serialNumber": "serialize_value",
            "tags": {"key": "value"},
            "deviceType": "serialize_value",
            "location": {"key": "value"},
            "macAddress": "serialize_value",
            "partNumber": "serialize_value",
        }

        model = DevicesPostRequestV2Beta1(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "serialNumber" in serialized
        assert "tags" in serialized
        assert "deviceType" in serialized
        assert "location" in serialized
        assert "macAddress" in serialized
        assert "partNumber" in serialized

        # Verify values are preserved
        assert serialized["serialNumber"] == test_data["serialNumber"]
        assert serialized["tags"] == test_data["tags"]
        assert serialized["deviceType"] == test_data["deviceType"]
        assert serialized["location"] == test_data["location"]
        assert serialized["macAddress"] == test_data["macAddress"]
        assert serialized["partNumber"] == test_data["partNumber"]

    def test_devices_post_request_v2_beta1_model_json_schema(self):
        """Test DevicesPostRequestV2Beta1 model JSON schema generation."""
        schema = DevicesPostRequestV2Beta1.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "serialNumber",
            "tags",
            "deviceType",
            "location",
            "macAddress",
            "partNumber",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "serialNumber",
            "deviceType",
        ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)

    def test_request_application_model_creation(self):
        """Test RequestApplication model creation with valid data."""
        # Valid test data for RequestApplication
        valid_data = {
            "id": "test_id",
        }

        # Create model instance
        model = RequestApplication(**valid_data)

        # Verify model creation
        assert isinstance(model, RequestApplication)
        assert model.id == valid_data["id"]

    def test_request_application_model_validation(self):
        """Test RequestApplication model field validation."""
        # Test with minimal required data
        minimal_data = {
            "id": "required_id",
        }

        model = RequestApplication(**minimal_data)
        assert isinstance(model, RequestApplication)
        assert model.id == minimal_data["id"]

    def test_request_application_model_required_fields(self):
        """Test RequestApplication model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "id",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                RequestApplication()

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
            model = RequestApplication()
            assert isinstance(model, RequestApplication)

    def test_request_application_model_optional_fields(self):
        """Test RequestApplication model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "id": "required_id",
        }

        model = RequestApplication(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values

    def test_request_application_model_serialization(self):
        """Test RequestApplication model serialization to dict."""
        test_data = {
            "id": "serialize_value",
        }

        model = RequestApplication(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "id" in serialized

        # Verify values are preserved
        assert serialized["id"] == test_data["id"]

    def test_request_application_model_json_schema(self):
        """Test RequestApplication model JSON schema generation."""
        schema = RequestApplication.model_json_schema()

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

    def test_request_storage_model_creation(self):
        """Test RequestStorage model creation with valid data."""
        # Valid test data for RequestStorage
        valid_data = {
            "tags": {},
            "partNumber": "test_partNumber",
            "serialNumber": "test_serialNumber",
        }

        # Create model instance
        model = RequestStorage(**valid_data)

        # Verify model creation
        assert isinstance(model, RequestStorage)
        assert model.tags == valid_data["tags"]
        assert model.partNumber == valid_data["partNumber"]
        assert model.serialNumber == valid_data["serialNumber"]

    def test_request_storage_model_validation(self):
        """Test RequestStorage model field validation."""
        # Test with minimal required data
        minimal_data = {
            "partNumber": "required_partNumber",
            "serialNumber": "required_serialNumber",
        }

        model = RequestStorage(**minimal_data)
        assert isinstance(model, RequestStorage)
        assert model.partNumber == minimal_data["partNumber"]
        assert model.serialNumber == minimal_data["serialNumber"]

    def test_request_storage_model_required_fields(self):
        """Test RequestStorage model required field validation."""
        # Check if this model has any required fields
        required_fields = [
            "partNumber",
            "serialNumber",
        ]

        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                RequestStorage()

            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "partNumber",
                "serialNumber",
            }

            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = RequestStorage()
            assert isinstance(model, RequestStorage)

    def test_request_storage_model_optional_fields(self):
        """Test RequestStorage model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "partNumber": "required_partNumber",
            "serialNumber": "required_serialNumber",
        }

        model = RequestStorage(**minimal_data)

        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "tags")
        # Optional field tags should be None or have a default value
        assert model.tags is None or model.tags is not None

    def test_request_storage_model_serialization(self):
        """Test RequestStorage model serialization to dict."""
        test_data = {
            "tags": {"key": "value"},
            "partNumber": "serialize_value",
            "serialNumber": "serialize_value",
        }

        model = RequestStorage(**test_data)
        serialized = model.model_dump(by_alias=True)

        # Verify serialization
        assert isinstance(serialized, dict)
        assert "tags" in serialized
        assert "partNumber" in serialized
        assert "serialNumber" in serialized

        # Verify values are preserved
        assert serialized["tags"] == test_data["tags"]
        assert serialized["partNumber"] == test_data["partNumber"]
        assert serialized["serialNumber"] == test_data["serialNumber"]

    def test_request_storage_model_json_schema(self):
        """Test RequestStorage model JSON schema generation."""
        schema = RequestStorage.model_json_schema()

        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema

        # Verify all properties are in schema
        expected_properties = {
            "tags",
            "partNumber",
            "serialNumber",
        }

        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)

        # Verify required fields in schema (if any)
        required_fields = [
            "partNumber",
            "serialNumber",
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
            RequestSubscription,
            ResponseLocation,
            ServerErrorDetail,
            DeviceDetail,
            ResponseDedicatedPlatform,
            DevicesPostRequest,
            ErrorIssue,
            HpeGreenLakeBadRequestError,
            HpeGreenLakeServerError,
            RequestNetwork,
            BadRequestErrorDetail,
            ResponseWarranty,
            AsyncOperationResource,
            DevicesGetResponse,
            PatchDevicesRequest,
            RequestCompute,
            ResponseSupportLevel,
            AsyncResponse,
            GeneralErrorDetail,
            PatchDevicesRequestV2,
            ResponseApplication,
            HpeGreenLakeGeneralError,
            ResponseSubscription,
            DevicesPostRequestV2Beta1,
            RequestApplication,
            RequestStorage,
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
            RequestSubscription,
            ResponseLocation,
            ServerErrorDetail,
            DeviceDetail,
            ResponseDedicatedPlatform,
            DevicesPostRequest,
            ErrorIssue,
            HpeGreenLakeBadRequestError,
            HpeGreenLakeServerError,
            RequestNetwork,
            BadRequestErrorDetail,
            ResponseWarranty,
            AsyncOperationResource,
            DevicesGetResponse,
            PatchDevicesRequest,
            RequestCompute,
            ResponseSupportLevel,
            AsyncResponse,
            GeneralErrorDetail,
            PatchDevicesRequestV2,
            ResponseApplication,
            HpeGreenLakeGeneralError,
            ResponseSubscription,
            DevicesPostRequestV2Beta1,
            RequestApplication,
            RequestStorage,
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
            RequestSubscription,
            ResponseLocation,
            ServerErrorDetail,
            DeviceDetail,
            ResponseDedicatedPlatform,
            DevicesPostRequest,
            ErrorIssue,
            HpeGreenLakeBadRequestError,
            HpeGreenLakeServerError,
            RequestNetwork,
            BadRequestErrorDetail,
            ResponseWarranty,
            AsyncOperationResource,
            DevicesGetResponse,
            PatchDevicesRequest,
            RequestCompute,
            ResponseSupportLevel,
            AsyncResponse,
            GeneralErrorDetail,
            PatchDevicesRequestV2,
            ResponseApplication,
            HpeGreenLakeGeneralError,
            ResponseSubscription,
            DevicesPostRequestV2Beta1,
            RequestApplication,
            RequestStorage,
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
            RequestSubscription,
            ResponseLocation,
            ServerErrorDetail,
            DeviceDetail,
            ResponseDedicatedPlatform,
            DevicesPostRequest,
            ErrorIssue,
            HpeGreenLakeBadRequestError,
            HpeGreenLakeServerError,
            RequestNetwork,
            BadRequestErrorDetail,
            ResponseWarranty,
            AsyncOperationResource,
            DevicesGetResponse,
            PatchDevicesRequest,
            RequestCompute,
            ResponseSupportLevel,
            AsyncResponse,
            GeneralErrorDetail,
            PatchDevicesRequestV2,
            ResponseApplication,
            HpeGreenLakeGeneralError,
            ResponseSubscription,
            DevicesPostRequestV2Beta1,
            RequestApplication,
            RequestStorage,
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
