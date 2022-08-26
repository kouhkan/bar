from django.urls import path, include
from rest_framework import routers

from apps.account.v1 import views

app_name = "account"

urlpatterns = [
    path("list", views.ListUsers.as_view(), name="list_users"),
    path("register", views.CreateUser.as_view(), name="create_user"),
]
