from django.urls import path
from .views import (
HomeView,
AlbumCreateView,
AlbumDetailView,
SongCreateView,
SongDetailView,
AlbumUpdateView,
SongUpdateView,
AlbumDeleteView,
SongDeleteView
)
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("add-album/", AlbumCreateView.as_view(), name="add_album"),
    path("album/<int:pk>/", AlbumDetailView.as_view(), name="album_detail"),
    path("add-song/", SongCreateView.as_view(), name="add_song"),
    path("song/<int:pk>/", SongDetailView.as_view(), name="song_detail"),
    path("album/<int:pk>/edit/", AlbumUpdateView.as_view(), name="album_edit"),
    path("album/<int:pk>/delete/", AlbumDeleteView.as_view(), name="album_delete"),
    path("song/<int:pk>/edit/", SongUpdateView.as_view(), name="song_edit"),
    path("song/<int:pk>/delete/", SongDeleteView.as_view(), name="song_delete")
]