from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _

from apps.account.manager import UserManager
from utils.db.base import BaseModel


class UserLevel(models.TextChoices):
    ADMIN = "ADMIN"
    USER = "USER"


class User(BaseModel, AbstractBaseUser):
    email = models.EmailField(_("Email Address"), max_length=255, unique=True, null=True)
    phone_number = models.CharField(max_length=10, unique=True, null=True)
    level = models.CharField(max_length=5, default="USER", choices=UserLevel.choices)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f"{self.id}"
