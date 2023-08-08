from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView

from apps.accounts.forms import RegisterForm, CustomLoginForm
from custom_validations.cv import CustomValidation as CV


@method_decorator(user_passes_test(CV.is_not_logged_in, login_url=reverse_lazy('index')), name='dispatch')
class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('index')
    form_class = CustomLoginForm


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('index')


class RegisterUserView(CreateView):
    template_name = 'accounts/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

