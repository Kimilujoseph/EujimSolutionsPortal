
from ..repository.skill_repository import SkillRepository,SkillSetRepository
from django.core.exceptions import ObjectDoesNotExist
from ..repository.jobseeker_repository import JobSeekerRepository
from ..repository.educationRepository import EducationRepository
from  django.core.exceptions import ValidationError
from ..permissions import admin_required
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
            profile_data['user_id'] = user_id
            return self.jobseeker_repo.create(**profile_data)

    def add_skill_to_profile(self, user_id: int, skill_data: dict):
    # Check if skill exists or create new
        skill, created = self.skill_repo.get_or_create(
            skillName=skill_data['skill_name'], 
            defaults={'description': skill_data.get('description', '')}
        )
        

        return self.skillset_repo.createSkillSet(
            user_id=user_id,
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