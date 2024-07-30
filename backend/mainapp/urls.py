from django.urls import path
from .views import *

urlpatterns = [
    path('get_user/', get_or_create_user, name='get_or_create_user'),
    path('start_mining/',start_mining,name="start_minig"),
    path('upgrade/',upgrade,name='upgrade'),
    path('set_max_energy/',set_max_energy,name='set_max_energy'),
]
