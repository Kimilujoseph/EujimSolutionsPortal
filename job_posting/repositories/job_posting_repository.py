# job_posting/repositories.py
from django.core.exceptions import ObjectDoesNotExist
from ..models import JobPosting, JobPostingSkill
from django.db.models import QuerySet
from typing import Optional,Dict,Any
import random
from datetime import date

class JobPostingRepository:
    def __init__(self):
        pass

    def get_all_job_postings(self)->QuerySet[JobPosting]:
        return JobPosting.objects.all()
    
  
    def get_paginated_job_postings(self, offset: int, limit: int):
        today = date.today()
        seed = int(today.strftime('%Y%m%d'))
        
        print("--- HITTING THE DATABASE to fetch job postings ---")
        all_postings = list(JobPosting.objects.filter(is_active=True))
        total_count = len(all_postings)
        
        random.seed(seed)
        random.shuffle(all_postings)
        
        return all_postings[offset:offset + limit], total_count 
    
    def get_job_posting_by_id(self,pk)->Optional[JobPosting]:
        print(f"id passd{pk}")
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
        print(f"id passed innvcs {job_posting}")
        if job_posting:
            skill_data['job_posting'] = job_posting
            return JobPostingSkill.objects.create(**skill_data)
        return None
    def find_skill_posted(self,job_posting_id,skill_id):
        print(f"have been deliverd the followinf id {job_posting_id} and {skill_id}")
        find_skill_posted = JobPostingSkill.objects.get(job_posting_id=job_posting_id,skill_id = skill_id)
        if not find_skill_posted:
            return None
        return find_skill_posted
     #deleteting a skill from a job posting
    def get_by_recruiter_id(self, recruiter_id: int) -> QuerySet[JobPosting]:
        return JobPosting.objects.filter(recruiter_id=recruiter_id)

    def delete_skill_from_job_posting(self,job_posting_id,skill_id):
        job_posting_skill = JobPostingSkill.objects.get(job_posting_id=job_posting_id, skill_id=skill_id)
        if job_posting_skill:           
           job_posting_skill.delete()
        return None
    
            

