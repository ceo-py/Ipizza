from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField, AuthenticationForm

from apps.checkout.models import UserProfile

User = get_user_model()


class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_attributes()

    def __set_attributes(self):
        self.fields["username"].widget.attrs["placeholder"] = "Email"
        self.fields["username"].widget.attrs["class"] = "form-control m-b-25"
        self.fields["password"].widget.attrs["placeholder"] = "Парола"
        self.fields["password"].widget.attrs["class"] = "form-control m-b-25"


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    # field_attrs = {
    #     "email": {
    #         "placeholder": "Email",
    #         "class": "form-control m-b-25",
    #     },
    #     "password": {
    #         "placeholder": "Парола",
    #         "class": "form-control m-b-25",
    #     },
    #     "password_2": {
    #         "placeholder": "Потвърди паролата",
    #         "class": "form-control m-b-25",
    #     },
    # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_attributes()

    def __set_attributes(self):

        self.fields["email"].widget.attrs["placeholder"] = "Email"
        self.fields["email"].widget.attrs["class"] = "form-control m-b-25"
        self.fields["password"].widget.attrs["placeholder"] = "Парола"
        self.fields["password"].widget.attrs["class"] = "form-control m-b-25"
        self.fields["password_2"].widget.attrs["placeholder"] = "Потвърди паролата"
        self.fields["password_2"].widget.attrs["class"] = "form-control m-b-25"

    class Meta:
        model = User
        fields = ["email", "password", "password_2"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("This email is taken")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")
        errors = {}

        try:
            if len(password) < 8:
                errors["password"] = "Password must be at least 8 characters long"

            if not any(char.isupper() for char in password):
                errors["password"] = "Password must contain at least one uppercase letter"

            if not any(char.islower() for char in password):
                errors["password"] = "Password must contain at least one lowercase letter"

            if not any(char.isdigit() for char in password):
                errors["password"] = "Password must contain at least one digit"

            if password != password_2:
                errors["password_2"] = "Passwords do not match"
        except:
            errors['password'] = 'Password must be at least 8 characters long\n' \
                                 ',must contain at least one uppercase letter\n' \
                                 ',must contain at least one lowercase letter\n' \
                                 ',must contain at least one digit'

        if errors:
            raise forms.ValidationError(errors)

        return cleaned_data

    def save(self, commit=True):
        form = super().save(commit=False)
        form.set_password(self.cleaned_data["password"])

        if commit:
            form.save()
            UserProfile.objects.create(user=form)

        return form


class UserAdminCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["email"]

    def clean(self):

        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")
        if password is not None and password != password_2:
            self.add_error("password_2", "Your passwords must match")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ["email", "password", "is_active", "admin"]

    def clean_password(self):
        return self.initial["password"]


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'telephone_number', 'address']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_class()

    def __set_class(self):
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control m-b-25',
                'placeholder': field.label
            })

    def save(self, user=None, commit=True):
        instance = super().save(commit=False)
        instance.user = user
        if commit:
            instance.save()
        return instance