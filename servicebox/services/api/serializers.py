from services.models import Service, ServiceRelation, Link
from tenancy.models import Tenant
from platforms.models import Platform
from rest_framework import serializers


from tenancy.api.serializers import NestedTenantSerializer
from platforms.api.serializers import NestedPlatformSerializer
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer


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


class ServiceSerializer(TaggitSerializer, serializers.HyperlinkedModelSerializer):

    owner = NestedTenantSerializer(read_only=True)
    owner_id = serializers.PrimaryKeyRelatedField(
        source="owner", write_only=True, queryset=Tenant.objects.all()
    )
    operator = NestedTenantSerializer(read_only=True)
    operator_id = serializers.PrimaryKeyRelatedField(
        source="operator", write_only=True, queryset=Tenant.objects.all()
    )
    platform = NestedPlatformSerializer(read_only=True)
    platform_id = serializers.PrimaryKeyRelatedField(
        source="platform", write_only=True, queryset=Platform.objects.all()
    )

    tags = TagListSerializerField(required=False)
    links = NestedLinkSerializer(many=True, read_only=True)

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
            "owner_id",
            "owner_contact_person",
            "operator",
            "operator_id",
            "operator_contact_person",
            "platform",
            "platform_id",
            "tags",
            "links",
            "summary",
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
