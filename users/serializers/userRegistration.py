import re
from rest_framework import serializers
from ..models import User
class UserRegistrationSerializer(serializers.Serializer):
    firstName = serializers.CharField(max_length=45)
    secondName = serializers.CharField(max_length=45)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    role = serializers.CharField()

    def validate_email(self, value):
        
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value.lower()

    def validate_role(self, value):
        allowed_roles = [r[0] for r in User.ROLE_ENUM] 
        if value not in allowed_roles:
            raise serializers.ValidationError(
                f"Invalid role. Must be one of: {', '.join(allowed_roles)}"
            )
        return value

    def validate_password(self, value):
        # Require at least one uppercase, one lowercase, one digit, and one special char
        if (
            not re.search(r'[A-Z]', value) or
            not re.search(r'[a-z]', value) or
            not re.search(r'\d', value) or
            not re.search(r'[!@#$%^&*(),.?":{}|<>]', value)
        ):
            raise serializers.ValidationError(
                "Password must contain at least one uppercase letter, one lowercase letter, "
                "one number, and one special character."
            )
        return value
