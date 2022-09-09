from django.urls import path

from apps.applicant.v1 import views

app_name = "applicant"

urlpatterns = [
    path("create", views.CreateApplicantView.as_view(), name="create_applicant"),
]
