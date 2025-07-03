from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from skills.models import Skill
class JobPosting(models.Model):
    JOB_TYPES = [
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('contract', 'Contract'),
        ('internship', 'Internship'),
        ('remote', 'Remote'),
    ]
    
    EXPERIENCE_LEVELS = [
        ('entry', 'Entry Level'),
        ('mid', 'Mid Level'),
        ('senior', 'Senior Level'),
        ('executive', 'Executive'),
    ]
    
    recruiter = models.ForeignKey(
        'recruiter.Recruiter',
        db_column='recruiter_id',
        on_delete=models.CASCADE,
        related_name='job_postings',
        db_constraint=False
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    requirements = models.TextField()
    responsibilities = models.TextField()
    location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=20, choices=JOB_TYPES)
    experience_level = models.CharField(max_length=20, choices=EXPERIENCE_LEVELS)
    salary_range_min = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    salary_range_max = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    application_deadline = models.DateField(null=True, blank=True)
    views_count = models.PositiveIntegerField(default=0)
    applications_count = models.PositiveIntegerField(default=0)
    
    class Meta:
        db_table = 'job_postings'
        ordering = ['-posted_at']
        
    def __str__(self):
        return f"{self.title} at {self.recruiter.companyName}"

class JobPostingSkill(models.Model):
    job_posting = models.ForeignKey(
        JobPosting,
        on_delete=models.CASCADE,
        related_name='job_posting'
    )
    skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE,
        related_name='required_skills'
    )
    
    
    class Meta:
        db_table = 'job_posting_skills'
        unique_together = ('job_posting', 'skill')
        
    def __str__(self):
        return f"{self.skill.skillName} for {self.job_posting.title}"

