"""
Models package for audit-logs MCP server.
"""

from .base import (
    BaseModel,
    BaseRequest,
    BaseResponse,
    AuditLog,
    AuditLogDetails,
    ErrorBadRequestDetails,
    ErrorGeneralDetails,
    ErrorNotFoundDetails,
    ErrorRetryDetails,
    AuditLogs,
    PaginatedApiResponse,
    Error,
)

__all__ = [
    "BaseModel",
    "BaseRequest",
    "BaseResponse",
    "AuditLog",
    "AuditLogDetails",
    "ErrorBadRequestDetails",
    "ErrorGeneralDetails",
    "ErrorNotFoundDetails",
    "ErrorRetryDetails",
    "AuditLogs",
    "PaginatedApiResponse",
    "Error",
]
