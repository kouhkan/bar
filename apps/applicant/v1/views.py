from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.applicant.v1.serializers import ApplicantSerializer


class CreateApplicantView(APIView):
    permission_classes = (permissions.IsAuthenticated, )
    serializer = ApplicantSerializer

    def post(self, request):
        serializer = self.serializer(data=request.data, context={"request": request})

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
