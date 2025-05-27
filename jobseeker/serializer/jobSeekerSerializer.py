from  rest_framework import serializers
from ..models import JobSeeker

class JobSeekerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobSeeker
        fields = [
            'id',
            'user_id',
            'first_name',
            'last_name',
            'phone_number',
            'address',
            'city',
            'country',
            'postal_code',
            'date_of_birth',
            'gender',
            'bio',
            'profile_picture',
            'resume',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['id', 'user_id', 'created_at', 'updated_at']
        extra_kwargs = {
            'date_of_birth': {'required': False},
            'profile_picture': {'required': False},
            'resume': {'required': False}
        }

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Add user email if needed
        if hasattr(instance.user, 'email'):
            representation['email'] = instance.user.email
        return representation