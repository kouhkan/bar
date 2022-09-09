from rest_framework import serializers

from apps.applicant.models import Applicant
from apps.applicant.v1.applicant_logics import create_applicant


class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = ("title", "description", "location")

    def save(self, **kwargs):
        user = self.context["request"].user
        create_applicant(user_id=user, **self.validated_data)
        return True
