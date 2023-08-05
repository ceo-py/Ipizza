from django.urls import path
from .views import DrinkListView

urlpatterns = [
    path('', DrinkListView.as_view(), name='drink'),
]
