from django.urls import re_path
from backend.consumers import *

websocket_urlpatterns = [
    re_path(r'ws/change_balance/(?P<user_id>\d+)/$', BalanceConsumer.as_asgi()),
]