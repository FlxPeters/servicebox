from django.test import TestCase

from platforms.models import Platform, PlatformGroup
from tenancy.models import Tenant


class PlatformGroupTest(TestCase):
    def _get_tenant(self):
        tenant = Tenant(name="Acme Corp.")
        tenant.save()
        return tenant

    def test_slug_is_generated_on_save(self):
        platform = Platform(name="Amazon", tenant=self._get_tenant())
        self.assertEquals("", platform.slug)
        platform.save()
        self.assertEquals("amazon", platform.slug)

    def test_create_with_minimal_data(self):
        platform = Platform(name="Amazon", tenant=self._get_tenant())
        platform.save()
        self.assertEquals("Amazon", platform.name)
        self.assertEquals("amazon", platform.slug)
        self.assertEquals("Acme Corp.", platform.tenant.name)

    def test_create_with_complete_data(self):

        group = PlatformGroup(name="Cloud")
        group.save()

        platform = Platform(
            name="Amazon",
            tenant=self._get_tenant(),
            description="Amazon AWS for Operations",
            group=group,
        )
        platform.save()
        self.assertEquals("Amazon", platform.name)
        self.assertEquals("amazon", platform.slug)
        self.assertEquals("Acme Corp.", platform.tenant.name)
        self.assertEquals("Amazon AWS for Operations", platform.description)
        self.assertEquals(group, platform.group)


class PlatformGroupModeltest(TestCase):
    def test_slug_is_generated_on_save(self):
        group = PlatformGroup(name="Cloud")
        self.assertEquals("", group.slug)
        group.save()
        self.assertEquals("cloud", group.slug)

    def test_group_has_parent_group(self):
        parent = PlatformGroup(name="parent")
        parent.save()
        child = PlatformGroup(name="child1", parent=parent)
        child.save()

    def test_complete_group(self):
        group = PlatformGroup(name="Cloud", slug="cl", description="A Cloud platform")
        self.assertEquals("Cloud", group.name)
        self.assertEquals("cl", group.slug)
        self.assertEquals("A Cloud platform", group.description)
