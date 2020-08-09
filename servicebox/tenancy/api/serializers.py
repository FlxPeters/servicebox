from tenancy.models import Tenant, TenantGroup
from rest_framework import serializers


class NestedTenantSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="tenancy-api:tenant-detail")

    class Meta:
        model = Tenant
        fields = ["id", "url", "name", "slug"]


class TenantSerializer(serializers.ModelSerializer):

    group_id = serializers.PrimaryKeyRelatedField(
        queryset=TenantGroup.objects.all(),
        allow_null=True,
        required=False,
        source="group",
        write_only=True,
    )

    group = serializers.HyperlinkedIdentityField(
        view_name="tenancy-api:tenantgroup-detail", read_only=True
    )

    class Meta:
        model = Tenant
        fields = [
            "name",
            "slug",
            "group_id",
            "group",
            "description",
        ]


class TenantGroupSerializer(serializers.ModelSerializer):

    parent = serializers.HyperlinkedRelatedField(
        read_only=True, view_name="tenancy-api:tenantgroup-detail"
    )

    parent_id = serializers.PrimaryKeyRelatedField(
        queryset=TenantGroup.objects.all(),
        allow_null=True,
        required=False,
        source="parent",
        write_only=True,
    )

    class Meta:
        model = TenantGroup
        fields = ["name", "slug", "parent", "parent_id", "description"]
