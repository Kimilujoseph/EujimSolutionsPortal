# services/recruiter_service.py
from ..models import Recruiter, RecruiterDoc,RecruiterTracking
from ..repository.recruiter_repository import (
    RecruiterRepository,
)
from ..serializers import (
    RecruiterRegistrationSerializer,
    RecruiterProfileSerializer,
)
from django.db import models
from rest_framework.exceptions import ValidationError
from typing import Optional, Dict, Any

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
    def get_recruiter_profile(self, user_id: int) -> Optional[Recruiter]:
        print(user_id)
        return self.recruiter_repo.get_recruiter_with_profile(user_id)

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



