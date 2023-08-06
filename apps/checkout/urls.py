from django.urls import path
from .views import checkout, cart

urlpatterns = [
    path('', checkout, name='checkout'),
    path('cart/', cart, name='cart'),
]
