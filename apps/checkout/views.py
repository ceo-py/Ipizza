from django.shortcuts import render
from django.views import View

from apps.checkout.models import CartItem


# Create your views here.

def checkout(request):
    return render(request, 'checkout/checkout.html')


class CartView(View):
    template_name = 'checkout/cart.html'

    def get(self, request):
        user = request.user
        context = {
            'items': CartItem.objects.filter(user=user),
            'cart_items': sum(x.quantity for x in CartItem.objects.filter(user=self.request.user)),
        }

        return render(request, self.template_name, context)
