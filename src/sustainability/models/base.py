# (c) Copyright 2026 Hewlett Packard Enterprise Development LP
"""
Base models for Sustainability_Insight_Center MCP server.

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
        extra="forbid"
    )


class BaseRequest(BaseModel):
    """Base request model with common pagination and filtering."""
    
    # Pagination parameters
    limit: Optional[int] = Field(
        default=None,
        ge=1,
        le=1000,
        description="Maximum number of items to return"
    )
    
    offset: Optional[int] = Field(
        default=None,
        ge=0,
        description="Number of items to skip"
    )
    
    # Filtering parameters
    filter_expression: Optional[str] = Field(
        default=None,
        description="OData-style filter expression"
    )
    
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
    total: Optional[int] = Field(
        default=None,
        description="Total number of items available"
    )
    
    count: Optional[int] = Field(
        default=None,
        description="Number of items in this response"
    )
    
    offset: Optional[int] = Field(
        default=None,
        description="Offset of the first item in this response"
    )
    
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
    details: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Additional error details"
    )


class ResourceMetadata(BaseModel):
    """Common resource metadata."""
    
    created_at: Optional[datetime] = Field(
        default=None,
        description="Resource creation timestamp"
    )
    
    updated_at: Optional[datetime] = Field(
        default=None,
        description="Resource last update timestamp"
    )
    
    created_by: Optional[str] = Field(
        default=None,
        description="User who created the resource"
    )
    
    updated_by: Optional[str] = Field(
        default=None,
        description="User who last updated the resource"
    )


# SERVICE-SPECIFIC MODELS GENERATED FROM OPENAPI SCHEMAS

class cloudTotal(BaseModel):
    """cloudTotal model"""
    
    
    co2eMetricTon: Optional[float] = Field(
        default=None,
        alias="co2eMetricTon",
        description="Total CO2 equivalent generation in metric tons."
    )
    
    type: str = Field(
        
        alias="type",
        description="Type of returned aggregate."
    )
    


class entity(BaseModel):
    """entity model"""
    
    
    locationState: Optional[str] = Field(
        default=None,
        alias="locationState",
        description="State that the the entity is located in."
    )
    
    entitySerialNum: Optional[str] = Field(
        default=None,
        alias="entitySerialNum",
        description="Serial number of the entity."
    )
    
    entityManufacturerTimestamp: Optional[str] = Field(
        default=None,
        alias="entityManufacturerTimestamp",
        description="Manufacturing timestamp of the entity."
    )
    
    name: Optional[str] = Field(
        default=None,
        alias="name",
        description="Name of the entity."
    )
    
    locationName: Optional[str] = Field(
        default=None,
        alias="locationName",
        description="The entity location name."
    )
    
    tags: Optional[List[Any]] = Field(
        default=None,
        alias="tags",
        description="List of the entity's tags"
    )
    
    entityProductId: Optional[str] = Field(
        default=None,
        alias="entityProductId",
        description="Product ID of the entity."
    )
    
    entityType: Optional[str] = Field(
        default=None,
        alias="entityType",
        description="Type of the entity."
    )
    
    locationId: Optional[str] = Field(
        default=None,
        alias="locationId",
        description="ID of the entity location."
    )
    
    type: str = Field(
        
        alias="type",
        description="Type of return object."
    )
    
    id: str = Field(
        
        alias="id",
        description="ID of the entity."
    )
    
    costUsd: Optional[float] = Field(
        default=None,
        alias="costUsd",
        description="Energy cost in USD."
    )
    
    locationCity: Optional[str] = Field(
        default=None,
        alias="locationCity",
        description="City that the the entity is located in."
    )
    
    co2eMetricTon: Optional[float] = Field(
        default=None,
        alias="co2eMetricTon",
        description="CO2 equivalent generation in metric tons."
    )
    
    cost: Optional[float] = Field(
        default=None,
        alias="cost",
        description="Energy cost in the provided currency type."
    )
    
    entityMake: Optional[str] = Field(
        default=None,
        alias="entityMake",
        description="Make of the entity."
    )
    
    currency: Optional[str] = Field(
        default=None,
        alias="currency",
        description="The three letter currency code the costs will be stored or returned in. Supported currencies are: THB - Thai Baht (Thailand) CHF - Swiss Franc (Switzerland) INR - Indian Rupee (India) EUR - Euro Italy, (Germany, Spain, Netherlands, Slovakia, Belgium, Greece, Austria, Slovenia, Finland, Portugal, Estonia) GBP - Pound Sterling (United Kingdom) NOK - Norwegian Krone (Norway) USD - US Dollar (United States, American Samoa, Puerto Rico, Myanmar) AUD - Australian Dollar (Australia) SEK - Swedish Krona (Sweden) HKD - Hong Kong Dollar (Hong Kong) AED - UAE Dirham (United Arab Emirates) NZD - New Zealand Dollar (New Zealand) BGN - Bulgarian Lev (Bulgaria) RON - Romanian Leu (Romania) CAD - Canadian Dollar (Canada) UAH - Ukrainian Hryvnia (Ukraine) MXN - Mexican Peso (Mexico) KRW - South Korean Won (South Korea) JPY - Japanese Yen (Japan) TRY - Turkish Lira (Turkey) DKK - Danish Krone (Denmark) PLN - Polish Zloty (Poland) CZK - Czech Koruna (Czech Republic) CLP - Chilean Peso (Chile) CNY - Chinese Yuan (China) ILS - Israeli New Shekel (Israel) HRK - Croatian Kuna (Croatia) BAM - Convertible Mark (Bosnia and Herzegovina) TWD - New Taiwan Dollar (Taiwan) MYR - Malaysian Ringgit (Malaysia)\n"
    )
    
    kwh: Optional[float] = Field(
        default=None,
        alias="kwh",
        description="Power consumption in kWh."
    )
    
    locationCountry: Optional[str] = Field(
        default=None,
        alias="locationCountry",
        description="Country that the the entity is located in."
    )
    
    entityModel: Optional[str] = Field(
        default=None,
        alias="entityModel",
        description="Model of the entity."
    )
    
    entityId: Optional[str] = Field(
        default=None,
        alias="entityId",
        description="ID of the entity."
    )
    


class apiError(BaseModel):
    """apiError model"""
    
    
    debugId: str = Field(
        
        alias="debugId",
        description="Unique identifier for the instance of this error"
    )
    
    errorCode: str = Field(
        
        alias="errorCode",
        description="Unique machine-friendly identifier for the error."
    )
    
    httpStatusCode: int = Field(
        
        alias="httpStatusCode",
        description="HTTP equivalent status code."
    )
    
    message: str = Field(
        
        alias="message",
        description="User-friendly error message."
    )
    


class coefficientCostInput(BaseModel):
    """coefficientCostInput model"""
    
    
    useCurrent: bool = Field(
        
        alias="useCurrent",
        description="Whether or not to use the preexisting coefficient for this location. Cannot be true if useDefault is also true. Will throw an error if there is no preexisting coefficient."
    )
    
    useDefault: bool = Field(
        
        alias="useDefault",
        description="Whether or not to use the default coefficient for this location. Cannot be true if useCurrent is also true."
    )
    
    value: Optional[float] = Field(
        default=None,
        alias="value",
        description="The coefficient mapping for this location. Used if neither useDefault or useCurrent flags are true."
    )
    
    currencyCode: Optional[str] = Field(
        default=None,
        alias="currencyCode",
        description="The three letter currency code the costs will be stored or returned in. Supported currencies are: THB - Thai Baht (Thailand) CHF - Swiss Franc (Switzerland) INR - Indian Rupee (India) EUR - Euro Italy, (Germany, Spain, Netherlands, Slovakia, Belgium, Greece, Austria, Slovenia, Finland, Portugal, Estonia) GBP - Pound Sterling (United Kingdom) NOK - Norwegian Krone (Norway) USD - US Dollar (United States, American Samoa, Puerto Rico, Myanmar) AUD - Australian Dollar (Australia) SEK - Swedish Krona (Sweden) HKD - Hong Kong Dollar (Hong Kong) AED - UAE Dirham (United Arab Emirates) NZD - New Zealand Dollar (New Zealand) BGN - Bulgarian Lev (Bulgaria) RON - Romanian Leu (Romania) CAD - Canadian Dollar (Canada) UAH - Ukrainian Hryvnia (Ukraine) MXN - Mexican Peso (Mexico) KRW - South Korean Won (South Korea) JPY - Japanese Yen (Japan) TRY - Turkish Lira (Turkey) DKK - Danish Krone (Denmark) PLN - Polish Zloty (Poland) CZK - Czech Koruna (Czech Republic) CLP - Chilean Peso (Chile) CNY - Chinese Yuan (China) ILS - Israeli New Shekel (Israel) HRK - Croatian Kuna (Croatia) BAM - Convertible Mark (Bosnia and Herzegovina) TWD - New Taiwan Dollar (Taiwan) MYR - Malaysian Ringgit (Malaysia)\n"
    )
    


class currencyComponent(BaseModel):
    """currencyComponent model"""
    
    
    currencyCode: str = Field(
        
        alias="currencyCode",
        description="The three letter currency code the costs will be stored or returned in. Supported currencies are: THB - Thai Baht (Thailand) CHF - Swiss Franc (Switzerland) INR - Indian Rupee (India) EUR - Euro Italy, (Germany, Spain, Netherlands, Slovakia, Belgium, Greece, Austria, Slovenia, Finland, Portugal, Estonia) GBP - Pound Sterling (United Kingdom) NOK - Norwegian Krone (Norway) USD - US Dollar (United States, American Samoa, Puerto Rico, Myanmar) AUD - Australian Dollar (Australia) SEK - Swedish Krona (Sweden) HKD - Hong Kong Dollar (Hong Kong) AED - UAE Dirham (United Arab Emirates) NZD - New Zealand Dollar (New Zealand) BGN - Bulgarian Lev (Bulgaria) RON - Romanian Leu (Romania) CAD - Canadian Dollar (Canada) UAH - Ukrainian Hryvnia (Ukraine) MXN - Mexican Peso (Mexico) KRW - South Korean Won (South Korea) JPY - Japanese Yen (Japan) TRY - Turkish Lira (Turkey) DKK - Danish Krone (Denmark) PLN - Polish Zloty (Poland) CZK - Czech Koruna (Czech Republic) CLP - Chilean Peso (Chile) CNY - Chinese Yuan (China) ILS - Israeli New Shekel (Israel) HRK - Croatian Kuna (Croatia) BAM - Convertible Mark (Bosnia and Herzegovina) TWD - New Taiwan Dollar (Taiwan) MYR - Malaysian Ringgit (Malaysia)\n"
    )
    
    currencyName: str = Field(
        
        alias="currencyName",
        description="The name of the currency"
    )
    


class tag(BaseModel):
    """tag model"""
    
    
    name: str = Field(
        
        alias="name",
        description="The name of the tag"
    )
    
    value: str = Field(
        
        alias="value",
        description="The value of the tag"
    )
    


class coefficient(BaseModel):
    """coefficient model"""
    
    
    costPerKwh: Optional[float] = Field(
        default=None,
        alias="costPerKwh",
        description="The cost coefficient per kilowatt-hour for this location. Null if default for this location."
    )
    
    currency: Optional[Dict[str, Any]] = Field(
        default=None,
        alias="currency",
        description="currency field"
    )
    
    updatedAt: str = Field(
        
        alias="updatedAt",
        description="The server-side last updated time of this resource in ISO8601 format."
    )
    
    type: str = Field(
        
        alias="type",
        description="Type of returned coefficient mapping"
    )
    
    associatedLocation: Optional[Dict[str, Any]] = Field(
        default=None,
        alias="associatedLocation",
        description="A reference to the Location resource that this coefficient is bound to."
    )
    
    co2eGramsPerKwh: Optional[float] = Field(
        default=None,
        alias="co2eGramsPerKwh",
        description="The CO2 equivalent generation coefficient in grams per kilowatt-hour for this location. Null if default for this location."
    )
    
    startTime: Optional[str] = Field(
        default=None,
        alias="startTime",
        description="The date in which this coefficient mapping takes effect for this location in ISO8601 format."
    )
    
    costUsdPerKwh: Optional[float] = Field(
        default=None,
        alias="costUsdPerKwh",
        description="The cost coefficient in USD per kilowatt-hour for this location. Null if default for this location."
    )
    
    createdAt: str = Field(
        
        alias="createdAt",
        description="The server-side creation time of this resource in ISO8601 format."
    )
    
    id: str = Field(
        
        alias="id",
        description="ID of the returned coefficient mapping"
    )
    
    generation: int = Field(
        
        alias="generation",
        description="Monotonically increasing update counter"
    )
    


class coefficientInput(BaseModel):
    """coefficientInput model"""
    
    
    useDefault: bool = Field(
        
        alias="useDefault",
        description="Whether or not to use the default coefficient for this location. Cannot be true if useCurrent is also true."
    )
    
    value: Optional[float] = Field(
        default=None,
        alias="value",
        description="The coefficient mapping for this location. Used if neither useDefault or useCurrent flags are true."
    )
    
    useCurrent: bool = Field(
        
        alias="useCurrent",
        description="Whether or not to use the preexisting coefficient for this location. Cannot be true if useDefault is also true. Will throw an error if there is no preexisting coefficient."
    )
    


class currencyCode(BaseModel):
    """The three letter currency code the costs will be stored or returned in. Supported currencies are: THB - Thai Baht (Thailand) CHF - Swiss Franc (Switzerland) INR - Indian Rupee (India) EUR - Euro Italy, (Germany, Spain, Netherlands, Slovakia, Belgium, Greece, Austria, Slovenia, Finland, Portugal, Estonia) GBP - Pound Sterling (United Kingdom) NOK - Norwegian Krone (Norway) USD - US Dollar (United States, American Samoa, Puerto Rico, Myanmar) AUD - Australian Dollar (Australia) SEK - Swedish Krona (Sweden) HKD - Hong Kong Dollar (Hong Kong) AED - UAE Dirham (United Arab Emirates) NZD - New Zealand Dollar (New Zealand) BGN - Bulgarian Lev (Bulgaria) RON - Romanian Leu (Romania) CAD - Canadian Dollar (Canada) UAH - Ukrainian Hryvnia (Ukraine) MXN - Mexican Peso (Mexico) KRW - South Korean Won (South Korea) JPY - Japanese Yen (Japan) TRY - Turkish Lira (Turkey) DKK - Danish Krone (Denmark) PLN - Polish Zloty (Poland) CZK - Czech Koruna (Czech Republic) CLP - Chilean Peso (Chile) CNY - Chinese Yuan (China) ILS - Israeli New Shekel (Israel) HRK - Croatian Kuna (Croatia) BAM - Convertible Mark (Bosnia and Herzegovina) TWD - New Taiwan Dollar (Taiwan) MYR - Malaysian Ringgit (Malaysia)\n"""
    
    


class datasource(BaseModel):
    """datasource model"""
    
    
    id: str = Field(
        
        alias="id",
        description="ID of the returned datasource record"
    )
    
    provider: Optional[str] = Field(
        default=None,
        alias="provider",
        description="Provider name"
    )
    
    updatedAt: str = Field(
        
        alias="updatedAt",
        description="The server-side last updated time of this resource in ISO8601 format."
    )
    
    lastCollectionTime: Optional[str] = Field(
        default=None,
        alias="lastCollectionTime",
        description="Time of the last collected data for this datasource in ISO8601 format."
    )
    
    name: Optional[str] = Field(
        default=None,
        alias="name",
        description="Name of the datasource"
    )
    
    type: str = Field(
        
        alias="type",
        description="Type of returned datasource"
    )
    
    firstCollectionTime: Optional[str] = Field(
        default=None,
        alias="firstCollectionTime",
        description="Time of the first collected data for this datasource in ISO8601 format."
    )
    
    createdAt: str = Field(
        
        alias="createdAt",
        description="The server-side creation time of this resource in ISO8601 format."
    )
    
    generation: int = Field(
        
        alias="generation",
        description="Monotonically increasing update counter"
    )
    


class total(BaseModel):
    """total model"""
    
    
    costUsd: Optional[float] = Field(
        default=None,
        alias="costUsd",
        description="Total energy cost in USD."
    )
    
    currency: Optional[str] = Field(
        default=None,
        alias="currency",
        description="The three letter currency code the costs will be stored or returned in. Supported currencies are: THB - Thai Baht (Thailand) CHF - Swiss Franc (Switzerland) INR - Indian Rupee (India) EUR - Euro Italy, (Germany, Spain, Netherlands, Slovakia, Belgium, Greece, Austria, Slovenia, Finland, Portugal, Estonia) GBP - Pound Sterling (United Kingdom) NOK - Norwegian Krone (Norway) USD - US Dollar (United States, American Samoa, Puerto Rico, Myanmar) AUD - Australian Dollar (Australia) SEK - Swedish Krona (Sweden) HKD - Hong Kong Dollar (Hong Kong) AED - UAE Dirham (United Arab Emirates) NZD - New Zealand Dollar (New Zealand) BGN - Bulgarian Lev (Bulgaria) RON - Romanian Leu (Romania) CAD - Canadian Dollar (Canada) UAH - Ukrainian Hryvnia (Ukraine) MXN - Mexican Peso (Mexico) KRW - South Korean Won (South Korea) JPY - Japanese Yen (Japan) TRY - Turkish Lira (Turkey) DKK - Danish Krone (Denmark) PLN - Polish Zloty (Poland) CZK - Czech Koruna (Czech Republic) CLP - Chilean Peso (Chile) CNY - Chinese Yuan (China) ILS - Israeli New Shekel (Israel) HRK - Croatian Kuna (Croatia) BAM - Convertible Mark (Bosnia and Herzegovina) TWD - New Taiwan Dollar (Taiwan) MYR - Malaysian Ringgit (Malaysia)\n"
    )
    
    kwh: Optional[float] = Field(
        default=None,
        alias="kwh",
        description="Total power consumption in kWh."
    )
    
    type: str = Field(
        
        alias="type",
        description="Type of returned aggregate."
    )
    
    co2eMetricTon: Optional[float] = Field(
        default=None,
        alias="co2eMetricTon",
        description="Total CO2 equivalent generation in metric tons."
    )
    
    cost: Optional[float] = Field(
        default=None,
        alias="cost",
        description="Total energy cost in the provided currency type."
    )
    


class timeseries(BaseModel):
    """timeseries model"""
    
    
    costUsd: Optional[float] = Field(
        default=None,
        alias="costUsd",
        description="Energy cost in USD for this time bucket."
    )
    
    currency: Optional[str] = Field(
        default=None,
        alias="currency",
        description="The three letter currency code the costs will be stored or returned in. Supported currencies are: THB - Thai Baht (Thailand) CHF - Swiss Franc (Switzerland) INR - Indian Rupee (India) EUR - Euro Italy, (Germany, Spain, Netherlands, Slovakia, Belgium, Greece, Austria, Slovenia, Finland, Portugal, Estonia) GBP - Pound Sterling (United Kingdom) NOK - Norwegian Krone (Norway) USD - US Dollar (United States, American Samoa, Puerto Rico, Myanmar) AUD - Australian Dollar (Australia) SEK - Swedish Krona (Sweden) HKD - Hong Kong Dollar (Hong Kong) AED - UAE Dirham (United Arab Emirates) NZD - New Zealand Dollar (New Zealand) BGN - Bulgarian Lev (Bulgaria) RON - Romanian Leu (Romania) CAD - Canadian Dollar (Canada) UAH - Ukrainian Hryvnia (Ukraine) MXN - Mexican Peso (Mexico) KRW - South Korean Won (South Korea) JPY - Japanese Yen (Japan) TRY - Turkish Lira (Turkey) DKK - Danish Krone (Denmark) PLN - Polish Zloty (Poland) CZK - Czech Koruna (Czech Republic) CLP - Chilean Peso (Chile) CNY - Chinese Yuan (China) ILS - Israeli New Shekel (Israel) HRK - Croatian Kuna (Croatia) BAM - Convertible Mark (Bosnia and Herzegovina) TWD - New Taiwan Dollar (Taiwan) MYR - Malaysian Ringgit (Malaysia)\n"
    )
    
    id: str = Field(
        
        alias="id",
        description="ID of the returned time-bucketed aggregate."
    )
    
    kwh: Optional[float] = Field(
        default=None,
        alias="kwh",
        description="Power consumption in kWh for this time bucket."
    )
    
    timeBucket: Optional[str] = Field(
        default=None,
        alias="timeBucket",
        description="Starting time of the returned time-bucketed aggregate in ISO8601 format."
    )
    
    type: str = Field(
        
        alias="type",
        description="Type of returned aggregate."
    )
    
    co2eMetricTon: Optional[float] = Field(
        default=None,
        alias="co2eMetricTon",
        description="CO2 equivalent generation in metric tons for this time bucket."
    )
    
    cost: Optional[float] = Field(
        default=None,
        alias="cost",
        description="Energy cost for this time bucket in the queried for currency type."
    )
    


class cloudEntity(BaseModel):
    """cloudEntity model"""
    
    
    serviceName: Optional[str] = Field(
        default=None,
        alias="serviceName",
        description="Service name of the entity."
    )
    
    serviceRegion: Optional[str] = Field(
        default=None,
        alias="serviceRegion",
        description="Service region of the entity."
    )
    
    entityId: Optional[str] = Field(
        default=None,
        alias="entityId",
        description="ID of the entity."
    )
    
    id: str = Field(
        
        alias="id",
        description="ID of the entity."
    )
    
    serviceAccount: Optional[str] = Field(
        default=None,
        alias="serviceAccount",
        description="Service account id of the entity."
    )
    
    name: Optional[str] = Field(
        default=None,
        alias="name",
        description="Name of the entity."
    )
    
    serviceProvider: Optional[str] = Field(
        default=None,
        alias="serviceProvider",
        description="Cloud service provider of the entity."
    )
    
    type: str = Field(
        
        alias="type",
        description="Type of return object."
    )
    
    co2eMetricTon: Optional[float] = Field(
        default=None,
        alias="co2eMetricTon",
        description="CO2 equivalent generation in metric tons."
    )
    


class cloudTimeseries(BaseModel):
    """cloudTimeseries model"""
    
    
    co2eMetricTon: Optional[float] = Field(
        default=None,
        alias="co2eMetricTon",
        description="CO2 equivalent generation in metric tons for this time bucket."
    )
    
    id: str = Field(
        
        alias="id",
        description="ID of the returned time-bucketed aggregate."
    )
    
    timeBucket: Optional[str] = Field(
        default=None,
        alias="timeBucket",
        description="Starting time of the returned time-bucketed aggregate in ISO8601 format."
    )
    
    type: str = Field(
        
        alias="type",
        description="Type of returned aggregate."
    )
    


class ingest(BaseModel):
    """ingest model"""
    
    
    updatedAt: str = Field(
        
        alias="updatedAt",
        description="The server-side last updated time of this resource in ISO8601 format."
    )
    
    createdAt: str = Field(
        
        alias="createdAt",
        description="The server-side creation time of this resource in ISO8601 format."
    )
    
    description: Optional[str] = Field(
        default=None,
        alias="description",
        description="Description of the ingest"
    )
    
    generation: int = Field(
        
        alias="generation",
        description="Monotonically increasing update counter"
    )
    
    id: str = Field(
        
        alias="id",
        description="ID of the returned record"
    )
    
    name: Optional[str] = Field(
        default=None,
        alias="name",
        description="Name of the record"
    )
    
    type: str = Field(
        
        alias="type",
        description="Type of returned record"
    )
    




