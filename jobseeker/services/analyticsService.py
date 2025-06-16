from .application_status import get_applications_status_stats
from .recruiter_interaction import get_recruiter_engagement
from .profile_completion import calculate_profile_completion
from .skill_distribution_service import skill_distribution,get_skills_growth_timeline,get_top_skills_by_success
from .education_service import EducationService

class AnalyticsService:
    @staticmethod
    def get_jobseeker_analytics(job_seeker_id: int):
        """
        Collects and returns various analytics for a job seeker.
        """
        profile_completion = calculate_profile_completion(job_seeker_id)
        recruiter_engagement = get_recruiter_engagement(job_seeker_id)
       # print(recruiter_engagement)
        application_status_stats = get_applications_status_stats(job_seeker_id)
        skill_distribution_data = skill_distribution(job_seeker_id)
        skills_growth_timeline = get_skills_growth_timeline(job_seeker_id)
        #top_skills_by_success = get_top_skills_by_success(job_seeker_id)
        education_service = EducationService()
        education_distribution = education_service.get_education_distribution(job_seeker_id)

        return {
            "profile_completion": profile_completion,
            "recruiter_engagement": recruiter_engagement,
            "application_status_stats": application_status_stats,
            "education_distribution": education_distribution,
            "skill_distribution": skill_distribution_data,
            "skills_growth_timeline": skills_growth_timeline,
        }