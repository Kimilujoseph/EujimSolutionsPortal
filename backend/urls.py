
from django.contrib import admin
from django.urls import path,include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1',include("users.urls.api")),
    path('api/v1', include("jobseeker.urls.api")),
]