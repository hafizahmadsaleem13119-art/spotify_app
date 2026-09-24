from rest_framework import serializers
from music.models import Song, Album
from playlist.models import Playlist
from users.models import User

class SongSerializer(serializers.ModelSerializer):

    albums = serializers.PrimaryKeyRelatedField(
        queryset=Album.objects.all()
    )

    class Meta:
        model = Song
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        request = self.context.get("request")

        if request and request.user.is_authenticated:
            self.fields["albums"].queryset = Album.objects.filter(
                artist=request.user
            )

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = "__all__"


class PlaylistSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Playlist
        fields = "__all__"
        read_only_fields = ["user"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"