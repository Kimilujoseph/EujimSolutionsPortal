# views/recruiter_views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from ..services.recruiter_services import (
    RecruiterService,
)
from ..serializers import (
    RecruiterProfileSerializer,
   
)
from ..permission import recruiter_required,recruiter_or_admin_required,check_recruiter_status

class RecruiterRegistrationView(APIView):
    @recruiter_required
    @check_recruiter_status
    def post(self, request):
        service = RecruiterService()
        try:
            user_id = request.user_data.get('id')
            if not user_id:
                return Response(
                    {'error': 'User ID not found in request data'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            recruiter = service.register_recruiter(user_id, request.data)
            return Response(
                {'message': 'Registration successful, upload documents for verification'},
                status=status.HTTP_201_CREATED
            )
        except ValidationError as e:
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)

class RecruiterProfileView(APIView):
    @recruiter_or_admin_required
    def get(self, request,user_id):
        service = RecruiterService()
        try:
            role = request.user_data.get('role')
            if role == 'admin' or 'superAdmin':
                user_id = user_id
            else:
                user_id = request.user_data.get('id')
            if not user_id:
                return Response(
                    {'error': 'User ID not found in request data'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            recruiter = service.get_recruiter_profile(user_id)
            if not recruiter:
                return Response(
                    {'error': 'Recruiter profile not found'},
                    status=status.HTTP_404_NOT_FOUND
                )
            
            serializer = RecruiterProfileSerializer(recruiter)
            return Response(serializer.data) 
        except Exception as e:
            print(f"Error retrieving recruiter profile: {str(e)}")
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @recruiter_or_admin_required
    def put(self, request,user_id):
        service = RecruiterService()
        try:
            role = request.user_data.get('role')
            if role == 'admin' or 'superAdmin':
                user_id = user_id
            else:
                user_id = request.user_data.get('id')
            if not user_id:
                return Response(
                    {'error': 'User ID not found in request data'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            if not request.data:
                return Response(
                    {'error': 'No data provided for update'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            recruiter = service.update_recruiter_profile(user_id, request.data,role)
            return Response(RecruiterProfileSerializer(recruiter).data)
        except ValidationError as e:
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    @recruiter_required
    def delete(self, request):
        service = RecruiterService()
        try:
            service.delete_recruiter_profile(request.user.id)
            return Response(
                {'message': 'Recruiter profile deleted successfully'},
                status=status.HTTP_204_NO_CONTENT
            )
        except ValidationError as e:
            return Response(e.detail, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

