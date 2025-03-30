# myapp/test_views.py

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class LoginViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_login_valid_user(self):
        """
        Ensure that a valid user can log in and receive access and refresh tokens.
        """
        response = self.client.post('/login/', {
            'username': self.username,
            'password': self.password
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_login_invalid_user(self):
        """
        Ensure that logging in with incorrect credentials returns an error.
        """
        response = self.client.post('/login/', {
            'username': 'wronguser',
            'password': 'wrongpassword'
        })

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn('error', response.data)
        self.assertEqual(response.data['error'], 'Invalid Credentials')
