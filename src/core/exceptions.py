from typing import Optional, Dict, Any
from fastapi import status


class AppException(Exception):
    """Base application exception"""
    def __init__(
        self,
        message: str,
        status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
        error_code: str = "internal_error",
        details: Optional[Dict[str, Any]] = None
    ):
        self.message = message
        self.status_code = status_code
        self.error_code = error_code
        self.details = details or {}
        super().__init__(self.message)


class BorrowerNotFoundException(AppException):
    def __init__(self, borrower_id: str):
        super().__init__(
            message=f"Borrower with ID {borrower_id} not found",
            status_code=status.HTTP_404_NOT_FOUND,
            error_code="borrower_not_found",
            details={"borrower_id": borrower_id}
        )


class CacheException(AppException):
    def __init__(self, message: str, error: Optional[Exception] = None):
        super().__init__(
            message=f"Cache error: {message}",
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            error_code="cache_error",
            details={"original_error": str(error) if error else None}
        )


class DatabaseException(AppException):
    def __init__(self, message: str, error: Optional[Exception] = None):
        super().__init__(
            message=f"Database error: {message}",
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            error_code="database_error",
            details={"original_error": str(error) if error else None}
        )


class LLMException(AppException):
    def __init__(self, message: str, error: Optional[Exception] = None):
        super().__init__(
            message=f"LLM error: {message}",
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            error_code="llm_error",
            details={"original_error": str(error) if error else None}
        )


class ValidationException(AppException):
    def __init__(self, message: str, field_errors: Dict[str, str]):
        super().__init__(
            message=f"Validation error: {message}",
            status_code=status.HTTP_400_BAD_REQUEST,
            error_code="validation_error",
            details={"field_errors": field_errors}
        )


class AgentException(AppException):
    def __init__(self, message: str, agent_name: str, error: Optional[Exception] = None):
        super().__init__(
            message=f"Agent '{agent_name}' error: {message}",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            error_code="agent_error",
            details={"agent": agent_name, "original_error": str(error) if error else None}
        )


class WorkflowException(AppException):
    def __init__(self, message: str, step: str, error: Optional[Exception] = None):
        super().__init__(
            message=f"Workflow error at step '{step}': {message}",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            error_code="workflow_error",
            details={"step": step, "original_error": str(error) if error else None}
        )


class CommunicationException(AppException):
    def __init__(self, message: str, channel: str, error: Optional[Exception] = None):
        super().__init__(
            message=f"Communication error via {channel}: {message}",
            status_code=status.HTTP_502_BAD_GATEWAY,
            error_code="communication_error",
            details={"channel": channel, "original_error": str(error) if error else None}
        )


class RateLimitException(AppException):
    def __init__(self, message: str, retry_after: int):
        super().__init__(
            message=message,
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            error_code="rate_limit_exceeded",
            details={"retry_after": retry_after}
        )


class ConfigurationException(AppException):
    def __init__(self, message: str):
        super().__init__(
            message=f"Configuration error: {message}",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            error_code="configuration_error"
        )