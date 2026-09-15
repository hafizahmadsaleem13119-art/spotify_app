from django.db import models
from django.conf import settings
from music.models import Song

class Playlist(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="playlists"
    )
    songs = models.ManyToManyField(
        Song,
        blank=True
    )
    def __str__(self):
        return self.name
