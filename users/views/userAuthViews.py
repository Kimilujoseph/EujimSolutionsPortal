from django.shortcuts import render
from  rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from ..services.userRegistration import AuthService
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from ..utils import send_confirmation_email,send_verification_email,send_approval_email
from  django.conf import settings
from django.shortcuts import redirect
from ..permissions import admin_required
from rest_framework.permissions import AllowAny
from ..serializers.user_serializer import UserSerializer
import uuid
from rest_framework.exceptions import AuthenticationFailed, ValidationError, APIException
from rest_framework import generics
from ..models import User
from ..serializers.user_serializer import UserSerializer

class RegisterView(APIView):
    @admin_required
    def post(self, request):
        
        service = AuthService()
        message = service.register_user(request.data,request)
        return Response({f"message":"${message}"}, status=status.HTTP_201_CREATED)
        
class RegisterEmployerView(APIView):
    def post(self,request):
        try:
            data  = request.data.copy();
            data["isVerified"] = False
            data["is_pending"] = False
            data["role"] = "employer"
            service = AuthService()
            user = service.register_user(data)
            return Response({"message":"Verification email sent"},status=status.HTTP_201_CREATED)
        except ValueError as e:
           return Response({"error":str(e)},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
           return Response({"message":"internal server errorr"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class VerifyEmail(APIView):

    def get(self, request, verification_code):
        try:
            service = AuthService()
            user = service.verify_email(verification_code)
            if user:
                frontend_login_url =f"{ settings.FRONTEND_URL}/login" 
                return redirect(frontend_login_url)
            else:
                frontend_expired_url = f"{settings.FRONTEND_URL}/token-expired"
                return redirect(frontend_expired_url)
        except Exception as e:
            print(str(e))
            return Response({"message": "Internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#later refactor this  module toabide by the architecture
class ResendVerificationEmail(APIView):
    def post(self, request):
        email = request.data.get('email')
       
        try:
            user = User.objects.get(email=email)
            if not user:
                return Response({"error": "Email not found"}, status=404)
            if user.isVerified:
                return Response({"message": "Email already verified"}, status=400)
            
            user.verificationCode = uuid.uuid4()
            user.save()
            send_verification_email(user, request)
            return Response({"message": "New verification email sent"})
            
        except User.DoesNotExist:
            return Response({"error": "Email not found"}, status=404)
        except Exception as e:
            print(f"Error in ResendVerificationEmail: {str(e)}")
            return Response({"error": "Internal server error"}, status=500)
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
            serializer = UserSerializer(user,many=False)
            response = Response()
            response.set_cookie(
                key='jwt',
                value=token,
                httponly=True,
                secure=not settings.DEBUG,
                samesite='Lax'
            )
            response.data = {
                'message': 'Login successful',
                'user':serializer.data
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