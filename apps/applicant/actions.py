from django.contrib import admin


@admin.action(description="Recover deleted item")
def recovery(self, request, queryset):
    queryset.update(is_deleted=False, deleted_at=None)
