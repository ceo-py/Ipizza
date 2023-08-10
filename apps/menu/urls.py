from django.urls import path

from apps.menu.views import ItemListView, ItemDetailView, MenuCategoryView, DeleteItemView, EditItemView, CreateItemView

urlpatterns = [
    path('details/<str:model>/<int:pk>/', ItemDetailView.as_view(), name='details'),
    path('<str:model>/', ItemListView.as_view(), name='item-list'),
    path('menu/<str:model>/', MenuCategoryView.as_view(), name='items-menu'),
    path('menu/<str:model>/<int:pk>/delete/', DeleteItemView.as_view(), name='item-delete'),
    path('edit/<str:model>/<int:pk>/', EditItemView.as_view(), name='item-edit'),
    path('edit/<str:model>/', CreateItemView.as_view(), name='item-create'),

]
