from django.urls import path, include
from .views import *


urlpatterns = [
    path('ajax/', include('store.ajax_urls')),
    path('', index, name='home'),
    path('products/<str:category>', products_list, name='products_list'),
    path('product/detail/<str:product_slug>', product_detail, name='product_detail'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    
    path('remove-from-cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('cart/', cart_view, name='cart_view'),
    path('checkout/', checkout, name='checkout'),
    path('wishlist/', wishlist_view, name='wishlist_view'),
    path('add-to-wishlist/<int:product_id>/', add_to_wishlist, name='add_to_wishlist'),
    path('order/track/', order_tracking, name='order_tracking'),
    path('search/products/', search_products, name='search_products'),
    path('save_user_address', save_user_address, name='save_user_address'),

    #admin urls
    path('store/admin/', store_admin, name='store_admin'),
]