from django.urls import path
from .views import checkout, CartView

urlpatterns = [
    path('', checkout, name='checkout'),
    path('cart/', CartView.as_view(), name='cart'),
]
