"""
Decorators for automatic exception handling in SCM SDK.

This module provides decorators that automatically convert OpenAPI-generated
exceptions into custom SCM exceptions with better error messages and structure.
"""

from functools import wraps
from typing import Callable, Any
from scm.error_parser import ErrorHandler


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
                # This is an OpenAPI ApiException - parse it
                custom_exception = ErrorHandler.parse_exception(e)
                # Raise custom exception with original exception as cause
                raise custom_exception from e
            else:
                # Not an API exception, re-raise as-is
                raise

    return wrapper
