from django.urls import path
from .views import *


urlpatterns = [
    path('login/', user_login, name='login'),
    path('register/', user_register, name='register'),
    path('logout/', user_logout, name='logout'),
    path('about/', about_us, name='about_us'),
]