from rest_framework import serializers
from ..models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'firstName', 'lastName', 'email', 'role', 'is_active', 'is_deleted', 'is_suspended', 'is_pending', 'isVerified', 'createdAt', 'updatedAt']
