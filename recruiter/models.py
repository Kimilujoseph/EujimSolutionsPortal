from django.db import models
from users.models import User
from jobseeker.models import JobSeeker
from users.models import User


class Recruiter(models.Model):
    companyName = models.CharField(max_length=45)
    companyLogo = models.CharField(max_length=500, null=True, blank=True)
    industry = models.CharField(max_length=250, null=True, blank=True)
    contactInfo = models.CharField(max_length=250, null=True, blank=True)
    companyEmail = models.EmailField(unique=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_column='users_id',
        related_name='recruiters' ,
        null=True,
        blank=True
    )
    isVerified = models.BooleanField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'recruiter'
        managed = True


class RecruiterDoc(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
    ]
    verifiedBy = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='verified_docs'
    )
    verifiedAt = models.DateTimeField(null=True, blank=True)
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE,null=True,blank=True)
    doc_type = models.CharField(max_length=45, null=True, blank=True)
    upload_path = models.FileField(upload_to='recruiter_docs/%Y/%m/%d/',null=True,blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'recruiter_doc'
        managed = True


class RecruiterTracking(models.Model):
    STATUS_CHOICES = [
        ('interviewed', 'Interviewed'),
        ('shortlisted', 'Shortlisted'),
        ('hired', 'Hired'),
        ('rejected', 'Rejected'),
    ]

    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE,null=True,blank=True)
    job_seeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE, related_name='tracking_records',null=True,blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='shortlisted', null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    job_posting = models.ForeignKey(
        'job_posting.JobPosting',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='tracking_records'
    )

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'recruiter_tracking'
        managed = True

