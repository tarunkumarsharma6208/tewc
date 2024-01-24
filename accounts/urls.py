from django.urls import path
from .views import *


urlpatterns = [
    path('', user_login, name='login'),
]