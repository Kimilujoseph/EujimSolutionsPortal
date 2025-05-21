from django.urls import path

from ..views.userAuthViews import (RegisterView,VerifyEmail,LoginView,LogoutView)

urlpatterns = [
    path('register/',RegisterView.as_view(),name= 'register')
]