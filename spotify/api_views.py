from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from playlist.models import Playlist
from .serializers import PlaylistSerializer, AlbumSerializer, SongSerializer, UserSerializer
from music.models import Song, Album
from users.models import User

class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [ IsAuthenticated]
    serializer_class = SongSerializer

class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    permission_classes = [ IsAuthenticated]
    serializer_class = AlbumSerializer

class PlaylistViewSet(ModelViewSet):
    queryset = Playlist.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = PlaylistSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
