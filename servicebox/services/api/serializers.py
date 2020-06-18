from services.models import Service
from rest_framework import serializers


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
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

