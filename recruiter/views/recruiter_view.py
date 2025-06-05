# views/recruiter_views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from ..services.recruiter_services import (
    RecruiterService,
    RecruiterDocService,
    RecruiterTrackingService
)
from ..serializers import (
    RecruiterRegistrationSerializer,
    RecruiterProfileSerializer,
    RecruiterDocSerializer,
    RecruiterTrackingSerializer
)

class RecruiterRegistrationView(APIView):
    def post(self, request):
        service = RecruiterService()
        try:
            recruiter = service.register_recruiter(request.user.id, request.data)
            return Response(
                {'message': 'Registration successful, upload documents for verification'},
                status=status.HTTP_201_CREATED
            )
        except ValidationError as e:
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)

class RecruiterProfileView(APIView):
    def get(self, request):
        service = RecruiterService()
        try:
            recruiter = service.get_recruiter_profile(request.user.id)
            if not recruiter:
                return Response(
                    {'error': 'Recruiter profile not found'},
                    status=status.HTTP_404_NOT_FOUND
                )
            return Response(RecruiterProfileSerializer(recruiter).data)
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def put(self, request):
        service = RecruiterService()
        try:
            recruiter = service.update_recruiter_profile(request.user.id, request.data)
            return Response(RecruiterProfileSerializer(recruiter).data)
        except ValidationError as e:
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def delete(self, request):
        service = RecruiterService()
        try:
            service.delete_recruiter_profile(request.user.id)
            return Response(
                {'message': 'Recruiter profile deleted successfully'},
                status=status.HTTP_204_NO_CONTENT
            )
        except ValidationError as e:
            return Response(e.detail, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class RecruiterDocView(APIView):
    def get(self, request):
        service = RecruiterDocService()
        try:
            recruiter = RecruiterService().get_recruiter_profile(request.user.id)
            if not recruiter:
                return Response(
                    {'error': 'Recruiter profile not found'},
                    status=status.HTTP_404_NOT_FOUND
                )
            docs = service.get_documents(recruiter.id)
            return Response(RecruiterDocSerializer(docs, many=True).data)
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def post(self, request):
        service = RecruiterDocService()
        try:
            recruiter = RecruiterService().get_recruiter_profile(request.user.id)
            if not recruiter:
                return Response(
                    {'error': 'Recruiter profile not found'},
                    status=status.HTTP_404_NOT_FOUND
                )
            doc = service.create_document(recruiter.id, request.data)
            return Response(
                RecruiterDocSerializer(doc).data,
                status=status.HTTP_201_CREATED
            )
        except ValidationError as e:
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class RecruiterDocDetailView(APIView):
    def get(self, request, doc_id):
        service = RecruiterDocService()
        try:
            doc = service.get_document(doc_id)
            if not doc:
                return Response(
                    {'error': 'Document not found'},
                    status=status.HTTP_404_NOT_FOUND
                )
            return Response(RecruiterDocSerializer(doc).data)
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def put(self, request, doc_id):
        service = RecruiterDocService()
        try:
            doc = service.update_document(doc_id, request.data)
            return Response(RecruiterDocSerializer(doc).data)
        except ValidationError as e:
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def delete(self, request, doc_id):
        service = RecruiterDocService()
        try:
            service.delete_document(doc_id)
            return Response(
                {'message': 'Document deleted successfully'},
                status=status.HTTP_204_NO_CONTENT
            )
        except ValidationError as e:
            return Response(e.detail, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

# Similar implementations for RecruiterTrackingView and RecruiterTrackingDetailView
# Following the same pattern as above