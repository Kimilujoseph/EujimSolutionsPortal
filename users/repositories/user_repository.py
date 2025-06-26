from ..models import User
from django.contrib.auth.hashers import make_password, check_password
from .base_repository import BaseRepository
from typing import Optional


class UserRepository(BaseRepository[User]):
    def __init__(self):
        super().__init__(User)

    def create_user(self, user_data: dict) -> User:    
        user = self.model_class(**user_data)
        user.full_clean()
        user.save()
        return user
       

    def find_by_email(self, email: str) -> Optional[User]:
        return self.model_class.objects.filter(email__iexact=email).first()

    def verify_credentials(self, email: str, password: str) -> Optional[User]:
        user = self.find_by_email(email)
        if not user:
            return None
        if user and user.password and check_password(password, user.password):
            return user
        return None

    def update_user(self, user_id: int, update_data: dict) -> User:
        user = self.get_by_id(user_id)
        for key, value in update_data.items():
            setattr(user, key, value)
        user.save()
        return user

    def verify_user_email(self, verification_code: str) -> bool:
        try:
            user = self.model_class.objects.get(
                verificationCode=verification_code,
                isVerified=False
            )
            user.isVerified = True
            user.save()
            return True
        except self.model_class.DoesNotExist:
            return False
