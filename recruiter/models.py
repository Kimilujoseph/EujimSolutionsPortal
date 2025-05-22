from django.db import models
from users.models import User
from jobseeker.models import JobSeeker

class Recruiter(models.Model):
    companyName = models.CharField(max_length=45)
    companyLogo = models.CharField(max_length=500, null=True, blank=True)
    industry = models.CharField(max_length=45, null=True, blank=True)
    contactInfo = models.CharField(max_length=45, null=True, blank=True)
    companyEmail = models.EmailField(unique=True)
    description = models.CharField(max_length=45, null=True, blank=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_column='users_id',
        related_name='recruiters' 
    )
    isVerified = models.BooleanField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'recruiter'
        managed = False


class RecruiterDoc(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
    ]

    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE)
    doc_type = models.CharField(max_length=45, null=True, blank=True)
    upload_path = models.CharField(max_length=500, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'reccruiter_doc'
        managed = False


class RecruiterTracking(models.Model):
    STATUS_CHOICES = [
        ('interviewed', 'Interviewed'),
        ('shortlisted', 'Shortlisted'),
        ('hired', 'Hired'),
        ('rejected', 'Rejected'),
    ]

    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE)
    job_seeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='shortlisted', null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'recruiter_tracking'
        managed = False

