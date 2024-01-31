from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('products/<str:category>', products_list, name='products_list'),
    path('product/detail/<str:product_slug>', product_detail, name='product_detail'),
]