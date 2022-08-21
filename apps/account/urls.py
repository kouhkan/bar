from django.urls import path

from apps.account import views

app_name = "account"

urlpatterns = [
    path("", views.index, name="index")
]