from rest_framework.exceptions import APIException
from rest_framework import status

class ServiceException(APIException):
    """Base for all service-level errors."""
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'A service error occurred.'

class NotFoundException(ServiceException):
    """Raised when a requested resource isn't found."""
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = 'Resource not found.'

class ConflictException(ServiceException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = 'Conflict occurred.'

class InternalErrorException(ServiceException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = 'Internal server error.'