from graphene_django import DjangoObjectType

from apps.applicant.models import Applicant


class ApplicantType(DjangoObjectType):
    class Meta:
        model = Applicant
        fields = ("id", "user_id", "title", "description", "location", "status", "created_at")
