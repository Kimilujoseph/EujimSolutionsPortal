# middleware/jwt_auth.py
from django.http import JsonResponse
import jwt
from django.conf import settings
from users.models import User

class JWTAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.exempt_paths = [
        '/api/v1/auth/login',
        '/api/v1/auth/logout',
        '/api/v1/auth/register/',
        '/api/v1/auth/verify-email/',
        ]

    def __call__(self, request):
        # Skip auth for exempt paths
        print(request.path)
        if any(request.path.startswith(path) for path in self.exempt_paths):
            return self.get_response(request)

        token = request.COOKIES.get('jwt')
        
        if not token:
            return JsonResponse({'error': 'Unauthorized'}, status=401)

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            print("ERERER",payload)
            # Attach user data directly from JWT payload (no DB query)
            request.user_data = {
                'id': payload['id'],
                'email': payload['email'],
                'role': payload['role'],
                'is_verified': payload.get('is_verified', False)
            }
            
            # Only query DB when absolutely necessary
            if hasattr(self, '_require_db_user'):
                request.user = User.objects.get(id=payload['id'])
            
        except jwt.ExpiredSignatureError:
            return JsonResponse({'error': 'Token expired'}, status=401)
        except jwt.DecodeError:
            return JsonResponse({'error': 'Invalid token'}, status=401)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=401)

        return self.get_response(request)