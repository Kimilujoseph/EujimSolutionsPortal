# serializers.py
from rest_framework import serializers
from .models import Recruiter, RecruiterDoc, RecruiterTracking
from users.models import User
from jobseeker.models import JobSeeker
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
# serializers.py

class JobSeekerProfileSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)

    class Meta:
        model = JobSeeker
        fields = ['id', 'github_url', 'linkedin_url', 'location', 'bioData', 'about', 'createdAt', 'updatedAt', 'user']

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
    # Read-only fields for display
    recruitmentId = serializers.IntegerField(source='id', read_only=True)
    companyName = serializers.CharField(source='recruiter.companyName', read_only=True)
    companyInfo = serializers.CharField(source='recruiter.contactInfo', read_only=True)
    job_seeker = serializers.CharField(source='job_seeker.user.id', read_only=True)
    firstName = serializers.CharField(source='job_seeker.user.firstName', read_only=True)
    lastName = serializers.CharField(source='job_seeker.user.lastName', read_only=True)
    githubUrl = serializers.URLField(source='job_seeker.github_url', read_only=True)
    linkedinUrl = serializers.URLField(source='job_seeker.linkedin_url', read_only=True)
    status = serializers.CharField(read_only=True)
    notes = serializers.CharField(read_only=True)
    createdAt = serializers.DateTimeField(read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)

    # Writable fields
    job_seeker_id = serializers.IntegerField(write_only=True)
    recruiter_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = RecruiterTracking
        fields = [
            'recruitmentId',
            'companyName',
            'companyInfo',
            'job_seeker',
            'job_seeker_id',
            'firstName',
            'lastName',
            'githubUrl',
            'linkedinUrl',
            'status',
            'status_display',
            'notes',
            'createdAt',
            'recruiter_id'  # Add this to fields
        ]

    def create(self, validated_data):
        # Handle the creation with the writable fields
        job_seeker_id = validated_data.pop('job_seeker_id')
        recruiter_id = validated_data.pop('recruiter_id')
        
        # Get the related objects
        job_seeker = JobSeeker.objects.get(user__id=job_seeker_id)
        recruiter = Recruiter.objects.get(id=recruiter_id)
        
        # Create the tracking record
        tracking = RecruiterTracking.objects.create(
            job_seeker=job_seeker,
            recruiter=recruiter,
            **validated_data
        )
        return tracking
    
class RecruiterTrackingUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecruiterTracking
        fields = ['status', 'notes']
        extra_kwargs = {
            'status': {'required': False},
            'notes': {'required': False}
        }