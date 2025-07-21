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
from django.core.cache import cache
from django.db import transaction


class JobSeekerProfileView(APIView):
    @check_user_status
    def get(self, request,user_id=None):
        role = request.user_data.get('role')
        if user_id is None:
            if role not in ['admin', 'userAdmin']:
                user_id = request.user_data.get('id')
            else:
                return Response({'error': 'User ID is required for admin users.'}, status=status.HTTP_400_BAD_REQUEST)

        if not user_id:
            return Response({'error': 'Unable to identify user.'}, status=status.HTTP_400_BAD_REQUEST)

        cache_key = f'jobseeker_profile_{user_id}'
        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(cached_data, status=status.HTTP_200_OK)

        service = ProfileService()
        profile_data  = service.get_jobseeker_full_profile(request,user_id)

        profile_serializer = JobSeekerProfileSerializer(profile_data["profile"])

        skills_serializer = SkillSetSerializer(profile_data["skills"], many=True)

        educations_serializer = EducationSerializer(profile_data["education"], many=True)

        response_data = {
            'profile': profile_serializer.data,
            'skills': skills_serializer.data,
            'educations': educations_serializer.data
        }

        
        cache.set(cache_key, response_data, timeout=900)  
        return Response(response_data, status=status.HTTP_200_OK)

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
            cache_key = f'jobseeker_analytics_{user_id}'
            cached_data = cache.get(cache_key)
            if cached_data:
                return Response(cached_data)

            analytics = AnalyticsService.get_jobseeker_analytics(user_id)
            if not analytics:
                return Response([])
            else:
                cache.set(cache_key, analytics, timeout=3600)
                return Response(analytics)
        except ValueError:
            return Response({'error': 'Invalid User ID'},
                          status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(f"Error fetching analytics: {e}")
            return Response({'error': 'Internal server error'},
                          status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CertificationListAPIView(APIView):
   
    def get(self, request,user_id=None):
        try:
          
            role = request.user_data.get('role')
           # print(f"User Role: {role}")

            if role in[ 'admin','employer','superAdmin'] and user_id is not None:
               targeted_id =   user_id
            elif user_id is not None and user_id != request.user_data.get('id'):
                return Response(
                    {'error': 'Unauthorized access'},
                    status=status.HTTP_403_FORBIDDEN
                )
            else:
                targeted_id = request.user_data.get('id')
            cache_key = f'user_certifications_{targeted_id}'
            cached_data = cache.get(cache_key)
            if cached_data:
                return Response(cached_data, status=status.HTTP_200_OK)

            certifications = CertificationService.get_user_certifications(targeted_id)
            serializer = CertificationSerializer(certifications, many=True)
            cache.set(cache_key, serializer.data, timeout=3600) 
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        except Exception as e:
            print(f"Error fetching certifications: {e}")
            return Response(
                {'error': 'Failed to fetch certifications'},
                status=status.HTTP_400_BAD_REQUEST
            )

