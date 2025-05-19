from rest_framework import serializers
from ..models import User

class UserRegistrationSerializer(serializers.Serializer):
    firstName = serializers.CharField(max_length=45)
    secondName = serializers.CharField(max_length=45)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    
    def validate_email(self, value):
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value.lower()

  