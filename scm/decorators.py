"""
Decorators for automatic exception handling in SCM SDK.

This module provides decorators that automatically convert OpenAPI-generated
exceptions into custom SCM exceptions with better error messages and structure.
"""

from functools import wraps
from typing import Callable, Any
from scm.error_parser import ErrorHandler


def _log_error_headers(exception):
    """
    Log response headers on API errors for debugging.
    Prints X-Request-ID and X-Trace-ID headers when available.
    """
    print("=== API RESPONSE HEADERS ===")

    # Get status code
    status = getattr(exception, 'status', None)
    if status:
        print(f"Status Code: {status}")

    # Get headers from exception
    headers = getattr(exception, 'headers', None)
    request_id = None
    trace_id = None
    flow_error = None

    if headers:
        # Handle HTTPHeaderDict (dict-like) from urllib3
        if hasattr(headers, 'get'):
            request_id = headers.get('X-Request-ID') or headers.get('x-request-id')
            trace_id = headers.get('X-Trace-ID') or headers.get('x-trace-id')
            flow_error = headers.get('X-Request-Flow-Error') or headers.get('x-request-flow-error')
        # Handle list of tuples from getheaders()
        elif isinstance(headers, list):
            for name, value in headers:
                name_lower = name.lower()
                if name_lower == 'x-request-id':
                    request_id = value
                elif name_lower == 'x-trace-id':
                    trace_id = value
                elif name_lower == 'x-request-flow-error':
                    flow_error = value

    if request_id:
        print(f"X-Request-ID: {request_id}")
    if trace_id:
        print(f"X-Trace-ID: {trace_id}")
    if flow_error:
        print(f"X-Request-Flow-Error: {flow_error}")

    # Log error body if available
    body = getattr(exception, 'body', None)
    if body:
        print("=== API ERROR RESPONSE ===")
        print(f"Error Body: {body}")

    print("============================")


def with_error_handling(func: Callable) -> Callable:
    """
    Decorator that automatically parses API exceptions into custom SCM exceptions.

    Wraps API methods to catch OpenAPI-generated exceptions and convert them
    to specific SCM exception types (NameNotUniqueError, ObjectNotPresentError, etc.)

    The decorator preserves the original exception chain using 'raise ... from ...'
    so users can still access the original ApiException if needed.

    Example:
        @with_error_handling
        def create_addresses(self, addresses=None, **kwargs):
            # Method implementation
            ...

    Usage:
        from scm.objects.api.addresses_api import AddressesApi
        from scm.exceptions import NameNotUniqueError, ObjectNotPresentError

        api = AddressesApi(client.objects.api_client)

        try:
            address = api.create_addresses(data)
        except NameNotUniqueError as e:
            print(f"Address '{e.object_name}' already exists")
        except ObjectNotPresentError as e:
            print(f"Object not found: {e}")
    """
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        try:
            return func(*args, **kwargs)
        except Exception as e:
            # Check if it's an API exception that we should parse
            if hasattr(e, 'status') and hasattr(e, 'body'):
                # Log response headers for debugging (X-Request-ID, X-Trace-ID, etc.)
                _log_error_headers(e)
                # This is an OpenAPI ApiException - parse it
                custom_exception = ErrorHandler.parse_exception(e)
                # Raise custom exception with original exception as cause
                raise custom_exception from e
            else:
                # Not an API exception, re-raise as-is
                raise

    return wrapper
