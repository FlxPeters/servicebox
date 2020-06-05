from platforms.models import PlatformGroup, Platform
from tenancy.models import Tenant

cloud, cr = PlatformGroup.objects.update_or_create(name="Cloud")
on_prem, cr = PlatformGroup.objects.update_or_create(name="On premise")
aws, cr = PlatformGroup.objects.update_or_create(
    name="Amazon Web Services", slug="aws", parent=cloud
)
gcp, cr = PlatformGroup.objects.update_or_create(
    name="Goggle Cloud Platform", slug="gcp", parent=cloud
)
gcp, cr = PlatformGroup.objects.update_or_create(
    name="VM Ware", slug="vmware", parent=on_prem
)

oct = Tenant.objects.get(slug="oct")
oct_vmware = Platform.objects.update_or_create(
    name="OCT VMWare Cluster", group=on_prem, tenant=oct
)
itops_vmware = Platform.objects.update_or_create(
    name="ITOPS VMWare Cluster", group=on_prem, tenant=oct
)
itops_aws_ops = Platform.objects.update_or_create(
    name="ITOPS AWS Ops", group=aws, tenant=oct
)
itops_aws = Platform.objects.update_or_create(name="ITOPS AWS", group=aws, tenant=oct)

itops_aws_eks = Platform.objects.update_or_create(
    name="ITOPS AWS Kubernetes", group=aws, tenant=oct
)
