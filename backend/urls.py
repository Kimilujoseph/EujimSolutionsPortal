
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include("users.urls.api")),
    path('api/v1', include("jobseeker.urls.api")),
    path('api/v1',include("recruiter.urls.api")),
    path('api/v1/', include("search.api")),
    path('api/v1/',include("job_posting.urls")),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico')))
]