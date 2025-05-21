# base_repository.py
from django.db import models
from typing import Type, Generic, TypeVar

T = TypeVar('T', bound=models.Model)

class BaseRepository(Generic[T]):
    def __init__(self, model_class: Type[T]):
        self.model_class = model_class

    def get_by_id(self, id: int) -> T:
        return self.model_class.objects.get(pk=id)

    def get_all(self) -> models.QuerySet:
        return self.model_class.objects.all()

    def filter(self, **kwargs) -> models.QuerySet:
        return self.model_class.objects.filter(**kwargs)
