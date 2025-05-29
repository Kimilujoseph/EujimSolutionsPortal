from django.urls import include,path

urlpatterns = [
    path('/graduate/',include("jobseeker.urls.job_seeker_profile")),
    path('/graduate/education/', include("jobseeker.urls.education_profile")),
]