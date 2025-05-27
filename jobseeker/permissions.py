from rest_framework.exceptions import PermissionDenied
from functools import wraps

def check_user_status(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        user_data = getattr(request, 'user_data', None)
        
        if not user_data:
            raise PermissionDenied("Authentication required")
            
        # Check if account is deleted
        if user_data.get('is_deleted', False):
            raise PermissionDenied("Account deleted. Contact support for recovery.")
            
        # Check if account is suspended
        if user_data.get('is_suspended', False):
            raise PermissionDenied("Account suspended. Please contact support.")
            
        # Check if account is pending approval
        if user_data.get('is_pending', False) and user_data.get('role') in ['employer', 'jobseeker']:
            raise PermissionDenied("Account pending approval. Please wait for activation.")
            
        # Check if account is verified (for non-admins)
        if not user_data.get('isVerified', False) and user_data.get('role') not in ['superAdmin', 'admin']:
            raise PermissionDenied("Account not verified. Please verify your email.")
            
        # Check if account is active
        if not user_data.get('is_active', True):
            raise PermissionDenied("Account inactive")
            
        return view_func(request, *args, **kwargs)
    return _wrapped_view


def admin_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        user_data = getattr(request, 'user_data', None)
        if not user_data or user_data.get('role') not in ['admin', 'superAdmin']:
            raise PermissionDenied("Admin privileges required")
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def superadmin_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        user_data = getattr(request, 'user_data', None)
        if not user_data or user_data.get('role') != 'superAdmin':
            raise PermissionDenied("SuperAdmin privileges required")
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def employer_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        user_data = getattr(request, 'user_data', None)
        if not user_data or user_data.get('role') != 'employer':
            raise PermissionDenied("Employer account required")
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def jobseeker_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        user_data = getattr(request, 'user_data', None)
        if not user_data or user_data.get('role') != 'jobseeker':
            raise PermissionDenied("Jobseeker account required")
        return view_func(request, *args, **kwargs)
    return _wrapped_view


# Additional specialized decorators
def active_account_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        user_data = getattr(request, 'user_data', None)
        if not user_data or not user_data.get('is_active', True):
            raise PermissionDenied("Active account required")
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def verified_email_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        user_data = getattr(request, 'user_data', None)
        if not user_data or not user_data.get('isVerified', False):
            raise PermissionDenied("Verified email required")
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def not_suspended(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        user_data = getattr(request, 'user_data', None)
        if not user_data or user_data.get('is_suspended', False):
            raise PermissionDenied("Account is suspended")
        return view_func(request, *args, **kwargs)
    return _wrapped_view