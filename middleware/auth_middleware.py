from django.http import JsonResponse
import jwt
from django.conf import settings
from users.models import User
from datetime import datetime, timezone

class JWTAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.exempt_paths = [
            '/api/v1/auth/login',
            '/api/v1/auth/logout',
            '/api/v1/auth/password-reset-confirm/',
            '/api/v1/auth/request-verification-code/',
            '/api/v1/auth/register/',
            '/api/v1/auth/request-reset-password/',
            '/api/v1/auth/verify-email/',
            '/api/v1/'
            '/api/v1/auth/request-reset-password/',
            '/favicon.ico'
            
        ]

    def __call__(self, request):
        # Skip auth for exempt paths
        print(request.path)
        if any(request.path.startswith(path) for path in self.exempt_paths):
            return self.get_response(request)

        token = request.COOKIES.get('jwt')
        
        if not token:
            return JsonResponse({'error': 'Unauthorized - No token provided'}, status=401)

        try:
            # Decode the JWT token
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            
            # Verify token expiration
            if datetime.now(timezone.utc).timestamp() > payload['exp']:
                return JsonResponse({'error': 'Token expired'}, status=401)
            
            # Attach comprehensive user data from JWT payload
            request.user_data = {
                'id': payload['id'],
                'email': payload['email'],
                'firstName': payload.get('firstName'),
                'secondName': payload.get('secondName'),
                'role': payload['role'],
                'isVerified': payload.get('isVerified', False),
                'is_active': payload.get('is_active', True),
                'is_deleted': payload.get('is_deleted', False),
                'is_pending': payload.get('is_pending', False),
                'is_suspended': payload.get('is_suspended', False),
                # Include token metadata for additional checks if needed
                'token_issued_at': payload['iat'],
                'token_expires_at': payload['exp']
            }
            
            # Only query DB when absolutely necessary (e.g., for fresh user data)
            if hasattr(self, '_require_db_user'):
                request.user = User.objects.get(id=payload['id'])
            
        except jwt.ExpiredSignatureError:
            return JsonResponse({'error': 'Token expired'}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({'error': 'Invalid token'}, status=401)
        except KeyError as e:
            return JsonResponse({'error': f'Malformed token - missing {str(e)}'}, status=401)
        except Exception as e:
            return JsonResponse({'error': 'Authentication failed'}, status=401)

        return self.get_response(request)