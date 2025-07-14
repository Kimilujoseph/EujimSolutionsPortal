from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ..services.job_posting_management_service import JobPostingManagementService as JobPostingService
from ..serializer import (
    JobPostingSerializer,
    JobPostingCreateSerializer,
)
from ..permission import recruiter_required

service  = JobPostingService()

class JobPostingCreateView(APIView):
    @recruiter_required
    def post(self, request):
        serializer = JobPostingCreateSerializer(data=request.data)
        if not serializer.is_valid():        
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        if not isinstance(serializer.validated_data,dict):
            return Response(
                {"detail": "Invalid data format"},
                status=status.HTTP_400_BAD_REQUEST
            )
        job_posting = service.create_job_posting(
                request=request,
                data=serializer.validated_data
            )
        return Response(JobPostingSerializer(job_posting).data, status=status.HTTP_201_CREATED)
  