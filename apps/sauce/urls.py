from django.urls import path

from apps.sauce.views import SauceListView



urlpatterns = [
    path('', SauceListView.as_view(), name='sauce'),
]
