from django.contrib import admin

# Register your models here.

from .models import Recruiter,RecruiterDoc,RecruiterTracking

admin.site.register(Recruiter,RecruiterDoc,RecruiterTracking)