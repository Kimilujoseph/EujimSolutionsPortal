from ..repositories.user_management_repository import UserManagementRepository
from ..models import User
from typing import Optional, Union
from django.utils import timezone
from django.db import models
from django.core.exceptions import ObjectDoesNotExist

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
        except Exception as e:
            print(f"Database error: {e}")
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
           raise ValueError('user does not exist')
          
        except Exception as e:
          raise ValueError("An error occured while processing the verification status request")
    def delete_user(self, user_id: int, deleted_by:dict, reason: Optional[str] = None) -> dict:
        try:
            user = self.user_repo.get_by_id(user_id)
            user.is_deleted = True
            user.is_active = False
            user.deleted_by = deleted_by['id']
            user.deleted_at = timezone.now()
            user.deletion_reason = reason
            user.save()

            return {
                'status': 'success',
                'message': f'{user.firstName} successfully deleted.',
                'data': {
                    'user_id': user.email,
                    'deleted_by': deleted_by["email"],
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

    def restore_user(self, user_id: int, restored_by:dict) -> dict:
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
                    'restored_by': restored_by["email"],
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

    def list_users(self, include_deleted: bool = False,role:Optional[str]= None) -> Union[models.QuerySet, dict]:
        try:
            if include_deleted:
                users = self.user_repo.fetch_users_by_role(role)
            users = self.user_repo.fetch_active_users(role)
          
            #print(users)
            return users

        except Exception as e:
            return {
                'status': 'error',
                'message': 'Failed to fetch user list.',
                'details': str(e),
                'code': 500
            }
        
    def get_user_with_profile(self, user_id):
        try:
            # Use both select_related and prefetch_related for performance
            user = self.user_repo.get_user_with_related(user_id)

            data = {
                'id': user.id,
                'email': user.email,
                'first_name': user.firstName,
                'second_name': user.lastName,
                'isVerified':user.isVerified,
                'isActive':user.is_active,
                'isDeleted':user.is_deleted,
                'isPending':user.is_pending,
                'role': user.role,
                
            }

            # If jobseeker profile exists
            if hasattr(user, 'jobseeker_profile'):
                js = getattr(user, 'jobseeker_profile', None)
                if js is None:
                    raise ValueError("Jobseeker profile not found for the user.")
                data['profile_type'] = 'jobseeker'
                data['profile'] = {
                    'github_url': js.github_url,
                    'linkedin_url': js.linkedin_url,
                    'location': js.location,
                    'bio_data': js.bioData,
                    'about': js.about,
                }

        
            elif hasattr(user,'recruiters'):

                recruiter = user.recruiters.first()
                if recruiter is None:
                    raise ValueError("recruiter profile not found for the user")

                data['profile_type'] = 'recruiter'
                data['profile'] = {
                    'company_name': recruiter.companyName,
                    'industry': recruiter.industry,
                    'contact_info': recruiter.contactInfo,
                    'company_email': recruiter.companyEmail,
                    'description': recruiter.description,
                    'is_verified': recruiter.isVerified,
                    'company_logo': recruiter.companyLogo,
                }
            else:
                data['profile_type'] = 'none'
                data['profile'] = {}

            return data

        except ObjectDoesNotExist:
            raise ValueError("User not found")
        
    def get_all_users(self):
        try:
            users = self.user_repo.fetch_all_users()
            return users
        except Exception as e:
            return {
                'status': 'error',
                'message': 'Failed to fetch all users.',
                'details': str(e),
                'code': 500
            }
    def update_user_names(self, user_id: int, first_name: str = None, last_name: str = None) -> dict:
        try:
            user = self.user_repo.get_by_id(user_id)
            
            if first_name is not None:
                user.firstName = first_name
            if last_name is not None:
                user.lastName = last_name
                
            user.save()
            
            return {
                'status': 'success',
                'message': 'User names updated successfully',
                'data': {
                    'user_id': user.id,
                    'first_name': user.firstName,
                    'last_name': user.lastName
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
                'message': 'An error occurred while updating user names',
                'details': str(e),
                'code': 500
            }    