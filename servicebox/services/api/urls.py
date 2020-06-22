from rest_framework import routers

from . import views


class ServicesRootView(routers.APIRootView):
    """
    Services API root view
    """

    def get_view_name(self):
        return "Services"


router = routers.DefaultRouter()
router.register("services", views.ServiceViewSet)

app_name = "services-api"
urlpatterns = router.urls
