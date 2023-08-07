from django.urls import path

from api.views import api_add_cart, api_delete_cart

urlpatterns = [
                  # path('api/', get_data_test.as_view(), name='add_to_cart_api'),
                  # path('get/', api_get_cart, name='get_cart_api'),
                  path('add/', api_add_cart, name='add_to_cart_api'),
                  path('delete/', api_delete_cart, name='api_delete_cart'),
              ]
