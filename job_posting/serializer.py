# job_posting/serializers.py
from rest_framework import serializers
from .models import JobPosting, JobPostingSkill


class JobPostingSkillSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = JobPostingSkill
        fields = ['skill', 'importance']

class JobPostingSerializer(serializers.ModelSerializer):
    required_skills = JobPostingSkillSerializer(source='job_posting', many=True, read_only=True)
    recruiter_company = serializers.CharField(source='recruiter.companyName', read_only=True)
    
    class Meta:
        model = JobPosting
        fields = [
            'id', 'title', 'description', 'requirements', 'responsibilities',
            'location', 'job_type', 'experience_level', 'salary_range_min',
            'salary_range_max', 'is_active', 'posted_at', 'updated_at',
            'application_deadline', 'views_count', 'applications_count',
            'recruiter_company', 'required_skills'
        ]

class JobPostingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosting
        fields = [
            'title', 'description', 'requirements', 'responsibilities',
            'location', 'job_type', 'experience_level', 'salary_range_min',
            'salary_range_max', 'application_deadline'
        ]
