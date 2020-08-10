from platforms.models import Platform, PlatformGroup
from tenancy.models import Tenant
from rest_framework import serializers


class NestedPlatformSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="platforms-api:platformgroup-detail"
    )

    class Meta:
        model = Platform
        fields = ["id", "url", "name", "slug"]


class PlatformSerializer(serializers.HyperlinkedModelSerializer):

    group = serializers.HyperlinkedRelatedField(
        read_only=True, view_name="platforms-api:platformgroup-detail"
    )
    group_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        source="group",
        queryset=PlatformGroup.objects.all(),
        required=False,
        allow_null=True,
    )

    tenant = serializers.HyperlinkedRelatedField(
        read_only=True, view_name="tenancy-api:tenant-detail"
    )
    tenant_id = serializers.PrimaryKeyRelatedField(
        write_only=True, source="tenant", queryset=Tenant.objects.all()
    )

    class Meta:
        model = Platform
        fields = [
            "name",
            "slug",
            "tenant",
            "tenant_id",
            "group",
            "group_id",
            "description",
        ]


class PlatformGroupSerializer(serializers.ModelSerializer):

    parent = serializers.HyperlinkedRelatedField(
        read_only=True, view_name="platforms-api:platformgroup-detail"
    )

    class Meta:
        model = PlatformGroup
        fields = ["name", "slug", "parent", "description"]
