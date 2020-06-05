from services.models import Service, Link, LinkTypeChoice
from tenancy.models import Tenant
from platforms.models import Platform

# Tenants
oct = Tenant.objects.get(slug="oct")
core = Tenant.objects.get(slug="itos-core")


ur, c = Service.objects.update_or_create(
    name="Uptime Robot",
    is_external=True,
    owner=oct,
    operator=oct,
    business_overview="External service monitoring for public HTTP endpoints",
)

Link.objects.update_or_create(
    link_type=LinkTypeChoice.WEBSITE, url="https://uptimerobot.com/", service=ur
)

Service.objects.create(
    name="Active Directory",
    owner=core,
    operator=core,
    business_overview="Microsoft Active directory",
    technical_overview="ADFS and Active Directoy, including DNS",
)
