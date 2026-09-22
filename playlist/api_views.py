from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Playlist
from .serializers import PlaylistSerializer

class PlaylistViewSet(ModelViewSet):
    queryset = Playlist.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = PlaylistSerializer
