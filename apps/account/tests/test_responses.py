from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from apps.account.utils.redis_auth_handler import remove_token_user


class AccountAppTests(APITestCase):
    def setUp(self) -> None:
        super().setUp()
        self.client = APIClient()

    def tearDown(self) -> None:
        email = "test@gmail.com"
        remove_token_user(email)

    def test_register_user(self):
        url = reverse("account:register_user")
        data = {"email": "test@gmail.com"}
        response = self.client.post(url, data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {})

    def test_token_user(self):
        self.client.post(reverse("account:register_user"), {"email": "test@gmail.com"})

        url = reverse("account:token_user")
        data = {"email": "test@gmail.com", "token": "000000"}
        response = self.client.put(url, data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)

        self.client.post(reverse("account:register_user"), {"email": "test@gmail.com"})

        url = reverse("account:token_user")
        data = {"email": "test@gmail.com", "token": "000000"}
        response = self.client.put(url, data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_list_users(self):
        url = reverse("account:list_users")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
