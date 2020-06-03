from django.contrib import admin
from .models import Service, ExternalService

admin.site.register(Service)
admin.site.register(ExternalService)
