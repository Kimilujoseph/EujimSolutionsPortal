
from ..repository.skill_repository import SkillRepository,SkillSetRepository
from django.core.exceptions import ObjectDoesNotExist
from ..repository.jobseeker_repository import JobSeekerRepository

class ProfileService:
    def __init__(self):
        self.jobseeker_repo = JobSeekerRepository()
        self.skill_repo = SkillRepository()
        self.skillset_repo = SkillSetRepository()

    def create_or_update_profile(self, user_id: int, profile_data: dict):
        jobseeker = self.jobseeker_repo.get_by_user_id(user_id)
        
        if jobseeker:
            return self.jobseeker_repo.update(jobseeker, **profile_data)
        else:
            profile_data['users_id'] = user_id
            return self.jobseeker_repo.create(**profile_data)

    def add_skill_to_profile(self,user_id: int, skill_data: dict):
        # Check if skill exists or create new
        skill, created = self.skill_repo.get_or_create(
            skill_name=skill_data['skill_name'],
            defaults={'description': skill_data.get('description', '')}
        )
        
        # Add to jobseeker's skillset
        return self.skillset_repo.create(
            userId=user_id,
            skill_id=skill.id,
            proffeciency_level=skill_data.get('proffeciency_level', 'beginner')
        )

    def get_jobseeker_profile(self, user_id: int):
        try:
            profile = self.jobseeker_repo.get_by_user_id(user_id)
            if not profile:
                raise ObjectDoesNotExist("Profile not found")
            return profile
        except ObjectDoesNotExist as e:
            raise ValueError(str(e))

    def get_jobseeker_skills(self, jobseeker_id: int):
        return self.skillset_repo.get_skills_for_jobseeker(jobseeker_id)