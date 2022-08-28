from datetime import timedelta
from random import randint

import redis as rd
from django.conf import settings


redis = rd.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=settings.REDIS_DB
)


def generate_prefix(identity: str):
    return f"identity:{identity}"


def generate_token():
    return randint(100000, 999999)


def set_user_token(identity: str):
    if settings.DEBUG:
        token = "000000"
    else:
        token = generate_token()
    redis.set(generate_prefix(identity), token, ex=timedelta(seconds=120))
    return token


def get_user_wait_time_token(identity: str):
    if redis.exists(generate_prefix(identity)):
        return redis.ttl(generate_prefix(identity))
    return 0


def check_user_token(identity: str, token: str) -> bool:
    if result := redis.get(generate_prefix(identity)):
        return result.decode("UTF-8") == token

    return False


def remove_token_user(identity: str):
    redis.delete(generate_prefix(identity))
    return True
