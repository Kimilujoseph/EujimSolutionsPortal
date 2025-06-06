from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ..views.recruiter_doc_management import (RecruiterDocDetailView,RecruiterDocView,RecruiterDocDowload)

urlpatterns =[
    path('upload/', RecruiterDocView.as_view(), name='recruiter-documents'),
    path('<int:doc_id>/download/', RecruiterDocDowload.as_view(), name='recruiter-document-download'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)