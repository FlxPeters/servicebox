from rest_framework import routers

from . import views


class PlatformRootView(routers.APIRootView):
    """
    Platforms API root view
    """

    def get_view_name(self):
        return "Platforms"


router = routers.DefaultRouter()
router.register("platforms", views.PlatformViewSet)
router.register("platform-groups", views.PlatformGroupViewSet)

app_name = "platforms-api"

urlpatterns = router.urls
