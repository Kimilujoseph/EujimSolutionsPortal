# services/recruiter_service.py
from ..models import RecruiterDoc
from ..repository.recruiter_repository import (
    RecruiterRepository,
    RecruiterDocRepository,
)
from ..serializers import (
    RecruiterDocSerializer,
   
)
from django.db import models
from rest_framework.exceptions import ValidationError
from typing import Optional, Dict, Any


class RecruiterDocService:
    def __init__(self):
        self.doc_repo = RecruiterDocRepository()
        self.recruiter_repo = RecruiterRepository()

    def create_document(self, recruiter_id: int, data: Dict[str, Any]) -> RecruiterDoc:
        serializer = RecruiterDocSerializer(data=data)
        if not serializer.is_valid():
            raise ValidationError(serializer.errors)
        if not isinstance(serializer.validated_data,dict):
            raise ValidationError({'error': 'Invalid data format'})
        return self.doc_repo.create(recruiter_id=recruiter_id, **serializer.validated_data)

    def get_documents(self, recruiter_id: int) -> models.QuerySet:
        return self.doc_repo.get_by_recruiter(recruiter_id)

    def get_document(self, doc_id: int) -> Optional[RecruiterDoc]:
        return self.doc_repo.get_by_id(doc_id)

    def update_document(self, doc_id: int, data: Dict[str, Any]) -> RecruiterDoc:
        doc = self.doc_repo.get_by_id(doc_id)
        if not doc:
            raise ValidationError({'error': 'Document not found'})
        
        serializer = RecruiterDocSerializer(instance=doc, data=data, partial=True)
        if not serializer.is_valid():
            raise ValidationError(serializer.errors)
        if not isinstance(serializer.validated_data, dict):
            raise ValidationError({'error': 'Invalid data format'})
        return self.doc_repo.update(instance=doc, **serializer.validated_data)

    def delete_document(self, doc_id: int) -> None:
        doc = self.doc_repo.get_by_id(doc_id)
        if not doc:
            raise ValidationError({'error': 'Document not found'})
        self.doc_repo.delete(instance=doc)

