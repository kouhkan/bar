from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from apps.account.models import create_user
from apps.account.v1.serializers import RegisterSerializer
from apps.account.v1.serializers import TokenSerializer
from apps.account.v1.serializers import UserSerializer


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
            if result := serializer.create(validated_data=serializer.data):
                if result:
                    user = create_user(serializer)
                    refresh = RefreshToken.for_user(user)
                    access = refresh.access_token
                    return Response(
                        {"access": str(access), "refresh": str(refresh)}
                    )
                return Response(
                    {"msg": "Code was wrong"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            return Response(
                {"msg": "Token does not exist."},
                status=status.HTTP_400_BAD_REQUEST,
            )


class ListUsers(APIView):
    serializer = UserSerializer
    model = get_user_model()

    def get(self, request):
        users = self.model.objects.filter(level="USER")
        return Response(self.serializer(users, many=True).data)
