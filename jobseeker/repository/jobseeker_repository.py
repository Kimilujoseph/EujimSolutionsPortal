from .base_repository import JobSeekerBaseRepository
from ..models import JobSeeker

class JobSeekerRepository(JobSeekerBaseRepository[JobSeeker]):
    def __init__(self):
        super().__init__(JobSeeker)

    def get_by_user_id(self, user_id: int) -> JobSeeker:
        return self.filter(user__id=user_id).first()