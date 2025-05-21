from ..models import User;
from .base_repository import BaseRepository
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from typing import Optional

class UserManagementRepository(BaseRepository[User]):
    def __init__(self):
        super().__init__(User)
    def is_suspending(self,user_id:int) ->Optional[User]:
      try:
         user = self.get_by_id(user_id)
         user.is_suspended = not user.is_suspended
         user.save()
         user.save()
         return user
      except self.model_class.DoesNotExist:
         raise ValueError("user does not exist")
      except Exception as e:
        raise ValueError("problem occurred during the processing of request")
    def is_pending(self,user_id:int) ->Optional[User]:
      try:
         user =  self.get_by_id(user_id)
         user.is_pending = not user.is_pending
         user.save()
         return user
      except self.model_class.DoesNotExist:
         raise ValueError("user does not exist")
      except Exception as e:
        raise ValueError("problem occurred during the processing of request")
   
    def is_verified(self,user_id:int) -> Optional[User]:
       try:
          user =  self.get_by_id(user_id)
          user.isVerified  = not user.isVerified
          user.save()
          return user
       except self.model_class.DoesNotExist:
          raise ValueError("user does not exist")
       except Exception as e:
          raise ValueError("problem when updating email")

    def soft_deletion(self,user_id:int) ->Optional[User]:
      try:
         user =  self.get_by_id(user_id)
         user.is_deleted = True
         user.is_active = False
         user.save()
         return user
      except self.model_class.DoesNotExist:
         raise ValueError("user does not exist")
      except Exception as e:
        raise ValueError("problem occurred during the processing of request")
      
    def user_restoration(self,user_id:int) -> Optional[User]:
       try:
          user = self.get_by_id(user_id)
          user.is_deleted = False
          user.is_active = True
          user.save()
          return user
       except self.model_class.DoesNotExist:
          raise ValueError("user does not exist")
       except Exception as e:
          raise ValueError("problem occured when processing the request")
       
    def fetchActive_users(self) -> Optional[User]:
       try:
         return  self.filter(is_Deleted = False)
       except Exception as e:
          raise ValueError("problem occurred while processing the request")
    
    def fetch_deleted_users(self) -> Optional[User]:
       try:
          return self.filter(is_Deleted = True)
       except Exception as e:
          raise ValueError("problem occured while processing the request")
      