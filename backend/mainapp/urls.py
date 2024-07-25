from django.urls import path
from .views import *

urlpatterns = [
    path('get_user/', get_or_create_user, name='get_or_create_user'),
    path('upgrade/',upgrade_room,name="upgrade_room"),
    path('lvl_up/',lvl_up,name="lvl_up"),
    path('upgrade_coin/',upgrade_coin,name="upgrade_coin")
]
