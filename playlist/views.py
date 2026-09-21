from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy
from .models import Song, Playlist
from django.shortcuts import redirect, render
from django.views import View
from .forms import PlaylistForm
from django.contrib.auth.mixins import LoginRequiredMixin

class PlaylistCreateView(LoginRequiredMixin, CreateView):
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
