from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from platforms.models import Platform
from tenancy.models import Tenant
from services.models import Service, ServiceRelation, Link, ServiceStatusChoices


class ServiceApiTest(APITestCase):
    def setUp(self):
        self.tenant_owner = Tenant.objects.create(name="Acme Corp.")
        self.tenant_operator = Tenant.objects.create(name="Operator Incl.")
        self.platform = Platform.objects.create(
            name="Road Runner Cloud", tenant=self.tenant_owner
        )

    def test_get_service_list(self):
        """
        Ensure we can a list of services
        """

        service = Service.objects.create(
            name="Demo SVC",
            operator=self.tenant_operator,
            owner=self.tenant_owner,
            platform=self.platform,
        )

        url = reverse("services-api:service-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_minimal_service(self):
        """
        Ensure we can a create a minimal service
        """
        url = reverse("services-api:service-list")
        data = {
            "name": "test-svc",
            "slug": "test-svc",
            "owner_id": self.tenant_owner.id,
            "operator_id": self.tenant_operator.id,
            "platform_id": self.platform.id,
        }

        response = self.client.post(url, data, format="json")
        svc = Service.objects.all().first()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(svc.name, "test-svc")

    def test_create_complete_service(self):
        """
        Ensure we can a create a fully fledged service
        """
        url = reverse("services-api:service-list")
        data = {
            "name": "test-svc",
            "slug": "test-svc",
            "status": "ACTIVE",
            "owner_id": self.tenant_owner.id,
            "owner_contact_person": "John Doe",
            "operator_id": self.tenant_operator.id,
            "operator_contact_person": "Marvin",
            "platform_id": self.platform.id,
            "tags": ["1", "2", "3"],
            "summary": "A text about my service"
        }

        response = self.client.post(url, data, format="json")
        svc = Service.objects.all().first()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(svc.name, "test-svc")
        self.assertEqual(svc.status, ServiceStatusChoices.ACTIVE)
        self.assertEqual(svc.owner_contact_person, "John Doe")
        self.assertEqual(svc.operator_contact_person, "Marvin")
        self.assertEqual(len(svc.tags.all()), 3)
        self.assertEqual(svc.summary, "A text about my service")
