from ..models import User
from django.contrib.auth.hashers import make_password, check_password
from .base_repository import BaseRepository
from typing import Optional


class UserRepository(BaseRepository[User]):
    def __init__(self):
        super().__init__(User)

    def create_user(self, user_data: dict) -> User:
        try:
            user_data["password"] = make_password(user_data["password"])
            user = self.model_class(**user_data)
            user.full_clean()
            user.save()
            return user
        except ValidationError as e:
            # e.message_dict will contain field-specific errors
            role_errors = e.message_dict.get("role", None)
            if role_errors:
                raise ValueError("Invalid role added, please check with the admin.")
            raise ValueError("Validation error occurred while creating user.")
        except IntegrityError:
            raise ValueError("Email must be unique or required fields are missing.")
        except Exception:
            raise ValueError("Something went wrong while creating the user.")

    def find_by_email(self, email: str) -> Optional[User]:
        return self.model_class.objects.filter(email__iexact=email).first()

    def verify_credentials(self, email: str, password: str) -> Optional[User]:
        user = self.find_by_email(email)
        if user and check_password(password, user.password):
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
