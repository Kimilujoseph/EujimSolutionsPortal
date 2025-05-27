from rest_framework.exceptions import PermissionDenied
from functools import wraps
from django.http import HttpRequest

def check_user_status(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        user = request.user
        
        # Check if user is authenticated
        if not user.is_authenticated:
            raise PermissionDenied("Authentication required")
            
        # Check account suspension status
        if getattr(user, 'is_suspended', False):
            raise PermissionDenied("Account suspended. Please contact support.")
            
        # Check deletion status
        if getattr(user, 'is_deleted', False):
            raise PermissionDenied("Account deleted. Contact support for recovery.")
            
        # Check pending status for certain roles
        if getattr(user, 'is_pending', False) and user.role in ['employer', 'jobseeker']:
            raise PermissionDenied("Account pending approval. Please wait for activation.")
            
        # Check verification status for non-admins
        if not getattr(user, 'isVerified', False) and user.role not in ['superAdmin', 'admin']:
            raise PermissionDenied("Account not verified. Please verify your email.")
            
        # Check active status
        if not getattr(user, 'is_active', True):
            raise PermissionDenied("Account inactive")
            
        return view_func(request, *args, **kwargs)
    return _wrapped_view


# Role-based permission decorators
def admin_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.role not in ['admin', 'superAdmin']:
            raise PermissionDenied("Admin privileges required")
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def superadmin_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.role != 'superAdmin':
            raise PermissionDenied("SuperAdmin privileges required")
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def employer_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.role != 'employer':
            raise PermissionDenied("Employer account required")
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def jobseeker_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.role != 'jobseeker':
            raise PermissionDenied("Jobseeker account required")
        return view_func(request, *args, **kwargs)
    return _wrapped_view