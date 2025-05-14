from django.db import models
from users.models import User

#Create models here

class JobSeeker(models.Model):
    github_url = models.URLField(max_length=255, null=True, blank=True)
    linkedin_url = models.URLField(max_length=255, null=True, blank=True)
    institution_name = models.CharField(max_length=45, null=True, blank=True)
    year_of_joining = models.DateField(null=True, blank=True)
    year_of_completion = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=45, null=True, blank=True)
    bio_data = models.TextField(null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='jobseeker_profile')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'job_seeker'
        managed = False


class JobSeekerCertification(models.Model):
    job_seeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE)
    issuer = models.CharField(max_length=45, null=True, blank=True)
    upload_path = models.CharField(max_length=500, null=True, blank=True)
    awarded_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'jobseeker_certification'
        managed = False

