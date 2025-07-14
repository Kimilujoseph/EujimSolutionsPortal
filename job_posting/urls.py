from django.urls import include, path,re_path
from . import consumers
from .views.job_posting_list_view import JobPostingListView
from .views.job_posting_detail_view import JobPostingDetailView
from .views.job_posting_create_view import JobPostingCreateView
from .views.job_posting_skill_view import JobPostingAddingRequiredSkills
from .views.recruiter_job_posting_list_view import RecruiterJobPostingListView
urlpatterns = [
    path('job-postings/', JobPostingListView.as_view(), name='job-posting-list'),
    path('job-postings/<int:pk>/', JobPostingDetailView.as_view(), name='job-posting-detail'),
    path('job-postings/create/', JobPostingCreateView.as_view(), name='job-posting-create'),
    path('job-postings/add-skills/<int:job_posting_id>/',JobPostingAddingRequiredSkills.as_view(),name='job-adding-skills'),
     path('recruiter-job-postings/', RecruiterJobPostingListView.as_view(), name='recruiter-job-posting-list'),
    path('recruiter-job-postings/<int:recruiter_id>/', RecruiterJobPostingListView.as_view(), name='recruiter-job-posting-list'),
    path('job-postings/<int:job_posting_id>/delete-skill/<int:skill_id>/',JobPostingAddingRequiredSkills.as_view(), name='job-posting-delete-skill'),
]
websocket_urlpatterns = [
    re_path(r'ws/jobs/feed/$', consumers.JobFeedConsumer.as_asgi()),
]