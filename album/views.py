from album.models import Album
from rest_framework import viewsets
from album.serializers import AlbumSerializer

class Album(viewsets.ReadOnlyModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
