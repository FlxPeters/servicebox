from services.models import Service
from rest_framework import serializers

from tenancy.api.serializers import NestedTenantSerializer
from platforms.api.serializers import NestedPlatformSerializer


class ServiceSerializer(serializers.HyperlinkedModelSerializer):

    owner = NestedTenantSerializer()
    operator = NestedTenantSerializer()
    platform = NestedPlatformSerializer()

    class Meta:
        model = Service
        fields = [
            "name",
            "slug",
            "created_at",
            "updated_at",
            "status",
            "is_external",
            "owner",
            "operator",
            "platform",
        ]
