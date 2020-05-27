from django.db import models

from platforms.models import Platform
from tenancy.models import Tenant


class Environment(models.Model):
    name = models.CharField(max_length=200, unique=True)


class Service(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(null=True)
    platform = models.ForeignKey(Platform, on_delete=models.PROTECT, null=True)
    tenant = models.ForeignKey(Tenant, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name
