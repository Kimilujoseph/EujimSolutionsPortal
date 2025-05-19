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

class RegisterView(APIView):
    def post(self,request):
       try:
         if not request.user_data or request.user_data.get('role') not in  ['superAdmin','admin']:
            return Response({'error': 'Admin priveledges required'}, status=status.HTTP_403_FORBIDDEN)
         service = AuthService()
         user = service.register_user(request.data)
         send_verification_email(user,request)
         return Response({"message":"Verification email sent"},status=status.HTTP_201_CREATED)
       except ValueError as e:
          return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)




class VerifyEmail(APIView):
   def get(self,request,verification_code):
      try:
         service = AuthService()
         user = service.verify_email(verification_code)
         if user:
            return Response({"message":"verification successfull"},status=status.HTTP_200_OK)
         else:
            return Response({"message":"verification failed,Token expired"},status=status.HTTP_404_NOT_FOUND)
      except Exception as e:
         print(str(e))
         return Response({"message":"internal sever error"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        
        if not email or not password:
            return Response(
                {'error': 'Email and password required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            service = AuthService()
            user, token = service.login_user(email, password)
            
            response = Response()
            response.set_cookie(
                key='jwt',
                value=token,
                httponly=True,
                secure=not settings.DEBUG,  # Secure in production
                samesite='Lax'
            )
            response.data = {
                'message': 'Login successful',
                'user': {
                    'id': user.id,
                    'email': user.email,
                    'role': user.role
                }
            }
            return response
            
        except AuthenticationFailed as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_401_UNAUTHORIZED
            )
        

class LogoutView(APIView):
    def post(self, request):
        response = Response({'message': 'Logged out successfully'})
        response.delete_cookie('jwt')
        return response