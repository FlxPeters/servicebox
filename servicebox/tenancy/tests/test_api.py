from django.test import TestCase

from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from rest_framework import status

from tenancy.api.views import TenantViewSet
from tenancy.models import Tenant


class AppTest(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.base_url = "/api/tenancy/"

    def test_api_root_exists(self):

        response = self.client.get("{}?format=api".format(self.base_url))

        self.assertEqual(response.status_code, 200)

    def test_list_view(self):
        url = "{}tenants".format(self.base_url)
        view = TenantViewSet.as_view({"get": "list"})

        request = self.factory.get(url)
        response = view(request)

        self.assertEqual(response.status_code, 200)

    def test_create_minimal_tenant(self):
        """
        Ensure we can create a new tenant object with full data.
        """

        url = "{}tenants/".format(self.base_url)
        data = {"name": "Foo"}

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tenant.objects.count(), 1)
        self.assertEqual(Tenant.objects.get().name, "Foo")
        self.assertEqual(Tenant.objects.get().slug, "foo")

    def test_create_full_tenant(self):
        """
        Ensure we can create a new tenant object with full data.
        """

        url = "{}tenants/".format(self.base_url)
        data = {"name": "Foo", "slug": "foo", "description": "Just a test"}

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tenant.objects.count(), 1)
        self.assertEqual(Tenant.objects.get().name, "Foo")
        self.assertEqual(Tenant.objects.get().slug, "foo")
        self.assertEqual(Tenant.objects.get().description, "Just a test")

