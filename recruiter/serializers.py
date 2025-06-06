# serializers.py
from rest_framework import serializers
from .models import Recruiter, RecruiterDoc, RecruiterTracking
from users.models import User
from django.db  import models
from django.core.validators import FileExtensionValidator,MaxValueValidator

class RecruiterRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruiter
        fields = ['companyName', 'companyLogo', 'industry', 'contactInfo', 'companyEmail', 'description']
        extra_kwargs = {
            'companyEmail': {'required': True},
            'companyName': {'required': True}
        }
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['email', 'firstName', 'secondName']
        read_only_fields = fields

class RecruiterProfileSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()  
    
    class Meta:
        model = Recruiter
        fields = [
            'id',
            'companyName',
            'companyLogo',
            'industry',
            'contactInfo',
            'companyEmail',
            'description',
            'isVerified',
            'createdAt',
            'updatedAt',
            'user' 
        ]
        read_only_fields = ['user', 'isVerified', 'createdAt', 'updatedAt']
class RecruiterDocSerializer(serializers.ModelSerializer):
    upload_path = serializers.FileField(
        validators=[
            FileExtensionValidator(allowed_extensions=['pdf','png', 'jpg']),
            lambda value: MaxValueValidator(5 * 1024 * 1024)(value) if value.size > 5 * 1024 * 1024 else None
        ],
        required=True
    )
    
    def validate_upload_path(self, value):
        if value.size > 5 * 1024 * 1024:  # 5MB
            raise serializers.ValidationError(
                f'File too large. Size should not exceed 5 MB'
            )
        return value
    class Meta:
        model = RecruiterDoc
        fields = ['doc_type', 'upload_path']
        extra_kwargs = {
            'upload_path': {'required': True}
        }
        read_only_fields = ['recruiter', 'status', 'createdAt', 'updatedAt']

class RecruiterTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecruiterTracking
        fields = '__all__'
        read_only_fields = ['recruiter', 'createdAt', 'updatedAt']