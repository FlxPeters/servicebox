from django_tables2 import tables, TemplateColumn, Column
from .models import Service


class ServiceTable(tables.Table):
    class Meta:
        model = Service
        template_name = "django_tables2/bootstrap.html"
        fields = ("name", "status", "owner", "operator", "platform", "edit")

    name = Column(linkify=True)
    edit = TemplateColumn(
        template_name="services/tables/edit.html", orderable=False, verbose_name=""
    )
