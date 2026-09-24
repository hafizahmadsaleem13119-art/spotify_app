from django import forms
from .models import Album, Song


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
        fields = ["name", "description", "audio", "albums"]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

        if user and user.is_authenticated:
            self.fields["albums"].queryset = Album.objects.filter(
                artist=user
            )
        else:
            self.fields["albums"].queryset = Album.objects.none()


