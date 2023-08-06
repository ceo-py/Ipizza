from django.urls import path

from apps.accounts.views import RegisterUserView

urlpatterns = [
    path('', RegisterUserView.as_view(), name='register_user'),

]
