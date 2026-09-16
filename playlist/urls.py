from django.urls import path
from .views import (
PlaylistCreateView,
SelectPlaylistView,
AddSongToPlaylistView,
PlaylistDetailView
)
urlpatterns = [
    path("create-palylist/", PlaylistCreateView.as_view(), name="create_playlist"),
    path("add-to-playlist/<int:pk>/",SelectPlaylistView.as_view(),name="add_to_playlist"),
    path("add-song-to-playlist/<int:playlist_pk>/<int:song_pk>/",AddSongToPlaylistView.as_view(),name="add_song_to_playlist"),
    path("playlist/<int:pk>/",PlaylistDetailView.as_view(),name="playlist_detail"),
]