from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from ..permissions import jobseeker_required, check_user_status
from ..services.profile_service import ProfileService
from ..services.analyticsService import AnalyticsService
from ..services.education_service import EducationService
from ..services.certification_service import CertificationService
from ..serializer.jobSeekerSerializer import JobSeekerProfileSerializer,JobSeekerUpdateSerializer, CertificationSerializer
from ..serializer.skillSerializer import SkillSetSerializer, SkillSerializer
from ..serializer.education_serializer import EducationSerializer
from django.core.exceptions import ValidationError

class CertificationDetailAPIView(APIView):
    @jobseeker_required
    def get(self, request, certification_id):
        try:
            user_id = request.user_data.get('id')
            certification = CertificationService.get_certification_detail(
                user_id=user_id,
                certification_id=certification_id
            )
            return Response(
                CertificationSerializer(certification).data,
                status=status.HTTP_200_OK
            )
        except ValidationError as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            print(f"Error fetching certification: {e}")
            return Response(
                {'error': 'Failed to fetch certification'},
                status=status.HTTP_400_BAD_REQUEST
            )

class CertificationAddAPIView(APIView):
    def post(self, request, *args, **kwargs):
        print("Current user:", request.user_data)  # Debugging
        
        serializer = CertificationSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            certification = CertificationService.add_certification(
                user_id=request.user_data.get('id'),  # Pass raw user ID directly
                certification_data=serializer.validated_data
            )
            return Response(
                CertificationSerializer(certification).data,
                status=status.HTTP_201_CREATED
            )
        except ValidationError as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            print(f"Error creating certification: {e}")
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

class CertificationDeleteAPIView(APIView):
    def delete(self, request, certification_id, *args, **kwargs):
        try:
            CertificationService.delete_certification(
                user_id=request.user_data.get('id'),  # Pass raw user ID
                certification_id=certification_id
            )
            return Response({'response':"Deleted succesfully"},status=status.HTTP_204_NO_CONTENT)
        except ValidationError as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_404_NOT_FOUND
            )