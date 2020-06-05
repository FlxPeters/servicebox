from django.db import models

from platforms.models import Platform
from tenancy.models import Tenant
from autoslug import AutoSlugField
from modelchoices import Choices
from taggit.managers import TaggableManager


class ServiceStatusChoices(Choices):
    """
    Status to show the livecycle status of an service
    """

    PLANNED = ("PLANNED", "Planed")
    STAGED = ("STAGED", "Staged")
    ACTIVE = ("ACTIVE", "Active")
    DECOMMISSIONING = ("DECOMMISSIONING", "Decommissioning")
    INACTIVE = ("INACTIVE", "Inactive")


class LinkTypeChoice(Choices):
    """
    Type of an service link
    """

    WEBSITE = ("WEBSITE", "Website")
    DOCUMENTATION = ("DOCUMENTATION", "Documentation")
    LOGIN = ("LOGIN", "Login")


class Service(models.Model):
    """
    A service represents every kind of software doing some kind of work.
    This could be a batch job, but also a HTTP based service or message broker.  
    """

    name = models.CharField(
        max_length=200, unique=True, help_text="Unique name of the service"
    )
    slug = AutoSlugField(populate_from="name", editable=True)
    is_external = models.BooleanField(default=False)
    status = models.CharField(
        max_length=20,
        choices=ServiceStatusChoices.CHOICES,
        default=ServiceStatusChoices.ACTIVE,
    )
    owner = models.ForeignKey(
        Tenant,
        on_delete=models.PROTECT,
        help_text="Which tenant owns this service from a bussiness perspective and is responsible for it?",
        related_name="%(app_label)s_%(class)s_owner",
    )
    operator = models.ForeignKey(
        Tenant,
        on_delete=models.PROTECT,
        help_text="Which tenant operates and runs this service?",
        related_name="%(app_label)s_%(class)s_operator",
    )
    platform = models.ForeignKey(
        Platform,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        help_text="Platform the service is running on",
    )
    tags = TaggableManager(blank=True)
    business_overview = models.TextField(
        help_text="What business need is met by this service or system?",
    )
    technical_overview = models.TextField(
        null=True, blank=True, help_text="What kind of system is this"
    )
    service_level = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        help_text="What explicit or implicit expectations are there from users or clients about the availability of the service or system?",
    )
    hours_of_operation = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        help_text="During what hours does the service or system actually need to operate? Can portions or features of the system be unavailable at times if needed?",
    )

    def __str__(self):
        return self.name


class Link(models.Model):
    """
    A link to a service related resource
    """

    link_type = models.CharField(
        max_length=20, choices=LinkTypeChoice.CHOICES, default=LinkTypeChoice.WEBSITE,
    )
    url = models.URLField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.url
