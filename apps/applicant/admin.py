from typing import Dict, Sequence

from django.contrib import admin

from apps.applicant.models import DeletedApplicant
from apps.applicant.models import Applicant
from apps.applicant.actions import recovery


@admin.register(Applicant)
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


@admin.register(DeletedApplicant)
class DeletedApplicantAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return DeletedApplicant.deleted.filter(is_deleted=True)

    actions = (recovery,)
    list_display: Sequence[str] = ("id", "user_id", "title", "deleted_at", "status")
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
