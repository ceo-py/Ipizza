from django.views.generic import ListView

from apps.drink.models import Drink


class DrinkListView(ListView):
    model = Drink
    template_name = "drink/drink.html"
    context_object_name = "items"
