from django.contrib.auth import forms, login
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class RegisterUserForm(forms.UserCreationForm):
    pass


class RegisterUserView(CreateView):
    template_name = ''
    form_class = forms.UserCreationForm
    success_url = reverse_lazy('register_user')

    def from_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)

        return result
