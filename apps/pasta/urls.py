from django.urls import path
from .views import PastaListView

urlpatterns = [
    path('', PastaListView.as_view(), name='pasta'),
]
