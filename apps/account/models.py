from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

from apps.account.manager import UserManager
from apps.account.utils.redis_auth_handler import check_user_token
from apps.account.utils.redis_auth_handler import remove_token_user
from apps.account.v1.tasks import create_user_token
from utils.db.base import BaseModel


class UserLevel(models.TextChoices):
    ADMIN = "ADMIN"
    USER = "USER"


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("Email Address"), max_length=255, unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=10, unique=True, null=True, blank=True)
    level = models.CharField(max_length=5, default="USER", choices=UserLevel.choices)
    password = models.CharField(_('password'), max_length=128, blank=True, null=True)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f"{self.id}"

    @property
    def is_staff(self):
        return self.level == UserLevel.ADMIN.name

    @property
    def is_superuser(self):
        return self.level == UserLevel.ADMIN.name

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_staff

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


def create_token_for_user(validated_data):
    identity = (
        validated_data.get("phoneNumber", None)
        if validated_data.get("phoneNumber", None)
        else validated_data.get("email")
    )

    return create_user_token(identity)


def verify_user_token(validated_data) -> bool:
    identity = (
        validated_data.get("phoneNumber", None)
        if validated_data.get("phoneNumber", None)
        else validated_data.get("email")
    )

    if not check_user_token(identity, validated_data.get("token")):
        return False
    remove_token_user(identity)

    return True


def create_user(serializer) -> User:
    user = User.objects.filter(
        Q(phone_number=serializer.data.get("phoneNumber", None))
        | Q(email=serializer.data.get("email", None))
    ).first()

    if not user:
        user = User.objects.create(
            phone_number=serializer.data.get("phoneNumber"),
            email=serializer.data.get("email")
        )

    return user
