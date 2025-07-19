# jobseeker/views/education_views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..services.education_service import EducationService
from ..serializer.education_serializer import EducationSerializer
from django.core.cache import cache
from django.db import transaction

class EducationView(APIView):
    def get(self, request):
        user_id = request.user_data.get('id')
        cache_key = f'user_educations_{user_id}'
        cached_educations = cache.get(cache_key)

        if cached_educations:
            return Response(cached_educations)

        service = EducationService()
        educations = service.get_user_educations(user_id)
        serializer = EducationSerializer(educations, many=True)
        cache.set(cache_key, serializer.data, timeout=3600) 
        return Response(serializer.data)

class EducationCreateView(APIView):
    def post(self, request):
        service = EducationService()
        user_id = request.user_data.get('id')
        serializer = EducationSerializer(data=request.data)
        
        if not serializer.is_valid():
            # Log the specific validation errors for easier debugging
            print(f"User ID: {user_id}, Education Serializer Errors: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            validated_data = serializer.validated_data
            if not isinstance(validated_data, dict):
                return Response({'error': 'Invalid data format'}, status=status.HTTP_400_BAD_REQUEST)

            education = service.create_education(user_id, validated_data)
            
            # Invalidate relevant caches upon successful creation
            def invalidate_cache_on_commit():
                cache.delete(f'user_educations_{user_id}')
                cache.delete(f'jobseeker_profile_{user_id}')
                cache.delete(f'jobseeker_analytics_{user_id}')

            transaction.on_commit(invalidate_cache_on_commit)
            
            response_serializer = EducationSerializer(education)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            # Log any other exceptions that occur during the process
            print(f"Error creating education for User ID {user_id}: {e}")
            return Response({'error': 'An unexpected error occurred.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class EducationDetailView(APIView):
    def put(self, request, education_id):
        service = EducationService()
        user_id = request.user_data.get('id')
        try:
            education = service.update_education(education_id, user_id, request.data)
            if education:
                cache.delete(f'user_educations_{user_id}')
                serializer = EducationSerializer(education)
                return Response(serializer.data)
            return Response({'error': 'Education not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, education_id):
        service = EducationService()
        user_id = request.user_data.get('id')
        if service.delete_education(education_id, user_id):
            def invalidate_cache_on_commit():
                cache.delete(f'user_educations_{user_id}')
                cache.delete(f'jobseeker_profile_{user_id}')
                cache.delete(f'jobseeker_analytics_{user_id}')

            transaction.on_commit(invalidate_cache_on_commit)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'Education not found'}, status=status.HTTP_404_NOT_FOUND)