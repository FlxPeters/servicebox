from django.urls import path

from tenancy.views import TenantsListView

urlpatterns = [
    path("", TenantsListView.as_view(), name="tenancy.views.list"),
]
