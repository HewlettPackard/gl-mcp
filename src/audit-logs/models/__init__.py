"""
Models package for audit-logs MCP server.
"""

from .base import (
    BaseModel,
    BaseRequest,
    BaseResponse,
    ErrorNotFoundDetails,
    AuditLog,
    AuditLogs,
    ErrorRetryDetails,
    AuditLogDetails,
    ErrorGeneralDetails,
    PaginatedApiResponse,
    Error,
    ErrorBadRequestDetails,
)

__all__ = [
    "BaseModel",
    "BaseRequest",
    "BaseResponse",
    "ErrorNotFoundDetails",
    "AuditLog",
    "AuditLogs",
    "ErrorRetryDetails",
    "AuditLogDetails",
    "ErrorGeneralDetails",
    "PaginatedApiResponse",
    "Error",
    "ErrorBadRequestDetails",
]
