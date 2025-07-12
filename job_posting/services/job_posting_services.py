# job_posting/services.py
from ..repositories.job_posting_repository import JobPostingRepository
from recruiter.repository.recruiter_repository import RecruiterTrackingRepository,RecruiterRepository
from users.exceptions import InternalErrorException,NotFoundException,ServiceException
from django.db import DatabaseError
from ..models import JobPosting,JobPostingSkill
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import QuerySet
from jobseeker.repository.skill_repository import SkillRepository
from django.utils import timezone
import logging
from typing import Optional,Dict,Any
import logging
from typing import Optional,Dict,Any
from django.core.cache import cache
logger = logging.getLogger(__name__)

class JobPostingService:
    def __init__(self):
        self.job_repository = JobPostingRepository()
        self.recruiter_repository = RecruiterTrackingRepository()  
        self.recruiter_info_repository = RecruiterRepository()
        self.skill_repository = SkillRepository()
    
    def _invalidate_job_posting_list_cache(self):
        cache.clear()

    def get_all_job_postings(self)->QuerySet[JobPosting]:
        try:
            return self.job_repository.get_all_job_postings()
        except DatabaseError as e:
            logger.error(f"error occured while fetching job postings: {str(e)}")
            raise ServiceException("database error,try again later")
        except Exception as e:
            logger.error(f"error occured while fetching job postings: {str(e)}")
            raise InternalErrorException("internal server error,try again later")
    
   
    def get_paginated_job_postings(self, page_number: int, page_size: int):
        try:
            offset = (page_number - 1) * page_size
            job_postings, total_count = self.job_repository.get_paginated_job_postings(
                offset=offset,
                limit=page_size
            )
            return job_postings, total_count
        except DatabaseError as e:
            logger.error(f"Error fetching paginated job postings: {str(e)}")
            raise InternalErrorException("Internal server error")
   
    def get_job_posting_details(self,pk:int) -> JobPosting:
        try:
            if not isinstance(pk, int) or pk <= 0:
                raise NotFoundException("Invalid job posting ID")
            job_posting = self.job_repository.get_job_posting_by_id(pk)

            if job_posting:
                job_posting.views_count += 1
                job_posting.save()
            else:
                raise ObjectDoesNotExist("job posting not found")
            return job_posting
        except ObjectDoesNotExist:
            logger.error(f"job posting with id {pk} does not exist")
            raise NotFoundException("job posting not found")
        except DatabaseError as e:
            logger.error(f"error occured while fetching job posting details: {str(e)}")
            raise InternalErrorException("Internal server error,try again later")
        except Exception as e:
            logger.error(f"error occured while fetching job posting details: {str(e)}")
            raise InternalErrorException("Internal server error,try again later")
     
    def create_job_posting(self,request, data:dict) -> JobPosting:
       try: 
            if  not isinstance(data,dict):
                raise ServiceException("you request cannot be processed")
            user_id=request.user_data.get("id")
            recruiter = self.recruiter_info_repository.get_by_user_id(user_id)
            if not recruiter:
                raise NotFoundException("Recruiter not found")
            data['recruiter'] = recruiter
            job_posting = self.job_repository.create_job_posting(data)
            self._invalidate_job_posting_list_cache()
            return job_posting
       except (ValueError,TypeError) as e:
            logger.error(f"error occured while creating job posting: {str(e)}")
            raise ServiceException("Invalid data format")
       except DatabaseError as e:
            logger.warning(f"error occured while  job posting: {str(e)}")
            raise InternalErrorException("Internal server error")
       except Exception as e:
            logger.error(f"error occured while creating job posting: {str(e)}")
            raise InternalErrorException("Internal server error ")
            
    def update_job_posting(self,pk, data)->Optional [JobPosting]:
        try:
            job_posting = self.job_repository.update_job_posting(pk, data)
            self._invalidate_job_posting_list_cache()
            return job_posting
        except ObjectDoesNotExist:
            logger.error(f"job posting with id {pk} does not exist")
            raise NotFoundException("job posting not found")
        except DatabaseError as e:
            logger.error(f"error occured while updating job posting: {str(e)}")
            raise InternalErrorException("internal server error,please try again later")
        except Exception as e:
            logger.error(f"error occured while updating job posting:{str(e)}")
            raise InternalErrorException("internal server error,plaese try again later")
    
    def delete_job_posting(self,pk):
        try:
            result = self.job_repository.delete_job_posting(pk)
            self._invalidate_job_posting_list_cache()
            return result
        except ObjectDoesNotExist:
            raise NotFoundException("job posting not found")
        except DatabaseError as e:
            logger.error(f"error occured while deleting job posting: {str(e)}")
            raise InternalErrorException("interrnal server error")
        except Exception as e:
            logger.error(f"error occured while deleting job posting: {str(e)}")
            raise InternalErrorException("internal server error,please try again later")
    
    
    def add_required_skills(self, job_posting_id, skills_data):
        try:
            skill_data = skills_data['skill']
            skill_instance, was_created = self.skill_repository.get_or_create(
            skillName=skill_data.get('skillName'),
            defaults={'description': skill_data.get('description', '')}
        )
        
            print(skill_instance)
            return self.job_repository.add_skill_to_job_posting(
            job_posting_id, 
            {'skill': skill_instance} 
        )
        except ObjectDoesNotExist:
            logger.error(f"job posting with id {job_posting_id} does not exist")
            raise NotFoundException("job posting not found")
        except DatabaseError as e:
            logger.error(f"error occurred while adding skills to job posting: {str(e)}")
            raise InternalErrorException("Internal server, please try again later")
        except Exception as e:
            logger.error(f"error occurred while adding skills to job posting: {str(e)}")
            raise InternalErrorException("Internal server error, please try again later")
    #delete required skill
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
    def close_job_posting(self,pk:int) -> bool:
        try:
            job_posting = self.job_repository.get_job_posting_by_id(pk)
            if job_posting:
                job_posting.is_active = False
                job_posting.save()
                return True
            return False
        except ObjectDoesNotExist:
            logger.error(f"job posting with id {pk} does not exist")
            raise NotFoundException("job posting not found")
        except DatabaseError as e:
            logger.error(f"error occured while closing job posting: {str(e)}")
            raise InternalErrorException("internal server error,please try again later")
        except Exception as e:
            logger.error(f"error occured while closing job posting: {str(e)}")
            raise InternalErrorException("internal server error,please try again later")

