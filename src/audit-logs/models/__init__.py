"""
Models package for audit-logs MCP server.
"""

from .base import (
    BaseModel,
    BaseRequest,
    BaseResponse,
    AuditLog,
    ErrorGeneralDetails,
    ErrorRetryDetails,
    PaginatedApiResponse,
    ErrorBadRequestDetails,
    AuditLogDetails,
    AuditLogs,
    Error,
    ErrorNotFoundDetails,
)

__all__ = [
    "BaseModel",
    "BaseRequest",
    "BaseResponse",
    "AuditLog",
    "ErrorGeneralDetails",
    "ErrorRetryDetails",
    "PaginatedApiResponse",
    "ErrorBadRequestDetails",
    "AuditLogDetails",
    "AuditLogs",
    "Error",
    "ErrorNotFoundDetails",
]
