from django.views.generic import ListView

from apps.sandwich.models import Sandwich


class SandwichListView(ListView):
    model = Sandwich
    template_name = "sandwich/sandwich.html"
    context_object_name = "items"
    ordering = ["name"]
