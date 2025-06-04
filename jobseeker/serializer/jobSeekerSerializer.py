from  rest_framework import serializers
from ..models import JobSeeker,JobSeekerCertification

class JobSeekerProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='user.email', read_only=True) 
    users_id = serializers.IntegerField(source='user.id', read_only=True)
    firstName = serializers.CharField(source='user.firstName', read_only=True)
    secondName = serializers.CharField(source='user.secondName', read_only=True)
    is_active = serializers.BooleanField(source='user.is_active', read_only=True)
 
    
    class Meta:
        model = JobSeeker
        fields = [
            'id',
            'users_id',
            'firstName',
            'secondName',
            'is_active',
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

class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobSeekerCertification
        fields = ['id', 'issuer', 'upload_path', 'awarded_date', 'description']
        extra_kwargs = {
            'upload_path': {'required': False},
            'awarded_date': {'required': False}
        }

class JobSeekerUpdateSerializer(serializers.ModelSerializer):
    certifications = CertificationSerializer(many=True, required=False, read_only=True)
    
    class Meta:
        model = JobSeeker
        fields = [
            'github_url', 'linkedin_url', 'location', 
            'bioData', 'about', 'certifications'
        ]
        extra_kwargs = {
            'github_url': {'required': False},
            'linkedin_url': {'required': False},
            'location': {'required': False},
            'bioData': {'required': False},
            'about': {'required': False}
        }