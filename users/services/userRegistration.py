from ..repositories.user_repository import UserRepository
from ..serializers.userRegistration import UserRegistrationSerializer
from ..models import User
from typing  import Tuple
import jwt
from django.conf import settings
from datetime import datetime,timedelta,timezone
from rest_framework.exceptions import AuthenticationFailed
class AuthService:
    def __init__(self):
        self.user_repo:UserRepository = UserRepository()

    def register_user(self,registration_data:dict) -> User:
        serializer = UserRegistrationSerializer(data=registration_data)
        serializer.is_valid(raise_exception = True)
        return self.user_repo.create_user(serializer.validated_data)
    def verify_email(self, verification_code: str) -> bool:
        return self.user_repo.verify_user_email(verification_code)
    def login_user(self, email: str, password: str) -> Tuple[User, str]:
        user = self.user_repo.verify_credentials(email, password)
        if not user:
            raise AuthenticationFailed('Invalid credentials')
        if not user.isVerified:
            raise AuthenticationFailed('Email not verified')
        
        token = self._generate_jwt_token(user)
        return user, token

    def _generate_jwt_token(self, user: User) -> str:
        payload = {
            'id': user.id,
            'email': user.email,
            'role': user.role,
            'verified':user.isVerified,
            'exp': datetime.now(timezone.utc) + timedelta(days=1),
            'iat': datetime.now(timezone.utc)
        }
        return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    def verify_admin(self, request) -> User:
        token = request.COOKIES.get('jwt')
        
        if not token:
            raise AuthenticationFailed('Unauthenticated')
        
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token expired')
        except:
            raise AuthenticationFailed('Invalid token')

        user = self.user_repo.get_by_id(payload['id'])
        if not user or user.role != 'admin':
            raise AuthenticationFailed('Admin privileges required')
        
        return user