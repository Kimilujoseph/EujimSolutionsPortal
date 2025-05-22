
from django.shortcuts import render
from  rest_framework.response import Response
from rest_framework.views import APIView
from ..services.userRegistration import AuthService
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from ..utils import send_confirmation_email,send_verification_email
from  django.conf import settings
# Create your views here.

from rest_framework import generics
from ..models import User
from ..serializers.user_serializer import UserSerializer

class RegisterView(APIView):
    def post(self,request):
        service = AuthService()
        user = service.register_user(request.data)
        return Response({"id":user.id,"email":user.email})

class ListUser(generics.ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class DetailUser(generics.RetrieveAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer