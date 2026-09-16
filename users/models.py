from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    bio = models.TextField(max_length=100)
    image = models.ImageField(upload_to="artists/", blank=True, null=True)

    ROLE_CHOICES = (
        ("user", "Normal User"),
        ("artist", "Artist"),
    )

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default="user"
    )

    def __str__(self):
        return self.username
