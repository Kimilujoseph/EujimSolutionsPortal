from ..repositories.user_repository import UserRepository
from ..serializers.userRegistration import UserRegistrationSerializer

class AuthService:
    def __init__(self):
        self.user_repo = UserRepository()

    def register_user(self,registration_data:dict):
        serializer = UserRegistrationSerializer(data=registration_data)
        serializer.is_valid(raise_exception = True)
        return self.user_repo.create_user(serializer.validated_data)