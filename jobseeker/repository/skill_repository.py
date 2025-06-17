from .base_repository import JobSeekerBaseRepository
from skills.models import Skill, SkillSet
from django.db import models

from typing import Tuple, Dict, Optional

class SkillRepository(JobSeekerBaseRepository[Skill]):
    def __init__(self):
        super().__init__(Skill)

    def get_or_create(self, skillName: str, defaults: Optional[Dict] = None) -> Tuple[Skill, bool]:
      
        if defaults is None:
            defaults = {}
            
        return self.model_class.objects.get_or_create(
            skillName=skillName, 
            defaults=defaults
        )
        
class SkillSetRepository(JobSeekerBaseRepository[SkillSet]):
    def __init__(self):
        super().__init__(SkillSet)


    def get_skills_for_jobseeker(self, jobseeker_id: int):
        return self.filter(user_id=jobseeker_id).select_related('skill')\
        .order_by('createdAt')
    # In SkillSetRepository
    def createSkillSet(self, user_id: int, skill_id: int, proffeciency_level: str) -> SkillSet:
        return self.model_class.objects.create(
            user_id=user_id,
            skill_id=skill_id,
            proffeciency_level=proffeciency_level
    )

    def delete_skill_for_user(self,user_id:int,skill_id:int)->int:
        return SkillSet.objects.filter(
            id = skill_id
        ).delete()[0]


class SkillDistributionSet(JobSeekerBaseRepository[SkillSet]):
    def __init__(self):
        super().__init__(SkillSet)

    def get_skill_distribution(self, job_seeker_id: int):
        return self.filter(user_id=job_seeker_id)\
        .values('proffeciency_level')\
        .annotate(count=models.Count('id'))\
        .order_by('proffeciency_level')
    def get_skill_set(self, job_seeker_id: int):
        return SkillSet.objects.filter(user_id=job_seeker_id)\
        .select_related('skill')\
        .order_by('createdAt')
