from django.urls import include,path

urlpatterns = [
    path('auth/',include("users.urls.auth")),
    path('list/',include("users.urls.userlist"))
]