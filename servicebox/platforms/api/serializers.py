from platforms.models import Platform, PlatformGroup
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
    tenant = serializers.HyperlinkedRelatedField(
        read_only=True, view_name="tenancy-api:tenant-detail"
    )

    class Meta:
        model = Platform
        fields = ["name", "slug", "tenant", "group", "description"]


class PlatformGroupSerializer(serializers.ModelSerializer):

    parent = serializers.HyperlinkedRelatedField(
        read_only=True, view_name="platforms-api:platformgroup-detail"
    )

    class Meta:
        model = PlatformGroup
        fields = ["name", "slug", "parent", "description"]
