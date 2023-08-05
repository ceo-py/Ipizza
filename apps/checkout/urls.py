from django.urls import path
from .views import checkout, card

urlpatterns = [
    path('', checkout, name='checkout'),
    path('card/', card, name='card'),
]
