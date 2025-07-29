
from ..repository.skill_repository import SkillRepository,SkillSetRepository
from django.core.exceptions import ObjectDoesNotExist
from ..repository.jobseeker_repository import JobSeekerRepository
from ..repository.educationRepository import EducationRepository
from  django.core.exceptions import ValidationError
from ..services.education_service import EducationService
from users.exceptions import (NotFoundException,InternalErrorException,ServiceException)
from ..permissions import admin_required
import logging
from django.db import DatabaseError
    

logger = logging.getLogger(__name__)
class ProfileService:
    def __init__(self):
        self.jobseeker_repo = JobSeekerRepository()
        self.skill_repo = SkillRepository()
        self.skillset_repo = SkillSetRepository()
    def get_jobseeker_full_profile(self,request,user_id):
       try:
            if request.user_data.get('role') not in ['admin','superAdmin'] and user_id is None:
                user_id = request.user_data.get('id')
            return {
                    "profile":self.get_jobseeker_profile(user_id),
                    "skills":self.get_jobseeker_skills(user_id),
                    "education": EducationService().get_user_educations(user_id)
                }
       except ObjectDoesNotExist as e:
           logger.error(f"error found in finding user profile {str(e)}")
           raise NotFoundException("user profile not found")
       except NotFoundException as e:
           logger.error(f"error found in finding noew  {str(e)}")
           raise NotFoundException("user profile not found")
       except DatabaseError as e:
           logger.error(f"error found {str(e)}")
           raise InternalErrorException("failed to fetch user profile")
       except Exception as e:
           logger.error(f"error found {str(e)}")
           raise InternalErrorException("failed to fetch user profile")
        

    def create_or_update_profile(self, user_id: int, profile_data: dict):
        try:
           
            jobseeker = self.jobseeker_repo.get_by_user_id(user_id)
          
            return self.jobseeker_repo.update(jobseeker, **profile_data)
        except ObjectDoesNotExist:
            logger.info(f"Profile not found for user_id {user_id}, creating a new profile.")
            try:
                profile_data['user_id'] = user_id
                return self.jobseeker_repo.create(**profile_data)
            except Exception as e:
                logger.error(f"Failed to create profile after not finding one: {str(e)}")
                raise ServiceException("Failed to create profile.")
        except DatabaseError as e:
            logger.error(f"Database error in create_or_update_profile: {str(e)}")
            raise InternalErrorException("Database error occurred while creating/updating profile")
        except Exception as e:
            logger.error(f"Unexpected error in create_or_update_profile: {str(e)}")
            raise ServiceException("An error occurred while creating/updating profile")
    def add_skill_to_profile(self, user_id: int, skill_data: dict):
    # Check if skill exists or create new
        skill, created = self.skill_repo.get_or_create(
            skillName=skill_data['skill_name'], 
            defaults={'description': skill_data.get('description', '')}
        )
        

        return self.skillset_repo.createSkillSet(
            user_id=user_id,
            skill_id=skill.pk,
            proffeciency_level=skill_data.get('proffeciency_level', 'beginner')
        )

    def get_jobseeker_profile(self, user_id: int):
        try:
            profile = self.jobseeker_repo.get_by_user_id(user_id)
            if not profile:
                raise NotFoundException("Profile not found")
            return profile
        except ObjectDoesNotExist as e:
            logger.error(f"error occured in getting user profile {str(e)}")
            raise 
        except NotFoundException as e:
            logger.error(f"error occured in getting user profile {str(e)}")
            raise
        except DatabaseError as e:
            logger.error(f"error occured in getting user profile {str(e)}")
            raise
        except Exception as e:
             logger.error(f"error occured in getting user profile {str(e)}")
             raise

    def get_jobseeker_skills(self, jobseeker_id: int):
        try:
            return self.skillset_repo.get_skills_for_jobseeker(jobseeker_id)
        except DatabaseError:
            raise
        except Exception as e:
            raise
    
    def delete_skill_from_profile(self,user_id:int,skill_id:int):
        try:
            deleted_count = self.skillset_repo.delete_skill_for_user(
                user_id=user_id,
                skill_id=skill_id
            )

            if deleted_count == 0:
                raise ValidationError("Skill not found or does not belong to the user")
            return True
        except Exception as e:
            raise ValidationError(f"Failed to delete skill: {str(e)}")