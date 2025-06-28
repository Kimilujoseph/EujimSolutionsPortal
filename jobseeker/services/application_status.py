from ..repository.recruiter_interaction import RecruiterInteraction
from ..repository.jobseeker_repository import JobSeekerRepository
from django.core.exceptions import ObjectDoesNotExist
from django.db import DatabaseError
from users.exceptions import ServiceException,InternalErrorException,NotFoundException


class Application:
    def __init__(self):
        self.recruiter_interaction_repo = RecruiterInteraction()
        self.recruiter_jobseeker_repo = JobSeekerRepository()
    
    def get_applications_status_stats(self,job_seeker_id: int):
        try:
            
            stats = self.recruiter_interaction_repo.get_status_counts_by_job_seeker(job_seeker_id)
           
    
            status_counts = {
                'hired': 0,
                'interviewed': 0,
                'shortlisted': 0,
                'rejected': 0
            }

            for item in stats:
                if item['status'] in status_counts:
                    status_counts[item['status']] = item['count']

            return status_counts
        except DatabaseError:
         raise InternalErrorException("Internal server error, please try again later")
        except Exception:
         raise InternalErrorException("Internal server error please try again later")

