from django.urls import path
from ..views.education_view import EducationView, EducationDetailView


urlpatterns = [
    path('educations/', EducationView.as_view(), name='educations'),
    path('educations/<int:education_id>/', EducationDetailView.as_view(), name='education-detail'),
]