from django.core.cache import cache
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import timedelta
from ..services.recruiter_analytics_service import RecruiterAnalyticsService
from ..services.recruiter_services import RecruiterService

class RecruiterDashboardView(APIView):
    CACHE_TIMEOUT = 900
    
    def get_cache_key(self, recruiter_id):
        return f'recruiter_dashboard_{recruiter_id}'
    
    def get(self, request):
        service = RecruiterService()
        try:
            user_id = request.user_data.get('id')
            if not user_id:
                return Response({'error': 'Please login and try again'}, 
                              status=status.HTTP_404_NOT_FOUND)
            
            employer_profile = service.get_recruiter_profile(user_id)
            if not employer_profile:
                return Response({'error': 'Employer profile not found'}, 
                              status=status.HTTP_404_NOT_FOUND)
            
          
            cache_key = self.get_cache_key(employer_profile.pk)
            
           
            cached_data = cache.get(cache_key)
            if cached_data is not None:
                return Response({'data': cached_data, 'cached': True}, 
                              status=status.HTTP_200_OK)
            
            
            analytics_service = RecruiterAnalyticsService(employer_profile.pk)
            analytics = analytics_service.get_dashboard_data()
            
           
            cache.set(cache_key, analytics, timeout=self.CACHE_TIMEOUT)
            
            return Response({'data': analytics, 'cached': False}, 
                          status=status.HTTP_200_OK)

        except ValidationError as e:
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(f"Error in RecruiterDashboardView: {str(e)}")
            return Response({'error': 'Internal server error'}, 
                          status=status.HTTP_500_INTERNAL_SERVER_ERROR)