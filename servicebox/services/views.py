from django.utils import timezone
from django_tables2 import SingleTableView
from django.views.generic import DetailView

from services.models import Service
from .tables import ServiceTable


class ServiceListView(SingleTableView):

    model = Service
    table_class = ServiceTable


class ServiceDetailView(DetailView):
    model = Service
    context_object_name = "service"
