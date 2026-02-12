"""
Error parsing utilities for SCM SDK exceptions.

Refactored to use structured error data with comprehensive exception hierarchy.
Uses a two-level mapping strategy for accurate exception classification.
"""

import json
from typing import Any, Dict, Optional, Type, Union

from scm.exceptions import (
    # Base exceptions
    ScmException,
    ClientError,
    ServerError,

    # Authentication errors (401)
    AuthenticationError,
    NotAuthenticatedError,
    InvalidCredentialError,
    KeyExpiredError,

    # Authorization errors (403)
    AuthorizationError,

    # Bad request errors (400)
    BadRequestError,
    InvalidObjectError,
    MissingQueryParameterError,
    InvalidQueryParameterError,
    MalformedCommandError,

    # Not found errors (404)
    NotFoundError,
    ObjectNotPresentError,

    # Conflict errors (409)
    ConflictError,
    NameNotUniqueError,
    ObjectNotUniqueError,
    ReferenceNotZeroError,

    # Other client errors
    MethodNotAllowedError,
    RequestTimeoutError,
    TooManyRequestsError,
    SessionTimedOutError,

    # Server errors (5xx)
    InternalServerError,
    BadGatewayError,
    ServiceUnavailableError,
    GatewayTimeoutError,
)


class ErrorHandler:
    """Centralized error handling with comprehensive exception hierarchy."""

    # Map HTTP status codes to base exception classes
    STATUS_CODE_MAP: Dict[int, Type[ScmException]] = {
        # 4xx Client Errors
        400: BadRequestError,
        401: AuthenticationError,
        403: AuthorizationError,
        404: NotFoundError,
        405: MethodNotAllowedError,
        408: RequestTimeoutError,
        409: ConflictError,
        429: TooManyRequestsError,

        # 5xx Server Errors
        500: InternalServerError,
        502: BadGatewayError,
        503: ServiceUnavailableError,
        504: GatewayTimeoutError,
    }

    # Map error codes to specific exception classes
    # Supports both direct mapping and nested mapping by errorType/message
    ERROR_CODE_MAP: Dict[str, Union[Type[ScmException], Dict[str, Type[ScmException]]]] = {
        # SCM API error codes
        "API_I00013": {
            "object not present": ObjectNotPresentError,
            "operation impossible": ObjectNotPresentError,
            "object already exists": NameNotUniqueError,
            "object_already_exists": NameNotUniqueError,
            "non_zero_refs": ReferenceNotZeroError,
            "reference not zero": ReferenceNotZeroError,
            "default": InvalidObjectError,  # Fallback for other API_I00013 messages
        },
        "API_I00035": {
            "resource not present": ObjectNotPresentError,
            "default": InvalidObjectError,  # Fallback for other messages
        },

        # Legacy error codes
        "E003": {
            "Missing Query Parameter": MissingQueryParameterError,
            "Invalid Query Parameter": InvalidQueryParameterError,
            "Invalid Object": InvalidObjectError,
            "Malformed Command": MalformedCommandError,
            "default": BadRequestError,
        },
        "E005": ObjectNotPresentError,
        "E006": NameNotUniqueError,
        "E009": ReferenceNotZeroError,

        # Authentication error codes
        "E001": NotAuthenticatedError,
        "E002": InvalidCredentialError,
        "E011": KeyExpiredError,
        "E016": SessionTimedOutError,

        # Authorization error codes
        "E004": AuthorizationError,

        # Server error codes
        "E007": InternalServerError,
        "E008": ServiceUnavailableError,
    }

    # Map message patterns to exception classes (for cases without error codes)
    MESSAGE_PATTERN_MAP: Dict[str, Type[ScmException]] = {
        # Authentication patterns
        "not authenticated": NotAuthenticatedError,
        "authentication failed": NotAuthenticatedError,
        "invalid credentials": InvalidCredentialError,
        "invalid client": InvalidCredentialError,
        "unauthorized": NotAuthenticatedError,
        "token expired": KeyExpiredError,
        "jwt expired": KeyExpiredError,
        "session expired": SessionTimedOutError,
        "session timed out": SessionTimedOutError,

        # Authorization patterns
        "forbidden": AuthorizationError,
        "access denied": AuthorizationError,
        "insufficient privileges": AuthorizationError,
        "permission denied": AuthorizationError,

        # Not found patterns
        "not found": ObjectNotPresentError,
        "does not exist": ObjectNotPresentError,
        "object not present": ObjectNotPresentError,

        # Conflict patterns
        "already exists": NameNotUniqueError,
        "duplicate": NameNotUniqueError,
        "name is not unique": NameNotUniqueError,
        "reference not zero": ReferenceNotZeroError,
        "still referenced": ReferenceNotZeroError,

        # Bad request patterns
        "invalid object": InvalidObjectError,
        "validation failed": InvalidObjectError,
        "missing parameter": MissingQueryParameterError,
        "invalid parameter": InvalidQueryParameterError,
        "malformed": MalformedCommandError,

        # Rate limiting
        "rate limit": TooManyRequestsError,
        "too many requests": TooManyRequestsError,

        # Server errors
        "internal server error": InternalServerError,
        "service unavailable": ServiceUnavailableError,
        "bad gateway": BadGatewayError,
        "gateway timeout": GatewayTimeoutError,
    }

    @classmethod
    def parse_exception(
        cls,
        exception_or_status,
        body: Optional[str] = None,
        reason: Optional[str] = None,
    ) -> ScmException:
        """
        Parse an API exception and return the appropriate custom exception.

        Args:
            exception_or_status: Either an ApiException object or HTTP status code
            body: Optional JSON response body (if status code provided)
            reason: Optional reason phrase (if status code provided)

        Returns:
            ScmException: Appropriate subclass based on error details

        Examples:
            # From caught exception
            try:
                api.get_by_id(id="...")
            except NotFoundException as e:
                custom_exc = ErrorHandler.parse_exception(e)

            # From status/body/reason
            custom_exc = ErrorHandler.parse_exception(404, '{"message": "..."}', "Not Found")
        """
        # Extract status, body, reason from exception or parameters
        if hasattr(exception_or_status, 'status'):
            # It's an ApiException object
            status = exception_or_status.status
            body = exception_or_status.body
            reason = exception_or_status.reason

            # Try to get structured error data from Pydantic model
            error_data = cls._extract_error_data(exception_or_status)
        else:
            # It's a status code
            status = exception_or_status
            try:
                error_data = json.loads(body) if body else {}
            except (json.JSONDecodeError, TypeError):
                # Not valid JSON, return generic exception
                return ScmException(
                    reason or f"HTTP {status}",
                    error_code=str(status),
                    http_status_code=status
                )

        # Extract error details from response
        error_info = cls._extract_error_info(error_data, status, reason)

        # Map to appropriate exception class
        exception_cls = cls._map_exception_class(
            status=status,
            error_code=error_info['error_code'],
            error_type=error_info['error_type'],
            message=error_info['message'],
        )

        # Extract retry_after if present (for rate limiting and service unavailable)
        retry_after = None
        if status in (429, 503):
            retry_after = error_info['details'].get('retry_after')

        # Instantiate exception with all available info
        return exception_cls(
            message=error_info['message'],
            error_code=error_info['error_code'],
            http_status_code=status,
            details=error_info['details'],
            # Include object_id/object_name if available
            object_id=error_info.get('object_id'),
            object_name=error_info.get('object_name'),
            # Include parameter info for query parameter errors
            parameter_name=error_info.get('parameter_name'),
            parameter_value=error_info.get('parameter_value'),
            # Include retry_after for rate limit and service unavailable
            retry_after=retry_after,
            # Include references for ReferenceNotZeroError
            references=error_info.get('references'),
            # Include errors list for InvalidObjectError
            errors=error_info.get('errors'),
        )

    @classmethod
    def _extract_error_data(cls, exception) -> Dict[str, Any]:
        """Extract error data from exception's data attribute (Pydantic model)."""
        if hasattr(exception, 'data') and exception.data:
            # Data is a Pydantic model, convert to dict
            if hasattr(exception.data, 'model_dump'):
                return exception.data.model_dump()
            elif hasattr(exception.data, 'dict'):
                return exception.data.dict()
            else:
                # Try to access as dict-like object
                return dict(exception.data) if exception.data else {}
        else:
            # Try to parse body as JSON
            try:
                return json.loads(exception.body) if exception.body else {}
            except (json.JSONDecodeError, TypeError, AttributeError):
                return {}

    @classmethod
    def _extract_error_info(cls, error_data: Dict[str, Any], status: int, reason: str) -> Dict[str, Any]:
        """
        Extract structured error information from API response.

        Returns dict with keys:
        - error_code: str
        - message: str
        - error_type: str (from details.errorType)
        - details: dict
        - object_id: Optional[str]
        - object_name: Optional[str]
        - parameter_name: Optional[str]
        - parameter_value: Optional[Any]
        - references: Optional[List[Dict]]
        - errors: Optional[List[Dict]]
        """
        # Handle GenericError model structure (common format)
        if 'errors' in error_data and isinstance(error_data['errors'], list) and len(error_data['errors']) > 0:
            first_error = error_data['errors'][0]
            error_code = first_error.get('code', '')
            message = first_error.get('message', reason or f"HTTP {status}")
            details = first_error.get('details', {})
        else:
            # Standard error format
            error_code = error_data.get('code', '')
            message = error_data.get('message', reason or f"HTTP {status}")
            details = error_data.get('details', {})

        # Ensure details is a dict (API sometimes returns a string)
        if not isinstance(details, dict):
            details = {}

        # Extract errorType from details (structured field provided by API)
        error_type = details.get('errorType', '')

        # Check for nested error structure
        if not error_type and 'errors' in details:
            errors_list = details.get('errors', [])
            if isinstance(errors_list, list) and len(errors_list) > 0:
                if isinstance(errors_list[0], dict):
                    error_type = errors_list[0].get('type', '')

        # Extract object_id and object_name from details if available
        object_id = details.get('id') or details.get('object_id')
        object_name = details.get('name') or details.get('object_name')

        # Extract parameter info from details
        parameter_name = details.get('parameter') or details.get('param')
        parameter_value = details.get('value')

        # Extract references for ReferenceNotZeroError
        references = details.get('references', [])

        # Extract validation errors for InvalidObjectError
        errors = details.get('errors', [])

        return {
            'error_code': error_code,
            'message': message,
            'error_type': error_type,
            'details': details,
            'object_id': object_id,
            'object_name': object_name,
            'parameter_name': parameter_name,
            'parameter_value': parameter_value,
            'references': references if isinstance(references, list) else [],
            'errors': errors if isinstance(errors, list) else [],
        }

    @classmethod
    def _map_exception_class(
        cls,
        status: int,
        error_code: str,
        error_type: str,
        message: str,
    ) -> Type[ScmException]:
        """
        Map error details to appropriate exception class using multi-level strategy.

        Priority:
        1. Error code + error type match (most specific)
        2. Error code match (general)
        3. Message pattern match (for cases without error codes)
        4. HTTP status code match
        5. Default to generic ClientError/ServerError based on status range
        """
        # Get base exception class from HTTP status code
        exception_cls = cls.STATUS_CODE_MAP.get(status)

        # If no specific mapping, use generic ClientError or ServerError
        if not exception_cls:
            if 400 <= status < 500:
                exception_cls = ClientError
            elif 500 <= status < 600:
                exception_cls = ServerError
            else:
                exception_cls = ScmException

        # Refine based on error code
        if error_code in cls.ERROR_CODE_MAP:
            code_mapping = cls.ERROR_CODE_MAP[error_code]

            # If mapping is a dict, match by errorType or message
            if isinstance(code_mapping, dict):
                # Try case-insensitive errorType match
                if error_type:
                    error_type_lower = error_type.lower()
                    code_mapping_lower = {k.lower(): v for k, v in code_mapping.items()}
                    if error_type_lower in code_mapping_lower:
                        exception_cls = code_mapping_lower[error_type_lower]
                        return exception_cls

                # Try exact message match
                if message in code_mapping:
                    exception_cls = code_mapping[message]
                    return exception_cls

                # Try case-insensitive message substring match
                message_lower = message.lower()
                for key, exc_class in code_mapping.items():
                    if key != 'default' and key.lower() in message_lower:
                        exception_cls = exc_class
                        return exception_cls

                # Try default fallback
                if 'default' in code_mapping:
                    exception_cls = code_mapping['default']
                    return exception_cls

                # Use base exception from status code
                return exception_cls
            else:
                # Direct mapping
                return code_mapping

        # Try message pattern matching (for cases without error codes)
        if message:
            message_lower = message.lower()
            for pattern, exc_class in cls.MESSAGE_PATTERN_MAP.items():
                if pattern in message_lower:
                    return exc_class

        # Use base exception from status code
        return exception_cls


# Backward compatibility: keep parse_scm_error function
def parse_scm_error(exception_or_status, body: Optional[str] = None, reason: Optional[str] = None) -> ScmException:
    """
    Parse an API exception and return the appropriate custom exception.

    This function is maintained for backward compatibility.
    New code should use ErrorHandler.parse_exception() directly.

    Args:
        exception_or_status: Either an ApiException object or HTTP status code
        body: Optional JSON response body (if status code provided)
        reason: Optional reason phrase (if status code provided)

    Returns:
        ScmException: Appropriate subclass based on error details

    Examples:
        # From caught exception
        try:
            addresses_api.get_addresses_by_id(id=created_obj.id)
        except NotFoundException as e:
            custom_exc = parse_scm_error(e)
            assert isinstance(custom_exc, ObjectNotPresentError)

        # From raw status/body/reason
        custom_exc = parse_scm_error(404, '{"message": "..."}', "Not Found")
    """
    return ErrorHandler.parse_exception(exception_or_status, body, reason)
