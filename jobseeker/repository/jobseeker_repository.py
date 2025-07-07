from .base_repository import JobSeekerBaseRepository
from ..models import JobSeeker
from typing import Optional

class JobSeekerRepository(JobSeekerBaseRepository[JobSeeker]):
    def __init__(self):
        super().__init__(JobSeeker)

    def get_by_user_id(self, job_seeker_id: int) -> JobSeeker:
        job_seeker = self.filter(user__id=job_seeker_id).first()
        if job_seeker is None:
            raise JobSeeker.DoesNotExist
        return job_seeker