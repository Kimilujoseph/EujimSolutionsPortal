from django.urls import path

from ..views import (RegisterView,VerifyEmail)

urlpatterns = [
    path('register',RegisterView.as_view(),name= 'register'),
    path('verify-email/<str:verification_code>/', VerifyEmail.as_view(), name='verify-email'),
]