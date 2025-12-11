"""
Models package for audit-logs MCP server.
"""

from .base import (
    BaseModel,
    BaseRequest,
    BaseResponse,
    AuditLogDetails,
    AuditLogs,
    ErrorGeneralDetails,
    ErrorNotFoundDetails,
    AuditLog,
    ErrorBadRequestDetails,
    ErrorRetryDetails,
    PaginatedApiResponse,
    Error,
)

__all__ = [
    "BaseModel",
    "BaseRequest",
    "BaseResponse",
    "AuditLogDetails",
    "AuditLogs",
    "ErrorGeneralDetails",
    "ErrorNotFoundDetails",
    "AuditLog",
    "ErrorBadRequestDetails",
    "ErrorRetryDetails",
    "PaginatedApiResponse",
    "Error",
]
