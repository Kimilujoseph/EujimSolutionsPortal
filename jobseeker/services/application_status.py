from ..repository.recruiter_interaction import RecruiterInteraction
RecruiterInteraction = RecruiterInteraction()

def get_applications_status_stats(job_seeker_id: int):
    stats = RecruiterInteraction.get_status_counts_by_job_seeker(job_seeker_id)

  
    status_counts = {
        'hired': 0,
        'interviewed': 0,
        'shortlisted': 0,
        'rejected': 0
    }

    for item in stats:
        if item['status'] in status_counts:
            status_counts[item['status']] = item['count']

    return status_counts
