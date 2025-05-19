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
       try:
        service = AuthService()
        user = service.register_user(request.data)
        send_verification_email(user,request)
        return Response({"message":"Verification email sent"},status=status.HTTP_201_CREATED)
       except Exception as e:
          return Response({"message":"internal server error"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
       



class VerifyEmail(APIView):
   def get(self,verify_code,request):
      try:
         service = AuthService()
         user = service.verify_email(verify_code)
         if user:
            return Response({"message":"verification successfull"},status=status.HTTP_200_OK)
         else:
            return Response({"message":"verification failed,Token expired"},status=status.HTTP_404_NOT_FOUND)
      except Exception as e:
         return Response({"message":"internal sever error"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
