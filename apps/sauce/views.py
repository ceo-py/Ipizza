from django.views.generic import ListView

from apps.sauce.models import SauceMenu


class SauceListView(ListView):
    model = SauceMenu
    template_name = "sauce/sauce.html"
    context_object_name = "items"
    ordering = ["name"]
