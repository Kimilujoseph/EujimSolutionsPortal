from ..repositories.job_posting_repository import JobPostingRepository
from recruiter.repository.recruiter_repository import RecruiterTrackingRepository
from recruiter.models  import RecruiterTracking
from users.exceptions import InternalErrorException,NotFoundException,ServiceException
from django.db import DatabaseError
from ..models import JobPosting,JobPostingSkill
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import QuerySet
from jobseeker.repository.skill_repository import SkillRepository
from django.utils import timezone
import logging
from typing import Optional,Dict,Any
logger = logging.getLogger(__name__)

class RecruitmentPipelineService:
    def __init__(self):
        self.recruiter_repository = RecruiterTrackingRepository()
    
    def get_candidates_for_job(self,job_posting_id):
        return self.recruiter_repository.get_tracking_records_by_job_posting(job_posting_id)
    
    

    