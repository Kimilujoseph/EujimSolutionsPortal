# urls.py
from django.urls import path
from .search_view import JobSeekerSearchView

urlpatterns = [
    path('search/jobseekers/', JobSeekerSearchView.as_view(), name='jobseeker-search'),
]