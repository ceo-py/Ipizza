from django.views.generic import ListView

from apps.appetizer.models import Appetizer


class AppetizerListView(ListView):
    model = Appetizer
    template_name = "appetizer/appetizer.html"
    context_object_name = "items"
    ordering = ["name"]
