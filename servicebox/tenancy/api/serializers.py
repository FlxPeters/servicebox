from tenancy.models import Tenant, TenantGroup
from rest_framework import serializers


class TenantSerializer(serializers.HyperlinkedModelSerializer):

    group = serializers.HyperlinkedRelatedField(
        read_only=True, view_name="tenantgroup-detail"
    )

    class Meta:
        model = Tenant
        fields = ["name", "slug", "group", "description"]


class TenantGroupSerializer(serializers.ModelSerializer):

    parent = serializers.HyperlinkedRelatedField(
        read_only=True, view_name="tenantgroup-detail"
    )

    class Meta:
        model = TenantGroup
        fields = ["name", "slug", "parent", "description"]
