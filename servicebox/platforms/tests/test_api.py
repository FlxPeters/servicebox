from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from platforms.models import Platform, PlatformGroup
from tenancy.models import Tenant


class PlatformGroupApiTest(APITestCase):
    def test_get_platform_group_list(self):
        """
        Ensure we can a list of platforms
        """
        p = PlatformGroup.objects.create(name="Group")

        url = reverse("platforms-api:platformgroup-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_platform_group(self):
        """
        Ensure we can a create of platforms
        """
        url = reverse("platforms-api:platformgroup-list")
        data = {"name": "test-group", "slug": "test"}
        response = self.client.post(url, data, format="json")

        group = PlatformGroup.objects.all().first()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(group.name, "test-group")

    def test_update_platform_group(self):
        """
        Ensure we can a update of platforms
        """
        p = PlatformGroup.objects.create(name="Group")
        url = reverse("platforms-api:platformgroup-detail", args=[p.id])
        data = {"name": "test-group", "slug": "test"}
        response = self.client.put(url, data, format="json")

        group = PlatformGroup.objects.all().first()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(group.name, "test-group")

    def test_delete_platform_group(self):
        """
        Ensure we can a delete of platforms
        """
        p = PlatformGroup.objects.create(name="Group")
        url = reverse("platforms-api:platformgroup-detail", args=[p.id])

        response = self.client.delete(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(PlatformGroup.objects.count(), 0)


class PlatformApiTest(APITestCase):
    def test_get_platform_list(self):
        """
        Ensure we can a list of platforms
        """
        url = reverse("platforms-api:platform-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_minimal_platform(self):
        """
        Ensure we can create a platform
        """

        tenant = Tenant.objects.create(name="Acme Corp.")

        url = reverse("platforms-api:platform-list")
        data = {
            "name": "test-platform-1",
            "slug": "test-platform",
            "tenant_id": tenant.id,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Platform.objects.count(), 1)

    def test_create_complete_platform(self):
        """
        Ensure we can create a platform
        """

        tenant = Tenant.objects.create(name="Acme Corp.")
        group = PlatformGroup.objects.create(name="Group", slug="group")

        url = reverse("platforms-api:platform-list")
        data = {
            "name": "test-platform-2",
            "slug": "test-platform",
            "tenant_id": tenant.id,
            "group_id": group.id,
            "description": "Foobar",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Platform.objects.count(), 1)

        plattform = Platform.objects.all().first()
        self.assertEqual(plattform.name, "test-platform-2")
        self.assertEqual(plattform.group.name, "Group")
        self.assertEqual(plattform.tenant.name, "Acme Corp.")

    def test_update_platform(self):
        """
        Ensure we can update a platform
        """
        tenant = Tenant.objects.create(name="Acme Corp.")
        p = Platform.objects.create(
            name="test-platform-3-old", slug="test", tenant=tenant
        )
        url = reverse("platforms-api:platform-detail", args=[p.id])
        data = {
            "name": "test-platform-3",
            "slug": "test-platform",
            "tenant_id": tenant.id,
            "description": "Foobar",
        }

        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Platform.objects.count(), 1)

        plattform = Platform.objects.all().first()
        self.assertEqual(plattform.name, "test-platform-3")
        self.assertEqual(plattform.description, "Foobar")

    def test_delete_platform(self):
        """
        Ensure we can delete a platform
        """

        tenant = Tenant.objects.create(name="Acme Corp.")
        p = Platform.objects.create(name="test", slug="test", tenant=tenant)
        url = reverse("platforms-api:platform-detail", args=[p.id])

        response = self.client.delete(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Platform.objects.count(), 0)
