from django.views.generic import ListView

from apps.pasta.models import Pasta


class PastaListView(ListView):
    model = Pasta
    template_name = "pasta/pasta.html"
    context_object_name = "items"
    ordering = ["name"]
