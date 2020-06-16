from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register("tenants", views.TenantViewSet)
router.register("tenant-groups", views.TenantGroupViewSet)

urlpatterns = router.urls
