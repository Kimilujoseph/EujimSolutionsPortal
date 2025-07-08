# views/recruiter_views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from ..services.recruiter_services import (
    RecruiterService
)
from ..serializers import (
    RecruiterProfileSerializer,
    
)

class RecruiterRegistrationView(APIView):
    def post(self, request):
        service = RecruiterService()
        try:
            recruiter = service.register_recruiter(request.user.id, request.data)
            return Response(
                {'message': 'Registration successful, upload documents for verification'},
                status=status.HTTP_201_CREATED
            )
        except ValidationError as e:
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)

class RecruiterProfileView(APIView):
    def get(self, request):
        service = RecruiterService()
        try:
            recruiter = service.get_recruiter_profile(request.user.id)
            if not recruiter:
                return Response(
                    {'error': 'Recruiter profile not found'},
                    status=status.HTTP_404_NOT_FOUND
                )
            return Response(RecruiterProfileSerializer(recruiter).data)
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def put(self, request):
        service = RecruiterService()
        role = request.user_data.get('role')
        recruiter = service.update_recruiter_profile(request.user.id, request.data,role=role)
        return Response(RecruiterProfileSerializer(recruiter).data,status=status.HTTP_200_OK)
       
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

