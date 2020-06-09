from django.urls import path

from platforms.views import PlatformListView

urlpatterns = [
    path("", PlatformListView.as_view(), name="platforms.views.list"),
]
