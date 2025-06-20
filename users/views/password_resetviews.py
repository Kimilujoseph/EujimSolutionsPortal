from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers.password_reset_serializer import PasswordResetRequestSerializer, PasswordResetConfirmSerializer
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
class PasswordResetRequestView(APIView):
    def post(self, request):
        serializer = PasswordResetRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(request=request)
            return Response({"detail": "Password reset email sent."})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PasswordResetConfirmView(APIView):
    def post(self, request, uidb64 , token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
        except (TypeError, ValueError, OverflowError):
            return Response({"error": "Invalid UID"}, status=400)

        data = {
            "uid": uid,
            "token": token,
            "new_password": request.data.get("new_password")
        }
        serializer = PasswordResetConfirmSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "Password has been reset."})
        print("Serializer errors:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
