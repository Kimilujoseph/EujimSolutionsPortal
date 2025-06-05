# permissions.py
from rest_framework.response import Response
from rest_framework import status
from functools import wraps

def recruiter_required(view_func):
    @wraps(view_func)
    def wrapped_view(self, request, *args, **kwargs):
        if not request.user_data or request.user_data.get('role') not in ['recruiter']:
            return Response({'error': 'Recruiter privileges required'}, status=status.HTTP_403_FORBIDDEN)
        return view_func(self, request, *args, **kwargs)
    return wrapped_view

def recruiter_or_admin_required(view_func):
    @wraps(view_func)
    def wrapped_view(self, request, *args, **kwargs):
        if not request.user_data or request.user_data.get('role') not in ['recruiter', 'superAdmin', 'admin']:
            return Response({'error': 'Recruiter or admin privileges required'}, status=status.HTTP_403_FORBIDDEN)
        return view_func(self, request, *args, **kwargs)
    return wrapped_view

def check_recruiter_status(view_func):
    @wraps(view_func)
    def wrapped_view(self, request, *args, **kwargs):
        user_data = request.user_data
        
        if not user_data:
            return Response({'error': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)
            
        # For recruiter-specific routes, verify role first
        if user_data.get('role') != 'recruiter':
            return Response({'error': 'Recruiter privileges required'}, status=status.HTTP_403_FORBIDDEN)
            
        # Check account suspension status
        if user_data.get('is_suspended', False):
            return Response({'error': 'Account suspended. Please contact support.'}, 
                          status=status.HTTP_403_FORBIDDEN)
            
        # Check verification status (both user and recruiter profile)
        if not user_data.get('isVerified', False):
            return Response({'error': 'User account not verified. Please verify your email.'}, 
                          status=status.HTTP_403_FORBIDDEN)
            
        # Additional recruiter-specific verification
        if not user_data.get('recruiter_profile', {}).get('isVerified', False):
            return Response({'error': 'Recruiter profile not verified. Please complete verification.'}, 
                          status=status.HTTP_403_FORBIDDEN)
            
        # Check active status
        if not user_data.get('is_active', True):
            return Response({'error': 'Account inactive'}, 
                          status=status.HTTP_403_FORBIDDEN)
            
        return view_func(self, request, *args, **kwargs)
    return wrapped_view

# Combined decorator for common recruiter routes
def recruiter_access_required(view_func):
    @wraps(view_func)
    @check_recruiter_status  # Reuse your existing user status checker
    @recruiter_required
    def wrapped_view(self, request, *args, **kwargs):
        return view_func(self, request, *args, **kwargs)
    return wrapped_view