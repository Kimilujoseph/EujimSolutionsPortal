from django.urls import path
from ..views.userManagmentViews import (AdminUserListView,AdminUserRestoreView,AdminUserDeleteView)


urlPattern = [
  path('user/<int:user_id>/delete/', AdminUserDeleteView.as_view(), name='admin-user-delete'),

]