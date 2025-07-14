from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.cache import cache
from ..services.job_posting_management_service import JobPostingManagementService
from ..serializer import JobPostingListSerializer

service = JobPostingManagementService()

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
