from django.contrib import admin
from .models import Playlist, Artist, Album, Song
# Register your models here.
admin.site.register(Playlist)
admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Song)