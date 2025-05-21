from django.urls import path
from ..views.userManagmentViews import (AdminUserListView,AdminUserRestoreView,AdminUserDeleteView,AdminTogglePendingStatusView,AdminToggleSuspendUserView,AdminToggleVerificationView)


urlPattern = [
  path('user/<int:user_id>/delete/', AdminUserDeleteView.as_view(), name='admin-user-delete'),
  path('user/<int:user_id>/restore',AdminUserRestoreView.as_view(),name='admin-user-restore'),
  path('users/<int:user_id>/toggle-suspend/', AdminToggleSuspendUserView.as_view(),name='admin-user-suspended'),
  path('users/<int:user_id>/toggle-pending/', AdminTogglePendingStatusView.as_view(),name='admin-user-pending'),
  path('users/<int:user_id>/toggle-verify/', AdminToggleVerificationView.as_view(),name='admin-user-verify'),
]