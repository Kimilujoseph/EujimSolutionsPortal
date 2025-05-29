from django.urls import path
from ..views.education_view import EducationView, EducationDetailView,EducationCreateView


urlpatterns = [
    path('view/', EducationView.as_view(), name='educations'),
    path('create', EducationCreateView.as_view(), name='education-create'),
    path('education/<int:education_id>/', EducationDetailView.as_view(), name='education-detail'),
]