# services/recruiter_service.py
from ..models import RecruiterTracking
from jobseeker.repository.jobseeker_repository import JobSeekerRepository
from ..repository.recruiter_repository import (
    RecruiterRepository,
    RecruiterTrackingRepository
)
from ..services.recruiter_tracking_base_service import BaseRecruiterTrackingService
from ..serializers import (
    RecruiterTrackingSerializer,
    RecruiterTrackingUpdateSerializer
)
from django.db import models
from rest_framework.exceptions import ValidationError
from typing import Optional, Dict, Any
from users.exceptions import InternalErrorException

class RecruiterTrackingService(BaseRecruiterTrackingService):
    def __init__(self):
        self.tracking_repo = RecruiterTrackingRepository()
        self.recruiter_repo = RecruiterRepository()
        self.job_seeker_repo = JobSeekerRepository()

    def create_tracking(self, user_id: int, data: Dict[str, Any]) -> RecruiterTracking:
        try:
             return super().create_tracking(user_id, data, "recruiter")
        except Exception as e:
             raise InternalErrorException("Internal server error")
            

    def get_trackings(self, user_id: int) -> models.QuerySet:
        recruiter = super().find_recruiter_profile(user_id)
        recruiter_id = getattr(recruiter, 'id', None)
        if not recruiter_id and not isinstance(recruiter_id, int):
            raise ValidationError({"error": "Recruiter not found"})
        return self.tracking_repo.get_by_recruiter(recruiter_id)
    def get_jobseeker_tracking(self,user_id:int) -> models.QuerySet:
        job_seeker = self.job_seeker_repo.get_by_user_id(user_id)
        if not job_seeker:
            raise ValidationError({'error': 'Job seeker profile not found'})
        job_seeker_id = getattr(job_seeker, 'id', None)
        if not job_seeker_id and not isinstance(job_seeker_id, int):
            raise ValidationError({"error": "Job seeker not found"})
        return self.tracking_repo.get_by_job_seeker(job_seeker_id)

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