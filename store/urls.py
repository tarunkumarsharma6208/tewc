from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('products/<str:category>', products_list, name='products_list'),
    path('product/detail/<str:product_slug>', product_detail, name='product_detail'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_view, name='cart_view'),
    path('checkout/', checkout, name='checkout'),
    path('wishlist/', wishlist_view, name='wishlist_view'),
    path('add-to-wishlist/<int:product_id>/', add_to_wishlist, name='add_to_wishlist'),
    path('store/admin/', store_admin, name='store_admin'),
]