from tenancy.models import TenantGroup, Tenant
from rest_framework import viewsets
from tenancy.api.serializers import TenantGroupSerializer, TenantSerializer


class TenantViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tenants to be viewed or edited.
    """

    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer


class TenantGroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tenant groups to be viewed or edited.
    """

    queryset = TenantGroup.objects.all()
    serializer_class = TenantGroupSerializer
