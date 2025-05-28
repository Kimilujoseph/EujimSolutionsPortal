from  rest_framework import serializers
from ..models import JobSeeker

class JobSeekerProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='user.email', read_only=True)  # Add email field explicitly
    users_id = serializers.IntegerField(source='user.id', read_only=True)  # Map user.id to users_id

    class Meta:
        model = JobSeeker
        fields = [
            'id',
            'users_id',
            'email', 
            'location',
            'bioData',
            'about',
            'linkedin_url',
            'github_url',
            'createdAt',
            'updatedAt'
        ]
        read_only_fields = [
            'id',
            'users_id',
            'email',  # Make email read-only
            'createdAt',
            'updatedAt'
        ]
        extra_kwargs = {
            'location': {'required': False},
            'bioData': {'required': False},
            'about': {'required': False},
            'linkedin_url': {'required': False},
            'github_url': {'required': False}
        }

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Remove duplicate fields if any
        return representation