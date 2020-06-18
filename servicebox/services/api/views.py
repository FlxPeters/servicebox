from services.models import Service
from rest_framework import viewsets
from services.api.serializers import ServiceSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows services to be viewed or edited.
    """

    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
