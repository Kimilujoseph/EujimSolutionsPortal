from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..permissions import jobseeker_required, check_user_status
from ..services.recruitment_tracking_special_service import Job_seeker_recruitment_tracking_service

class Job_seeker_Recruitment_tracking(APIView):
    @jobseeker_required
    def post(self,request):

        user_id = request.user_data.get('id')
        recruitement_data = request.data
        recruitment_tracking_service = Job_seeker_recruitment_tracking_service()
        recruitment_tracking_service.create_tracking(user_id, recruitement_data)
        return Response(
            {'message': 'Recruitment tracking created successfully'},
            status=status.HTTP_201_CREATED
        )
    