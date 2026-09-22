from django.urls import path
from rest_framework.routers import DefaultRouter

from .api_views import SongViewSet, AlbumViewSet

router = DefaultRouter()

router.register("songs", SongViewSet)
router.register("albums", AlbumViewSet)

urlpatterns = router.urls

