# views/recruiter_views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from ..services.recruiter_doc_service import (
    RecruiterDocService,
)
from ..services.recruiter_services import ( RecruiterService)
from ..serializers import (
    RecruiterRegistrationSerializer,
    RecruiterProfileSerializer,
    RecruiterDocSerializer,
    RecruiterTrackingSerializer
)

from ..permission import recruiter_required, recruiter_or_admin_required, check_recruiter_status


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
            recruiter_id = getattr(recruiter, 'id', None)
            if not recruiter_id:
                return Response(
                    {'error': 'Recruiter ID not found'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            docs = service.get_documents(recruiter_id)
            return Response(RecruiterDocSerializer(docs, many=True).data)
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def post(self, request):
        service = RecruiterDocService()
        try:
            user_id = request.user_data.get('id')
            recruiter = RecruiterService().get_recruiter_profile(user_id)
            if not recruiter:
                return Response(
                    {'error': 'Recruiter profile not found'},
                    status=status.HTTP_404_NOT_FOUND
                )
            recruiter_id = getattr(recruiter, 'id', None)
            if not recruiter_id:
                return Response(
                    {'error': 'Recruiter ID not found'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            if not request.content_type.startswith('multipart/form-data'):
                return Response(
                    {'error': 'Content-Type must be multipart/form-data'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            data = request.data.copy()
            data['recruiter_id'] = recruiter_id
            
            doc = service.create_document(recruiter_id, data)
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