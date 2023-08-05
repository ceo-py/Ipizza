from django.urls import path
from .views import PizzaListView

urlpatterns = [
    path('', PizzaListView.as_view(), name='pizza'),
]
