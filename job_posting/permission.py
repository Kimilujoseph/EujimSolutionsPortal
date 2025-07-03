from rest_framework.response import Response
from rest_framework import status
from functools import wraps

def recruiter_required(view_func):
    @wraps(view_func)
    def wrapped_view(self, request, *args, **kwargs):
        if not request.user_data or request.user_data.get('role') not in ['employer']:
            return Response({'error': 'Recruiter privileges required'}, status=status.HTTP_403_FORBIDDEN)
        return view_func(self, request, *args, **kwargs)
    return wrapped_view

def recruiter_or_admin_required(view_func):
    @wraps(view_func)
    def wrapped_view(self, request, *args, **kwargs):
        if not request.user_data or request.user_data.get('role') not in ['employer', 'superAdmin', 'admin']:
            return Response({'error': 'Recruiter or admin privileges required'}, status=status.HTTP_403_FORBIDDEN)
        return view_func(self, request, *args, **kwargs)
    return wrapped_view