# services/recruiter_service.py
from ..models import Recruiter, RecruiterDoc,RecruiterTracking
from ..repository.recruiter_repository import (
    RecruiterRepository,
    RecruiterDocRepository,
    RecruiterTrackingRepository
)
from ..serializers import (
    RecruiterRegistrationSerializer,
    RecruiterProfileSerializer,
    RecruiterDocSerializer,
    RecruiterTrackingSerializer
)
from django.db import models
from rest_framework.exceptions import ValidationError
from typing import Optional, Dict, Any

class RecruiterService:
    def __init__(self):
        self.recruiter_repo = RecruiterRepository()
        self.doc_repo = RecruiterDocRepository()
        self.tracking_repo = RecruiterTrackingRepository()

    def register_recruiter(self, user_id: int, data: Dict[str, Any]) -> Recruiter:
        if self.recruiter_repo.get_by_user_id(user_id):
            raise ValidationError({'error': 'User already registered as recruiter'})
        
        serializer = RecruiterRegistrationSerializer(data=data)
        if not serializer.is_valid():
            raise ValidationError(serializer.errors)
        print(f"Creating recruiter profile for user_id: {user_id} with data: {serializer.validated_data}")
        return self.recruiter_repo.create(user_id=user_id, **serializer.validated_data)
    def get_recruiter_profile(self, user_id: int) -> Optional[Recruiter]:
        return self.recruiter_repo.get_by_user_id(user_id)

    def update_recruiter_profile(self, user_id: int, data: Dict[str, Any]) -> Recruiter:
        recruiter = self.recruiter_repo.get_by_user_id(user_id)
        if not recruiter:
            raise ValidationError({'error': 'Recruiter profile not found'})
        
        serializer = RecruiterProfileSerializer(instance=recruiter, data=data, partial=True)
        if not serializer.is_valid():
            raise ValidationError(serializer.errors)
        
        return self.recruiter_repo.update(instance=recruiter, **serializer.validated_data)

    def delete_recruiter_profile(self, user_id: int) -> None:
        recruiter = self.recruiter_repo.get_by_user_id(user_id)
        if not recruiter:
            raise ValidationError({'error': 'Recruiter profile not found'})
        self.recruiter_repo.delete(instance=recruiter)

class RecruiterDocService:
    def __init__(self):
        self.doc_repo = RecruiterDocRepository()
        self.recruiter_repo = RecruiterRepository()

    def create_document(self, recruiter_id: int, data: Dict[str, Any]) -> RecruiterDoc:
        serializer = RecruiterDocSerializer(data=data)
        if not serializer.is_valid():
            raise ValidationError(serializer.errors)
        return self.doc_repo.create(recruiter_id=recruiter_id, **serializer.validated_data)

    def get_documents(self, recruiter_id: int) -> models.QuerySet:
        return self.doc_repo.get_by_recruiter(recruiter_id)

    def get_document(self, doc_id: int) -> Optional[RecruiterDoc]:
        return self.doc_repo.get_by_id(doc_id)

    def update_document(self, doc_id: int, data: Dict[str, Any]) -> RecruiterDoc:
        doc = self.doc_repo.get_by_id(doc_id)
        if not doc:
            raise ValidationError({'error': 'Document not found'})
        
        serializer = RecruiterDocSerializer(instance=doc, data=data, partial=True)
        if not serializer.is_valid():
            raise ValidationError(serializer.errors)
        
        return self.doc_repo.update(instance=doc, **serializer.validated_data)

    def delete_document(self, doc_id: int) -> None:
        doc = self.doc_repo.get_by_id(doc_id)
        if not doc:
            raise ValidationError({'error': 'Document not found'})
        self.doc_repo.delete(instance=doc)

class RecruiterTrackingService:
    def __init__(self):
        self.tracking_repo = RecruiterTrackingRepository()
        self.recruiter_repo = RecruiterRepository()

    def create_tracking(self, recruiter_id: int, data: Dict[str, Any]) -> RecruiterTracking:
        serializer = RecruiterTrackingSerializer(data=data)
        if not serializer.is_valid():
            raise ValidationError(serializer.errors)
        return self.tracking_repo.create(recruiter_id=recruiter_id, **serializer.validated_data)

    def get_trackings(self, recruiter_id: int) -> models.QuerySet:
        return self.tracking_repo.get_by_recruiter(recruiter_id)

    def get_tracking(self, tracking_id: int) -> Optional[RecruiterTracking]:
        return self.tracking_repo.get_by_id(tracking_id)

    def update_tracking(self, tracking_id: int, data: Dict[str, Any]) -> RecruiterTracking:
        tracking = self.tracking_repo.get_by_id(tracking_id)
        if not tracking:
            raise ValidationError({'error': 'Tracking record not found'})
        
        serializer = RecruiterTrackingSerializer(instance=tracking, data=data, partial=True)
        if not serializer.is_valid():
            raise ValidationError(serializer.errors)
        
        return self.tracking_repo.update(instance=tracking, **serializer.validated_data)

    def delete_tracking(self, tracking_id: int) -> None:
        tracking = self.tracking_repo.get_by_id(tracking_id)
        if not tracking:
            raise ValidationError({'error': 'Tracking record not found'})
        self.tracking_repo.delete(instance=tracking)