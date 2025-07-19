from  ..repository.educationRepository import EducationRepository
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from users.exceptions import InternalErrorException, NotFoundException, ServiceException
import logging

logger = logging.getLogger(__name__)

class EducationService:
    def __init__(self):
        self.education_repo = EducationRepository()

    def create_education(self, user_id: int, education_data: dict):
        try:
            education_data['user_id'] = user_id
            return self.education_repo.create(**education_data)
        except ValidationError as e:
            logger.warning(f"Validation error while creating education for user {user_id}: {e}")
            raise ServiceException(str(e))
        except Exception as e:
            logger.error(f"Error creating education for user {user_id}: {e}")
            raise InternalErrorException("Could not create education record.")

    def update_education(self, education_id: int, user_id: int, update_data: dict):
        try:
            return self.education_repo.update_education(education_id, user_id, update_data)
        except ObjectDoesNotExist:
            raise NotFoundException("Education record not found.")
        except ValidationError as e:
            logger.warning(f"Validation error while updating education {education_id} for user {user_id}: {e}")
            raise ServiceException(str(e))
        except NotFoundException:
            raise NotFoundException("user education record not found")
        except Exception as e:
            logger.error(f"Error updating education {education_id} for user {user_id}: {e}")
            raise InternalErrorException("Could not update education record.")

    def delete_education(self, education_id: int, user_id: int):
        try:
            education = self.education_repo.filter(id=education_id, user_id=user_id).first()
            if education:
                self.education_repo.delete(education)
                return True
            raise NotFoundException("Education record not found.")
        except ObjectDoesNotExist:
            raise NotFoundException("Education record not found.")
        except Exception as e:
            logger.error(f"Error deleting education {education_id} for user {user_id}: {e}")
            raise InternalErrorException("Error deleting education record.")

    def get_user_educations(self, user_id: int):
        try:
            return self.education_repo.get_educations_by_user(user_id)
        except ObjectDoesNotExist:
            raise NotFoundException("User not found.")
        except Exception as e:
            logger.error(f"Error fetching educations for user {user_id}: {e}")
            return []

    def get_education_distribution(self, user_id: int):
        try:
            return self.education_repo.get_education_distribution(user_id)
        except ValidationError as e:
            logger.warning(f"Validation error getting education distribution for user {user_id}: {e}")
            return []
        except ObjectDoesNotExist:
            raise NotFoundException("User not found.")
        except Exception as e:
            logger.error(f"An error occurred while fetching education distribution for user {user_id}: {e}")
            return []