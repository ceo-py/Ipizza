from django.views.generic import ListView

from apps.desert.models import Desert


class DesertListView(ListView):
    model = Desert
    template_name = "deserts/desert.html"
    context_object_name = "items"
    ordering = ["name"]
