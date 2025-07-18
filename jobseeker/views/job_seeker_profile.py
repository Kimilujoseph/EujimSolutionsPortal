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


class JobSeekerProfileView(APIView):   
    def get(self, request,user_id=None):
        
            service = ProfileService() 
            profile_data  = service.get_jobseeker_full_profile(request,user_id)
            
            profile_serializer = JobSeekerProfileSerializer(profile_data["profile"])
           
            skills_serializer = SkillSetSerializer(profile_data["skills"], many=True)

            educations_serializer = EducationSerializer(profile_data["education"], many=True)

            return Response({
                'profile': profile_serializer.data,
                'skills': skills_serializer.data,
                'educations': educations_serializer.data
            }, status=status.HTTP_200_OK)
                 
class JobSeekerAnalyticsView(APIView):
    @check_user_status
    def get(self, request,user_id=None):
        role = request.user_data.get('role');
        if user_id is None and role not in ['admin','userAdmin']:
             user_id = request.user_data.get('id') 
        if not user_id:
            return Response({'error': 'User ID is required'}, 
                          status=status.HTTP_400_BAD_REQUEST)
        try:
            user_id = int(user_id) 
            analytics = AnalyticsService.get_jobseeker_analytics(user_id)
            if not analytics:
                return Response([])
            else:
                return Response(analytics)
        except ValueError:
            return Response({'error': 'Invalid User ID'}, 
                          status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(f"Error fetching analytics: {e}")
            return Response({'error': 'Internal server error'}, 
                          status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CertificationListAPIView(APIView):
    @jobseeker_required
    def get(self, request):
        try:
            user_id = request.user_data.get('id')
            certifications = CertificationService.get_user_certifications(user_id)
            return Response(
                CertificationSerializer(certifications, many=True).data,
                status=status.HTTP_200_OK
            )
        except Exception as e:
            print(f"Error fetching certifications: {e}")
            return Response(
                {'error': 'Failed to fetch certifications'},
                status=status.HTTP_400_BAD_REQUEST
            )

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