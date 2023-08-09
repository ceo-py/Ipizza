from django.db.models import Sum
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from apps.appetizer.models import Appetizer
from apps.checkout.models import CartItem
from apps.chicken.models import Chicken
from apps.desert.models import Desert
from apps.drink.models import Drink
from apps.ingredient.models import Spice, Meat, Vegetable, Cheese, Sauce
from apps.pasta.models import Pasta
from apps.pizza.models import Pizza
from apps.salad.models import Salad
from apps.sandwich.models import Sandwich
from apps.sauce.models import SauceMenu

all_menu_models = {
    "appetizer": Appetizer,
    "pizza": Pizza,
    "chicken": Chicken,
    "pasta": Pasta,
    "sandwich": Sandwich,
    "salad": Salad,
    "sauce": SauceMenu,
    "desert": Desert,
    "drink": Drink,
}


class ItemListView(ListView):
    model = None
    context_object_name = "items"
    ordering = ["name"]

    def get_template_names(self):
        model_name = self.kwargs["model"]
        return [f"{model_name}/{model_name}.html"]

    def get_queryset(self):
        self.model = all_menu_models.get(self.kwargs["model"])
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model_name"] = self.kwargs["model"]

        if self.request.user.is_authenticated:
            cart_items_sum = CartItem.objects.filter(user=self.request.user).aggregate(Sum('quantity'))['quantity__sum']
            context["cart_items"] = cart_items_sum if cart_items_sum else 0

        return context


class ItemDetailView(DetailView):
    model = None
    context_object_name = "item"
    template_name = "menu/details.html"

    def get_object(self, queryset=None):
        model_name = self.kwargs["model"]
        self.model = all_menu_models.get(model_name)
        pk = self.kwargs["pk"]
        return get_object_or_404(self.model, pk=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            cart_items_sum = CartItem.objects.filter(user=self.request.user).aggregate(Sum('quantity'))['quantity__sum']
            context["cart_items"] = cart_items_sum if cart_items_sum else 0
            context["spices"] = Spice.objects.all()
            context["meats"] = Meat.objects.all()
            context["vegetables"] = Vegetable.objects.all()
            context["cheese"] = Cheese.objects.all()
            context["sauce"] = Sauce.objects.all()

        return context
