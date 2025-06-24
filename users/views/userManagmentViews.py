from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from  ..services.userManagement import UserManagementService
from ..serializers.user_serializer import UserSerializer
from ..utils import send_approval_email,send_disapproval_email,send_suspension_email,send_unsuspension_email
from ..permissions import admin_required

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
        include_deleted = request.query_params.get('show_deleted','false').lower() == 'true'
        role=request.query_params.get('role')
        users = service.list_users(include_deleted=include_deleted,role=role)
        if isinstance(users, dict) and users.get('status') == 'error':
            return Response(users, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# class AdminUserListAllView(APIView):
#     @admin_required
#     def get(self, request):
#         service = UserManagementService()
#         users = service.get_all_users()
#         if isinstance(users, dict) and users.get('status') == 'error':
#             return Response(users, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
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
            
            suspension_reason = request.data.get('reason', 'Violation of terms of service')
            
            user = service.toggle_suspension(user_id)
            if not user:
                return Response({
                    'status':'failed',
                    'message':'failed to update',
                    'code':404
                },status=status.HTTP_404_NOT_FOUND)
            
            if user.is_suspended:
                send_suspension_email(
                    user=user,
                    request=request,
                    suspension_reason=suspension_reason
                )
                message = f"User {user.firstName} has been suspended."
            else:
                send_unsuspension_email(user, request)
                message = f"User {user.firstName}'s suspension has been lifted."
    
            return Response({
                'status': 'success',
                'message': message,
                'is_suspended': user.is_suspended
            }, status=status.HTTP_200_OK)
            
        except ValueError as ve:
            return Response({
                'status': 'error',
                'message': str(ve),
                'code': 404
            }, status=status.HTTP_404_NOT_FOUND)
            
        except Exception as e:
            print(f"Database error: {e}")
            return Response({
                'status': 'error',
                'message': 'Failed to update suspension status',
                'details': str(e),
                'code': 500
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AdminTogglePendingStatusView(APIView):
    @admin_required
    def post(self, request, user_id):
        service = UserManagementService()

        try:
            user = service.toggle_pending_status(user_id)
            if not user:
                return Response({
                    'status':'failed',
                    'message':'the user is not found',
                    'code':404
                },status=status.HTTP_404_NOT_FOUND)
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
            if not user:
                return Response({
                    'status':'failed',
                    'message':'the user is not found',
                    'code':404
                },status=status.HTTP_404_NOT_FOUND)
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

class UserUpdateNamesView(APIView):
    def put(self, request, user_id):
        # Verify the requesting user is either an admin or updating their own profile
        if not request.user_data or (str(request.user_data['id']) != str(user_id) and 
                                    request.user_data.get('role') not in ['admin', 'superAdmin']):
            return Response(
                {'error': 'You can only update your own profile or need admin privileges'},
                status=status.HTTP_403_FORBIDDEN
            )

        service = UserManagementService()
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        
        # Validate at least one field is provided
        if not any([first_name, last_name]):
            return Response(
                {'error': 'At least one of first_name or last_name must be provided'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        result = service.update_user_names(
            user_id=user_id,
            first_name=first_name,
            last_name=last_name
        )
        
        if result['status'] == 'error':
            return Response(result, status=result.get('code', status.HTTP_500_INTERNAL_SERVER_ERROR))
            
        return Response(result, status=status.HTTP_200_OK)
     
