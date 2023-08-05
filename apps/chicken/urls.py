from django.urls import path
from .views import ChickenListView

urlpatterns = [
    path('', ChickenListView.as_view(), name='chicken'),
]
