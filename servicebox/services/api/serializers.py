from services.models import Service, ServiceRelation, Link
from rest_framework import serializers

from tenancy.api.serializers import NestedTenantSerializer
from platforms.api.serializers import NestedPlatformSerializer


class NestedLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ["link_type", "url", "description"]


class NestedRelatedServiceSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name="services-api:service-detail")

    class Meta:
        model = Service
        fields = ["name", "slug", "url"]


class ServiceRelationSerializer(serializers.ModelSerializer):

    source = NestedRelatedServiceSerializer()
    dest = NestedRelatedServiceSerializer()

    class Meta:
        model = ServiceRelation
        fields = [
            "source",
            "relation",
            "dest",
            "comment",
        ]


class ServiceSerializer(serializers.HyperlinkedModelSerializer):

    owner = NestedTenantSerializer()
    operator = NestedTenantSerializer()
    platform = NestedPlatformSerializer()
    links = NestedLinkSerializer(many=True)

    inbound_relations = serializers.SerializerMethodField()
    outbound_relations = serializers.SerializerMethodField()

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
            "links",
            "inbound_relations",
            "outbound_relations",
        ]

    def get_inbound_relations(self, obj):
        return ServiceRelationSerializer(
            obj.get_inbound_relations(), many=True, context=self.context
        ).data

    def get_outbound_relations(self, obj):
        return ServiceRelationSerializer(
            obj.get_outbound_relations(), many=True, context=self.context
        ).data
