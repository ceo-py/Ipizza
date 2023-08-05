from django.views.generic import ListView

from apps.salad.models import Salad


class SaladListView(ListView):
    model = Salad
    template_name = "salad/salad.html"
    context_object_name = "items"
    ordering = ["name"]
