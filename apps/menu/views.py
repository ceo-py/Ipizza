from django.contrib.auth.decorators import user_passes_test
from django.db.models import Sum
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
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
from custom_validations.cv import CustomValidation as CV
from django import forms

all_menu_models = {
    "appetizer": Appetizer,
    "pizza": Pizza,
    "chicken": Chicken,
    "pasta": Pasta,
    "sandwich": Sandwich,
    "salad": Salad,
    "sauce": SauceMenu,
    "saucemenu": SauceMenu,
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

            group_info = []
            selected_groups = self.request.user.groups.all()

            for group in selected_groups:
                models_in_group = set(group.permissions.all().values_list('content_type__model', flat=True))
                group_info.append({
                    'name': group.name,
                    'models': models_in_group,
                })
                context["models"] = models_in_group

            cart_items_sum = CartItem.objects.filter(user=self.request.user).aggregate(Sum('quantity'))['quantity__sum']
            context["cart_items"] = cart_items_sum if cart_items_sum else 0

        return context


@method_decorator(
    user_passes_test(CV.logged_in, login_url=reverse_lazy("index")),
    name="dispatch",
)
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

            group_info = []
            selected_groups = self.request.user.groups.all()

            for group in selected_groups:
                models_in_group = set(group.permissions.all().values_list('content_type__model', flat=True))
                group_info.append({
                    'name': group.name,
                    'models': models_in_group,
                })
                context["models"] = models_in_group

            cart_items_sum = CartItem.objects.filter(user=self.request.user).aggregate(Sum('quantity'))['quantity__sum']
            context["cart_items"] = cart_items_sum if cart_items_sum else 0
            context["spices"] = Spice.objects.all()
            context["meats"] = Meat.objects.all()
            context["vegetables"] = Vegetable.objects.all()
            context["cheese"] = Cheese.objects.all()
            context["sauce"] = Sauce.objects.all()

        return context


class MenuCategoryView(ListView):
    model = None
    context_object_name = "items"
    template_name = 'menu/menu.html'

    def get_queryset(self):
        self.model = all_menu_models.get(self.kwargs["model"])
        return self.model.objects.all().order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model_name"] = self.kwargs["model"]

        if self.request.user.is_authenticated:
            cart_items_sum = CartItem.objects.filter(user=self.request.user).aggregate(Sum('quantity'))['quantity__sum']
            context["cart_items"] = cart_items_sum if cart_items_sum else 0

        return context


class DeleteItemView(View):
    def get(self, request, model, pk):
        model_obj = all_menu_models.get(model)
        item = get_object_or_404(model_obj, id=pk)
        item.delete()

        menu_url = reverse('items-menu', kwargs={'model': model})
        return redirect(menu_url)


class EditItemView(DetailView):
    template_name = 'menu/edit_item.html'
    model = None

    def get_form_class(self):
        class EditItemForm(forms.ModelForm):
            class Meta:
                model = self.model
                fields = '__all__'

        return EditItemForm

    def get_object(self):
        model_name = self.kwargs.get("model")
        self.model = all_menu_models.get(model_name)
        pk = self.kwargs.get("pk")
        return get_object_or_404(self.model, pk=pk)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = form_class(instance=self.object)
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = form_class(request.POST, instance=self.object)
        if form.is_valid():
            form.save()
            return redirect('items-menu', model=self.model.__name__.lower())
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)


class CreateItemView(View):
    template_name = 'menu/create_item.html'

    def get_form_class(self):
        model_name = self.kwargs.get("model")
        model_class = all_menu_models.get(model_name)

        class CreateItemForm(forms.ModelForm):
            class Meta:
                model = model_class
                fields = '__all__'

        return CreateItemForm

    def get(self, request, model):
        form_class = self.get_form_class()
        form = form_class()
        context = {
            'form': form,
            'model_name': model,
        }
        return render(request, self.template_name, context)

    def post(self, request, model):
        form_class = self.get_form_class()
        form = form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('items-menu', model=model)
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)
