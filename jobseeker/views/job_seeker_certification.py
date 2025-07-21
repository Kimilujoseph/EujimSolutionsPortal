from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from ..permissions import jobseeker_required, check_user_status
from ..services.certification_service import CertificationService
from ..serializer.jobSeekerSerializer import CertificationSerializer
from django.core.exceptions import ValidationError
from django.core.cache import cache
from django.db import transaction

class CertificationDetailAPIView(APIView):
    @jobseeker_required
    def get(self, request, certification_id,user_id=None):
        try:
            role = request.user_data.get('role')

            if role in[ 'admin','recruiter','superAdmin'] and user_id is not None:
               targeted_id =   user_id
            elif user_id is not None and user_id != request.user_data.get('id'):
                return Response(
                    {'error': 'Unauthorized access'},
                    status=status.HTTP_403_FORBIDDEN
                )
            else:
                targeted_id = request.user_data.get('id')
            cache_key = f'certification_{certification_id}_user_{targeted_id}'
            cached_data = cache.get(cache_key)
            if cached_data:
                return Response(cached_data, status=status.HTTP_200_OK)

            certification = CertificationService.get_certification_detail(
                user_id=targeted_id,
                certification_id=certification_id
            )
            serializer = CertificationSerializer(certification)
            cache.set(cache_key, serializer.data, timeout=3600)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        except ValidationError as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            print(f"Error fetching certification: {e}")
            return Response(
                {'error': 'Failed to fetch certification'},
                status=status.HTTP_400_BAD_REQUEST
            )

class CertificationAddAPIView(APIView):
    @jobseeker_required
    def post(self, request, *args, **kwargs):
        serializer = CertificationSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user_id = request.user_data.get('id')
            certification = CertificationService.add_certification(
                user_id=user_id,
                certification_data=serializer.validated_data
            )

            def update_cache_on_commit():
                certifications = CertificationService.get_user_certifications(user_id)
                serializer = CertificationSerializer(certifications, many=True)
                cache.set(f'user_certifications_{user_id}', serializer.data, timeout=3600)
                cache.delete(f'jobseeker_profile_{user_id}')
                cache.delete(f'jobseeker_analytics_{user_id}')

            transaction.on_commit(update_cache_on_commit)

            return Response(
                CertificationSerializer(certification).data,
                status=status.HTTP_201_CREATED
            )
        except ValidationError as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            print(f"Error creating certification: {e}")
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

class CertificationDeleteAPIView(APIView):
    @jobseeker_required
    def delete(self, request, certification_id, *args, **kwargs):
        try:
            user_id = request.user_data.get('id')
            CertificationService.delete_certification(
                user_id=user_id,
                certification_id=certification_id
            )

            def update_cache_on_commit():
                certifications = CertificationService.get_user_certifications(user_id)
                serializer = CertificationSerializer(certifications, many=True)
                cache.set(f'user_certifications_{user_id}', serializer.data, timeout=3600)
                cache.delete(f'certification_{certification_id}_user_{user_id}')
                cache.delete(f'jobseeker_profile_{user_id}')
                cache.delete(f'jobseeker_analytics_{user_id}')

            transaction.on_commit(update_cache_on_commit)

            return Response({'response':"Deleted succesfully"},status=status.HTTP_204_NO_CONTENT)
        except ValidationError as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:   
            print(f"Error deleting certification: {e}")
            return Response(
                {'error': 'Failed to delete certification'},
                status=status.HTTP_400_BAD_REQUEST
            )