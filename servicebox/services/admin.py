from django.contrib import admin
from .models import Service, Link, ServiceRelation

admin.site.register(Service)
admin.site.register(Link)
admin.site.register(ServiceRelation)
