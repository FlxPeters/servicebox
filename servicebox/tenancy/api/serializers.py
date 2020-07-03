from tenancy.models import Tenant, TenantGroup
from rest_framework import serializers


class NestedTenantSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="tenancy-api:tenant-detail")

    class Meta:
        model = Tenant
        fields = ["id", "url", "name", "slug"]


class TenantSerializer(serializers.HyperlinkedModelSerializer):

    group = serializers.HyperlinkedRelatedField(
        read_only=True, view_name="tenancy-api:tenantgroup-detail"
    )

    class Meta:
        model = Tenant
        fields = ["name", "slug", "group", "description"]


class TenantGroupSerializer(serializers.ModelSerializer):

    parent = serializers.HyperlinkedRelatedField(
        read_only=True, view_name="tenancy-api:tenantgroup-detail"
    )

    class Meta:
        model = TenantGroup
        fields = ["name", "slug", "parent", "description"]
