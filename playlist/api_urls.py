from rest_framework.routers import DefaultRouter
from .api_views import PlaylistViewSet

router = DefaultRouter()
router.register(r'playlists', PlaylistViewSet)
urlpatterns = router.urls