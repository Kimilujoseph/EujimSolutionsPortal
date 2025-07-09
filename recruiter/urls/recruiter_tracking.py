from django.urls import path
from ..views.recruiter_tracking_views import (RecruiterTrackingDetailView,RecruiterTrackingListView,Jobseeker_recruitment_trackingListView,JobApplicantsView)
urlpatterns = [
  path('tracking/', RecruiterTrackingListView.as_view(), name='recruiter_tracking_list'),
  path('tracking/<int:user_id>/', RecruiterTrackingListView.as_view(), name='recruiter_tracking_detail'),
  path('tracking/jobseeker/<int:user_id>/', Jobseeker_recruitment_trackingListView.as_view(), name='admin-jobseeker_recruitment_tracking_list'),
  path('tracking/jobseeker/', Jobseeker_recruitment_trackingListView.as_view(), name='jobseeker_recruitment_tracking_list'),
  path('tracking/manage/<int:tracking_id>/', RecruiterTrackingDetailView.as_view(), name='recruiter_tracking_detail'),
  path(
        'job-postings/<int:job_posting_id>/applicants/',
        JobApplicantsView.as_view(),
        name='job-applicants-list'
    )
]