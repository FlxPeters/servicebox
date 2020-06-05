from tenancy.models import Tenant, TenantGroup

br, cr = TenantGroup.objects.update_or_create(name="Breuninger")
it, cr = TenantGroup.objects.update_or_create(name="ITOPS", parent=br)

oct, cr = Tenant.objects.update_or_create(name="Ops Core Tooling", slug="oct", group=it)
core, cr = Tenant.objects.update_or_create(name="Core IT", slug="itos-core", group=it)
neteng, cr = Tenant.objects.update_or_create(
    name="Network Engineering", slug="itops-neteng", group=it
)
