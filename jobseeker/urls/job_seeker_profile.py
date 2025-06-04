from django.urls import path
from ..views.job_seeker_profile import (JobSeekerProfileView,JobSeekerCreateOrUpdateProfile,JobSeekerSkillsView,SkillListView,JobSeekerUpdateSkill,CertificationListAPIView,CertificationDetailAPIView,CertificationAddAPIView,CertificationDeleteAPIView)

urlpatterns = [
    path('profile/', JobSeekerProfileView.as_view(), name='jobseeker-profile'),
    path('profile/<int:user_id>/', JobSeekerProfileView.as_view(), name='jobseeker-profile-detail'),
    path('profile/create-or-update', JobSeekerCreateOrUpdateProfile.as_view(), name='jobseeker-create-or-update'),
    path('profile/skills/', JobSeekerSkillsView.as_view(), name='jobseeker-skills'),
    path('profile/skills/add/', JobSeekerUpdateSkill.as_view(), name='jobseeker-add-skill'),
    path('skills/', SkillListView.as_view(), name='skill-list'),
    path('certifications/', CertificationListAPIView.as_view(), name='jobseeker-certifications'),
    path('certifications/<int:certification_id>/',CertificationDetailAPIView.as_view(), name='jobseeker-certification-detail'),
    path('certifications/add/',CertificationAddAPIView.as_view(),name='jobseeker-add-certification'),
    path('certifications/<int:certification_id>/delete/',CertificationDeleteAPIView.as_view(),name='jobseeker-delete-certification'),
]