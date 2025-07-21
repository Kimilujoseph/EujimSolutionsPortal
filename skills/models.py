from django.db import models
from jobseeker.models import JobSeeker
from users.models import User
from django.conf import settings

class Skill(models.Model):
    skillName = models.CharField(max_length=45)
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'skills'
        managed = True

class SkillSet(models.Model):
    PROFICIENCY_CHOICES = [
        ('begginner', 'Begginner'),
        ('intermediate', 'Intermediate'),
        ('midlevel', 'Midlevel'),
        ('proffessional', 'Professional'),
    ]
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='skill_sets',
        db_column='userId',
        null=True,
        blank=True
    )
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, null=True, blank=True)
    proffeciency_level = models.CharField(max_length=20, choices=PROFICIENCY_CHOICES, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'skillSet'
        managed = True

