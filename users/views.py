from django.shortcuts import render
from  rest_framework.response import Response
from rest_framework.views import APIView
from .services.userRegistration import AuthService
# Create your views here.

class RegisterView(APIView):
    def post(self,request):
        service = AuthService()
        user = service.register_user(request.data)
        return Response({"id":user.id,"email":user.email})