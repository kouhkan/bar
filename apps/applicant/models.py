from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Manager

from utils.db.base import BaseModel
from utils.db.soft_delete import SoftDelete

User = get_user_model()


class ApplicantStatus(models.TextChoices):
    SEND = "SEND"
    ACCEPTED = "ACCEPTED"


class Applicant(BaseModel, SoftDelete):
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="applicants"
    )
    title = models.CharField(max_length=255, null=False, unique=False)
    slug = models.SlugField(max_length=255, null=False, unique=True)
    description = models.TextField()
    location = models.TextField()
    status = models.CharField(
        max_length=10,
        null=False,
        choices=ApplicantStatus.choices,
        default="SEND",
    )

    class Meta:
        default_manager_name = "objects"

    def __str__(self) -> str:
        return f"{self.id}"


class DeletedApplicant(Applicant):
    deleted = Manager()

    class Meta:
        proxy = True
