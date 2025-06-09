# views/jobseeker_search_views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .search_service import JobSeekerSearchService
from .search_serializer import JobSeekerSearchSerializer


class JobSeekerSearchView(APIView):
  
    
    def get(self, request):
        skill_names = request.query_params.get('skills', '').split(',')
        min_proficiency = request.query_params.get('proficiency')
        
        if not skill_names:
            return Response(
                {'error': 'At least one skill is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        results = JobSeekerSearchService.search_by_skills(
            skill_names=skill_names,
            min_proficiency=min_proficiency
        )

        if not results:
            return Response(
                {'message': 'No job seekers found'},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = JobSeekerSearchSerializer(results, many=True)
        return Response(serializer.data)