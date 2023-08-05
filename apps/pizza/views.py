from django.views.generic import ListView
from apps.pizza.models import Pizza


class PizzaListView(ListView):
    model = Pizza
    template_name = "pizza/pizza.html"
    context_object_name = "items"
    paginate_by = 8
    ordering = ["name"]
