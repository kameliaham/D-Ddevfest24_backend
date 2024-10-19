from django.urls import re_path
from . import consumers


# Define WebSocket URL patterns for routing WebSocket connections.
websocket_urlpatterns = [
    re_path(r'ws/machine-data/$', consumers.MachineDataConsumer.as_asgi()),
]
