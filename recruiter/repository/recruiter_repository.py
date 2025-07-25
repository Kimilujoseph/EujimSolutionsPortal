# repositories/recruiter_repository.py
from .base_repository import BaseRepository
from ..models import Recruiter, RecruiterDoc, RecruiterTracking
from typing import Type, Optional
from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import QuerySet

class RecruiterRepository(BaseRepository[Recruiter]):
    def __init__(self):
        super().__init__(Recruiter)

    def get_by_user_id(self, user_id: int) -> Recruiter:
        recruiter = self.filter(user_id=user_id).first()
        if recruiter is None:
            raise Recruiter.DoesNotExist
        return recruiter

    def get_recruiter_with_docs(self, recruiter_id: int) -> Recruiter:
        return self.model_class.objects.prefetch_related('recruiterdoc_set').get(id=recruiter_id)
    def get_recruiter_with_profile(self, user_id: int) -> Optional[Recruiter]:
        return self.model_class.objects \
        .select_related('user') \
        .only(
            'companyName', 
            'companyEmail',
            'user__email',      
            'user__firstName', 
            'user__lastName'  
        ) \
        .filter(user_id=user_id) \
        .first()


class RecruiterDocRepository(BaseRepository[RecruiterDoc]):
    def __init__(self):
        super().__init__(RecruiterDoc)

    def get_by_recruiter(self, recruiter_id: int) -> models.QuerySet:
        return self.filter(recruiter_id=recruiter_id)

    def update_status(self, doc: RecruiterDoc, status: str) -> RecruiterDoc:
        return self.update(instance=doc, status=status)

class RecruiterTrackingRepository(BaseRepository[RecruiterTracking]):
    def __init__(self):
        super().__init__(RecruiterTracking)

    def get_by_recruiter(self, recruiter_id: int) -> models.QuerySet:
       return self.model_class.objects.filter(recruiter_id=recruiter_id)\
        .select_related(
            'recruiter',
            'job_seeker',
            'job_seeker__user'    
        )\
            .only(
            'id',
            'status',
            'notes',
            'createdAt',
            'recruiter__companyName',
            'recruiter__contactInfo',
            'job_seeker__github_url', 
            'job_seeker__linkedin_url',
            'job_seeker__user__firstName',
            'job_seeker__user__lastName',
            'job_seeker__user__id'
        )\
        .order_by('-createdAt')

    def get_by_job_seeker(self, job_seeker_id: int) -> models.QuerySet:
        return self.model_class.objects.filter(job_seeker_id=job_seeker_id)\
         .select_related(
            'recruiter',
            'job_seeker',
            'job_seeker__user',
            'job_posting',
        )\
            .only(
            'id',
            'status',
            'notes',
            'createdAt',
            'recruiter__companyName',
            'recruiter__contactInfo',
            'job_seeker__github_url',
            'job_seeker__linkedin_url',
            'job_seeker__user__firstName',
            'job_seeker__user__lastName',
            'job_seeker__user__id',
            'job_posting__id',
            'job_posting__title',
            'job_posting__location',
            'job_posting__posted_at'
        )\
            .order_by('-createdAt')
    def get_tracking_by_id(self, tracking_id: int) -> Optional[RecruiterTracking]:
        return self.model_class.objects.filter(id=tracking_id)\
        .select_related(
            'recruiter',
            'job_seeker'
        ).first()
    def get_tracking_records_by_job_posting(self,job_posting_id):
        return RecruiterTracking.objects.filter(job_posting_id=job_posting_id)\
        .select_related(
            'recruiter',
            'job_seeker',
            'job_posting'
        )\
    
        
    def update_status(self, tracking: RecruiterTracking, status: str, notes: Optional[str] = None) -> Optional[RecruiterTracking]:
        update_data = {'status': status}
        if notes is not None:
            update_data['notes'] = notes
        return self.update(instance=tracking, **update_data)
    #check if a job post exist with the same jobseeker id 
    def check_existing_job_tracking(self,job_post_id:int,job_seeker_id:int):
        print(f"jobseeker:{job_seeker_id}")
        print(f"job+posttt:{job_post_id}")
        return RecruiterTracking.objects.filter(
            job_seeker_id=job_seeker_id,
            job_posting_id = job_post_id
        ).exists()
    
    def get_applicants_for_job(self,job_posting_id: int) -> QuerySet[RecruiterTracking]:
        
        queryset = RecruiterTracking.objects.filter(
            job_posting_id=job_posting_id,
            user_type='recruiter'
        ).select_related('job_seeker__user', 'job_posting')
            
        return queryset.order_by('-createdAt')
        