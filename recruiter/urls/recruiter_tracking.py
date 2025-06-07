from django.urls import path
from ..views.recruiter_tracking_views import (RecruiterTrackingDetailView,RecruiterTrackingListView)
urlpatterns = [
  path('tracking/', RecruiterTrackingListView.as_view(), name='recruiter_tracking_list'),
  path('tracking/user/<int:user_id>/', RecruiterTrackingListView.as_view(), name='recruiter_tracking_detail'),
]