from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register("platforms", views.PlatformViewSet)
router.register("platform-groups", views.PlatformGroupViewSet)

urlpatterns = router.urls
