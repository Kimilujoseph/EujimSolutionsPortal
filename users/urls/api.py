
from django.urls import include,path

urlpatterns = [
    path('/auth/',include("users.urls.auth")),
    path('/manage/',include("users.urls.usermanagement"))
]