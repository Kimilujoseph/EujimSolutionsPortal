from .application_status import get_applications_status_stats
from .recruiter_interaction import get_recruiter_engagement
from .profile_completion import calculate_profile_completion
from .education_service import EducationService

class AnalyticsService:
    @staticmethod
    def get_jobseeker_analytics(job_seeker_id: int):
        """
        Collects and returns various analytics for a job seeker.
        """
        profile_completion = calculate_profile_completion(job_seeker_id)
        recruiter_engagement = get_recruiter_engagement(job_seeker_id)
        application_status_stats = get_applications_status_stats(job_seeker_id)
        
        education_service = EducationService()
        education_distribution = education_service.get_education_distribution(job_seeker_id)

        return {
            "profile_completion": profile_completion,
            "recruiter_engagement": recruiter_engagement,
            "application_status_stats": application_status_stats,
            "education_distribution": education_distribution
        }