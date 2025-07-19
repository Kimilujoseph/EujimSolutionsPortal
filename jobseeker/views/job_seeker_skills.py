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
from django.db import transaction
from django.core.cache import cache

class JobSeekerSkillsView(APIView):

    @check_user_status
    def get(self, request):
        """Get all skills for jobseeker"""
        try:
            service = ProfileService()
            profile = service.get_jobseeker_profile(request.user.id)
            skills = service.get_jobseeker_skills(profile.pk)
            return Response(
                SkillSetSerializer(skills, many=True).data,
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response({'error': str(e)}, 
                          status=status.HTTP_400_BAD_REQUEST)


class JobSeekerUpdateSkill(APIView):
       
    @check_user_status
    def post(self, request):
        """Add skill to jobseeker profile"""
        try:
            required_fields = ['skill_name']
            if not all(field in request.data for field in required_fields):
                return Response(
                    {'error': f'Required fields: {", ".join(required_fields)}'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            user_id = request.user_data.get('id')
            if not user_id:
                return Response({'error': 'User ID is required'}, 
                              status=status.HTTP_400_BAD_REQUEST)
                
            service = ProfileService()
            skill = service.add_skill_to_profile(user_id, request.data)
            def update_cache_on_commit():
                cache.delete(f'jobseeker_profile_{user_id}')
                cache.delete(f'jobseeker_analytics_{user_id}')

            transaction.on_commit(update_cache_on_commit)
            return Response(
                SkillSetSerializer(skill).data,
                status=status.HTTP_201_CREATED
            )
        except ValueError as e:
            return Response({'error': str(e)}, 
                          status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(f"Error adding skill: {e}")
            return Response({'error': 'Internal server error'}, 
                          status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SkillListView(APIView):
    
    @check_user_status
    def get(self, request):
        """Get all available skills"""
        try:
            service = ProfileService()
            skills = service.skill_repo.get_all()
            return Response(
                SkillSerializer(skills, many=True).data,
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response({'error': str(e)}, 
                          status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class JobSeekerDeleteSkill(APIView):
    @check_user_status
    def delete(self, request, skill_id):
        user_id = request.user_data.get('id')
        try:
            service = ProfileService()
            success = service.delete_skill_from_profile(
                user_id=user_id,
                skill_id=skill_id
            )
            def update_cache_on_commit():
                cache.delete(f'jobseeker_profile_{user_id}')
                cache.delete(f'jobseeker_analytics_{user_id}')

            transaction.on_commit(update_cache_on_commit)
            
            if success:
                return Response(
                    {'message': 'Skill removed successfully'},
                    status=status.HTTP_204_NO_CONTENT
                )
            return Response(
                {'error': 'Skill not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
        
