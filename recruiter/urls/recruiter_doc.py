from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ..views.recruiter_doc_management import (RecruiterDocDetailView,RecruiterDocView)

urlpatterns =[
    path('upload/', RecruiterDocView.as_view(), name='recruiter-documents'),
    path('documents/<int:doc_id>/', RecruiterDocDetailView.as_view(), name='recruiter-document-detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)