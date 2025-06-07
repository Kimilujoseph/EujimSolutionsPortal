# serializers.py
from rest_framework import serializers
from users.models import User
from skills.models import SkillSet
from jobseeker.models import JobSeeker

class SkillSetSerializer(serializers.ModelSerializer):
    skill_name = serializers.CharField(source='skill.skillName', read_only=True)
    
    class Meta:
        model = SkillSet
        fields = ['skill_name', 'proffeciency_level']
        read_only_fields = fields

class JobSeekerSearchSerializer(serializers.ModelSerializer):
    skills = serializers.SerializerMethodField()
    profile = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'firstName',
            'secondName',
            'skills',
            'profile'
        ]
    
    def get_skills(self, obj):
        skill_sets = obj.skill_sets.all().select_related('skill')
        return SkillSetSerializer(skill_sets, many=True).data
    
    def get_profile(self, obj):
        profile = obj.jobseeker_profile
        return {
            'github_url': profile.github_url,
            'linkedin_url': profile.linkedin_url,
            'location': profile.location,
            'about': profile.about
        }