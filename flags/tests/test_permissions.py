import json
from uuid import uuid4

from rest_framework import status
from rest_framework.test import APITestCase, APIClient, RequestsClient
from rest_framework.reverse import reverse

from flags.models import Classifier
from users.models import CustomUser

class RedFlagsTest(APITestCase):
    def create_client(self, user=None):
        u = user
        if not u:
            u = self.super_user

        client = APIClient()
        client.force_authenticate(u)
        return client

    def setUp(self):
        self.super_user = CustomUser.objects.create_superuser(
            username="super_user",
            email="super_user@gmail.com",
            password="super_user"
        )

        self.super_client = self.create_client()

        self.simple_user = CustomUser.objects.create_user(
            username="simple_user",
            email="simple_user@gmail.com",
            password="simple_user"
        )

        self.simple_client = self.create_client(user=self.simple_user)

    def get_objects(self, endpoint, params=None, client=None, pk=None):
        c = client
        if c is None:
            c = self.super_client
        if pk:
            url = reverse(endpoint, kwargs={"pk": pk})
        else:
            url = reverse(endpoint)
        if params:
            return c.get(url, data=params)
        else:
            return c.get(url)

    def test_list_request_super_user(self):
        response = self.get_objects("classifier-list", client=self.super_client)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_request_simple_user(self):
        response = self.get_objects("classifier-list", client=self.simple_client)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_request_not_auth(self):
        client = APIClient()
        response = self.get_objects("classifier-list", client=client)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_request_super_user(self):
        data = {
            "id":"12131",
            "name": "Classifier #1 name",
            "description": "Classifier #1 description",
        }
        response = self.super_client.post(reverse("classifier-list"), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Classifier.objects.count(), 1)

    def test_create_request_simple_user(self):
        data = {
            "id":"12131",
            "name": "Classifier #1 name",
            "description": "Classifier #1 description",
        }
        response = self.simple_client.post(reverse("classifier-list"), data=data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)