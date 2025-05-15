from django.urls import include,path

urlpatterns = [
    path('auth/',include("usermanagement.urls.auth"))
]