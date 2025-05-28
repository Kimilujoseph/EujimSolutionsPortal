# jobseeker/repository/education_repository.py
from typing import Optional, Dict
from ..models import Education
from .base_repository import JobSeekerBaseRepository

class EducationRepository(JobSeekerBaseRepository[Education]):
    def __init__(self):
        super().__init__(Education)

    def get_educations_by_user(self, user_id: int):
        return self.filter(user_id=user_id).order_by('-end_year', '-start_year')

    def update_education(self, education_id: int, user_id: int, update_data: Dict):
        education = self.filter(id=education_id, user_id=user_id).first()
        if education:
            return self.update(education, **update_data)
        return None