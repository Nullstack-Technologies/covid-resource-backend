from math import ceil

from rest_framework.views import exception_handler
from rest_framework.exceptions import Throttled, PermissionDenied


def throttled_exception_handler(exc, context):
    """
        Override the throttled exception
        to look it more reader friendly
    """

    response = exception_handler(exc, context)

    if isinstance(exc, Throttled):
        custom_response_data = {
            'non_field_errors': f'⚠️ You are doing too much, Why not come back after {ceil(exc.wait / 60)} minute(s)?',
        }
        response.data = custom_response_data
    if isinstance(exc, PermissionDenied):
        custom_response_data = {
            'non_field_errors': f'⚠️ {exc}',
        }
        response.data = custom_response_data
    return response
