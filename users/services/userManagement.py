from ..repositories.user_management_repository import UserManagementRepository
from ..models import User
from typing import Optional, Union
from django.utils import timezone
from django.db import models

class UserManagementService:
    def __init__(self):
        self.user_repo = UserManagementRepository()

    def toggle_suspension(self, user_id: int) -> Optional[User]:
        try:
            user = self.user_repo.get_by_id(user_id)
            user.is_suspended = not user.is_suspended
            user.save()
            return user
        except User.DoesNotExist:
            raise ValueError("User does not exist.")
        except Exception:
            raise ValueError("An error occurred while processing the suspension request.")

    def toggle_pending_status(self, user_id: int) -> Optional[User]:
        try:
            user = self.user_repo.get_by_id(user_id)
            user.is_pending = not user.is_pending
            user.save()
            return user
        except User.DoesNotExist:
            raise ValueError("User does not exist.")
        except Exception:
            raise ValueError("An error occurred while processing the pending status request.")

    def toggle_verification(self, user_id: int) -> Optional[User]:
        try:
            user = self.user_repo.get_by_id(user_id)
            user.isVerified = not user.isVerified
            user.save()
            return user
        except User.DoesNotExist:
            raise ValueError("User does not exist.")
        except Exception:
            raise ValueError("An error occurred while updating verification status.")

    def delete_user(self, user_id: int, deleted_by: User, reason: Optional[str] = None) -> dict:
        try:
            user = self.user_repo.get_by_id(user_id)
            user.is_deleted = True
            user.is_active = False
            user.deleted_by = deleted_by.id
            user.deleted_at = timezone.now()
            user.deletion_reason = reason
            user.save()

            return {
                'status': 'success',
                'message': f'{user.firstName} successfully deleted.',
                'data': {
                    'user_id': user.id,
                    'deleted_by': deleted_by.email,
                    'deleted_at': user.deleted_at,
                    'deletion_reason': user.deletion_reason,
                }
            }
        except User.DoesNotExist:
            return {
                'status': 'error',
                'message': 'User does not exist.',
                'code': 404
            }
        except Exception as e:
            return {
                'status': 'error',
                'message': 'An unexpected error occurred while deleting the user.',
                'details': str(e),
                'code': 500
            }

    def restore_user(self, user_id: int, restored_by: User) -> dict:
        try:
            user = self.user_repo.get_by_id(user_id)
            user.is_deleted = False
            user.is_active = True
            user.save()

            return {
                'status': 'success',
                'message': f'User {user.id} successfully restored.',
                'data': {
                    'user_id': user.id,
                    'restored_by': restored_by.email,
                    'restored_at': timezone.now()
                }
            }
        except User.DoesNotExist:
            return {
                'status': 'error',
                'message': 'User does not exist.',
                'code': 404
            }
        except Exception as e:
            return {
                'status': 'error',
                'message': 'An unexpected error occurred while restoring the user.',
                'details': str(e),
                'code': 500
            }

    def list_users(self, include_deleted: bool = False) -> Union[models.QuerySet, dict]:
        try:
            if include_deleted:
                return self.user_repo.get_all()
            return self.user_repo.fetch_active_users()
        except Exception as e:
            return {
                'status': 'error',
                'message': 'Failed to fetch user list.',
                'details': str(e),
                'code': 500
            }
