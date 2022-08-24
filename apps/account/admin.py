from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm


@admin.action(description="Covert to ADMIN level")
def change_to_admin(modeladmin, request, queryset):
    queryset.update(level="ADMIN")


@admin.action(description="Covert to USER level")
def change_to_user(modeladmin, request, queryset):
    queryset.update(level="USER")


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    model = get_user_model()
    list_display = ("id", "email", "phone_number", "level")
    list_filter = ("created_at", "level")
    list_editable = ("level", )
    list_per_page = 25
    
    fieldsets = (
        (None, {"fields": ("email", "phone_number")}),
        ("Permissions", {"fields": ("level",)}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "phone_number", "password1", "password2"),
        }),
    )
    search_fields = ("email",)
    ordering = ("-created_at",)


admin.site.register(get_user_model(), CustomUserAdmin)
