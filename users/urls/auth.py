from django.urls import path

from ..views.userAuthViews import RegisterView

urlpatterns = [
    path('register/',RegisterView.as_view(),name= 'register')
]