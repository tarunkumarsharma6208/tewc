from django.urls import path
from .views import *
from .ajax_views import *


urlpatterns = [
    path('increse_prod_quentity', increse_prod_quentity, name='increse_prod_quentity'),
    path('activate_addtess', activate_addtess, name='activate_addtess'),
]