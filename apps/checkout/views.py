from django.shortcuts import render
from django.views import View

from apps.checkout.models import CartItem
from apps.menu.views import get_groups_models


# Create your views here.


def checkout(request):
    return render(request, "checkout/checkout.html")


class CartView(View):
    template_name = "checkout/cart.html"

    def get(self, request):
        user = request.user
        context = {
            "items": CartItem.objects.filter(user=user),
            "cart_items": sum(
                x.quantity for x in CartItem.objects.filter(user=self.request.user)
            ),
            "models": get_groups_models(self.request.user.groups.all()),
        }

        return render(request, self.template_name, context)
