from jobseeker.repository.jobseeker_repository import JobSeekerRepository
from jobseeker.models import JobSeeker
from users.exceptions import NotFoundException,InternalErrorException,ServiceException
from ..repository.recruiter_repository import RecruiterRepository,RecruiterTrackingRepository
from ..models import Recruiter
from..serializers import RecruiterTrackingSerializer, RecruiterTrackingUpdateSerializer
from typing import Optional,Dict,Any,Tuple,Union
from django.db import DatabaseError
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import ValidationError
import logging
logger = logging.getLogger(__name__)
class BaseRecruiterTrackingService:
    def __init__(self):
        self.tracking_repo = RecruiterTrackingRepository()
        self.recruiter_repo = RecruiterRepository()
        self.job_seeker_repo = JobSeekerRepository()
    
    def find_job_seeker_profile(self,id:int) -> JobSeeker:
        try:
            print(f"user_id:{id}")
            return self.job_seeker_repo.get_by_user_id(id)
        except (ObjectDoesNotExist,JobSeeker.DoesNotExist) as e:
            logger.error(f"An unexpected error occurred when finding jobseeker_profile:{str(e)}")
            raise 
        except DatabaseError as e:
            logger.error(f"An unexpected error occurred:{str(e)}")
            raise InternalErrorException("internal server error")
        except Exception as e:
            logger.error(f"An unexpected error occurred:{str(e)}")
            raise InternalErrorException("Internal server error")
    def find_recruiter_profile(self,id:int) -> Recruiter:
        try:
            return self.recruiter_repo.get_by_user_id(id)
        except (ObjectDoesNotExist,Recruiter.DoesNotExist) as e:
            raise
        except DatabaseError as e:
            raise 
        except Exception as e:
            raise 
    def validate_user_type_user_id(self,user_type:str,user_id:int)->Tuple[Union[Recruiter,JobSeeker],str]: 
        try:
            if user_type == "recruiter":
                user = self.find_recruiter_profile(user_id)
                id_attr = 'recruiter_id'
            elif user_type == "job_seeker":
                user = self.find_job_seeker_profile(user_id)
                id_attr = 'job_seeker_id'
            else:
                raise ValidationError({"detail":"invalid user type"})
            return user,id_attr
        except (ObjectDoesNotExist,Recruiter.DoesNotExist,JobSeeker.DoesNotExist,NotFoundException) as e:
            logger.error(f"An unexpected error occurred:{str(e)}")
            raise
        except ValidationError as e:
            logger.error(f"Validation error occurred: {e}")
            raise
        except DatabaseError as e:
            logger.error(f"An unexpected error occurred:{str(e)}")
            raise 
        except Exception as e:
            logger.error(f"An unexpected error occurred:{str(e)}")
            raise InternalErrorException("Internal server error") from e
    def validate_existing_tracking(self,job_posting_id:int,job_seeker_id:int):
        try:
            existing_tracking = self.tracking_repo.check_existing_job_tracking(job_posting_id,job_seeker_id)
            print(f"existing job_seeker_tracking:{existing_tracking}")
            if existing_tracking:
                raise ValidationError({"detail":"already showed intrest in this job"})
        except ValidationError as e:
            raise
        except DatabaseError as e:
            raise
        except Exception as e:
            logger.error(f"cvalidation erored: {str(e)}")
            raise InternalErrorException("Internal server error")
    def create_tracking(self, user_id: int, data: Dict[str, Any], user_type: str):
        try:
            user, id_attr = self.validate_user_type_user_id(user_type,user_id)
            requester_data = data.copy()
            requester_data[id_attr] = user.pk  
            requester_data['user_type'] = user_type
            if requester_data.get("job_posting_id"):
               self.validate_existing_tracking(requester_data["job_posting_id"],user.pk)
     
            serializer = RecruiterTrackingSerializer(data=requester_data)
            if not serializer.is_valid():
                raise ValidationError(serializer.errors)
            if not isinstance(serializer.validated_data, dict):
                raise ValidationError({'error': 'incorrect data format passed'})  
            return self.tracking_repo.create(**serializer.validated_data)   
        except (ObjectDoesNotExist,JobSeeker.DoesNotExist,Recruiter.DoesNotExist):
            raise
        except NotFoundException as e: 
            raise 
        except ValidationError as e:
            logger.error(f"Validation error occurred: {e.detail}")
            error_detail = e.detail
            raise 
        except DatabaseError as e:
            logger.error(f"Database error occurred: {e}")
            raise InternalErrorException("Internal server errorss")
        except Exception as e:
            raise
            # logger.error(f"An unexpected error occurred:{str(e)}")
            # raise InternalErrorException("internal server error")
    
