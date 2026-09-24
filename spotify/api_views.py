from rest_framework.viewsets import ModelViewSet
from playlist.models import Playlist
from .serializers import PlaylistSerializer, AlbumSerializer, SongSerializer, UserSerializer
from music.models import Song, Album
from users.models import User
from .permissions import IsArtistOrReadOnly,IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser


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
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Playlist.objects.filter(
            user=self.request.user
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
