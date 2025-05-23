from django.urls import path

from ..views.userAuthViews import (RegisterView,VerifyEmail,LoginView,LogoutView,RegisterEmployerView)

urlpatterns = [
    path('register',RegisterView.as_view(),name= 'register'),
    path('register/employer',RegisterEmployerView.as_view(),name='employerRegister'),
    path('verify-email/<str:verification_code>/', VerifyEmail.as_view(), name='verify-email'),
    path('login',LoginView.as_view(),name='login'),
    path('logout',LogoutView.as_view(),name='logout')
]