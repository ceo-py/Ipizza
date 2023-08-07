from django.contrib import admin

from apps.checkout.models import PurchaseHistory, CartItem

# Register your models here.
admin.site.register(PurchaseHistory)
admin.site.register(CartItem)