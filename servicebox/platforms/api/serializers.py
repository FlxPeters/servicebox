from platforms.models import Platform, PlatformGroup
from rest_framework import serializers


class PlatformSerializer(serializers.HyperlinkedModelSerializer):

    group = serializers.HyperlinkedRelatedField(
        read_only=True, view_name="platformgroup-detail"
    )
    tenant = serializers.HyperlinkedRelatedField(
        read_only=True, view_name="tenant-detail"
    )

    class Meta:
        model = Platform
        fields = ["name", "slug", "tenant", "group", "description"]


class PlatformGroupSerializer(serializers.ModelSerializer):

    parent = serializers.HyperlinkedRelatedField(
        read_only=True, view_name="platformgroup-detail"
    )

    class Meta:
        model = PlatformGroup
        fields = ["name", "slug", "parent", "description"]
