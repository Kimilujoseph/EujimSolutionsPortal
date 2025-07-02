# job_posting/repositories.py
from django.core.exceptions import ObjectDoesNotExist
from ..models import JobPosting, JobPostingSkill
from django.db.models import QuerySet
from typing import Optional,Dict,Any
class JobPostingRepository:
    def __init__(self):
        pass

    def get_all_job_postings(self)->QuerySet[JobPosting]:
        return JobPosting.objects.all()
    
  
    def get_active_job_postings(self)->QuerySet[JobPosting]:
        return JobPosting.objects.filter(is_active=True)
    
   
    def get_job_posting_by_id(self,pk)->Optional[JobPosting]:
        return JobPosting.objects.get(pk=pk)
        
    
    def create_job_posting(self,data)->JobPosting:
        return JobPosting.objects.create(**data)
    
  
    def update_job_posting(self,pk, data)->Optional[JobPosting]:
        job_posting =self.get_job_posting_by_id(pk)
        if job_posting:
            for key, value in data.items():
                setattr(job_posting, key, value)
            job_posting.save()
            return job_posting
        return None
    

    def delete_job_posting(self,pk):
        job_posting = self.get_job_posting_by_id(pk)
        if job_posting:
            job_posting.delete()
            return True
        return False
    
    def add_skill_to_job_posting(self,job_posting_id, skill_data):
        job_posting = self.get_job_posting_by_id(job_posting_id)
        if job_posting:
            skill_data['job_posting'] = job_posting
            return JobPostingSkill.objects.create(**skill_data)
        return None

