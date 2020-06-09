from django.views.generic import ListView
from .models import Tenant


class TenantsListView(ListView):
    model = Tenant
