from django.db import models
from users.models import User

class Album(models.Model):
    name = models.TextField(max_length=100)
    image = models.ImageField(upload_to="albums/", blank=True, null=True)
    relesed_date = models.DateField()
    artist = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="albums"
    )

    def __str__(self):
        return self.name

class Song(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    audio = models.FileField(upload_to="songs/")
    duration = models.DurationField()
    albums = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        related_name="song"
    )

    def __str__(self):
        return self.name


