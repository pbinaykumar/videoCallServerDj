from django.urls import path
from . import consumer

websocket_urlpaterns = [
    path('ws/', consumer.CallConnection.as_asgi()),
]