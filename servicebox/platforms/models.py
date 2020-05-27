from django.db import models
from tenancy.models import Tenant
from mptt.models import MPTTModel, TreeForeignKey


class PlatformGroup(MPTTModel):
    """
    An arbitrary collection of Platforms.
    """
    name = models.CharField(
        max_length=50,
        unique=True
    )
    slug = models.SlugField(
        unique=True
    )
    parent = TreeForeignKey(
        to='self',
        on_delete=models.CASCADE,
        related_name='children',
        blank=True,
        null=True,
        db_index=True
    )

    class Meta:
        ordering = ['name']

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Platform(models.Model):
    """
    A platform represents a hosting environment for service like Amazon Web Services, 
    """
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    platform_group = models.ForeignKey(PlatformGroup, on_delete=models.PROTECT)
    tenant = models.ForeignKey(Tenant, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
