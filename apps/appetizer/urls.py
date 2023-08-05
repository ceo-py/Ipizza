from django.urls import path
from .views import AppetizerListView

urlpatterns = [
    path('', AppetizerListView.as_view(), name='appetizer'),
]
