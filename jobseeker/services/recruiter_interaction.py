from ..repository.recruiter_interaction import RecruiterInteraction


def get_recruiter_engagement(job_seeker_id: int):
    recruiter_interaction_repo = RecruiterInteraction()
    return recruiter_interaction_repo.recruiter_engagement(job_seeker_id)