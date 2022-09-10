from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()


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
