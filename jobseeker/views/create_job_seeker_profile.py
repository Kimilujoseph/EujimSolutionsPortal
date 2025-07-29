from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..permissions import jobseeker_required, check_user_status
from ..services.profile_service import ProfileService
from ..serializer.jobSeekerSerializer import JobSeekerProfileSerializer
from django.core.exceptions import ValidationError
from django.core.cache import cache

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
            
            # Invalidate the cache for the updated profile
            cache_key = f'jobseeker_profile_{user_id}'
            cache.delete(cache_key)
            
            print("Profile created/updated successfully:", profile)
            return Response(
                JobSeekerProfileSerializer(profile).data, 
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            print(f"Error creating/updating profile: {e}")
            return Response({'error': str(e)}, 
                          status=status.HTTP_400_BAD_REQUEST)
