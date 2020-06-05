from django.contrib import admin
from .models import Tenant, TenantGroup
from mptt.admin import MPTTModelAdmin

admin.site.register(TenantGroup, MPTTModelAdmin)
admin.site.register(Tenant)
