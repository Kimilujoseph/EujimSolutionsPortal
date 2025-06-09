from rest_framework.response import Response
from rest_framework import status
from functools import wraps

def jobseeker_required(view_func):
    @wraps(view_func)
    def wrapped_view(self, request, *args, **kwargs):
        if not request.user_data or request.user_data.get('role') not in ['jobseeker']:
            return Response({'error': 'Jobseeker privileges required'}, status=status.HTTP_403_FORBIDDEN)
        return view_func(self, request, *args, **kwargs)
    return wrapped_view

def admin_required(view_func):
    @wraps(view_func)
    def wrapped_view(self, request, *args, **kwargs):
       
        if not request.user_data or request.user_data.get('role') not in ['superAdmin', 'admin']:
            return Response({'error': 'Admin privileges required'}, status=status.HTTP_403_FORBIDDEN)
        return view_func(self, request, *args, **kwargs)
    return wrapped_view

def check_user_status(view_func):
    @wraps(view_func)
    def wrapped_view(self, request, *args, **kwargs):
      
        user_data = request.user_data
        
        if not user_data:
            return Response({'error': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)
            
        # Check account suspension status
        if user_data.get('is_suspended', False):
            return Response({'error': 'Account suspended. Please contact support.'}, 
                          status=status.HTTP_403_FORBIDDEN)
            
        # Check verification status for non-admins
        if not user_data.get('isVerified', False):
            return Response({'error': 'Account not verified. Please verify your email.'}, 
                          status=status.HTTP_403_FORBIDDEN)
            
        # Check active status
        if not user_data.get('is_active', True):
            return Response({'error': 'Account inactive'}, 
                          status=status.HTTP_403_FORBIDDEN)
            
        return view_func(self, request, *args, **kwargs)
    return wrapped_view