from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Person(models.Model):
    """
    A personal contact
    """
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)


class TenantGroup(MPTTModel):
    """
    An arbitrary collection of Tenants.
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
    description = models.CharField(
        max_length=200,
        blank=True
    )

    class Meta:
        ordering = ['name']

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Tenant(models.Model):
    """
    A Tenant represents an organization unit. This is typically a customer or an internal department.
    """
    name = models.CharField(
        max_length=30,
        unique=True
    )
    slug = models.SlugField(
        unique=True
    )
    group = models.ForeignKey(
        to='tenancy.TenantGroup',
        on_delete=models.SET_NULL,
        related_name='tenants',
        blank=True,
        null=True
    )
    description = models.CharField(
        max_length=200,
        blank=True
    )

    default_contact = models.ForeignKey(Person, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
