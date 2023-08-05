from django.urls import path
from .views import SaladListView

urlpatterns = [
    path('', SaladListView.as_view(), name='salad'),
]
