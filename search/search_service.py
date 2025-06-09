from django.db.models import Q
from jobseeker.models import JobSeeker, JobSeekerCertification
from skills.models import Skill, SkillSet
from users.models import User
from typing import List, Optional

class JobSeekerSearchService:
    @staticmethod
    def search_by_skills(skill_names: List[str], min_proficiency: Optional[str] = None):
      
        skills = Skill.objects.filter(skillName__in=skill_names)
        skill_ids = skills.values_list('id', flat=True)
        query = Q(skill_id__in=skill_ids)

       
        if min_proficiency:
            proficiency_order = ['begginer', 'intermediate', 'midlevel', 'proffessional'] 
            min_index = proficiency_order.index(min_proficiency)
            valid_levels = proficiency_order[min_index:]
            query &= Q(proffeciency_level__in=valid_levels)

        skilled_users = SkillSet.objects.filter(query).values_list('user_id', flat=True)

       
        text_query = Q()
        for skill in skill_names:
            text_query |= Q(about__icontains=skill) | Q(bioData__icontains=skill)

        text_match_users = JobSeeker.objects.filter(text_query).values_list('user_id', flat=True)

        
        cert_query = Q()
        for skill in skill_names:
            cert_query |= Q(issuer__icontains=skill) | Q(description__icontains=skill)

        cert_users = JobSeekerCertification.objects.filter(cert_query).values_list('user_id', flat=True)

        
        all_user_ids = set(skilled_users) | set(text_match_users) | set(cert_users)

        
        return User.objects.filter(id__in=all_user_ids).select_related('jobseeker_profile')
