from django.urls import path
from ..views.job_seeker_recruiter_tracking import Job_seeker_Recruitment_tracking

urlpatterns = [
    path('create/', Job_seeker_Recruitment_tracking.as_view(), name='job-seeker-recruitment-tracking-create'),   
]