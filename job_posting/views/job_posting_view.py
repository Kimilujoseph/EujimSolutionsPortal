from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from ..services.job_posting_services import JobPostingService
from recruiter.services.recruiter_services import  RecruiterService
from ..serializer import (
    JobPostingSerializer,
    JobPostingCreateSerializer,
    JobPostingSkillSerializer,JobPostingListSerializer
)
from ..permission import recruiter_required,recruiter_or_admin_required
from django.core.cache import cache

service  = JobPostingService()
recruiter_service = RecruiterService()

class JobPostingListView(APIView):
    def get(self, request):
        page_number = request.query_params.get('page', 1)
        page_size = request.query_params.get('limit', 10)
        
        cache_key = f'job_postings_page_{page_number}_size_{page_size}'
        cached_data = cache.get(cache_key)

        if cached_data:
            return Response(cached_data)

        job_postings, total_count = service.get_paginated_job_postings(
            page_number=int(page_number),
            page_size=int(page_size)
        )
        
        serializer = JobPostingListSerializer(job_postings, many=True)
        
        response_data = {
            'count': total_count,
            'page': int(page_number),
            'page_size': int(page_size),
            'results': serializer.data
        }
        
        cache.set(cache_key, response_data, timeout=60 * 15) # cache for 15 minutes
        
        return Response(response_data)
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
    
class JobPostingAddingRequiredSkills(APIView):
    @recruiter_required
    def post(self,request,job_posting_id):
        if not request.data or not isinstance(request.data,dict):
            Response({"details":"please provide valid skill data"},status=status.HTTP_400_BAD_REQUEST)
        serializer = JobPostingSkillSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        print(serializer.validated_data)  
        skillAdded = service.add_required_skills(job_posting_id,serializer.validated_data)
        return Response({"sucessfully added the course"},status=status.HTTP_200_OK)
    def delete(self,request,job_posting_id,skill_id):
        if not job_posting_id or not skill_id:
            return Response({"details":"please provide valid job posting id and skill id"},status=status.HTTP_400_BAD_REQUEST)
        service.delete_required_skill(job_posting_id,skill_id)
        return Response({"details":"sucessfully deleted the skill from the job posting"},status=status.HTTP_200_OK)

