from django.urls import path
from .views import SandwichListView

urlpatterns = [
    path('', SandwichListView.as_view(), name='sandwich'),
]
