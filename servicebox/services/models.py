from django.db import models

from platforms.models import Platform
from tenancy.models import Tenant
from autoslug import AutoSlugField
from modelchoices import Choices


class ServiceStatusChoices(Choices):
    STATUS_ACTIVE = ("ACTIVE", "Active")
    STATUS_PLANNED = ("PLANNED", "planed")
    STATUS_STAGED = ("STAGED", "staged")
    STATUS_DECOMMISSIONING = ("DECOMMISSIONING", "Decommissioning")


class BaseService(models.Model):
    """
    An abstract definition of services.
    A service has allways a unique name, status, owner and operator. 
    """

    name = models.CharField(
        max_length=200, unique=True, help_text="Unique name of the service"
    )
    slug = AutoSlugField(populate_from="name")
    status = models.CharField(
        max_length=20,
        choices=ServiceStatusChoices.CHOICES,
        default=ServiceStatusChoices.STATUS_ACTIVE,
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
    business_overview = models.TextField(
        help_text="What business need is met by this service or system?",
    )

    class Meta:
        abstract = True


class ExternalService(BaseService):
    """
    Represents an service which is not under direct controll of the organization running servicebox.
    """

    website = models.URLField(
        null=True, blank=True, help_text="Link to the website of the external service.",
    )

    # todo: sla
    # statuspage
    # monitoring


class Service(BaseService):
    """
    A service represents every kind of software doing some kind of work.
    This could be a batch job, but also a HTTP based service or message broker.  
    """

    platform = models.ForeignKey(
        Platform,
        on_delete=models.PROTECT,
        help_text="Platform the service is running on",
    )
    source_code_link = models.URLField(
        null=True,
        blank=True,
        help_text="Link to the source code and configuration management of the service.",
    )
    documentation_link = models.URLField(
        null=True,
        blank=True,
        help_text="Link to the service docs. For example a Wiki page. ",
    )
    technical_overview = models.TextField(
        null=True, blank=True, help_text="What kind of system is this"
    )
    sla = models.CharField(
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
    components = models.TextField(
        null=True,
        blank=True,
        help_text="Which distinct software applications, daemons, services, etc. make up the service or system?",
    )
    depends_on = models.ManyToManyField(
        "Service",
        blank=True,
        help_text="What external dependencies does the service have?",
    )

    def __str__(self):
        return self.name
