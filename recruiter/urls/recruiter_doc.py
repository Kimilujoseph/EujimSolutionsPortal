from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ..views.recruiter_doc_management import (RecruiterDocView,RecruiterDocDowload)

urlpatterns =[
    path('upload/', RecruiterDocView.as_view(), name='recruiter-documents'),
    path('<int:doc_id>/download/', RecruiterDocDowload.as_view(), name='recruiter-document-download'),
    path('upload/<int:doc_id>/', RecruiterDocView.as_view(), name='recruiter-document-detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)