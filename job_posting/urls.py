from django.urls import include, path
from .views.job_posting_view import JobPostingListView,JobPostingDetailView,JobPostingCreateView,JobPostingAddingRequiredSkills
urlpatterns = [
    path('job-postings/', JobPostingListView.as_view(), name='job-posting-list'),
    path('job-postings/<int:pk>/', JobPostingDetailView.as_view(), name='job-posting-detail'),
    path('job-postings/create/', JobPostingCreateView.as_view(), name='job-posting-create'),
    path('job-postings/add-skills/<int:job_posting_id>/',JobPostingAddingRequiredSkills.as_view(),name='job-adding-skills'),
    path('job-postings/<int:job_posting_id>/delete-skill/<int:skill_id>/',JobPostingAddingRequiredSkills.as_view(), name='job-posting-delete-skill'),
]