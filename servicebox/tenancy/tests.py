from django.test import TestCase

from tenancy.models import Tenant, TenantGroup
from django.db.utils import IntegrityError


class TenantModelTest(TestCase):
    def test_slug_is_generated_on_save(self):
        tenant = Tenant(name="ACME")
        self.assertEquals("", tenant.slug)
        tenant.save()
        self.assertEquals("acme", tenant.slug)

    def test_create_with_minimal_data(self):
        tenant = Tenant(name="ACME")
        tenant.save()
        self.assertEquals("ACME", tenant.name)
        self.assertEquals("acme", tenant.slug)

    def test_complete_tenant(self):

        group = TenantGroup(name="Corporations")
        group.save()
        tenant = Tenant(name="ACME", slug="a-c-m-e",
                        description="The ACME Corp", group=group)
        tenant.save()
        self.assertEquals("ACME", tenant.name)
        self.assertEquals("a-c-m-e", tenant.slug)
        self.assertEquals("The ACME Corp", tenant.description)
        self.assertEquals(group, tenant.group)

    def test_tenant_name_must_be_unique(self):
        with self.assertRaises(IntegrityError):
            tenant = Tenant(name="ACME")
            tenant.save()
            tenant2 = Tenant(name="ACME")
            tenant2.save()


class TenantGroupModelTest(TestCase):

    def test_slug_is_generated_on_save(self):
        group = TenantGroup(name="OPS")
        self.assertEquals("", group.slug)
        group.save()
        self.assertEquals("ops", group.slug)

    def test_group_has_parent_group(self):
        parent = TenantGroup(name="parent")
        parent.save()
        child = TenantGroup(name="child1", parent=parent)
        child.save()
