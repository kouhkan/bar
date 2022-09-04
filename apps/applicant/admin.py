from typing import Dict, Sequence

from django.contrib import admin

from .models import Applicant


class ApplicantAdmin(admin.ModelAdmin):
    list_display: Sequence[str] = ("id", "user_id", "title", "status")
    list_filter: Sequence[str] = ("status",)
    list_editable: Sequence[str] = ("status",)
    list_per_page: int = 25
    search_fields: Sequence[str] = (
        "title",
        "description",
        "user_id",
        "location",
    )
    prepopulated_fields: Dict[str, Sequence[str]] = {"slug": ("title",)}


admin.site.register(Applicant, ApplicantAdmin)
