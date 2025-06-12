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
        fields = ['email', 'firstName', 'lastName']
        read_only_fields = fields

class RecruiterProfileSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)
    
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
        read_only_fields = ['user', 'createdAt', 'updatedAt']

    def __init__(self, *args, **kwargs):
        self.role = kwargs.pop('role', None)
        super().__init__(*args, **kwargs)
        
        # Correct way to set field attributes
        if self.role not in ['admin', 'superAdmin']:
            self.fields['isVerified'].read_only = True

class RecruiterDocSerializer(serializers.ModelSerializer):
    download_url = serializers.SerializerMethodField()
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
    def get_download_url(self, obj):
        request = self.context.get('request')
        if obj.upload_path:
            if request is not None and obj.upload_path:
                return request.build_absolute_uri(obj.upload_path.url)
            return None
        return None
    class Meta:
        model = RecruiterDoc
        fields = ['doc_type', 'upload_path','download_url', 'status', 'recruiter', 'createdAt', 'updatedAt','id']
        extra_kwargs = {
            'upload_path': {'required': True}
        }
        read_only_fields = ['recruiter', 'status', 'createdAt', 'updatedAt']

class RecruiterDocVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecruiterDoc
        fields = ['status'] 
        extra_kwargs = {
            'status': {'required': True}
        }

class RecruiterSerializer(serializers.ModelSerializer):
   # email = serializers.EmailField(source='user.email')
   # name = serializers.CharField(source='user.firstName', read_only=True)

    class Meta:
        model = Recruiter
        fields = ['id', 'companyName', 'companyEmail', 'contactInfo']

class RecruiterTrackingSerializer(serializers.ModelSerializer):
    recruiter = RecruiterSerializer()
    job_seeker = UserProfileSerializer()
    status_display = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = RecruiterTracking
        fields = [
            'id',
            'recruiter',
            'job_seeker',
            'status',
            'status_display',
            'notes',
            'createdAt',
            'updatedAt'
        ]
        read_only_fields = fields
    
class RecruiterTrackingUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecruiterTracking
        fields = ['status', 'notes']
        extra_kwargs = {
            'status': {'required': False},
            'notes': {'required': False}
        }