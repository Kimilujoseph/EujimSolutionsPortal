from ..repository.recruiter_interaction import RecruiterInteraction
from ..repository.jobseeker_repository import   JobSeekerRepository


def get_recruiter_engagement(job_seeker_id: int):
    recruiter_interaction_repo = RecruiterInteraction()
    job_seeker_profile_repo = JobSeekerRepository()
    jobSeeker = job_seeker_profile_repo.get_by_user_id(job_seeker_id) 
    if not jobSeeker:
        return 0
    return recruiter_interaction_repo.recruiter_engagement(jobSeeker.pk)