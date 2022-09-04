from django.contrib.auth import get_user_model
from rest_framework import serializers, status
from rest_framework.exceptions import ValidationError

from .token_logics import create_token_for_user, verify_user_token


class RegisterSerializer(serializers.Serializer):
    phoneNumber = serializers.CharField(
        min_length=10, max_length=10, default=""
    )
    email = serializers.EmailField(max_length=100, default="")

    def validate(self, attrs):
        if attrs.get("phoneNumber") is None and attrs.get("email") is None:
            raise ValidationError(
                detail="phone number or email must be entered.",
                code=status.HTTP_400_BAD_REQUEST,
            )
        return attrs

    def create(self, validated_data):
        return create_token_for_user(validated_data)


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(min_length=6, max_length=6)
    phoneNumber = serializers.CharField(
        min_length=10, max_length=10, default=""
    )
    email = serializers.EmailField(max_length=100, default="")

    def validate(self, attrs):
        if attrs.get("phoneNumber") is None and attrs.get("email") is None:
            raise ValidationError(
                detail="phone number or email must be entered.",
                code=status.HTTP_400_BAD_REQUEST,
            )
        return attrs

    def create(self, validated_data):
        return verify_user_token(validated_data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("phone_number", "email", "id", "level")
