from ..repositories.user_repository import UserRepository
from ..serializers.userRegistration import UserRegistrationSerializer
from ..models import User
class AuthService:
    def __init__(self):
        self.user_repo:UserRepository = UserRepository()

    def register_user(self,registration_data:dict) -> User:
        serializer = UserRegistrationSerializer(data=registration_data)
        serializer.is_valid(raise_exception = True)
        return self.user_repo.create_user(serializer.validated_data)
    def verify_email(self, verification_code: str) -> bool:
        return self.user_repo.verify_user_email(verification_code)
  