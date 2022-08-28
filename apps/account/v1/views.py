import json

from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.account.v1.serializers import (
    RegisterSerializer,
    TokenSerializer,
    UserSerializer
)


class RegisterUserView(APIView):
    serializer = RegisterSerializer

    def post(self, request):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            token = serializer.create(validated_data=serializer.data)
            print("token -> ", token)
            return Response({}, status=status.HTTP_200_OK)


class TokenSerializerView(APIView):
    serializer = TokenSerializer
    model = get_user_model()

    def put(self, request):
        serializer = self.serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            print(serializer.data)
            if result := serializer.create(validated_data=serializer.data):
                if result:

                    user = get_user_model().objects.filter(
                        Q(phone_number=serializer.data.get("phoneNumber", None)) |
                        Q(email=serializer.data.get("email", None))
                    ).first()

                    if not user:
                        user = self.model()
                        if phone_number := serializer.data.get("phoneNumber", None):
                            user.phone_number = phone_number
                        if email := serializer.data.get("email", None):
                            user.email = email
                        user.save()
                        return Response({"phoneNumber": user.phone_number, "email": user.email, "level": user.level}, status=status.HTTP_201_CREATED)
                    return Response({"phoneNumber": user.phone_number, "email": user.email, "level": user.level}, status=status.HTTP_200_OK)
                return Response({"msg": "Code was wrong"}, status=status.HTTP_400_BAD_REQUEST)
            return Response({"msg": "Token does not exist."}, status=status.HTTP_400_BAD_REQUEST)


class ListUsers(APIView):
    serializer = UserSerializer
    model = get_user_model()

    def get(self, request):
        users = self.model.objects.filter(level="USER")
        return Response(self.serializer(users, many=True).data)
