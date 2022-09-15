from django.urls import path
# from django.views.decorators.csrf import csrf_exempt
# from graphene_django.views import GraphQLView

from apps.applicant.v1 import views

app_name = "applicant"

urlpatterns = [
    path("create", views.CreateApplicantView.as_view(), name="create_applicant"),
]
# path("", csrf_exempt(GraphQLView.as_view(graphiql=True)), name="graphql"),
