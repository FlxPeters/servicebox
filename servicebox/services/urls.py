from django.urls import path


from services.views import ServiceListView, ServiceDetailView

urlpatterns = [
    path("", ServiceListView.as_view(), name="services.views.list"),
    path("<int:pk>/", ServiceDetailView.as_view(), name="services.views.details"),
]
