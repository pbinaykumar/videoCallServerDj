"""
ASGI config for videocallwebrtc project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from .routing import websocket_urlpaterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'videocallwebrtc.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket":  #override AuthMiddlewareStack to use TokenAuthMiddlewareFromCookie
        URLRouter(
            websocket_urlpaterns,
        )
    }
)