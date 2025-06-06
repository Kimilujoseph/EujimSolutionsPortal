from  django.urls import include, path

urlpatterns = [
    path('/recruiter/', include("recruiter.urls.recruiter_profile")),
    path('/recruiter/documents/', include("recruiter.urls.recruiter_doc")),
    #path('/recruiter/tracking/', include("recruiter.urls.recruiter_tracking")),
]