from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers.password_reset_serializer import PasswordResetRequestSerializer, PasswordResetConfirmSerializer

class PasswordResetRequestView(APIView):
    def post(self, request):
        serializer = PasswordResetRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(request=request)
            return Response({"detail": "Password reset email sent."})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PasswordResetConfirmView(APIView):
    def post(self, request):
        serializer = PasswordResetConfirmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "Password has been reset."})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
