from django.test import TestCase

from services.models import Service, ServiceStatusChoices
from tenancy.models import Tenant
from platforms.models import Platform


class ServiceModelTest(TestCase):
    def setUp(self):
        self.tenant_owner = Tenant.objects.create(name="Acme Corp.")
        self.tenant_operator = Tenant.objects.create(name="Operator Incl.")
        self.platform = Platform.objects.create(
            name="Road Runner Cloud", tenant=self.tenant_owner
        )

    def test_slug_is_generated_on_save(self):
        service = Service(
            name="Prometheus",
            operator=self.tenant_operator,
            owner=self.tenant_owner,
            platform=self.platform,
        )
        self.assertEquals("", service.slug)
        service.save()
        self.assertEquals("prometheus", service.slug)

    def test_service_is_active_by_default(self):

        service = Service(
            name="Prometheus",
            operator=self.tenant_operator,
            owner=self.tenant_owner,
            platform=self.platform,
        )
        self.assertEquals(ServiceStatusChoices.ACTIVE, service.status)
