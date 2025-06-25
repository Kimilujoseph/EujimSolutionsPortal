from ..repositories.user_repository import UserRepository
from ..serializers.userRegistration import UserRegistrationSerializer
from ..models import User
from typing  import Tuple
import jwt
from django.conf import settings
from django.shortcuts import redirect
from datetime import datetime,timedelta,timezone
from rest_framework.exceptions import AuthenticationFailed, ValidationError,APIException
from django.db import IntegrityError, DatabaseError
from ..exceptions import (ServiceException, NotFoundException, ConflictException, InternalErrorException)
from ..utils import send_verification_email

class AuthService:
    def __init__(self):
        self.user_repo: UserRepository = UserRepository()

    def register_user(self, registration_data: dict,request) -> str:
        try:
            serializer = UserRegistrationSerializer(data=registration_data)
            serializer.is_valid(raise_exception=True)
            if not isinstance(serializer.validated_data, dict):
             raise  ServiceException('Validated data is not a valid dictionary')
            user = self.user_repo.create_user(serializer.validated_data)
            send_verification_email(user, request)
            message=f'User {user.firstName} registered successfully. Verification email sent.'
            return message
        except ValidationError as e:
            raise ServiceException(f"Validation error: {e.detail}")
        except (IntegrityError, DatabaseError) as e:
            raise InternalErrorException("Database error occurred while creating user.")
        except Exception as e:
            raise InternalErrorException("Unexpected error during user registration.")

    def verify_email(self, verification_code: str) -> str:
        try:
            user= self.user_repo.verify_user_email(verification_code)
            if user:
               frontend_login_url =f"{settings.FRONTEND_URL}/login"
               return frontend_login_url
            else:
                frontend_expired_url = f"{settings.FRONTEND_URL}/token-expired"
                return frontend_expired_url
        except User.DoesNotExist:
            raise NotFoundException("User with this verification code does not exist.")
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
            'id': user.pk,
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