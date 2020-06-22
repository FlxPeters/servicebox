from rest_framework import routers

from . import views


class TenancyRootView(routers.APIRootView):
    """
    Tenancy API root view
    """

    def get_view_name(self):
        return "Tenancy"


router = routers.DefaultRouter()
router.APIRootView = TenancyRootView

router.register("tenants", views.TenantViewSet)
router.register("tenant-groups", views.TenantGroupViewSet)

app_name = "tenancy-api"
urlpatterns = router.urls
