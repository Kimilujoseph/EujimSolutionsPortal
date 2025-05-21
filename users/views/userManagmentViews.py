# views/admin.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from  ..services.userManagement import UserManagementService

class AdminUserDeleteView(APIView):
    def delete(self, request, user_id):
        if not request.user_data or request.user_data.get('role') not in  ['superAdmin','admin']:
            return Response({'error': 'Admin priveledges required'}, status=status.HTTP_403_FORBIDDEN)
        service = UserManagementService()
        result = service.delete_user(
            user_id=user_id,
            deleted_by=request.user_data,
            reason=request.data.get('reason')
        )
        return Response(result, status=status.HTTP_200_OK)

    

class AdminUserListView(APIView):
    def get(self, request):
        service = UserManagementService()
        users = service.list_users(include_deleted=request.query_params.get('show_deleted', False))
        # Add serialization here
        return Response(users, status=status.HTTP_200_OK)

class AdminUserRestoreView(APIView):
    def post(self, request, user_id):
        if not request.user_data or request.user_data.get('role') not in  ['superAdmin','admin']:
            return Response({'error': 'Admin priveledges required'}, status=status.HTTP_403_FORBIDDEN)
        service = UserManagementService()
        result = service.restore_user(
            user_id=user_id,
            restored_by=request.user_data
        )
        return Response(result, status=status.HTTP_200_OK)
    
class AdminToggleSuspendUserView(APIView):
    def post(self, request, user_id):
        if not request.user_data or request.user_data.get('role') not in ['admin', 'superAdmin']:
            return Response({'error': 'Admin privileges required'}, status=status.HTTP_403_FORBIDDEN)
        
        service = UserManagementService()
        try:
            user = service.toggle_suspension(user_id)
            return Response({
                'status': 'success',
                'message': f"User {user.id} suspension status updated.",
                'is_suspended': user.is_suspended
            }, status=status.HTTP_200_OK)
        except ValueError as ve:
            return Response({'error': str(ve)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AdminTogglePendingStatusView(APIView):
    def post(self, request, user_id):
        if not request.user_data or request.user_data.get('role') not in ['admin', 'superAdmin']:
            return Response({'error': 'Admin privileges required'}, status=status.HTTP_403_FORBIDDEN)

        service = UserManagementService()
        try:
            user = service.toggle_pending_status(user_id)
            return Response({
                'status': 'success',
                'message': f"User {user.id} pending status updated.",
                'is_pending': user.is_pending
            }, status=status.HTTP_200_OK)
        except ValueError as ve:
            return Response({'error': str(ve)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AdminToggleVerificationView(APIView):
    def post(self, request, user_id):
        if not request.user_data or request.user_data.get('role') not in ['admin', 'superAdmin']:
            return Response({'error': 'Admin privileges required'}, status=status.HTTP_403_FORBIDDEN)

        service = UserManagementService()
        try:
            user = service.toggle_verification(user_id)
            return Response({
                'status': 'success',
                'message': f"User {user.id} verification status updated.",
                'is_verified': user.isVerified
            }, status=status.HTTP_200_OK)
        except ValueError as ve:
            return Response({'error': str(ve)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
