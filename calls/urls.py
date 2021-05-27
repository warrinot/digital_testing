from rest_framework.routers import DefaultRouter
from calls.api_views import CallApiViewSet


router = DefaultRouter()
router.register('calls', CallApiViewSet)


urlpatterns = router.urls
