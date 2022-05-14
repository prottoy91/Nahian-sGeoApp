
#!/usr/bin/env python3

from channels.routing import ProtocolTypeRouter
from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    #re_path(r'd5f9-113-11-39-222.in.ngrok.io/ws/socket-server/',consumers.PracticeConsumer.as_asgi()),
    re_path(r'ws/socket-server/',consumers.PracticeConsumer.as_asgi()),
    #re_path(r'ws/socket-server/',consumers.PracticeConsumer.as_pyproj()),
]

#r'ws/socket-server/',
