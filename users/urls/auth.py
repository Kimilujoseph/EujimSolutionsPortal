from django.urls import path
from ..views.password_resetviews import PasswordResetRequestView, PasswordResetConfirmView
from ..views.userAuthViews import (RegisterView,VerifyEmail,LoginView,LogoutView,RegisterEmployerView)
from django.views.generic import TemplateView
urlpatterns = [
    path('register',RegisterView.as_view(),name= 'register'),
    path('register/employer',RegisterEmployerView.as_view(),name='employerRegister'),
    path('verify-email/<str:verification_code>/', VerifyEmail.as_view(), name='verify-email'),
    path('login',LoginView.as_view(),name='login'),
    path('logout',LogoutView.as_view(),name='logout'),
    path('request-reset-password', PasswordResetRequestView.as_view(), name='request-reset-password'),
    path('password-reset-confirm/<int:uid>/<str:token>', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),

    path('password-reset/done/', TemplateView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset/complete/', TemplateView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]