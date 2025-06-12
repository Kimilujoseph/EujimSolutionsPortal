# views/recruiter_views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from django.core.cache import cache
from ..services.recruiter_doc_service import (
    RecruiterDocService,
)
from django.conf import settings
from ..services.recruiter_services import ( RecruiterService)
from ..serializers import (
    RecruiterDocSerializer,
    RecruiterDocVerificationSerializer
)

from ..permission import recruiter_required, recruiter_or_admin_required, check_recruiter_status
from django.http import FileResponse, Http404
from django.utils.encoding import smart_str
from django.utils.timezone import now
import os
  
class RecruiterDocView(APIView):
  def get(self, request, user_id=None):
    service = RecruiterDocService()
    try:
        role = request.user_data.get('role');
        if user_id is None and role not in ['admin','superAdmin']:
             user_id = request.user_data.get('id')
        if not user_id:
            return Response(
                {'error': 'User ID not found'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
       
        cache_key = f'recruiter_docs_{user_id}'
   
        cached_docs = cache.get(cache_key)
        if cached_docs and not settings.DEBUG:  # Skip cache in debug mode
            return Response(cached_docs)
        
        # Not in cache or debug mode - fetch from DB
        recruiter = RecruiterService().get_recruiter_profile(user_id)
        if not recruiter:
            return Response(
                {'error': 'Recruiter profile not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        recruiter_id = getattr(recruiter, 'id', None)
        if recruiter_id is None:
            return Response(
                {'error': 'Recruiter ID not found'},
                status=status.HTTP_400_BAD_REQUEST
            )        
        docs = service.get_documents(recruiter_id)
        if not docs:
            return Response(
                {'message': 'No documents found'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = RecruiterDocSerializer(docs, many=True,context={'request': request})
        
        # Cache for 1 hour (3600 seconds)
        cache.set(cache_key, serializer.data, timeout=3600)
        
        return Response(serializer.data)
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

  def delete(self, request, doc_id=None):
        service = RecruiterDocService()
        try:
            if doc_id is None:
                return Response(
                    {'error': 'Document ID is required'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            print(doc_id)
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


class RecruiterDocDowload(APIView):
      def get(self, request, doc_id):
        service = RecruiterDocService()
        if not doc_id:
            return Response(
                {'error': 'Document ID is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            cache_key = f'document_{doc_id}_download'
            cached_file_path = cache.get(cache_key)

            if cached_file_path and os.path.exists(cached_file_path):
                response = FileResponse(open(cached_file_path, 'rb'), as_attachment=True)
                response['Content-Disposition'] = f'attachment; filename="{smart_str(os.path.basename(cached_file_path))}"'
                return response

           
            doc = service.get_document(doc_id)
            if not doc or not doc.upload_path:
                return Response(
                    {'error': 'Document not found or no file associated'},
                    status=status.HTTP_404_NOT_FOUND
                )

            file_path = doc.upload_path.path 
            if not os.path.exists(file_path):
                raise Http404('File not found')
            cache.set(cache_key, file_path, timeout=3600) 

        
            response = FileResponse(open(file_path, 'rb'), as_attachment=True)
            response['Content-Disposition'] = f'attachment; filename="{smart_str(os.path.basename(file_path))}"'
            return response
        except Http404:
            return Response(
                {'error': 'File not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
class RecruiterDocVerificationView(APIView):
    def put(self, request, doc_id):
        service = RecruiterDocService()
        try:
            # Check if user is admin
            if not request.user_data.get('role') in ['admin', 'superAdmin']:
                return Response(
                    {'error': 'Admin privileges required'},
                    status=status.HTTP_403_FORBIDDEN
                )
            
            # Validate only status update is allowed
            serializer = RecruiterDocVerificationSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            if not isinstance(serializer.validated_data,dict):
                return Response(
                    {'error': 'Status must be a string'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            verification_data = {
                'status': serializer.validated_data['status'],
                'verifiedBy': request.user_data.get('id'),
                'verifiedAt': now()
            }
            
            # Update document
            doc = service.update_document(doc_id, verification_data)
            return Response(RecruiterDocSerializer(doc).data)
            
        except ValidationError as e:
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )