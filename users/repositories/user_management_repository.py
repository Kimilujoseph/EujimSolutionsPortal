from ..models import User
from .base_repository import BaseRepository
from typing import Optional

class UserManagementRepository(BaseRepository[User]):
    def __init__(self):
        super().__init__(User)

    def fetch_active_users(self):
        return self.filter(is_deleted=False)

    def fetch_deleted_users(self):
        return self.filter(is_deleted=True)
