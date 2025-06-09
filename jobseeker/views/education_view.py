# jobseeker/views/education_views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..services.education_service import EducationService
from ..serializer.education_serializer import EducationSerializer

class EducationView(APIView):
    def get(self, request):
        service = EducationService()
        user_id = request.user_data.get('id')
        educations = service.get_user_educations(user_id)
        serializer = EducationSerializer(educations, many=True)
        return Response(serializer.data)

class EducationCreateView(APIView):
    def post(self, request):
        service = EducationService()
        user_id = request.user_data.get('id')
        serializer = EducationSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            education = service.create_education(user_id, serializer.validated_data)
            response_serializer = EducationSerializer(education)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(f"Error creating education: {e}")
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class EducationDetailView(APIView):
    def put(self, request, education_id):
        service = EducationService()
        user_id = request.user_data.get('id')
        try:
            education = service.update_education(education_id, user_id, request.data)
            if education:
                serializer = EducationSerializer(education)
                return Response(serializer.data)
            return Response({'error': 'Education not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, education_id):
        service = EducationService()
        user_id = request.user_data.get('id')
        if service.delete_education(education_id, user_id):
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'Education not found'}, status=status.HTTP_404_NOT_FOUND)