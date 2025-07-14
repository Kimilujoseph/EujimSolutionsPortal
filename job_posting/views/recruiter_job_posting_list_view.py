from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializer import JobPostingListSerializer
from ..permission import recruiter_or_admin_required
from ..services.job_posting_management_service import JobPostingManagementService

service = JobPostingManagementService()

class RecruiterJobPostingListView(APIView):
    @recruiter_or_admin_required
    def get(self, request, recruiter_id=None):
        role = request.user_data.get('role')
        request_user_id = request.user_data.get('id')
        if role in ['admin','superAdmin']:
            targeted_id = recruiter_id if recruiter_id is not None else request_user_id
        else:
            if recruiter_id is not None and request_user_id != recruiter_id:
                return Response(
                    {'error':'unauthorsied'},
                    status=status.HTTP_403_FORBIDDEN
                )
            targeted_id = request_user_id

        job_postings = service.get_job_postings_by_recruiter(targeted_id)
        serializer = JobPostingListSerializer(job_postings, many=True)
        print(f"data returned:{serializer.data}")
        return Response(serializer.data, status=status.HTTP_200_OK)
