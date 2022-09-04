from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class ApplicaStatus(models.TextChoices):
    SEND = "SEND"
    ACCEPTED = "ACCEPTED"


class Applicant(models.Model):
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
        choices=ApplicaStatus.choices,
        default="SEND",
    )

    def __str__(self) -> str:
        return f"{self.id}"
