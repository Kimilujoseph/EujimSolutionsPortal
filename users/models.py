from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
import uuid
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from recruiter.models import Recruiter
    from jobseeker.models import JobSeeker

class User(AbstractBaseUser, PermissionsMixin):
    ROLE_ENUM = [
        ('employer', 'Employer'),
        ('jobseeker', 'JobSeeker'),
        ('superAdmin', 'SuperAdmin'),
        ('admin', 'Admin')
    ]

    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=45)
    secondName = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    is_suspended = models.BooleanField(default=True)
    is_pending = models.BooleanField(default=True)
    password = models.CharField(max_length=255)
    isVerified = models.BooleanField(default=False)
    verificationCode = models.UUIDField(default=uuid.uuid4, editable=False)
    role = models.CharField(max_length=20, choices=ROLE_ENUM, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    deleted_at = models.DateTimeField(null=True, blank=True)
    deletion_reason = models.TextField(null=True, blank=True)

    deleted_by = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='deleted_users'
    )

    restored_by = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='restored_users'
    )
    if TYPE_CHECKING:
        jobseeker_profile: 'JobSeeker'
        recruiters: models.QuerySet['Recruiter']

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstName', 'secondName']

    def __str__(self):
        return self.email

    class Meta:
        db_table = "users"
        managed = True
