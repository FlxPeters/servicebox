from django.db import models
from django.urls import reverse

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


class ServiceRealtionChoice(Choices):
    """
    Type of a service relation
    """

    RELATED = ("RELATED", "Is related to")
    DEPENDS_ON = ("DEPENDS_ON", "Depends on")
    BELONGS_TO = ("BELONGS_TO", "Belongs to")
    DUPLICATES = ("DUPLICATES", "Duplicates")


class ServiceRelation(models.Model):
    """
    A relation between two services
    """

    source = models.ForeignKey(
        "Service", on_delete=models.CASCADE, related_name="source_service_set"
    )
    relation = models.CharField(max_length=20, choices=ServiceRealtionChoice.CHOICES)
    dest = models.ForeignKey(
        "Service", on_delete=models.CASCADE, related_name="dest_service_set",
    )
    comment = models.CharField(
        max_length=200, null=True, blank=True, help_text="A comment about the relation"
    )

    def __str__(self):
        return "{} {} {}".format(self.source, self.relation, self.dest)


class Service(models.Model):
    """
    A service represents every kind of software doing some kind of work.
    This could be a batch job, but also a HTTP based service or message broker.  
    """

    name = models.CharField(
        max_length=200, unique=True, help_text="Unique name of the service"
    )
    slug = AutoSlugField(populate_from="name", editable=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_external = models.BooleanField(default=False, verbose_name="External")
    status = models.CharField(
        max_length=20,
        choices=ServiceStatusChoices.CHOICES,
        default=ServiceStatusChoices.ACTIVE,
    )
    owner = models.ForeignKey(
        Tenant,
        on_delete=models.PROTECT,
        help_text="Which tenant owns this service from a bussiness perspective and is responsible for it?",
        related_name="owner",
    )
    owner_contact_person = models.TextField(
        null=True, blank=True, help_text="A primary contact person on the owner tenant"
    )

    operator = models.ForeignKey(
        Tenant,
        on_delete=models.PROTECT,
        help_text="Which tenant operates and runs this service?",
        related_name="operator",
    )
    operator_contact_person = models.TextField(
        null=True,
        blank=True,
        help_text="A primary contact person on the operator tenant",
    )

    platform = models.ForeignKey(
        Platform,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        help_text="Platform the service is running on",
    )
    tags = TaggableManager(blank=True)
    summary = models.TextField(
        help_text="A short summary about the service", null=True, blank=True
    )
    # technical_overview = models.TextField(
    #     null=True, blank=True, help_text="What kind of system is this"
    # )
    # service_level = models.CharField(
    #     max_length=200,
    #     null=True,
    #     blank=True,
    #     help_text="What explicit or implicit expectations are there from users or clients about the availability of the service or system?",
    # )
    # hours_of_operation = models.CharField(
    #     max_length=200,
    #     null=True,
    #     blank=True,
    #     help_text="During what hours does the service or system actually need to operate? Can portions or features of the system be unavailable at times if needed?",
    # )

    def get_absolute_url(self):
        return reverse("services.views.details", args=[str(self.id)])

    def get_fully_qualified_name(self):
        return "%s-%s" % (self.owner.slug, self.slug)

    def get_inbound_relations(self):
        return self.dest_service_set.all()

    def get_outbound_relations(self):
        return self.source_service_set.all()

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
    service = models.ForeignKey(
        "Service", on_delete=models.CASCADE, related_name="links"
    )
    description = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.url

