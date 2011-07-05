"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.conf import settings
from time import sleep
from apikey.models import Token


class TokenTest(TestCase):

    fixtures = ['items.json']

    def setUp(self):
        self.user = User.objects.create_user('u', 'u@u.com', 'u')

    def test_create_token(self):
        " Create a token."
        token = Token.objects.create(self.user)
        self.assertEqual(len(token.token), settings.TOKEN_SIZE)

    def test_make_request(self):
        " Make a request authenticated with Token."

        token = Token.objects.create(self.user)
        client = Client()
        response = client.get('/items', HTTP_X_AUTH_TEST_TOKEN=token.token)
        self.assertEqual(response.status_code, 200)

    def test_make_request_without_token(self):
        " Make a request without token."

        client = Client()
        response = client.get('/items')
        self.assertEqual(response.status_code, 401)

    def test_make_request_with_non_existing_token(self):
        " Make a request with an non existing token."

        client = Client()
        response = client.get('/items', HTTP_X_AUTH_TEST_TOKEN='xxx')
        self.assertEqual(response.status_code, 401)

    def test_make_request_with_invalid_token(self):
        " Make a request with an invalid token."

        token = Token.objects.create(self.user)
        client = Client()
        response = client.get('/items', HTTP_X_AUTH_TEST_TOKEN=token.token)
        self.assertEqual(response.status_code, 200)
        sleep(2)
        response = client.get('/items', HTTP_X_AUTH_TEST_TOKEN=token.token)
        self.assertEqual(response.status_code, 401)
