from django.db import models

from platforms.models import Platform
from tenancy.models import Tenant


class Environment(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=200, unique=True,
                            help_text="Unique name of the service")
    platform = models.ForeignKey(
        Platform, on_delete=models.PROTECT, null=True, blank=True, help_text="Platform the service is running on")
    owner = models.ForeignKey(
        Tenant, on_delete=models.PROTECT, null=True, blank=True, help_text="Which team owns and runs this service or system?")
    configration_management = models.URLField(
        null=True, blank=True, help_text="Link to the source code and configuration management of the service.")
    documentation = models.URLField(
        null=True, blank=True, help_text="Link to the service docs. For example a Wiki page. ")
    business_overview = models.TextField(
        null=True, blank=True, help_text="What business need is met by this service or system? What expectations do we have about availability and performance?")
    technical_overview = models.TextField(
        null=True, blank=True, help_text="What kind of system is this")
    sla = models.CharField(
        max_length=200, null=True, blank=True, help_text="What explicit or implicit expectations are there from users or clients about the availability of the service or system?")
    hours_of_operation = models.CharField(
        max_length=200, null=True, blank=True, help_text="During what hours does the service or system actually need to operate? Can portions or features of the system be unavailable at times if needed?")
    components = models.TextField(
        null=True, blank=True, help_text="Which distinct software applications, daemons, services, etc. make up the service or system?")
    depends_on = models.ManyToManyField(
        "Service", blank=True, help_text="What external dependencies does the service have?")

    def __str__(self):
        return self.name
