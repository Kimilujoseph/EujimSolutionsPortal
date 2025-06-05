# serializers.py
from rest_framework import serializers
from .models import Recruiter, RecruiterDoc, RecruiterTracking

class RecruiterRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruiter
        fields = ['companyName', 'companyLogo', 'industry', 'contactInfo', 'companyEmail', 'description']
        extra_kwargs = {
            'companyEmail': {'required': True},
            'companyName': {'required': True}
        }

class RecruiterProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruiter
        fields = '__all__'
        read_only_fields = ['user', 'isVerified', 'createdAt', 'updatedAt']

class RecruiterDocSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecruiterDoc
        fields = '__all__'
        read_only_fields = ['recruiter', 'status', 'createdAt', 'updatedAt']

class RecruiterTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecruiterTracking
        fields = '__all__'
        read_only_fields = ['recruiter', 'createdAt', 'updatedAt']