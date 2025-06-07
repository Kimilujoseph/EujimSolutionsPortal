from  ..models import Recruiter
from rest_framework import serializers

class RecruiterRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruiter
        fields = ['companyName', 'companyEmail', 'industry', 'contactInfo', 'description']
        extra_kwargs = {'companyEmail': {'required': True}}


