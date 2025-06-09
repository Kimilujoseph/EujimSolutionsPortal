from ..repositories.user_repository import UserRepository
from ..serializers.userRegistration import UserRegistrationSerializer
from ..models import User
from typing  import Tuple
import jwt
from django.conf import settings
from datetime import datetime,timedelta,timezone
from rest_framework.exceptions import AuthenticationFailed, ValidationError,APIException
from django.db import IntegrityError, DatabaseError

class AuthService:
    def __init__(self):
        self.user_repo: UserRepository = UserRepository()

    def register_user(self, registration_data: dict) -> User:
        try:
            serializer = UserRegistrationSerializer(data=registration_data)
            serializer.is_valid(raise_exception=True)
            return self.user_repo.create_user(serializer.validated_data)
        except ValidationError as e:
            raise e
        except (IntegrityError, DatabaseError) as e:
            raise APIException("Database error occurred while creating user.")
        except Exception as e:
            raise APIException("Unexpected error during user registration.")

    def verify_email(self, verification_code: str) -> bool:
        try:
            return self.user_repo.verify_user_email(verification_code)
        except Exception:
            raise APIException("Error verifying email.")

    def login_user(self, email: str, password: str) -> Tuple[User, str]:
        user = self.user_repo.verify_credentials(email, password)
        if not user:
            raise AuthenticationFailed('Invalid credentials')
        if not user.isVerified:
            raise AuthenticationFailed('Email not verified')
        return user, self._generate_jwt_token(user)

    def _generate_jwt_token(self, user: User) -> str:
        payload = {
            'id': user.id,
            'email': user.email,
            'firstName': user.firstName,
            'secondName': user.lastName,
            'role': user.role,
            'isVerified': bool(user.isVerified),
            'is_active': bool(user.is_active),
            'is_deleted': bool(user.is_deleted),
            'is_pending': bool(user.is_pending),
            'is_suspended': bool(user.is_suspended),
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
        except jwt.DecodeError:
            raise AuthenticationFailed('Invalid token')
        user = self.user_repo.get_by_id(payload['id'])
        if not user or user.role != 'admin':
            raise AuthenticationFailed('Admin privileges required')
        return user