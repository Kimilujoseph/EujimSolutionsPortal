from django.urls import path
from ..views.userManagmentViews import (AdminUserListView,AdminUserRestoreView,AdminUserDeleteView,AdminTogglePendingStatusView,AdminToggleSuspendUserView,AdminToggleVerificationView)


urlpatterns = [
    path('admin/user/<int:user_id>/delete/', AdminUserDeleteView.as_view(), name='admin-user-delete'),
    path('admin/user/<int:user_id>/restore/', AdminUserRestoreView.as_view(), name='admin-user-restore'),
    path('admin/user/<int:user_id>/toggle-suspend/', AdminToggleSuspendUserView.as_view(), name='admin-user-suspend'),
    path('admin/user/<int:user_id>/toggle-pending/', AdminTogglePendingStatusView.as_view(), name='admin-user-pending'),
    path('admin/user/<int:user_id>/toggle-verify/', AdminToggleVerificationView.as_view(), name='admin-user-verify'),
    path('admin/users/all/', AdminUserListView.as_view(), name='admin-user-list'),
]
