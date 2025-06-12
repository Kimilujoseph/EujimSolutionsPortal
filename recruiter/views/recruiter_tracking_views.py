# views/recruiter_tracking_views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError
from ..services.recruiter_tracking_service import RecruiterTrackingService
from ..serializers import (
    RecruiterTrackingSerializer,
)


class RecruiterTrackingListView(APIView):
    def get(self, request,user_id=None):
        service = RecruiterTrackingService()
        user_id = request.user_data.get('id') or user_id       
        if not user_id or not isinstance(user_id, int):
            return Response(
                {'error': 'Invalid or missing user ID'},
                status=status.HTTP_400_BAD_REQUEST
            )
        if not user_id:
            return Response(
                {'error': 'User ID not found'},
                status=status.HTTP_400_BAD_REQUEST
            )
        trackings = service.get_trackings(user_id)
        serializer = RecruiterTrackingSerializer(trackings, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        service = RecruiterTrackingService()
        try:
            user_id = request.user_data.get('id');
            if not request.data:
                return Response(
                    {'error':'no data provided'},
                    status = status.HTTP_400_BAD_REQUEST
                )
            request_data = request.data.copy()
            request_data['recruiter_id'] = user_id
            tracking = service.create_tracking(
                user_id=user_id,
                data=request.data
            )
            serializer = RecruiterTrackingSerializer(tracking)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

class RecruiterTrackingDetailView(APIView):
   
    
    def get(self, request, tracking_id):
        service = RecruiterTrackingService()
        try:
            tracking = service.get_tracking(tracking_id)
            if not tracking:
                return Response(
                    {'error': 'Tracking record not found'},
                    status=status.HTTP_404_NOT_FOUND
                )
            serializer = RecruiterTrackingSerializer(tracking)
            return Response(serializer.data)
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def put(self, request, tracking_id):
        service = RecruiterTrackingService()
        try:
            tracking = service.update_tracking(
                tracking_id=tracking_id,
                data=request.data
            )
            serializer = RecruiterTrackingSerializer(tracking)
            return Response(serializer.data)
        except ValidationError as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def delete(self, request, tracking_id):
        service = RecruiterTrackingService()
        try:
            service.delete_tracking(tracking_id)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ValidationError as e:
            return Response(e, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )