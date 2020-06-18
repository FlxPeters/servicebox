from platforms.models import PlatformGroup, Platform
from rest_framework import viewsets
from platforms.api.serializers import PlatformGroupSerializer, PlatformSerializer


class PlatformViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tenants to be viewed or edited.
    """

    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer


class PlatformGroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tenant groups to be viewed or edited.
    """

    queryset = PlatformGroup.objects.all()
    serializer_class = PlatformGroupSerializer
