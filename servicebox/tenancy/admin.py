from django.contrib import admin
from .models import Tenant, TenantGroup, Person


admin.site.register(TenantGroup)
admin.site.register(Tenant)
admin.site.register(Person)
