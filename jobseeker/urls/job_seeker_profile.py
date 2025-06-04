from django.urls import path

from ..views.job_seeker_profile import (JobSeekerProfileView,JobSeekerCreateOrUpdateProfile,JobSeekerSkillsView,SkillListView,JobSeekerUpdateSkill,JobSeekerAnalyticsView,JobSeekerDeleteSkill)

urlpatterns = [
    path('profile/', JobSeekerProfileView.as_view(), name='jobseeker-profile'),
    path('profile/<int:user_id>/', JobSeekerProfileView.as_view(), name='jobseeker-profile-detail'),
    path('profile/create-or-update', JobSeekerCreateOrUpdateProfile.as_view(), name='jobseeker-create-or-update'),
    path('profile/skills/', JobSeekerSkillsView.as_view(), name='jobseeker-skills'),
    path('profile/skills/add/', JobSeekerUpdateSkill.as_view(), name='jobseeker-add-skill'),
    path('profile/skills/delete/<int:skill_id>/', JobSeekerDeleteSkill.as_view(),name='jobseeker-delete-skill'),
    path('skills/', SkillListView.as_view(), name='skill-list'),
    path('profile/analytics/', JobSeekerAnalyticsView.as_view(), name='jobseeker-analytics'),
]