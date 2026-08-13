from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from ..services.admin_analytics_service import AdminAnalyticsService

class AdminDashboardView(APIView):  
    CACHE_KEY = 'admin_dashboard_analytics'
    CACHE_TIMEOUT = 900  # 15 minutes

    def get(self, request):
        try:
            force_refresh = request.query_params.get('refresh', '').lower() == 'true'
            if not force_refresh:
                cached_data = cache.get(self.CACHE_KEY)
                if cached_data is not None:
                    return Response(cached_data, status=status.HTTP_200_OK)

            service = AdminAnalyticsService()
            data = service.get_dashboard_data()
            cache.set(self.CACHE_KEY, data, timeout=self.CACHE_TIMEOUT)
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            print(f"Error in AdminDashboardView: {str(e)}")
            return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)