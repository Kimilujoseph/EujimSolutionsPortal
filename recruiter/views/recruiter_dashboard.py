from django.core.cache import cache
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import timedelta
import time
from ..services.recruiter_analytics_service import RecruiterAnalyticsService
from ..services.recruiter_services import RecruiterService

class RecruiterDashboardView(APIView):
    CACHE_TIMEOUT = 900
    
    def get_cache_key(self, recruiter_id):
        return f'recruiter_dashboard_{recruiter_id}'
    
    def get(self, request,user_id=None):
        service = RecruiterService()
        
        employer_profile = service.get_recruiter_profile(request,user_id)

        cache_key = self.get_cache_key(employer_profile.pk)
        cached_data = cache.get(cache_key)       
        if cached_data and cached_data.get('cache_time', 0) > employer_profile.updateAt.timestamp():
            return Response({
                'data': cached_data['data'], 
                'cached': True
            }, status=status.HTTP_200_OK)
        analytics_service = RecruiterAnalyticsService(employer_profile.pk)
        fresh_data = analytics_service.get_dashboard_data()
        cache.set(cache_key, {
            'data': fresh_data,
            'cache_time': time.time()  # Current timestamp
            }, timeout=self.CACHE_TIMEOUT)      
        return Response({
            'data': fresh_data,
            'cached': False
        }, status=status.HTTP_200_OK)