from django.urls import include,path

urlpatterns = [
    path('/graduate/',include("jobseeker.urls.auth")),
]