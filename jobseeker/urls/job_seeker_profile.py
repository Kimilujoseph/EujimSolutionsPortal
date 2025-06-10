from django.urls import path
from ..views.job_seeker_profile import (JobSeekerProfileView,JobSeekerCreateOrUpdateProfile,JobSeekerSkillsView,SkillListView,JobSeekerUpdateSkill,JobSeekerAnalyticsView,JobSeekerDeleteSkill,CertificationListAPIView,CertificationDetailAPIView,CertificationAddAPIView,CertificationDeleteAPIView)

urlpatterns = [
    path('profile/', JobSeekerProfileView.as_view(), name='jobseeker-profile'),
    path('profile/<int:user_id>/', JobSeekerProfileView.as_view(), name='jobseeker-profile-detail'),
    path('profile/create-or-update', JobSeekerCreateOrUpdateProfile.as_view(), name='jobseeker-create-or-update'),
    path('profile/skills/', JobSeekerSkillsView.as_view(), name='jobseeker-skills'),
    path('profile/skills/add/', JobSeekerUpdateSkill.as_view(), name='jobseeker-add-skill'),
    path('profile/skills/delete/<int:skill_id>/', JobSeekerDeleteSkill.as_view(),name='jobseeker-delete-skill'),
    path('skills/', SkillListView.as_view(), name='skill-list'),
    path('profile/analytics/', JobSeekerAnalyticsView.as_view(), name='jobseeker-analytics_individual'),
    path('profile/analytics/<int:user_id>/', JobSeekerAnalyticsView.as_view(), name='jobseeker-analytics'),
    path('certifications/', CertificationListAPIView.as_view(), name='jobseeker-certifications'),
    path('certifications/<int:certification_id>/',CertificationDetailAPIView.as_view(), name='jobseeker-certification-detail'),
    path('certifications/add/',CertificationAddAPIView.as_view(),name='jobseeker-add-certification'),
    path('certifications/<int:certification_id>/delete/',CertificationDeleteAPIView.as_view(),name='jobseeker-delete-certification'),
]