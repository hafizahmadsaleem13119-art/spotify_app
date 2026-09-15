from .models import Song, Album
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from .froms import AlbumForm, SongForm

class HomeView(ListView):
    model = Album
    template_name = "music/home.html"
    context_object_name = "albums"
    paginate_by = 10


class SongDetailView(DetailView):
    model = Song
    template_name = "music/song_detail.html"
    context_object_name = "song"


class AlbumDetailView(DetailView):
    model = Album
    template_name = "music/album_detail.html"
    context_object_name = "album"


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


