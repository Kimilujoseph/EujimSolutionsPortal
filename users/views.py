from django.shortcuts import render
from  rest_framework.response import Response
from rest_framework.views import APIView
from .services.userRegistration import AuthService
from rest_framework import status
from rest_framework.decorators import api_view
from .utils import send_confirmation_email,send_verification_email
# Create your views here.

class RegisterView(APIView):
    def post(self,request):
        service = AuthService()
        user = service.register_user(request.data)
        send_verification_email(user,request)
        return Response({"message":"Verification email sent"},status=status.HTTP_201_CREATED)