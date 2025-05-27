from .base_repository import JobSeekerBaseRepository
from skills.models import Skill, SkillSet

class SkillRepository(JobSeekerBaseRepository[Skill]):
    def __init__(self):
        super().__init__(Skill)

   
class SkillSetRepository(JobSeekerBaseRepository[SkillSet]):
    def __init__(self):
        super().__init__(SkillSet)


def get_skills_for_jobseeker(self, jobseeker_id: int):
        return self.filter(userId=jobseeker_id).select_related('skill')  