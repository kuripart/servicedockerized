"""
ASGI config for servicedockerized project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
import chat.routing
import game.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'servicedockerized.settings')

# This root routing configuration specifies that when a connection is made to the Channels development server, 
# the ProtocolTypeRouter will first inspect the type of connection. If it is a WebSocket connection (ws:// or wss://), 
# the connection will be given to the AuthMiddlewareStack.
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    # The AuthMiddlewareStack will populate the connection’s scope with a reference to the currently authenticated user, 
    # similar to how Django’s AuthenticationMiddleware populates the request object of a view function with the currently authenticated user
    "websocket": AuthMiddlewareStack(
        URLRouter(
            game.routing.websocket_urlpatterns
        )
    ),
})
