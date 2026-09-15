from django import forms
from .models import Album, Song, Playlist


class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album

        fields = [
            "name",
            "image",
            "relesed_date",
        ]

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = [
            "name",
            "description",
            "audio",
            "duration",
            "albums",
        ]

class PlaylistForm(forms.ModelForm):

    class Meta:
        model = Playlist
        fields = [
            "name",
        ]
