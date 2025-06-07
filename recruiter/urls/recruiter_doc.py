from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ..views.recruiter_doc_management import (RecruiterDocView,RecruiterDocDowload,RecruiterDocVerificationView)

urlpatterns =[
    path('upload/', RecruiterDocView.as_view(), name='recruiter-documents'),
    path('upload/<int:user_id>',RecruiterDocView.as_view(),name='recruiter-documents-fetching'),
    path('<int:doc_id>/download/', RecruiterDocDowload.as_view(), name='recruiter-document-download'),
    path('upload/<int:doc_id>/', RecruiterDocView.as_view(), name='recruiter-document-detail'),
    path('verify/<int:doc_id>/', RecruiterDocVerificationView.as_view(), name='recruiter-document-verification'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)