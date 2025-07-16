from django.db import models
from django.utils import timezone

class JobListing(models.Model):
    SOURCE_CHOICES = [
        ('LINKEDIN', 'LinkedIn'),
        ('CAREERJET', 'CareerJet'),
    ]

    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    url = models.URLField(unique=True)
    source = models.CharField(max_length=20, choices=SOURCE_CHOICES)
    job_type = models.CharField(max_length=100, blank=True, null=True)
    posted_at = models.DateTimeField(blank=True, null=True)
    scraped_at = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-posted_at']
        indexes = [
            models.Index(fields=['source']),
            models.Index(fields=['title']),
            models.Index(fields=['company']),
        ]

    def __str__(self):
        return f"{self.title} at {self.company}"
