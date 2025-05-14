from django.db import models
from jobseeker.models import JobSeeker

class Skill(models.Model):
    skill_name = models.CharField(max_length=45)
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'skills'
        managed = False

class SkillSet(models.Model):
    PROFICIENCY_CHOICES = [
        ('begginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('midlevel', 'Midlevel'),
        ('proffessional', 'Professional'),
    ]

    job_seeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE, null=True, blank=True)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, null=True, blank=True)
    proffeciency_level = models.CharField(max_length=20, choices=PROFICIENCY_CHOICES, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'skillSet'
        managed = False

