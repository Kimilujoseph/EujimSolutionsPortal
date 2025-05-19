from django.contrib import admin

# Register your models here.
from .models import JobSeeker,JobSeekerCertification

admin.site.register(JobSeeker)
admin.site.register(JobSeekerCertification)