"""
Models package for audit-logs MCP server.
"""

from .base import (
    BaseModel,
    BaseRequest,
    BaseResponse,
    AuditLogDetails,
    Error,
    AuditLog,
    AuditLogs,
    ErrorGeneralDetails,
    ErrorRetryDetails,
    ErrorBadRequestDetails,
    ErrorNotFoundDetails,
    PaginatedApiResponse,
)

__all__ = [
    "BaseModel",
    "BaseRequest",
    "BaseResponse",
    "AuditLogDetails",
    "Error",
    "AuditLog",
    "AuditLogs",
    "ErrorGeneralDetails",
    "ErrorRetryDetails",
    "ErrorBadRequestDetails",
    "ErrorNotFoundDetails",
    "PaginatedApiResponse",
]
