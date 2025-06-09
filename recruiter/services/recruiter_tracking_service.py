# services/recruiter_service.py
from ..models import RecruiterTracking
from ..repository.recruiter_repository import (
    RecruiterRepository,
    RecruiterTrackingRepository
)
from ..serializers import (
    RecruiterTrackingSerializer,
    RecruiterTrackingUpdateSerializer
)
from django.db import models
from rest_framework.exceptions import ValidationError
from typing import Optional, Dict, Any


class RecruiterTrackingService:
    def __init__(self):
        self.tracking_repo = RecruiterTrackingRepository()
        self.recruiter_repo = RecruiterRepository()

    def create_tracking(self, user_id: int, data: Dict[str, Any]) -> RecruiterTracking:
        serializer = RecruiterTrackingSerializer(data=data)
        recruiter = self.recruiter_repo.get_by_user_id(user_id);
        if not recruiter:
            raise ValidationError({'error':'recruiter profile not found'})
        recruiter_id = getattr(recruiter,'id',None)
        if not recruiter_id:
            raise ValidationError({"error":"recruter not found"})
        if not serializer.is_valid():
            raise ValidationError(serializer.errors)
        if not isinstance(serializer.validated_data,dict):
            raise ValidationError({'error':'incorrect data format passed'})
        return self.tracking_repo.create(recruiter_id=recruiter_id, **serializer.validated_data)

    def get_trackings(self, user_id: int) -> models.QuerySet:
        recruiter = self.recruiter_repo.get_by_user_id(user_id)
        if not recruiter:
            raise ValidationError({'error': 'Recruiter profile not found'})
        recruiter_id = getattr(recruiter, 'id', None)
        if not recruiter_id and not isinstance(recruiter_id, int):
            raise ValidationError({"error": "Recruiter not found"})
        return self.tracking_repo.get_by_recruiter(recruiter_id)

    def get_tracking(self, tracking_id: int) -> Optional[RecruiterTracking]:
        return self.tracking_repo.get_tracking_by_id(tracking_id)

    def update_tracking(self, tracking_id: int, data: Dict[str, Any]) -> RecruiterTracking:
       tracking = self.tracking_repo.get_by_id(tracking_id)
       if not tracking:
            raise ValidationError({'error': 'Tracking record not found'})
       serializer = RecruiterTrackingUpdateSerializer(
            instance=tracking, 
            data=data, 
            partial=True
        )
        
       if not serializer.is_valid():
            raise ValidationError(serializer.errors)
    
       try:
            if not isinstance(serializer.validated_data,dict):
                raise ValidationError({'error':'invalid data received'})
            return self.tracking_repo.update(
                instance=tracking,
                **serializer.validated_data
            )
       except Exception as e:
            raise ValidationError({'error': f'Update failed: {str(e)}'})

    def delete_tracking(self, tracking_id: int) -> None:
        tracking = self.tracking_repo.get_by_id(tracking_id)
        if not tracking:
            raise ValidationError({'error': 'Tracking record not found'})
        self.tracking_repo.delete(instance=tracking)