# job_posting/serializers.py
from rest_framework import serializers
from .models import JobPosting, JobPostingSkill

class JobPostingSkillSerializer(serializers.ModelSerializer):
    skill_name = serializers.CharField(source='skill.skillName')
    skill_description = serializers.CharField(source='skill.description', required=False)
    
    class Meta:
        model = JobPostingSkill
        fields = ['id', 'skill_name', 'skill_description']
        read_only_fields = ['id']


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
            'recruiter_company','recruiter_id','required_skills'
        ]

class JobPostingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosting
        fields = [
            'title', 'description', 'requirements', 'responsibilities',
            'location', 'job_type', 'experience_level', 'salary_range_min',
            'salary_range_max', 'application_deadline','is_active'
        ]

