"""
SCM Custom Exceptions - Comprehensive error handling for SCM SDK.

Exception Hierarchy:
    ScmException (base)
    ├── ClientError (4xx)
    │   ├── AuthenticationError (401)
    │   │   ├── NotAuthenticatedError
    │   │   ├── InvalidCredentialError
    │   │   └── KeyExpiredError
    │   ├── AuthorizationError (403)
    │   ├── BadRequestError (400)
    │   │   ├── InvalidObjectError
    │   │   ├── MissingQueryParameterError
    │   │   ├── InvalidQueryParameterError
    │   │   └── MalformedCommandError
    │   ├── NotFoundError (404)
    │   │   └── ObjectNotPresentError
    │   ├── ConflictError (409)
    │   │   ├── NameNotUniqueError
    │   │   ├── ObjectNotUniqueError
    │   │   └── ReferenceNotZeroError
    │   ├── MethodNotAllowedError (405)
    │   ├── RequestTimeoutError (408)
    │   ├── TooManyRequestsError (429)
    │   └── SessionTimedOutError
    └── ServerError (5xx)
        ├── InternalServerError (500)
        ├── BadGatewayError (502)
        ├── ServiceUnavailableError (503)
        └── GatewayTimeoutError (504)

These exceptions are automatically raised via decorators. No manual parsing required.

Example:
    from scm.exceptions import NameNotUniqueError, ObjectNotPresentError

    try:
        response = api.create_addresses(addresses=data)
    except NameNotUniqueError as e:
        print(f"Name '{e.object_name}' already exists")
        print(f"Error code: {e.error_code}")
    except ObjectNotPresentError as e:
        print(f"Object not found: {e.object_id}")
"""

from typing import Optional, List, Dict, Any


# =============================================================================
# BASE EXCEPTIONS
# =============================================================================

class ScmException(Exception):
    """Base exception for all SCM-specific errors with structured attributes."""

    def __init__(
        self,
        message: str,
        error_code: Optional[str] = None,
        http_status_code: Optional[int] = None,
        details: Optional[Dict[str, Any]] = None,
        **kwargs
    ):
        """
        Initialize SCM exception.

        Args:
            message: Human-readable error message
            error_code: API error code (e.g., "API_I00013", "E006")
            http_status_code: HTTP status code (e.g., 400, 404, 409)
            details: Additional error details from API response
            **kwargs: Additional attributes (stored for subclasses)
        """
        super().__init__(message)
        self.message = message
        self.error_code = error_code
        self.http_status_code = http_status_code
        self.details = details or {}

        # Store any additional kwargs as attributes
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        """Return string representation including error codes."""
        parts = [self.message]
        if self.error_code:
            parts.append(f"[{self.error_code}]")
        if self.http_status_code:
            parts.append(f"(HTTP {self.http_status_code})")
        return " ".join(parts)


class ClientError(ScmException):
    """Base class for all 4xx client errors."""
    pass


class ServerError(ScmException):
    """Base class for all 5xx server errors."""
    pass


# =============================================================================
# AUTHENTICATION ERRORS (401)
# =============================================================================

class AuthenticationError(ClientError):
    """
    Base class for authentication errors (401).

    Raised when authentication fails or credentials are invalid.
    """
    pass


class NotAuthenticatedError(AuthenticationError):
    """
    Raised when request is not authenticated.

    HTTP Status: 401 Unauthorized

    Common causes:
    - Missing authentication credentials
    - Invalid or expired token
    - Token not provided
    """
    pass


class InvalidCredentialError(AuthenticationError):
    """
    Raised when credentials are invalid.

    HTTP Status: 401 Unauthorized

    Common causes:
    - Invalid client_id or client_secret
    - Incorrect username/password
    - Malformed credentials
    """
    pass


class KeyExpiredError(AuthenticationError):
    """
    Raised when API key or token has expired.

    HTTP Status: 401 Unauthorized

    Common causes:
    - JWT token expired
    - API key expired
    - Session expired
    """
    pass


# =============================================================================
# AUTHORIZATION ERRORS (403)
# =============================================================================

class AuthorizationError(ClientError):
    """
    Raised when user lacks permission for the requested operation.

    HTTP Status: 403 Forbidden

    Common causes:
    - Insufficient privileges
    - Resource access denied
    - Operation not permitted for user role
    """
    pass


# =============================================================================
# BAD REQUEST ERRORS (400)
# =============================================================================

class BadRequestError(ClientError):
    """
    Base class for bad request errors (400).

    Raised when request is malformed or contains invalid data.
    """
    pass


class InvalidObjectError(BadRequestError):
    """
    Raised when object data fails validation.

    HTTP Status: 400 Bad Request
    API Error Codes: E003, API_I00035

    Attributes:
        errors: List of validation errors
    """

    def __init__(
        self,
        message: Optional[str] = None,
        errors: Optional[List[Dict]] = None,
        **kwargs
    ):
        """
        Initialize InvalidObjectError.

        Args:
            message: Error message from API
            errors: List of validation errors
            **kwargs: Additional parameters (error_code, http_status_code, details)
        """
        self.errors = errors or []

        # Build message if not provided
        if not message:
            error_count = len(self.errors)
            if error_count > 0:
                message = f"Object validation failed: {error_count} error(s)"
            else:
                message = "Object validation failed"

        super().__init__(message, **kwargs)


class MissingQueryParameterError(BadRequestError):
    """
    Raised when a required query parameter is missing.

    HTTP Status: 400 Bad Request
    API Error Code: E003 (with message="Missing Query Parameter")

    Attributes:
        parameter_name: Name of the missing parameter
    """

    def __init__(
        self,
        message: Optional[str] = None,
        parameter_name: Optional[str] = None,
        **kwargs
    ):
        """
        Initialize MissingQueryParameterError.

        Args:
            message: Error message from API
            parameter_name: Name of the missing parameter
            **kwargs: Additional parameters (error_code, http_status_code, details)
        """
        self.parameter_name = parameter_name

        # Build message if not provided
        if not message:
            if parameter_name:
                message = f"Missing required parameter: {parameter_name}"
            else:
                message = "Missing required query parameter"

        super().__init__(message, **kwargs)


class InvalidQueryParameterError(BadRequestError):
    """
    Raised when a query parameter has an invalid value.

    HTTP Status: 400 Bad Request

    Attributes:
        parameter_name: Name of the invalid parameter
        parameter_value: Invalid value provided
    """

    def __init__(
        self,
        message: Optional[str] = None,
        parameter_name: Optional[str] = None,
        parameter_value: Optional[Any] = None,
        **kwargs
    ):
        """
        Initialize InvalidQueryParameterError.

        Args:
            message: Error message from API
            parameter_name: Name of the invalid parameter
            parameter_value: Invalid value provided
            **kwargs: Additional parameters (error_code, http_status_code, details)
        """
        self.parameter_name = parameter_name
        self.parameter_value = parameter_value

        # Build message if not provided
        if not message:
            if parameter_name and parameter_value is not None:
                message = f"Invalid value '{parameter_value}' for parameter '{parameter_name}'"
            elif parameter_name:
                message = f"Invalid value for parameter '{parameter_name}'"
            else:
                message = "Invalid query parameter"

        super().__init__(message, **kwargs)


class MalformedCommandError(BadRequestError):
    """
    Raised when command syntax is malformed.

    HTTP Status: 400 Bad Request

    Common causes:
    - Invalid JSON structure
    - Malformed request body
    - Incorrect API call format
    """
    pass


# =============================================================================
# NOT FOUND ERRORS (404)
# =============================================================================

class NotFoundError(ClientError):
    """
    Base class for not found errors (404).

    Raised when requested resource does not exist.
    """
    pass


class ObjectNotPresentError(NotFoundError):
    """
    Raised when an object is not found.

    HTTP Status: 404 Not Found
    API Error Codes: E005, API_I00013 (with errorType="object not present")

    Attributes:
        object_id: ID of the object that was not found
        object_name: Name of the object that was not found
    """

    def __init__(
        self,
        message: Optional[str] = None,
        object_id: Optional[str] = None,
        object_name: Optional[str] = None,
        **kwargs
    ):
        """
        Initialize ObjectNotPresentError.

        Args:
            message: Error message from API
            object_id: ID of the missing object
            object_name: Name of the missing object
            **kwargs: Additional parameters (error_code, http_status_code, details)
        """
        self.object_id = object_id
        self.object_name = object_name

        # Build message if not provided
        if not message:
            if object_id:
                message = f"Object with ID '{object_id}' not found"
            elif object_name:
                message = f"Object '{object_name}' not found"
            else:
                message = "Object not found"

        super().__init__(message, **kwargs)


# =============================================================================
# CONFLICT ERRORS (409)
# =============================================================================

class ConflictError(ClientError):
    """
    Base class for conflict errors (409).

    Raised when request conflicts with current state.
    """
    pass


class NameNotUniqueError(ConflictError):
    """
    Raised when an object name already exists in the same container.

    HTTP Status: 409 Conflict
    API Error Codes: E006, API_I00013 (with errorType="object already exists")

    Attributes:
        object_name: Name of the object that already exists
        container: Container where duplicate was found (folder/snippet/device)
    """

    def __init__(
        self,
        message: Optional[str] = None,
        object_name: Optional[str] = None,
        container: Optional[str] = None,
        **kwargs
    ):
        """
        Initialize NameNotUniqueError.

        Args:
            message: Error message from API
            object_name: Name of the duplicate object
            container: Container (folder/snippet/device)
            **kwargs: Additional parameters (error_code, http_status_code, details)
        """
        self.object_name = object_name
        self.container = container

        # Build message if not provided
        if not message:
            if object_name and container:
                message = f"Object '{object_name}' already exists in {container}"
            elif object_name:
                message = f"Object '{object_name}' already exists"
            else:
                message = "Object name is not unique"

        super().__init__(message, **kwargs)


class ObjectNotUniqueError(ConflictError):
    """
    Raised when object is not unique (broader than name).

    HTTP Status: 409 Conflict

    Similar to NameNotUniqueError but applies to other uniqueness constraints
    (e.g., IP address, MAC address, etc.)
    """
    pass


class ReferenceNotZeroError(ConflictError):
    """
    Raised when attempting to delete an object that is still referenced by other objects.

    HTTP Status: 409 Conflict
    API Error Codes: E009, API_I00013 (with errorType="reference not zero")

    Attributes:
        object_name: Name of the object that cannot be deleted
        references: List of objects that reference this object
    """

    def __init__(
        self,
        message: Optional[str] = None,
        object_name: Optional[str] = None,
        references: Optional[List[Dict]] = None,
        **kwargs
    ):
        """
        Initialize ReferenceNotZeroError.

        Args:
            message: Error message from API
            object_name: Name of the object that is still referenced
            references: List of referencing objects
            **kwargs: Additional parameters (error_code, http_status_code, details)
        """
        self.object_name = object_name
        self.references = references or []

        # Build message if not provided
        if not message:
            ref_count = len(self.references)
            if object_name and ref_count > 0:
                message = f"Cannot delete '{object_name}' - referenced by {ref_count} object(s)"
            elif object_name:
                message = f"Cannot delete '{object_name}' - still has references"
            else:
                message = "Object is still referenced and cannot be deleted"

        super().__init__(message, **kwargs)


# =============================================================================
# OTHER CLIENT ERRORS
# =============================================================================

class MethodNotAllowedError(ClientError):
    """
    Raised when HTTP method is not allowed for the resource.

    HTTP Status: 405 Method Not Allowed

    Common causes:
    - Using POST when only GET is allowed
    - Using DELETE on a read-only resource
    """
    pass


class RequestTimeoutError(ClientError):
    """
    Raised when request times out.

    HTTP Status: 408 Request Timeout

    Common causes:
    - Request took too long to process
    - Client didn't send complete request in time
    """
    pass


class TooManyRequestsError(ClientError):
    """
    Raised when rate limit is exceeded.

    HTTP Status: 429 Too Many Requests

    Attributes:
        retry_after: Number of seconds to wait before retrying
    """

    def __init__(
        self,
        message: Optional[str] = None,
        retry_after: Optional[int] = None,
        **kwargs
    ):
        """
        Initialize TooManyRequestsError.

        Args:
            message: Error message from API
            retry_after: Seconds to wait before retrying
            **kwargs: Additional parameters (error_code, http_status_code, details)
        """
        self.retry_after = retry_after

        # Build message if not provided
        if not message:
            if retry_after:
                message = f"Rate limit exceeded. Retry after {retry_after} seconds"
            else:
                message = "Rate limit exceeded"

        super().__init__(message, **kwargs)


class SessionTimedOutError(ClientError):
    """
    Raised when session has timed out.

    Common causes:
    - Session expired due to inactivity
    - Token expired
    """
    pass


# =============================================================================
# SERVER ERRORS (5xx)
# =============================================================================

class InternalServerError(ServerError):
    """
    Raised when server encounters an internal error.

    HTTP Status: 500 Internal Server Error

    Common causes:
    - Unexpected server condition
    - Unhandled exception on server
    - Server misconfiguration
    """
    pass


class BadGatewayError(ServerError):
    """
    Raised when gateway receives invalid response from upstream server.

    HTTP Status: 502 Bad Gateway

    Common causes:
    - Upstream server down
    - Invalid response from upstream
    - Gateway misconfiguration
    """
    pass


class ServiceUnavailableError(ServerError):
    """
    Raised when service is temporarily unavailable.

    HTTP Status: 503 Service Unavailable

    Attributes:
        retry_after: Number of seconds to wait before retrying

    Common causes:
    - Server maintenance
    - Server overloaded
    - Temporary outage
    """

    def __init__(
        self,
        message: Optional[str] = None,
        retry_after: Optional[int] = None,
        **kwargs
    ):
        """
        Initialize ServiceUnavailableError.

        Args:
            message: Error message from API
            retry_after: Seconds to wait before retrying
            **kwargs: Additional parameters (error_code, http_status_code, details)
        """
        self.retry_after = retry_after

        # Build message if not provided
        if not message:
            if retry_after:
                message = f"Service unavailable. Retry after {retry_after} seconds"
            else:
                message = "Service temporarily unavailable"

        super().__init__(message, **kwargs)


class GatewayTimeoutError(ServerError):
    """
    Raised when gateway times out waiting for upstream server.

    HTTP Status: 504 Gateway Timeout

    Common causes:
    - Upstream server not responding
    - Network connectivity issues
    - Request processing taking too long
    """
    pass


# =============================================================================
# BACKWARDS COMPATIBILITY ALIASES
# =============================================================================

# Keep old names for backwards compatibility
APIError = ScmException  # Alias for pan-scm-sdk compatibility
