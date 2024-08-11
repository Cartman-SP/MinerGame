from django.urls import path
from .views import *

urlpatterns = [
    path('get_user/', get_or_create_user, name='get_or_create_user'),
    path('start_mining/',start_mining,name="start_minig"),
    path('upgrade/',upgrade,name='upgrade'),
    path('set_max_energy/',set_max_energy,name='set_max_energy'),
    path('lvlup/',lvlup,name='lvlup'),
    path('check_subscribe/',check_subscribe,name='check_subscribe'),
    path('get_friends/',get_friends,name='get_friends'),
    path('claim_reward/',claim_reward,name='claim_reward'),
    path('get_top/',get_top,name='get_top'),
    path('upgrade_mining/',upgrade_mining),
    path('sitevisited/',sitevisited),
    path('get_task/',gettasks),
    path('uptime/',uptime),
    path('turnvibrate/',turnvibrate),
    path('turnsound/',turnsound),
    path('get_invoice_link/',get_innovice_link),
    path('set_video/',set_video)
]
