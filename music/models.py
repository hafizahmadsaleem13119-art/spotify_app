from django.db import models
from django.contrib.auth.models import User


class Artist(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="artist",
        null=True,
        blank=True
    )

    name = models.CharField(max_length=20)
    bio = models.TextField(max_length=100)
    image = models.ImageField(upload_to="artists/", blank=True, null=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.TextField(max_length=100)
    image = models.ImageField(upload_to="albums/", blank=True, null=True)
    relesed_date = models.DateField()
    artist = models.ForeignKey(
        Artist,
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

class Playlist(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="playlists"
    )
    songs = models.ManyToManyField(
        Song,
        blank=True
    )
    def __str__(self):
        return self.name


class Profile(models.Model):
    ROLE_CHOICES = (
        ("user", "Normal User"),
        ("artist", "Artist"),
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default="user"
    )

    def __str__(self):
        return self.user.username


