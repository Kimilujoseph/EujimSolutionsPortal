
from django.shortcuts import render
from  rest_framework.response import Response
from rest_framework.views import APIView
from .services.userRegistration import AuthService
# Create your views here.

from rest_framework import generics
from .models import User
from .serializers.user_serializer import UserSerializer

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