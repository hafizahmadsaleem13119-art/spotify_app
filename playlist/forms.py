from django import forms
from .models import Playlist
from music.models import Album, Song

class PlaylistForm(forms.ModelForm):

    class Meta:
        model = Playlist
        fields = [
            "name",
        ]