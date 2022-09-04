from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()


def create_user(serializer) -> User:
    user = User.objects.filter(
        Q(phone_number=serializer.data.get("phoneNumber", None))
        | Q(email=serializer.data.get("email", None))
    ).first()

    if not user:
        user = User
        if phone_number := serializer.data.get("phoneNumber", None):
            user.phone_number = phone_number
        if email := serializer.data.get("email", None):
            user.email = email
        user.save()

    return user
