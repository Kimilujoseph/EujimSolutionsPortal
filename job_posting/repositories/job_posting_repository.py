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
    
  
    def get_paginated_job_postings(self, offset: int, limit: int) -> QuerySet[JobPosting]:
        return JobPosting.objects.filter(is_active=True)\
            .order_by('?')[offset:offset + limit] 
    
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
     #deleteting a skill from a job posting
    def delete_skill_from_job_posting(self,job_posting_id,skill_id):
        job_posting_skill = JobPostingSkill.objects.get(job_posting_id=job_posting_id, skill_id=skill_id)
        if job_posting_skill:           
           job_posting_skill.delete()
        return None
    
            

