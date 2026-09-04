from .models import Song, Playlist, Album, Artist, Profile 
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import redirect, render
from .froms import AlbumForm, SongForm, PlaylistForm

class HomeView(ListView):
    model = Album
    template_name = "music/home.html"
    context_object_name = "albums"


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = "music/signup.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(
            user=self.object
        )

        return response


class UserLoginView(LoginView):
    template_name = "music/login.html"


class UserLogoutView(LogoutView):
    next_page = "/"


class SongDetailView(DetailView):
    model = Song
    template_name = "music/song_detail.html"
    context_object_name = "song"


class AlbumDetailView(DetailView):
    model = Album
    template_name = "music/album_detail.html"
    context_object_name = "album"


class BecomeArtistView(View):

    def post(self, request):
        profile = request.user.profile
        profile.role = "artist"
        profile.save()

        Artist.objects.create(
            user=request.user,
            name=request.user.username,
            bio=""
        )

        return redirect("profile")

class ProfileView(View):

    def get(self, request):
        profile = request.user.profile
        playlists = Playlist.objects.filter(
            user=request.user
        )

        return render(
            request,
            "music/profile.html",
            {
                "profile": profile,
                "playlists":playlists
            }
        )      


class AlbumCreateView(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = "music/add_album.html"
    success_url = reverse_lazy("home")
    def form_valid(self, form):
        form.instance.artist = self.request.user.artist
        return super().form_valid(form)    


class SongCreateView(CreateView):
    model = Song
    form_class = SongForm
    template_name = "music/add_song.html"
    success_url = reverse_lazy("home")


class PlaylistCreateView(CreateView):
    model = Playlist
    form_class = PlaylistForm
    template_name = "music/create_playlist.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class SelectPlaylistView(View):
    def get(self, request, pk):
        song = Song.objects.get(pk=pk)
        playlists = Playlist.objects.filter(
            user=request.user
        )

        return render(
            request,
            "music/add_to_playlist.html",
            {
                "song": song,
                "playlists": playlists
            }
        )


class AddSongToPlaylistView(View):
    def get(self, request, playlist_pk, song_pk):

        playlist = Playlist.objects.get(
            pk=playlist_pk,
            user=request.user
        )

        song = Song.objects.get(pk=song_pk)

        playlist.songs.add(song)

        return redirect("song_detail", pk=song.pk)


class PlaylistDetailView(DetailView):
    model = Playlist
    template_name = "music/playlist_detail.html"
    context_object_name = "playlist"    