from django.urls import path
from .views import *
from .ajax_views import *


urlpatterns = [
    path('increse_prod_quentity', increse_prod_quentity, name='increse_prod_quentity'),
    path('activate_addtess', activate_addtess, name='activate_addtess'),
    path('get_products_query', get_products_query, name='get_products_query'),
    path('add_to_cart', add_to_cart, name='add_to_cart'),
    path('add_to_wishlist', add_to_wishlist, name='add_to_wishlist'),
]