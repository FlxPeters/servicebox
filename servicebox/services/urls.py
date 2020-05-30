from django.urls import path


from services.views import ServiceListView

urlpatterns = [
    path('', ServiceListView.as_view(), name='service-list'),
]
