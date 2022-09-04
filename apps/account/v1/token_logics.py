from apps.account.utils.redis_auth_handler import (
    check_user_token,
    remove_token_user,
)
from apps.account.v1.tasks import create_user_token


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
