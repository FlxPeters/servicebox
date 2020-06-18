from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register("services", views.ServiceViewSet)

urlpatterns = router.urls
