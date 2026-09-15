from django.urls import path
from .views import (
HomeView,
UserLoginView, 
UserLogoutView, 
SignupView, 
SongDetailView,
BecomeArtistView,
ProfileView,
AlbumCreateView,
AlbumDetailView,
SongCreateView,
PlaylistCreateView,
SelectPlaylistView,
AddSongToPlaylistView,
PlaylistDetailView
)
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("signup/",SignupView.as_view(),name="signup"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("song/<int:pk>/", SongDetailView.as_view(), name="song_detail"),
    path("become-artist/", BecomeArtistView.as_view(), name="become_artist"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("add-album/", AlbumCreateView.as_view(), name="add_album"),
    path("album/<int:pk>/", AlbumDetailView.as_view(), name="album_detail"),
    path("add-song/", SongCreateView.as_view(), name="add_song"),
    path("create-palylist/", PlaylistCreateView.as_view(), name="create_playlist"),
    path("add-to-playlist/<int:pk>/",SelectPlaylistView.as_view(),name="add_to_playlist"),
    path("add-song-to-playlist/<int:playlist_pk>/<int:song_pk>/",AddSongToPlaylistView.as_view(),name="add_song_to_playlist"),
    path("playlist/<int:pk>/",PlaylistDetailView.as_view(),name="playlist_detail"),
]