from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.account.v1.serializers import UserSerializer


class CreateUser(APIView):
    serializer = UserSerializer
    model = get_user_model()

    def post(self, request):
        serializer = self.serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response(serializer.data)


class ListUsers(APIView):
    serializer = UserSerializer
    model = get_user_model()

    def get(self, request):
        users = self.model.objects.filter(level="USER")
        return Response(self.serializer(users, many=True).data)
