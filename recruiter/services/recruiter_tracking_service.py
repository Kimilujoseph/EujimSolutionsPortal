# services/recruiter_service.py
from ..models import RecruiterTracking
from ..repository.recruiter_repository import (
    RecruiterRepository,
    RecruiterTrackingRepository
)
from ..serializers import (
    RecruiterTrackingSerializer
)
from django.db import models
from rest_framework.exceptions import ValidationError
from typing import Optional, Dict, Any


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