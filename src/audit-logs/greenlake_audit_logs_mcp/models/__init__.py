"""
Models package for audit-logs MCP server.
"""

from .base import (
    BaseModel,
    BaseRequest,
    BaseResponse,
    Error,
    ErrorNotFoundDetails,
    PaginatedApiResponse,
    ErrorBadRequestDetails,
    ErrorRetryDetails,
    AuditLog,
    AuditLogs,
    ErrorGeneralDetails,
    AuditLogDetails,
)

__all__ = [
    "BaseModel",
    "BaseRequest",
    "BaseResponse",
    "Error",
    "ErrorNotFoundDetails",
    "PaginatedApiResponse",
    "ErrorBadRequestDetails",
    "ErrorRetryDetails",
    "AuditLog",
    "AuditLogs",
    "ErrorGeneralDetails",
    "AuditLogDetails",
]
