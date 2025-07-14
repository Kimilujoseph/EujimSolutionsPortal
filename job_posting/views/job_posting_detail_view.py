from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ..services.job_posting_management_service import JobPostingManagementService
from recruiter.services.recruiter_services import  RecruiterService
from ..serializer import (
    JobPostingSerializer,
    JobPostingCreateSerializer,
)

service  = JobPostingManagementService()
recruiter_service = RecruiterService()

class JobPostingDetailView(APIView):
    def get(self, request, pk):
        job_posting = service.get_job_posting_details(pk)
        if job_posting:
            serializer = JobPostingSerializer(job_posting)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response({"detail": "Job posting not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        serializer = JobPostingCreateSerializer(data=request.data)
        if serializer.is_valid():
                updated_job = service.update_job_posting(pk, serializer.validated_data)
                return Response(JobPostingSerializer(updated_job).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
    def delete(self, request, pk):
        job_posting = service.get_job_posting_details(pk)
        user_id = request.user_data.get('id')
        recruiter_profile = recruiter_service.get_recruiter_profile(user_id)
        print(f"recruiter_profile:{job_posting.recruiter}")
        if job_posting:
            if job_posting.recruiter.id != recruiter_profile.pk:
                return Response(
                    {"detail": "You don't have permission to delete this job posting"},
                    status=status.HTTP_403_FORBIDDEN
                )
            
            service.delete_job_posting(pk)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"detail": "Job posting not found"}, status=status.HTTP_404_NOT_FOUND)
