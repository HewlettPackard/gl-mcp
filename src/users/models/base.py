# (c) Copyright 2025 Hewlett Packard Enterprise Development LP
"""
Base models for users MCP server.

This module provides base Pydantic models and common types used throughout the service.
"""

from datetime import datetime
from typing import Any, Dict, List, Optional, Literal, Union  # noqa: F401
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


class Message(BaseModel):
    """Message model"""

    message: str = Field(alias="message", description="Message")


class NBUser(BaseModel):
    """User's information for north bound apis."""

    username: str = Field(alias="username", description="User's Email Address")

    lastLogin: Optional[str] = Field(
        default=None, alias="lastLogin", description="Time when this user had last logged in."
    )

    updatedAt: Optional[str] = Field(
        default=None, alias="updatedAt", description="The time the resource was last updated."
    )

    userStatus: Optional[str] = Field(default=None, alias="userStatus", description="On-Boarding Status of a user")

    generation: Optional[int] = Field(default=None, alias="generation", description="Resource history of updates")

    resourceUri: Optional[str] = Field(default=None, alias="resourceUri", description="Full path of the resource")

    id: str = Field(alias="id", description="Resource unique identification")

    createdAt: Optional[str] = Field(default=None, alias="createdAt", description="The time the resource was created.")

    type: str = Field(alias="type", description="Type of data")


class NBUserPaginate(BaseModel):
    """NBUserPaginate model"""

    items: List[Dict[str, Any]] = Field(alias="items", description="List of users")

    offset: int = Field(alias="offset", description="Specifies the offset of the returned page")

    total: int = Field(alias="total", description="The total number of items in the result set")

    count: int = Field(alias="count", description="The number of returned items")


class NBUserPreferences(BaseModel):
    """NBUserPreferences model"""

    idleTimeout: Optional[int] = Field(
        default=None, alias="idleTimeout", description="The user's session idle timeout in seconds."
    )

    language: Optional[str] = Field(default=None, alias="language", description="The preferred language of the user.")


class StandardErrorResponse(BaseModel):
    """Standard GreenLake error response model"""

    debugId: str = Field(
        alias="debugId", description="A unique identifier for this error used to help with troubleshooting."
    )

    errorCode: str = Field(alias="errorCode", description="HPE GreenLake standard error code")

    httpStatusCode: int = Field(alias="httpStatusCode", description="HTTP status code")

    message: str = Field(alias="message", description="A user-friendly error message.")


class UserLanguages(BaseModel):
    """An enumeration."""


class UserStatus(BaseModel):
    """An enumeration."""


class Body_invite_user_to_account_identity_v1_users_post(BaseModel):
    """Body_invite_user_to_account_identity_v1_users_post model"""

    email: Optional[str] = Field(default=None, alias="email", description="Email address of the invited user.")

    sendWelcomeEmail: Optional[bool] = Field(
        default=None, alias="sendWelcomeEmail", description="If enabled, a welcome email is sent to the invited user."
    )
