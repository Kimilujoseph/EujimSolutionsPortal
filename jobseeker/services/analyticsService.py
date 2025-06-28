from .application_status import Application
from .recruiter_interaction import RecruiterEngagement
from .profile_completion import ProfileCompletionService
from .skill_distribution_service import SkillAnalyticsService
from .education_service import EducationService
from users.exceptions import NotFoundException
from ..repository.jobseeker_repository import JobSeekerRepository
import logging

logger = logging.getLogger(__name__)
job_seeker_repo = JobSeekerRepository()
class AnalyticsService:
    @staticmethod
    def get_jobseeker_analytics(user_id: int) -> dict:
        job_seeker_id = None
        result = {
            "profile_completion": 0,
            "recruiter_engagement": {},
            "application_status_stats": {},
            "education_distribution": [],
            "skill_distribution": {},
            "skills_growth_timeline": [],
            "errors": []
        }
        
        services = {
            "profile_completion": ProfileCompletionService(),
            "recruiter_engagement": RecruiterEngagement(),
            "application_status_stats": Application(),
            "skill_distribution": SkillAnalyticsService(),
            "education_distribution": EducationService(),
        }
        try:
            if not isinstance(user_id, int) or user_id <= 0:
                raise ValueError("Invalid job seeker ID")
            job_seeker =job_seeker_repo.get_by_user_id(user_id)
            if not job_seeker:
                return result
            job_seeker_id = job_seeker.pk

        except Exception as e:
            logger.warning(f"Validation error for user {user_id}: {str(e)}")
            result["errors"].append("Invalid job seeker ID")
            return result
        try:
            result["profile_completion"] = services["profile_completion"].calculate_profile_completion(user_id)
        except Exception as e:
            logger.warning(f"Profile completion failed for {job_seeker_id}: {str(e)}")
            result["errors"].append("profile_completion")

        try:
            result["recruiter_engagement"] = services["recruiter_engagement"].get_recruiter_engagement(job_seeker_id)
        except NotFoundException:
            result["recruiter_engagement"] = {"recruiter_count": 0, "recent_interactions": []}
        except Exception as e:
            logger.warning(f"Recruiter engagement failed for {job_seeker_id}: {str(e)}")
            result["errors"].append("recruiter_engagement")

        try:
            result["application_status_stats"] = services["application_status_stats"].get_applications_status_stats(job_seeker_id)
        except NotFoundException:
            result["application_status_stats"] = {
                'hired': 0,
                'interviewed': 0,
                'shortlisted': 0,
                'rejected': 0
            }
        except Exception as e:
            logger.warning(f"Application stats failed for {job_seeker_id}: {str(e)}")
            result["errors"].append("application_status_stats")

        try:
            skill_service = services["skill_distribution"]
            result["skill_distribution"] = skill_service.skill_distribution(user_id)
            result["skills_growth_timeline"] = skill_service.get_skills_growth_timeline(user_id)
        except NotFoundException:
            # Empty results if no skills exist
            result["skill_distribution"] = {
                'beginner': 0,
                'intermediate': 0,
                'midlevel': 0,
                'professional': 0
            }
            result["skills_growth_timeline"] = []
        except Exception as e:
            logger.warning(f"Skill analytics failed for {job_seeker_id}: {str(e)}")
            result["errors"].append("skill_analytics")

        try:
            result["education_distribution"] = services["education_distribution"].get_education_distribution(user_id)
        except NotFoundException:
            result["education_distribution"] = []
        except Exception as e:
            logger.warning(f"Education distribution failed for {job_seeker_id}: {str(e)}")
            result["errors"].append("education_distribution")

        return result