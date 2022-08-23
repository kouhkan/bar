from django.contrib import admin
from django.contrib.auth import get_user_model


@admin.action(description="Covert to ADMIN level")
def change_to_admin(modeladmin, request, queryset):
    queryset.update(level="ADMIN")

class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "phone_number", "level")
    list_per_page = 25
    list_editable = ("level",)
    list_filter = ("level", "created_at")
    actions = (change_to_admin, )


admin.site.register(get_user_model(), UserAdmin)
