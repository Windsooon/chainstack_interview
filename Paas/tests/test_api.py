import json
from django.urls import reverse
from django.test import TestCase
from django.contrib.auth import get_user_model
from resources.models import Resource


class ApiTestCase(TestCase):

    def test_unlimited_user_create_resource(self):
        '''
        Unlimited user can create unlimit resource
        '''
        self.user = get_user_model().objects.create_user(
            email='test@test.com', password='test_password')
        self.assertEqual(0, Resource.objects.count())
        self.client.force_login(self.user)
        response = self.client.post(
            '/resource/', content_type='application/json')
        self.assertEqual(1, Resource.objects.count())
        response = self.client.post(
            '/resource/', content_type='application/json')
        self.assertEqual(2, Resource.objects.count())

    def test_limited_user_create_resource(self):
        '''
        limited user can only create resources depend on their quota
        '''
        self.user = get_user_model().objects.create_user(
            email='test@test.com', quota=1, password='test_password')
        self.assertEqual(0, Resource.objects.count())
        self.client.force_login(self.user)
        response = self.client.post(
            '/resource/', content_type='application/json')
        self.assertEqual(1, Resource.objects.count())
        response = self.client.post(
            '/resource/', content_type='application/json')
        self.assertEqual(1, Resource.objects.count())
        self.assertEqual(response.content, b'["You do not have enough quota."]')

