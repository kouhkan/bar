"""Custom User Manager."""

from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """Create Users Method"""

    def create_user(self, identity: str, **kwargs):
        if not identity:
            raise ValueError(_("Email or PhoneNumber must be entered"))

        if "@" in identity:
            identity = self.normalize_email(identity)
            user = self.model(email=identity, **kwargs)
        elif identity.isdigit():
            user = self.model(phone_number=identity, **kwargs)
        else:
            raise ValueError(_("Invalid identity"))

        user.save()
        return user

    def create_superuser(self,  password: str, **kwargs):
        user = self.model(**kwargs)
        user.set_password(password)
        user.level = "ADMIN"
        user.save()
        return user
