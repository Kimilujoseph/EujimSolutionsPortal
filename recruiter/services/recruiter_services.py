# services/recruiter_service.py
from ..models import Recruiter, RecruiterDoc,RecruiterTracking
from ..repository.recruiter_repository import (
    RecruiterRepository,
)
from django.db import DatabaseError,IntegrityError
from ..serializers import (
    RecruiterRegistrationSerializer,
    RecruiterProfileSerializer,
)
from django.db import models
from rest_framework.exceptions import ValidationError
from typing import Optional, Dict, Any
from users.exceptions import (NotFoundException,InternalErrorException,BadRequestException)
class RecruiterService:
    def __init__(self):
        self.recruiter_repo = RecruiterRepository()
        
    def register_recruiter(self, user_id: int, data: Dict[str, Any]) -> Recruiter:
        if self.recruiter_repo.get_by_user_id(user_id):
            raise ValidationError({'error': 'User already registered as recruiter'})
        serializer = RecruiterRegistrationSerializer(data=data)
        if not serializer.is_valid():
            raise ValidationError(serializer.errors)
        if not isinstance(serializer.validated_data, dict):
            raise ValidationError({'error': 'Validated data is not a valid dictionary'})
        return self.recruiter_repo.create(user_id=user_id,**serializer.validated_data)
    def get_recruiter_profile(self,request,user_id=None) -> Optional[Recruiter]:
        try:
            if not hasattr(request, 'user_data'):
              raise BadRequestException("Invalid request object")
            if request.user_data.get('role') not in ['admin','superAdmin']:
               user_id=request.user_data.get('id')
            if not user_id and not isinstance(user_id,int):
                raise NotFoundException("bad request")
            recruiter = self.recruiter_repo.get_recruiter_with_profile(user_id)
            if not recruiter:
                raise NotFoundException("recruiter profile not found")
            return recruiter 
        except DatabaseError:
            raise InternalErrorException("error when accessing the database")
        except ValidationError:
            raise BadRequestException("bad request")
        except Exception as e:
            raise InternalErrorException(e)
    def update_recruiter_profile(self, user_id: int, data: Dict[str, Any],role:str) -> Recruiter:
        recruiter = self.recruiter_repo.get_by_user_id(user_id)
        if not recruiter:
            raise ValidationError({'error': 'Recruiter profile not found'})
        
        serializer = RecruiterProfileSerializer(instance=recruiter, data=data,partial=True,role=role)
        if not serializer.is_valid():
            raise ValidationError(serializer.errors)
        
        validated_data = serializer.validated_data
        if not isinstance(validated_data, dict):
            raise ValidationError({'error': 'Validated data is not a valid dictionary'})
        return self.recruiter_repo.update(instance=recruiter, **validated_data)
    
    def delete_recruiter_profile(self, user_id: int) -> None:
        recruiter = self.recruiter_repo.get_by_user_id(user_id)
        if not recruiter:
            raise ValidationError({'error': 'Recruiter profile not found'})
        self.recruiter_repo.delete(instance=recruiter)



