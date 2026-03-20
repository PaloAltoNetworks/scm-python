"""
Common test helper utilities for SCM Python SDK tests.

This module provides shared utilities used across all test files to avoid duplication.
"""

import json
import logging

logger = logging.getLogger(__name__)


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
    if headers:
        # Handle both dict and HTTPHeaderDict types
        if hasattr(headers, 'get'):
            request_id = headers.get('X-Request-ID', headers.get('x-request-id', ''))
            trace_id = headers.get('X-Trace-ID', headers.get('x-trace-id', ''))
            flow_error = headers.get('X-Request-Flow-Error', headers.get('x-request-flow-error', ''))

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


def perform(func, response_type=None, **kwargs):
    """
    Local utility to call an API function and log the request/response details.
    Handles deserialization for 201 responses where the SDK might return None data.

    Args:
        func: The API function to call (should be a _with_http_info method)
        response_type: Optional Pydantic model class for manual deserialization
        **kwargs: Arguments to pass to the API function

    Returns:
        The deserialized response data

    Example:
        created_obj = perform(
            api.create_resource_with_http_info,
            response_type=ResourceModel,
            resource=payload
        )
    """
    func_name = func.__name__
    logger.info(f"\n>>> API REQUEST [{func_name}]")

    # Prepare arguments for logging
    log_kwargs = {}
    for k, v in kwargs.items():
        if hasattr(v, "to_dict"):
            log_kwargs[k] = v.to_dict()
        else:
            log_kwargs[k] = v

    logger.info(json.dumps(log_kwargs, indent=2, default=str))

    # Execute with error header logging
    try:
        response = func(**kwargs)
    except Exception as e:
        # Log response headers on error for debugging
        _log_error_headers(e)
        raise

    # Log raw response info
    logger.info(f"\n<<< API RESPONSE [{func_name}]")

    # Logic to unwrap ApiResponse if present (from _with_http_info calls)
    final_data = response

    if hasattr(response, 'data') and hasattr(response, 'raw_data'):
        logger.info(f"Status Code: {getattr(response, 'status_code', 'N/A')}")

        if response.data is not None:
            final_data = response.data
        elif response.raw_data and response_type:
            # Manual deserialization if SDK returned None for data (common in 201)
            try:
                if hasattr(response_type, 'model_validate_json'):
                    final_data = response_type.model_validate_json(response.raw_data)
                elif hasattr(response_type, 'parse_raw'):
                    final_data = response_type.parse_raw(response.raw_data)
                else:
                    final_data = json.loads(response.raw_data)
            except Exception as e:
                logger.warning(f"Failed to manual deserialize: {e}")
                final_data = response.raw_data

    # Handle tuple responses (legacy support)
    elif isinstance(response, tuple):
        data, status, _ = response
        logger.info(f"Status: {status}")
        if hasattr(data, "to_dict"):
            logger.info(json.dumps(data.to_dict(), indent=2, default=str))
        else:
            logger.info(str(data))
        return data

    # Log the final data
    if hasattr(final_data, "to_dict"):
        logger.info(json.dumps(final_data.to_dict(), indent=2, default=str))
    else:
        logger.info(str(final_data))

    return final_data
