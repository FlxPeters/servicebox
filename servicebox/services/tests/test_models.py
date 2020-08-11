from django.test import TestCase

from services.models import (
    Service,
    ServiceStatusChoices,
    ServiceRelation,
    ServiceRealtionChoice,
    Link,
    LinkTypeChoice,
)
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

    def test_service_has_related_services(self):
        source = Service.objects.create(
            name="Source",
            operator=self.tenant_operator,
            owner=self.tenant_owner,
            platform=self.platform,
        )
        dest = Service.objects.create(
            name="Dest",
            operator=self.tenant_operator,
            owner=self.tenant_owner,
            platform=self.platform,
        )

        ServiceRelation.objects.create(
            source=source,
            relation=ServiceRealtionChoice.RELATED,
            dest=dest,
            comment="test",
        )

        inbound_list = dest.get_inbound_relations()
        self.assertEqual(1, len(inbound_list))
        self.assertEqual("test", inbound_list.first().comment)
        self.assertEqual("Source", inbound_list.first().source.name)

        outbound_list = source.get_outbound_relations()
        self.assertEqual(1, len(outbound_list))
        self.assertEqual("test", outbound_list.first().comment)
        self.assertEqual("Dest", outbound_list.first().dest.name)

    def test_service_has_link(self):
        svc = Service.objects.create(
            name="Service",
            operator=self.tenant_operator,
            owner=self.tenant_owner,
            platform=self.platform,
        )

        link = Link.objects.create(
            link_type=LinkTypeChoice.WEBSITE,
            url="http://example.com",
            description="My fancy Website",
            service=svc,
        )

        self.assertEqual(svc.links.first().url, "http://example.com")
        self.assertEqual(svc.links.first().link_type, LinkTypeChoice.WEBSITE)
        self.assertEqual(svc.links.first().description, "My fancy Website")
