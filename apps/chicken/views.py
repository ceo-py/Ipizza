from django.views.generic import ListView

from apps.chicken.models import Chicken


class ChickenListView(ListView):
    model = Chicken
    template_name = "chicken/chicken.html"
    context_object_name = "chickens"
    ordering = ["name"]
