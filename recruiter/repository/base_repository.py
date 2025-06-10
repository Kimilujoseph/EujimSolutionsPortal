# repositories/base_repository.py
from django.db import models
from typing import Type, Generic, TypeVar, Optional

T = TypeVar('T', bound=models.Model)

class BaseRepository(Generic[T]):
    def __init__(self, model_class: Type[T]):
        self.model_class = model_class

    def get_by_id(self, id: int) -> Optional[T]:
        try:
            return self.model_class.objects.get(pk=id)
        except self.model_class.DoesNotExist:
            return None

    def get_all(self) -> models.QuerySet:
        return self.model_class.objects.all()

    def filter(self, **kwargs) -> models.QuerySet:
        return self.model_class.objects.filter(**kwargs)

    def create(self, **kwargs) -> T:
        return self.model_class.objects.create(**kwargs)

    def update(self, instance: T, **kwargs) -> T:
        for key, value in kwargs.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    def delete(self, instance: T) -> None:
        instance.delete()