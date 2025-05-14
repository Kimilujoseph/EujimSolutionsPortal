from django.db import models
#create models here

class User(models.Model):
    ROLE_CHOICES = [
        ('employer', 'Employer'),
        ('jobseeker', 'Job Seeker'),
        ('superAdmin', 'Super Admin'),
        ('admin', 'Admin'),
    ]

    first_name = models.CharField(max_length=45)
    second_name = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    is_verified = models.BooleanField(null=True, blank=True)
    verification_code = models.CharField(max_length=45, null=True, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'
        managed = False


