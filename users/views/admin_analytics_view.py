# views/admin_analytics.py
from rest_framework.views import APIView
from rest_framework.response import Response
from ..services.admin_analytics_service import AdminAnalyticsService

class AdminDashboardView(APIView):  
    def get(self, request):
        service = AdminAnalyticsService()
        data = service.get_dashboard_data()
        return Response(data)