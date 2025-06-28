from typing import Dict, Any,Optional
from ..models import   JobSeeker
from django.core.exceptions import ObjectDoesNotExist
from django.db import DatabaseError
import logging
from users.exceptions import InternalErrorException,NotFoundException,ServiceException
from ..repository.jobseeker_repository import   JobSeekerRepository
from ..repository.educationRepository import EducationRepository
from ..repository.skill_repository import SkillSetRepository
from ..services.certification_service import CertificationService


logger = logging.getLogger(__name__)

class ProfileCompletionService:
    def __init__(self):
        self.jobseeker_repo = JobSeekerRepository()
        self.education_repo = EducationRepository()
        self.skill_repo = SkillSetRepository()
        self.cert_service = CertificationService()

    def calculate_profile_completion(self, job_seeker_id: int) -> int:
     
        try:
            if not isinstance(job_seeker_id, int) or job_seeker_id <= 0:
                raise ServiceException("bad request,please check again and try again")
                
            jobseeker = self._get_jobseeker_profile(job_seeker_id)
            if not jobseeker:
                return 0
                
            completion_data = self._gather_completion_data(job_seeker_id, jobseeker)
            return self._calculate_percentage(completion_data)
            
        except ValueError as e:
            logger.warning(f"Validation error for user {job_seeker_id}: {str(e)}")
            raise ServiceException("Invalid input data")
        except ObjectDoesNotExist as e:
            raise NotFoundException("jobseeker profile not found")
            return 0
        except DatabaseError as e:
            logger.error(f"Database error for user {job_seeker_id}: {str(e)}")
            raise InternalErrorException("Internal server error,please try again later")
        except Exception as e:
            logger.error(f"Unexpected error calculating completion for {job_seeker_id}: {str(e)}")
            raise InternalErrorException("Profile completion calculation failed") from e

    def _get_jobseeker_profile(self, job_seeker_id: int) -> Optional[JobSeeker]:
        return self.jobseeker_repo.get_by_user_id(job_seeker_id)

    def _gather_completion_data(self, job_seeker_id: int, jobseeker: Any) -> Dict[str, bool]:
        fields = {
            'github': bool(jobseeker.github_url),
            'linkedin': bool(jobseeker.linkedin_url),
            'location': bool(jobseeker.location),
            'bio': bool(jobseeker.bioData),
            'about': bool(jobseeker.about),
            'education': self._has_education(job_seeker_id),
            'skills': self._has_skills(job_seeker_id),
            'certifications': self._has_certifications(job_seeker_id)
        }
        return fields

    def _has_education(self, job_seeker_id: int) -> bool:
        """Check if education exists"""
        try:
            return bool(self.education_repo.get_educations_by_user(job_seeker_id))
        except Exception as e:
            logger.warning(f"Error checking education for {job_seeker_id}: {str(e)}")
            return False

    def _has_skills(self, job_seeker_id: int) -> bool:
        """Check if skills exist"""
        try:
            return bool(self.skill_repo.get_skills_for_jobseeker(job_seeker_id))
        except Exception as e:
            logger.warning(f"Error checking skills for {job_seeker_id}: {str(e)}")
            return False

    def _has_certifications(self, job_seeker_id: int) -> bool:
        try:
            return bool(self.cert_service.get_user_certifications(job_seeker_id))
        except Exception as e:
            logger.warning(f"Error checking certifications for {job_seeker_id}: {str(e)}")
            return False

    def _calculate_percentage(self, completion_data: Dict[str, bool]) -> int:
        try:
            filled_fields = sum(1 for field in completion_data.values() if field)
            total_fields = len(completion_data)
            return int((filled_fields / total_fields) * 100) if total_fields > 0 else 0
        except Exception as e:
            logger.error(f"Calculation error: {str(e)}")
            raise InternalErrorException("Completion calculation failed") from e