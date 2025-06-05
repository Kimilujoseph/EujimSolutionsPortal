# repositories/recruiter_repository.py
from .base_repository import BaseRepository
from ..models import Recruiter, RecruiterDoc, RecruiterTracking
from typing import Type
from django.db import models

class RecruiterRepository(BaseRepository[Recruiter]):
    def __init__(self):
        super().__init__(Recruiter)

    def get_by_user_id(self, user_id: int) -> Recruiter:
        return self.filter(user_id=user_id).first()

    def get_recruiter_with_docs(self, recruiter_id: int) -> Recruiter:
        return self.model_class.objects.prefetch_related('recruiterdoc_set').get(id=recruiter_id)

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
        return self.filter(recruiter_id=recruiter_id)

    def get_by_job_seeker(self, job_seeker_id: int) -> models.QuerySet:
        return self.filter(job_seeker_id=job_seeker_id)

    def update_status(self, tracking: RecruiterTracking, status: str, notes: str = None) -> RecruiterTracking:
        update_data = {'status': status}
        if notes is not None:
            update_data['notes'] = notes
        return self.update(instance=tracking, **update_data)