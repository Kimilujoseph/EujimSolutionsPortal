# services/recruiter_service.py
from ..models import Recruiter, RecruiterDoc,RecruiterTracking
from ..repository.recruiter_repository import (
    RecruiterRepository,
)
from ..serializers import (
    RecruiterRegistrationSerializer,
    RecruiterProfileSerializer,
)
from django.db import models,DatabaseError
from rest_framework.exceptions import ValidationError
from typing import Optional, Dict, Any
from users.exceptions import ServiceException,InternalErrorException,NotFoundException
from ..services.recruiter_tracking_base_service import BaseRecruiterTrackingService
class RecruiterService(BaseRecruiterTrackingService):
    def __init__(self):
        self.recruiter_repo = RecruiterRepository()
        
    def register_recruiter(self, user_id: int, data: Dict[str, Any]) -> Recruiter:
        try:
            try:
                 if super().find_recruiter_profile(user_id):
                   raise ValidationError({'User already registered as recruiter'})
            except NotFoundException:
                pass
            serializer = RecruiterRegistrationSerializer(data=data)
            if not serializer.is_valid():
                raise ValidationError(serializer.errors)
            if not isinstance(serializer.validated_data, dict):
                raise ValidationError({'error': 'Validated data is not a valid dictionary'})
            return self.recruiter_repo.create(user_id=user_id,**serializer.validated_data)
        except ValidationError as e:
            error_found = e.detail
            raise ServiceException(error_found)
    def get_recruiter_profile(self, user_id: int) -> Optional[Recruiter]:
        try:
            return self.recruiter_repo.get_recruiter_with_profile(user_id)
        except (Recruiter.DoesNotExist):
            raise NotFoundException("recruiter profile not found")
        except Exception as e:
            raise InternalErrorException("internal server error")

    def update_recruiter_profile(self, user_id: int, data: Dict[str, Any],role:str) -> Recruiter:
        try:
           
           recruiter = super().find_recruiter_profile(user_id)
           
           serializer = RecruiterProfileSerializer(instance=recruiter, data=data,partial=True,role=role)
           if not serializer.is_valid():
                raise ValidationError(serializer.errors)
            
           validated_data = serializer.validated_data
           if not isinstance(validated_data, dict):
                raise ValidationError({'error': 'Validated data is not a valid dictionary'})
           return self.recruiter_repo.update(instance=recruiter, **validated_data)
        except NotFoundException as e:
            raise NotFoundException("recruiter profile not found")
        except ValidationError as e:
            error_found = e.detail
            raise ValidationError(error_found)
        except DatabaseError as e:
            raise InternalErrorException("internal server error")  
        except Exception as e:
            raise InternalErrorException("Internal server error")
        
        
    def delete_recruiter_profile(self, user_id: int) -> None:
       try:
            recruiter = super().find_recruiter_profile(user_id)
            self.recruiter_repo.delete(instance=recruiter)
       except NotFoundException:
           raise NotFoundException("recruiter profile not found")
       except DatabaseError as e:
           raise InternalErrorException("failed to delete the recruite profile")
       except Exception as e:
           raise InternalErrorException("internal server error")


