from rest_framework.viewsets import ModelViewSet
from playlist.models import Playlist
from .serializers import PlaylistSerializer, AlbumSerializer, SongSerializer, UserSerializer
from music.models import Song, Album
from users.models import User
from .permissions import IsArtistOrReadOnly, IsAuthenticatedReadOnly


class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [IsArtistOrReadOnly]

class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [IsArtistOrReadOnly]
   
class PlaylistViewSet(ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedReadOnly]
