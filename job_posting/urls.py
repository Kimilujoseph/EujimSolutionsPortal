from django.urls import include, path
from .views.job_posting_view import JobPostingListView,JobPostingDetailView

urlpatterns = [
    path('job-postings/', JobPostingListView.as_view(), name='job-posting-list'),
    path('job-postings/<int:pk>/', JobPostingDetailView.as_view(), name='job-posting-detail'),
]