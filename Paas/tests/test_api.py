import json
from rest_framework.reverse import reverse
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
            reverse('resource-list'), content_type='application/json')
        self.assertEqual(1, Resource.objects.count())
        response = self.client.post(
            reverse('resource-list'), content_type='application/json')
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
            reverse('resource-list'), content_type='application/json')
        self.assertEqual(1, Resource.objects.count())
        response = self.client.post(
            reverse('resource-list'), content_type='application/json')
        self.assertEqual(1, Resource.objects.count())
        self.assertEqual(response.content, b'["You do not have enough quota."]')

    def test_user_list_resource(self):
        self.user = get_user_model().objects.create_user(
            email='test@test.com', password='test_password')
        self.client.force_login(self.user)
        # Create some resources
        for _ in range(3):
            response = self.client.post(
                reverse('resource-list'), content_type='application/json')
        response = self.client.get(
            reverse('resource-list'), content_type='application/json')
        self.assertEqual(3, len(response.json()))

    def test_user_delete_resource(self):
        self.user = get_user_model().objects.create_user(
            email='test@test.com', password='test_password')
        self.client.force_login(self.user)
        # Create some resources
        response = self.client.post(
            reverse('resource-list'), content_type='application/json')
        id = response.json()['id']
        self.assertEqual(1, Resource.objects.count())
        response = self.client.delete(
            reverse('resource-detail', args=(id,)),
            content_type='application/json')
        self.assertEqual(0, Resource.objects.count())

    def test_user_wouldnot_list_others_resource(self):
        self.user = get_user_model().objects.create_user(
            email='test@test.com', password='test_password')
        self.user2 = get_user_model().objects.create_user(
            email='test2@test.com', password='test_password')
        self.client.force_login(self.user)
        response = self.client.post(
            reverse('resource-list'), content_type='application/json')
        self.client.logout()
        # Can't list other user's resource
        self.client.force_login(self.user2)
        response = self.client.get(
            reverse('resource-list'), content_type='application/json')
        self.assertEqual(0, len(response.json()))

    def test_user_cannot_access_others_resource(self):
        '''
        Except Sueruser, user can't access others's resources
        '''
        self.user = get_user_model().objects.create_user(
            email='test@test.com', password='test_password')
        self.user2 = get_user_model().objects.create_user(
            email='test2@test.com', password='test_password')
        # Create Superuser
        self.superuser = get_user_model().objects.create_superuser(
            email='super@user.com', password='test_password')
        self.client.force_login(self.user)
        response = self.client.post(
            reverse('resource-list'), content_type='application/json')
        self.client.logout()
        self.client.force_login(self.user2)
        id = response.json()['id']
        response = self.client.get(
            reverse('resource-detail', args=(id,)),
            content_type='application/json')
        self.assertEqual(
            {"detail":"Only owner can access the resource."}, response.json())
        response = self.client.delete(
            reverse('resource-detail', args=(id,)),
            content_type='application/json')
        self.assertEqual(
            {"detail":"Only owner can access the resource."}, response.json())
        self.client.logout()
        # Superuser can access resource
        self.client.force_login(self.superuser)
        response = self.client.get(
            reverse('resource-detail', args=(id,)),
            content_type='application/json')
        self.assertEqual(1, response.json()['id'])

    def test_superuser_operate_resource(self):
        '''
        Superuser can list, create, delete his/her own resources
        '''
        self.superuser = get_user_model().objects.create_superuser(
            email='super@user.com', password='test_password')
        self.client.force_login(self.user)
