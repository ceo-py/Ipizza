from django.urls import path
from .views import DesertListView

urlpatterns = [
    path('', DesertListView.as_view(), name='desert'),
]
