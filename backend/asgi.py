import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

# Initialize Django ASGI application FIRST to populate the App Registry
django_asgi_app = get_asgi_application()

# Import Channels routing AFTER get_asgi_application() has initialized Django apps
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import job_posting.urls

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter(
            job_posting.urls.websocket_urlpatterns
        )
    ),
})


