from .models import Song, Album
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from .froms import AlbumForm, SongForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from mutagen import File

class HomeView(ListView):
    model = Album
    template_name = "music/home.html"
    context_object_name = "albums"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["songs"] = Song.objects.all()[:10]
        return context

class SongDetailView(DetailView):
    model = Song
    template_name = "music/song_detail.html"
    context_object_name = "song"


class AlbumDetailView(DetailView):
    model = Album
    template_name = "music/album_detail.html"
    context_object_name = "album"


class AlbumCreateView(LoginRequiredMixin, CreateView):
    model = Album
    form_class = AlbumForm
    template_name = "music/add_album.html"
    success_url = reverse_lazy("home")
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role != "artist":
            raise Http404("You are not an artist")
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        form.instance.artist = self.request.user
        return super().form_valid(form)    


class SongCreateView(LoginRequiredMixin, CreateView):
    model = Song
    form_class = SongForm
    template_name = "music/add_song.html"
    success_url = reverse_lazy("home")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role != "artist":
            raise Http404("You are not an artist")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):

        form.instance.albums.artist = self.request.user


        audio_file = form.cleaned_data.get("audio")

        if audio_file:
            audio = File(audio_file)

            if audio and audio.info:
                seconds = int(audio.info.length)

                minutes = seconds // 60
                remaining_seconds = seconds % 60

                form.instance.duration = (
                    f"{minutes}:{remaining_seconds:02d}"
                )

        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

class AlbumUpdateView(LoginRequiredMixin, UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = "music/edit_album.html"
    success_url = reverse_lazy("home")

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)

        album = self.get_object()

        if request.user.role != "artist":
            raise Http404("You are not an artist")

        if album.artist != request.user:
            raise Http404("You cannot edit this album")

        return super().dispatch(request, *args, **kwargs)


class SongUpdateView(LoginRequiredMixin, UpdateView):
    model = Song
    form_class = SongForm
    template_name = "music/edit_song.html"
    success_url = reverse_lazy("home")

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)

        song = self.get_object()

        if request.user.role != "artist":
            raise Http404("You are not an artist")

        if song.albums.artist != request.user:
            raise Http404("You cannot edit this song")

        return super().dispatch(request, *args, **kwargs)


class AlbumDeleteView(LoginRequiredMixin, DeleteView):
    model = Album
    template_name = "music/delete_album.html"
    success_url = reverse_lazy("home")

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)

        album = self.get_object()

        if request.user.role != "artist":
            raise Http404("You are not an artist")

        if album.artist != request.user:
            raise Http404("You cannot delete this album")

        return super().dispatch(request, *args, **kwargs)


class SongDeleteView(LoginRequiredMixin, DeleteView):
    model = Song
    template_name = "music/delete_song.html"
    success_url = reverse_lazy("home")

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)

        song = self.get_object()

        if request.user.role != "artist":
            raise Http404("You are not an artist")

        if song.albums.artist != request.user:
            raise Http404("You cannot delete this song")

        return super().dispatch(request, *args, **kwargs)