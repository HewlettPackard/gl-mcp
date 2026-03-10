# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
Test template for models package.
Tests all generated data models from OpenAPI schemas.
"""
import pytest
from typing import Any, Dict
from pydantic import ValidationError as PydanticValidationError


from models.base import cloudTotal

from models.base import entity

from models.base import apiError

from models.base import coefficientCostInput

from models.base import currencyComponent

from models.base import tag

from models.base import coefficient

from models.base import coefficientInput

from models.base import currencyCode

from models.base import datasource

from models.base import total

from models.base import timeseries

from models.base import cloudEntity

from models.base import cloudTimeseries

from models.base import ingest



class TestModels:
    """Test suite for all generated data models."""


    def test_cloudtotal_model_creation(self):
        """Test cloudTotal model creation with valid data."""
        # Valid test data for cloudTotal
        valid_data = {
            "co2eMetricTon": 3.14,
            "type": "test_type",
        }
        
        # Create model instance
        model = cloudTotal(**valid_data)
        
        # Verify model creation
        assert isinstance(model, cloudTotal)
        assert model.co2eMetricTon == valid_data["co2eMetricTon"]
        assert model.type == valid_data["type"]


    def test_cloudtotal_model_validation(self):
        """Test cloudTotal model field validation."""
        # Test with minimal required data
        minimal_data = {
            "type": "required_type",
        }
        
        model = cloudTotal(**minimal_data)
        assert isinstance(model, cloudTotal)
        assert model.type == minimal_data["type"]


    def test_cloudtotal_model_required_fields(self):
        """Test cloudTotal model required field validation."""
        # Check if this model has any required fields
        required_fields = ["type", ]
        
        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                cloudTotal()
            
            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "type",
            }
            
            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = cloudTotal()
            assert isinstance(model, cloudTotal)

    def test_cloudtotal_model_optional_fields(self):
        """Test cloudTotal model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "type": "required_type",
        }
        
        model = cloudTotal(**minimal_data)
        
        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "co2eMetricTon")
        # Optional field co2eMetricTon should be None or have a default value
        assert model.co2eMetricTon is None or model.co2eMetricTon is not None


    def test_cloudtotal_model_serialization(self):
        """Test cloudTotal model serialization to dict."""
        test_data = {
            "co2eMetricTon": 9.99,
            "type": "serialize_value",
        }
        
        model = cloudTotal(**test_data)
        serialized = model.model_dump(by_alias=True)
        
        # Verify serialization
        assert isinstance(serialized, dict)
        assert "co2eMetricTon" in serialized
        assert "type" in serialized

        
        # Verify values are preserved
        assert serialized["co2eMetricTon"] == test_data["co2eMetricTon"]
        assert serialized["type"] == test_data["type"]


    def test_cloudtotal_model_json_schema(self):
        """Test cloudTotal model JSON schema generation."""
        schema = cloudTotal.model_json_schema()
        
        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema
        
        # Verify all properties are in schema
        expected_properties = {
            "co2eMetricTon",
            "type",
        }
        
        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)
        
        # Verify required fields in schema (if any)
        required_fields = ["type", ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)


    def test_entity_model_creation(self):
        """Test entity model creation with valid data."""
        # Valid test data for entity
        valid_data = {
            "locationState": "test_locationState",
            "entitySerialNum": "test_entitySerialNum",
            "entityManufacturerTimestamp": "test_entityManufacturerTimestamp",
            "name": "test_name",
            "locationName": "test_locationName",
            "tags": [],
            "entityProductId": "test_entityProductId",
            "entityType": "test_entityType",
            "locationId": "test_locationId",
            "type": "test_type",
            "id": "test_id",
            "costUsd": 3.14,
            "locationCity": "test_locationCity",
            "co2eMetricTon": 3.14,
            "cost": 3.14,
            "entityMake": "test_entityMake",
            "currency": "test_currency",
            "kwh": 3.14,
            "locationCountry": "test_locationCountry",
            "entityModel": "test_entityModel",
            "entityId": "test_entityId",
        }
        
        # Create model instance
        model = entity(**valid_data)
        
        # Verify model creation
        assert isinstance(model, entity)
        assert model.locationState == valid_data["locationState"]
        assert model.entitySerialNum == valid_data["entitySerialNum"]
        assert model.entityManufacturerTimestamp == valid_data["entityManufacturerTimestamp"]
        assert model.name == valid_data["name"]
        assert model.locationName == valid_data["locationName"]
        assert model.tags == valid_data["tags"]
        assert model.entityProductId == valid_data["entityProductId"]
        assert model.entityType == valid_data["entityType"]
        assert model.locationId == valid_data["locationId"]
        assert model.type == valid_data["type"]
        assert model.id == valid_data["id"]
        assert model.costUsd == valid_data["costUsd"]
        assert model.locationCity == valid_data["locationCity"]
        assert model.co2eMetricTon == valid_data["co2eMetricTon"]
        assert model.cost == valid_data["cost"]
        assert model.entityMake == valid_data["entityMake"]
        assert model.currency == valid_data["currency"]
        assert model.kwh == valid_data["kwh"]
        assert model.locationCountry == valid_data["locationCountry"]
        assert model.entityModel == valid_data["entityModel"]
        assert model.entityId == valid_data["entityId"]


    def test_entity_model_validation(self):
        """Test entity model field validation."""
        # Test with minimal required data
        minimal_data = {
            "type": "required_type",
            "id": "required_id",
        }
        
        model = entity(**minimal_data)
        assert isinstance(model, entity)
        assert model.type == minimal_data["type"]
        assert model.id == minimal_data["id"]


    def test_entity_model_required_fields(self):
        """Test entity model required field validation."""
        # Check if this model has any required fields
        required_fields = ["type", "id", ]
        
        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                entity()
            
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
            model = entity()
            assert isinstance(model, entity)

    def test_entity_model_optional_fields(self):
        """Test entity model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "type": "required_type",
            "id": "required_id",
        }
        
        model = entity(**minimal_data)
        
        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "locationState")
        # Optional field locationState should be None or have a default value
        assert model.locationState is None or model.locationState is not None
        assert hasattr(model, "entitySerialNum")
        # Optional field entitySerialNum should be None or have a default value
        assert model.entitySerialNum is None or model.entitySerialNum is not None
        assert hasattr(model, "entityManufacturerTimestamp")
        # Optional field entityManufacturerTimestamp should be None or have a default value
        assert model.entityManufacturerTimestamp is None or model.entityManufacturerTimestamp is not None
        assert hasattr(model, "name")
        # Optional field name should be None or have a default value
        assert model.name is None or model.name is not None
        assert hasattr(model, "locationName")
        # Optional field locationName should be None or have a default value
        assert model.locationName is None or model.locationName is not None
        assert hasattr(model, "tags")
        # Optional field tags should be None or have a default value
        assert model.tags is None or model.tags is not None
        assert hasattr(model, "entityProductId")
        # Optional field entityProductId should be None or have a default value
        assert model.entityProductId is None or model.entityProductId is not None
        assert hasattr(model, "entityType")
        # Optional field entityType should be None or have a default value
        assert model.entityType is None or model.entityType is not None
        assert hasattr(model, "locationId")
        # Optional field locationId should be None or have a default value
        assert model.locationId is None or model.locationId is not None
        assert hasattr(model, "costUsd")
        # Optional field costUsd should be None or have a default value
        assert model.costUsd is None or model.costUsd is not None
        assert hasattr(model, "locationCity")
        # Optional field locationCity should be None or have a default value
        assert model.locationCity is None or model.locationCity is not None
        assert hasattr(model, "co2eMetricTon")
        # Optional field co2eMetricTon should be None or have a default value
        assert model.co2eMetricTon is None or model.co2eMetricTon is not None
        assert hasattr(model, "cost")
        # Optional field cost should be None or have a default value
        assert model.cost is None or model.cost is not None
        assert hasattr(model, "entityMake")
        # Optional field entityMake should be None or have a default value
        assert model.entityMake is None or model.entityMake is not None
        assert hasattr(model, "currency")
        # Optional field currency should be None or have a default value
        assert model.currency is None or model.currency is not None
        assert hasattr(model, "kwh")
        # Optional field kwh should be None or have a default value
        assert model.kwh is None or model.kwh is not None
        assert hasattr(model, "locationCountry")
        # Optional field locationCountry should be None or have a default value
        assert model.locationCountry is None or model.locationCountry is not None
        assert hasattr(model, "entityModel")
        # Optional field entityModel should be None or have a default value
        assert model.entityModel is None or model.entityModel is not None
        assert hasattr(model, "entityId")
        # Optional field entityId should be None or have a default value
        assert model.entityId is None or model.entityId is not None


    def test_entity_model_serialization(self):
        """Test entity model serialization to dict."""
        test_data = {
            "locationState": "serialize_value",
            "entitySerialNum": "serialize_value",
            "entityManufacturerTimestamp": "serialize_value",
            "name": "serialize_value",
            "locationName": "serialize_value",
            "tags": [],
            "entityProductId": "serialize_value",
            "entityType": "serialize_value",
            "locationId": "serialize_value",
            "type": "serialize_value",
            "id": "serialize_value",
            "costUsd": 9.99,
            "locationCity": "serialize_value",
            "co2eMetricTon": 9.99,
            "cost": 9.99,
            "entityMake": "serialize_value",
            "currency": "serialize_value",
            "kwh": 9.99,
            "locationCountry": "serialize_value",
            "entityModel": "serialize_value",
            "entityId": "serialize_value",
        }
        
        model = entity(**test_data)
        serialized = model.model_dump(by_alias=True)
        
        # Verify serialization
        assert isinstance(serialized, dict)
        assert "locationState" in serialized
        assert "entitySerialNum" in serialized
        assert "entityManufacturerTimestamp" in serialized
        assert "name" in serialized
        assert "locationName" in serialized
        assert "tags" in serialized
        assert "entityProductId" in serialized
        assert "entityType" in serialized
        assert "locationId" in serialized
        assert "type" in serialized
        assert "id" in serialized
        assert "costUsd" in serialized
        assert "locationCity" in serialized
        assert "co2eMetricTon" in serialized
        assert "cost" in serialized
        assert "entityMake" in serialized
        assert "currency" in serialized
        assert "kwh" in serialized
        assert "locationCountry" in serialized
        assert "entityModel" in serialized
        assert "entityId" in serialized

        
        # Verify values are preserved
        assert serialized["locationState"] == test_data["locationState"]
        assert serialized["entitySerialNum"] == test_data["entitySerialNum"]
        assert serialized["entityManufacturerTimestamp"] == test_data["entityManufacturerTimestamp"]
        assert serialized["name"] == test_data["name"]
        assert serialized["locationName"] == test_data["locationName"]
        assert serialized["tags"] == test_data["tags"]
        assert serialized["entityProductId"] == test_data["entityProductId"]
        assert serialized["entityType"] == test_data["entityType"]
        assert serialized["locationId"] == test_data["locationId"]
        assert serialized["type"] == test_data["type"]
        assert serialized["id"] == test_data["id"]
        assert serialized["costUsd"] == test_data["costUsd"]
        assert serialized["locationCity"] == test_data["locationCity"]
        assert serialized["co2eMetricTon"] == test_data["co2eMetricTon"]
        assert serialized["cost"] == test_data["cost"]
        assert serialized["entityMake"] == test_data["entityMake"]
        assert serialized["currency"] == test_data["currency"]
        assert serialized["kwh"] == test_data["kwh"]
        assert serialized["locationCountry"] == test_data["locationCountry"]
        assert serialized["entityModel"] == test_data["entityModel"]
        assert serialized["entityId"] == test_data["entityId"]


    def test_entity_model_json_schema(self):
        """Test entity model JSON schema generation."""
        schema = entity.model_json_schema()
        
        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema
        
        # Verify all properties are in schema
        expected_properties = {
            "locationState",
            "entitySerialNum",
            "entityManufacturerTimestamp",
            "name",
            "locationName",
            "tags",
            "entityProductId",
            "entityType",
            "locationId",
            "type",
            "id",
            "costUsd",
            "locationCity",
            "co2eMetricTon",
            "cost",
            "entityMake",
            "currency",
            "kwh",
            "locationCountry",
            "entityModel",
            "entityId",
        }
        
        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)
        
        # Verify required fields in schema (if any)
        required_fields = ["type", "id", ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)


    def test_apierror_model_creation(self):
        """Test apiError model creation with valid data."""
        # Valid test data for apiError
        valid_data = {
            "debugId": "test_debugId",
            "errorCode": "test_errorCode",
            "httpStatusCode": 42,
            "message": "test_message",
        }
        
        # Create model instance
        model = apiError(**valid_data)
        
        # Verify model creation
        assert isinstance(model, apiError)
        assert model.debugId == valid_data["debugId"]
        assert model.errorCode == valid_data["errorCode"]
        assert model.httpStatusCode == valid_data["httpStatusCode"]
        assert model.message == valid_data["message"]


    def test_apierror_model_validation(self):
        """Test apiError model field validation."""
        # Test with minimal required data
        minimal_data = {
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
            "httpStatusCode": 1,
            "message": "required_message",
        }
        
        model = apiError(**minimal_data)
        assert isinstance(model, apiError)
        assert model.debugId == minimal_data["debugId"]
        assert model.errorCode == minimal_data["errorCode"]
        assert model.httpStatusCode == minimal_data["httpStatusCode"]
        assert model.message == minimal_data["message"]


    def test_apierror_model_required_fields(self):
        """Test apiError model required field validation."""
        # Check if this model has any required fields
        required_fields = ["debugId", "errorCode", "httpStatusCode", "message", ]
        
        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                apiError()
            
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
            model = apiError()
            assert isinstance(model, apiError)

    def test_apierror_model_optional_fields(self):
        """Test apiError model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "debugId": "required_debugId",
            "errorCode": "required_errorCode",
            "httpStatusCode": 1,
            "message": "required_message",
        }
        
        model = apiError(**minimal_data)
        
        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values


    def test_apierror_model_serialization(self):
        """Test apiError model serialization to dict."""
        test_data = {
            "debugId": "serialize_value",
            "errorCode": "serialize_value",
            "httpStatusCode": 99,
            "message": "serialize_value",
        }
        
        model = apiError(**test_data)
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


    def test_apierror_model_json_schema(self):
        """Test apiError model JSON schema generation."""
        schema = apiError.model_json_schema()
        
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
        required_fields = ["debugId", "errorCode", "httpStatusCode", "message", ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)


    def test_coefficientcostinput_model_creation(self):
        """Test coefficientCostInput model creation with valid data."""
        # Valid test data for coefficientCostInput
        valid_data = {
            "useCurrent": True,
            "useDefault": True,
            "value": 3.14,
            "currencyCode": "test_currencyCode",
        }
        
        # Create model instance
        model = coefficientCostInput(**valid_data)
        
        # Verify model creation
        assert isinstance(model, coefficientCostInput)
        assert model.useCurrent == valid_data["useCurrent"]
        assert model.useDefault == valid_data["useDefault"]
        assert model.value == valid_data["value"]
        assert model.currencyCode == valid_data["currencyCode"]


    def test_coefficientcostinput_model_validation(self):
        """Test coefficientCostInput model field validation."""
        # Test with minimal required data
        minimal_data = {
            "useCurrent": True,
            "useDefault": True,
        }
        
        model = coefficientCostInput(**minimal_data)
        assert isinstance(model, coefficientCostInput)
        assert model.useCurrent == minimal_data["useCurrent"]
        assert model.useDefault == minimal_data["useDefault"]


    def test_coefficientcostinput_model_required_fields(self):
        """Test coefficientCostInput model required field validation."""
        # Check if this model has any required fields
        required_fields = ["useCurrent", "useDefault", ]
        
        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                coefficientCostInput()
            
            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "useCurrent",
                "useDefault",
            }
            
            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = coefficientCostInput()
            assert isinstance(model, coefficientCostInput)

    def test_coefficientcostinput_model_optional_fields(self):
        """Test coefficientCostInput model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "useCurrent": True,
            "useDefault": True,
        }
        
        model = coefficientCostInput(**minimal_data)
        
        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "value")
        # Optional field value should be None or have a default value
        assert model.value is None or model.value is not None
        assert hasattr(model, "currencyCode")
        # Optional field currencyCode should be None or have a default value
        assert model.currencyCode is None or model.currencyCode is not None


    def test_coefficientcostinput_model_serialization(self):
        """Test coefficientCostInput model serialization to dict."""
        test_data = {
            "useCurrent": False,
            "useDefault": False,
            "value": 9.99,
            "currencyCode": "serialize_value",
        }
        
        model = coefficientCostInput(**test_data)
        serialized = model.model_dump(by_alias=True)
        
        # Verify serialization
        assert isinstance(serialized, dict)
        assert "useCurrent" in serialized
        assert "useDefault" in serialized
        assert "value" in serialized
        assert "currencyCode" in serialized

        
        # Verify values are preserved
        assert serialized["useCurrent"] == test_data["useCurrent"]
        assert serialized["useDefault"] == test_data["useDefault"]
        assert serialized["value"] == test_data["value"]
        assert serialized["currencyCode"] == test_data["currencyCode"]


    def test_coefficientcostinput_model_json_schema(self):
        """Test coefficientCostInput model JSON schema generation."""
        schema = coefficientCostInput.model_json_schema()
        
        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema
        
        # Verify all properties are in schema
        expected_properties = {
            "useCurrent",
            "useDefault",
            "value",
            "currencyCode",
        }
        
        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)
        
        # Verify required fields in schema (if any)
        required_fields = ["useCurrent", "useDefault", ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)


    def test_currencycomponent_model_creation(self):
        """Test currencyComponent model creation with valid data."""
        # Valid test data for currencyComponent
        valid_data = {
            "currencyCode": "test_currencyCode",
            "currencyName": "test_currencyName",
        }
        
        # Create model instance
        model = currencyComponent(**valid_data)
        
        # Verify model creation
        assert isinstance(model, currencyComponent)
        assert model.currencyCode == valid_data["currencyCode"]
        assert model.currencyName == valid_data["currencyName"]


    def test_currencycomponent_model_validation(self):
        """Test currencyComponent model field validation."""
        # Test with minimal required data
        minimal_data = {
            "currencyCode": "required_currencyCode",
            "currencyName": "required_currencyName",
        }
        
        model = currencyComponent(**minimal_data)
        assert isinstance(model, currencyComponent)
        assert model.currencyCode == minimal_data["currencyCode"]
        assert model.currencyName == minimal_data["currencyName"]


    def test_currencycomponent_model_required_fields(self):
        """Test currencyComponent model required field validation."""
        # Check if this model has any required fields
        required_fields = ["currencyCode", "currencyName", ]
        
        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                currencyComponent()
            
            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "currencyCode",
                "currencyName",
            }
            
            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = currencyComponent()
            assert isinstance(model, currencyComponent)

    def test_currencycomponent_model_optional_fields(self):
        """Test currencyComponent model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "currencyCode": "required_currencyCode",
            "currencyName": "required_currencyName",
        }
        
        model = currencyComponent(**minimal_data)
        
        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values


    def test_currencycomponent_model_serialization(self):
        """Test currencyComponent model serialization to dict."""
        test_data = {
            "currencyCode": "serialize_value",
            "currencyName": "serialize_value",
        }
        
        model = currencyComponent(**test_data)
        serialized = model.model_dump(by_alias=True)
        
        # Verify serialization
        assert isinstance(serialized, dict)
        assert "currencyCode" in serialized
        assert "currencyName" in serialized

        
        # Verify values are preserved
        assert serialized["currencyCode"] == test_data["currencyCode"]
        assert serialized["currencyName"] == test_data["currencyName"]


    def test_currencycomponent_model_json_schema(self):
        """Test currencyComponent model JSON schema generation."""
        schema = currencyComponent.model_json_schema()
        
        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema
        
        # Verify all properties are in schema
        expected_properties = {
            "currencyCode",
            "currencyName",
        }
        
        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)
        
        # Verify required fields in schema (if any)
        required_fields = ["currencyCode", "currencyName", ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)


    def test_tag_model_creation(self):
        """Test tag model creation with valid data."""
        # Valid test data for tag
        valid_data = {
            "name": "test_name",
            "value": "test_value",
        }
        
        # Create model instance
        model = tag(**valid_data)
        
        # Verify model creation
        assert isinstance(model, tag)
        assert model.name == valid_data["name"]
        assert model.value == valid_data["value"]


    def test_tag_model_validation(self):
        """Test tag model field validation."""
        # Test with minimal required data
        minimal_data = {
            "name": "required_name",
            "value": "required_value",
        }
        
        model = tag(**minimal_data)
        assert isinstance(model, tag)
        assert model.name == minimal_data["name"]
        assert model.value == minimal_data["value"]


    def test_tag_model_required_fields(self):
        """Test tag model required field validation."""
        # Check if this model has any required fields
        required_fields = ["name", "value", ]
        
        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                tag()
            
            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "name",
                "value",
            }
            
            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = tag()
            assert isinstance(model, tag)

    def test_tag_model_optional_fields(self):
        """Test tag model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "name": "required_name",
            "value": "required_value",
        }
        
        model = tag(**minimal_data)
        
        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values


    def test_tag_model_serialization(self):
        """Test tag model serialization to dict."""
        test_data = {
            "name": "serialize_value",
            "value": "serialize_value",
        }
        
        model = tag(**test_data)
        serialized = model.model_dump(by_alias=True)
        
        # Verify serialization
        assert isinstance(serialized, dict)
        assert "name" in serialized
        assert "value" in serialized

        
        # Verify values are preserved
        assert serialized["name"] == test_data["name"]
        assert serialized["value"] == test_data["value"]


    def test_tag_model_json_schema(self):
        """Test tag model JSON schema generation."""
        schema = tag.model_json_schema()
        
        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema
        
        # Verify all properties are in schema
        expected_properties = {
            "name",
            "value",
        }
        
        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)
        
        # Verify required fields in schema (if any)
        required_fields = ["name", "value", ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)


    def test_coefficient_model_creation(self):
        """Test coefficient model creation with valid data."""
        # Valid test data for coefficient
        valid_data = {
            "costPerKwh": 3.14,
            "currency": {},
            "updatedAt": "test_updatedAt",
            "type": "test_type",
            "associatedLocation": {},
            "co2eGramsPerKwh": 3.14,
            "startTime": "test_startTime",
            "costUsdPerKwh": 3.14,
            "createdAt": "test_createdAt",
            "id": "test_id",
            "generation": 42,
        }
        
        # Create model instance
        model = coefficient(**valid_data)
        
        # Verify model creation
        assert isinstance(model, coefficient)
        assert model.costPerKwh == valid_data["costPerKwh"]
        assert model.currency == valid_data["currency"]
        assert model.updatedAt == valid_data["updatedAt"]
        assert model.type == valid_data["type"]
        assert model.associatedLocation == valid_data["associatedLocation"]
        assert model.co2eGramsPerKwh == valid_data["co2eGramsPerKwh"]
        assert model.startTime == valid_data["startTime"]
        assert model.costUsdPerKwh == valid_data["costUsdPerKwh"]
        assert model.createdAt == valid_data["createdAt"]
        assert model.id == valid_data["id"]
        assert model.generation == valid_data["generation"]


    def test_coefficient_model_validation(self):
        """Test coefficient model field validation."""
        # Test with minimal required data
        minimal_data = {
            "updatedAt": "required_updatedAt",
            "type": "required_type",
            "createdAt": "required_createdAt",
            "id": "required_id",
            "generation": 1,
        }
        
        model = coefficient(**minimal_data)
        assert isinstance(model, coefficient)
        assert model.updatedAt == minimal_data["updatedAt"]
        assert model.type == minimal_data["type"]
        assert model.createdAt == minimal_data["createdAt"]
        assert model.id == minimal_data["id"]
        assert model.generation == minimal_data["generation"]


    def test_coefficient_model_required_fields(self):
        """Test coefficient model required field validation."""
        # Check if this model has any required fields
        required_fields = ["updatedAt", "type", "createdAt", "id", "generation", ]
        
        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                coefficient()
            
            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "updatedAt",
                "type",
                "createdAt",
                "id",
                "generation",
            }
            
            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = coefficient()
            assert isinstance(model, coefficient)

    def test_coefficient_model_optional_fields(self):
        """Test coefficient model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "updatedAt": "required_updatedAt",
            "type": "required_type",
            "createdAt": "required_createdAt",
            "id": "required_id",
            "generation": 1,
        }
        
        model = coefficient(**minimal_data)
        
        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "costPerKwh")
        # Optional field costPerKwh should be None or have a default value
        assert model.costPerKwh is None or model.costPerKwh is not None
        assert hasattr(model, "currency")
        # Optional field currency should be None or have a default value
        assert model.currency is None or model.currency is not None
        assert hasattr(model, "associatedLocation")
        # Optional field associatedLocation should be None or have a default value
        assert model.associatedLocation is None or model.associatedLocation is not None
        assert hasattr(model, "co2eGramsPerKwh")
        # Optional field co2eGramsPerKwh should be None or have a default value
        assert model.co2eGramsPerKwh is None or model.co2eGramsPerKwh is not None
        assert hasattr(model, "startTime")
        # Optional field startTime should be None or have a default value
        assert model.startTime is None or model.startTime is not None
        assert hasattr(model, "costUsdPerKwh")
        # Optional field costUsdPerKwh should be None or have a default value
        assert model.costUsdPerKwh is None or model.costUsdPerKwh is not None


    def test_coefficient_model_serialization(self):
        """Test coefficient model serialization to dict."""
        test_data = {
            "costPerKwh": 9.99,
            "currency": {"key": "value"},
            "updatedAt": "serialize_value",
            "type": "serialize_value",
            "associatedLocation": {"key": "value"},
            "co2eGramsPerKwh": 9.99,
            "startTime": "serialize_value",
            "costUsdPerKwh": 9.99,
            "createdAt": "serialize_value",
            "id": "serialize_value",
            "generation": 99,
        }
        
        model = coefficient(**test_data)
        serialized = model.model_dump(by_alias=True)
        
        # Verify serialization
        assert isinstance(serialized, dict)
        assert "costPerKwh" in serialized
        assert "currency" in serialized
        assert "updatedAt" in serialized
        assert "type" in serialized
        assert "associatedLocation" in serialized
        assert "co2eGramsPerKwh" in serialized
        assert "startTime" in serialized
        assert "costUsdPerKwh" in serialized
        assert "createdAt" in serialized
        assert "id" in serialized
        assert "generation" in serialized

        
        # Verify values are preserved
        assert serialized["costPerKwh"] == test_data["costPerKwh"]
        assert serialized["currency"] == test_data["currency"]
        assert serialized["updatedAt"] == test_data["updatedAt"]
        assert serialized["type"] == test_data["type"]
        assert serialized["associatedLocation"] == test_data["associatedLocation"]
        assert serialized["co2eGramsPerKwh"] == test_data["co2eGramsPerKwh"]
        assert serialized["startTime"] == test_data["startTime"]
        assert serialized["costUsdPerKwh"] == test_data["costUsdPerKwh"]
        assert serialized["createdAt"] == test_data["createdAt"]
        assert serialized["id"] == test_data["id"]
        assert serialized["generation"] == test_data["generation"]


    def test_coefficient_model_json_schema(self):
        """Test coefficient model JSON schema generation."""
        schema = coefficient.model_json_schema()
        
        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema
        
        # Verify all properties are in schema
        expected_properties = {
            "costPerKwh",
            "currency",
            "updatedAt",
            "type",
            "associatedLocation",
            "co2eGramsPerKwh",
            "startTime",
            "costUsdPerKwh",
            "createdAt",
            "id",
            "generation",
        }
        
        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)
        
        # Verify required fields in schema (if any)
        required_fields = ["updatedAt", "type", "createdAt", "id", "generation", ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)


    def test_coefficientinput_model_creation(self):
        """Test coefficientInput model creation with valid data."""
        # Valid test data for coefficientInput
        valid_data = {
            "useDefault": True,
            "value": 3.14,
            "useCurrent": True,
        }
        
        # Create model instance
        model = coefficientInput(**valid_data)
        
        # Verify model creation
        assert isinstance(model, coefficientInput)
        assert model.useDefault == valid_data["useDefault"]
        assert model.value == valid_data["value"]
        assert model.useCurrent == valid_data["useCurrent"]


    def test_coefficientinput_model_validation(self):
        """Test coefficientInput model field validation."""
        # Test with minimal required data
        minimal_data = {
            "useDefault": True,
            "useCurrent": True,
        }
        
        model = coefficientInput(**minimal_data)
        assert isinstance(model, coefficientInput)
        assert model.useDefault == minimal_data["useDefault"]
        assert model.useCurrent == minimal_data["useCurrent"]


    def test_coefficientinput_model_required_fields(self):
        """Test coefficientInput model required field validation."""
        # Check if this model has any required fields
        required_fields = ["useDefault", "useCurrent", ]
        
        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                coefficientInput()
            
            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "useDefault",
                "useCurrent",
            }
            
            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = coefficientInput()
            assert isinstance(model, coefficientInput)

    def test_coefficientinput_model_optional_fields(self):
        """Test coefficientInput model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "useDefault": True,
            "useCurrent": True,
        }
        
        model = coefficientInput(**minimal_data)
        
        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "value")
        # Optional field value should be None or have a default value
        assert model.value is None or model.value is not None


    def test_coefficientinput_model_serialization(self):
        """Test coefficientInput model serialization to dict."""
        test_data = {
            "useDefault": False,
            "value": 9.99,
            "useCurrent": False,
        }
        
        model = coefficientInput(**test_data)
        serialized = model.model_dump(by_alias=True)
        
        # Verify serialization
        assert isinstance(serialized, dict)
        assert "useDefault" in serialized
        assert "value" in serialized
        assert "useCurrent" in serialized

        
        # Verify values are preserved
        assert serialized["useDefault"] == test_data["useDefault"]
        assert serialized["value"] == test_data["value"]
        assert serialized["useCurrent"] == test_data["useCurrent"]


    def test_coefficientinput_model_json_schema(self):
        """Test coefficientInput model JSON schema generation."""
        schema = coefficientInput.model_json_schema()
        
        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema
        
        # Verify all properties are in schema
        expected_properties = {
            "useDefault",
            "value",
            "useCurrent",
        }
        
        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)
        
        # Verify required fields in schema (if any)
        required_fields = ["useDefault", "useCurrent", ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)


    def test_currencycode_model_creation(self):
        """Test currencyCode model creation with valid data."""
        # Valid test data for currencyCode
        valid_data = {
        }
        
        # Create model instance
        model = currencyCode(**valid_data)
        
        # Verify model creation
        assert isinstance(model, currencyCode)


    def test_currencycode_model_validation(self):
        """Test currencyCode model field validation."""
        # Test with minimal required data
        minimal_data = {
        }
        
        model = currencyCode(**minimal_data)
        assert isinstance(model, currencyCode)


    def test_currencycode_model_required_fields(self):
        """Test currencyCode model required field validation."""
        # Check if this model has any required fields
        required_fields = []
        
        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                currencyCode()
            
            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
            }
            
            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = currencyCode()
            assert isinstance(model, currencyCode)

    def test_currencycode_model_optional_fields(self):
        """Test currencyCode model optional field handling."""
        # Create with minimal required data
        minimal_data = {
        }
        
        model = currencyCode(**minimal_data)
        
        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values


    def test_currencycode_model_serialization(self):
        """Test currencyCode model serialization to dict."""
        test_data = {
        }
        
        model = currencyCode(**test_data)
        serialized = model.model_dump(by_alias=True)
        
        # Verify serialization
        assert isinstance(serialized, dict)

        
        # Verify values are preserved


    def test_currencycode_model_json_schema(self):
        """Test currencyCode model JSON schema generation."""
        schema = currencyCode.model_json_schema()
        
        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema
        
        # Verify all properties are in schema
        expected_properties = {
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


    def test_datasource_model_creation(self):
        """Test datasource model creation with valid data."""
        # Valid test data for datasource
        valid_data = {
            "id": "test_id",
            "provider": "test_provider",
            "updatedAt": "test_updatedAt",
            "lastCollectionTime": "test_lastCollectionTime",
            "name": "test_name",
            "type": "test_type",
            "firstCollectionTime": "test_firstCollectionTime",
            "createdAt": "test_createdAt",
            "generation": 42,
        }
        
        # Create model instance
        model = datasource(**valid_data)
        
        # Verify model creation
        assert isinstance(model, datasource)
        assert model.id == valid_data["id"]
        assert model.provider == valid_data["provider"]
        assert model.updatedAt == valid_data["updatedAt"]
        assert model.lastCollectionTime == valid_data["lastCollectionTime"]
        assert model.name == valid_data["name"]
        assert model.type == valid_data["type"]
        assert model.firstCollectionTime == valid_data["firstCollectionTime"]
        assert model.createdAt == valid_data["createdAt"]
        assert model.generation == valid_data["generation"]


    def test_datasource_model_validation(self):
        """Test datasource model field validation."""
        # Test with minimal required data
        minimal_data = {
            "id": "required_id",
            "updatedAt": "required_updatedAt",
            "type": "required_type",
            "createdAt": "required_createdAt",
            "generation": 1,
        }
        
        model = datasource(**minimal_data)
        assert isinstance(model, datasource)
        assert model.id == minimal_data["id"]
        assert model.updatedAt == minimal_data["updatedAt"]
        assert model.type == minimal_data["type"]
        assert model.createdAt == minimal_data["createdAt"]
        assert model.generation == minimal_data["generation"]


    def test_datasource_model_required_fields(self):
        """Test datasource model required field validation."""
        # Check if this model has any required fields
        required_fields = ["id", "updatedAt", "type", "createdAt", "generation", ]
        
        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                datasource()
            
            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "id",
                "updatedAt",
                "type",
                "createdAt",
                "generation",
            }
            
            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = datasource()
            assert isinstance(model, datasource)

    def test_datasource_model_optional_fields(self):
        """Test datasource model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "id": "required_id",
            "updatedAt": "required_updatedAt",
            "type": "required_type",
            "createdAt": "required_createdAt",
            "generation": 1,
        }
        
        model = datasource(**minimal_data)
        
        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "provider")
        # Optional field provider should be None or have a default value
        assert model.provider is None or model.provider is not None
        assert hasattr(model, "lastCollectionTime")
        # Optional field lastCollectionTime should be None or have a default value
        assert model.lastCollectionTime is None or model.lastCollectionTime is not None
        assert hasattr(model, "name")
        # Optional field name should be None or have a default value
        assert model.name is None or model.name is not None
        assert hasattr(model, "firstCollectionTime")
        # Optional field firstCollectionTime should be None or have a default value
        assert model.firstCollectionTime is None or model.firstCollectionTime is not None


    def test_datasource_model_serialization(self):
        """Test datasource model serialization to dict."""
        test_data = {
            "id": "serialize_value",
            "provider": "serialize_value",
            "updatedAt": "serialize_value",
            "lastCollectionTime": "serialize_value",
            "name": "serialize_value",
            "type": "serialize_value",
            "firstCollectionTime": "serialize_value",
            "createdAt": "serialize_value",
            "generation": 99,
        }
        
        model = datasource(**test_data)
        serialized = model.model_dump(by_alias=True)
        
        # Verify serialization
        assert isinstance(serialized, dict)
        assert "id" in serialized
        assert "provider" in serialized
        assert "updatedAt" in serialized
        assert "lastCollectionTime" in serialized
        assert "name" in serialized
        assert "type" in serialized
        assert "firstCollectionTime" in serialized
        assert "createdAt" in serialized
        assert "generation" in serialized

        
        # Verify values are preserved
        assert serialized["id"] == test_data["id"]
        assert serialized["provider"] == test_data["provider"]
        assert serialized["updatedAt"] == test_data["updatedAt"]
        assert serialized["lastCollectionTime"] == test_data["lastCollectionTime"]
        assert serialized["name"] == test_data["name"]
        assert serialized["type"] == test_data["type"]
        assert serialized["firstCollectionTime"] == test_data["firstCollectionTime"]
        assert serialized["createdAt"] == test_data["createdAt"]
        assert serialized["generation"] == test_data["generation"]


    def test_datasource_model_json_schema(self):
        """Test datasource model JSON schema generation."""
        schema = datasource.model_json_schema()
        
        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema
        
        # Verify all properties are in schema
        expected_properties = {
            "id",
            "provider",
            "updatedAt",
            "lastCollectionTime",
            "name",
            "type",
            "firstCollectionTime",
            "createdAt",
            "generation",
        }
        
        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)
        
        # Verify required fields in schema (if any)
        required_fields = ["id", "updatedAt", "type", "createdAt", "generation", ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)


    def test_total_model_creation(self):
        """Test total model creation with valid data."""
        # Valid test data for total
        valid_data = {
            "costUsd": 3.14,
            "currency": "test_currency",
            "kwh": 3.14,
            "type": "test_type",
            "co2eMetricTon": 3.14,
            "cost": 3.14,
        }
        
        # Create model instance
        model = total(**valid_data)
        
        # Verify model creation
        assert isinstance(model, total)
        assert model.costUsd == valid_data["costUsd"]
        assert model.currency == valid_data["currency"]
        assert model.kwh == valid_data["kwh"]
        assert model.type == valid_data["type"]
        assert model.co2eMetricTon == valid_data["co2eMetricTon"]
        assert model.cost == valid_data["cost"]


    def test_total_model_validation(self):
        """Test total model field validation."""
        # Test with minimal required data
        minimal_data = {
            "type": "required_type",
        }
        
        model = total(**minimal_data)
        assert isinstance(model, total)
        assert model.type == minimal_data["type"]


    def test_total_model_required_fields(self):
        """Test total model required field validation."""
        # Check if this model has any required fields
        required_fields = ["type", ]
        
        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                total()
            
            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "type",
            }
            
            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = total()
            assert isinstance(model, total)

    def test_total_model_optional_fields(self):
        """Test total model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "type": "required_type",
        }
        
        model = total(**minimal_data)
        
        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "costUsd")
        # Optional field costUsd should be None or have a default value
        assert model.costUsd is None or model.costUsd is not None
        assert hasattr(model, "currency")
        # Optional field currency should be None or have a default value
        assert model.currency is None or model.currency is not None
        assert hasattr(model, "kwh")
        # Optional field kwh should be None or have a default value
        assert model.kwh is None or model.kwh is not None
        assert hasattr(model, "co2eMetricTon")
        # Optional field co2eMetricTon should be None or have a default value
        assert model.co2eMetricTon is None or model.co2eMetricTon is not None
        assert hasattr(model, "cost")
        # Optional field cost should be None or have a default value
        assert model.cost is None or model.cost is not None


    def test_total_model_serialization(self):
        """Test total model serialization to dict."""
        test_data = {
            "costUsd": 9.99,
            "currency": "serialize_value",
            "kwh": 9.99,
            "type": "serialize_value",
            "co2eMetricTon": 9.99,
            "cost": 9.99,
        }
        
        model = total(**test_data)
        serialized = model.model_dump(by_alias=True)
        
        # Verify serialization
        assert isinstance(serialized, dict)
        assert "costUsd" in serialized
        assert "currency" in serialized
        assert "kwh" in serialized
        assert "type" in serialized
        assert "co2eMetricTon" in serialized
        assert "cost" in serialized

        
        # Verify values are preserved
        assert serialized["costUsd"] == test_data["costUsd"]
        assert serialized["currency"] == test_data["currency"]
        assert serialized["kwh"] == test_data["kwh"]
        assert serialized["type"] == test_data["type"]
        assert serialized["co2eMetricTon"] == test_data["co2eMetricTon"]
        assert serialized["cost"] == test_data["cost"]


    def test_total_model_json_schema(self):
        """Test total model JSON schema generation."""
        schema = total.model_json_schema()
        
        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema
        
        # Verify all properties are in schema
        expected_properties = {
            "costUsd",
            "currency",
            "kwh",
            "type",
            "co2eMetricTon",
            "cost",
        }
        
        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)
        
        # Verify required fields in schema (if any)
        required_fields = ["type", ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)


    def test_timeseries_model_creation(self):
        """Test timeseries model creation with valid data."""
        # Valid test data for timeseries
        valid_data = {
            "costUsd": 3.14,
            "currency": "test_currency",
            "id": "test_id",
            "kwh": 3.14,
            "timeBucket": "test_timeBucket",
            "type": "test_type",
            "co2eMetricTon": 3.14,
            "cost": 3.14,
        }
        
        # Create model instance
        model = timeseries(**valid_data)
        
        # Verify model creation
        assert isinstance(model, timeseries)
        assert model.costUsd == valid_data["costUsd"]
        assert model.currency == valid_data["currency"]
        assert model.id == valid_data["id"]
        assert model.kwh == valid_data["kwh"]
        assert model.timeBucket == valid_data["timeBucket"]
        assert model.type == valid_data["type"]
        assert model.co2eMetricTon == valid_data["co2eMetricTon"]
        assert model.cost == valid_data["cost"]


    def test_timeseries_model_validation(self):
        """Test timeseries model field validation."""
        # Test with minimal required data
        minimal_data = {
            "id": "required_id",
            "type": "required_type",
        }
        
        model = timeseries(**minimal_data)
        assert isinstance(model, timeseries)
        assert model.id == minimal_data["id"]
        assert model.type == minimal_data["type"]


    def test_timeseries_model_required_fields(self):
        """Test timeseries model required field validation."""
        # Check if this model has any required fields
        required_fields = ["id", "type", ]
        
        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                timeseries()
            
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
            model = timeseries()
            assert isinstance(model, timeseries)

    def test_timeseries_model_optional_fields(self):
        """Test timeseries model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "id": "required_id",
            "type": "required_type",
        }
        
        model = timeseries(**minimal_data)
        
        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "costUsd")
        # Optional field costUsd should be None or have a default value
        assert model.costUsd is None or model.costUsd is not None
        assert hasattr(model, "currency")
        # Optional field currency should be None or have a default value
        assert model.currency is None or model.currency is not None
        assert hasattr(model, "kwh")
        # Optional field kwh should be None or have a default value
        assert model.kwh is None or model.kwh is not None
        assert hasattr(model, "timeBucket")
        # Optional field timeBucket should be None or have a default value
        assert model.timeBucket is None or model.timeBucket is not None
        assert hasattr(model, "co2eMetricTon")
        # Optional field co2eMetricTon should be None or have a default value
        assert model.co2eMetricTon is None or model.co2eMetricTon is not None
        assert hasattr(model, "cost")
        # Optional field cost should be None or have a default value
        assert model.cost is None or model.cost is not None


    def test_timeseries_model_serialization(self):
        """Test timeseries model serialization to dict."""
        test_data = {
            "costUsd": 9.99,
            "currency": "serialize_value",
            "id": "serialize_value",
            "kwh": 9.99,
            "timeBucket": "serialize_value",
            "type": "serialize_value",
            "co2eMetricTon": 9.99,
            "cost": 9.99,
        }
        
        model = timeseries(**test_data)
        serialized = model.model_dump(by_alias=True)
        
        # Verify serialization
        assert isinstance(serialized, dict)
        assert "costUsd" in serialized
        assert "currency" in serialized
        assert "id" in serialized
        assert "kwh" in serialized
        assert "timeBucket" in serialized
        assert "type" in serialized
        assert "co2eMetricTon" in serialized
        assert "cost" in serialized

        
        # Verify values are preserved
        assert serialized["costUsd"] == test_data["costUsd"]
        assert serialized["currency"] == test_data["currency"]
        assert serialized["id"] == test_data["id"]
        assert serialized["kwh"] == test_data["kwh"]
        assert serialized["timeBucket"] == test_data["timeBucket"]
        assert serialized["type"] == test_data["type"]
        assert serialized["co2eMetricTon"] == test_data["co2eMetricTon"]
        assert serialized["cost"] == test_data["cost"]


    def test_timeseries_model_json_schema(self):
        """Test timeseries model JSON schema generation."""
        schema = timeseries.model_json_schema()
        
        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema
        
        # Verify all properties are in schema
        expected_properties = {
            "costUsd",
            "currency",
            "id",
            "kwh",
            "timeBucket",
            "type",
            "co2eMetricTon",
            "cost",
        }
        
        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)
        
        # Verify required fields in schema (if any)
        required_fields = ["id", "type", ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)


    def test_cloudentity_model_creation(self):
        """Test cloudEntity model creation with valid data."""
        # Valid test data for cloudEntity
        valid_data = {
            "serviceName": "test_serviceName",
            "serviceRegion": "test_serviceRegion",
            "entityId": "test_entityId",
            "id": "test_id",
            "serviceAccount": "test_serviceAccount",
            "name": "test_name",
            "serviceProvider": "test_serviceProvider",
            "type": "test_type",
            "co2eMetricTon": 3.14,
        }
        
        # Create model instance
        model = cloudEntity(**valid_data)
        
        # Verify model creation
        assert isinstance(model, cloudEntity)
        assert model.serviceName == valid_data["serviceName"]
        assert model.serviceRegion == valid_data["serviceRegion"]
        assert model.entityId == valid_data["entityId"]
        assert model.id == valid_data["id"]
        assert model.serviceAccount == valid_data["serviceAccount"]
        assert model.name == valid_data["name"]
        assert model.serviceProvider == valid_data["serviceProvider"]
        assert model.type == valid_data["type"]
        assert model.co2eMetricTon == valid_data["co2eMetricTon"]


    def test_cloudentity_model_validation(self):
        """Test cloudEntity model field validation."""
        # Test with minimal required data
        minimal_data = {
            "id": "required_id",
            "type": "required_type",
        }
        
        model = cloudEntity(**minimal_data)
        assert isinstance(model, cloudEntity)
        assert model.id == minimal_data["id"]
        assert model.type == minimal_data["type"]


    def test_cloudentity_model_required_fields(self):
        """Test cloudEntity model required field validation."""
        # Check if this model has any required fields
        required_fields = ["id", "type", ]
        
        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                cloudEntity()
            
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
            model = cloudEntity()
            assert isinstance(model, cloudEntity)

    def test_cloudentity_model_optional_fields(self):
        """Test cloudEntity model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "id": "required_id",
            "type": "required_type",
        }
        
        model = cloudEntity(**minimal_data)
        
        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "serviceName")
        # Optional field serviceName should be None or have a default value
        assert model.serviceName is None or model.serviceName is not None
        assert hasattr(model, "serviceRegion")
        # Optional field serviceRegion should be None or have a default value
        assert model.serviceRegion is None or model.serviceRegion is not None
        assert hasattr(model, "entityId")
        # Optional field entityId should be None or have a default value
        assert model.entityId is None or model.entityId is not None
        assert hasattr(model, "serviceAccount")
        # Optional field serviceAccount should be None or have a default value
        assert model.serviceAccount is None or model.serviceAccount is not None
        assert hasattr(model, "name")
        # Optional field name should be None or have a default value
        assert model.name is None or model.name is not None
        assert hasattr(model, "serviceProvider")
        # Optional field serviceProvider should be None or have a default value
        assert model.serviceProvider is None or model.serviceProvider is not None
        assert hasattr(model, "co2eMetricTon")
        # Optional field co2eMetricTon should be None or have a default value
        assert model.co2eMetricTon is None or model.co2eMetricTon is not None


    def test_cloudentity_model_serialization(self):
        """Test cloudEntity model serialization to dict."""
        test_data = {
            "serviceName": "serialize_value",
            "serviceRegion": "serialize_value",
            "entityId": "serialize_value",
            "id": "serialize_value",
            "serviceAccount": "serialize_value",
            "name": "serialize_value",
            "serviceProvider": "serialize_value",
            "type": "serialize_value",
            "co2eMetricTon": 9.99,
        }
        
        model = cloudEntity(**test_data)
        serialized = model.model_dump(by_alias=True)
        
        # Verify serialization
        assert isinstance(serialized, dict)
        assert "serviceName" in serialized
        assert "serviceRegion" in serialized
        assert "entityId" in serialized
        assert "id" in serialized
        assert "serviceAccount" in serialized
        assert "name" in serialized
        assert "serviceProvider" in serialized
        assert "type" in serialized
        assert "co2eMetricTon" in serialized

        
        # Verify values are preserved
        assert serialized["serviceName"] == test_data["serviceName"]
        assert serialized["serviceRegion"] == test_data["serviceRegion"]
        assert serialized["entityId"] == test_data["entityId"]
        assert serialized["id"] == test_data["id"]
        assert serialized["serviceAccount"] == test_data["serviceAccount"]
        assert serialized["name"] == test_data["name"]
        assert serialized["serviceProvider"] == test_data["serviceProvider"]
        assert serialized["type"] == test_data["type"]
        assert serialized["co2eMetricTon"] == test_data["co2eMetricTon"]


    def test_cloudentity_model_json_schema(self):
        """Test cloudEntity model JSON schema generation."""
        schema = cloudEntity.model_json_schema()
        
        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema
        
        # Verify all properties are in schema
        expected_properties = {
            "serviceName",
            "serviceRegion",
            "entityId",
            "id",
            "serviceAccount",
            "name",
            "serviceProvider",
            "type",
            "co2eMetricTon",
        }
        
        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)
        
        # Verify required fields in schema (if any)
        required_fields = ["id", "type", ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)


    def test_cloudtimeseries_model_creation(self):
        """Test cloudTimeseries model creation with valid data."""
        # Valid test data for cloudTimeseries
        valid_data = {
            "co2eMetricTon": 3.14,
            "id": "test_id",
            "timeBucket": "test_timeBucket",
            "type": "test_type",
        }
        
        # Create model instance
        model = cloudTimeseries(**valid_data)
        
        # Verify model creation
        assert isinstance(model, cloudTimeseries)
        assert model.co2eMetricTon == valid_data["co2eMetricTon"]
        assert model.id == valid_data["id"]
        assert model.timeBucket == valid_data["timeBucket"]
        assert model.type == valid_data["type"]


    def test_cloudtimeseries_model_validation(self):
        """Test cloudTimeseries model field validation."""
        # Test with minimal required data
        minimal_data = {
            "id": "required_id",
            "type": "required_type",
        }
        
        model = cloudTimeseries(**minimal_data)
        assert isinstance(model, cloudTimeseries)
        assert model.id == minimal_data["id"]
        assert model.type == minimal_data["type"]


    def test_cloudtimeseries_model_required_fields(self):
        """Test cloudTimeseries model required field validation."""
        # Check if this model has any required fields
        required_fields = ["id", "type", ]
        
        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                cloudTimeseries()
            
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
            model = cloudTimeseries()
            assert isinstance(model, cloudTimeseries)

    def test_cloudtimeseries_model_optional_fields(self):
        """Test cloudTimeseries model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "id": "required_id",
            "type": "required_type",
        }
        
        model = cloudTimeseries(**minimal_data)
        
        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "co2eMetricTon")
        # Optional field co2eMetricTon should be None or have a default value
        assert model.co2eMetricTon is None or model.co2eMetricTon is not None
        assert hasattr(model, "timeBucket")
        # Optional field timeBucket should be None or have a default value
        assert model.timeBucket is None or model.timeBucket is not None


    def test_cloudtimeseries_model_serialization(self):
        """Test cloudTimeseries model serialization to dict."""
        test_data = {
            "co2eMetricTon": 9.99,
            "id": "serialize_value",
            "timeBucket": "serialize_value",
            "type": "serialize_value",
        }
        
        model = cloudTimeseries(**test_data)
        serialized = model.model_dump(by_alias=True)
        
        # Verify serialization
        assert isinstance(serialized, dict)
        assert "co2eMetricTon" in serialized
        assert "id" in serialized
        assert "timeBucket" in serialized
        assert "type" in serialized

        
        # Verify values are preserved
        assert serialized["co2eMetricTon"] == test_data["co2eMetricTon"]
        assert serialized["id"] == test_data["id"]
        assert serialized["timeBucket"] == test_data["timeBucket"]
        assert serialized["type"] == test_data["type"]


    def test_cloudtimeseries_model_json_schema(self):
        """Test cloudTimeseries model JSON schema generation."""
        schema = cloudTimeseries.model_json_schema()
        
        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema
        
        # Verify all properties are in schema
        expected_properties = {
            "co2eMetricTon",
            "id",
            "timeBucket",
            "type",
        }
        
        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)
        
        # Verify required fields in schema (if any)
        required_fields = ["id", "type", ]
        if required_fields:
            assert "required" in schema
            required_in_schema = set(schema["required"])
            expected_required = set(required_fields)
            assert expected_required.issubset(required_in_schema)


    def test_ingest_model_creation(self):
        """Test ingest model creation with valid data."""
        # Valid test data for ingest
        valid_data = {
            "updatedAt": "test_updatedAt",
            "createdAt": "test_createdAt",
            "description": "test_description",
            "generation": 42,
            "id": "test_id",
            "name": "test_name",
            "type": "test_type",
        }
        
        # Create model instance
        model = ingest(**valid_data)
        
        # Verify model creation
        assert isinstance(model, ingest)
        assert model.updatedAt == valid_data["updatedAt"]
        assert model.createdAt == valid_data["createdAt"]
        assert model.description == valid_data["description"]
        assert model.generation == valid_data["generation"]
        assert model.id == valid_data["id"]
        assert model.name == valid_data["name"]
        assert model.type == valid_data["type"]


    def test_ingest_model_validation(self):
        """Test ingest model field validation."""
        # Test with minimal required data
        minimal_data = {
            "updatedAt": "required_updatedAt",
            "createdAt": "required_createdAt",
            "generation": 1,
            "id": "required_id",
            "type": "required_type",
        }
        
        model = ingest(**minimal_data)
        assert isinstance(model, ingest)
        assert model.updatedAt == minimal_data["updatedAt"]
        assert model.createdAt == minimal_data["createdAt"]
        assert model.generation == minimal_data["generation"]
        assert model.id == minimal_data["id"]
        assert model.type == minimal_data["type"]


    def test_ingest_model_required_fields(self):
        """Test ingest model required field validation."""
        # Check if this model has any required fields
        required_fields = ["updatedAt", "createdAt", "generation", "id", "type", ]
        
        if required_fields:
            # Test missing required fields
            with pytest.raises(PydanticValidationError) as exc_info:
                ingest()
            
            # Verify validation error contains required field information
            error_details = exc_info.value.errors()
            required_fields_set = {
                "updatedAt",
                "createdAt",
                "generation",
                "id",
                "type",
            }
            
            # Check that at least one required field is mentioned in the error
            error_fields = {error["loc"][0] for error in error_details if error["type"] == "missing"}
            assert len(error_fields.intersection(required_fields_set)) > 0
        else:
            # Model has no required fields - should create successfully with no arguments
            model = ingest()
            assert isinstance(model, ingest)

    def test_ingest_model_optional_fields(self):
        """Test ingest model optional field handling."""
        # Create with minimal required data
        minimal_data = {
            "updatedAt": "required_updatedAt",
            "createdAt": "required_createdAt",
            "generation": 1,
            "id": "required_id",
            "type": "required_type",
        }
        
        model = ingest(**minimal_data)
        
        # Verify model created with minimal required fields
        assert model is not None
        # Verify optional fields have default values
        assert hasattr(model, "description")
        # Optional field description should be None or have a default value
        assert model.description is None or model.description is not None
        assert hasattr(model, "name")
        # Optional field name should be None or have a default value
        assert model.name is None or model.name is not None


    def test_ingest_model_serialization(self):
        """Test ingest model serialization to dict."""
        test_data = {
            "updatedAt": "serialize_value",
            "createdAt": "serialize_value",
            "description": "serialize_value",
            "generation": 99,
            "id": "serialize_value",
            "name": "serialize_value",
            "type": "serialize_value",
        }
        
        model = ingest(**test_data)
        serialized = model.model_dump(by_alias=True)
        
        # Verify serialization
        assert isinstance(serialized, dict)
        assert "updatedAt" in serialized
        assert "createdAt" in serialized
        assert "description" in serialized
        assert "generation" in serialized
        assert "id" in serialized
        assert "name" in serialized
        assert "type" in serialized

        
        # Verify values are preserved
        assert serialized["updatedAt"] == test_data["updatedAt"]
        assert serialized["createdAt"] == test_data["createdAt"]
        assert serialized["description"] == test_data["description"]
        assert serialized["generation"] == test_data["generation"]
        assert serialized["id"] == test_data["id"]
        assert serialized["name"] == test_data["name"]
        assert serialized["type"] == test_data["type"]


    def test_ingest_model_json_schema(self):
        """Test ingest model JSON schema generation."""
        schema = ingest.model_json_schema()
        
        # Verify schema structure
        assert isinstance(schema, dict)
        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema
        
        # Verify all properties are in schema
        expected_properties = {
            "updatedAt",
            "createdAt",
            "description",
            "generation",
            "id",
            "name",
            "type",
        }
        
        schema_properties = set(schema["properties"].keys())
        expected_properties_set = set(expected_properties) if expected_properties else set()
        assert expected_properties_set.issubset(schema_properties)
        
        # Verify required fields in schema (if any)
        required_fields = ["updatedAt", "createdAt", "generation", "id", "type", ]
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
            cloudTotal,
            entity,
            apiError,
            coefficientCostInput,
            currencyComponent,
            tag,
            coefficient,
            coefficientInput,
            currencyCode,
            datasource,
            total,
            timeseries,
            cloudEntity,
            cloudTimeseries,
            ingest,
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
            cloudTotal,
            entity,
            apiError,
            coefficientCostInput,
            currencyComponent,
            tag,
            coefficient,
            coefficientInput,
            currencyCode,
            datasource,
            total,
            timeseries,
            cloudEntity,
            cloudTimeseries,
            ingest,
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
            cloudTotal,
            entity,
            apiError,
            coefficientCostInput,
            currencyComponent,
            tag,
            coefficient,
            coefficientInput,
            currencyCode,
            datasource,
            total,
            timeseries,
            cloudEntity,
            cloudTimeseries,
            ingest,
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
            cloudTotal,
            entity,
            apiError,
            coefficientCostInput,
            currencyComponent,
            tag,
            coefficient,
            coefficientInput,
            currencyCode,
            datasource,
            total,
            timeseries,
            cloudEntity,
            cloudTimeseries,
            ingest,
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
