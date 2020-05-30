from django.contrib import admin
from .models import Tenant, TenantGroup


admin.site.register(TenantGroup)
admin.site.register(Tenant)
