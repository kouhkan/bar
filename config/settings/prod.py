from .local import *

DEBUG = False

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "db",
        "PORT": "5432",
    }
}
# CELERY CONFIGURATIONS
CELERY_BROKER_URL = "amqp://rabbitmq"
CELERY_RESULT_BACKEND = "rpc://"

REDIS_HOST = "redis"
REDIS_DB = 0
REDIS_PORT = 6379

CSRF_TRUSTED_ORIGINS = ["http://localhost", "https://localhost"]

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "staticfiles")
)
