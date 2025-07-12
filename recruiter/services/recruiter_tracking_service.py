# services/recruiter_service.py
from ..models import RecruiterTracking,Recruiter
from jobseeker.models import JobSeeker
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
from django.db.models import QuerySet
from django.db  import DatabaseError
from django.core.exceptions import ValidationError
from users.exceptions import NotFoundException,ServiceException,InternalErrorException
import logging

logger  = logging.getLogger(__name__)
class RecruiterTrackingService(BaseRecruiterTrackingService):
    def __init__(self):
        self.tracking_repo = RecruiterTrackingRepository()
        self.recruiter_repo = RecruiterRepository()
        self.job_seeker_repo = JobSeekerRepository()
        self.role = "recruiter"

    def create_tracking(self, user_id: int, data: Dict[str, Any]) -> RecruiterTracking:
        try:
             return super().create_tracking(user_id, data,self.role)
        except ValidationError as e:
            raise ServiceException(str(e))
        except JobSeeker.DoesNotExist:
            raise NotFoundException("job seeker profile not found")
        except Recruiter.DoesNotExist:
            raise NotFoundException("recruiter profile not found")
        except NotFoundException as e:
            raise NotFoundException("user profile not found")
        except ValidationError as e:
            raise ServiceException({"details":e.message})
        except DatabaseError as e:
            raise InternalErrorException("Internal server error")
        except Exception as e:
             raise InternalErrorException("Internal server error")
            

    def get_trackings(self, user_id: int) -> models.QuerySet:
        try:
            recruiter = super().find_recruiter_profile(user_id)
            recruiter_id = getattr(recruiter, 'id', None)
            if not recruiter_id and not isinstance(recruiter_id, int):
                raise ValidationError({"error": "Recruiter not found"})
            data_fetched = self.tracking_repo.get_by_recruiter(recruiter_id)
            if not data_fetched:
                raise NotFoundException({"data not found"})
            return data_fetched
        except ValidationError as e:
            logger.error(f"error occured:{str(e)}")
            raise ServiceException({"details":e.message})
        except NotFoundException as e:
            logger.error(f"error occured:{str(e)}")
            raise NotFoundException({"details":e.detail})
        except DatabaseError as e:
            logger.error(f"error occured:{str(e)}")
            raise InternalErrorException("internal server error")
        except Exception as e:
            logger.error(f"error occured:{str(e)}")
            raise InternalErrorException("internal server error")
    
    def get_jobseeker_tracking(self,user_id:int) -> Optional[models.QuerySet]:
        try:
            job_seeker = super().find_job_seeker_profile(user_id)
            job_seeker_id = getattr(job_seeker, 'id', None)
            if not job_seeker_id and not isinstance(job_seeker_id, int):
                raise ValidationError({"detail":"Job seeker not found"})
            data_fetched = self.tracking_repo.get_by_job_seeker(job_seeker_id)
            if not data_fetched:
                raise NotFoundException(detail="recruiter tracking info not found")
            return data_fetched
        except ValidationError as e:
            ServiceException(str(e))
        except (JobSeeker.DoesNotExist):
            raise NotFoundException("user profile not found")
        except NotFoundException as e:
            raise NotFoundException(detail=e.detail) 
        except DatabaseError as e:
            logger.error(f"database error occured in the services layer:{str(e)}")
            raise InternalErrorException("Internal server error") 
        except Exception as e:
            logger.error(f"error occured in the services layer:{str(e)}")
            raise InternalErrorException("Internal server error") 

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
    def get_job_applicants(self, job_posting_id: int) -> QuerySet[RecruiterTracking]:
        try:
            applicants = self.tracking_repo.get_applicants_for_job(job_posting_id)
            
            if not applicants.exists():
                raise NotFoundException("No applicants found for this job posting")
                
            return applicants
            
        except Exception as e:
            logger.error(f"Error fetching applicants for job {job_posting_id}: {str(e)}")
            raise ServiceException("Failed to retrieve applicants")