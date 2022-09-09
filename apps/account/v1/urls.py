from django.urls import path

from apps.account.v1 import views

app_name = "account"

urlpatterns = [
    path("", views.ListUsers.as_view(), name="list_users"),
    path("register", views.RegisterUserView.as_view(), name="register_user"),
    path("token", views.TokenSerializerView.as_view(), name="token_user"),
]
