from django.urls import path
from ..views.recruiter_profile_managment import (RecruiterRegistrationView,RecruiterProfileView)

urlpatterns = [
    path('register', RecruiterRegistrationView.as_view(), name='recruiter-register'),
    path('profile/', RecruiterProfileView.as_view(), name='recruiter-profile'),
    path('profile/<int:user_id>',RecruiterProfileView.as_view(),name='recruiter-personal-profile')
]