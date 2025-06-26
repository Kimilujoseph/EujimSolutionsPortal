from django.urls import path
from ..views.userManagmentViews import (AdminUserListView,AdminUserRestoreView,AdminUserDeleteView,AdminTogglePendingStatusView,AdminToggleSuspendUserView,AdminToggleVerificationView,AdminUserDetailView,UserUpdateNamesView)
from ..views.admin_analytics_view import AdminDashboardView


urlpatterns = [
    path('admin/user/<int:user_id>/delete', AdminUserDeleteView.as_view(), name='admin-user-delete'),
    path('admin/user/<int:user_id>/restore', AdminUserRestoreView.as_view(), name='admin-user-restore'),
    path('admin/user/<int:user_id>/toggle-suspend', AdminToggleSuspendUserView.as_view(), name='admin-user-suspend'),
    path('admin/user/<int:user_id>/toggle-pending', AdminTogglePendingStatusView.as_view(), name='admin-user-pending'),
    path('admin/user/<int:user_id>/toggle-verify', AdminToggleVerificationView.as_view(), name='admin-user-verify'),
    path('admin/user/<int:user_id>/profile',AdminUserDetailView.as_view(),name='admin-user-view'),
    path('admin/dashboard/',AdminDashboardView.as_view(),name='admin_view_dashboard'), 
    path('admin/users/all/', AdminUserListView.as_view(), name='admin-user-list'),
    path('users/<int:user_id>/update-names', UserUpdateNamesView.as_view(), name='update-user-names'),
]
