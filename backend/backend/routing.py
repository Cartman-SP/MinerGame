from django.urls import re_path
from .consumers import TapConsumer, MiningConsumer, EnergyConsumer

websocket_urlpatterns = [
    re_path(r'ws/some_path/(?P<user_id>\w+)/$', TapConsumer.as_asgi()),
    re_path(r'ws/mining/(?P<user_id>\w+)/$', MiningConsumer.as_asgi()),
    re_path(r'ws/energy/(?P<user_id>\w+)/$', EnergyConsumer.as_asgi()),
]
