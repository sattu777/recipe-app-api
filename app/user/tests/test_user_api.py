"""
Test for the user api
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse('user:create')

def create_user(**params):
    """Create and return a new user"""
    return get_user_model().objects.create_user(**params)

class PublicUserAPITests(TestCase):
    '''
    Test the public features of user api
    '''
    def setUp(self):
        self.client = APIClient()

    def test_create_user_success(self):
        '''
        test for creating user is successful
        '''

        payload = {
            'email': 'test@exaple.com',
            'password': 'testpass123',
            'name': 'Test Name',
        }

        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(email=payload['email'])
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_user_with_email_exists_error(self):
        '''
        checks if user with email already exists
        '''

        payload = {
            'email': 'test@exaple.com',
            'password': 'testpass123',
            'name': 'Test Name',
        }

        create_user(**payload)

        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

def test_password_too_short_error(self):
    '''
    check if the user password is too small
    '''

    payload = {
            'email': 'test@exaple.com',
            'password': 'pw',
            'name': 'Test Name',
        }

    res = self.client.post(CREATE_USER_URL, payload)

    res.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    user_exists = get_user_model().objects.filter(
        email=payload['email']
    ).exists()

    self.assertFalse(user_exists)
