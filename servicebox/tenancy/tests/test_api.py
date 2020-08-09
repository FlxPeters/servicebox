from django.test import TestCase

from rest_framework.test import APITestCase
from rest_framework import status

from tenancy.api.views import TenantViewSet
from tenancy.models import Tenant, TenantGroup


class TenantGroupTest(APITestCase):
    def setUp(self):
        self.base_url = "/api/tenancy/tenant-groups/"

    def test_api_root_exists(self):
        response = self.client.get("{}?format=api".format(self.base_url))
        self.assertEqual(response.status_code, 200)

    def test_list(self):
        TenantGroup.objects.create(name="group")
        response = self.client.get(self.base_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "group")

    def test_create(self):
        data = {"name": "group", "slug": "group"}
        response = self.client.post(self.base_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(TenantGroup.objects.count(), 1)

    def test_update(self):
        group = TenantGroup.objects.create(name="Group", slug="group")
        data = {"name": "Group", "description": "foobar", "slug": "group"}
        response = self.client.put(self.base_url + str(group.id) + "/", data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(TenantGroup.objects.all().first().name, "Group")
        self.assertEqual(TenantGroup.objects.all().first().description, "foobar")

    def test_delete(self):
        group = TenantGroup.objects.create(name="Group", slug="group")
        response = self.client.delete(self.base_url + str(group.id) + "/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(TenantGroup.objects.count(), 0)


class TenantTest(APITestCase):
    def setUp(self):
        self.base_url = "/api/tenancy/tenants/"

    def test_api_root_exists(self):
        response = self.client.get("{}?format=api".format(self.base_url))
        self.assertEqual(response.status_code, 200)

    def test_list(self):
        Tenant.objects.create(name="Test", slug="test")
        response = self.client.get(self.base_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["slug"], "test")

    def test_create_minimal_tenant(self):
        """
        Ensure we can create a new tenant object with full data.
        """

        data = {"name": "Foo", "slug": "foo", "group": None}
        response = self.client.post(self.base_url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tenant.objects.count(), 1)
        self.assertEqual(Tenant.objects.get().name, "Foo")
        self.assertEqual(Tenant.objects.get().slug, "foo")
        self.assertEqual(Tenant.objects.count(), 1)

    def test_create_full_tenant(self):
        """
        Ensure we can create a new tenant object with full data.
        """

        group = TenantGroup.objects.create(name="Group", slug="group")
        data = {
            "name": "Foo",
            "slug": "foo",
            "description": "Just a test",
            "group_id": group.id,
        }

        response = self.client.post(self.base_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tenant.objects.count(), 1)
        self.assertEqual(Tenant.objects.get().name, "Foo")
        self.assertEqual(Tenant.objects.get().slug, "foo")
        self.assertEqual(Tenant.objects.get().description, "Just a test")
        self.assertEqual(Tenant.objects.get().group.name, "Group")
        self.assertEqual(Tenant.objects.count(), 1)

    def test_update(self):
        tenant = Tenant.objects.create(name="Test", slug="test")
        data = {"name": "Test", "slug": "test", "description": "test"}
        response = self.client.put(self.base_url + str(tenant.id) + "/", data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Tenant.objects.all().first().description, "test")

    def test_delete(self):
        tenant = Tenant.objects.create(name="Test", slug="test")
        response = self.client.delete(self.base_url + str(tenant.id) + "/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Tenant.objects.count(), 0)
