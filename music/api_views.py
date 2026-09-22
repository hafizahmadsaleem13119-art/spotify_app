from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Song, Album
from .serializers import AlbumSerializer, SongSerializer
from .permissions import IsArtistOrReadOnly


class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [ IsArtistOrReadOnly]
    serializer_class = SongSerializer

class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    permission_classes = [ IsArtistOrReadOnly]
    serializer_class = AlbumSerializer