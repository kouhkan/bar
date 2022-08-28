from celery import shared_task
from rest_framework import status
from rest_framework.exceptions import ValidationError

from apps.account.utils.redis_auth_handler import (
    get_user_wait_time_token,
    set_user_token
)


@shared_task
def create_user_token(identity: str):
    if wait_time := get_user_wait_time_token(identity):
        raise ValidationError(
            detail=f"{wait_time} second(s) left to got new token.",
            code=status.HTTP_429_TOO_MANY_REQUESTS,
        )
    token = set_user_token(identity=identity)
    print(token)
    return token
