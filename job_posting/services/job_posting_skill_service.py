# job_posting/services/job_posting_skill_service.py
from ..repositories.job_posting_repository import JobPostingRepository
from users.exceptions import InternalErrorException,NotFoundException,ServiceException
from django.db import DatabaseError
from django.core.exceptions import ObjectDoesNotExist,ValidationError
from jobseeker.repository.skill_repository import SkillRepository
import logging

logger = logging.getLogger(__name__)

class JobPostingSkillService:
    def __init__(self):
        self.job_repository = JobPostingRepository()
        self.skill_repository = SkillRepository()

    def add_required_skills(self, job_posting_id, skills_data):
        try:
            skill_data = skills_data['skill']
            skill_instance, was_created = self.skill_repository.get_or_create(
            skillName=skill_data.get('skillName'),
            defaults={'description': skill_data.get('description', '')}
        )
            fetch_skill_posted = self.job_repository.find_skill_posted(job_posting_id,skill_instance.pk)
            if fetch_skill_posted is not None:
                raise ValidationError({"skill": "This skill is already added to the job posting"})
            print(skill_instance)
            return self.job_repository.add_skill_to_job_posting(
            job_posting_id, 
            {'skill': skill_instance} 
        )
        except ValidationError as e:
            raise ServiceException(e)
        except ObjectDoesNotExist:
            logger.error(f"job posting with id {job_posting_id} does not exist")
            raise NotFoundException("job posting not found")
        except DatabaseError as e:
            logger.error(f"error occurred while adding skills to job posting: {str(e)}")
            raise InternalErrorException("Internal server, please try again later")
        except Exception as e:
            logger.error(f"error occurred while adding skills to job posting: {str(e)}")
            raise InternalErrorException("Internal server error, please try again later")

    def delete_required_skill(self, job_posting_id: int, skill_id: int):
        try:
            return self.job_repository.delete_skill_from_job_posting(job_posting_id, skill_id)
        except ObjectDoesNotExist:
            logger.error(f"job posting with id {job_posting_id} does not exist")
            raise NotFoundException("job posting not found")
        except DatabaseError as e:
            logger.error(f"error occurred while deleting skill from job posting: {str(e)}")
            raise InternalErrorException("internal server error, please try again later")
        except Exception as e:
            logger.error(f"error occurred while deleting skill from job posting: {str(e)}")
            raise InternalErrorException("internal server error, please try again later")
