from ..repository.recruiter_interaction import RecruiterInteraction
from ..repository.jobseeker_repository import   JobSeekerRepository
from django.core.exceptions import ObjectDoesNotExist
from django.db import DatabaseError
from ..models import JobSeeker
from  users.exceptions import NotFoundException, ServiceException,InternalErrorException
from typing import Optional, Dict, Any
import logging

logger = logging.getLogger(__name__)

class RecruiterEngagement:
    def __init__(self):
        self.recruiter_interaction_repo = RecruiterInteraction()
        self.job_seeker_profile_repo = JobSeekerRepository()

    def get_recruiter_engagement(self, job_seeker_id: int):
        try:
            if not isinstance(job_seeker_id, int) or job_seeker_id <= 0:
                raise ServiceException("bad request,please check again and try again")
                
            engagement_count = self.recruiter_interaction_repo.recruiter_engagement(job_seeker_id)
            return engagement_count
            
        except ValueError as e:
            logger.warning(f"Validation error for user {job_seeker_id}: {str(e)}")
            raise ServiceException("Invalid input data") from e
        except DatabaseError as e:
            logger.error(f"Database error for user {job_seeker_id}: {str(e)}")
            raise InternalErrorException("Internal server error,please try again later") from e
        except Exception as e:
            raise InternalErrorException("Internal server error,please try again later") from e
