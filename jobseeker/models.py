from django.db import models
from users.models import User
from django.conf import settings
#Create models here

class JobSeeker(models.Model):
    github_url = models.URLField(max_length=255, null=True, blank=True)
    linkedin_url = models.URLField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=45, null=True, blank=True)
    bioData = models.TextField(null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    user = models.OneToOneField(
    User,
    on_delete=models.CASCADE,
    related_name='jobseeker_profile',
    db_column='users_id'
    )
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'job_seeker'
        managed = False
class JobSeekerCertification(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='certifications',
        db_column='userId'  # Match exact DB column name
    )
    issuer = models.CharField(max_length=45, null=True, blank=True)
    upload_path = models.CharField(
        max_length=500, 
        null=True, 
        blank=True,
        db_column='uploadPath'  # Match DB column
    )
    awarded_date = models.DateField(
        null=True, 
        blank=True,
        db_column='awardedDate'  # Match DB column
    )
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='createdAt'  # Match DB column
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        db_column='updatedAt'  # Match DB column
    )

    class Meta:
        db_table = 'jobseeker_certification'
        managed = False



class Education(models.Model):
    DEGREE_CHOICES = [
        ('high_school', 'High School'),
        ('diploma', 'Diploma'),
        ('bachelor', "Bachelor's Degree"),
        ('master', "Master's Degree"),
        ('phd', 'PhD'),
        ('certificate', 'Certificate'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='educations',
        db_column='user_id'
    )
    institution_name = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    degree = models.CharField(max_length=20, choices=DEGREE_CHOICES)
    field_of_study = models.CharField(max_length=100)
    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField(null=True, blank=True)  # Null if still studying
    is_current = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)
    school_logo = models.TextField(
        null=True,
        blank=True,
        max_length=255
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'education_qualifications'
        managed = False  # Set to False since you're working with an existing database
        ordering = ['-end_year', '-start_year']

    def __str__(self):
        return f"{self.qualification} at {self.institution_name} ({self.start_year}-{self.end_year or 'Present'})"