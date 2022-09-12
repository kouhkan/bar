from django.urls import path

from graphene_django.views import GraphQLView

from apps.applicant.v1 import views

app_name = "applicant"

urlpatterns = [
    path("", GraphQLView.as_view(graphiql=True), name="graphql"),
    path("create", views.CreateApplicantView.as_view(), name="create_applicant"),
]
