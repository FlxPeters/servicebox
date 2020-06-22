from services.models import Service
from rest_framework import serializers


class ServiceSerializer(serializers.HyperlinkedModelSerializer):

    owner = serializers.HyperlinkedRelatedField(
        read_only=True, view_name="tenancy-api:tenant-detail"
    )

    operator = serializers.HyperlinkedRelatedField(
        read_only=True, view_name="tenancy-api:tenant-detail"
    )

    platform = serializers.HyperlinkedRelatedField(
        read_only=True, view_name="platforms-api:platform-detail"
    )

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
