from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

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
