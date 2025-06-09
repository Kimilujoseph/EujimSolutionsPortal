from rest_framework import serializers
from ..urls.tokens import password_reset_token
from ..utils import send_password_reset_email
from ..models import User

class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):

        if not User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("User with this email does not exist.")
        return value

    def save(self, request):
        user = User.objects.get(email__iexact=self.validated_data['email'])
        token = password_reset_token.make_token(user)
        send_password_reset_email(user, request, token)

        
class PasswordResetConfirmSerializer(serializers.Serializer):
    uid = serializers.IntegerField()
    token = serializers.CharField()
    new_password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        from django.contrib.auth import get_user_model
        User = get_user_model()

        try:
            user = User.objects.get(id=attrs['uid'])
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid user")

        if not password_reset_token.check_token(user, attrs['token']):
            raise serializers.ValidationError("Invalid or expired token")

        attrs['user'] = user
        return attrs

    def save(self):
        user = self.validated_data['user']
        user.set_password(self.validated_data['new_password'])
        user.save()


