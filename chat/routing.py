from django.urls import re_path

# from . import consumers
from . import consumers3
websocket_urlpatterns = [
    # re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatRoomConsumer),
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers3.ChatRoomConsumer.as_asgi()),
]
