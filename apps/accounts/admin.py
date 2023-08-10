from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminCreationForm, UserAdminChangeForm
from ..checkout.models import UserProfile

User = get_user_model()

# admin.site.unregister(Group)


class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ["email", "admin"]
    list_filter = ["admin"]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Group", {"fields": ('groups', )}),
        ("Permissions", {"fields": ("is_active", "staff", "admin")}),
    )

    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "password1", "password2")}),
    )
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.register(UserProfile)
