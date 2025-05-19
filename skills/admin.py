from django.contrib import admin

# Register your models here.

from .models import Skill,SkillSet

admin.site.register(Skill)
admin.site.register(SkillSet)