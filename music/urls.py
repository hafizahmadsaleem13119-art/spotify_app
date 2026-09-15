from django.urls import path
from .views import (
HomeView,
AlbumCreateView,
AlbumDetailView,
SongCreateView,
SongDetailView
)
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("add-album/", AlbumCreateView.as_view(), name="add_album"),
    path("album/<int:pk>/", AlbumDetailView.as_view(), name="album_detail"),
    path("add-song/", SongCreateView.as_view(), name="add_song"),
    path("song/<int:pk>/", SongDetailView.as_view(), name="song_detail"),
]