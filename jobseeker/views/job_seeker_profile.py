from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from ..permissions import jobseeker_required, check_user_status
from ..services.profile_service import ProfileService
from ..services.analyticsService import AnalyticsService
from ..services.education_service import EducationService
from ..serializer.jobSeekerSerializer import JobSeekerProfileSerializer
from ..serializer.skillSerializer import SkillSetSerializer, SkillSerializer
from ..serializer.education_serializer import EducationSerializer


class JobSeekerProfileView(APIView):
  
    
    @check_user_status
    def get(self, request,user_id=None):
        try:
            service = ProfileService()
            educationService = EducationService()
            target_user_id = user_id if user_id is not None else request.user_data.get('id')     
            profile = service.get_jobseeker_profile(target_user_id)
            skills = service.get_jobseeker_skills(target_user_id)
            educations = educationService.get_user_educations(target_user_id)
            if not  target_user_id:
                return Response({'error': 'User ID is required'}, 
                              status=status.HTTP_400_BAD_REQUEST)
            target_user_id = int(target_user_id)  
            profile = service.get_jobseeker_profile(target_user_id)
            skills = service.get_jobseeker_skills(target_user_id)

            profile_serializer = JobSeekerProfileSerializer(profile)
           
            skills_serializer = SkillSetSerializer(skills, many=True)

            educations_serializer = EducationSerializer(educations, many=True)

            return Response({
                'profile': profile_serializer.data,
                'skills': skills_serializer.data,
                'educations': educations_serializer.data
            }, status=status.HTTP_200_OK)
            
        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print('Error fetching jobseeker profile:', e)
            return Response({'error': 'Internal server error'}, 
                          status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class JobSeekerCreateOrUpdateProfile(APIView):

    @jobseeker_required
    def post(self, request):
       
        try:
            user_id = request.user_data.get('id')
            profile_data = request.data
            #insert the new user_id into profile_data
            profile_data['user_id'] = user_id
            
            service = ProfileService()
            profile = service.create_or_update_profile(user_id,profile_data)
            print("Profile created/updated successfully:", profile)
            return Response(
                JobSeekerProfileSerializer(profile).data, 
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            print(f"Error creating/updating profile: {e}")
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

class JobSeekerAnalyticsView(APIView):
    @check_user_status
    def get(self, request):
        user_id = request.user_data.get('id') or request.query_params.get('user_id')
        if not user_id:
            return Response({'error': 'User ID is required'}, 
                          status=status.HTTP_400_BAD_REQUEST)
        try:
            user_id = int(user_id) 
            analytics = AnalyticsService.get_jobseeker_analytics(user_id)
            print(f"Analytics for user {user_id}: {analytics}")
            return Response(analytics)
        except ValueError:
            return Response({'error': 'Invalid User ID'}, 
                          status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(f"Error fetching analytics: {e}")
            return Response({'error': 'Internal server error'}, 
                          status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class JobSeekerDeleteSkill(APIView):
    @check_user_status
    def delete(self, request, skill_id):
        
        try:
            service = ProfileService()
            success = service.delete_skill_from_profile(
                user_id=request.user_data.get('id'),
                skill_id=skill_id
            )
            
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
        except Exception as e:
            return Response(
                {'error': 'Internal server error'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        