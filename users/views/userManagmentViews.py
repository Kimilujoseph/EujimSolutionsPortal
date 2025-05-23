from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from  ..services.userManagement import UserManagementService
from ..serializers.user_serializer import UserSerializer
from ..utils import send_approval_email,send_disapproval_email
class AdminUserDeleteView(APIView):
    @admin_required
    def delete(self, request, user_id):
        service = UserManagementService()
        result = service.delete_user(
            user_id=user_id,
            deleted_by=request.user_data,
            reason=request.data.get('reason')
        )
        return Response(result, status=status.HTTP_200_OK)

    

class AdminUserListView(APIView):
    @admin_required
    def get(self, request):
        service = UserManagementService()
        users = service.list_users(include_deleted=request.query_params.get('show_deleted', False))
        if isinstance(users, dict) and users.get('status') == 'error':
            return Response(users, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        

class AdminUserRestoreView(APIView):
    @admin_required
    def post(self, request, user_id):
        service = UserManagementService()
        result = service.restore_user(
            user_id=user_id,
            restored_by=request.user_data
        )
        return Response(result, status=status.HTTP_200_OK)
    
class AdminToggleSuspendUserView(APIView):
    @admin_required
    def post(self, request, user_id):      
        service = UserManagementService()
        try:
            user = service.toggle_suspension(user_id)
            return Response({
                'status': 'success',
                'message': f"User {user.firstName} suspension status updated.",
                'is_suspended': user.is_suspended
            }, status=status.HTTP_200_OK)
        except ValueError as ve:
            return Response({'error': str(ve)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AdminTogglePendingStatusView(APIView):
    @admin_required
    def post(self, request, user_id):
        service = UserManagementService()

        try:
            user = service.toggle_pending_status(user_id)
            if user.is_pending is False:
                send_approval_email(user,request)
            else:
                send_disapproval_email(user,request)
            return Response({
                'status': 'success',
                'message': f"User {user.firstName} pending status updated.",
                'is_pending': user.is_pending
            }, status=status.HTTP_200_OK)
        except ValueError as ve:
            return Response({'error': str(ve)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AdminToggleVerificationView(APIView):
    @admin_required
    def post(self, request, user_id):
        service = UserManagementService()
        try:
            user = service.toggle_verification(user_id)
            return Response({
                'status': 'success',
                'message': f"User {user.firstName} verification status updated.",
                'is_verified': user.isVerified
            }, status=status.HTTP_200_OK)
        except ValueError as ve:
            return Response({'error': str(ve)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AdminUserDetailView(APIView):
    @admin_required
    def get(self, request, user_id):
        if not request.user_data or request.user_data.get('role') not in ['admin', 'superAdmin']:
            return Response({'error': 'Admin privileges required'}, status=status.HTTP_403_FORBIDDEN)

        service = UserManagementService()
        try:
            data = service.get_user_with_profile(user_id)
            return Response(data)
        except ValueError as e:
            return Response({'error': str(e)}, status=404)
     
