import graphene
from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType

from apps.applicant.models import Applicant


class ApplicantType(DjangoObjectType):
    class Meta:
        model = Applicant
        fields = ("id", "user_id", "title", "description", "location", "status", "created_at")


class ApplicantInput(graphene.InputObjectType):
    id = graphene.Int(required=False)
    user_id = graphene.Int()
    title = graphene.String()
    description = graphene.String()
    location = graphene.String()


class ApplicantUpdateInput(graphene.InputObjectType):
    id = graphene.Int(required=True)
    user_id = graphene.Int(required=False)
    title = graphene.String(required=False)
    description = graphene.String(required=False)
    location = graphene.String(required=False)


class ApplicantDeleteInput(graphene.InputObjectType):
    id = graphene.Int(required=True)


class Query(graphene.ObjectType):
    applicants = graphene.List(ApplicantType)
    applicant = graphene.Field(ApplicantType, id=graphene.Int())

    def resolve_applicants(self, info, **kwargs):
        return Applicant.objects.all()

    def resolve_applicant(self, info, id):
        return Applicant.objects.get(id=id)


class CreateApplicant(graphene.Mutation):
    class Arguments:
        data = ApplicantInput(required=True)

    applicant = graphene.Field(ApplicantType)

    @staticmethod
    def mutate(root, info, data=None):
        user = get_user_model().objects.get(id=data.user_id)
        applicant = Applicant.objects.create(
            user_id=user,
            title=data.title,
            description=data.description,
            location=data.location,
        )

        return CreateApplicant(applicant=applicant)


class UpdateApplicant(graphene.Mutation):
    class Arguments:
        data = ApplicantUpdateInput(required=True)

    applicant = graphene.Field(ApplicantType)

    @staticmethod
    def mutate(root, info, data=None):
        if not (applicant := Applicant.objects.get(id=data.id)):
            return UpdateApplicant(applicant=None)

        applicant.title = data.get("title", applicant.title)
        applicant.description = data.get("description", applicant.description)
        applicant.location = data.get("location", applicant.location)
        if user := get_user_model().objects.get(id=data.user_id):
            applicant.user_id = user
        applicant.save()
        return UpdateApplicant(applicant=applicant)


class DeleteApplicant(graphene.Mutation):
    class Arguments:
        data = ApplicantDeleteInput(required=True)

    applicant = graphene.Field(ApplicantType)

    @staticmethod
    def mutate(root, info, data):
        if not (applicant := Applicant.objects.get(id=data.id)):
            return DeleteApplicant(applicant=None)
        applicant.delete()
        return None


class Mutation(graphene.ObjectType):
    create_applicant = CreateApplicant.Field()
    update_applicant = UpdateApplicant.Field()
    delete_applicant = DeleteApplicant.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
