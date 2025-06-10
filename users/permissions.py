from rest_framework.response import Response
from rest_framework import status

def admin_required(view_func):
    def wrapped_view(self, request, *args, **kwargs):
        if not request.user_data or request.user_data.get('role') not in ['superAdmin', 'admin']:
            return Response({'error': 'Admin privileges required'}, status=status.HTTP_403_FORBIDDEN)
        return view_func(self, request, *args, **kwargs)
    return wrapped_view