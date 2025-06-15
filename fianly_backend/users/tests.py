from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status

class UsersEndpointTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            "username": "testuser",
            "password": "TestPass123",
            "first_name": "Test",
            "last_name": "User"
        }

    def test_register_user_success(self):
        response = self.client.post("/register", self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["message"], "Usuario creado exitosamente")

    def test_auth_user_success(self):
        User.objects.create_user(**self.user_data)
        response = self.client.post("/auth", {
            "user": "testuser",
            "password": "TestPass123"
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("token", response.data)
        self.assertEqual(response.data["user_name"], "Test")

    def test_get_users_requires_auth(self):
        User.objects.create_user(**self.user_data)
        token_response = self.client.post("/auth", {
            "user": "testuser",
            "password": "TestPass123"
        }, format='json')
        token = token_response.data["token"]

        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        response = self.client.get("/user")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(isinstance(response.data, list))
        self.assertEqual(response.data[0]["user_name"], "Test")
        self.assertEqual(response.data[0]["user_lastname"], "User")
