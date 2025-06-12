from ..models import User
from .base_repository import BaseRepository
from typing import Optional

class UserManagementRepository(BaseRepository[User]):
    def __init__(self):
        super().__init__(User)

    def fetch_active_users(self,role):
        return self.filter(is_deleted=False,role=role)

    def fetch_deleted_users(self):
        return self.filter(is_deleted=True)
    def get_user_with_related(self,user_id):
        return User.objects.select_related('jobseeker_profile').prefetch_related('recruiters').get(id=user_id)
    def fetch_users_by_role(self,role):
        return self.filter(role=role)
    # def fetch_all_users(self):
    #     return self.get_all(self)



