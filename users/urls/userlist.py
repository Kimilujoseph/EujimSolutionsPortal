
from django.urls import path
from ..views.userAuthViews import ListUser,DetailUser

urlpatterns=[
    path('',ListUser.as_view()),
    path('<int:pk>/',DetailUser.as_view(),name='detail')
]