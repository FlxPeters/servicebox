from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Platform, PlatformGroup

admin.site.register(PlatformGroup, MPTTModelAdmin)
admin.site.register(Platform)
