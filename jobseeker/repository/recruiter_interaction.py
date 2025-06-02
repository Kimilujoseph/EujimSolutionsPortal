from .base_repository import JobSeekerBaseRepository
from recruiter.models import Recruiter, RecruiterDoc, RecruiterTracking
from django.db.models import Count

class RecruiterInteraction(JobSeekerBaseRepository):
    def __init__(self,model: RecruiterTracking = None):
        super().__init__(model)
        #initalize with the RecruiterTracking model
        self.model = model or RecruiterTracking

    #filter jobseeker
    def get_status_counts_by_job_seeker(self, job_seeker_id: int):
        return self.model.objects.filter(job_seeker_id=job_seeker_id) \
            .values('status') \
            .annotate(count=Count('id'))

    def recruiter_engagement(self, job_seeker_id: int):
   
       try:
            recruiter_count = self.model.objects.filter(job_seeker_id=job_seeker_id) \
            .values('recruiter') \
            .distinct() \
            .count()

            recent_interactions = self.model.objects.filter(job_seeker_id=job_seeker_id).select_related('recruiter') \
                .order_by('-createdAt')[:10]  
            return {
                'recruiter_count': recruiter_count,
                'recent_interactions': [
                    {
                        'company': interaction.recruiter.companyName,
                        'status': interaction.status,
                        'date': interaction.updatedAt,
                        'notes': interaction.notes
                    } for interaction in recent_interactions
                ]
            }
       except Exception as e:
                print(f"Error fetching recruiter engagement for job seeker {job_seeker_id}: {e}")
                return {
                    'recruiter_count': 0,
                    'recent_interactions': []
                }
            