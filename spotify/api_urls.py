from rest_framework.routers import DefaultRouter
from .api_views import PlaylistViewSet, AlbumViewSet, SongViewSet, UserViewSet


router = DefaultRouter()
router.register(r'playlists', PlaylistViewSet)
router.register("songs", SongViewSet)
router.register("albums", AlbumViewSet)
router.register(r'users', UserViewSet)  

urlpatterns = router.urls