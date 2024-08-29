from django.urls import path
from .views import home, product_detail, product_detail, add_to_cart, cart_detail, remove_from_cart

urlpatterns = [
    path('', home, name='home'),
    path('product/<slug:slug>/', product_detail, name='product_detail'),
    path('cart/', cart_detail, name='cart_detail'),
    path('add-to-cart/<slug:slug>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<slug:slug>/', remove_from_cart, name='remove_from_cart'),
]