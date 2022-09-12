from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Manager
from django.db.transaction import atomic

from utils.db import BaseModel
from utils.db import SoftDelete

User = get_user_model()


class ApplicantStatus(models.TextChoices):
    SEND = "SEND"
    ACCEPTED = "ACCEPTED"


class Applicant(SoftDelete, BaseModel):
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="applicants"
    )
    title = models.CharField(max_length=255, null=False, unique=False)
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


@atomic
def create_applicant(user_id: User, title: str, description: str, location: str) -> Applicant:
    applicant = Applicant()
    applicant.user_id = user_id
    applicant.title = title
    applicant.description = description
    applicant.location = location
    applicant.save()
    return applicant
