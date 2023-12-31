from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from django.views.generic import CreateView

from apps.accounts.forms import RegisterForm, CustomLoginForm, UserProfileForm
from apps.checkout.models import UserProfile
from apps.menu.views import get_groups_models
from custom_validations.cv import CustomValidation as CV


@method_decorator(
    user_passes_test(CV.is_not_logged_in, login_url=reverse_lazy("index")),
    name="dispatch",
)
class CustomLoginView(LoginView):
    template_name = "accounts/login.html"
    success_url = reverse_lazy("index")
    form_class = CustomLoginForm


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("index")


@method_decorator(
    user_passes_test(CV.is_not_logged_in, login_url=reverse_lazy("index")),
    name="dispatch",
)
class RegisterUserView(CreateView):
    template_name = "accounts/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class ProfileView(LoginRequiredMixin, View):
    template_name = 'accounts/profile.html'
    form_class = UserProfileForm

    def get(self, request, *args, **kwargs):
        group = {}
        try:
            group['group'] = self.request.user.groups.all()[0]
        except IndexError as e:
            print(e)
        user_profile = get_object_or_404(UserProfile, user=request.user)
        context = {
            'form': self.form_class(instance=user_profile),
            'reg_date': user_profile.registration_date,
            'email': user_profile.user,
            'is_active': request.user.is_active,
            'is_staff': request.user.is_staff,
            'is_admin': request.user.is_admin,
            'models': get_groups_models(self.request.user.groups.all()),
        }
        context.update(group)

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        user_profile = get_object_or_404(UserProfile, user=request.user)
        form = self.form_class(request.POST, instance=user_profile)
        if form.is_valid():
            form.save(user=request.user)
            return redirect('profile')
        return render(request, self.template_name, {'form': form})
