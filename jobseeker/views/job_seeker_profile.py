from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from ..permissions import jobseeker_required, check_user_status
from ..services.profile_service import ProfileService
from ..serializer.jobSeekerSerializer import JobSeekerProfileSerializer
from ..serializer.skillSerializer import SkillSetSerializer,SkillSerializer


class JobSeekerProfileView(APIView):
    permission_classes = [IsAuthenticated]
    
    @check_user_status
    def get(self, request):
        """Get jobseeker profile with skills"""
        try:
            service = ProfileService()
            profile = service.get_jobseeker_profile(request.user.id)
            skills = service.get_jobseeker_skills(profile.id)
            
            profile_serializer = JobSeekerProfileSerializer(profile)
            skills_serializer = SkillSetSerializer(skills, many=True)
            
            return Response({
                'profile': profile_serializer.data,
                'skills': skills_serializer.data
            }, status=status.HTTP_200_OK)
            
        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': 'Internal server error'}, 
                          status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @check_user_status
   
    def post(self, request):
        """Create or update jobseeker profile"""
        try:
            service = ProfileService()
            profile = service.create_or_update_profile(request.user.id, request.data)
            return Response(
                JobSeekerProfileSerializer(profile).data, 
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response({'error': str(e)}, 
                          status=status.HTTP_400_BAD_REQUEST)


class JobSeekerSkillsView(APIView):
    permission_classes = [IsAuthenticated]
    
    @check_user_status
    
    def get(self, request):
        """Get all skills for jobseeker"""
        try:
            service = ProfileService()
            profile = service.get_jobseeker_profile(request.user.id)
            skills = service.get_jobseeker_skills(profile.id)
            return Response(
                SkillSetSerializer(skills, many=True).data,
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response({'error': str(e)}, 
                          status=status.HTTP_400_BAD_REQUEST)

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
                
            service = ProfileService()
            profile = service.get_jobseeker_profile(request.user.id)
            skill = service.add_skill_to_profile(profile.id, request.data)
            
            return Response(
                SkillSetSerializer(skill).data,
                status=status.HTTP_201_CREATED
            )
        except ValueError as e:
            return Response({'error': str(e)}, 
                          status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': 'Internal server error'}, 
                          status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SkillListView(APIView):
    permission_classes = [IsAuthenticated]
    
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