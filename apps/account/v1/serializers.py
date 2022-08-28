from django.contrib.auth import get_user_model
from rest_framework import serializers, status
from rest_framework.exceptions import ValidationError

from apps.account.utils.redis_auth_handler import (
    get_user_wait_time_token,
    set_user_token,
    remove_token_user,
    check_user_token

)


class RegisterSerializer(serializers.Serializer):
    phoneNumber = serializers.CharField(min_length=10, max_length=10, default="")
    email = serializers.EmailField(max_length=100, default="")

    def validate(self, attrs):
        if attrs.get("phoneNumber") is None and attrs.get("email") is None:
            raise ValidationError(
                detail="phone number or email must be entered.",
                code=status.HTTP_400_BAD_REQUEST
            )
        return attrs

    def create(self, validated_data):
        identity = validated_data.get("phoneNumber", None) \
            if validated_data.get("phoneNumber", None) else \
            validated_data.get("email")

        if wait_time := get_user_wait_time_token(identity):
            raise ValidationError(
                detail=f"{wait_time} second(s) left to got new token.",
                code=status.HTTP_429_TOO_MANY_REQUESTS,
            )

        return set_user_token(identity=identity)

    def update(self, instance, validated_data):
        pass


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(min_length=6, max_length=6)
    phoneNumber = serializers.CharField(min_length=10, max_length=10, default="")
    email = serializers.EmailField(max_length=100, default="")

    def validate(self, attrs):
        if attrs.get("phoneNumber") is None and attrs.get("email") is None:
            raise ValidationError(
                detail="phone number or email must be entered.",
                code=status.HTTP_400_BAD_REQUEST
            )
        return attrs

    def create(self, validated_data):
        identity = validated_data.get("phoneNumber", None) \
            if validated_data.get("phoneNumber", None) else \
            validated_data.get("email")

        if not check_user_token(identity, validated_data.get("token")):
            return False
        remove_token_user(identity)

        return True


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("phone_number", "email", "id", "level")
